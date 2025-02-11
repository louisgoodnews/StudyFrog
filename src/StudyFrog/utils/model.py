"""
Author: lodego
Date: 2025-02-05
"""

from typing import *

from utils.database_service import DatabaseService
from utils.field import Field
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous
from utils.object import ImmutableBaseObject


__all__: List[str] = [
    "ImmutableBaseModel",
]


T: TypeVar("T") = TypeVar("T")


class ImmutableBaseModel(ImmutableBaseObject):
    """
    Represents an immutable base model for interacting with a SQLite database table.

    This class provides a base implementation for models that are stored in a SQLite database table.

    Attributes:
        logger (Logger): The logger instance associated with the object.
    """

    logger: Logger = Logger.get_logger(name="ImmutableBaseModel")

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
                self.to_dict(exclude=["_logger"])
            )

            # Extract columns and values
            columns = ", ".join(converted_data.keys())
            placeholders = ", ".join(["?" for _ in converted_data])
            parameters = tuple(converted_data.values())  # Convert to tuple

            # Construct SQL query
            sql = f"INSERT INTO {self.table} ({columns}) VALUES ({placeholders});"

            # Execute SQL command and return the last row ID
            return await DatabaseService.create(
                database=database,
                parameters=parameters,
                sql=sql,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'save' method from '{self.__class__.__name__}' class: {e}"
            )

            # Return None indicating an exception occurred
            return None

    @classmethod
    async def create_table(
        cls,
        database: str,
    ) -> None:
        """
        Creates the table based on the defined fields.

        Args:
            database (str): Path to the SQLite database file.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Build the SQL query
            sql: str = (
                f"CREATE TABLE IF NOT EXISTS {cls.table} ({", ".join([value.to_sql_string() for value in cls.__dict__.values() if isinstance(value, Field)])})"
            )

            # Execute the SQL query
            await DatabaseService.execute(
                database=database,
                parameters=(),
                sql=sql,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_table' method from '{cls.__name__}' class: {e}"
            )

            # Return None indicating an exception occurred
            return None

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
            return await DatabaseService.delete(
                database=database,
                parameters=(self.id,),
                sql=sql,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}' class: {e}"
            )

            # Return False indicating the operation failed
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
            return await DatabaseService.execute(
                database=database,
                parameters=(),
                sql=sql,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'drop_table' method from '{cls.__name__}' class: {e}"
            )

            # Return False indicating the operation failed
            return False

    @classmethod
    async def execute(
        cls,
        database: str,
        sql: str,
        parameters: Optional[Tuple[..., Any]] = [],
    ) -> Any:
        """
        Executes a custom SQL query.

        Args:
            database (str): Path to the SQLite database file.
            parameters (Tuple[..., Any], optional): Parameters for the query.
            sql (str): The SQL query to execute.

        Returns:
            Any: The result of the query.
        """
        try:
            # Execute the SQL query
            return await DatabaseService.execute(
                database=database,
                parameters=parameters,
                sql=sql,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'execute' method from '{cls.__name__}' class: {e}"
            )

            # Return None indicating an exception occurred
            return None

    @classmethod
    async def get_all(
        cls: Type[T],
        database: str,
    ) -> List[T]:
        """
        Retrieves all rows from the model's table.

        Args:
            database (str): Path to the SQLite database file.

        Returns:
            List[T]: List of model instances.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Build the SQL query
            sql: str = f"SELECT * FROM {cls.table}"

            # Execute the SQL query
            rows: List[Dict[str, Any]] = await DatabaseService.read_all(
                database=database,
                parameters=(),
                sql=sql,
            )

            # Return the model instances
            return [
                cls(**Miscellaneous.convert_from_db_format(data=row)) for row in rows
            ]
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{cls.__name__}' class: {e}"
            )

            # Return an empty list indicating an exception occurred
            return []

    @classmethod
    async def get_by(
        cls: Type[T],
        database: str,
        column: str,
        value: Any,
    ) -> Optional[T]:
        """
        Retrieves a single model entry by a column value.

        Args:
            database (str): Path to the SQLite database file.
            column (str): Column to filter by.
            value (Any): Value to match.

        Returns:
            Optional[T]: The model instance if found, otherwise None.
        """
        try:
            # Build the SQL query
            sql: str = f"SELECT * FROM {cls.table} WHERE {column} = ?"

            # Execute the SQL query
            row: Dict[str, Any] = await DatabaseService.read_one(
                database=database,
                parameters=(value,),
                sql=sql,
            )

            # Return the model instance
            return (
                cls(**Miscellaneous.convert_from_db_format(data=row)) if row else None
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{cls.__name__}' class: {e}"
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
            return (
                await DatabaseService.update(
                    database=database,
                    parameters=parameters,
                    sql=sql,
                )
                > 0
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}' class: {e}"
            )

            # Return False indicating an exception occurred
            return False
