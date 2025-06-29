"""
Author: lodego
Date: 2025-02-05
"""

import traceback

from typing import *

from utils.database_service import DatabaseService
from utils.field import Field
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous
from utils.object import ImmutableBaseObject


__all__: Final[List[str]] = [
    "ImmutableBaseModel",
]


T: TypeVar = TypeVar("T")


class ImmutableBaseModel(ImmutableBaseObject):
    """
    Represents an immutable base model for interacting with a SQLite database table.

    This class provides a base implementation for models that are stored in a SQLite database table.

    Attributes:
        logger (Logger): The logger instance associated with the object.
    """

    database_service: DatabaseService = DatabaseService()

    logger: Final[Logger] = Logger.get_logger(name="ImmutableBaseModel")

    def __init__(
        self,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the ImmutableBaseModel class.

        Args:
            **kwargs: Keyword arguments.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(**kwargs)

    @classmethod
    async def count(
        cls,
        database: str,
    ) -> int:
        """
        Counts the number of entries in the database table.

        Args:
            database (str): The path to the database.

        Returns:
            int: The number of entries in the database table or 0 if an exception occurred.
        """
        try:
            # Count the number of entries in the database table
            result: Union[bool, List[Dict[str, Any]]] = (
                await cls.database_service.execute(
                    database=database,
                    sql=f"SELECT COUNT(*) FROM {cls.table};",
                )
            )

            # Check, if the execute operation failed (i.e., if a boolean was returned)
            if isinstance(result, bool) and not result:
                # Log a warning message
                cls.logger.warning(
                    message=f"Failed to count entries in table '{cls.table}' in the database."
                )

                # Return 0 indicating an exception occurred
                return 0

            # Return the number of entries in the database table or 0
            return result["COUNT(*)"] or 0
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{cls.__name__}' class: {e}"
            )

            # Log the traceback of the exception
            cls.logger.error(
                message=f"Traceback: {traceback.format_exc()}"
            )

            # Return 0 indicating an exception occurred
            return 0

    async def create(
        self,
        database: str,
    ) -> Optional[int]:
        """
        Saves the current model instance to the database.

        Args:
            database (str): The path to the database.

        Returns:
            Optional[int]: The ID of the newly created entry, or None if an error occurred.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert object to dictionary and ensure DB-friendly format
            converted_data = Miscellaneous.convert_to_db_format(
                self.to_dict(
                    exclude=[
                        "_logger",
                        "id",
                        "table",
                    ]
                )
            )

            # Extract columns and values
            columns = ", ".join(converted_data.keys())
            placeholders = ", ".join(["?" for _ in converted_data])
            parameters = tuple(converted_data.values())  # Convert to tuple

            # Construct SQL query
            sql = f"INSERT INTO {self.table} ({columns}) VALUES ({placeholders});"

            # Execute SQL command and return the last row ID
            result: Union[bool, int] = await self.database_service.create(
                database=database,
                parameters=parameters,
                sql=sql,
            )

            # Check, if the create operation failed (i.e., if a boolean was returned)
            if isinstance(result, bool) and not result:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create entry in table '{self.table}' in the database."
                )

                # Return None indicating the operation was not successful
                return None

            # Log an info message
            self.logger.info(
                message=f"Created entry in table '{self.table}' in the database."
            )

            # Return the ID of the newly created entry
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'save' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback of the exception
            self.logger.error(
                message=f"Traceback: {traceback.format_exc()}"
            )

            # Return None indicating an exception occurred
            return None

    @classmethod
    async def create_table(
        cls,
        database: str,
    ) -> bool:
        """
        Creates the table based on the defined fields.

        Args:
            database (str): Path to the SQLite database file.

        Returns:
            bool: True if the table was created successfully, False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Build the SQL query
            sql: str = (
                f"CREATE TABLE IF NOT EXISTS {cls.table} ({", ".join([value.to_sql_string() for value in cls.__dict__.values() if isinstance(value, Field)])})"
            )

            # Execute the SQL query
            result: Union[bool, List[Dict[str, Any]]] = (
                await cls.database_service.execute(
                    database=database,
                    parameters=(),
                    sql=sql,
                )
            )

            # Check, if the create operation failed (i.e., if a boolean was returned)
            if isinstance(result, bool) and not result:
                # Log a warning message
                cls.logger.warning(
                    message=f"Failed to create table '{cls.table}' in the database."
                )

                # Return False indicating the operation was not successful
                return False

            # Log an info message
            cls.logger.info(message=f"Created table '{cls.table}' in the database.")

            # Return True indicating the operation was successful
            return True
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_table' method from '{cls.__name__}' class: {e}"
            )

            # Log the traceback of the exception
            cls.logger.error(
                message=f"Traceback: {traceback.format_exc()}"
            )

            # Return False indicating an exception occurred
            return False

    async def delete(
        self,
        database: str,
    ) -> bool:
        """
        Deletes the model instance from the database.

        Args:
            database (str): Path to the SQLite database file.

        Returns:
            bool: True if deletion was successful, False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Build the SQL query
            sql: str = f"DELETE FROM {self.table} WHERE id = ?"

            # Execute the SQL query
            result: Union[bool, int] = await self.database_service.delete(
                database=database,
                parameters=(self.id,),
                sql=sql,
            )

            # Check, if the delete operation failed (i.e., if a boolean was returned)
            if isinstance(result, bool) and not result:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to delete model instance from the database."
                )

                # Return False indicating the operation was not successful
                return False

            # Log an info message
            self.logger.info(message=f"Deleted model instance from the database.")

            # Return True indicating the operation was successful
            return True
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback of the exception
            self.logger.error(
                message=f"Traceback: {traceback.format_exc()}"
            )

            # Return False indicating the operation failed (i.e., if a boolean was returned)
            return False

    @classmethod
    async def drop_table(
        cls,
        database: str,
    ) -> bool:
        """
        Drops the table associated with the model.

        Args:
            database (str): Path to the SQLite database file.

        Returns:
            bool: True if the table was dropped successfully, False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Build the SQL query
            sql: str = f"DROP TABLE IF EXISTS {cls.table}"

            # Execute the SQL query
            result: Union[bool, List[Dict[str, Any]]] = (
                await cls.database_service.execute(
                    database=database,
                    parameters=(),
                    sql=sql,
                )
            )

            # Check, if the drop operation failed (i.e., if a boolean was returned)
            if isinstance(result, bool) and not result:
                # Log a warning message
                cls.logger.warning(
                    message=f"Failed to drop table '{cls.table}' from the database."
                )

                # Return False indicating the operation was not successful
                return False

            # Log an info message
            cls.logger.info(message=f"Dropped table '{cls.table}' from the database.")

            # Return True indicating the operation was successful
            return True
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'drop_table' method from '{cls.__name__}' class: {e}"
            )

            # Log the traceback of the exception
            cls.logger.error(
                message=f"Traceback: {traceback.format_exc()}"
            )

            # Return False indicating the operation failed (i.e., if a boolean was returned)
            return False

    @classmethod
    async def execute(
        cls,
        database: str,
        sql: str,
        parameters: Optional[Tuple[Any, ...]] = [],
    ) -> Any:
        """
        Executes a custom SQL query.

        Args:
            database (str): Path to the SQLite database file.
            parameters (Tuple[Any, ...], optional): Parameters for the query.
            sql (str): The SQL query to execute.

        Returns:
            Any: The result of the query.
        """
        try:
            # Execute the SQL query
            result: Union[bool, int] = await cls.database_service.execute(
                database=database,
                parameters=parameters,
                sql=sql,
            )

            # Check, if the execute operation failed (i.e., if a boolean was returned)
            if isinstance(result, bool) and not result:
                # Log a warning message
                cls.logger.warning(message=f"Failed to execute SQL query: {sql}")

                # Return None indicating an exception occurred
                return None

            # Log an info message
            cls.logger.info(message=f"Executed SQL query: {sql}")

            # Return the result of the query
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'execute' method from '{cls.__name__}' class: {e}"
            )

            # Log the traceback of the exception
            cls.logger.error(
                message=f"Traceback: {traceback.format_exc()}"
            )

            # Return None indicating an exception occurred
            return None

    @classmethod
    async def get_all(
        cls,
        database: str,
    ) -> List[Any]:
        """
        Retrieves all rows from the model's table.

        Args:
            database (str): Path to the SQLite database file.

        Returns:
            List[Any]: List of model instances.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Build the SQL query
            sql: str = f"SELECT * FROM {cls.table}"

            # Execute the SQL query
            result: Union[bool, List[Dict[str, Any]]] = (
                await cls.database_service.read_all(
                    database=database,
                    parameters=(),
                    sql=sql,
                )
            )

            # Check, if the read_all operation failed (i.e., if a boolean was returned)
            if isinstance(result, bool) and not result:
                # Log a warning message
                cls.logger.warning(
                    message=f"Failed to retrieve rows from table '{cls.table}' in the database."
                )

                # Return an empty list indicating an exception occurred
                return []

            # Return the model instances
            return [
                cls(**Miscellaneous.convert_from_db_format(data=row)) for row in result
            ]
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{cls.__name__}' class: {e}"
            )

            # Log the traceback of the exception
            cls.logger.error(
                message=f"Traceback: {traceback.format_exc()}"
            )

            # Return an empty list indicating an exception occurred
            return []

    @classmethod
    async def get_by(
        cls,
        database: str,
        column: str,
        value: Any,
    ) -> Optional[Union[Any, List[Any]]]:
        """
        Looks up models in the database by a column value.

        Args:
            database (str): Path to the SQLite database file.
            column (str): Column to filter by.
            value (Any): Value to match.

        Returns:
            Optional[Union[Any, List[Any]]]: The model instance if found, otherwise None.
        """
        try:
            # Build the SQL query to find entries where the specified column matches the given value
            sql: str = f"SELECT * FROM {cls.table} WHERE {column} LIKE ?"

            # Execute the SQL query and retrieve all matching rows
            result: Union[bool, List[Dict[str, Any]]] = (
                await cls.database_service.read_all(
                    database=database,
                    parameters=(value,),
                    sql=sql,
                )
            )

            # Check, if the read_all operation failed (i.e., if a boolean was returned)
            if isinstance(result, bool) and not result:
                # Log a warning message
                cls.logger.warning(
                    message=f"Failed to retrieve rows from table '{cls.table}' in the database."
                )

                # Return None indicating an exception occurred
                return None

            # Check if no rows were returned
            if len(result) == 0:
                # Return None if no entries are found
                return None

            # Check if only one row was returned
            if len(result) == 1:
                # Convert the single row to a model instance and return it
                return cls(**Miscellaneous.convert_from_db_format(data=result[0]))
            else:
                # Return a list of model instances for all matching rows
                return [
                    cls(**Miscellaneous.convert_from_db_format(data=row))
                    for row in result
                ]
        except Exception as e:
            # Log an error message indicating an exception occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{cls.__name__}' class: {e}"
            )

            # Log the traceback of the exception
            cls.logger.error(
                message=f"Traceback: {traceback.format_exc()}"
            )

            # Return None indicating an exception occurred
            return None

    @classmethod
    async def search(
        cls,
        database: str,
        **kwargs,
    ) -> Optional[List[Any]]:
        """
        Searches for entries in the database using the provided keyword arguments.

        Args:
            database (str): Path to the SQLite database file.
            **kwargs: The keyword arguments to use as search conditions.

        Returns:
            Optional[List[Any]]: A list of model instances if multiple entries were found, or None if no entries were found in the database.
        """
        try:
            # Initialize the conditions list as an empty list
            conditions: List[str] = []

            # Initialize the parameters list as an empty list
            parameters: List[Any] = []

            # Iterate over the keyword arguments
            for (
                key,
                value,
            ) in kwargs.items():
                # Get the field object
                field: Field = getattr(
                    cls,
                    key,
                )

                # Check the type of the field
                if field["type"] == "INTEGER":
                    # Add a condition to the SQL query to filter by the INTEGER field
                    conditions.append(f"{key} = ?")

                    # Add the value to the parameters list
                    parameters.append(value)

                elif field["type"] == "TEXT":
                    # Add a condition to the SQL query to filter by the TEXT field
                    conditions.append(f"{key} LIKE ?")

                    # Add the value to the parameters list
                    parameters.append(value)

                elif field["type"] == "VARCHAR":
                    # Add a condition to the SQL query to filter by the VARCHAR field
                    conditions.append(f"{key} LIKE ?")

                    # Add the value to the parameters list
                    parameters.append(value)

                elif field["type"] == "REAL":
                    # Add a condition to the SQL query to filter by the REAL field
                    conditions.append(f"{key} = ?")

                    # Add the value to the parameters list
                    parameters.append(value)

                elif field["type"] == "FLOAT":
                    # Add a condition to the SQL query to filter by the FLOAT field
                    conditions.append(f"{key} = ?")

                    # Add the value to the parameters list
                    parameters.append(value)

                elif field["type"] == "INTEGER":
                    # Add a condition to the SQL query to filter by the INTEGER field
                    conditions.append(f"{key} = ?")
                    # Add the value to the parameters list
                    parameters.append(value)

                elif field["type"] == "NUMERIC":
                    # Add a condition to the SQL query to filter by the NUMERIC field
                    conditions.append(f"{key} = ?")

                    # Add the value to the parameters list
                    parameters.append(value)

                elif field["type"] == "NULL":
                    # Add a condition to the SQL query to filter by the NULL field
                    conditions.append(f"{key} IS NULL")

                elif field["type"] == "DATE":
                    # Add a condition to the SQL query to filter by the DATE field
                    conditions.append(f"{key} = ?")

                    # Add the value to the parameters list
                    parameters.append(value)

                elif field["type"] == "DATETIME":
                    # Add a condition to the SQL query to filter by the DATETIME field
                    conditions.append(f"{key} = ?")

                    # Add the value to the parameters list
                    parameters.append(value)

                elif field["type"] == "TIME":
                    # Add a condition to the SQL query to filter by the TIME field
                    conditions.append(f"{key} = ?")

                    # Add the value to the parameters list
                    parameters.append(value)

                elif field["type"] == "BLOB":
                    # Add a condition to the SQL query to filter by the BLOB field
                    conditions.append(f"{key} = ?")

                    # Add the value to the parameters list
                    parameters.append(value)

                elif field["type"] == "BOOLEAN":
                    # Add a condition to the SQL query to filter by the BOOLEAN field
                    conditions.append(f"{key} = ?")

                    # Add the value to the parameters list
                    parameters.append(value)

                elif field["type"] == "JSON":
                    # Add a condition to the SQL query to filter by the JSON field
                    conditions.append(f"JSON_CONTAINS({key}, ?)")

                    # Add the value to the parameters list
                    parameters.append(value)

                elif field["type"] == "ARRAY":
                    # Add a condition to the SQL query to filter by the ARRAY field
                    conditions.append(f"JSON_CONTAINS({key}, ?)")

                    # Add the value to the parameters list
                    parameters.append(value)

                elif field["type"] == "UUID":
                    # Add a condition to the SQL query to filter by the UUID field
                    conditions.append(f"{key} = ?")

                    # Add the value to the parameters list
                    parameters.append(value)

                else:
                    # Log a warning message indicating an unsupported field type
                    cls.logger.warning(
                        message=f"Unsupported field type: '{cls.__dict__[key]['type']}' in '{cls.__name__}' class. This is likely a bug."
                    )

            # Build the SQL query to search for entries that match the given keyword arguments
            sql: str = f"SELECT * FROM {cls.table} WHERE {' AND '.join(conditions)}"

            # Execute the SQL query and retrieve all matching rows
            result: Union[bool, List[Dict[str, Any]]] = (
                await cls.database_service.read_all(
                    database=database,
                    parameters=parameters,
                    sql=sql,
                )
            )

            # Check, if the read operation failed (i.e., if a boolean was returned)
            if isinstance(result, bool) and not result:
                # Log a warning message
                cls.logger.warning(
                    message=f"Failed to search entries from table '{cls.table}' in the database. SQL: '{sql}' | Parameters: '{parameters}'."
                )

                # Return None indicating the operation was not successful
                return None

            # Check, if the result list is empty
            if len(result) == 0:
                # Return None indicating no entries were found in the database
                return None

            # Return the list of model instances if multiple entries were found
            return [
                cls(**Miscellaneous.convert_from_db_format(data=row)) for row in result
            ]
        except Exception as e:
            # Log an error message indicating an exception occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{cls.__name__}' class: {e}"
            )

            # Log the traceback of the exception
            cls.logger.error(
                message=f"Traceback: {traceback.format_exc()}"
            )

            # Return None indicating an exception occurred
            return None

    @classmethod
    def to_sql_string(cls) -> str:
        """
        Returns a SQL string representation of the model's fields.

        Returns:
            str: The SQL string representation of the model's fields.
        """

        # Return a SQL string representation of the model's fields
        return ", ".join(
            [
                field.to_sql_string()
                for field in cls.__dict__.values()
                if isinstance(
                    field,
                    Field,
                )
            ]
        )

    async def update(
        self,
        database: str,
        **kwargs,
    ) -> bool:
        """
        Updates an existing model entry in the database.

        Args:
            database (str): Path to the SQLite database file.
            **kwargs: Fields to update and their new values.

        Returns:
            bool: True if update was successful, False otherwise.
        """
        try:
            # Build the SQL query
            updates: str = ", ".join([f"{key} = ?" for key in kwargs.keys()])

            # Build the parameters tuple
            parameters: Tuple[Any, ...] = tuple(
                Miscellaneous.convert_to_db_format(data=kwargs).values()
            ) + (self.id,)

            # Build the SQL query
            sql: str = f"UPDATE {self.table} SET {updates} WHERE id = ?"

            # Execute the SQL query
            result: Union[bool, int] = (
                await self.database_service.update(
                    database=database,
                    parameters=parameters,
                    sql=sql,
                )
                is not None
            )

            # Check, if the update operation failed (i.e., if a boolean was returned)
            if isinstance(result, bool) and not result:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to update entry in table '{self.table}' in the database."
                )

                # Return False indicating the operation was not successful
                return False

            # Log an info message
            self.logger.info(
                message=f"Updated entry in table '{self.table}' in the database."
            )

            # Return True indicating the operation was successful
            return True
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback of the exception
            self.logger.error(
                message=f"Traceback: {traceback.format_exc()}"
            )

            # Return False indicating an exception occurred
            return False

    @classmethod
    async def upsert_table(
        cls,
        database: str,
    ) -> None:
        """
        Creates the table if it does not exist or updates it if the schema has changed.

        Args:
            database (str): Path to the SQLite database file.

        Returns:
            None
        """
        try:
            # Execute the CREATE TABLE statement
            result: Union[bool, int] = await cls.database_service.execute(
                database=database,
                parameters=(),
                sql=f"CREATE TABLE IF NOT EXISTS {cls.table} ({', '.join([value.to_sql_string() for value in cls.__dict__.values() if isinstance(value, Field)])})",
            )

            # Check, if the table creation failed
            if isinstance(result, bool) and not result:
                # Log a warning message
                cls.logger.warning(
                    message=f"Failed to create table '{cls.table}' in the database."
                )

                # Return None indicating the operation was not successful
                return None

            # Get the existing columns
            existing_columns: Union[bool, List[Dict[str, Any]]] = (
                await cls.database_service.execute(
                    database=database,
                    parameters=(),
                    sql=f"PRAGMA table_info({cls.table});",
                )
            )

            # Check, if the table information retrieval failed
            if isinstance(result, bool) and not result:
                # Log a warning message
                cls.logger.warning(
                    message=f"Failed to retrieve table information for table '{cls.table}' in the database."
                )

                # Return None indicating the operation was not successful
                return None

            # Add missing columns
            for (
                field_name,
                field,
            ) in cls.__dict__.items():
                if isinstance(field, Field) and not any(
                    column["name"] == field_name for column in existing_columns
                ):
                    # Execute the ALTER TABLE statement
                    await cls.database_service.execute(
                        database=database,
                        parameters=(),  # Empty tuple
                        sql=f"ALTER TABLE {cls.table} ADD COLUMN {field.to_sql_string()};",
                    )

                    # Log an info message
                    cls.logger.info(
                        message=f"Added column '{field_name}' to table '{cls.table}' in the database."
                    )

            # Remove extra columns
            for column in existing_columns:
                if column["name"] not in cls.__dict__:
                    # Execute the ALTER TABLE statement
                    await cls.database_service.execute(
                        database=database,
                        parameters=(),  # Empty tuple
                        sql=f"ALTER TABLE {cls.table} DROP COLUMN {column['name']};",
                    )

                    # Log an info message
                    cls.logger.info(
                        message=f"Removed column '{column['name']}' from table '{cls.table}' in the database."
                    )

            # Log an info message
            cls.logger.info(
                message=f"Successfully updated table '{cls.table}' in the database."
            )
        except Exception as e:
            # Log an error message indicating an exception occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'upsert_table' method from '{cls.__name__}' class: {e}"
            )

            # Log the traceback of the exception
            cls.logger.error(
                message=f"Traceback: {traceback.format_exc()}"
            )

            # Raise the exception to the caller
            raise e
