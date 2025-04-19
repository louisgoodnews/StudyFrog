"""
Author: lodego
Date: 2025-02-05
"""

import aiosqlite

from datetime import datetime, timedelta
from typing import *

from utils.logger import Logger
from utils.miscellaneous import Miscellaneous


__all__: Final[List[str]] = ["DatabaseService"]


class DatabaseService:
    """
    A class used to interact with a SQLite database.

    Attributes:
        logger (Logger): The logger instance associated with the object.
    """

    # This class' Logger instance
    logger: Final[Logger] = Logger.get_logger(name="DatabaseService")

    # This class' cache dictionary
    cache: Final[Dict[str, Dict[str, Any]]] = {}

    # This class' time limit int
    time_limit: Final[int] = 3600

    # The timestamp datetime of when the cache was last updated/flushed
    timestamp: datetime = Miscellaneous.get_current_datetime()

    @classmethod
    def add_to_cache(
        cls,
        sql: str,
        result: Any,
        parameters: Optional[Tuple[..., Any]] = [],
    ) -> None:
        """
        Adds a result to the cache with the given SQL query and parameters.

        Args:
            sql (str): The SQL query used to retrieve the result.
            result (Any): The result to cache.
            parameters (Optional[Tuple[..., Any]], optional): The parameters that were used to retrieve the result. Defaults to None.
        """

        # Check, if the cache is valid
        if cls.is_cache_valid():
            # Flush the cache
            cls.flush_cache()

        # Check, if the already exists in the cache
        if cls.is_key_in_cache(key=sql):
            # Log an info message
            cls.logger.info(
                message=f"Query '{sql}' already exists in cache. Overwriting..."
            )

        # Add the result to the cache
        cls.cache[sql] = {
            "parameters": parameters or (),
            "result": result,
        }

    @classmethod
    def check_cache(
        cls,
        sql: str,
        parameters: Optional[Tuple[Any, ...]] = None,
    ) -> Union[Any, bool]:
        """
        Checks, if the cache contains the passed SQL query and if the parameters of the cached result
        match the passed parameters.

        If the cache contains the passed SQL query and the parameters of the cached result match the
        passed parameters, the cached result is returned. Otherwise, False is returned.

        Args:
            sql (str): The SQL query to check.
            parameters (Optional[Tuple[Any, ...]], optional): The parameters to check. Defaults to None.

        Returns:
            Union[Any, bool]: The cached result if the cache contains the passed SQL query and the
            parameters of the cached result match the passed parameters, or False otherwise.
        """

        # Check, if the cache is valid
        if not cls.is_cache_valid():
            # Flush the cache
            cls.flush_cache()

            # Return False early
            return False

        # Check, if the passed sql is contained in the cache
        if not cls.is_key_in_cache(key=sql):
            # Return False early
            return False

        # Check, if the cache entry associated to the passed sql has the same parameters
        if cls.cache[sql]["parameters"] != parameters:
            # Return False early
            return False

        # Return the result associated with the passed sql
        return cls.cache[sql]["result"]

    @classmethod
    def check_timestamp(cls) -> bool:
        """
        Checks if the cache needs to be cleared.

        Returns True if the cache needs to be cleared, False otherwise.
        """

        # Return True if the cache needs to be cleared, False otherwise
        return datetime.now() - cls.timestamp >= timedelta(seconds=cls.time_limit)

    @classmethod
    def clear_cache(cls) -> None:
        """
        Clears the cache if it is not empty and updates the timestamp.

        This method checks if the cache is empty. If not, it clears all cached
        entries and updates the timestamp to the current datetime.
        """

        # Check, if the cache is empty
        if cls.cache.empty():
            # Return early
            return

        # Clear the cache
        cls.cache.clear()

        # Update the timestamp
        cls.timestamp = Miscellaneous.get_current_datetime()

    @classmethod
    async def create(
        cls,
        database: str,
        sql: str,
        parameters: Optional[Tuple[..., Any]] = [],
    ) -> Optional[int]:
        """
        Creates an entry in the database using a given SQL query.

        Args:
            database (str): The path to the database file.
            parameters (Tuple[..., Any]): The parameters to pass to the SQL query.
            sql (str): The SQL query to execute.

        Returns:
            Optional[int]: The ID of the last row inserted, or None if an exception occurred.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the SQL query starts with 'INSERT'
            if not sql.strip().upper().startswith("INSERT"):
                # Raise an error if it doesn't
                raise ValueError("SQL query must start with 'INSERT'.")

            # Initialize the result (optional) int as None
            result: Optional[int] = None

            # Connect to the database
            async with aiosqlite.connect(database=database) as db:
                # Execute the SQL query
                async with db.execute(
                    sql,
                    parameters,
                ) as cursor:
                    # Fetch the ID of the last row inserted
                    result = cursor.lastrowid

                    # Commit the transaction
                    await db.commit()

            # Add the parameters, result and SQL query to the cache
            cls.add_to_cache(
                parameters=parameters,
                result=result,
                sql=sql,
            )

            # Return the ID of the last row inserted
            return result
        except Exception as e:
            # Log an error message indicating an exception occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occurred
            return None

    @classmethod
    async def delete(
        cls,
        database: str,
        sql: str,
        parameters: Optional[Tuple[..., Any]] = [],
    ) -> Optional[Dict[str, Any]]:
        """
        Deletes a row from the database using a given SQL query.

        Args:
            database (str): The path to the database file.
            parameters (Tuple[..., Any]): The parameters to pass to the SQL query.
            sql (str): The SQL query to execute.

        Returns:
            Dict[str, Any]: A dictionary containing the result of the SQL query.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the SQL query starts with 'DELETE'
            if not sql.strip().upper().startswith("DELETE"):
                # Raise an error if it doesn't
                raise ValueError("SQL query must start with 'DELETE'.")

            # Initialize the result (optional) bool as None
            result: Optinoal[Dict[str, Any]] = None

            # Connect to the database
            async with aiosqlite.connect(database=database) as db:
                # Execute the SQL query
                async with db.execute(
                    sql,
                    parameters,
                ) as cursor:
                    # Fetch the number of rows deleted
                    rowcount: int = cursor.rowcount

                    # Log a message indicating the number of rows deleted
                    cls.logger.info(
                        message=f"Deleted {rowcount} row(s) in the database."
                    )

                    # Commit the transaction
                    await db.commit()

                    # Return True if at least one row was deleted, False otherwise
                    result = {
                        "result": True if rowcount > 0 else False,
                        "rowcount": rowcount,
                    }

            # Add the parameters, result and SQL query to the cache
            cls.add_to_cache(
                parameters=parameters,
                result=result,
                sql=sql,
            )

            # Return the result
            return result
        except Exception as e:
            # Log an error message indicating an exception occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occurred
            return None

    @classmethod
    async def execute(
        cls,
        database: str,
        sql: str,
        parameters: Optional[Tuple[..., Any]] = [],
    ) -> Optional[Any]:
        """
        Executes a SQL query and returns the result.

        Args:
            database (str): The path to the database file.
            parameters (Tuple[..., Any]): The parameters to pass to the SQL query.
            sql (str): The SQL query to execute.

        Returns:
            Optional[Any]: The result of the SQL query or None if an exception occurred.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check the cache:
            cache_check: Union[Any, bool] = cls.check_cache(
                parameters=parameters,
                sql=sql,
            )

            # Check, if the cache check is not a boolean (i.e. False)
            if not isinstance(
                cache_check,
                bool,
            ):
                # Return the check result early
                return cache_check["result"]

            # Initialize the (optional) result as None
            result: Optional[Any] = None

            # Connect to the database
            async with aiosqlite.connect(database=database) as db:
                # Execute the SQL query
                async with db.execute(
                    sql,
                    parameters,
                ) as cursor:
                    # Fetch all rows
                    result = await cursor.fetchall()

                    # Commit the transaction
                    await db.commit()

            # Add the parameters, result and SQL query to the cache
            cls.add_to_cache(
                parameters=parameters,
                result=result,
                sql=sql,
            )

            # Return the result
            return result
        except Exception as e:
            # Log an error message indicating an exception occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'execute' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occurred
            return None

    @classmethod
    def flush_cache(cls) -> None:
        """
        Flushes the cache.

        Checks if the cache is empty. If it is, the timestamp is updated and the method returns early. Otherwise, the cache is cleared.

        :return: None
        :rtype: None
        """

        # Check, if the cache is empty
        if cls.is_cache_empty():
            # Update the timestamp
            cls.timestamp = Miscellaneous.get_current_datetime()

            # Return early
            return

        # Clear the cache
        cls.clear_cache()

    @classmethod
    def get_cache_keys(cls) -> List[str]:
        """
        Returns the keys of the cache.

        The method returns a list of all keys in the cache.

        :return: A list of keys in the cache.
        :rtype: List[str]
        """

        return list(cls.cache.keys())

    @classmethod
    def get_cache_values(cls) -> List[Any]:
        """
        Returns the values of the cache.

        The method returns a list of all values in the cache.

        :return: A list of values in the cache.
        :rtype: List[Any]
        """

        return list(cls.cache.values())

    @classmethod
    def get_from_cache(
        cls,
        key: str,
    ) -> Optional[Any]:
        """
        Retrieves a value from the cache by its key.

        If the key is not found in the cache, the method returns None.

        Args:
            key (str): The key of the value to retrieve.

        Returns:
            Optional[Any]: The value associated with the passed key if the key is found, otherwise None.
        """

        # Check, if the passed sql exists in the cache
        if not cls.is_key_in_cache(key=key):
            # Return early
            return

        # Return the value associated with the passed sql
        return cls.cache[sql]

    @classmethod
    def is_cache_empty(cls) -> bool:
        """
        Checks if the cache is empty.

        The method returns True if the cache is empty, otherwise False.

        Returns:
            bool: True if the cache is empty, otherwise False.
        """

        return cls.cache.empty()

    @classmethod
    def is_cache_valid(cls) -> bool:
        """
        Checks if the cache is valid.

        The cache is considered valid if the timestamp check passes
        and the cache is not empty.

        Returns:
            bool: True if the cache is valid, False otherwise.
        """

        return cls.check_timestamp() and not cls.is_cache_empty()

    @classmethod
    def is_key_in_cache(
        cls,
        key: str,
    ) -> bool:
        """
        Checks if a key exists in the cache.

        Args:
            key (str): The key to check.

        Returns:
            bool: True if the key exists in the cache, False otherwise.
        """

        # Return True if the pased key is contained in the cache or False if otherweise
        return key in cls.cache.keys()

    @classmethod
    async def read_all(
        cls,
        database: str,
        sql: str,
        parameters: Optional[Tuple[..., Any]] = [],
    ) -> Optional[List[Dict[str, Any]]]:
        """
        Reads all rows from the database using a given SQL query.

        Args:
            database (str): The path to the database file.
            parameters (Tuple[..., Any]): The parameters to pass to the SQL query.
            sql (str): The SQL query to execute.

        Returns:
            List[Dict[str, Any]]: The rows read from the database.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the SQL query starts with 'SELECT'
            if not sql.strip().upper().startswith("SELECT"):
                # Raise an error if it doesn't
                raise ValueError("SQL query must start with 'SELECT'.")

            # Check the cache:
            cache_check: Union[Any, bool] = cls.check_cache(
                parameters=parameters,
                sql=sql,
            )

            # Check, if the cache check is not a boolean (i.e. False)
            if not isinstance(
                cache_check,
                bool,
            ):
                # Return the check result early
                return cache_check["result"]

            # Initialize the (optional) list result as None
            result: Optional[List[Dict[str, Any]]] = None

            # Connect to the database
            async with aiosqlite.connect(database=database) as db:
                # Set the row factory
                db.row_factory = aiosqlite.Row
                # Execute the SQL query
                async with db.execute(
                    sql,
                    parameters,
                ) as cursor:
                    # Fetch the rows
                    rows: Optional[List[Dict[str, Any]]] = await cursor.fetchall()

                    # Add a list of dictionary representations of the rows to the result or an empty list
                    result = [dict(row) for row in rows] if rows else []

            # Add the parameters, result and SQL query to the cache
            cls.add_to_cache(
                parameters=parameters,
                result=result,
                sql=sql,
            )

            # Return the rows read from the database as a list of dictionaries
            return result
        except Exception as e:
            # Log an error message indicating an exception occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'read_all' method from '{cls.__name__}': {e}"
            )

            # Return an empty list indicating an exception occurred
            return []

    @classmethod
    async def read_one(
        cls,
        database: str,
        sql: str,
        parameters: Optional[Tuple[..., Any]] = [],
    ) -> Dict[str, Any]:
        """
        Reads a single row from the database using a given SQL query.

        Args:
            database (str): The path to the database file.
            parameters (Tuple[..., Any]): The parameters to pass to the SQL query.
            sql (str): The SQL query to execute.

        Returns:
            Dict[str, Any]: The row read from the database.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the SQL query starts with 'SELECT'
            if not sql.strip().upper().startswith("SELECT"):
                # Raise an error if it doesn't
                raise ValueError("SQL query must start with 'SELECT'.")

            # Check the cache:
            cache_check: Union[Any, bool] = cls.check_cache(
                parameters=parameters,
                sql=sql,
            )

            # Check, if the cache check is not a boolean (i.e. False)
            if not isinstance(
                cache_check,
                bool,
            ):
                # Return the check result early
                return cache_check["result"]

            # Initialize the (optional) dictionary result as None
            result: Optional[Dict[str, Any]] = None

            # Connect to the database
            async with aiosqlite.connect(database=database) as db:
                # Set the row factory
                db.row_factory = aiosqlite.Row
                # Execute the SQL query
                async with db.execute(
                    sql,
                    parameters,
                ) as cursor:
                    # Fetch the row
                    row: Optional[Dict[str, Any]] = await cursor.fetchone()

                    # Add a dictionary representations of the row to the result or an empty dictionary
                    result = dict(row) if row else {}

            # Add the parameters, result and SQL query to the cache
            cls.add_to_cache(
                parameters=parameters,
                result=result,
                sql=sql,
            )

            # Return the result
            return result
        except Exception as e:
            # Log an error message indicating an exception occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'read_one' method from '{cls.__name__}': {e}"
            )

            # Return an empty dictionary indicating an exception occurred
            return {}

    @classmethod
    def remove_from_cache(
        cls,
        key: str,
    ) -> None:
        """
        Removes an item from the cache by its key.

        Args:
            key (str): The key of the item to remove.

        Returns:
            None
        """

        # Check if the passed key is contained in the cache
        if not cls.is_key_in_cache(key=key):
            # Return early
            return

        # Remove the item associated with the passed key from the cache
        cls.cache.pop(key)

    @classmethod
    async def update(
        cls,
        database: str,
        sql: str,
        parameters: Optional[Tuple[..., Any]] = [],
    ) -> Optional[Dict[str, Any]]:
        """
        Updates a row in the database using a given SQL query.

        Args:
            database (str): The path to the database file.
            parameters (Tuple[..., Any]): The parameters to pass to the SQL query.
            sql (str): The SQL query to execute.

        Returns:
            bool: True if at least one row was updated, False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the SQL query starts with 'UPDATE'
            if not sql.strip().upper().startswith("UPDATE"):
                # Raise an error if it doesn't
                raise ValueError("SQL query must start with 'UPDATE'.")

            # Check the cache:
            cache_check: Union[Any, bool] = cls.check_cache(
                parameters=parameters,
                sql=sql,
            )

            # Check, if the cache check is not a boolean (i.e. False)
            if not isinstance(
                cache_check,
                bool,
            ):
                # Return the check result early
                return cache_check["result"]

            # Initialize the result (optional) int as None
            result: Optional[int] = None

            # Connect to the database
            async with aiosqlite.connect(database=database) as db:
                # Execute the SQL query
                async with db.execute(
                    sql,
                    parameters,
                ) as cursor:
                    # Fetch the number of rows deleted
                    rowcount: int = cursor.rowcount

                    # Log a message indicating the number of rows deleted
                    cls.logger.info(
                        message=f"Updated {rowcount} row(s) in the database."
                    )

                    # Commit the transaction
                    await db.commit()

                    # Return True if at least one row was deleted, False otherwise
                    result = {
                        "result": True if rowcount > 0 else False,
                        "rowcount": rowcount,
                    }

            # Add the parameters, result and SQL query to the cache
            cls.add_to_cache(
                parameters=parameters,
                result=result,
                sql=sql,
            )

            # Return the result
            return result
        except Exception as e:
            # Log an error message indicating an exception occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{cls.__name__}': {e}"
            )

            # Return False indicating an exception occurred
            return False

    @classmethod
    def update_in_cache(
        cls,
        sql: str,
        result: Any,
        parameters: Optional[Tuple[..., Any]] = [],
    ) -> None:
        """
        Updates the cache with the given SQL query, result, and parameters.

        If the SQL query already exists in the cache, it will be overwritten.

        Args:
            sql (str): The SQL query to associate with the result.
            result (Any): The result to store in the cache.
            parameters (Optional[Tuple[..., Any]], optional): The parameters used with the query.
        """

        # Add or update the result in the cache
        cls.add_to_cache(
            parameters=parameters,
            result=result,
            sql=sql,
        )
