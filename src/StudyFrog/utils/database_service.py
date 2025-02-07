"""
Author: lodego
Date: 2025-02-05
"""

import aiosqlite

from typing import *

from utils.logger import Logger


__all__: List[str] = ["DatabaseService"]


class DatabaseService:
    """
    A class used to interact with a SQLite database.

    Attributes:
        logger (Logger): The logger instance associated with the object.
    """

    logger: Logger = Logger.get_logger(name="DatabaseService")

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

            # Connect to the database
            async with aiosqlite.connect(database=database) as db:
                # Execute the SQL query
                async with db.execute(
                    sql,
                    parameters,
                ) as cursor:

                    # Return the ID of the last row inserted
                    result: int = cursor.lastrowid

                    # Commit the transaction
                    await db.commit()

                    # Return the ID of the last row inserted
                    return result
        except Exception as e:
            # Log an error message indicating an exception occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_database' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occurred
            return None

    @classmethod
    async def delete(
        cls,
        database: str,
        sql: str,
        parameters: Optional[Tuple[..., Any]] = [],
    ) -> Optional[int]:
        """
        Deletes a row from the database using a given SQL query.

        Args:
            database (str): The path to the database file.
            parameters (Tuple[..., Any]): The parameters to pass to the SQL query.
            sql (str): The SQL query to execute.

        Returns:
            bool: True if at least one row was deleted, False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the SQL query starts with 'DELETE'
            if not sql.strip().upper().startswith("DELETE"):
                # Raise an error if it doesn't
                raise ValueError("SQL query must start with 'DELETE'.")

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
                    return True if rowcount > 0 else False
        except Exception as e:
            # Log an error message indicating an exception occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{cls.__name__}': {e}"
            )

            # Return False indicating an exception occurred
            return False

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
            # Connect to the database
            async with aiosqlite.connect(database=database) as db:
                # Execute the SQL query
                async with db.execute(
                    sql,
                    parameters,
                ) as cursor:
                    # Fetch all rows
                    result: Optional[Any] = await cursor.fetchall()

                    # Commit the transaction
                    await db.commit()

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
    async def read_all(
        cls,
        database: str,
        sql: str,
        parameters: Optional[Tuple[..., Any]] = [],
    ) -> List[Dict[str, Any]]:
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

                    # Return the rows read from the database as a list of dictionaries
                    return [dict(row) for row in rows]
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

                    # Return the row
                    return dict(row) if row else {}
        except Exception as e:
            # Log an error message indicating an exception occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'read_one' method from '{cls.__name__}': {e}"
            )

            # Return an empty dictionary indicating an exception occurred
            return {}

    @classmethod
    async def update(
        cls,
        database: str,
        sql: str,
        parameters: Optional[Tuple[..., Any]] = [],
    ) -> bool:
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

            # Connect to the database
            async with aiosqlite.connect(database=database) as db:
                # Execute the SQL query
                async with db.execute(
                    sql,
                    parameters,
                ) as cursor:
                    # Fetch the number of rows updated
                    rowcount: int = cursor.rowcount

                    # Log a message indicating the number of rows updated
                    cls.logger.info(
                        message=f"Updated {rowcount} row(s) in the database."
                    )

                    # Commit the transaction
                    await db.commit()

                    # Return True if at least one row was updated, False otherwise
                    return True if rowcount > 0 else False
        except Exception as e:
            # Log an error message indicating an exception occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{cls.__name__}': {e}"
            )

            # Return False indicating an exception occurred
            return False
