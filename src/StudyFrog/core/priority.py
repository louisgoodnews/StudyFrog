"""
Author: lodego
Date: 2025-02-05
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
    "ImmutablePriority",
    "MutablePriority",
    "PriorityConverter",
    "PriorityFactory",
    "PriorityManager",
    "PriorityModel",
]


class ImmutablePriority(ImmutableBaseObject):
    """
    An immutable class representing a priority.

    A priority has a value between 0 and 1 that represents the importance of an object.

    Attributes:
        name (str): The name of the priority.
        value (float): The value of the priority.
        created_at (datetime): The timestamp when the priority was created.
        id (int): The ID of the priority.
        key (str): The key of the priority.
        updated_at (datetime): The timestamp when the priority was last updated.
        uuid (str): The UUID of the priority.
    """

    def __init__(
        self,
        name: str,
        value: float,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutablePriority class.

        Args:
            name (str): The name of the priority.
            value (float): The value of the priority.
            created_at (Optional[datetime]): The timestamp when the priority was created.
            id (Optional[int]): The ID of the priority.
            key (Optional[str]): The key of the priority.
            updated_at (Optional[datetime]): The timestamp when the priority was last updated.
            uuid (Optional[str]): The UUID of the priority.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            id=id,
            key=key,
            name=name,
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )

    def to_mutable(self) -> "MutablePriority":
        """
        Returns a MutablePriority instance corresponding to the current ImmutablePriority instance.

        Returns:
            MutablePriority: A MutablePriority instance corresponding to the current ImmutablePriority instance.
        """

        # Return a MutablePriority instance corresponding to the current ImmutablePriority instance
        return MutablePriority(**self.to_dict(exclude=["_logger"]))


class MutablePriority(MutableBaseObject):
    """
    A mutable class representing a priority.

    A priority has a value between 0 and 1 that represents the importance of an object.

    Attributes:
        name (str): The name of the priority.
        value (float): The value of the priority.
        created_at (datetime): The timestamp when the priority was created.
        id (int): The ID of the priority.
        key (str): The key of the priority.
        updated_at (datetime): The timestamp when the priority was last updated.
        uuid (str): The UUID of the priority.
    """

    def __init__(
        self,
        name: str,
        value: float,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutablePriority class.

        Args:
            name (str): The name of the priority.
            value (float): The value of the priority.
            created_at (Optional[datetime]): The timestamp when the priority was created.
            id (Optional[int]): The ID of the priority.
            key (Optional[str]): The key of the priority.
            updated_at (Optional[datetime]): The timestamp when the priority was last updated.
            uuid (Optional[str]): The UUID of the priority.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            id=id,
            key=key,
            name=name,
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )

    def to_immutable(self) -> ImmutablePriority:
        """
        Returns an ImmutablePriority instance corresponding to the current MutablePriority instance.

        Returns:
            ImmutablePriority: An ImmutablePriority instance corresponding to the current MutablePriority instance.
        """

        # Return a MutablePriority instance corresponding to the current ImmutablePriority instance
        return ImmutablePriority(**self.to_dict(exclude=["_logger"]))


class PriorityConverter:
    """
    A converter class for transforming between PriorityModel and ImmutablePriority instances.

    This class provides methods to convert a PriorityModel instance to an ImmutablePriority instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the PriorityConverter class.
    """

    logger: Logger = Logger.get_logger(name="PriorityConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "PriorityModel",
    ) -> Optional[ImmutablePriority]:
        """
        Converts a given PriorityModel instance to an ImmutablePriority instance.

        Args:
            model (PriorityModel): The PriorityModel instance to be converted.

        Returns:
            ImmutablePriority: The converted ImmutablePriority instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the PriorityModel instance.
        """
        try:
            # Attempt to create and return a new instance of the Priority class from the dictionary representation of the PriorityModel instance
            return ImmutablePriority(
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
        object: ImmutablePriority,
    ) -> Optional["PriorityModel"]:
        """
        Converts a given ImmutablePriority instance to a PriorityModel instance.

        Args:
            object (ImmutablePriority): The ImmutablePriority instance to be converted.

        Returns:
            PriorityModel: The converted PriorityModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ImmutablePriority instance.
        """
        try:
            # Attempt to create and return a new instance of the PriorityModel class from the dictionary representation of the ImmutablePriority instance
            return PriorityModel(**object.to_dict(exclude=["_logger"]))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'object_to_model' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class PriorityFactory:
    logger: Logger = Logger.get_logger(name="PriorityFactory")

    @classmethod
    def create_priority(
        cls,
        name: str,
        value: float,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutablePriority]:
        """
        Creates a new instance of the ImmutablePriority class.

        Args:
            created_at (Optional[datetime]): The timestamp when the priority was created.
            id (Optional[int]): The ID of the priority.
            key (Optional[str]): The key of the priority.
            name (str): The name of the priority.
            updated_at (Optional[datetime]): The timestamp when the priority was last updated.
            uuid (Optional[str]): The UUID of the priority.
            value (Optional[float]): The value of the priority.

        Returns:
            Optional[ImmutablePriority]: The new instance of the ImmutablePriority class.
        """
        try:
            # Attempt to create and return a Priority object
            return ImmutablePriority(
                created_at=created_at,
                id=id,
                key=key,
                name=name,
                updated_at=updated_at,
                uuid=uuid,
                value=value,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_priority' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class PriorityManager(BaseObjectManager):
    """
    A manager class for managing priorities in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for priorities.

    Attributes:
        cache: (List[Any]): The cache for storing priorities.
        logger (Logger): The logger instance associated with the object.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the PriorityManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def count_priorities(self) -> int:
        """
        Returns the number of priorities in the database.

        Returns:
            int: The number of priorities in the database.
        """
        try:
            # Count the number of priorities in the database
            result: Any = asyncio.run(
                PriorityModel.execute(
                    database=Constants.DATABASE_PATH,
                    sql=f"SELECT COUNT(*) FROM {Constants.PRIORITIES};",
                )
            )

            # Return the number of priorities in the database
            return result[0][0] if result else 0
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_priority(
        self,
        priority: ImmutablePriority,
    ) -> Optional[ImmutablePriority]:
        """
        Creates a new priority in the database.

        Args:
            priority (ImmutablePriority): The priority to be created.

        Returns:
            Optional[ImmutablePriority]: The newly created immutable priority if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the priority.
        """
        try:
            # Check if the priority object is immutable
            if isinstance(
                priority,
                ImmutablePriority,
            ):
                # If it is, convert it to a mutable priority
                priority = MutablePriority(**priority.to_dict(exclude=["_logger"]))

            # Set the created_at timestamp of the priority
            priority.created_at = Miscellaneous.get_current_datetime()

            # Set the key of the priority
            priority.key = f"PRIORITY_{self.count_priorities() + 1}"

            # Set the updated_at timestamp of the priority
            priority.updated_at = Miscellaneous.get_current_datetime()

            # Set the uuid of the priority
            priority.uuid = Miscellaneous.get_uuid()

            # Convert the priority object to a PriorityModel object
            model: PriorityModel = PriorityConverter.object_to_model(object=priority)

            # Create a new priority in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            if id:
                # Set the ID of the priority
                priority.id = id

                # Convert the priority to an immutable priority
                priority = ImmutablePriority(**priority.to_dict(exclude=["_logger"]))

                # Add the priority to the cache
                self.add_to_cache(
                    key=priority.key,
                    value=priority,
                )

                # Return the newly created immutable priority
                return priority

            # Log a warning message indicating an error has occurred
            self.logger.warning(
                message=f"It seems that an error has occured while attempting to create a priority ({priority}) in the database."
            )

            # Return None indicating an error has occurred
            return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_priority' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete_priority(
        self,
        priority: ImmutablePriority,
    ) -> bool:
        """
        Deletes a priority from the database.

        Args:
            priority (ImmutablePriority): The priority to be deleted.

        Returns:
            bool: True if the priority was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the priority to an immutable priority and delete the priority from the database
            result: bool = asyncio.run(
                PriorityConverter.object_to_model(
                    object=ImmutablePriority(**priority.to_dict(exclude=["_logger"]))
                ).delete()
            )

            # Return True if the priority was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all_priorities(self) -> Optional[List[ImmutablePriority]]:
        """
        Returns a list of all priorities in the database.

        Returns:
            Optional[List[ImmutablePriority]]: A list of all priorities in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if cache and table size are equal
            if self.cache and len(self._cache) == self.count():
                # Return the list of immutable priorities from the cache
                return self.get_cache_values()

            # Get all priorities from the database
            models: List[PriorityModel] = asyncio.run(
                PriorityModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of PriorityModel objects to a list of Priority objects
            priorities: List[ImmutablePriority] = [
                Priority(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable priorities
            for priority in priorities:
                if not self.is_key_in_cache(key=priority.key):
                    # Add the immutable priority to the cache
                    self.add_to_cache(
                        key=priority.key,
                        value=priority,
                    )
                else:
                    # Update the immutable priority in the cache
                    self.update_in_cache(
                        key=priority.key,
                        value=priority,
                    )

            # Return the list of immutable priorities
            return priorities
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_default_priorities(self) -> Optional[List[ImmutablePriority]]:
        """
        Retrieves the default priorities from the database.

        Returns:
            Optional[List[ImmutablePriority]]: A list of default priorities if no exception occurs. Otherwise, None.

        Raises:
            Exception: If no 'priority' defaults are found or any other exception occurs.
        """
        try:
            # Import necessary classes
            from core.default import ImmutableDefault, DefaultManager

            # Initialize an empty list to store the priorities
            result: List[ImmutablePriority] = []

            # Retrieve defaults with the name 'priority'
            defaults: Optional[List[ImmutableDefault]] = [
                DefaultManager().get_default_by(
                    field="name",
                    value=f"priority:{priority}",
                )
                for priority in [
                    Constants.HIGHEST,
                    Constants.HIGH,
                    Constants.MEDIUM,
                    Constants.LOW,
                    Constants.LOWEST,
                ]
            ]

            # Raise exception if no defaults are found
            if not defaults:
                raise Exception("Found no 'priority' defaults in the database.")

            # Iterate over each default
            for default in defaults:
                # Check if the priority already exists
                existing_priority: Optional[ImmutablePriority] = self.get_priority_by(
                    field="name",
                    value=default.value,
                )

                if not existing_priority:
                    # Create a new priority if it doesn't exist
                    priority: ImmutablePriority = PriorityFactory.create_priority(
                        name=default.value,
                        value=(
                            float(5 / 5)
                            if default.value.lower() == Constants.HIGHEST
                            else (
                                float(4 / 5)
                                if default.value.lower() == Constants.HIGH
                                else (
                                    float(3 / 5)
                                    if default.value.lower() == Constants.MEDIUM
                                    else (
                                        float(2 / 5)
                                        if default.value.lower() == Constants.LOW
                                        else float(1 / 5)
                                    )
                                )
                            )
                        ),
                    )

                    # Add the newly created priority to the result
                    result.append(self.create_priority(priority=priority))
                else:
                    # If the priority exists, retrieve it from the database
                    result.append(existing_priority)

            # Return the list of priorities
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_default_priorities' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_priority_by(
        self,
        field: str,
        value: Any,
    ) -> Optional[ImmutablePriority]:
        """
        Retrieves a priority by the given field and value.

        Args:
            field (str): The field to search by.
            value (Any): The value to search for.

        Returns:
            Optional[ImmutablePriority]: The priority with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the priority is already in the cache
            if self.is_key_in_cache(key=field):
                # Return the priority from the cache
                return self.get_value_from_cache(key=field)

            # Get the priority with the given field and value from the database
            model: Optional[PriorityModel] = asyncio.run(
                PriorityModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Return the priority if it exists
            if model is not None:
                # Convert the PriorityModel object to an Priority object
                return ImmutablePriority(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the priority does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_priority_by_id(
        self,
        id: int,
    ) -> Optional[ImmutablePriority]:
        """
        Returns a priority with the given ID.

        Args:
            id (int): The ID of the priority.

        Returns:
            Optional[ImmutablePriority]: The priority with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the priority is already in the cache
            if self.is_key_in_cache(key=f"PRIORITY_{id}"):
                # Return the priority from the cache
                return self.get_value_from_cache(key=f"PRIORITY_{id}")

            # Get the priority with the given ID from the database
            model: Optional[PriorityModel] = asyncio.run(
                PriorityModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the priority if it exists
            if model is not None:
                # Convert the PriorityModel object to an ImmutablePriority object
                return ImmutablePriority(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the priority does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_priority_by_uuid(
        self,
        uuid: str,
    ) -> Optional[ImmutablePriority]:
        """
        Returns a priority with the given UUID.

        Args:
            uuid (str): The UUID of the priority.

        Returns:
            Optional[ImmutablePriority]: The priority with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the priority is already in the cache
            if self.is_key_in_cache(key=uuid):
                # Return the priority from the cache
                return self.get_value_from_cache(key=uuid)

            # Get the priority with the given UUID from the database
            model: Optional[PriorityModel] = asyncio.run(
                PriorityModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the priority if it exists
            if model is not None:
                # Convert the PriorityModel object to an ImmutablePriority object
                return ImmutablePriority(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the priority does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_priority(
        self,
        priority: ImmutablePriority,
    ) -> Optional[ImmutablePriority]:
        """
        Updates a priority with the given ID.

        Args:
            priority (ImmutablePriority): The priority to update.

        Returns:
            Optional[ImmutablePriority]: The updated priority if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the priority to an immutable priority and update the priority in the database
            model: Optional[PriorityModel] = asyncio.run(
                PriorityConverter.object_to_model(
                    object=ImmutablePriority(**priority.to_dict(exclude=["_logger"]))
                ).update(
                    **priority.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    )
                )
            )

            # Return the updated priority if it exists
            if model is not None:
                # Convert the PriorityModel object to an ImmutablePriority object
                priority = ImmutablePriority(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the priority to the cache
                self.update_in_cache(
                    key=priority.key,
                    value=priority,
                )

                # Return the updated priority
                return priority
            else:
                # Return None indicating that the priority does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class PriorityModel(ImmutableBaseModel):
    """
    A model class representing a priority.

    A priority has a value between 0 and 1 that represents the importance of an object.

    Attributes:
        name (str): The name of the priority.
        value (float): The value of the priority.
    """

    table: str = Constants.PRIORITIES

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
        unique=True,
    )

    created_at: Field = Field(
        default=None,
        description="",
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
        default=None,
        description="",
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
        default=None,
        description="",
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
        default=None,
        description="",
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
        default=None,
        description="",
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
        default=None,
        description="",
        index=False,
        name="value",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="DOUBLE",
        unique=False,
    )

    def __init__(
        self,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        name: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
        value: Optional[float] = None,
    ) -> None:
        """
        Initializes a new instance of the PriorityModel class.

        Args:
            created_at (Optional[datetime]): The timestamp when the priority was created.
            id (Optional[int]): The ID of the priority.
            key (Optional[str]): The key of the priority.
            name (Optional[str]): The name of the priority.
            updated_at (Optional[datetime]): The timestamp when the priority was last updated.
            uuid (Optional[str]): The UUID of the priority.
            value (Optional[float]): The value of the priority.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            id=id,
            key=key,
            name=name,
            table=Constants.PRIORITIES,
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )
