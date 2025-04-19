"""
Author: lodego
Date: 2025-02-06
"""

import asyncio

from datetime import datetime
from typing import *

from utils.constants import Constants
from utils.field import Field
from utils.logger import Logger
from utils.manager import BaseObjectManager
from utils.miscellaneous import Miscellaneous
from utils.model import ImmutableBaseModel
from utils.object import MutableBaseObject, ImmutableBaseObject


__all__: Final[List[str]] = [
    "ImmutableChangeHistory",
    "MutableChangeHistory",
    "ChangeHistoryConverter",
    "ChangeHistoryFactory",
    "ChangeHistoryManager",
    "ChangeHistoryModel",
    "ImmutableChangeHistoryItem",
    "MutableChangeHistoryItem",
    "ChangeHistoryItemConverter",
    "ChangeHistoryItemFactory",
    "ChangeHistoryItemManager",
    "ChangeHistoryItemModel",
]


class ImmutableChangeHistory(ImmutableBaseObject):
    """
    Represents an immutable change history.

    An immutable change history represents a log of the changes made to a mutable object.

    Attributes:
        source (Dict[str, Any]): The source of the change history.
        created_at (Optional[datetime]): The timestamp when the change history was created.
        icon (Optional[str]): The icon of the change history.
        id (Optional[int]): The ID of the change history.
        key (Optional[str]): The key of the change history.
        updated_at (Optional[datetime]): The timestamp when the change history was last updated.
        uuid (Optional[str]): The UUID of the change_history.
    """

    def __init__(
        self,
        source: Dict[str, Any],
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "🕒",
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableChangeHistory class.

        Args:
            source (Dict[str, Any]): The source of the change history.
            created_at (Optional[datetime]): The timestamp when the change history was created.
            icon (Optional[str]): The icon of the change history. Defaults to "🕒".
            id (Optional[int]): The ID of the change history.
            key (Optional[str]): The key of the change history.
            updated_at (Optional[datetime]): The timestamp when the change history was last updated.
            uuid (Optional[str]): The UUID of the change_history.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            icon=icon,
            id=id,
            key=key,
            source=source,
            updated_at=updated_at,
            uuid=uuid,
        )
    
    def to_mutable(self) -> Optional["MutableChangeHistory"]:
        """
        Converts the immutable change history to a mutable change history.

        Returns:
            Optional[MutableChangeHistory]: The mutable change history if no exception occurs. Otherwise, None.
        """
        try:
            # Attempt to create and return a new instance of the MutableChangeHistory class from the dictionary representation of the ImmutableChangeHistory instance
            return MutableChangeHistory(
                **self.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_mutable' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class MutableChangeHistory(MutableBaseObject):
    """
    Represents a mutable change history.

    A mutable change history represents a log of the changes made to a mutable object.

    Attributes:
        source (Dict[str, Any]): The source of the change history.
        created_at (Optional[datetime]): The timestamp when the change history was created.
        icon (Optional[str]): The icon of the change history.
        id (Optional[int]): The ID of the change history.
        key (Optional[str]): The key of the change history.
        updated_at (Optional[datetime]): The timestamp when the change history was last updated.
        uuid (Optional[str]): The UUID of the change_history.
    """

    def __init__(
        self,
        source: Dict[str, Any],
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "🕒",
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableChangeHistory class.

        Args:
            source (Dict[str, Any]): The source of the change history.
            created_at (Optional[datetime]): The timestamp when the change history was created.
            icon (Optional[str]): The icon of the change history. Defaults to "🕒".
            id (Optional[int]): The ID of the change history.
            key (Optional[str]): The key of the change history.
            updated_at (Optional[datetime]): The timestamp when the change history was last updated.
            uuid (Optional[str]): The UUID of the change_history.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            icon=icon,
            id=id,
            key=key,
            source=source,
            updated_at=updated_at,
            uuid=uuid,
        )
    
    def to_immutable(self) -> Optional[ImmutableChangeHistory]:
        """
        Converts the mutable change history to an immutable change history.

        Returns:
            Optional[ImmutableChangeHistory]: The immutable change history if no exception occurs. Otherwise, None.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableChangeHistory class from the dictionary representation of the MutableChangeHistory instance
            return ImmutableChangeHistory(
                **self.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_immutable' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class ChangeHistoryConverter:
    """
    A converter class for transforming between ChangeHistoryModel and ChangeHistory instances.

    This class provides methods to convert a ChangeHistoryModel instance to an ChangeHistory instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the ChangeHistoryConverter class.
    """

    logger: Final[Logger] = Logger.get_logger(name="ChangeHistoryConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "ChangeHistoryModel",
    ) -> Optional[ImmutableChangeHistory]:
        """
        Converts a given ChangeHistoryModel instance to an ChangeHistory instance.

        Args:
            model (ChangeHistoryModel): The ChangeHistoryModel instance to be converted.

        Returns:
            ChangeHistory: The converted ChangeHistory instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ChangeHistoryModel instance.
        """
        try:
            # Attempt to create and return a new instance of the ChangeHistory class from the dictionary representation of the ChangeHistoryModel instance
            return Immutable(
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
        object: ImmutableChangeHistory,
    ) -> Optional["ChangeHistoryModel"]:
        """
        Converts a given ChangeHistory instance to a ChangeHistoryModel instance.

        Args:
            object (ChangeHistory): The ChangeHistory instance to be converted.

        Returns:
            ChangeHistoryModel: The converted ChangeHistoryModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ChangeHistory instance.
        """
        try:
            # Attempt to create and return a new instance of the ChangeHistoryModel class from the dictionary representation of the ChangeHistory instance
            return ChangeHistoryModel(
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


class ChangeHistoryFactory:
    logger: Final[Logger] = Logger.get_logger(name="ChangeHistoryFactory")

    @classmethod
    def create_change_history(
        cls,
        source: Dict[str, Any],
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "🕒",
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutableChangeHistory]:
        """
        Creates and returns a new instance of ChangeHistory class.

        Args:
            source (Dict[str, Any]): The source of the change_history.
            created_at (Optional[datetime]): The timestamp when the change history was created.
            icon (Optional[str]): The icon of the change_history. Defaults to "🕒".
            id (Optional[int]): The ID of the change_history.
            key (Optional[str]): The key of the change_history.
            updated_at (Optional[datetime]): The timestamp when the change history was last updated.
            uuid (Optional[str]): The UUID of the change_history.

        Returns:
            Optional[ChangeHistory]: The created change history object if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the change_history.
        """
        try:
            return Immutable(
                source=source,
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
                message=f"Caught an exception while attempting to run 'create_change_history' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class ChangeHistoryManager(BaseObjectManager):
    """
    A manager class for managing change histories in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for change histories.

    Attributes:
        cache: (List[Any]): The cache for storing change histories.
        logger (Logger): The logger instance associated with the object.
    """

    _shared_instance: Optional["ChangeHistoryManager"] = None

    def __new__(cls) -> "ChangeHistoryManager":
        """
        Creates and returns a new instance of the ChangeHistoryManager class.

        If the instance does not exist, creates a new one by calling the parent class
        constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Returns:
            ChangeHistoryManager: The created or existing instance of ChangeHistoryManager class.
        """
        
        # Check if the shared instance does not exist
        if cls._shared_instance is None:
            # Create a new instance by calling the parent class constructor
            cls._shared_instance = super(ChangeHistoryManager, cls).__new__(cls)
            # Initialize the instance
            cls._shared_instance.init()
        
        # Return the shared instance
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes a new instance of the ChangeHistoryManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def count_change_history_items(self) -> int:
        """
        Returns the number of change histories in the database.

        Returns:
            int: The number of change histories in the database.
        """
        try:
            # Count the number of change histories in the database
            result: Any = asyncio.run(
                ChangeHistoryModel.execute(
                    database=Constants.DATABASE_PATH,
                    sql=f"SELECT COUNT(*) FROM {Constants.CHANGE_HISTORIES};",
                )
            )

            # Return the number of change histories in the database
            return result[0][0] if result else 0
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_change_history_item(
        self,
        change_history: Union[ImmutableChangeHistory, MutableChangeHistory],
    ) -> Optional[ImmutableChangeHistory]:
        """
        Creates a new change history in the database.

        Args:
            change history (Union[ChangeHistory, ChangeHistory]): The change history to be created.

        Returns:
            Optional[ChangeHistory]: The newly created immutable change history if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the change_history.
        """
        try:
            # Check if the change history object is immutable
            if isinstance(
                change_history,
                ImmutableChangeHistory,
            ):
                # If it is, convert it to a mutable change history
                change_history = change_history.to_mutable(
                    **change_history.to_dict(
                        exclude=[
                            "_logger",
                        ]
                    )
                )

            # Set the created_at timestamp of the change history
            change_history.created_at = Miscellaneous.get_current_datetime()

            # Set the key of the change history
            change_history.key = (
                f"CHANGE_HISTORY_{self.count_change_history_items() + 1}"
            )

            # Set the updated_at timestamp of the change history
            change_history.updated_at = Miscellaneous.get_current_datetime()

            # Set the uuid of the change history
            change_history.uuid = Miscellaneous.get_uuid()

            # Convert the change history object to a ChangeHistoryModel object
            model: ChangeHistoryModel = ChangeHistoryConverter.object_to_model(
                object=change_history
            )

            # Create a new change history in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            if id:
                # Set the ID of the change history
                change_history.id = id

                # Convert the change history to an immutable change history
                change_history = Immutable(
                    **change_history.to_dict(
                        exclude=[
                            "_logger",
                        ]
                    )
                )

                # Add the change history to the cache
                self.add_to_cache(
                    key=change_history.key,
                    value=change_history,
                )

                # Return the newly created immutable change history
                return change_history

            # Log a warning message indicating an error has occurred
            self.logger.warning(
                message=f"It seems that an error has occured while attempting to create a change history ({change_history}) in the database."
            )

            # Return None indicating an error has occurred
            return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_change history' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete_change_history(
        self,
        change_history: Union[ImmutableChangeHistory, MutableChangeHistory],
    ) -> bool:
        """
        Deletes a change history from the database.

        Args:
            change history (Union[ChangeHistory, ChangeHistory]): The change history to be deleted.

        Returns:
            bool: True if the change history was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the change history to an immutable change history and delete the change history from the database
            result: bool = asyncio.run(
                ChangeHistoryConverter.object_to_model(
                    object=Immutable(
                        **change_history.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).delete()
            )

            # Return True if the change history was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all_change_history_items(self) -> Optional[List[ImmutableChangeHistory]]:
        """
        Returns a list of all change histories in the database.

        Returns:
            Optional[List[ChangeHistory]]: A list of all change histories in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if cache and table size are equal
            if self.cache and len(self._cache) == self.count_change_history_items():
                # Return the list of immutable change histories from the cache
                return self.get_cache_values()

            # Get all change histories from the database
            models: List[ChangeHistoryModel] = asyncio.run(
                ChangeHistoryModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of ChangeHistoryModel objects to a list of ChangeHistory objects
            change_histories: List[ChangeHistory] = [
                Immutable(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable change histories
            for change_history in change_histories:
                if not self.is_key_in_cache(key=change_history.key):
                    # Add the immutable change history to the cache
                    self.add_to_cache(
                        key=change_history.key,
                        value=change_history,
                    )
                else:
                    # Update the immutable change history in the cache
                    self.update_in_cache(
                        key=change_history.key,
                        value=change_history,
                    )

            # Return the list of immutable change histories
            return change_histories
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_change_history_by(
        self,
        field: str,
        value: Any,
    ) -> Optional[ImmutableChangeHistory]:
        """
        Retrieves a change history by the given field and value.

        Args:
            field (str): The field to search by.
            value (Any): The value to search for.

        Returns:
            Optional[ChangeHistory]: The change history with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the change history is already in the cache
            if self.is_key_in_cache(key=field):
                # Return the change history from the cache
                return self.get_value_from_cache(key=field)

            # Get the change history with the given field and value from the database
            model: Optional[ChangeHistoryModel] = asyncio.run(
                ChangeHistoryModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Return the change history if it exists
            if model is not None:
                # Convert the ChangeHistoryModel object to an ChangeHistory object
                return Immutable(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the change history does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_change_history_by_id(
        self,
        id: int,
    ) -> Optional[ImmutableChangeHistory]:
        """
        Returns a change history with the given ID.

        Args:
            id (int): The ID of the change_history.

        Returns:
            Optional[ChangeHistory]: The change history with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the change history is already in the cache
            if self.is_key_in_cache(key=f"CHANGE_HISTORY_{id}"):
                # Return the change history from the cache
                return self.get_value_from_cache(key=f"CHANGE_HISTORY_{id}")

            # Get the change history with the given ID from the database
            model: Optional[ChangeHistoryModel] = asyncio.run(
                ChangeHistoryModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the change history if it exists
            if model is not None:
                # Convert the ChangeHistoryModel object to an ChangeHistory object
                return ChangeHistory(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the change history does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_change_history_by_uuid(
        self,
        uuid: str,
    ) -> Optional[ImmutableChangeHistory]:
        """
        Returns a change history with the given UUID.

        Args:
            uuid (str): The UUID of the change_history.

        Returns:
            Optional[ImmutableChangeHistory]: The change history with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the change history is already in the cache
            if self.is_key_in_cache(key=uuid):
                # Return the change history from the cache
                return self.get_value_from_cache(key=uuid)

            # Get the change history with the given UUID from the database
            model: Optional[ChangeHistoryModel] = asyncio.run(
                ChangeHistoryModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the change history if it exists
            if model is not None:
                # Convert the ChangeHistoryModel object to an ImmutableChangeHistory object
                return ImmutableChangeHistory(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the change history does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def search_change_histories(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[Union[List[ImmutableChangeHistory]]]:
        """
        Searches for change histories in the database.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            **kwargs: Any additional keyword arguments to be passed to the search method of the ChangeHistoryModel class.

        Returns:
            Optional[Union[List[ImmutableChangeHistory]]]: The found change histories if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Search the stack for the passed keyword arguments
                cached_result: Optional[List[ImmutableChangeHistory]] = self.search_cache(**kwargs)

                # Check, if any cached results exist
                if cached_result:
                    # Return the cached results
                    return cached_result

            # Search for change histories in the database
            models: Optional[List[ChangeHistoryModel]] = asyncio.run(
                ChangeHistoryModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found change histories if any
            if models is not None and len(models) > 0:
                return [
                    ImmutableChangeHistory(
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
                # Return None indicating that no change histories were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_change_history(
        self,
        change_history: Union[ImmutableChangeHistory, MutableChangeHistory],
    ) -> Optional[ImmutableChangeHistory]:
        """
        Updates a change history with the given ID.

        Args:
            change history (Union[ImmutableChangeHistory, MutableChangeHistory]): The change history to update.

        Returns:
            Optional[ImmutableChangeHistory]: The updated change history if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the change history to an immutable change history and update the change history in the database
            model: Optional[ChangeHistoryModel] = asyncio.run(
                ChangeHistoryConverter.object_to_model(
                    object=ImmutableChangeHistory(
                        **change_history.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).update(
                    database=Constants.DATABASE_PATH,
                    **change_history.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Return the updated change history if it exists
            if model is not None:
                # Convert the ChangeHistoryModel object to an ImmutableChangeHistory object
                change_history = ImmutableChangeHistory(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the change history to the cache
                self.update_in_cache(
                    key=change_history.key,
                    value=change_history,
                )

                # Return the updated change history
                return change_history
            else:
                # Return None indicating that the change history does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class ChangeHistoryModel(ImmutableBaseModel):
    """
    Represents the structure of a change history model.

    A change history model represents a change made to a mutable object.

    Attributes:
        id (Field): The ID field of the change_history.
        created_at (Field): The timestamp when the change history was created.
        icon (Field): The icon of the change_history. Defaults to "🕒".
        key (Field): The key of the change_history.
        source (Field): The source of the change_history.
        updated_at (Field): The timestamp when the change history was last updated.
        uuid (Field): The UUID of the change_history.
    """

    table: Final[str] = Constants.CHANGE_HISTORIES

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
        default="🕒",
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

    source: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="source",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
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
        icon: Optional[str] = "🕒",
        id: Optional[int] = None,
        key: Optional[str] = None,
        source: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ChangeHistoryModel class.

        Args:
            created_at (Optional[datetime]): The timestamp when the change history was created.
            icon (Optional[str]): The icon of the change_history. Defaults to "🕒".
            id (Optional[int]): The ID of the change_history.
            key (Optional[str]): The key of the change_history.
            source (Optional[Dict[str, Any]]): The source of the change_history.
            updated_at (Optional[datetime]): The timestamp when the change history was last updated.
            uuid (Optional[str]): The UUID of the change_history.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            icon="🕒",
            id=id,
            key=key,
            source=source,
            table=Constants.CHANGE_HISTORIES,
            updated_at=updated_at,
            uuid=uuid,
        )


class ImmutableChangeHistoryItem(ImmutableBaseObject):
    """
    Represents an immutable change history item.

    A change history item represents a change made to a mutable object.

    Attributes:
        from_ (Any): The original value of the item.
        to (Any): The new value of the item.
        created_at (Optional[datetime]): The timestamp when the item was created.
        icon (Optional[str]): The icon of the item.
        id (Optional[int]): The ID of the item.
        key (Optional[str]): The key of the item.
        updated_at (Optional[datetime]): The timestamp when the item was last updated.
        uuid (Optional[str]): The UUID of the item.
    """

    def __init__(
        self,
        from_: Any,
        to: Any,
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "🕒",
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableChangeHistoryItem class.

        Args:
            from_ (Any): The original value of the item.
            to (Any): The new value of the item.
            created_at (Optional[datetime]): The timestamp when the item was created.
            icon (Optional[str]): The icon of the item. Defaults to "🕒".
            id (Optional[int]): The ID of the item.
            key (Optional[str]): The key of the item.
            updated_at (Optional[datetime]): The timestamp when the item was last updated.
            uuid (Optional[str]): The UUID of the item.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            from_=from_,
            icon=icon,
            id=id,
            key=key,
            to=to,
            updated_at=updated_at,
            uuid=uuid,
        )
    
    def to_mutable(self) -> Optional["MutableChangeHistoryItem"]:
        """
        Converts the immutable change history item to a mutable change history item.

        Returns:
            Optional[MutableChangeHistoryItem]: The mutable change history item if no exception occurs. Otherwise, None.
        """
        try:
            # Attempt to create and return a new instance of the MutableChangeHistoryItem class from the dictionary representation of the ImmutableChangeHistoryItem instance
            return MutableChangeHistoryItem(
                **self.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_mutable' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class MutableChangeHistoryItem(MutableBaseObject):
    """
    Represents a mutable change history item.

    A change history item represents a change made to a mutable object.

    Attributes:
        from_ (Any): The original value of the item.
        to (Any): The new value of the item.
        created_at (Optional[datetime]): The timestamp when the item was created.
        icon (Optional[str]): The icon of the item.
        id (Optional[int]): The ID of the item.
        key (Optional[str]): The key of the item.
        updated_at (Optional[datetime]): The timestamp when the item was last updated.
        uuid (Optional[str]): The UUID of the item.
    """

    def __init__(
        self,
        from_: Any,
        to: Any,
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "🕒",
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableChangeHistoryItem class.

        Args:
            from_ (Any): The original value of the item.
            to (Any): The new value of the item.
            created_at (Optional[datetime]): The timestamp when the item was created.
            icon (Optional[str]): The icon of the item. Defaults to "🕒".
            id (Optional[int]): The ID of the item.
            key (Optional[str]): The key of the item.
            updated_at (Optional[datetime]): The timestamp when the item was last updated.
            uuid (Optional[str]): The UUID of the item.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            from_=from_,
            icon=icon,
            id=id,
            key=key,
            to=to,
            updated_at=updated_at,
            uuid=uuid,
        )
    
    def to_immutable(self) -> Optional[ImmutableChangeHistoryItem]:
        """
        Converts the mutable change history item to an immutable change history item.

        Returns:
            Optional[ImmutableChangeHistoryItem]: The immutable change history item if no exception occurs. Otherwise, None.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableChangeHistoryItem class from the dictionary representation of the MutableChangeHistoryItem instance
            return ImmutableChangeHistoryItem(
                **self.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_immutable' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class ChangeHistoryItemConverter:
    """
    A converter class for transforming between ChangeHistoryItemModel and ImmutableChangeHistoryItem instances.

    This class provides methods to convert a ChangeHistoryItemModel instance to an ImmutableChangeHistoryItem instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the ChangeHistoryItemConverter class.
    """

    logger: Final[Logger] = Logger.get_logger(name="ChangeHistoryItemConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "ChangeHistoryItemModel",
    ) -> Optional[ImmutableChangeHistoryItem]:
        """
        Converts a given ChangeHistoryItemModel instance to an ImmutableChangeHistoryItem instance.

        Args:
            model (ChangeHistoryItemModel): The ChangeHistoryItemModel instance to be converted.

        Returns:
            ImmutableChangeHistoryItem: The converted ImmutableChangeHistoryItem instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ChangeHistoryItemModel instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableChangeHistoryItem class from the dictionary representation of the ChangeHistoryItemModel instance
            return ImmutableChangeHistoryItem(
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
        object: ImmutableChangeHistoryItem,
    ) -> Optional["ChangeHistoryItemModel"]:
        """
        Converts a given ImmutableChangeHistoryItem instance to a ChangeHistoryItemModel instance.

        Args:
            object (ImmutableChangeHistoryItem): The ImmutableChangeHistoryItem instance to be converted.

        Returns:
            ChangeHistoryItemModel: The converted ChangeHistoryItemModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ImmutableChangeHistoryItem instance.
        """
        try:
            # Attempt to create and return a new instance of the ChangeHistoryItemModel class from the dictionary representation of the ImmutableChangeHistoryItem instance
            return ChangeHistoryItemModel(
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


class ChangeHistoryItemFactory:
    """
    A factory class used to create instances of ImmutableChangeHistoryItem class.

    Attributes:
        logger (Logger): The logger instance associated with the object.
    """

    logger: Final[Logger] = Logger.get_logger(name="ChangeHistoryItemFactory")

    @classmethod
    def create_change_history_item(
        cls,
        from_: Any,
        to: Any,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutableChangeHistoryItem]:
        """
        Creates and returns a new instance of ImmutableChangeHistoryItem class.

        Args:
            from_ (Any): The original value of the item.
            to (Any): The new value of the item.
            created_at (Optional[datetime]): The timestamp when the item was created.
            id (Optional[int]): The ID of the item.
            key (Optional[str]): The key of the item.
            updated_at (Optional[datetime]): The timestamp when the item was last updated.
            uuid (Optional[str]): The UUID of the item.

        Returns:
            Optional[ImmutableChangeHistoryItem]: The new instance of ImmutableChangeHistoryItem class.

        Raises:
            Exception: If an exception occurs while creating the item.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableChangeHistoryItem class
            return ImmutableChangeHistoryItem(
                from_=from_,
                to=to,
                created_at=created_at,
                id=id,
                key=key,
                updated_at=updated_at,
                uuid=uuid,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_change_history_item' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class ChangeHistoryItemManager(BaseObjectManager):
    """
    A manager class for managing change histories in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for change histories.

    Attributes:
        cache: (List[Any]): The cache for storing change histories.
        logger (Logger): The logger instance associated with the object.
    """

    _shared_instance: Optional["ChangeHistoryItemManager"] = None

    def __new__(cls) -> "ChangeHistoryItemManager":
        """
        Creates and returns a new instance of the ChangeHistoryItemManager class.

        If the instance does not exist, creates a new one by calling the parent class
        constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Returns:
            ChangeHistoryItemManager: The created or existing instance of ChangeHistoryItemManager class.
        """
        
        # Check if the shared instance does not exist
        if cls._shared_instance is None:
            # Create a new instance by calling the parent class constructor
            cls._shared_instance = super(ChangeHistoryItemManager, cls).__new__(cls)
            # Initialize the instance
            cls._shared_instance.init()
        
        # Return the shared instance
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes a new instance of the ChangeHistoryItemManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def count_change_history_items(self) -> int:
        """
        Returns the number of change histories in the database.

        Returns:
            int: The number of change histories in the database.
        """
        try:
            # Count the number of change histories in the database
            result: Any = asyncio.run(
                ChangeHistoryItemModel.execute(
                    database=Constants.DATABASE_PATH,
                    sql=f"SELECT COUNT(*) FROM {Constants.CHANGE_HISTORIES};",
                )
            )

            # Return the number of change histories in the database
            return result[0][0] if result else 0
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_change_history_item(
        self,
        change_history_item: Union[ImmutableChangeHistoryItem, MutableChangeHistoryItem],
    ) -> Optional[ImmutableChangeHistoryItem]:
        """
        Creates a new change history item in the database.

        Args:
            change history item (Union[ImmutableChangeHistoryItem, MutableChangeHistoryItem]): The change history item to be created.

        Returns:
            Optional[ImmutableChangeHistoryItem]: The newly created immutable change history item if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the change_history_item.
        """
        try:
            # Check if the change history item object is immutable
            if isinstance(
                change_history_item,
                MutableChangeHistoryItem,
            ):
                # If it is, convert it to a mutable change history item
                change_history_item = change_history_item.to_mutable()

            # Set the created_at timestamp of the change history item
            change_history_item.created_at = Miscellaneous.get_current_datetime()

            # Set the key of the change history item
            change_history_item.key = (
                f"CHANGE_HISTORY_ITEM_{self.count_change_history_items() + 1}"
            )

            # Set the updated_at timestamp of the change history item
            change_history_item.updated_at = Miscellaneous.get_current_datetime()

            # Set the uuid of the change history item
            change_history_item.uuid = Miscellaneous.get_uuid()

            # Convert the change history item object to a ChangeHistoryItemModel object
            model: ChangeHistoryItemModel = ChangeHistoryItemConverter.object_to_model(
                object=change_history_item
            )

            # Create a new change history item in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            if id:
                # Set the ID of the change history item
                change_history_item.id = id

                # Convert the change history item to an immutable change history item
                change_history_item = ImmutableChangeHistoryItem(
                    **change_history_item.to_dict(
                        exclude=[
                            "_logger",
                        ]
                    )
                )

                # Add the change history item to the cache
                self.add_to_cache(
                    key=change_history_item.key,
                    value=change_history_item,
                )

                # Return the newly created immutable change history item
                return change_history_item

            # Log a warning message indicating an error has occurred
            self.logger.warning(
                message=f"It seems that an error has occured while attempting to create a change history item ({change_history_item}) in the database."
            )

            # Return None indicating an error has occurred
            return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_change history item' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete_change_history_item(
        self,
        change_history_item: Union[ImmutableChangeHistoryItem, MutableChangeHistoryItem],
    ) -> bool:
        """
        Deletes a change history item from the database.

        Args:
            change history item (Union[ImmutableChangeHistoryItem, MutableChangeHistoryItem]): The change history item to be deleted.

        Returns:
            bool: True if the change history item was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the change history item to an immutable change history item and delete the change history item from the database
            result: bool = asyncio.run(
                ChangeHistoryItemConverter.object_to_model(
                    object=ImmutableChangeHistoryItem(
                        **change_history_item.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).delete()
            )

            # Return True if the change history item was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all_change_history_items(self) -> Optional[List[ImmutableChangeHistoryItem]]:
        """
        Returns a list of all change histories in the database.

        Returns:
            Optional[List[ImmutableChangeHistoryItem]]: A list of all change histories in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if cache and table size are equal
            if self.cache and len(self._cache) == self.count_change_histories():
                # Return the list of immutable change histories from the cache
                return self.get_cache_values()

            # Get all change histories from the database
            models: List[ChangeHistoryItemModel] = asyncio.run(
                ChangeHistoryItemModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of ChangeHistoryItemModel objects to a list of ImmutableChangeHistoryItem objects
            change_histories: List[ImmutableChangeHistoryItem] = [
                ImmutableChangeHistoryItem(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable change histories
            for change_history_item in change_histories:
                if not self.is_key_in_cache(key=change_history_item.key):
                    # Add the immutable change history item to the cache
                    self.add_to_cache(
                        key=change_history_item.key,
                        value=change_history_item,
                    )
                else:
                    # Update the immutable change history item in the cache
                    self.update_in_cache(
                        key=change_history_item.key,
                        value=change_history_item,
                    )

            # Return the list of immutable change histories
            return change_histories
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_change_history_item_by(
        self,
        field: str,
        value: Any,
    ) -> Optional[ImmutableChangeHistoryItem]:
        """
        Retrieves a change history item by the given field and value.

        Args:
            field (str): The field to search by.
            value (Any): The value to search for.

        Returns:
            Optional[ImmutableChangeHistoryItem]: The change history item with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the change history item is already in the cache
            if self.is_key_in_cache(key=field):
                # Return the change history item from the cache
                return self.get_value_from_cache(key=field)

            # Get the change history item with the given field and value from the database
            model: Optional[ChangeHistoryItemModel] = asyncio.run(
                ChangeHistoryItemModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Return the change history if it exists
            if model is not None:
                # Convert the ChangeHistoryItemModel object to an ImmutableChangeHistoryItem object
                return ImmutableChangeHistoryItem(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the change history does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_change_history_item_by_id(
        self,
        id: int,
    ) -> Optional[ImmutableChangeHistoryItem]:
        """
        Returns a change history item with the given ID.

        Args:
            id (int): The ID of the change_history_item.

        Returns:
            Optional[ImmutableChangeHistoryItem]: The change history item with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the change history item is already in the cache
            if self.is_key_in_cache(key=f"CHANGE_HISTORY_ITEM_{id}"):
                # Return the change history item from the cache
                return self.get_value_from_cache(key=f"CHANGE_HISTORY_ITEM_{id}")

            # Get the change history item with the given ID from the database
            model: Optional[ChangeHistoryItemModel] = asyncio.run(
                ChangeHistoryItemModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the change history item if it exists
            if model is not None:
                # Convert the ChangeHistoryItemModel object to an ImmutableChangeHistoryItem object
                return ImmutableChangeHistoryItem(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the change history item does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_change_history_item_by_uuid(
        self,
        uuid: str,
    ) -> Optional[ImmutableChangeHistoryItem]:
        """
        Returns a change history item with the given UUID.

        Args:
            uuid (str): The UUID of the change_history_item.

        Returns:
            Optional[ImmutableChangeHistoryItem]: The change history item with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the change history item is already in the cache
            if self.is_key_in_cache(key=uuid):
                # Return the change history item from the cache
                return self.get_value_from_cache(key=uuid)

            # Get the change history item with the given UUID from the database
            model: Optional[ChangeHistoryItemModel] = asyncio.run(
                ChangeHistoryItemModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the change history item if it exists
            if model is not None:
                # Convert the ChangeHistoryItemModel object to an ImmutableChangeHistoryItem object
                return ImmutableChangeHistoryItem(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the change history item does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def search_change_history_items(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[Union[List[ImmutableChangeHistoryItem]]]:
        """
        Searches for change history items in the database.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            **kwargs: Any additional keyword arguments to be passed to the search method of the ChangeHistoryItemModel class.

        Returns:
            Optional[Union[List[ImmutableChangeHistoryItem]]]: The found change history items if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Search the stack for the passed keyword arguments
                cached_result: Optional[List[ImmutableChangeHistoryItem]] = self.search_cache(**kwargs)

                # Check, if any cached results exist
                if cached_result:
                    # Return the cached results
                    return cached_result

            # Search for change history items in the database
            models: Optional[List[ChangeHistoryItemModel]] = asyncio.run(
                ChangeHistoryItemModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found change history items if any
            if models is not None and len(models) > 0:
                return [
                    ImmutableChangeHistoryItem(
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
                # Return None indicating that no change histories were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_change_history_item(
        self,
        change_history_item: Union[ImmutableChangeHistoryItem, MutableChangeHistoryItem],
    ) -> Optional[ImmutableChangeHistoryItem]:
        """
        Updates a change history item with the given ID.

        Args:
            change history item (Union[ImmutableChangeHistoryItem, MutableChangeHistoryItem]): The change history item to update.

        Returns:
            Optional[ImmutableChangeHistoryItem]: The updated change history item if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the change history item to an immutable change history item and update the change history item in the database
            model: Optional[ChangeHistoryItemModel] = asyncio.run(
                ChangeHistoryItemConverter.object_to_model(
                    object=ImmutableChangeHistoryItem(
                        **change_history_item.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).update(
                    database=Constants.DATABASE_PATH,
                    **change_history_item.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Return the updated change history item if it exists
            if model is not None:
                # Convert the ChangeHistoryItemModel object to an ImmutableChangeHistoryItem object
                change_history_item = ImmutableChangeHistoryItem(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                        ]
                    )
                )

                # Add the change history item to the cache
                self.update_in_cache(
                    key=change_history_item.key,
                    value=change_history_item,
                )

                # Return the updated change history item
                return change_history_item
            else:
                # Return None indicating that the change history item does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class ChangeHistoryItemModel(ImmutableBaseModel):
    """
    Represents the structure of a change history item model.

    A change history item model represents a change made to a mutable object.

    Attributes:
        created_at (Optional[datetime]): The timestamp when the item was created.
        from_ (Optional[Any]): The original value of the item.
        icon (Optional[str]): The icon of the item. Defaults to "🕒".
        id (Optional[int]): The ID of the item.
        key (Optional[Any]): The key of the item.
        source (Optional[Dict[str, Any]]): The source of the item.
        to (Optional[Any]): The new value of the item.
        updated_at (Optional[datetime]): The timestamp when the item was last updated.
        uuid (Optional[str]): The UUID of the item.
    """

    table: Final[str] = Constants.CHANGE_HISTORY_ITEMS

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

    from_: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="from_",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=False,
    )

    icon: Field = Field(
        autoincrement=False,
        default="🕒",
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

    source: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="source",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
        unique=False,
    )

    to: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="to",
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
        from_: Optional[Any] = None,
        icon: Optional[str] = "🕒",
        id: Optional[int] = None,
        key: Optional[Any] = None,
        source: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ChangeHistoryItem class.

        Args:
            created_at (Optional[datetime]): The timestamp when the item was created.
            from_ (Optional[Any]): The original value of the item.
            icon (Optional[str]): The icon of the item. Defaults to "🕒".
            id (Optional[int]): The ID of the item.
            key (Optional[Any]): The key of the item.
            source (Optional[Dict[str, Any]]): The source of the item.
            updated_at (Optional[datetime]): The timestamp when the item was last updated.
            uuid (Optional[str]): The UUID of the item.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            from_=from_,
            icon="🕒",
            id=id,
            key=key,
            source=source,
            table=Constants.CHANGE_HISTORY_ITEMS,
            updated_at=updated_at,
            uuid=uuid,
        )
