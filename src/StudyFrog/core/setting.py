"""
Author: lodego
Date 2025-02-09
"""

import asyncio

from datetime import datetime

from typing import *

from core.default import ImmutableDefault, DefaultManager

from utils.constants import Constants
from utils.field import Field
from utils.logger import Logger
from utils.manager import BaseObjectManager
from utils.miscellaneous import Miscellaneous
from utils.model import ImmutableBaseModel
from utils.object import MutableBaseObject, ImmutableBaseObject


__all__: List[str] = [
    "ImmutableSetting",
    "SettingConverter",
    "SettingFactory",
    "SettingManager",
    "SettingModel",
    "SettingService",
]


class ImmutableSetting(ImmutableBaseObject):
    """
    An immutable class representing a setting.

    Attributes:
        name (str): The name of the setting.
        value (str): The value of the setting.
        created_at (datetime): The timestamp when the setting was created.
        icon (str): The icon of the setting.
        id (int): The ID of the setting.
        updated_at (datetime): The timestamp when the setting was last updated.
        uuid (str): The UUID of the setting.
    """

    def __init__(
        self,
        name: str,
        value: str,
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "⚙️",
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableSetting class.

        Args:
            name (str): The name of the setting.
            value (str): The value of the setting.
            created_at (Optional[datetime]): The timestamp when the setting was created.
            icon (Optional[str]): The icon of the setting. Defaults to "⚙️".
            id (Optional[int]): The ID of the setting.
            key (Optional[str]): The key of the setting.
            updated_at (Optional[datetime]): The timestamp when the setting was last updated.
            uuid (Optional[str]): The UUID of the setting.

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
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )

    def to_mutable(self) -> "Mutable":
        """
        Converts the immutable setting to a mutable setting.

        Returns:
            Mutable: The mutable setting.
        """

        # Convert the immutable setting to a mutable setting
        return Mutable(**self.to_dict(exclude=["_logger"]))


class Mutable(MutableBaseObject):
    """
    A mutable class representing a setting.

    Attributes:
        name (str): The name of the setting.
        value (str): The value of the setting.
        created_at (Optional[datetime]): The timestamp when the setting was created.
        icon (Optional[str]): The icon of the setting.
        id (Optional[int]): The ID of the setting.
        key (Optional[str]): The key of the setting.
        updated_at (Optional[datetime]): The timestamp when the setting was last updated.
        uuid (Optional[str]): The UUID of the setting.
    """

    def __init__(
        self,
        name: str,
        value: str,
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "⚙️",
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the Mutable class.

        Args:
            name (str): The name of the setting.
            value (str): The value of the setting.
            created_at (Optional[datetime]): The timestamp when the setting was created.
            icon (Optional[str]): The icon of the setting. Defaults to "⚙️".
            id (Optional[int]): The ID of the setting.
            key (Optional[str]): The key of the setting.
            updated_at (Optional[datetime]): The timestamp when the setting was last updated.
            uuid (Optional[str]): The UUID of the setting.

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
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )

    def to_immutable(self) -> ImmutableSetting:
        """
        Converts the mutable setting to an immutable setting.

        Returns:
            ImmutableSetting: The immutable setting.
        """

        # Convert the mutable setting to an immutable setting
        return ImmutableSetting(**self.to_dict(exclude=["_logger"]))


class SettingConverter:
    """
    A converter class for transforming between SettingModel and ImmutableSetting instances.

    This class provides methods to convert a SettingModel instance to an ImmutableSetting instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the SettingConverter class.
    """

    logger: Logger = Logger.get_logger(name="SettingConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "SettingModel",
    ) -> Optional[ImmutableSetting]:
        """
        Converts a given SettingModel instance to an ImmutableSetting instance.

        Args:
            model (SettingModel): The SettingModel instance to be converted.

        Returns:
            ImmutableSetting: The converted ImmutableSetting instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the SettingModel instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableSetting class from the dictionary representation of the SettingModel instance
            return ImmutableSetting(
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
        object: ImmutableSetting,
    ) -> Optional["SettingModel"]:
        """
        Converts a given ImmutableSetting instance to a SettingModel instance.

        Args:
            object (ImmutableSetting): The ImmutableSetting instance to be converted.

        Returns:
            SettingModel: The converted SettingModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ImmutableSetting instance.
        """
        try:
            # Attempt to create and return a new instance of the SettingModel class from the dictionary representation of the ImmutableSetting instance
            return SettingModel(**object.to_dict(exclude=["_logger"]))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'object_to_model' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class SettingFactory:
    """
    A factory class used to create instances of ImmutableSetting class.

    Attributes:
        logger (Logger): The logger instance associated with the object.
    """

    logger: Logger = Logger.get_logger(name="SettingFactory")

    @classmethod
    def create_setting(
        cls,
        name: str,
        value: str,
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "⚙️",
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutableSetting]:
        """
        Creates and returns a new instance of the ImmutableSetting class.

        Args:
            name (str): The name of the setting.
            value (str): The value of the setting.
            created_at (Optional[datetime]): The timestamp when the setting was created.
            icon (Optional[str]): The icon of the setting. Defaults to "⚙️".
            id (Optional[int]): The ID of the setting.
            key (Optional[str]): The key of the setting.
            updated_at (Optional[datetime]): The timestamp when the setting was last updated.
            uuid (Optional[str]): The UUID of the setting.

        Returns:
            ImmutableSetting: The created ImmutableSetting instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to create the ImmutableSetting instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableSetting class
            return ImmutableSetting(
                name=name,
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
                message=f"Caught an exception while attempting to run 'create_setting' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class SettingManager(BaseObjectManager):
    """
    A manager class for managing settings in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for settings.

    Attributes:
        cache: (List[Any]): The cache for storing settings.
        logger (Logger): The logger instance associated with the object.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the SettingManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def count_settings(self) -> int:
        """
        Returns the number of settings in the database.

        Returns:
            int: The number of settings in the database.
        """
        try:
            # Count the number of settings in the database
            result: Any = asyncio.run(
                SettingModel.execute(
                    database=Constants.DATABASE_PATH,
                    sql=f"SELECT COUNT(*) FROM {Constants.SETTINGS};",
                )
            )

            # Return the number of settings in the database
            return result[0][0] if result else 0
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_setting(
        self,
        setting: Union[ImmutableSetting, Mutable],
    ) -> Optional[ImmutableSetting]:
        """
        Creates a new setting in the database.

        Args:
            setting (Union[ImmutableSetting, Mutable]): The setting to be created.

        Returns:
            Optional[ImmutableSetting]: The newly created immutable setting if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the setting.
        """
        try:
            # Set the created_at timestamp of the setting
            setting.created_at = Miscellaneous.get_current_datetime()

            # Set the key of the setting
            setting.key = f"SETTING_{self.count_settings() + 1}"

            # Set the updated_at timestamp of the setting
            setting.updated_at = Miscellaneous.get_current_datetime()

            # Set the uuid of the setting
            setting.uuid = Miscellaneous.get_uuid()

            # Convert the setting object to a SettingModel object
            model: SettingModel = SettingConverter.object_to_model(object=setting)

            # Create a new setting in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            if id:
                # Set the ID of the setting
                setting.id = id

                # Convert the setting to an immutable setting
                setting = ImmutableSetting(**setting.to_dict(exclude=["_logger"]))

                # Add the setting to the cache
                self.add_to_cache(
                    key=setting.key,
                    value=setting,
                )

                # Return the newly created immutable setting
                return setting

            # Log a warning message indicating an error has occurred
            self.logger.warning(
                message=f"It seems that an error has occured while attempting to create a setting ({setting}) in the database."
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

    def delete_setting(
        self,
        setting: Union[ImmutableSetting, Mutable],
    ) -> bool:
        """
        Deletes a setting from the database.

        Args:
            setting (Union[ImmutableSetting, Mutable]): The setting to be deleted.

        Returns:
            bool: True if the setting was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the setting to an immutable setting and delete the setting from the database
            result: bool = asyncio.run(
                SettingConverter.object_to_model(
                    object=ImmutableSetting(**setting.to_dict(exclude=["_logger"]))
                ).delete()
            )

            # Return True if the setting was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all_settings(self) -> Optional[List[ImmutableSetting]]:
        """
        Returns a list of all settings in the database.

        Returns:
            Optional[List[ImmutableSetting]]: A list of all settings in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if cache and table size are equal
            if self.cache and len(self._cache) == self.count_settings():
                # Return the list of immutable settings from the cache
                return self.get_cache_values()

            # Get all settings from the database
            models: List[SettingModel] = asyncio.run(
                SettingModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of SettingModel objects to a list of ImmutableSetting objects
            settings: List[ImmutableSetting] = [
                ImmutableSetting(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable settings
            for setting in settings:
                if not self.is_key_in_cache(key=setting.key):
                    # Add the immutable setting to the cache
                    self.add_to_cache(
                        key=setting.key,
                        value=setting,
                    )
                else:
                    # Update the immutable setting in the cache
                    self.update_in_cache(
                        key=setting.key,
                        value=setting,
                    )

            # Return the list of immutable settings
            return settings
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_setting_by(
        self,
        field: str,
        value: Any,
    ) -> Optional[ImmutableSetting]:
        """
        Retrieves a setting by the given field and value.

        Args:
            field (str): The field to search by.
            value (Any): The value to search for.

        Returns:
            Optional[ImmutableSetting]: The setting with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the setting is already in the cache
            if self.is_key_in_cache(key=field):
                # Return the setting from the cache
                return self.get_value_from_cache(key=field)

            # Get the setting with the given field and value from the database
            model: Optional[SettingModel] = asyncio.run(
                SettingModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Return the setting if it exists
            if model is not None:
                # Convert the SettingModel object to an ImmutableSetting object
                return ImmutableSetting(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the setting does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_setting_by_id(
        self,
        id: int,
    ) -> Optional[ImmutableSetting]:
        """
        Returns a setting with the given ID.

        Args:
            id (int): The ID of the setting.

        Returns:
            Optional[ImmutableSetting]: The setting with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the setting is already in the cache
            if self.is_key_in_cache(key=f"SETTING_{id}"):
                # Return the setting from the cache
                return self.get_value_from_cache(key=f"SETTING_{id}")

            # Get the setting with the given ID from the database
            model: Optional[SettingModel] = asyncio.run(
                SettingModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the setting if it exists
            if model is not None:
                # Convert the SettingModel object to an ImmutableSetting object
                return ImmutableSetting(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the setting does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_setting_by_uuid(
        self,
        uuid: str,
    ) -> Optional[ImmutableSetting]:
        """
        Returns a setting with the given UUID.

        Args:
            uuid (str): The UUID of the setting.

        Returns:
            Optional[ImmutableSetting]: The setting with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the setting is already in the cache
            if self.is_key_in_cache(key=uuid):
                # Return the setting from the cache
                return self.get_value_from_cache(key=uuid)

            # Get the setting with the given UUID from the database
            model: Optional[SettingModel] = asyncio.run(
                SettingModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the setting if it exists
            if model is not None:
                # Convert the SettingModel object to an ImmutableSetting object
                return ImmutableSetting(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the setting does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def search_settings(
        self,
        **kwargs,
    ) -> Optional[Union[List[ImmutableSetting]]]:
        """
        Searches for settings in the database.

        Args:
            **kwargs: Any additional keyword arguments to be passed to the search method of the SettingModel class.

        Returns:
            Optional[Union[List[ImmutableSetting]]]: The found settings if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Search for settings in the database
            models: Optional[List[SettingModel]] = asyncio.run(
                SettingModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found settings if any
            if models is not None and len(models) > 0:
                return [
                    ImmutableSetting(
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
                # Return None indicating that no settings were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_setting(
        self,
        setting: Union[ImmutableSetting, Mutable],
    ) -> Optional[ImmutableSetting]:
        """
        Updates a setting with the given ID.

        Args:
            setting (Union[ImmutableSetting, Mutable]): The setting to update.

        Returns:
            Optional[ImmutableSetting]: The updated setting if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the setting to an immutable setting and update the setting in the database
            model: Optional[SettingModel] = asyncio.run(
                SettingConverter.object_to_model(
                    object=ImmutableSetting(**setting.to_dict(exclude=["_logger"]))
                ).update(
                    database=Constants.DATABASE_PATH,
                    **setting.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Return the updated setting if it exists
            if model is not None:
                # Convert the SettingModel object to an ImmutableSetting object
                setting = ImmutableSetting(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the setting to the cache
                self.update_in_cache(
                    key=setting.key,
                    value=setting,
                )

                # Return the updated setting
                return setting
            else:
                # Return None indicating that the setting does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class SettingModel(ImmutableBaseModel):
    """
    Represents the structure of a setting model.

    Attributes:
        created_at (Optional[datetime]): The timestamp when the setting was created.
        icon (Optional[str]): The icon of the setting. Defaults to "⚙️".
        id (Optional[int]): The ID of the setting.
        key (Optional[str]): The key of the setting.
        name (Optional[str]): The name of the setting.
        updated_at (Optional[datetime]): The timestamp when the setting was last updated.
        uuid (Optional[str]): The UUID of the setting.
        value (Optional[str]): The value of the setting.
    """

    table: str = Constants.SETTINGS

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
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
        value: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the SettingModel class.

        Args:
            created_at (Optional[datetime]): The timestamp when the setting was created.
            icon (Optional[str]): The icon of the setting. Defaults to "⚙️".
            id (Optional[int]): The ID of the setting.
            key (Optional[str]): The key of the setting.
            name (Optional[str]): The name of the setting.
            updated_at (Optional[datetime]): The timestamp when the setting was last updated.
            uuid (Optional[str]): The UUID of the setting.
            value (Optional[str]): The value of the setting.

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
            table=Constants.SETTINGS,
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )


class SettingService:
    """
    A class used to manage settings.

    This class provides methods to get, set, and remove settings. It utilizes a logger to capture and log messages.

    Attributes:
        logger (Logger): The logger instance associated with the SettingService class.
        default_manager (DefaultManager): The manager instance associated with the SettingService class.
        setting_manager (SettingManager): The manager instance associated with the SettingService class.
    """

    _shared_instance: Optional["SettingService"] = None

    def __new__(cls) -> "SettingService":
        """
        Creates and returns a new instance of the SettingService class.

        If the instance does not exist, creates a new one by calling the parent class constructor
        and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Returns:
            SettingService: The created or existing instance of SettingService class.
        """
        if cls._shared_instance is None:
            cls._shared_instance = super().__new__(cls)
            cls._shared_instance.init()
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes the SettingService instance.

        Initializes the SettingService instance by getting a logger with the name of the class.

        Returns:
            None
        """

        # Initialize the logger
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Initialize the default manager
        self.default_manager: DefaultManager = DefaultManager()

        # Initialize the setting manager
        self.setting_manager: SettingManager = SettingManager()

    def create_setting(
        self,
        name: str,
        value: str,
    ) -> Optional[ImmutableSetting]:
        """
        Creates a new setting with the given name and value in the database.

        Args:
            name (str): The name of the setting to create.
            value (str): The value of the setting to create.

        Returns:
            Optional[ImmutableSetting]: The newly created immutable setting if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the setting.
        """
        try:
            # Atttempt to create an ImmutableSetting object from the given name and value
            setting: ImmutableSetting = SettingFactory.create_setting(
                name=name,
                value=value,
            )

            # Store the ImmutableSetting in the database and return it
            return self.setting_manager.create_setting(setting=setting)

        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_setting' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def load_default(
        self,
        name: str,
    ) -> Optional[ImmutableSetting]:
        """
        Loads a default setting with the given name from the database.

        Args:
            name (str): The name of the default setting to load.

        Returns:
            Optional[ImmutableSetting]: The loaded immutable setting if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Attempt to load the default object from the database
            default: Optional[ImmutableDefault] = self.default_manager.get_default_by(
                field="name",
                value=name,
            )

            if not default:
                # Log a warning message indicating the default was not found
                self.logger.warning(message=f"Default with name '{name}' not found.")

                # Return None indicating the default was not found
                return None

            # Convert the default object to an immutable setting and return it
            return SettingFactory.create_setting(**default.to_dict(exclude=["_logger"]))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'load_default' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def load_setting(
        self,
        name: str,
    ) -> Optional[ImmutableSetting]:
        """
        Loads a setting with the given name from the database.

        Args:
            name (str): The name of the setting to load.

        Returns:
            Optional[ImmutableSetting]: The loaded immutable setting if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Attempt to load the setting from the database
            setting: Optional[ImmutableSetting] = self.setting_manager.get_setting_by(
                field="name",
                value=name,
            )

            if not setting:
                # Log a warning message indicating the setting was not found
                self.logger.warning(
                    message=f"ImmutableSetting with {field} = {value} not found."
                )

                # Return None indicating the setting was not found
                return None

            # Return the setting
            return setting
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'load_setting' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_setting(
        self,
        setting: Union[ImmutableSetting, Mutable],
    ) -> Optional[ImmutableSetting]:
        """
        Updates a given setting in the database.

        Args:
            setting (Union[ImmutableSetting, Mutable]): The setting to update.

        Returns:
            Optional[ImmutableSetting]: The updated immutable setting if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Update the setting in the database
            return self.setting_manager.update_setting(setting=setting)
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update_setting' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def on_request_setting_create(
        self,
        setting: ImmutableSetting,
    ) -> Optional[ImmutableSetting]:
        """
        Creates a new setting in the database.

        Args:
            setting (ImmutableSetting): The setting to create.

        Returns:
            Optional[ImmutableSetting]: The newly created immutable setting if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Create the setting in the database
            return self.setting_manager.create_setting(setting=setting)
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_setting_create' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def on_request_setting_delete(
        self,
        setting: ImmutableSetting,
    ) -> Optional[ImmutableSetting]:
        """
        Deletes a setting from the database.

        Args:
            setting (ImmutableSetting): The setting to delete.

        Returns:
            Optional[ImmutableSetting]: The deleted immutable setting if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Delete the setting from the database
            return self.setting_manager.delete_setting(setting=setting)
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_setting_delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def on_request_setting_load(self, **kwargs) -> Optional[List[ImmutableSetting]]:
        """
        Loads settings from the database.

        Args:
            **kwargs: Keyword arguments to be passed to the database query.

        Returns:
            Optional[List[ImmutableSetting]]: The loaded settings if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Load the settings from the database
            return self.setting_manager.get_setting_by(**kwargs)
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_setting_load' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def on_request_setting_update(
        self,
        setting: ImmutableSetting,
    ) -> Optional[ImmutableSetting]:
        """
        Updates an existing setting in the database.

        Args:
            setting (ImmutableSetting): The setting to update.

        Returns:
            Optional[ImmutableSetting]: The updated immutable setting if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Update the setting in the database
            return self.setting_manager.update_setting(setting=setting)
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_setting_update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None
