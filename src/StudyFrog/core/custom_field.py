"""
Author: lodego
Date: 2025-02-09
"""

import asyncio

import uuid

from datetime import datetime

from typing import *

from utils.constants import Constants
from utils.field import Field
from utils.logger import Logger
from utils.manager import BaseObjectManager
from utils.miscellaneous import Miscellaneous
from utils.model import ImmutableBaseModel
from utils.object import MutableBaseObject, ImmutableBaseObject


__all__: List[str] = [
    "CustomField",
    "CustomFieldConverter",
    "CustomFieldFactory",
    "CustomFieldModel",
]


class CustomField(ImmutableBaseObject):
    """
    An immutable class representing a custom field.

    Attributes:
        name (str): The name of the custom field.
        type (str): The type of the custom field.
        created_at (Optional[datetime]): The timestamp when the custom field was created.
        id (Optional[int]): The ID of the custom field.
        key (Optional[str]): The key of the custom field.
        updated_at (Optional[datetime]): The timestamp when the custom field was last updated.
        uuid (Optional[str]): The UUID of the custom field.
    """

    def __init__(
        self,
        name: str,
        type: str,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the CustomField class.

        Args:
            name (str): The name of the custom field.
            type (str): The type of the custom field.
            created_at (Optional[datetime]): The timestamp when the custom field was created.
            id (Optional[int]): The ID of the custom field.
            key (Optional[str]): The key of the custom field.
            updated_at (Optional[datetime]): The timestamp when the custom field was last updated.
            uuid (Optional[str]): The UUID of the custom field.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            id=id,
            key=key,
            name=name,
            type=type,
            updated_at=updated_at,
            uuid=uuid,
        )


class CustomFieldConverter:
    """
    A converter class for transforming between CustomFieldModel and CustomField instances.

    This class provides methods to convert a CustomFieldModel instance to an CustomField instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the CustomFieldConverter class.
    """

    logger: Logger = Logger.get_logger(name="CustomFieldConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "CustomFieldModel",
    ) -> Optional[CustomField]:
        """
        Converts a given CustomFieldModel instance to an CustomField instance.

        Args:
            model (CustomFieldModel): The CustomFieldModel instance to be converted.

        Returns:
            CustomField: The converted CustomField instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the CustomFieldModel instance.
        """
        try:
            # Attempt to create and return a new instance of the CustomField class from the dictionary representation of the CustomFieldModel instance
            return CustomField(
                **model.to_dict(
                    exclude=[
                        "_logger",
                        "table",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'model_to_object' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def object_to_model(
        cls,
        object: CustomField,
    ) -> Optional["CustomFieldModel"]:
        """
        Converts a given CustomField instance to a CustomFieldModel instance.

        Args:
            object (CustomField): The CustomField instance to be converted.

        Returns:
            CustomFieldModel: The converted CustomFieldModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the CustomField instance.
        """
        try:
            # Attempt to create and return a new instance of the CustomFieldModel class from the dictionary representation of the CustomField instance
            return CustomFieldModel(**object.to_dict(exclude=["_logger"]))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'object_to_model' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class CustomFieldFactory:
    logger: Logger = Logger.get_logger(name="CustomFieldFactory")

    @classmethod
    def create_custom_field(
        cls,
        name: str,
        type: str,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[CustomField]:
        """
        Creates and returns a new instance of the CustomField class.

        Args:
            name (str): The name of the custom field.
            type (str): The type of the custom field.
            created_at (datetime): The timestamp when the custom field was created.
            id (int): The ID of the custom field.
            key (str): The key of the custom field.
            updated_at (datetime): The timestamp when the custom field was last updated.
            uuid (str): The UUID of the custom field.

        Returns:
            Optional[CustomField]: The newly created CustomField instance or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create the CustomField instance.
        """
        try:
            # Attempt to create and return a new instance of the CustomField class
            return CustomField(
                created_at=created_at,
                id=id,
                key=key,
                name=name,
                type=type,
                updated_at=updated_at,
                uuid=uuid,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_custom_field' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class CustomFieldManager(BaseObjectManager):
    """
    A manager class for managing custom fields in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for custom fields.

    Attributes:
        cache: (List[Any]): The cache for storing custom fields.
        logger (Logger): The logger instance associated with the object.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the CustomFieldManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def count_custom_fields(self) -> int:
        """
        Returns the number of custom fields in the database.

        Returns:
            int: The number of custom fields in the database.
        """
        try:
            # Count the number of custom fields in the database
            result: Any = asyncio.run(
                CustomFieldModel.execute(
                    database=Constants.DATABASE_PATH,
                    sql=f"SELECT COUNT(*) FROM {Constants.SETTINGS};",
                )
            )

            # Return the number of custom fields in the database
            return result[0][0] if result else 0
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_custom_field(
        self,
        custom_field: CustomField,
    ) -> Optional[CustomField]:
        """
        Creates a new custom field in the database.

        Args:
            custom field (CustomField): The custom field to be created.

        Returns:
            Optional[CustomField]: The newly created immutable custom field if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the custom field.
        """
        try:
            # Set the created_at timestamp of the custom field
            custom_field.created_at = Miscellaneous.get_current_datetime()

            # Set the key of the custom field
            custom_field.key = f"CUSTOM_FIELD_{self.count_custom_fields() + 1}"

            # Set the updated_at timestamp of the custom field
            custom_field.updated_at = Miscellaneous.get_current_datetime()

            # Set the uuid of the custom field
            custom_field.uuid = Miscellaneous.get_uuid()

            # Convert the custom field object to a CustomFieldModel object
            model: CustomFieldModel = CustomFieldConverter.object_to_model(
                object=setting
            )

            # Create a new custom field in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            if id:
                # Set the ID of the custom field
                custom_field.id = id

                # Convert the custom field to an immutable custom field
                custom_field = CustomField(**custom_field.to_dict(exclude=["_logger"]))

                # Add the custom field to the cache
                self.add_to_cache(
                    key=custom_field.key,
                    value=setting,
                )

                # Return the newly created immutable custom field
                return custom_field

            # Log a warning message indicating an error has occurred
            self.logger.warning(
                message=f"It seems that an error has occured while attempting to create a custom field ({setting}) in the database."
            )

            # Return None indicating an error has occurred
            return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_setting' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete_custom_field(
        self,
        custom_field: CustomField,
    ) -> bool:
        """
        Deletes a custom field from the database.

        Args:
            custom field (CustomField): The custom field to be deleted.

        Returns:
            bool: True if the custom field was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the custom field to an immutable custom field and delete the custom field from the database
            result: bool = asyncio.run(
                CustomFieldConverter.object_to_model(
                    object=CustomField(**custom_field.to_dict(exclude=["_logger"]))
                ).delete()
            )

            # Return True if the custom field was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all_custom_fields(self) -> Optional[List[CustomField]]:
        """
        Returns a list of all custom fields in the database.

        Returns:
            Optional[List[CustomField]]: A list of all custom fields in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if cache and table size are equal
            if self.cache and len(self._cache) == self.count_custom_fields():
                # Return the list of immutable custom fields from the cache
                return self.get_cache_values()

            # Get all custom fields from the database
            models: List[CustomFieldModel] = asyncio.run(
                CustomFieldModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of CustomFieldModel objects to a list of CustomField objects
            custom_fields: List[CustomField] = [
                CustomField(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable custom fields
            for custom_field in custom_fields:
                if not self.is_key_in_cache(key=custom_field.key):
                    # Add the immutable custom field to the cache
                    self.add_to_cache(
                        key=custom_field.key,
                        value=setting,
                    )
                else:
                    # Update the immutable custom field in the cache
                    self.update_in_cache(
                        key=custom_field.key,
                        value=setting,
                    )

            # Return the list of immutable custom fields
            return custom_fields
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_custom_field_by(
        self,
        field: str,
        value: Any,
    ) -> Optional[CustomField]:
        """
        Retrieves a custom field by the given field and value.

        Args:
            field (str): The field to search by.
            value (Any): The value to search for.

        Returns:
            Optional[CustomField]: The custom field with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the custom field is already in the cache
            if self.is_key_in_cache(key=field):
                # Return the custom field from the cache
                return self.get_value_from_cache(key=field)

            # Get the custom field with the given field and value from the database
            model: Optional[CustomFieldModel] = asyncio.run(
                CustomFieldModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Return the custom field if it exists
            if model is not None:
                # Convert the CustomFieldModel object to an CustomField object
                return CustomField(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the custom field does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_custom_field_by_id(
        self,
        id: int,
    ) -> Optional[CustomField]:
        """
        Returns a custom field with the given ID.

        Args:
            id (int): The ID of the custom_field.

        Returns:
            Optional[CustomField]: The custom field with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the custom field is already in the cache
            if self.is_key_in_cache(key=f"CUSTOM_FIELD_{id}"):
                # Return the custom field from the cache
                return self.get_value_from_cache(key=f"CUSTOM_FIELD_{id}")

            # Get the custom field with the given ID from the database
            model: Optional[CustomFieldModel] = asyncio.run(
                CustomFieldModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the custom field if it exists
            if model is not None:
                # Convert the CustomFieldModel object to an CustomField object
                return CustomField(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the custom field does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_custom_field_by_uuid(
        self,
        uuid: str,
    ) -> Optional[CustomField]:
        """
        Returns a custom field with the given UUID.

        Args:
            uuid (str): The UUID of the custom_field.

        Returns:
            Optional[CustomField]: The custom field with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the custom field is already in the cache
            if self.is_key_in_cache(key=uuid):
                # Return the custom field from the cache
                return self.get_value_from_cache(key=uuid)

            # Get the custom field with the given UUID from the database
            model: Optional[CustomFieldModel] = asyncio.run(
                CustomFieldModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the custom field if it exists
            if model is not None:
                # Convert the CustomFieldModel object to an CustomField object
                return CustomField(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the custom field does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def search_custom_fields(
        self,
        **kwargs,
    ) -> Optional[Union[List[CustomField]]]:
        """
        Searches for custom fields in the database.

        Args:
            **kwargs: Any additional keyword arguments to be passed to the search method of the CustomFieldModel class.

        Returns:
            Optional[Union[List[CustomField]]]: The found custom fields if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Search for custom fields in the database
            models: Optional[List[CustomFieldModel]] = asyncio.run(
                CustomFieldModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found custom fields if any
            if models is not None and len(models) > 0:
                return [
                    CustomField(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                    for model in models
                ]
            else:
                # Return None indicating that no custom fields were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_custom_field(
        self,
        custom_field: CustomField,
    ) -> Optional[CustomField]:
        """
        Updates a custom field with the given ID.

        Args:
            custom field (CustomField): The custom field to update.

        Returns:
            Optional[CustomField]: The updated custom field if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the custom field to an immutable custom field and update the custom field in the database
            model: Optional[CustomFieldModel] = asyncio.run(
                CustomFieldConverter.object_to_model(
                    object=CustomField(**custom_field.to_dict(exclude=["_logger"]))
                ).update(
                    database=Constants.DATABASE_PATH,
                    **custom_field.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Return the updated custom field if it exists
            if model is not None:
                # Convert the CustomFieldModel object to an CustomField object
                custom_field = CustomField(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the custom field to the cache
                self.update_in_cache(
                    key=custom_field.key,
                    value=setting,
                )

                # Return the updated custom field
                return custom_field
            else:
                # Return None indicating that the custom field does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class CustomFieldModel(ImmutableBaseModel):
    """
    Represents the structure of a custom field model.

    Attributes:
        created_at (datetime): The timestamp when the custom field was created.
        id (int): The ID of the custom field.
        key (str): The key of the custom field.
        name (str): The name of the custom field.
        type (str): The type of the custom field.
        updated_at (datetime): The timestamp when the custom field was last updated.
        uuid (str): The UUID of the custom field.
    """

    table: str = Constants.CUSTOM_FIELDS

    id: Field = Field(
        autoincrement=True,
        default=None,
        description="",
        foreign_key=None,
        index=True,
        name="id",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=True,
        size=None,
        type="INTEGER",
        unique=False,
    )

    created_at: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="created_at",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="DATETIME",
        unique=False,
    )

    key: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="key",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=True,
    )

    name: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="name",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=True,
    )

    type: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="type",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=False,
    )

    updated_at: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="updated_at",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="DATETIME",
        unique=False,
    )

    uuid: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="uuid",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=True,
    )

    def __init__(
        self,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        name: Optional[str] = None,
        type: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the CustomField class.

        Args:
            created_at (Optional[datetime]): The timestamp when the custom field was created.
            id (Optional[int]): The ID of the custom field.
            key (Optional[str]): The key of the custom field.
            name (Optional[str]): The name of the custom field.
            type (Optional[str]): The type of the custom field.
            updated_at (Optional[datetime]): The timestamp when the custom field was last updated.
            uuid (Optional[str]): The UUID of the custom field.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            id=id,
            key=key,
            name=name,
            type=type,
            updated_at=updated_at,
            uuid=uuid,
        )
