"""
Author: lodego
Date: 2025-02-05
"""

from typing import *

from utils.database_service import DatabaseService
from utils.field import Field
from utils.object import ImmutableBaseObject


__all__: List[str] = [
    "ImmutableBaseModel",
]


T: TypeVar("T") = TypeVar("T")


class ImmutableBaseModel(ImmutableBaseObject):
    def __init__(
        self,
        table: str,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the ImmutableBaseModel class.

        Args:
            table (str): The name of the table represented by the model.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            fields={},
            table=table,
        )

        for (
            key,
            value,
        ) in kwargs.items():
            self.add_field(
                key=key,
                value=value,
            )

    def add_field(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Adds a key-value pair to the model's fields dictionary.

        Args:
            key (str): The name of the field.
            value (Any): The value of the field.

        Returns:
            None
        """

        # Check if the field already exists
        if key in self.fields.keys():
            # Log a warning message
            self.logger.warning(message=f"Field '{key}' already exists. Overwriting...")

        # Add the field to the fields dictionary
        self.fields[key] = value

    async def create_table(
        self,
        database: str,
    ) -> bool:
        """
        Creates the table based on the defined fields.

        Args:
            database (str): Path to the SQLite database file.

        Returns:
            bool: True if the table was created successfully, False otherwise.
        """

        # Build the field definitions string
        field_definitions: str = ", ".join(
            [field.to_sql_string() for field in self.fields.values()]
        )

        # Build the SQL query
        sql: str = f"CREATE TABLE IF NOT EXISTS {self.table} ({field_definitions})"

        # Execute the SQL query
        return await DatabaseService.execute(
            database=database,
            sql=sql,
        )

    async def drop_table(
        self,
        database: str,
    ) -> bool:
        """
        Drops the table associated with the model.

        Args:
            database (str): Path to the SQLite database file.

        Returns:
            bool: True if the table was dropped successfully, False otherwise.
        """

        # Build the SQL query
        sql: str = f"DROP TABLE IF EXISTS {self.table}"

        # Execute the SQL query
        return await DatabaseService.execute(
            database=database,
            sql=sql,
        )

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
        # Build the SQL query
        sql: str = f"SELECT * FROM {cls.table} WHERE {column} = ?"

        # Execute the SQL query
        row: Dict[str, Any] = await DatabaseService.read_one(database, sql, value)

        # Return the model instance
        return cls(**row) if row else None

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
        """

        # Build the SQL query
        sql: str = f"SELECT * FROM {cls.table}"

        # Execute the SQL query
        rows: List[Dict[str, Any]] = await DatabaseService.read_all(
            database=database,
            sql=sql,
        )

        # Return the model instances
        return [cls(**row) for row in rows]

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
        """

        # Build the SQL query
        sql: str = f"DELETE FROM {self.table} WHERE id = ?"

        # Execute the SQL query
        return await DatabaseService.delete(database, sql, self.id) > 0

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

        # Build the SQL query
        updates: str = ", ".join([f"{key} = ?" for key in kwargs.keys()])

        # Build the values tuple
        values: Tuple[Any, ...] = tuple(kwargs.values()) + (self.id,)

        # Build the SQL query
        sql: str = f"UPDATE {self.table} SET {updates} WHERE id = ?"

        # Execute the SQL query
        return await DatabaseService.update(database, sql, *values) > 0

    async def execute(
        self,
        database: str,
        sql: str,
        *args,
    ) -> bool:
        """
        Executes a custom SQL query.

        Args:
            database (str): Path to the SQLite database file.
            sql (str): The SQL query to execute.
            *args: Parameters for the query.

        Returns:
            bool: True if query executed successfully, False otherwise.
        """

        # Execute the SQL query
        return await DatabaseService.execute(
            database,
            sql,
            *args,
        )

    async def save(
        self,
        database: str,
    ) -> Optional[int]:
        """
        Inserts a new model instance into the database.

        Args:
            database (str): Path to the SQLite database file.

        Returns:
            Optional[int]: The ID of the inserted row or None if insert failed.
        """

        # Get the fields and values
        fields: List[str] = [key for key in self.fields.keys()]

        # Build the placeholder string
        placeholders: str = ", ".join(["?" for _ in fields])

        # Build the field names
        field_names: str = ", ".join(fields)

        # Build the SQL query
        sql = f"INSERT INTO {self.table} ({field_names}) VALUES ({placeholders})"

        # Get the values of the value
        values: Tuple[Any, ...] = tuple(
            getattr(
                self,
                field,
            )
            for field in fields
        )

        # Execute the SQL query
        return await DatabaseService.create(
            database,
            sql,
            *values,
        )

    def to_sql_string(self) -> str:
        """
        Returns a SQL string representation of the model's fields.

        Returns:
            str: The SQL string representation of the model's fields.
        """

        # Return a SQL string representation of the model's fields
        return ", ".join([field.to_sql_string() for field in self.fields.values()])
