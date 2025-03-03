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
    "ImmutableDefault",
    "MutableDefault",
    "DefaultConverter",
    "DefaultFactory",
    "DefaultManager",
    "DefaultModel",
]


class ImmutableDefault(ImmutableBaseObject):
    """
    An immutable class representing a default.

    Attributes:
        name (str): The name of the default.
        type (str): The type of the default.
        value (str): The value of the default.
        created_at (datetime): The timestamp when the default was created.
        icon (str): The icon of the default.
        id (int): The ID of the default.
        key (str): The key of the default.
        updated_at (datetime): The timestamp when the default was last updated.
        uuid (str): The UUID of the default.
    """

    def __init__(
        self,
        name: str,
        type: str,
        value: str,
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "⚙️",
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableDefault class.

        Args:
            name (str): The name of the default.
            type (str): The type of the default.
            value (str): The value of the default.
            created_at (Optional[datetime]): The timestamp when the default was created.
            icon (Optional[str]): The icon of the default. Defaults to "⚙️".
            id (Optional[int]): The ID of the default.
            key (Optional[str]): The key of the default.
            updated_at (Optional[datetime]): The timestamp when the default was last updated.
            uuid (Optional[str]): The UUID of the default.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            icon=icon,
            id=id,
            key=key,
            name=name,
            type=type,
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )

    def to_mutable(self) -> "MutableDefault":
        """
        Returns a mutable copy of the ImmutableDefault instance.

        Returns:
            MutableDefault: A mutable copy of the ImmutableDefault instance.
        """

        # Create a new MutableDefault instance from the dictionary representation of the ImmutableDefault instance
        return MutableDefault(
            **self.to_dict(
                exclude=[
                    "_logger",
                ]
            )
        )


class MutableDefault(MutableBaseObject):
    """
    A mutable class representing a default.

    Attributes:
        name (str): The name of the default.
        type (str): The type of the default.
        value (str): The value of the default.
        created_at (datetime): The timestamp when the default was created.
        icon (str): The icon of the default.
        id (int): The ID of the default.
        key (str): The key of the default.
        updated_at (datetime): The timestamp when the default was last updated.
        uuid (str): The UUID of the default.
    """

    def __init__(
        self,
        name: str,
        type: str,
        value: str,
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "⚙️",
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableDefault class.

        Args:
            name (str): The name of the default.
            type (str): The type of the default.
            value (str): The value of the default.
            created_at (Optional[datetime]): The timestamp when the default was created.
            icon (Optional[str]): The icon of the default. Defaults to "⚙️".
            id (Optional[int]): The ID of the default.
            key (Optional[str]): The key of the default.
            updated_at (Optional[datetime]): The timestamp when the default was last updated.
            uuid (Optional[str]): The UUID of the default.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            icon=icon,
            id=id,
            key=key,
            name=name,
            type=type,
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )

    def to_immutable(self) -> "ImmutableDefault":
        """
        Returns an immutable copy of the MutableDefault instance.

        Returns:
            ImmutableDefault: An immutable copy of the MutableDefault instance.
        """

        # Create a new ImmutableDefault instance from the dictionary representation of the MutableDefault instance
        return ImmutableDefault(
            **self.to_dict(
                exclude=[
                    "_logger",
                ]
            )
        )


class DefaultConverter:
    """
    A converter class for transforming between DefaultModel and Default instances.

    This class provides methods to convert a DefaultModel instance to an Default instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the DefaultConverter class.
    """

    logger: Logger = Logger.get_logger(name="DefaultConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "DefaultModel",
    ) -> Optional[ImmutableDefault]:
        """
        Converts a given DefaultModel instance to an Default instance.

        Args:
            model (DefaultModel): The DefaultModel instance to be converted.

        Returns:
            Default: The converted Default instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the DefaultModel instance.
        """
        try:
            # Attempt to create and return a new instance of the Default class from the dictionary representation of the DefaultModel instance
            return ImmutableDefault(
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
        object: ImmutableDefault,
    ) -> Optional["DefaultModel"]:
        """
        Converts a given Default instance to a DefaultModel instance.

        Args:
            object (Default): The Default instance to be converted.

        Returns:
            DefaultModel: The converted DefaultModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the Default instance.
        """
        try:
            # Attempt to create and return a new instance of the DefaultModel class from the dictionary representation of the Default instance
            return DefaultModel(
                **object.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'object_to_model' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class DefaultFactory:
    """
    A factory class for creating instances of the Default class.

    Attributes:
        logger (Logger): The logger instance associated with the object.
    """

    logger: Logger = Logger.get_logger(name="DefaultFactory")

    @classmethod
    def create_default(
        cls,
        name: str,
        type: str,
        value: str,
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "⚙️",
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutableDefault]:
        """
        Creates a new instance of the Default class.

        Args:
            name (str): The name of the default.
            type (str): The type of the default.
            value (str): The value of the default.
            created_at (Optional[datetime]): The timestamp when the default was created.
            icon (Optional[str]): The icon of the default. Defaults to "⚙️".
            id (Optional[int]): The ID of the default.
            key (Optional[str]): The key of the default.
            updated_at (Optional[datetime]): The timestamp when the default was last updated.
            uuid (Optional[str]): The UUID of the default.

        Returns:
            Optional[ImmutableDefault]: The newly created instance of the Default class or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create the Default instance.
        """
        try:
            # Attempt to create and return a new instance of the Default class
            return ImmutableDefault(
                name=name,
                type=type,
                value=value,
                created_at=created_at,
                icon=icon,
                id=id,
                key=key,
                updated_at=updated_at,
                uuid=uuid,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_default' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class DefaultManager(BaseObjectManager):
    """
    A manager class for managing defaults in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for defaults.

    Attributes:
        cache: (List[Any]): The cache for storing defaults.
        logger (Logger): The logger instance associated with the object.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the DefaultManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def count_defaults(self) -> int:
        """
        Returns the number of defaults in the database.

        Returns:
            int: The number of defaults in the database.
        """
        try:
            # Count the number of defaults in the database
            result: Any = asyncio.run(
                DefaultModel.execute(
                    database=Constants.DATABASE_PATH,
                    sql=f"SELECT COUNT(*) FROM {Constants.DEFAULTS};",
                )
            )

            # Return the number of defaults in the database
            return result[0][0] if result else 0
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_default(
        self,
        default: ImmutableDefault,
    ) -> Optional[ImmutableDefault]:
        """
        Creates a new default in the database.

        Args:
            default (Default): The default to be created.

        Returns:
            Optional[ImmutableDefault]: The newly created immutable default if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the default.
        """
        try:
            # Check if the default object is immutable
            if isinstance(
                default,
                ImmutableDefault,
            ):
                # If it is, convert it to a mutable default
                default = MutableDefault(
                    **default.to_dict(
                        exclude=[
                            "_logger",
                        ]
                    )
                )

            # Set the created_at timestamp of the default
            default.created_at = Miscellaneous.get_current_datetime()

            # Set the key of the default
            default.key = f"DEFAULT_{self.count_defaults() + 1}"

            # Set the updated_at timestamp of the default
            default.updated_at = Miscellaneous.get_current_datetime()

            # Set the uuid of the default
            default.uuid = Miscellaneous.get_uuid()

            # Convert the default object to a DefaultModel object
            model: DefaultModel = DefaultConverter.object_to_model(object=default)

            # Create a new default in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            if id:
                # Set the ID of the default
                default.id = id

                # Convert the default to an immutable default
                default = ImmutableDefault(
                    **default.to_dict(
                        exclude=[
                            "_logger",
                        ]
                    )
                )

                # Add the default to the cache
                self.add_to_cache(
                    key=default.key,
                    value=default,
                )

                # Return the newly created immutable default
                return default

            # Log a warning message indicating an error has occurred
            self.logger.warning(
                message=f"It seems that an error has occured while attempting to create a default ({default}) in the database."
            )

            # Return None indicating an error has occurred
            return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_default' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete_default(
        self,
        default: ImmutableDefault,
    ) -> bool:
        """
        Deletes a default from the database.

        Args:
            default (Default): The default to be deleted.

        Returns:
            bool: True if the default was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the default to an immutable default and delete the default from the database
            result: bool = asyncio.run(
                DefaultConverter.object_to_model(
                    object=ImmutableDefault(
                        **default.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).delete()
            )

            # Return True if the default was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all_defaults(self) -> Optional[List[ImmutableDefault]]:
        """
        Returns a list of all defaults in the database.

        Returns:
            Optional[List[ImmutableDefault]]: A list of all defaults in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if cache and table size are equal
            if self.cache and len(self._cache) == self.count_defaults():
                # Return the list of immutable defaults from the cache
                return self.get_cache_values()

            # Get all defaults from the database
            models: List[DefaultModel] = asyncio.run(
                DefaultModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of DefaultModel objects to a list of Default objects
            defaults: List[ImmutableDefault] = [
                ImmutableDefault(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable defaults
            for default in defaults:
                if not self.is_key_in_cache(key=default.key):
                    # Add the immutable default to the cache
                    self.add_to_cache(
                        key=default.key,
                        value=default,
                    )
                else:
                    # Update the immutable default in the cache
                    self.update_in_cache(
                        key=default.key,
                        value=default,
                    )

            # Return the list of immutable defaults
            return defaults
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_default_by(
        self,
        field: str,
        value: Any,
    ) -> Optional[Union[ImmutableDefault, List[ImmutableDefault]]]:
        """
        Retrieves a default or list of defaults by the given field and value.

        Args:
            field (str): The field to search by.
            value (Any): The value to search for.

        Returns:
            Optional[Union[ImmutableDefault, List[ImmutableDefault]]]: The default(s) with the given field and value
            if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the default is already in the cache
            if self.is_key_in_cache(key=field):
                # Return the default from the cache
                return self.get_value_from_cache(key=field)

            # Get the default(s) with the given field and value from the database
            models: Optional[Union[DefaultModel, List[DefaultModel]]] = asyncio.run(
                DefaultModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Check if no default(s) are found
            if models is None:
                # Return None indicating that the default(s) do not exist
                return None

            # Convert the model(s) to ImmutableDefault(s)
            if isinstance(
                models,
                list,
            ):
                # Return a list of ImmutableDefault objects
                return [
                    ImmutableDefault(
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
                # Return a single ImmutableDefault object
                return ImmutableDefault(
                    **models.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_default_by_id(
        self,
        id: int,
    ) -> Optional[ImmutableDefault]:
        """
        Returns a default with the given ID.

        Args:
            id (int): The ID of the default.

        Returns:
            Optional[ImmutableDefault]: The default with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the default is already in the cache
            if self.is_key_in_cache(key=f"DEFAULT_{id}"):
                # Return the default from the cache
                return self.get_value_from_cache(key=f"DEFAULT_{id}")

            # Get the default with the given ID from the database
            model: Optional[DefaultModel] = asyncio.run(
                DefaultModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the default if it exists
            if model is not None:
                # Convert the DefaultModel object to an Default object
                return ImmutableDefault(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the default does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_default_by_uuid(
        self,
        uuid: str,
    ) -> Optional[ImmutableDefault]:
        """
        Returns a default with the given UUID.

        Args:
            uuid (str): The UUID of the default.

        Returns:
            Optional[ImmutableDefault]: The default with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the default is already in the cache
            if self.is_key_in_cache(key=uuid):
                # Return the default from the cache
                return self.get_value_from_cache(key=uuid)

            # Get the default with the given UUID from the database
            model: Optional[DefaultModel] = asyncio.run(
                DefaultModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the default if it exists
            if model is not None:
                # Convert the DefaultModel object to an Default object
                return ImmutableDefault(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the default does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def search_defaults(
        self,
        **kwargs,
    ) -> Optional[Union[List[ImmutableDefault]]]:
        """
        Searches for defaults in the database.

        Args:
            **kwargs: Any additional keyword arguments to be passed to the search method of the DefaultModel class.

        Returns:
            Optional[Union[List[ImmutableDefault]]]: The found defaults if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Search for defaults in the database
            models: Optional[List[DefaultModel]] = asyncio.run(
                DefaultModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found defaults if any
            if models is not None and len(models) > 0:
                return [
                    ImmutableDefault(
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
                # Return None indicating that no defaults were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_default(
        self,
        default: ImmutableDefault,
    ) -> Optional[ImmutableDefault]:
        """
        Updates a default with the given ID.

        Args:
            default (Default): The default to update.

        Returns:
            Optional[ImmutableDefault]: The updated default if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the default to an immutable default and update the default in the database
            model: Optional[DefaultModel] = asyncio.run(
                DefaultConverter.object_to_model(
                    object=ImmutableDefault(
                        **default.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).update(
                    database=Constants.DATABASE_PATH,
                    **default.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Return the updated default if it exists
            if model is not None:
                # Convert the DefaultModel object to an Default object
                default = ImmutableDefault(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the default to the cache
                self.update_in_cache(
                    key=default.key,
                    value=default,
                )

                # Return the updated default
                return default
            else:
                # Return None indicating that the default does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class DefaultModel(ImmutableBaseModel):
    """
    Represents the structure of a default model.

    Attributes:
        created_at (Optional[datetime]): The timestamp when the default was created.
        icon (Optional[str]): The icon of the default. Defaults to "⚙️".
        id (Optional[int]): The ID of the default.
        key (Optional[str]): The key of the default.
        name (Optional[str]): The name of the default.
        type (Optional[str]): The type of the default.
        updated_at (Optional[datetime]): The timestamp when the default was last updated.
        uuid (Optional[str]): The UUID of the default.
        value (Optional[str]): The value of the default.
    """

    table: str = Constants.DEFAULTS

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

    icon: Field = Field(
        autoincrement=False,
        default="⚙️",
        description="",
        foreign_key=None,
        index=False,
        name="icon",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
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

    value: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="value",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=False,
    )

    def __init__(
        self,
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "⚙️",
        id: Optional[int] = None,
        key: Optional[str] = None,
        name: Optional[str] = None,
        type: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
        value: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the DefaultModel class.

        Args:
            created_at (Optional[datetime]): The timestamp when the default was created.
            icon (Optional[str]): The icon of the default. Defaults to "⚙️".
            id (Optional[int]): The ID of the default.
            key (Optional[str]): The key of the default.
            name (Optional[str]): The name of the default.
            type (Optional[str]): The type of the default.
            updated_at (Optional[datetime]): The timestamp when the default was last updated.
            uuid (Optional[str]): The UUID of the default.
            value (Optional[str]): The value of the default.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            icon="⚙️",
            id=id,
            key=key,
            name=name,
            table=Constants.DEFAULTS,
            type=type,
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )
