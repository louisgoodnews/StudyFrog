"""
Author: lodego
Date: 2025-02-05
"""

from typing import *

from utils.object import ImmutableBaseObject


__all__: List[str] = ["Field"]


class Field(ImmutableBaseObject):
    """
    Represents a column in a SQLite databse table.

    Attributes:
        autoincrement (bool): If the field is an auto-incrementing primary key.
        default (Any): The default value for the field.
        description (str): A description of the field.
        foreign_key (str): The name of the field that this field is a foreign key to.
        index (bool): If the field should be indexed.
        name (str): The name of the field.
        nullable (bool): If the field can be null.
        on_delete (str): What to do when the referenced field is deleted.
            Possible values are "CASCADE", "SET NULL", "NO ACTION", "RESTRICT", "SET DEFAULT"
        on_update (str): What to do when the referenced field is updated.
            Possible values are "CASCADE", "SET NULL", "NO ACTION", "RESTRICT", "SET DEFAULT"
        primary (bool): If the field is a primary key.
        size (int): The size of the field.
        type (str): The type of the field.
            Possible values are "BLOB", "BOOLEAN", "DATE", "DATETIME", "FLOAT", "INTEGER", "JSON","TIME", "VARCHAR", "NULL", "REAL", "TEXT"
        unique (bool): If the field is unique.
            If True, the field will be indexed and a unique constraint will be created.
        unique_together (List[str]): A list of fields that should be unique together.
    """

    def __init__(
        self,
        autoincrement: Optional[bool] = None,
        default: Optional[Any] = None,
        description: Optional[str] = None,
        foreign_key: Optional[str] = None,
        index: Optional[bool] = None,
        name: Optional[str] = None,
        nullable: Optional[bool] = None,
        on_delete: Optional[
            Literal["CASCADE", "SET NULL", "NO ACTION", "RESTRICT", "SET DEFAULT"]
        ] = None,
        on_update: Optional[
            Literal["CASCADE", "SET NULL", "NO ACTION", "RESTRICT", "SET DEFAULT"]
        ] = None,
        primary: Optional[bool] = None,
        size: Optional[int] = None,
        type: Optional[
            Literal[
                "BLOB",
                "BOOLEAN",
                "DATE",
                "DATETIME",
                "FLOAT",
                "INTEGER",
                "JSON",
                "TIME",
                "VARCHAR",
                "NULL",
                "REAL",
                "TEXT",
            ]
        ] = None,
        unique: Optional[bool] = None,
        unique_together: Optional[List[str]] = None,
    ) -> None:
        """
        Represents a field in a table.

        Attributes:
            autoincrement (bool): If the field is an auto-incrementing primary key.
            default (Any): The default value for the field.
            description (str): A description of the field.
            foreign_key (str): The name of the field that this field is a foreign key to.
            index (bool): If the field should be indexed.
            name (str): The name of the field.
            nullable (bool): If the field can be null.
            on_delete (str): What to do when the referenced field is deleted.
                Possible values are "CASCADE", "SET NULL", "NO ACTION", "RESTRICT", "SET DEFAULT"
            on_update (str): What to do when the referenced field is updated.
                Possible values are "CASCADE", "SET NULL", "NO ACTION", "RESTRICT", "SET DEFAULT"
            primary (bool): If the field is a primary key.
            size (int): The size of the field.
            type (str): The type of the field.
                Possible values are "BLOB", "BOOLEAN", "DATE", "DATETIME", "FLOAT", "INTEGER", "JSON","TIME", "VARCHAR", "NULL", "REAL", "TEXT"
            unique (bool): If the field should be unique.
            unique_together (List[str]): A list of fields that should be unique together.

        Returns:
            None
        """

        # Call the super class constructor
        super().__init__(
            autoincrement=autoincrement,
            default=default,
            description=description,
            foreign_key=foreign_key,
            index=index,
            name=name,
            nullable=nullable,
            on_delete=on_delete,
            on_update=on_update,
            primary=primary,
            size=size,
            type=type,
            unique=unique,
            unique_together=unique_together,
        )

    def to_sql_string(self) -> str:
        """
        Converts the field object to a SQL-compatible column definition.

        Args:
            None

        Returns:
            str: The SQL string representing the field.
        """
        if not self.name or not self.type:
            raise ValueError("Field must have a name and type.")

        sql_parts: List[str] = [
            # Column name and type
            f'"{self.name}" {self.type}',
        ]

        if self.size and self.type.upper() in {"VARCHAR"}:
            # Add size if field is VARCHAR
            sql_parts[-1] += f"({self.size})"

        if self.primary:
            # PRIMARY KEY and AUTOINCREMENT
            sql_parts.append("PRIMARY KEY")
            if self.autoincrement and self.type.upper() == "INTEGER":
                sql_parts.append("AUTOINCREMENT")

        if self.unique:
            # UNIQUE constraint
            sql_parts.append("UNIQUE")

        if self.nullable is not None:
            # NULL or NOT NULL
            sql_parts.append("NULL" if self.nullable else "NOT NULL")

        if self.default is not None:
            # DEFAULT value
            sql_parts.append(f"DEFAULT {self.default!r}")

        if self.foreign_key:
            # FOREIGN KEY
            sql_parts.append(f"REFERENCES {self.foreign_key}")

        if self.on_delete:
            # ON DELETE action
            sql_parts.append(f"ON DELETE {self.on_delete}")
        if self.on_update:
            # ON UPDATE action
            sql_parts.append(f"ON UPDATE {self.on_update}")

        # Join all parts together
        return " ".join(sql_parts)
