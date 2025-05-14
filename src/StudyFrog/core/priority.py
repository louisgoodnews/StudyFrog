"""
Author: lodego
Date: 2025-02-05
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
        created_at (datetime): The timestamp when the priority was created.
        description (Optional[str]): The description of the priority.
        emoji (str): The emoji of the priority.
        icon (str): The icon of the priority.
        id (int): The ID of the priority.
        key (str): The key of the priority.
        metadata (Optional[Dict[str, Any]]): The metadata of the priority.
        name (str): The name of the priority.
        updated_at (datetime): The timestamp when the priority was last updated.
        uuid (str): The UUID of the priority.
        value (float): The value of the priority.
    """

    def __init__(
        self,
        emoji: str,
        name: str,
        value: float,
        created_at: Optional[datetime] = None,
        description: Optional[str] = None,
        icon: Optional[str] = "🔥",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutablePriority class.

        Args:
            created_at (Optional[datetime]): The timestamp when the priority was created.
            description (Optional[str]): The description of the priority.
            emoji (str): The emoji of the priority.
            icon (Optional[str]): The icon of the priority. Defaults to "🔥".
            id (Optional[int]): The ID of the priority.
            key (Optional[str]): The key of the priority.
            metadata (Optional[Dict[str, Any]]): The metadata of the priority.
            name (str): The name of the priority.
            updated_at (Optional[datetime]): The timestamp when the priority was last updated.
            uuid (Optional[str]): The UUID of the priority.
            value (float): The value of the priority.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            description=description,
            emoji=emoji,
            hide_attributes=True,
            icon=icon,
            id=id,
            key=key,
            metadata=metadata,
            name=name,
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )

    @property
    def created_at(self) -> datetime:
        """
        Returns the timestamp when the priority was created.

        Returns:
            datetime: The timestamp when the priority was created.
        """

        # Return the timestamp when the priority was created
        return self._created_at

    @property
    def description(self) -> str:
        """
        Returns the description of the priority.

        Returns:
            str: The description of the priority.
        """

        # Return the description of the priority
        return self._description

    @property
    def emoji(self) -> str:
        """
        Returns the emoji of the priority.

        Returns:
            str: The emoji of the priority.
        """

        # Return the emoji of the priority
        return self._emoji

    @property
    def icon(self) -> str:
        """
        Returns the icon of the priority.

        Returns:
            str: The icon of the priority.
        """

        # Return the icon of the priority
        return self._icon

    @property
    def key(self) -> str:
        """
        Returns the key of the priority.

        Returns:
            str: The key of the priority.
        """

        # Return the key of the priority
        return self._key

    @property
    def metadata(self) -> Optional[Dict[str, Any]]:
        """
        Returns the metadata of the priority.

        Returns:
            Optional[Dict[str, Any]]: The metadata of the priority.
        """

        # Return the metadata of the priority
        return self._metadata

    @property
    def name(self) -> str:
        """
        Returns the name of the priority.

        Returns:
            str: The name of the priority.
        """

        # Return the name of the priority
        return self._name

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp when the priority was last updated.

        Returns:
            datetime: The timestamp when the priority was last updated.
        """

        # Return the timestamp when the priority was last updated
        return self._updated_at

    @property
    def uuid(self) -> str:
        """
        Returns the UUID of the priority.

        Returns:
            str: The UUID of the priority.
        """

        # Return the UUID of the priority
        return self._uuid

    @property
    def value(self) -> float:
        """
        Returns the value of the priority.

        Returns:
            float: The value of the priority.
        """

        # Return the value of the priority
        return self._value

    def to_mutable(self) -> "MutablePriority":
        """
        Returns a MutablePriority instance corresponding to the current ImmutablePriority instance.

        Returns:
            MutablePriority: A MutablePriority instance corresponding to the current ImmutablePriority instance.
        """
        try:
            # Return a MutablePriority instance corresponding to the current ImmutablePriority instance
            return MutablePriority(
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

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None


class MutablePriority(MutableBaseObject):
    """
    A mutable class representing a priority.

    A priority has a value between 0 and 1 that represents the importance of an object.

    Attributes:
        created_at (datetime): The timestamp when the priority was created.
        description (Optional[str]): The description of the priority.
        emoji (str): The emoji of the priority.
        icon (str): The icon of the priority.
        id (int): The ID of the priority.
        key (str): The key of the priority.
        metadata (Optional[Dict[str, Any]]): The metadata of the priority.
        name (str): The name of the priority.
        updated_at (datetime): The timestamp when the priority was last updated.
        uuid (str): The UUID of the priority.
        value (float): The value of the priority.
    """

    def __init__(
        self,
        emoji: str,
        name: str,
        value: float,
        created_at: Optional[datetime] = None,
        description: Optional[str] = None,
        icon: Optional[str] = "🔥",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutablePriority class.

        Args:
            created_at (Optional[datetime]): The timestamp when the priority was created.
            description (Optional[str]): The description of the priority.
            emoji (str): The emoji of the priority.
            icon (Optional[str]): The icon of the priority.
            id (Optional[int]): The ID of the priority.
            key (Optional[str]): The key of the priority.
            metadata (Optional[Dict[str, Any]]): The metadata of the priority.
            name (str): The name of the priority.
            updated_at (Optional[datetime]): The timestamp when the priority was last updated.
            uuid (Optional[str]): The UUID of the priority.
            value (float): The value of the priority.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            description=description,
            emoji=emoji,
            hide_attributes=True,
            icon=icon,
            id=id,
            key=key,
            metadata=metadata,
            name=name,
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )

    @property
    def created_at(self) -> datetime:
        """
        Returns the timestamp when the priority was created.

        Returns:
            datetime: The timestamp when the priority was created.
        """

        # Return the timestamp when the priority was created
        return self._created_at

    @created_at.setter
    def created_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the timestamp when the priority was created.

        Args:
            value (datetime): The timestamp when the priority was created.

        Returns:
            None
        """

        # Set the timestamp when the priority was created
        self._created_at = value

    @property
    def description(self) -> str:
        """
        Returns the description of the priority.

        Returns:
            str: The description of the priority.
        """

        # Return the description of the priority
        return self._description

    @description.setter
    def description(
        self,
        value: str,
    ) -> None:
        """
        Sets the description of the priority.

        Args:
            value (str): The description of the priority.

        Returns:
            None
        """

        # Set the description of the priority
        self._description = value

    @property
    def emoji(self) -> str:
        """
        Returns the emoji of the priority.

        Returns:
            str: The emoji of the priority.
        """

        # Return the emoji of the priority
        return self._emoji

    @emoji.setter
    def emoji(
        self,
        value: str,
    ) -> None:
        """
        Sets the emoji of the priority.

        Args:
            value (str): The emoji of the priority.

        Returns:
            None
        """

        # Set the emoji of the priority
        self._emoji = value

    @property
    def icon(self) -> str:
        """
        Returns the icon of the priority.

        Returns:
            str: The icon of the priority.
        """

        # Return the icon of the priority
        return self._icon

    @icon.setter
    def icon(
        self,
        value: str,
    ) -> None:
        """
        Sets the icon of the priority.

        Args:
            value (str): The icon of the priority.

        Returns:
            None
        """

        # Set the icon of the priority
        self._icon = value

    @property
    def key(self) -> str:
        """
        Returns the key of the priority.

        Returns:
            str: The key of the priority.
        """

        # Return the key of the priority
        return self._key

    @key.setter
    def key(
        self,
        value: str,
    ) -> None:
        """
        Sets the key of the priority.

        Args:
            value (str): The key of the priority.

        Returns:
            None
        """

        # Set the key of the priority
        self._key = value

    @property
    def metadata(self) -> Optional[Dict[str, Any]]:
        """
        Returns the metadata of the priority.

        Returns:
            Optional[Dict[str, Any]]: The metadata of the priority.
        """

        # Return the metadata of the priority
        return self._metadata

    @metadata.setter
    def metadata(
        self,
        value: Optional[Dict[str, Any]],
    ) -> None:
        """
        Sets the metadata of the priority.

        Args:
            value (Optional[Dict[str, Any]]): The metadata of the priority.

        Returns:
            None
        """

        # Set the metadata of the priority
        self._metadata = value

    @property
    def name(self) -> str:
        """
        Returns the name of the priority.

        Returns:
            str: The name of the priority.
        """

        # Return the name of the priority
        return self._name

    @name.setter
    def name(
        self,
        value: str,
    ) -> None:
        """
        Sets the name of the priority.

        Args:
            value (str): The name of the priority.

        Returns:
            None
        """

        # Set the name of the priority
        self._name = value

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp when the priority was last updated.

        Returns:
            datetime: The timestamp when the priority was last updated.
        """

        # Return the timestamp when the priority was last updated
        return self._updated_at

    @updated_at.setter
    def updated_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the timestamp when the priority was last updated.

        Args:
            value (datetime): The timestamp when the priority was last updated.

        Returns:
            None
        """

        # Set the timestamp when the priority was last updated
        self._updated_at = value

    @property
    def uuid(self) -> str:
        """
        Returns the UUID of the priority.

        Returns:
            str: The UUID of the priority.
        """

        # Return the UUID of the priority
        return self._uuid

    @uuid.setter
    def uuid(
        self,
        value: str,
    ) -> None:
        """
        Sets the UUID of the priority.

        Args:
            value (str): The UUID of the priority.

        Returns:
            None
        """

        # Set the UUID of the priority
        self._uuid = value

    @property
    def value(self) -> float:
        """
        Returns the value of the priority.

        Returns:
            float: The value of the priority.
        """

        # Return the value of the priority
        return self._value

    @value.setter
    def value(
        self,
        value: float,
    ) -> None:
        """
        Sets the value of the priority.

        Args:
            value (float): The value of the priority.

        Returns:
            None
        """

        # Set the value of the priority
        self._value = value

    def to_immutable(self) -> ImmutablePriority:
        """
        Returns an ImmutablePriority instance corresponding to the current MutablePriority instance.

        Returns:
            ImmutablePriority: An ImmutablePriority instance corresponding to the current MutablePriority instance.
        """
        try:
            # Return a MutablePriority instance corresponding to the current ImmutablePriority instance
            return ImmutablePriority(
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

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None


class PriorityConverter:
    """
    A converter class for transforming between PriorityModel and ImmutablePriority instances.

    This class provides methods to convert a PriorityModel instance to an ImmutablePriority instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the PriorityConverter class.
    """

    logger: Final[Logger] = Logger.get_logger(name="PriorityConverter")

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

            # Log the traceback of the exception
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

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
            return PriorityModel(
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

            # Log the traceback of the exception
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None


class PriorityFactory:
    """
    Factory class for creating ImmutablePriority instances.

    Attributes:
        logger (Logger): The logger instance associated with the PriorityFactory class.
    """

    logger: Final[Logger] = Logger.get_logger(name="PriorityFactory")

    @classmethod
    def create_priority(
        cls,
        emoji: str,
        name: str,
        value: float,
        created_at: Optional[datetime] = None,
        description: Optional[str] = None,
        icon: Optional[str] = "🔥",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutablePriority]:
        """
        Creates a new instance of the ImmutablePriority class.

        Args:
            created_at (Optional[datetime]): The timestamp when the priority was created.
            description (Optional[str]): The description of the priority.
            emoji (Optional[str]): The emoji of the priority.
            icon (Optional[str]): The icon of the priority. Defaults to "🔥".
            id (Optional[int]): The ID of the priority.
            key (Optional[str]): The key of the priority.
            metadata (Optional[Dict[str, Any]]): The metadata of the priority.
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
                description=description,
                emoji=emoji,
                icon=icon,
                id=id,
                key=key,
                metadata=metadata,
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


class PriorityBuilder(BaseObjectBuilder):
    """
    A builder class for creating Priority instances.

    This class extends the BaseObjectBuilder class and provides a method for building Priority instances.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the PriorityBuilder class.

        Args:
            None

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    @override
    def build(
        self,
        as_mutable: bool = False,
    ) -> Optional[
        Union[
            ImmutablePriority,
            MutablePriority,
        ]
    ]:
        """
        Builds a new instance of the Priority class.

        Args:
            as_mutable (bool): Whether to return a mutable instance of the Priority class. Defaults to False.

        Returns:
            Optional[Union[ImmutablePriority, MutablePriority]]: The new instance of the Priority class.

        Raises:
            Exception: If an exception occurs while attempting to build the Priority instance.
        """
        try:
            # Attempt to create a new ImmutablePriority instance
            priority: Optional[ImmutablePriority] = PriorityFactory.create_priority(
                **self.configuration
            )

            # Check, if the priority exists
            if not priority:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create priority from configuration: {self.configuration}"
                )

                # Return None indicating an exception has occurred
                return None

            # Check, if the priority should be mutable
            if as_mutable:
                # Convert the priority to a MutablePriority instance
                priority = priority.to_mutable()

            # Return the created instance
            return priority
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'build' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    def created_at(
        self,
        value: datetime,
    ) -> Self:
        """
        Sets the created_at value of the priority.

        Args:
            value (datetime): The created_at value to set.

        Returns:
            Self: The builder instance.
        """

        # Set the created_at value
        self.configuration["created_at"] = value

        # Return the builder instance
        return self

    def description(
        self,
        value: str,
    ) -> Self:
        """
        Sets the description value of the priority.

        Args:
            value (str): The description value to set.

        Returns:
            Self: The builder instance.
        """

        # Set the description value
        self.configuration["description"] = value

        # Return the builder instance
        return self

    def emoji(
        self,
        value: str,
    ) -> Self:
        """
        Sets the emoji value of the priority.

        Args:
            value (str): The emoji value to set.

        Returns:
            Self: The builder instance.
        """

        # Set the emoji value
        self.configuration["emoji"] = value

        # Return the builder instance
        return self

    def metadata(
        self,
        **kwargs,
    ) -> Self:
        """
        Sets the metadata value of the priority.

        Args:
            **kwargs: The keyword arguments to set.

        Returns:
            Self: The builder instance.
        """

        # Check, if the 'metadata key is in the configuration dictionary
        if "metadata" not in self.configuration:
            # Initialize the metadata dictionary
            self.configuration["metadata"] = {}

        # Update the metadata dictionary with the provided keyword arguments
        self.configuration["metadata"].update(kwargs)

        # Return the builder instance
        return self

    def name(
        self,
        value: str,
    ) -> Self:
        """
        Sets the name value of the priority.

        Args:
            value (str): The name value to set.

        Returns:
            Self: The builder instance.
        """

        # Set the name value
        self.configuration["name"] = value

        # Return the builder instance
        return self

    def updated_at(
        self,
        value: datetime,
    ) -> Self:
        """
        Sets the updated_at value of the priority.

        Args:
            value (datetime): The updated_at value to set.

        Returns:
            Self: The builder instance.
        """

        # Set the updated_at value
        self.configuration["updated_at"] = value

        # Return the builder instance
        return self


class PriorityManager(BaseObjectManager):
    """
    A manager class for managing priorities in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for priorities.

    Attributes:
        cache: (List[Any]): The cache for storing priorities.
        logger (Logger): The logger instance associated with the object.
    """

    _shared_instance: Optional["PriorityManager"] = None

    def __new__(cls) -> "PriorityManager":
        """
        Creates and returns a new instance of the PriorityManager class.

        If the instance does not exist, creates a new one by calling the parent class
        constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Returns:
            PriorityManager: The created or existing instance of PriorityManager class.
        """
        if cls._shared_instance is None:
            # Create a new instance by calling the parent class constructor
            cls._shared_instance = super(PriorityManager, cls).__new__(cls)
            # Initialize the instance
            cls._shared_instance.init()
        # Return the shared instance
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes a new instance of the PriorityManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def _run_pre_create_tasks(
        self,
        priority: Union[
            ImmutablePriority,
            MutablePriority,
        ],
    ) -> MutablePriority:
        """
        Runs pre-create tasks for the priority.

        Args:
            priority (Union[ImmutablePriority, MutablePriority]): The priority to run pre-create tasks on.

        Returns:
            MutablePriority: The priority with pre-create tasks run.
        """

        # Check if the priority object is immutable
        if not priority.is_mutable():
            # If it is, convert it to a mutable priority
            priority: MutablePriority = priority.to_mutable()

        # Set the created_at timestamp of the priority
        priority.created_at = priority.created_at or Miscellaneous.get_current_datetime()

        # Set the key of the priority
        priority.key = f"PRIORITY_{self.count_priorities() + 1}"

        # Set the updated_at timestamp of the priority
        priority.updated_at = priority.updated_at or Miscellaneous.get_current_datetime()

        # Set the uuid of the priority
        priority.uuid = Miscellaneous.get_uuid()

        # Return the priority object
        return priority

    def count_priorities(self) -> int:
        """
        Returns the number of priorities in the database.

        Returns:
            int: The number of priorities in the database.
        """
        try:
            # Count and return the number of priorities in the database
            return asyncio.run(PriorityModel.count(database=Constants.DATABASE_PATH))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_priority(
        self,
        priority: Union[
            ImmutablePriority,
            MutablePriority,
        ],
    ) -> Optional[ImmutablePriority]:
        """
        Creates a new priority in the database.

        Args:
            priority (Union[ImmutablePriority, MutablePriority]): The priority to be created.

        Returns:
            Optional[ImmutablePriority]: The newly created immutable priority if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the priority.
        """
        try:
            # Initialize the result (optional) ImmutablePriority to none
            result: Optional[ImmutablePriority] = None

            # Run pre-create tasks
            priority: MutablePriority = self._run_pre_create_tasks(priority=priority)

            # Convert the priority object to a PriorityModel object
            model: PriorityModel = PriorityConverter.object_to_model(object=priority)

            # Create a new priority in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            # Check, if the ID is not None
            if not id:
                # Log a warning message indicating an error has occurred
                self.logger.warning(
                    message=f"It seems that an error has occured while attempting to create a priority ({priority.__repr__()}) in the database."
                )

                # Return early
                return

            # Convert the priority to a dictionary
            kwargs: Dict[str, Any] = priority.to_dict(
                exclude=[
                    "_logger",
                ]
            )

            # Set the ID of the priority
            kwargs["id"] = id

            # Create a new ImmutablePriority object
            result = PriorityFactory.create_priority(**kwargs)

            # Check, if the result is not None
            if not result:
                # Log an error message indicating an error has occurred
                self.logger.error(
                    message=f"It seems that there was an error while attempting to create an ImmutablePriority from the dictionary ({kwargs}) returned by the database. This is likely a serious issue."
                )

                # Return early
                return

            # Add the priority to the cache
            self.add_to_cache(
                key=result.key,
                value=result,
            )

            # Return the newly created immutable priority
            return result
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
                    object=ImmutablePriority(
                        **priority.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
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

    def get_all_priorities(
        self,
        force_refetch: bool = False,
    ) -> Optional[List[ImmutablePriority]]:
        """
        Returns a list of all priorities in the database.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.

        Returns:
            Optional[List[ImmutablePriority]]: A list of all priorities in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if cache and table size are equal
                if self.cache and len(self._cache) == self.count_priorities():
                    # Return the list of immutable priorities from the cache
                    return self.get_cache_values()

            # Get all priorities from the database
            models: List[PriorityModel] = asyncio.run(
                PriorityModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of PriorityModel objects to a list of ImmutablePriority objects
            priorities: List[ImmutablePriority] = [
                ImmutablePriority(
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
                        emoji=(
                            "🔴"
                            if default.value.lower() == Constants.HIGHEST
                            else (
                                "🟠"
                                if default.value.lower() == Constants.HIGH
                                else (
                                    "🟡"
                                    if default.value.lower() == Constants.MEDIUM
                                    else (
                                        "🔵"
                                        if default.value.lower() == Constants.LOW
                                        else "🟢"
                                    )
                                )
                            )
                        ),
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
        force_refetch: bool = False,
    ) -> Optional[ImmutablePriority]:
        """
        Retrieves a priority by the given field and value.

        Args:
            field (str): The field to search by.
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            value (Any): The value to search for.

        Returns:
            Optional[ImmutablePriority]: The priority with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
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
                # Convert the PriorityModel object to an ImmutablePriority object
                priority: ImmutablePriority = PriorityFactory.create_priority(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the priority to the cache
                self.add_to_cache(
                    key=priority.key,
                    value=priority,
                )

                # Return the priority
                return priority
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
        force_refetch: bool = False,
    ) -> Optional[ImmutablePriority]:
        """
        Returns a priority with the given ID.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            id (int): The ID of the priority.

        Returns:
            Optional[ImmutablePriority]: The priority with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
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
                priority: ImmutablePriority = PriorityFactory.create_priority(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the priority to the cache
                self.add_to_cache(
                    key=priority.key,
                    value=priority,
                )

                # Return the priority
                return priority
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

    def get_priority_by_key(
        self,
        key: str,
        force_refetch: bool = False,
    ) -> Optional[ImmutablePriority]:
        """
        Returns a priority with the given key.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            key (str): The key of the priority.

        Returns:
            Optional[ImmutablePriority]: The priority with the given key if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if the flashcard is already in the cache
                if self.is_key_in_cache(key=key):
                    # Return the flashcard from the cache
                    return self.get_value_from_cache(key=key)

            # Get the flashcard with the given key from the database
            model: Optional[PriorityModel] = asyncio.run(
                PriorityModel.get_by(
                    column="key",
                    database=Constants.DATABASE_PATH,
                    value=key,
                )
            )

            # Return the priority if it exists
            if model is not None:
                # Convert the PriorityModel object to an ImmutablePriority object
                priority: ImmutablePriority = PriorityFactory.create_priority(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the priority to the cache
                self.add_to_cache(
                    key=priority.key,
                    value=priority,
                )

                # Return the priority
                return priority
            else:
                # Return None indicating that the priority does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_key' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_priority_by_uuid(
        self,
        uuid: str,
        force_refetch: bool = False,
    ) -> Optional[ImmutablePriority]:
        """
        Returns a priority with the given UUID.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            uuid (str): The UUID of the priority.

        Returns:
            Optional[ImmutablePriority]: The priority with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
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
                priority: ImmutablePriority = PriorityFactory.create_priority(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the priority to the cache
                self.add_to_cache(
                    key=priority.key,
                    value=priority,
                )

                # Return the priority
                return priority
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

    def search_priorities(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[Union[List[ImmutablePriority]]]:
        """
        Searches for priorities in the database.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            **kwargs: Any additional keyword arguments to be passed to the search method of the PriorityModel class.

        Returns:
            Optional[Union[List[ImmutablePriority]]]: The found priorities if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Search the stack for the passed keyword arguments
                cached_result: Optional[List[ImmutablePriority]] = self.search_cache(
                    **kwargs
                )

                # Check, if any cached results exist
                if cached_result:
                    # Return the cached results
                    return cached_result

            # Search for priorities in the database
            models: Optional[List[PriorityModel]] = asyncio.run(
                PriorityModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found priorities if any
            if models is not None and len(models) > 0:
                priorities: List[ImmutablePriority] = [
                    PriorityFactory.create_priority(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                    for model in models
                ]

                # Add the priorities to the cache
                self.add_to_cache(
                    key=[priority.key for priority in priorities],
                    value=priorities,
                )

                # Return the priorities
                return priorities
            else:
                # Return None indicating that no priorities were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
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
                    object=ImmutablePriority(
                        **priority.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).update(
                    database=Constants.DATABASE_PATH,
                    **priority.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Return the updated priority if it exists
            if model is not None:
                # Convert the PriorityModel object to an ImmutablePriority object
                priority: ImmutablePriority = PriorityFactory.create_priority(
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
        id (int): The ID of the priority.
        created_at (datetime): The timestamp when the priority was created.
        description (str): The description of the priority.
        emoji (str): The emoji of the priority.
        icon (str): The icon of the priority. Defaults to "🔥".
        key (str): The key of the priority.
        metadata (Dict[str, Any]): The metadata of the priority.
        name (str): The name of the priority.
        updated_at (datetime): The timestamp when the priority was last updated.
        uuid (str): The UUID of the priority.
        value (float): The value of the priority.
    """

    table: Final[str] = Constants.PRIORITIES

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
        autoincrement=False,
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

    description: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        index=False,
        name="description",
        nullable=False,
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
        index=False,
        name="emoji",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=True,
    )

    icon: Field = Field(
        autoincrement=False,
        default="🔥",
        description="",
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
        index=False,
        name="metadata",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
        unique=False,
    )

    name: Field = Field(
        autoincrement=False,
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
        autoincrement=False,
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
        autoincrement=False,
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
        autoincrement=False,
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
        description: Optional[str] = None,
        emoji: Optional[str] = None,
        icon: Optional[str] = "🔥",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
        value: Optional[float] = None,
    ) -> None:
        """
        Initializes a new instance of the PriorityModel class.

        Args:
            created_at (Optional[datetime]): The timestamp when the priority was created.
            description (Optional[str]): The description of the priority.
            emoji (Optional[str]): The emoji of the priority.
            icon (Optional[str]): The icon of the priority. Defaults to "🔥".
            id (Optional[int]): The ID of the priority.
            key (Optional[str]): The key of the priority.
            metadata (Optional[Dict[str, Any]]): The metadata of the priority.
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
            description=description,
            emoji=emoji,
            icon="🔥",
            id=id,
            key=key,
            metadata=metadata,
            name=name,
            table=Constants.PRIORITIES,
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )
