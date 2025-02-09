"""
Author: lodego
Date: 2025-02-06
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
    "ChangeHistory",
    "ChangeHistoryConverter",
    "ChangeHistoryFactory",
    "ChangeHistoryManager",
    "ChangeHistoryModel",
    "ChangeHistoryItem",
    "ChangeHistoryItemConverter",
    "ChangeHistoryItemFactory",
    "ChangeHistoryItemManager",
    "ChangeHistoryItemModel",
]


class ChangeHistory(ImmutableBaseObject):
    """
    Represents a change_history.

    A change history represents a log of the changes made to a mutable object.

    Attributes:
        source (Dict[str, Any]): The source of the change_history.
        created_at (Optional[datetime]): The timestamp when the change history was created.
        id (Optional[int]): The ID of the change_history.
        key (Optional[str]): The key of the change_history.
        updated_at (Optional[datetime]): The timestamp when the change history was last updated.
        uuid (Optional[str]): The UUID of the change_history.
    """

    def __init__(
        self,
        source: Dict[str, Any],
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ChangeHistory class.

        Args:
            source (Dict[str, Any]): The source of the change_history.
            created_at (Optional[datetime]): The timestamp when the change history was created.
            id (Optional[int]): The ID of the change_history.
            key (Optional[str]): The key of the change_history.
            updated_at (Optional[datetime]): The timestamp when the change history was last updated.
            uuid (Optional[str]): The UUID of the change_history.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            id=id,
            key=key,
            source=source,
            updated_at=updated_at,
            uuid=uuid,
        )


class ChangeHistoryConverter:
    """
    A converter class for transforming between ChangeHistoryModel and ChangeHistory instances.

    This class provides methods to convert a ChangeHistoryModel instance to an ChangeHistory instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the ChangeHistoryConverter class.
    """

    logger: Logger = Logger.get_logger(name="ChangeHistoryConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "ChangeHistoryModel",
    ) -> Optional[ChangeHistory]:
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
            return ChangeHistory(**model.to_dict(exclude=["_logger"]))
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
        object: ChangeHistory,
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
            return ChangeHistoryModel(**object.to_dict(exclude=["_logger"]))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'object_to_model' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class ChangeHistoryFactory:
    logger: Logger = Logger.get_logger(name="ChangeHistoryFactory")

    @classmethod
    def create_change_history(
        cls,
        source: Dict[str, Any],
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ChangeHistory]:
        """
        Creates and returns a new instance of ChangeHistory class.

        Args:
            source (Dict[str, Any]): The source of the change_history.
            created_at (Optional[datetime]): The timestamp when the change history was created.
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
            return ChangeHistory(
                source=source,
                created_at=created_at,
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

    def __init__(self) -> None:
        """
        Initializes a new instance of the ChangeHistoryManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def count(self) -> int:
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

    def create(
        self,
        change_history: Union[ChangeHistory, ChangeHistory],
    ) -> Optional[ChangeHistory]:
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
                ChangeHistory,
            ):
                # If it is, convert it to a mutable change history
                change_history = ChangeHistory(
                    **change_history.to_dict(exclude=["_logger"])
                )

            # Set the created_at timestamp of the change history
            change_history.created_at = Miscellaneous.get_current_datetime()

            # Set the key of the change history
            change_history.key = f"CHANGE_HISTORY_{self.count() + 1}"

            # Set the updated_at timestamp of the change history
            change_history.updated_at = Miscellaneous.get_current_datetime()

            # Set the uuid of the change history
            change_history.uuid = str(uuid.uuid4())

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
                change_history = ChangeHistory(
                    **change_history.to_dict(exclude=["_logger"])
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

    def delete(
        self,
        change_history: Union[ChangeHistory, ChangeHistory],
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
                    object=ChangeHistory(**change_history.to_dict(exclude=["_logger"]))
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

    def get_all(self) -> Optional[List[ChangeHistory]]:
        """
        Returns a list of all change histories in the database.

        Returns:
            Optional[List[ChangeHistory]]: A list of all change histories in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if cache and table size are equal
            if self.cache and len(self._cache) == self.count():
                # Return the list of immutable change histories from the cache
                return self.get_cache_values()

            # Get all change histories from the database
            models: List[ChangeHistoryModel] = asyncio.run(
                ChangeHistoryModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of ChangeHistoryModel objects to a list of ChangeHistory objects
            change_histories: List[ChangeHistory] = [
                ChangeHistory(**model.to_dict(exclude=["_logger"])) for model in models
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

    def get_by_id(
        self,
        id: int,
    ) -> Optional[ChangeHistory]:
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
                return ChangeHistory(**model.to_dict(exclude=["_logger"]))
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

    def get_by_uuid(
        self,
        uuid: str,
    ) -> Optional[ChangeHistory]:
        """
        Returns a change history with the given UUID.

        Args:
            uuid (str): The UUID of the change_history.

        Returns:
            Optional[ChangeHistory]: The change history with the given UUID if no exception occurs. Otherwise, None.

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
                # Convert the ChangeHistoryModel object to an ChangeHistory object
                return ChangeHistory(**model.to_dict(exclude=["_logger"]))
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

    def update(
        self,
        change_history: Union[ChangeHistory, ChangeHistory],
    ) -> Optional[ChangeHistory]:
        """
        Updates a change history with the given ID.

        Args:
            change history (Union[ChangeHistory, ChangeHistory]): The change history to update.

        Returns:
            Optional[ChangeHistory]: The updated change history if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the change history to an immutable change history and update the change history in the database
            model: Optional[ChangeHistoryModel] = asyncio.run(
                ChangeHistoryConverter.object_to_model(
                    object=ChangeHistory(**change_history.to_dict(exclude=["_logger"]))
                ).update(
                    **change_history.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    )
                )
            )

            # Return the updated change history if it exists
            if model is not None:
                # Convert the ChangeHistoryModel object to an ChangeHistory object
                change_history = ChangeHistory(**model.to_dict(exclude=["_logger"]))

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
        key (Field): The key of the change_history.
        source (Field): The source of the change_history.
        updated_at (Field): The timestamp when the change history was last updated.
        uuid (Field): The UUID of the change_history.
    """

    table: str = Constants.CHANGE_HISTORIES

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
        id: Optional[int] = None,
        key: Optional[str] = None,
        source: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ChangeHistory class.

        Args:
            created_at (Optional[datetime]): The timestamp when the change history was created.
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
            id=id,
            key=key,
            source=source,
            table=Constants.CHANGE_HISTORIES,
            updated_at=updated_at,
            uuid=uuid,
        )


class ChangeHistoryItem(ImmutableBaseObject):
    """
    Represents a change history item.

    A change history item represents a change made to a mutable object.

    Attributes:
        from_ (Any): The original value of the item.
        to (Any): The new value of the item.
        created_at (Optional[datetime]): The timestamp when the item was created.
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
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ChangeHistoryItem class.

        Args:
            from_ (Any): The original value of the item.
            to (Any): The new value of the item.
            created_at (Optional[datetime]): The timestamp when the item was created.
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
            id=id,
            key=key,
            to=to,
            updated_at=updated_at,
            uuid=uuid,
        )


class ChangeHistoryItemConverter:
    """
    A converter class for transforming between ChangeHistoryItemModel and ChangeHistoryItem instances.

    This class provides methods to convert a ChangeHistoryItemModel instance to an ChangeHistoryItem instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the ChangeHistoryItemConverter class.
    """

    logger: Logger = Logger.get_logger(name="ChangeHistoryItemConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "ChangeHistoryItemModel",
    ) -> Optional[ChangeHistoryItem]:
        """
        Converts a given ChangeHistoryItemModel instance to an ChangeHistoryItem instance.

        Args:
            model (ChangeHistoryItemModel): The ChangeHistoryItemModel instance to be converted.

        Returns:
            ChangeHistoryItem: The converted ChangeHistoryItem instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ChangeHistoryItemModel instance.
        """
        try:
            # Attempt to create and return a new instance of the ChangeHistoryItem class from the dictionary representation of the ChangeHistoryItemModel instance
            return ChangeHistoryItem(**model.to_dict(exclude=["_logger"]))
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
        object: ChangeHistoryItem,
    ) -> Optional["ChangeHistoryItemModel"]:
        """
        Converts a given ChangeHistoryItem instance to a ChangeHistoryItemModel instance.

        Args:
            object (ChangeHistoryItem): The ChangeHistoryItem instance to be converted.

        Returns:
            ChangeHistoryItemModel: The converted ChangeHistoryItemModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ChangeHistoryItem instance.
        """
        try:
            # Attempt to create and return a new instance of the ChangeHistoryItemModel class from the dictionary representation of the ChangeHistoryItem instance
            return ChangeHistoryItemModel(**object.to_dict(exclude=["_logger"]))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'object_to_model' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class ChangeHistoryItemFactory:
    """
    A factory class used to create instances of ChangeHistoryItem class.

    Attributes:
        logger (Logger): The logger instance associated with the object.
    """

    logger: Logger = Logger.get_logger(name="ChangeHistoryItemFactory")

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
    ) -> Optional[ChangeHistoryItem]:
        """
        Creates and returns a new instance of ChangeHistoryItem class.

        Args:
            from_ (Any): The original value of the item.
            to (Any): The new value of the item.
            created_at (Optional[datetime]): The timestamp when the item was created.
            id (Optional[int]): The ID of the item.
            key (Optional[str]): The key of the item.
            updated_at (Optional[datetime]): The timestamp when the item was last updated.
            uuid (Optional[str]): The UUID of the item.

        Returns:
            Optional[ChangeHistoryItem]: The new instance of ChangeHistoryItem class.

        Raises:
            Exception: If an exception occurs while creating the item.
        """
        try:
            # Attempt to create and return a new instance of the ChangeHistoryItem class
            return ChangeHistoryItem(
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

    def __init__(self) -> None:
        """
        Initializes a new instance of the ChangeHistoryItemManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def count(self) -> int:
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

    def create(
        self,
        change_history_item: Union[ChangeHistoryItem, ChangeHistoryItem],
    ) -> Optional[ChangeHistoryItem]:
        """
        Creates a new change history item in the database.

        Args:
            change history item (Union[ChangeHistoryItem, ChangeHistoryItem]): The change history item to be created.

        Returns:
            Optional[ChangeHistoryItem]: The newly created immutable change history item if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the change_history_item.
        """
        try:
            # Check if the change history item object is immutable
            if isinstance(
                change_history_item,
                ChangeHistoryItem,
            ):
                # If it is, convert it to a mutable change history item
                change_history_item = ChangeHistoryItem(
                    **change_history_item.to_dict(exclude=["_logger"])
                )

            # Set the created_at timestamp of the change history item
            change_history_item.created_at = Miscellaneous.get_current_datetime()

            # Set the key of the change history item
            change_history_item.key = f"CHANGE_HISTORY_{self.count() + 1}"

            # Set the updated_at timestamp of the change history item
            change_history_item.updated_at = Miscellaneous.get_current_datetime()

            # Set the uuid of the change history item
            change_history_item.uuid = str(uuid.uuid4())

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
                change_history_item = ChangeHistoryItem(
                    **change_history_item.to_dict(exclude=["_logger"])
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

    def delete(
        self,
        change_history_item: Union[ChangeHistoryItem, ChangeHistoryItem],
    ) -> bool:
        """
        Deletes a change history item from the database.

        Args:
            change history item (Union[ChangeHistoryItem, ChangeHistoryItem]): The change history item to be deleted.

        Returns:
            bool: True if the change history item was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the change history item to an immutable change history item and delete the change history item from the database
            result: bool = asyncio.run(
                ChangeHistoryItemConverter.object_to_model(
                    object=ChangeHistoryItem(
                        **change_history_item.to_dict(exclude=["_logger"])
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

    def get_all(self) -> Optional[List[ChangeHistoryItem]]:
        """
        Returns a list of all change histories in the database.

        Returns:
            Optional[List[ChangeHistoryItem]]: A list of all change histories in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if cache and table size are equal
            if self.cache and len(self._cache) == self.count():
                # Return the list of immutable change histories from the cache
                return self.get_cache_values()

            # Get all change histories from the database
            models: List[ChangeHistoryItemModel] = asyncio.run(
                ChangeHistoryItemModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of ChangeHistoryItemModel objects to a list of ChangeHistoryItem objects
            change_histories: List[ChangeHistoryItem] = [
                ChangeHistoryItem(**model.to_dict(exclude=["_logger"]))
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

    def get_by_id(
        self,
        id: int,
    ) -> Optional[ChangeHistoryItem]:
        """
        Returns a change history item with the given ID.

        Args:
            id (int): The ID of the change_history_item.

        Returns:
            Optional[ChangeHistoryItem]: The change history item with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the change history item is already in the cache
            if self.is_key_in_cache(key=f"CHANGE_HISTORY_{id}"):
                # Return the change history item from the cache
                return self.get_value_from_cache(key=f"CHANGE_HISTORY_{id}")

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
                # Convert the ChangeHistoryItemModel object to an ChangeHistoryItem object
                return ChangeHistoryItem(**model.to_dict(exclude=["_logger"]))
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

    def get_by_uuid(
        self,
        uuid: str,
    ) -> Optional[ChangeHistoryItem]:
        """
        Returns a change history item with the given UUID.

        Args:
            uuid (str): The UUID of the change_history_item.

        Returns:
            Optional[ChangeHistoryItem]: The change history item with the given UUID if no exception occurs. Otherwise, None.

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
                # Convert the ChangeHistoryItemModel object to an ChangeHistoryItem object
                return ChangeHistoryItem(**model.to_dict(exclude=["_logger"]))
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

    def update(
        self,
        change_history_item: Union[ChangeHistoryItem, ChangeHistoryItem],
    ) -> Optional[ChangeHistoryItem]:
        """
        Updates a change history item with the given ID.

        Args:
            change history item (Union[ChangeHistoryItem, ChangeHistoryItem]): The change history item to update.

        Returns:
            Optional[ChangeHistoryItem]: The updated change history item if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the change history item to an immutable change history item and update the change history item in the database
            model: Optional[ChangeHistoryItemModel] = asyncio.run(
                ChangeHistoryItemConverter.object_to_model(
                    object=ChangeHistoryItem(
                        **change_history_item.to_dict(exclude=["_logger"])
                    )
                ).update(
                    **change_history_item.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    )
                )
            )

            # Return the updated change history item if it exists
            if model is not None:
                # Convert the ChangeHistoryItemModel object to an ChangeHistoryItem object
                change_history_item = ChangeHistoryItem(
                    **model.to_dict(exclude=["_logger"])
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
        id (Optional[int]): The ID of the item.
        key (Optional[Any]): The key of the item.
        source (Optional[Dict[str, Any]]): The source of the item.
        to (Optional[Any]): The new value of the item.
        updated_at (Optional[datetime]): The timestamp when the item was last updated.
        uuid (Optional[str]): The UUID of the item.
    """

    table: str = Constants.CHANGE_HISTORY_ITEMS

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
            id=id,
            key=key,
            source=source,
            table=Constants.CHANGE_HISTORY_ITEMS,
            updated_at=updated_at,
            uuid=uuid,
        )
