"""
Author: lodego
Date: 2025-02-15
"""

import asyncio

from datetime import datetime
from typing import *

from utils.builder import BaseObjectBuilder
from utils.constants import Constants
from utils.field import Field
from utils.logger import Logger
from utils.manager import BaseObjectManager
from utils.miscellaneous import Miscellaneous
from utils.model import ImmutableBaseModel
from utils.object import MutableBaseObject, ImmutableBaseObject


__all__: Final[List[str]] = [
    "ImmutableStatus",
    "MutableStatus",
    "StatusConverter",
    "StatusFactory",
    "StatusManager",
    "StatusModel",
]


class ImmutableStatus(ImmutableBaseObject):
    """
    A class representing an immutable status.

    Attributes:
        created_at (Optional[datetime]): The timestamp when the status was created.
        description (Optional[str]): The description of the status.
        emoji (Optional[str]): The emoji of the status.
        icon (Optional[str]): The icon of the status.
        id (Optional[int]): The ID of the status.
        key (Optional[str]): The key of the status.
        metadata (Optional[Dict[str, Any]]): The metadata of the status.
        name (str): The name of the status.
        updated_at (Optional[datetime]): The timestamp when the status was last updated.
        uuid (Optional[str]): The UUID of the status.
    """

    def __init__(
        self,
        name: str,
        created_at: Optional[datetime] = None,
        description: Optional[str] = None,
        emoji: Optional[str] = None,
        icon: Optional[str] = "🏷️",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableStatus class.

        Args:
            name (str): The name of the status.
            created_at (Optional[datetime]): The timestamp when the status was created.
            description (Optional[str]): The description of the status.
            emoji (Optional[str]): The emoji of the status.
            icon (Optional[str]): The icon of the status. Defaults to "🏷️".
            id (Optional[int]): The ID of the status.
            key (Optional[str]): The key of the status.
            metadata (Optional[Dict[str, Any]]): The metadata of the status.
            updated_at (Optional[datetime]): The timestamp when the status was last updated.
            uuid (Optional[str]): The UUID of the status.
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            description=description,
            emoji=emoji,
            icon=icon,
            id=id,
            key=key,
            metadata=metadata,
            name=name,
            updated_at=updated_at,
            uuid=uuid,
        )

    def to_mutable(self) -> "MutableStatus":
        """
        Converts the ImmutableStatus instance to a MutableStatus instance.

        Returns:
            MutableStatus: The converted MutableStatus instance.
        """

        # Return a new instance of the MutableStatus class with the same attributes as the ImmutableStatus instance
        return MutableStatus(
            **self.to_dict(
                exclude=[
                    "_logger",
                ]
            )
        )


class MutableStatus(MutableBaseObject):
    """
    A class representing a mutable status.

    Attributes:
        created_at (Optional[datetime]): The timestamp when the status was created.
        description (Optional[str]): The description of the status.
        emoji (Optional[str]): The emoji of the status.
        icon (Optional[str]): The icon of the status.
        id (Optional[int]): The ID of the status.
        key (Optional[str]): The key of the status.
        metadata (Optional[Dict[str, Any]]): The metadata of the status.
        name (str): The name of the status.
        updated_at (Optional[datetime]): The timestamp when the status was last updated.
        uuid (Optional[str]): The UUID of the status.
    """

    def __init__(
        self,
        name: str,
        created_at: Optional[datetime] = None,
        description: Optional[str] = None,
        emoji: Optional[str] = None,
        icon: Optional[str] = "🏷️",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableStatus class.

        Args:
            name (str): The name of the status.
            created_at (Optional[datetime]): The timestamp when the status was created.
            description (Optional[str]): The description of the status.
            emoji (Optional[str]): The emoji of the status.
            icon (Optional[str]): The icon of the status. Defaults to "🏷️".
            id (Optional[int]): The ID of the status.
            key (Optional[str]): The key of the status.
            metadata (Optional[Dict[str, Any]]): The metadata of the status.
            updated_at (Optional[datetime]): The timestamp when the status was last updated.
            uuid (Optional[str]): The UUID of the status.
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            description=description,
            emoji=emoji,
            icon=icon,
            id=id,
            key=key,
            metadata=metadata,
            name=name,
            updated_at=updated_at,
            uuid=uuid,
        )

    def to_immutable(self) -> ImmutableStatus:
        """
        Converts the MutableStatus instance to an ImmutableStatus instance.

        Returns:
            ImmutableStatus: The converted ImmutableStatus instance.
        """

        # Return a new instance of the ImmutableStatus class with the same attributes as the ImmutableStatus instance
        return ImmutableStatus(
            **self.to_dict(
                exclude=[
                    "_logger",
                ]
            )
        )


class StatusConverter:
    """
    A converter class for transforming between StatusModel and ImmutableStatus instances.

    This class provides methods to convert a StatusModel instance to an ImmutableStatus instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the StatusConverter class.
    """

    logger: Final[Logger] = Logger.get_logger(name="StatusConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "StatusModel",
    ) -> Optional[ImmutableStatus]:
        """
        Converts a given StatusModel instance to an ImmutableStatus instance.

        Args:
            model (StatusModel): The StatusModel instance to be converted.

        Returns:
            ImmutableStatus: The converted ImmutableStatus instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the StatusModel instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableStatus class from the dictionary representation of the StatusModel instance
            return ImmutableStatus(
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
        object: ImmutableStatus,
    ) -> Optional["StatusModel"]:
        """
        Converts a given ImmutableStatus instance to a StatusModel instance.

        Args:
            object (ImmutableStatus): The ImmutableStatus instance to be converted.

        Returns:
            StatusModel: The converted StatusModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ImmutableStatus instance.
        """
        try:
            # Attempt to create and return a new instance of the StatusModel class from the dictionary representation of the ImmutableStatus instance
            return StatusModel(
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


class StatusFactory:
    logger: Final[Logger] = Logger.get_logger(name="StatusFactory")

    @classmethod
    def create_status(
        cls,
        name: str,
        created_at: Optional[datetime] = None,
        description: Optional[str] = None,
        emoji: Optional[str] = None,
        icon: Optional[str] = "🏷️",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> ImmutableStatus:
        """
        Creates a new instance of the ImmutableStatus class.

        Args:
            name (str): The name of the status.
            created_at (Optional[datetime]): The timestamp when the status was created.
            description (Optional[str]): The description of the status.
            emoji (Optional[str]): The emoji of the status.
            icon (Optional[str]): The icon of the status. Defaults to "🏷️".
            id (Optional[int]): The ID of the status.
            key (Optional[str]): The key of the status.
            metadata (Optional[Dict[str, Any]]): The metadata of the status.
            updated_at (Optional[datetime]): The timestamp when the status was last updated.
            uuid (Optional[str]): The UUID of the status.

        Returns:
            ImmutableStatus: The created instance of the ImmutableStatus class.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableStatus class
            return ImmutableStatus(
                name=name,
                created_at=created_at,
                description=description,
                emoji=emoji,
                icon=icon,
                id=id,
                key=key,
                metadata=metadata,
                updated_at=updated_at,
                uuid=uuid,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_status' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class StatusBuilder(BaseObjectBuilder):
    """ """

    pass


class StatusManager(BaseObjectManager):
    """
    A manager class for managing statuses in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for statuses.

    Attributes:
        cache: (List[Any]): The cache for storing statuses.
        logger (Logger): The logger instance associated with the object.
    """

    _shared_instance: Optional["StatusManager"] = None

    def __new__(cls) -> "StatusManager":
        """
        Creates and returns a new instance of the StatusManager class.

        If the instance does not exist, creates a new one by calling the parent class
        constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Returns:
            StatusManager: The created or existing instance of StatusManager class.
        """
        if cls._shared_instance is None:
            # Create a new instance by calling the parent class constructor
            cls._shared_instance = super(StatusManager, cls).__new__(cls)
            # Initialize the instance
            cls._shared_instance.init()
        # Return the shared instance
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes a new instance of the StatusManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def count_statuses(self) -> int:
        """
        Returns the number of statuses in the database.

        Returns:
            int: The number of statuses in the database.
        """
        try:
            # Count and return the number of statuses in the database
            return asyncio.run(StatusModel.count(database=Constants.DATABASE_PATH))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_status(
        self,
        status: Union[ImmutableStatus, MutableStatus],
    ) -> Optional[ImmutableStatus]:
        """
        Creates a new status in the database.

        Args:
            status (Union[ImmutableStatus, MutableStatus]): The status to be created.

        Returns:
            Optional[ImmutableStatus]: The newly created immutable status if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the status.
        """
        try:
            # Check if the status object is immutable
            if isinstance(
                status,
                ImmutableStatus,
            ):
                # If it is, convert it to a mutable status
                status = status.to_mutable()

            # Set the created_at timestamp of the status
            status.created_at = Miscellaneous.get_current_datetime()

            # Set the key of the status
            status.key = f"STATUS_{self.count_statuses() + 1}"

            # Set the updated_at timestamp of the status
            status.updated_at = Miscellaneous.get_current_datetime()

            # Set the uuid of the status
            status.uuid = Miscellaneous.get_uuid()

            # Convert the status object to a StatusModel object
            model: StatusModel = StatusConverter.object_to_model(object=status)

            # Create a new status in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            if id:
                # Set the ID of the status
                status.id = id

                # Convert the status to an immutable status
                status = StatusFactory.create_status(
                    **status.to_dict(
                        exclude=[
                            "_logger",
                        ]
                    )
                )

                # Add the status to the cache
                self.add_to_cache(
                    key=status.key,
                    value=status,
                )

                # Return the newly created immutable status
                return status

            # Log a warning message indicating an error has occurred
            self.logger.warning(
                message=f"It seems that an error has occured while attempting to create a status ({status}) in the database."
            )

            # Return None indicating an error has occurred
            return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_status' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete_status(
        self,
        status: Union[ImmutableStatus, MutableStatus],
    ) -> bool:
        """
        Deletes a status from the database.

        Args:
            status (Union[ImmutableStatus, MutableStatus]): The status to be deleted.

        Returns:
            bool: True if the status was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the status to an immutable status and delete the status from the database
            result: bool = asyncio.run(
                StatusConverter.object_to_model(
                    object=StatusFactory.create_status(
                        **status.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).delete()
            )

            # Remove the status from the cache
            self.remove_from_cache(key=status.key)

            # Return True if the status was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all_statuses(self, force_refetch: bool = False,) -> Optional[List[ImmutableStatus]]:
        """
        Returns a list of all statuses in the database.

        Args:
            force_refetch (bool): Whether to force a refetch of the statuses from the database. Defaults to False.

        Returns:
            Optional[List[ImmutableStatus]]: A list of all statuses in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if cache and table size are equal
                if self.cache and len(self._cache) == self.count_statuses():
                    # Return the list of immutable statuses from the cache
                    return self.get_cache_values()

            # Get all statuses from the database
            models: List[StatusModel] = asyncio.run(
                StatusModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of StatusModel objects to a list of ImmutableStatus objects
            statuses: List[ImmutableStatus] = [
                StatusFactory.create_status(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Add the immutable statuses to the cache
            self.add_to_cache(
                key=[status.key for status in statuses],
                value=statuses,
            )

            # Return the list of immutable statuses
            return statuses
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_default_statuses(self) -> Optional[List[ImmutableStatus]]:
        """
        Retrieves the default statuses from the database.

        Returns:
            Optional[List[ImmutableStatus]]: A list of default statuses if no exception occurs. Otherwise, None.

        Raises:
            Exception: If no 'status' defaults are found or any other exception occurs.
        """
        try:
            # Import necessary classes
            from core.default import ImmutableDefault, DefaultManager

            # Initialize an empty list to store the statuses
            result: List[ImmutableStatus] = []

            # Retrieve defaults with the name 'status'
            defaults: Optional[List[ImmutableDefault]] = [
                DefaultManager().get_default_by(
                    field="name",
                    value=f"status:{status}",
                )
                for status in [
                    Constants.NEW,
                    Constants.LEARNING,
                    Constants.REVIEW,
                    Constants.COMPLETED,
                ]
            ]

            # Raise exception if no defaults are found
            if not defaults:
                raise Exception("Found no 'status' defaults in the database.")

            # Iterate over each default
            for default in defaults:
                # Check if the status already exists
                existing_status: Optional[ImmutableStatus] = self.get_status_by(
                    field="name",
                    value=default.value,
                )

                if not existing_status:
                    # Create a new status if it doesn't exist
                    status: ImmutableStatus = StatusFactory.create_status(
                        emoji=(
                            "🆕"
                            if default.value == Constants.NEW.capitalize()
                            else (
                                "📖"
                                if default.value == Constants.LEARNING.capitalize()
                                else (
                                    "🔄"
                                    if default.value == Constants.REVIEW.capitalize()
                                    else "✅"
                                )
                            )
                        ),
                        name=default.value,
                    )

                    # Add the newly created status to the result
                    result.append(self.create_status(status=status))
                else:
                    # If the status exists, retrieve it from the database
                    result.append(existing_status)

            # Return the list of statuses
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_default_statuses' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_status_by(
        self,
        field: str,
        value: Any,
        force_refetch: bool = False,
    ) -> Optional[ImmutableStatus]:
        """
        Retrieves a status by the given field and value.

        Args:
            field (str): The field to search by.
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            value (Any): The value to search for.

        Returns:
            Optional[ImmutableStatus]: The status with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if the status is already in the cache
                if self.is_key_in_cache(key=field):
                    # Return the status from the cache
                    return self.get_value_from_cache(key=field)

            # Get the status with the given field and value from the database
            model: Optional[StatusModel] = asyncio.run(
                StatusModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Return the status if it exists
            if model is not None:
                # Convert the StatusModel object to an ImmutableStatus object
                status: ImmutableStatus = StatusFactory.create_status(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the status to the cache
                self.add_to_cache(
                    key=status.key,
                    value=status,
                )

                # Return the status
                return status
            else:
                # Return None indicating that the status does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_status_by_id(
        self,
        id: int,
        force_refetch: bool = False,
    ) -> Optional[ImmutableStatus]:
        """
        Returns a status with the given ID.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            id (int): The ID of the status.

        Returns:
            Optional[ImmutableStatus]: The status with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if the status is already in the cache
                if self.is_key_in_cache(key=f"STATUS_{id}"):
                    # Return the status from the cache
                    return self.get_value_from_cache(key=f"STATUS_{id}")

            # Get the status with the given ID from the database
            model: Optional[StatusModel] = asyncio.run(
                StatusModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the status if it exists
            if model is not None:
                # Convert the StatusModel object to an ImmutableStatus object
                status: ImmutableStatus = StatusFactory.create_status(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the status to the cache
                self.add_to_cache(
                    key=status.key,
                    value=status,
                )

                # Return the status
                return status
            else:
                # Return None indicating that the status does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_status_by_key(
        self,
        key: str,
        force_refetch: bool = False,
    ) -> Optional[ImmutableStatus]:
        """
        Returns a status with the given key.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            key (str): The key of the status.

        Returns:
            Optional[ImmutableStatus]: The status with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if the status is already in the cache
                if self.is_key_in_cache(key=key):
                    # Return the status from the cache
                    return self.get_value_from_cache(key=key)

            # Get the status with the given key from the database
            model: Optional[StatusModel] = asyncio.run(
                StatusModel.get_by(
                    column="key",
                    database=Constants.DATABASE_PATH,
                    value=key,
                )
            )

            # Return the status if it exists
            if model is not None:
                # Convert the StatusModel object to an ImmutableStatus object
                status: ImmutableStatus = StatusFactory.create_status(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the status to the cache
                self.add_to_cache(
                    key=status.key,
                    value=status,
                )

                # Return the status
                return status
            else:
                # Return None indicating that the status does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_key' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_status_by_uuid(
        self,
        uuid: str,
        force_refetch: bool = False,
    ) -> Optional[ImmutableStatus]:
        """
        Returns a status with the given UUID.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            uuid (str): The UUID of the status.

        Returns:
            Optional[ImmutableStatus]: The status with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if the status is already in the cache
                if self.is_key_in_cache(key=uuid):
                    # Return the status from the cache
                    return self.get_value_from_cache(key=uuid)

            # Get the status with the given UUID from the database
            model: Optional[StatusModel] = asyncio.run(
                StatusModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the status if it exists
            if model is not None:
                # Convert the StatusModel object to an ImmutableStatus object
                return StatusFactory.create_status(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the status does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def search_statuses(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[Union[List[ImmutableStatus]]]:
        """
        Searches for statuses in the database.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            **kwargs: Any additional keyword arguments to be passed to the search method of the StatusModel class.

        Returns:
            Optional[Union[List[ImmutableStatus]]]: The found statuses if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Search the stack for the passed keyword arguments
                cached_result: Optional[List[ImmutableStatus]] = self.search_cache(
                    **kwargs
                )

                # Check, if any cached results exist
                if cached_result:
                    # Return the cached results
                    return cached_result

            # Search for statuses in the database
            models: Optional[List[StatusModel]] = asyncio.run(
                StatusModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found statuses if any
            if models is not None and len(models) > 0:
                statuses: List[ImmutableStatus] = [
                    StatusFactory.create_status(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                    for model in models
                ]

                # Add the statuses to the cache
                self.add_to_cache(
                    key=[status.key for status in statuses],
                    value=statuses,
                )

                # Return the found statuses
                return statuses
            else:
                # Return None indicating that no statuses were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_status(
        self,
        status: Union[ImmutableStatus, MutableStatus],
    ) -> Optional[ImmutableStatus]:
        """
        Updates a status with the given ID.

        Args:
            status (Union[ImmutableStatus, MutableStatus]): The status to update.

        Returns:
            Optional[ImmutableStatus]: The updated status if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the status object is immutable
            if isinstance(
                status,
                ImmutableStatus,
            ):
                # If it is, convert it to a mutable status
                status = status.to_mutable()

            # Update the updated_at timestamp of the status
            status.updated_at = Miscellaneous.get_current_datetime()

            # Convert the status to an immutable status and update the status in the database
            result: bool = asyncio.run(
                StatusConverter.object_to_model(
                    object=StatusFactory.create_status(
                        **status.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).update(
                    database=Constants.DATABASE_PATH,
                    **status.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Check, if the status was updated successfully
            if result:
                # Update the status in the cache
                self.update_in_cache(
                    key=status.key,
                    value=status,
                )

                # Return the updated status
                return status.to_immutable()
            else:
                # Return None indicating that the status does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class StatusModel(ImmutableBaseModel):
    """
    Represents the structure of a status model.

    Attributes:
        created_at (datetime): The timestamp when the status was created.
        description (str): The description of the status.
        emoji (str): The emoji of the status.
        icon (str): The icon of the status. Defaults to "🏷️".
        id (int): The ID of the status.
        key (str): The key of the status.
        metadata (Dict[str, Any]): The metadata of the status.
        name (str): The name of the status.
        updated_at (datetime): The timestamp when the status was last updated.
        uuid (str): The UUID of the status.
    """

    table: Final[str] = Constants.STATUSES

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

    description: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="description",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=False,
    )

    emoji: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="emoji",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=True,
    )

    icon: Field = Field(
        autoincrement=False,
        default="🏷️",
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

    metadata: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="metadata",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=False,
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
        description: Optional[str] = None,
        emoji: Optional[str] = None,
        icon: Optional[str] = "🏷️",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the StatusModel class.

        Args:
            created_at (Optional[datetime]): The timestamp when the status was created.
            description (Optional[str]): The description of the status.
            emoji (Optional[str]): The emoji of the status.
            icon (Optional[str]): The icon of the status. Defaults to "🏷️".
            id (Optional[int]): The ID of the status.
            key (Optional[str]): The key of the status.
            metadata (Optional[Dict[str, Any]]): The metadata of the status.
            name (Optional[str]): The name of the status.
            updated_at (Optional[datetime]): The timestamp when the status was last updated.
            uuid (Optional[str]): The UUID of the status.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            description=description,
            emoji=emoji,
            icon="🏷️",
            id=id,
            key=key,
            metadata=metadata,
            name=name,
            table=Constants.STATUSES,
            updated_at=updated_at,
            uuid=uuid,
        )
