"""
Autor: lodego
Date: 2025-04-22
"""

import aiosqlite
import asyncio
import traceback

from typing import *

from utils.constants import Constants
from utils.object import ImmutableBaseObject

__all__: Final[List[str]] = ["DatabaseService"]


class DatabaseService(ImmutableBaseObject):
    """
    A singleton class that provides methods for database operations.

    Attributes:
        _shared_instance (Optional["DatabaseService"]): The shared instance of the DatabaseService class.
        logger (Logger): The logger instance.
    """

    _shared_instance: Optional["DatabaseService"] = None

    def __new__(cls) -> "DatabaseService":
        """
        Creates and returns a new instance of the DatabaseService class.

        If the instance does not exist, creates a new one by calling the parent class constructor.
        If the instance already exists, returns the existing instance.

        Returns:
            DatabaseService: The created or existing instance of DatabaseService class.
        """

        # If the shared instance is not initialized, create a new instance
        if cls._shared_instance is None:
            cls._shared_instance = super().__new__(cls)

        # Return the shared instance
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes the DatabaseService instance.

        This method is called when the shared instance of the DatabaseService is created,
        and it initializes the instance by calling the parent class constructor.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    async def create(
        self,
        sql: str,
        database: str = Constants.DATABASE_PATH,
        parameters: Tuple[Any, ...] = (),
    ) -> Union[bool, int]:
        """
        Creates a new entry in the database based on the provided SQL query.

        Args:
            sql (str): The SQL query to execute.
            database (str, optional): The path to the SQLite database file. Defaults to Constants.DATABASE_PATH.
            parameters (Tuple[Any, ...], optional): The parameters for the SQL query. Defaults to ().

        Returns:
            Union[bool, int]: The last row ID if the query was successful, or False otherwise.

        Raises:
            Exception: If an exception occurs during the execution of the query.
        """

        # Initialize the result Union[bool, int] as False
        result: Union[bool, int] = False

        try:
            async with aiosqlite.connect(database=database) as connection:
                async with connection.cursor() as cursor:
                    # Execute the the passed SQL query with the parameters
                    await cursor.execute(
                        sql=sql,
                        parameters=parameters,
                    )

                    # Commit the transaction
                    await connection.commit()

                    # Update the result Union[bool, int] with the last row ID
                    result = cursor.lastrowid
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e
        finally:
            # Return the result Union[bool, int] to the caller
            return result

    async def delete(
        self,
        sql: str,
        database: str = Constants.DATABASE_PATH,
        parameters: Tuple[Any, ...] = (),
    ) -> Union[bool, int]:
        """
        Deletes records from the database based on the provided SQL query.

        Args:
            sql (str): The SQL query to execute.
            database (str, optional): The path to the SQLite database file. Defaults to Constants.DATABASE_PATH.
            parameters (Tuple[Any, ...], optional): The parameters for the SQL query. Defaults to ().

        Returns:
            Union[bool, int]: The number of rows affected if the query was successful, or False otherwise.

        Raises:
            Exception: If an exception occurs during the execution of the query.
        """

        # Initialize the result Union[bool, int] as False
        result: Union[bool, int] = False

        try:
            async with aiosqlite.connect(database=database) as connection:
                async with connection.cursor() as cursor:
                    # Execute the the passed SQL query with the parameters
                    await cursor.execute(
                        sql=sql,
                        parameters=parameters,
                    )

                    # Commit the transaction
                    await connection.commit()

                    # Update the result Union[bool, int] with the number of rows affected
                    result = cursor.rowcount

                    # Log an info message
                    self.logger.info(
                        message=f"Successfully deleted {result} row(s) from database."
                    )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e
        finally:
            # Return the result Union[bool, int] to the caller
            return result

    async def execute(
        self,
        sql: str,
        database: str = Constants.DATABASE_PATH,
        parameters: Tuple[Any, ...] = (),
    ) -> Union[bool, Union[int, Dict[str, Any], List[Dict[str, Any]]]]:
        """
        Executes a SQL query and returns the result.

        Args:
            sql (str): The SQL query to execute.
            database (str, optional): The path to the SQLite database file. Defaults to Constants.DATABASE_PATH.
            parameters (Tuple[Any, ...], optional): The parameters for the SQL query. Defaults to ().

        Returns:
            Union[bool, Union[int, Dict[str, Any], List[Dict[str, Any]]]]: The result of the query execution.

        Raises:
            Exception: If an exception occurs during the execution of the query.
        """

        # Initialize the result Union[bool, Union[int, Dict[str, Any], List[Dict[str, Any]]]] as False
        result: Union[bool, Union[int, Dict[str, Any], List[Dict[str, Any]]]] = False

        try:
            async with aiosqlite.connect(database=database) as connection:

                # Set the row factory to aiosqlite.Row
                connection.row_factory = aiosqlite.Row

                async with connection.cursor() as cursor:
                    # Execute the the passed SQL query with the parameters
                    await cursor.execute(
                        sql=sql,
                        parameters=parameters,
                    )

                    # Check, if the SQL query is a SELECT query
                    if sql.startswith("SELECT "):
                        # Fetch all the rows
                        rows: List[aiosqlite.Row] = await cursor.fetchall()

                        # Check, if rows are not empty
                        if not rows:
                            # Return an empty list
                            result = []
                        elif len(rows) == 1:
                            # Return the first row
                            result = dict(rows[0])
                        else:
                            # Return the list of rows
                            result = [dict(row) for row in rows]

                    # Check, if the SQL query is an INSERT query
                    elif sql.startswith("INSERT "):
                        # Commit the transaction
                        await connection.commit()

                        # Return the last row ID
                        result = cursor.lastrowid

                    elif sql.startswith("PRAGMA "):
                        # Fetch all the rows
                        rows: List[aiosqlite.Row] = await cursor.fetchall()

                        # Check, if rows are not empty
                        if not rows:
                            # Return an empty list
                            result = []
                        elif len(rows) == 1:
                            # Return the first row
                            result = dict(rows[0])
                        else:
                            # Return the list of rows
                            result = [dict(row) for row in rows]

                    # Check, if the SQL query is an UPDATE or DELETE query
                    elif sql.startswith("UPDATE ") or sql.startswith("DELETE "):
                        # Commit the transaction
                        await connection.commit()

                        # Return the number of rows affected
                        result = cursor.rowcount
                    else:
                        # Commit the transaction
                        await connection.commit()

                        # Return True
                        result = True
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'execute' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e
        finally:
            # Return the result Union[bool, Union[Dict[str, Any], List[Dict[str, Any]]]] to the caller
            return result

    async def read_all(
        self,
        sql: str,
        database: str = Constants.DATABASE_PATH,
        parameters: Tuple[Any, ...] = (),
    ) -> Union[bool, List[Dict[str, Any]]]:
        """
        Executes a SQL query to retrieve all rows from a database.

        Args:
            sql (str): The SQL query to execute.
            database (str, optional): The path to the SQLite database file. Defaults to Constants.DATABASE_PATH.
            parameters (Tuple[Any, ...], optional): The parameters for the SQL query. Defaults to ().

        Returns:
            Union[bool, List[Dict[str, Any]]]: A list of rows represented as dictionaries if successful, or False otherwise.

        Raises:
            Exception: If an exception occurs during the execution of the query.
        """

        # Initialize the result Union[bool, List[Dict[str, Any]]] as False
        result: Union[bool, List[Dict[str, Any]]] = False

        try:
            async with aiosqlite.connect(database=database) as connection:

                # Set the row factory to aiosqlite.Row
                connection.row_factory = aiosqlite.Row

                async with connection.cursor() as cursor:
                    # Execute the the passed SQL query with the parameters
                    await cursor.execute(
                        sql=sql,
                        parameters=parameters,
                    )

                    # Fetch all the rows
                    rows: List[aiosqlite.Row] = await cursor.fetchall()

                    # Check, if rows are not empty
                    if rows:
                        # Convert the rows to a list of dictionaries
                        result = [dict(row) for row in rows]

                    # Log an info message
                    self.logger.info(
                        message=f"Successfully read {len(rows)} row(s) from database."
                    )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'read_all' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e
        finally:
            # Return the result Union[bool, List[Dict[str, Any]]] to the caller
            return result

    async def read_one(
        self,
        sql: str,
        database: str = Constants.DATABASE_PATH,
        parameters: Tuple[Any, ...] = (),
    ) -> Union[bool, Dict[str, Any]]:
        """
        Retrieves a single row from the database.

        Args:
            sql (str): The SQL query to execute.
            database (str, optional): The path to the SQLite database file. Defaults to Constants.DATABASE_PATH.
            parameters (Tuple[Any, ...], optional): The parameters for the SQL query. Defaults to ().

        Returns:
            Union[bool, Dict[str, Any]]: The first row of the query result, or False if no row was found.
        
        Raises:
            Exception: If an exception occurs during the execution of the query.
        """

        # Initialize the result Union[bool, Dict[str, Any]] as False
        result: Union[bool, Dict[str, Any]] = False

        try:
            async with aiosqlite.connect(database=database) as connection:

                # Set the row factory to aiosqlite.Row
                connection.row_factory = aiosqlite.Row

                async with connection.cursor() as cursor:
                    # Execute the the passed SQL query with the parameters
                    await cursor.execute(
                        sql=sql,
                        parameters=parameters,
                    )

                    # Fetch the first row
                    row: aiosqlite.Row = await cursor.fetchone()

                    # Check, if row is not empty
                    if row:
                        # Convert the row to a dictionary
                        result = dict(row)

                    # Log an info message
                    self.logger.info(
                        message=f"Successfully read {result} row(s) from database."
                    )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'read_one' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e
        finally:
            # Return the result Union[bool, Dict[str, Any]] to the caller
            return result

    async def update(
        self,
        sql: str,
        database: str = Constants.DATABASE_PATH,
        parameters: Tuple[Any, ...] = (),
    ) -> Union[bool, int]:
        """
        Updates existing records in the database.

        Args:
            sql (str): The SQL query to execute.
            database (str, optional): The path to the SQLite database file. Defaults to Constants.DATABASE_PATH.
            parameters (Tuple[Any, ...], optional): The parameters for the SQL query. Defaults to ().

        Returns:
            Union[bool, int]: The number of rows affected if the query was successful, or False otherwise.

        Raises:
            Exception: If an exception occurs during the execution of the query.
        """

        # Initialize the result Union[bool, int] as False
        result: Union[bool, int] = False

        try:
            async with aiosqlite.connect(database=database) as connection:
                async with connection.cursor() as cursor:
                    # Execute the the passed SQL query with the parameters
                    await cursor.execute(
                        sql=sql,
                        parameters=parameters,
                    )

                    # Commit the transaction
                    await connection.commit()

                    # Update the result Union[bool, int] with the number of rows affected
                    result = cursor.rowcount

                    # Log an info message
                    self.logger.info(
                        message=f"Successfully updated {result} row(s) in database."
                    )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e
        finally:
            # Return the result Union[bool, int] to the caller
            return result
