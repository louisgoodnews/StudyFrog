"""
Author: lodego
Date: 2025-02-05
"""

import asyncio
import traceback

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
    "ImmutableDifficulty",
    "MutableDifficulty",
    "DifficultyConverter",
    "DifficultyFactory",
    "DifficultyManager",
    "DifficultyModel",
]


class ImmutableDifficulty(ImmutableBaseObject):
    """
    An immutable class representing a difficulty.

    A difficulty has a value between 0 and 1 that represents the importance of an object.

    Attributes:
        created_at (datetime): The timestamp when the difficulty was created.
        description (Optional[str]): The description of the difficulty.
        emoji (str): The emoji of the difficulty.
        icon (str): The icon of the difficulty.
        id (int): The ID of the difficulty.
        key (str): The key of the difficulty.
        metadata (Dict[str, Any]): The metadata of the difficulty.
        name (str): The name of the difficulty.
        updated_at (datetime): The timestamp when the difficulty was last updated.
        uuid (str): The UUID of the difficulty.
        value (float): The value of the difficulty.
    """

    def __init__(
        self,
        emoji: str,
        name: str,
        value: float,
        created_at: Optional[datetime] = None,
        description: Optional[str] = None,
        icon: Optional[str] = "⭐",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the Difficulty class.

        Args:
            created_at (Optional[datetime]): The timestamp when the difficulty was created.
            description (Optional[str]): The description of the difficulty.
            emoji (str): The emoji of the difficulty.
            icon (Optional[str]): The icon of the difficulty. Defaults to "⭐".
            id (Optional[int]): The ID of the difficulty.
            key (Optional[str]): The key of the difficulty.
            metadata (Optional[Dict[str, Any]]): The metadata of the difficulty.
            name (str): The name of the difficulty.
            updated_at (Optional[datetime]): The timestamp when the difficulty was last updated.
            uuid (Optional[str]): The UUID of the difficulty.
            value (float): The value of the difficulty.

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
        Returns the timestamp when the difficulty was created.

        Returns:
            datetime: The timestamp when the difficulty was created.
        """

        # Return the timestamp when the difficulty was created
        return self._created_at

    @property
    def description(self) -> str:
        """
        Returns the description of the difficulty.

        Returns:
            str: The description of the difficulty.
        """

        # Return the description of the difficulty
        return self._description

    @property
    def emoji(self) -> str:
        """
        Returns the emoji of the difficulty.

        Returns:
            str: The emoji of the difficulty.
        """

        # Return the emoji of the difficulty
        return self._emoji

    @property
    def icon(self) -> str:
        """
        Returns the icon of the difficulty.

        Returns:
            str: The icon of the difficulty.
        """

        # Return the icon of the difficulty
        return self._icon

    @property
    def id(self) -> int:
        """
        Returns the ID of the difficulty.

        Returns:
            int: The ID of the difficulty.
        """

        # Return the ID of the difficulty
        return self._id

    @property
    def key(self) -> str:
        """
        Returns the key of the difficulty.

        Returns:
            str: The key of the difficulty.
        """

        # Return the key of the difficulty
        return self._key

    @property
    def metadata(self) -> Optional[Dict[str, Any]]:
        """
        Returns the metadata of the difficulty.

        Returns:
            Optional[Dict[str, Any]]: The metadata of the difficulty.
        """

        # Return the metadata of the difficulty
        return self._metadata

    @property
    def name(self) -> str:
        """
        Returns the name of the difficulty.

        Returns:
            str: The name of the difficulty.
        """

        # Return the name of the difficulty
        return self._name

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp when the difficulty was last updated.

        Returns:
            datetime: The timestamp when the difficulty was last updated.
        """

        # Return the timestamp when the difficulty was last updated
        return self._updated_at

    @property
    def uuid(self) -> str:
        """
        Returns the UUID of the difficulty.

        Returns:
            str: The UUID of the difficulty.
        """

        # Return the UUID of the difficulty
        return self._uuid

    @property
    def value(self) -> float:
        """
        Returns the value of the difficulty.

        Returns:
            float: The value of the difficulty.
        """

        # Return the value of the difficulty
        return self._value

    def to_mutable(self) -> "MutableDifficulty":
        """
        Converts the immutable difficulty to a mutable difficulty.

        Returns:
            MutableDifficulty: The mutable difficulty.
        """
        try:
            # Attempt to create and return a new instance of the MutableDifficulty class
            return MutableDifficulty(
                **self.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_mutable' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e


class MutableDifficulty(MutableBaseObject):
    """
    A mutable class representing a difficulty.

    A difficulty has a value between 0 and 1 that represents the importance of an object.

    Attributes:
        created_at (datetime): The timestamp when the difficulty was created.
        description (Optional[str]): The description of the difficulty.
        emoji (str): The emoji of the difficulty.
        icon (str): The icon of the difficulty.
        id (int): The ID of the difficulty.
        key (str): The key of the difficulty.
        metadata (Dict[str, Any]): The metadata of the difficulty.
        name (str): The name of the difficulty.
        updated_at (datetime): The timestamp when the difficulty was last updated.
        uuid (str): The UUID of the difficulty.
        value (float): The value of the difficulty.
    """

    def __init__(
        self,
        emoji: str,
        name: str,
        value: float,
        created_at: Optional[datetime] = None,
        description: Optional[str] = None,
        icon: Optional[str] = "⭐",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableDifficulty class.

        Args:
            created_at (Optional[datetime]): The timestamp when the difficulty was created.
            description (Optional[str]): The description of the difficulty.
            emoji (str): The emoji of the difficulty.
            icon (Optional[str]): The icon of the difficulty. Defaults to "⭐".
            id (Optional[int]): The ID of the difficulty.
            key (Optional[str]): The key of the difficulty.
            metadata (Optional[Dict[str, Any]]): The metadata of the difficulty.
            name (str): The name of the difficulty.
            updated_at (Optional[datetime]): The timestamp when the difficulty was last updated.
            uuid (Optional[str]): The UUID of the difficulty.
            value (float): The value of the difficulty.

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
        Returns the timestamp when the difficulty was created.

        Returns:
            datetime: The timestamp when the difficulty was created.
        """

        # Return the timestamp when the difficulty was created
        return self._created_at

    @created_at.setter
    def created_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the timestamp when the difficulty was created.

        Args:
            value (datetime): The timestamp when the difficulty was created.

        Returns:
            None
        """

        # Set the timestamp when the difficulty was created
        self._created_at = value

    @property
    def description(self) -> str:
        """
        Returns the description of the difficulty.

        Returns:
            str: The description of the difficulty.
        """

        # Return the description of the difficulty
        return self._description

    @description.setter
    def description(
        self,
        value: str,
    ) -> None:
        """
        Sets the description of the difficulty.

        Args:
            value (str): The description of the difficulty.

        Returns:
            None
        """

        # Set the description of the difficulty
        self._description = value

    @property
    def emoji(self) -> str:
        """
        Returns the emoji of the difficulty.

        Returns:
            str: The emoji of the difficulty.
        """

        # Return the emoji of the difficulty
        return self._emoji

    @emoji.setter
    def emoji(
        self,
        value: str,
    ) -> None:
        """
        Sets the emoji of the difficulty.

        Args:
            value (str): The emoji of the difficulty.

        Returns:
            None
        """

        # Set the emoji of the difficulty
        self._emoji = value

    @property
    def icon(self) -> str:
        """
        Returns the icon of the difficulty.

        Returns:
            str: The icon of the difficulty.
        """

        # Return the icon of the difficulty
        return self._icon

    @icon.setter
    def icon(
        self,
        value: str,
    ) -> None:
        """
        Sets the icon of the difficulty.

        Args:
            value (str): The icon of the difficulty.

        Returns:
            None
        """

        # Set the icon of the difficulty
        self._icon = value

    @property
    def id(self) -> int:
        """
        Returns the ID of the difficulty.

        Returns:
            int: The ID of the difficulty.
        """

        # Return the ID of the difficulty
        return self._id

    @id.setter
    def id(
        self,
        value: int,
    ) -> None:
        """
        Sets the ID of the difficulty.

        Args:
            value (int): The ID of the difficulty.

        Returns:
            None
        """

        # Set the ID of the difficulty
        self._id = value

    @property
    def key(self) -> str:
        """
        Returns the key of the difficulty.

        Returns:
            str: The key of the difficulty.
        """

        # Return the key of the difficulty
        return self._key

    @key.setter
    def key(
        self,
        value: str,
    ) -> None:
        """
        Sets the key of the difficulty.

        Args:
            value (str): The key of the difficulty.

        Returns:
            None
        """

        # Set the key of the difficulty
        self._key = value

    @property
    def metadata(self) -> Dict[str, Any]:
        """
        Returns the metadata of the difficulty.

        Returns:
            Dict[str, Any]: The metadata of the difficulty.
        """

        # Return the metadata of the difficulty
        return self._metadata

    @metadata.setter
    def metadata(
        self,
        value: Dict[str, Any],
    ) -> None:
        """
        Sets the metadata of the difficulty.

        Args:
            value (Dict[str, Any]): The metadata of the difficulty.

        Returns:
            None
        """

        # Set the metadata of the difficulty
        self._metadata = value

    @property
    def name(self) -> str:
        """
        Returns the name of the difficulty.

        Returns:
            str: The name of the difficulty.
        """

        # Return the name of the difficulty
        return self._name

    @name.setter
    def name(
        self,
        value: str,
    ) -> None:
        """
        Sets the name of the difficulty.

        Args:
            value (str): The name of the difficulty.

        Returns:
            None
        """

        # Set the name of the difficulty
        self._name = value

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp when the difficulty was last updated.

        Returns:
            datetime: The timestamp when the difficulty was last updated.
        """

        # Return the timestamp when the difficulty was last updated
        return self._updated_at

    @updated_at.setter
    def updated_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the timestamp when the difficulty was last updated.

        Args:
            value (datetime): The timestamp when the difficulty was last updated.

        Returns:
            None
        """

        # Set the timestamp when the difficulty was last updated
        self._updated_at = value

    @property
    def uuid(self) -> str:
        """
        Returns the UUID of the difficulty.

        Returns:
            str: The UUID of the difficulty.
        """

        # Return the UUID of the difficulty
        return self._uuid

    @uuid.setter
    def uuid(
        self,
        value: str,
    ) -> None:
        """
        Sets the UUID of the difficulty.

        Args:
            value (str): The UUID of the difficulty.

        Returns:
            None
        """

        # Set the UUID of the difficulty
        self._uuid = value

    @property
    def value(self) -> float:
        """
        Returns the value of the difficulty.

        Returns:
            float: The value of the difficulty.
        """

        # Return the value of the difficulty
        return self._value

    @value.setter
    def value(
        self,
        value: float,
    ) -> None:
        """
        Sets the value of the difficulty.

        Args:
            value (float): The value of the difficulty.

        Returns:
            None
        """

        # Set the value of the difficulty
        self._value = value

    def to_immutable(self) -> ImmutableDifficulty:
        """
        Converts the mutable difficulty to an immutable difficulty.

        Returns:
            ImmutableDifficulty: The immutable difficulty.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableDifficulty class
            return ImmutableDifficulty(
                **self.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_immutable' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e


class DifficultyConverter:
    """
    A converter class for transforming between DifficultyModel and Difficulty instances.

    This class provides methods to convert a DifficultyModel instance to an Difficulty instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the DifficultyConverter class.
    """

    logger: Final[Logger] = Logger.get_logger(name="DifficultyConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "DifficultyModel",
    ) -> Optional[ImmutableDifficulty]:
        """
        Converts a given DifficultyModel instance to an ImmutableDifficulty instance.

        Args:
            model (DifficultyModel): The DifficultyModel instance to be converted.

        Returns:
            ImmutableDifficulty: The converted ImmutableDifficulty instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the DifficultyModel instance.
        """
        try:
            # Attempt to create and return a new instance of the Difficulty class from the dictionary representation of the DifficultyModel instance
            return ImmutableDifficulty(
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

            # Log the traceback
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def object_to_model(
        cls,
        object: ImmutableDifficulty,
    ) -> Optional["DifficultyModel"]:
        """
        Converts a given ImmutableDifficulty instance to a DifficultyModel instance.

        Args:
            object (ImmutableDifficulty): The ImmutableDifficulty instance to be converted.

        Returns:
            DifficultyModel: The converted DifficultyModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the Difficulty instance.
        """
        try:
            # Attempt to create and return a new instance of the DifficultyModel class from the dictionary representation of the Difficulty instance
            return DifficultyModel(
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

            # Log the traceback
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None


class DifficultyFactory:
    """
    Factory class for creating Difficulty instances.

    Attributes:
        logger (Logger): The logger instance associated with the DifficultyFactory class.
    """

    logger: Final[Logger] = Logger.get_logger(name="DifficultyFactory")

    @classmethod
    def create_difficulty(
        cls,
        emoji: str,
        name: str,
        value: float,
        created_at: Optional[datetime] = None,
        description: Optional[str] = None,
        icon: Optional[str] = "⭐",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutableDifficulty]:
        """
        Creates a new instance of the Difficulty class.

        Args:
            created_at (Optional[datetime]): The timestamp when the difficulty was created.
            description (Optional[str]): The description of the difficulty.
            emoji (str): The emoji of the difficulty.
            icon (Optional[str]): The icon of the difficulty. Defaults to "⭐".
            id (Optional[int]): The ID of the difficulty.
            key (Optional[str]): The key of the difficulty.
            metadata (Optional[Dict[str, Any]]): The metadata of the difficulty.
            name (str): The name of the difficulty.
            updated_at (Optional[datetime]): The timestamp when the difficulty was last updated.
            uuid (Optional[str]): The UUID of the difficulty.
            value (float): The value of the difficulty.

        Returns:
            Optional[ImmutableDifficulty]: The new instance of the Difficulty class.
        """
        try:
            # Attempt to create and return a Difficulty object
            return ImmutableDifficulty(
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
                message=f"Caught an exception while attempting to run 'create_difficulty' method from '{cls.__name__}': {e}"
            )

            # Log the traceback
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None


class DifficultyBuilder(BaseObjectBuilder):
    """ """

    def __init__(self) -> None:
        """ """

        # Call the parent class constructor
        super().__init__()

    @override
    def build(
        self,
        as_mutable: bool = False,
    ) -> Optional[
        Union[
            ImmutableDifficulty,
            MutableDifficulty,
        ]
    ]:
        """
        Builds a new instance of the Difficulty class.

        Args:
            as_mutable (bool): A flag indicating whether to return a mutable instance of the Difficulty class. Defaults to False.

        Returns:
            Optional[Union[ImmutableDifficulty, MutableDifficulty]]: The new instance of the Difficulty class.

        Raises:
            Exception: If an exception occurs while attempting to build the Difficulty instance.
        """
        try:
            # Attempt to create a new ImmutableDifficulty instance
            difficulty: Optional[ImmutableDifficulty] = (
                DifficultyFactory.create_difficulty(**self.configuration)
            )

            # Check, if the difficulty exists
            if not difficulty:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create a new difficulty instance from the configuration: {self.configuration}"
                )

                # Return early
                return

            # Check, if the 'as_mutable' flag is set to True
            if as_mutable:
                # Convert the difficulty in to a MutableDifficulty instance and return it
                return difficulty.to_mutable()

            # Return the difficulty
            return difficulty
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'build' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    def created_at(
        self,
        value: datetime,
    ) -> Self:
        """
        Sets the created_at timestamp of the difficulty.

        Args:
            value (datetime): The created_at timestamp of the difficulty.

        Returns:
            Self: The instance of the DifficultyBuilder class.
        """

        # Set the created_at timestamp of the difficulty
        self._configuration["created_at"] = value

        # Return the instance
        return self

    def description(
        self,
        value: str,
    ) -> Self:
        """
        Sets the description of the difficulty.

        Args:
            value (str): The description of the difficulty.

        Returns:
            Self: The instance of the DifficultyBuilder class.
        """

        # Set the description of the difficulty
        self._configuration["description"] = value

        # Return the instance
        return self

    def emoji(
        self,
        value: str,
    ) -> Self:
        """
        Sets the emoji of the difficulty.

        Args:
            value (str): The emoji of the difficulty.

        Returns:
            Self: The instance of the DifficultyBuilder class.
        """

        # Set the emoji of the difficulty
        self._configuration["emoji"] = value

        # Return the instance
        return self

    def metadata(
        self,
        **kwargs,
    ) -> Self:
        """ """

        # Check, if the 'metadata' key exists in the configuration dictionary
        if "metadata" not in self._configuration:
            # Initialize the 'metadata' key with an empty dictionary
            self._configuration["metadata"] = {}

        # Update the 'metadata' key with the provided keyword arguments
        self._configuration["metadata"].update(kwargs)

        # Return the instance
        return self

    def name(
        self,
        value: str,
    ) -> Self:
        """
        Sets the name of the difficulty.

        Args:
            value (str): The name of the difficulty.

        Returns:
            Self: The instance of the DifficultyBuilder class.
        """

        # Set the name of the difficulty
        self._configuration["name"] = value

        # Return the instance
        return self

    def updated_at(
        self,
        value: datetime,
    ) -> Self:
        """
        Sets the updated_at timestamp of the difficulty.

        Args:
            value (datetime): The updated_at timestamp of the difficulty.

        Returns:
            Self: The instance of the DifficultyBuilder class.
        """

        # Set the updated_at timestamp of the difficulty
        self._configuration["updated_at"] = value

        # Return the instance
        return self


class DifficultyManager(BaseObjectManager):
    """
    A manager class for managing difficulties in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for difficulties.

    Attributes:
        cache: (List[Any]): The cache for storing difficulties.
        logger (Logger): The logger instance associated with the object.
    """

    _shared_instance: Optional["DifficultyManager"] = None

    def __new__(cls) -> "DifficultyManager":
        """
        Creates and returns a new instance of the DifficultyManager class.

        If the instance does not exist, creates a new one by calling the parent class
        constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Returns:
            DifficultyManager: The created or existing instance of DifficultyManager class.
        """
        if cls._shared_instance is None:
            # Create a new instance by calling the parent class constructor
            cls._shared_instance = super(DifficultyManager, cls).__new__(cls)
            # Initialize the instance
            cls._shared_instance.init()
        # Return the shared instance
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes a new instance of the DifficultyManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def _run_pre_create_tasks(
        self,
        difficulty: Union[
            ImmutableDifficulty,
            MutableDifficulty,
        ],
    ) -> MutableDifficulty:
        """
        Runs pre-create tasks for the difficulty.

        Args:
            difficulty (Union[ImmutableDifficulty, MutableDifficulty]): The difficulty to run pre-create tasks on.

        Returns:
            MutableDifficulty: The difficulty with pre-create tasks run.
        """

        # Check if the difficulty object is immutable
        if isinstance(
            difficulty,
            ImmutableDifficulty,
        ):
            # If it is, convert it to a mutable difficulty
            difficulty = MutableDifficulty(
                **difficulty.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )

        # Set the created_at timestamp of the difficulty
        difficulty.created_at = (
            difficulty.created_at or Miscellaneous.get_current_datetime()
        )

        # Set the key of the difficulty
        difficulty.key = f"DIFFICULTY_{self.count_difficulties() + 1}"

        # Set the updated_at timestamp of the difficulty
        difficulty.updated_at = (
            difficulty.updated_at or Miscellaneous.get_current_datetime()
        )

        # Set the uuid of the difficulty
        difficulty.uuid = Miscellaneous.get_uuid()

        # Return the difficulty object
        return difficulty

    def count_difficulties(self) -> int:
        """
        Returns the number of difficulties in the database.

        Returns:
            int: The number of difficulties in the database.
        """
        try:
            # Count and return the number of difficulties in the database
            return asyncio.run(DifficultyModel.count(database=Constants.DATABASE_PATH))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_difficulty(
        self,
        difficulty: Union[
            ImmutableDifficulty,
            MutableDifficulty,
        ],
    ) -> Optional[ImmutableDifficulty]:
        """
        Creates a new difficulty in the database.

        Args:
            difficulty (Union[ImmutableDifficulty, MutableDifficulty]): The difficulty to be created.

        Returns:
            Optional[ImmutableDifficulty]: The newly created immutable difficulty if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the difficulty.
        """
        try:
            # Initialize the result (optional) ImmutableDifficulty to none
            result: Optional[ImmutableDifficulty] = None

            # Run pre-create tasks
            difficulty: MutableDifficulty = self._run_pre_create_tasks(
                difficulty=difficulty
            )

            # Convert the difficulty object to a DifficultyModel object
            model: DifficultyModel = DifficultyConverter.object_to_model(
                object=difficulty
            )

            # Create a new difficulty in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            # Check, if the ID is not None
            if not id:
                # Log a warning message indicating an error has occurred
                self.logger.warning(
                    message=f"It seems that an error has occured while attempting to create a difficulty ({difficulty.__repr__()}) in the database."
                )

                # Return early
                return

            # Convert the difficulty to a dictionary
            kwargs: Dict[str, Any] = difficulty.to_dict(
                exclude=[
                    "_logger",
                ]
            )

            # Set the ID of the difficulty
            kwargs["id"] = id

            # Create a new ImmutableDifficulty object
            result = DifficultyFactory.create_difficulty(**kwargs)

            # Check, if the result is not None
            if not result:
                # Log an error message indicating an error has occurred
                self.logger.error(
                    message=f"It seems that there was an error while attempting to create an ImmutableDifficulty from the dictionary ({kwargs}) returned by the database. This is likely a serious issue."
                )

                # Return early
                return

            # Add the difficulty to the cache
            self.add_to_cache(
                key=result.key,
                value=result,
            )

            # Return the newly created immutable difficulty
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_difficulty' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete_difficulty(
        self,
        difficulty: ImmutableDifficulty,
    ) -> bool:
        """
        Deletes a difficulty from the database.

        Args:
            difficulty (ImmutableDifficulty): The difficulty to be deleted.

        Returns:
            bool: True if the difficulty was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the difficulty to an immutable difficulty and delete the difficulty from the database
            result: bool = asyncio.run(
                DifficultyConverter.object_to_model(
                    object=ImmutableDifficulty(
                        **difficulty.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).delete()
            )

            # Return True if the difficulty was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all_difficulties(
        self,
        force_refetch: bool = False,
    ) -> Optional[List[ImmutableDifficulty]]:
        """
        Returns a list of all difficulties in the database.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.

        Returns:
            Optional[List[ImmutableDifficulty]]: A list of all difficulties in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if cache and table size are equal
                if self.cache and len(self._cache) == self.count_difficulties():
                    # Return the list of immutable difficulties from the cache
                    return self.get_cache_values()

            # Get all difficulties from the database
            models: List[DifficultyModel] = asyncio.run(
                DifficultyModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of DifficultyModel objects to a list of Difficulty objects
            difficulties: List[ImmutableDifficulty] = [
                ImmutableDifficulty(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable difficulties
            for difficulty in difficulties:
                if not self.is_key_in_cache(key=difficulty.key):
                    # Add the immutable difficulty to the cache
                    self.add_to_cache(
                        key=difficulty.key,
                        value=difficulty,
                    )
                else:
                    # Update the immutable difficulty in the cache
                    self.update_in_cache(
                        key=difficulty.key,
                        value=difficulty,
                    )

            # Return the list of immutable difficulties
            return difficulties
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_default_difficulties(self) -> Optional[List[ImmutableDifficulty]]:
        """
        Retrieves the default difficulties from the database.

        Returns:
            Optional[List[ImmutableDifficulty]]: A list of default difficulties if no exception occurs. Otherwise, None.

        Raises:
            Exception: If no 'difficulty' defaults are found or any other exception occurs.
        """
        try:
            # Import necessary classes
            from core.default import ImmutableDefault, DefaultManager

            # Initialize an empty list to store the difficulties
            result: List[ImmutableDifficulty] = []

            # Retrieve defaults with the name 'difficulty'
            defaults: Optional[List[ImmutableDefault]] = [
                DefaultManager().get_default_by(
                    field="name",
                    value=f"difficulty:{difficulty}",
                )
                for difficulty in [
                    Constants.HARD,
                    Constants.MEDIUM,
                    Constants.EASY,
                ]
            ]

            # Raise exception if no defaults are found
            if not defaults:
                raise Exception("Found no 'difficulty' defaults in the database.")

            # Iterate over each default
            for default in defaults:
                # Check if the difficulty already exists
                existing_difficulty: Optional[ImmutableDifficulty] = (
                    self.get_difficulty_by(
                        field="name",
                        value=default.value,
                    )
                )

                if not existing_difficulty:
                    # Create a new difficulty if it doesn't exist
                    difficulty: ImmutableDifficulty = (
                        DifficultyFactory.create_difficulty(
                            emoji=(
                                "⭐"
                                if default.value.lower() == Constants.EASY
                                else (
                                    "⭐⭐"
                                    if default.value.lower() == Constants.MEDIUM
                                    else "⭐⭐⭐"
                                )
                            ),
                            name=default.value,
                            value=(
                                float(1 / 3)
                                if default.value.lower() == Constants.EASY
                                else (
                                    float(2 / 3)
                                    if default.value.lower() == Constants.MEDIUM
                                    else 1.0
                                )
                            ),
                        )
                    )

                    # Add the newly created difficulty to the result
                    result.append(self.create_difficulty(difficulty=difficulty))
                else:
                    # If the difficulty exists, retrieve it from the database
                    result.append(existing_difficulty)

            # Return the list of difficulties
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_default_difficulties' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_difficulty_by(
        self,
        field: str,
        value: Any,
        force_refetch: bool = False,
    ) -> Optional[ImmutableDifficulty]:
        """
        Retrieves a difficulty by the given field and value.

        Args:
            field (str): The field to search by.
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            value (Any): The value to search for.

        Returns:
            Optional[ImmutableDifficulty]: The difficulty with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if the difficulty is already in the cache
                if self.is_key_in_cache(key=field):
                    # Return the difficulty from the cache
                    return self.get_value_from_cache(key=field)

            # Get the difficulty with the given field and value from the database
            model: Optional[DifficultyModel] = asyncio.run(
                DifficultyModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Return the difficulty if it exists
            if model is not None:
                # Convert the DifficultyModel object to an Difficulty object
                difficulty: ImmutableDifficulty = DifficultyFactory.create_difficulty(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the difficulty to the cache
                self.add_to_cache(
                    key=difficulty.key,
                    value=difficulty,
                )

                # Return the difficulty
                return difficulty
            else:
                # Return None indicating that the difficulty does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_difficulty_by_id(
        self,
        id: int,
        force_refetch: bool = False,
    ) -> Optional[ImmutableDifficulty]:
        """
        Returns a difficulty with the given ID.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            id (int): The ID of the difficulty.

        Returns:
            Optional[ImmutableDifficulty]: The difficulty with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if the difficulty is already in the cache
                if self.is_key_in_cache(key=f"DIFFICULTY_{id}"):
                    # Return the difficulty from the cache
                    return self.get_value_from_cache(key=f"DIFFICULTY_{id}")

            # Get the difficulty with the given ID from the database
            model: Optional[DifficultyModel] = asyncio.run(
                DifficultyModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the difficulty if it exists
            if model is not None:
                # Convert the DifficultyModel object to an ImmutableDifficulty object
                difficulty: ImmutableDifficulty = DifficultyFactory.create_difficulty(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the difficulty to the cache
                self.add_to_cache(
                    key=difficulty.key,
                    value=difficulty,
                )

                # Return the difficulty
                return difficulty
            else:
                # Return None indicating that the difficulty does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_difficulty_by_key(
        self,
        key: str,
        force_refetch: bool = False,
    ) -> Optional[ImmutableDifficulty]:
        """
        Returns a difficulty with the given key.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            key (str): The ID of the difficulty.

        Returns:
            Optional[ImmutableDifficulty]: The difficulty with the given key if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if the difficulty is already in the cache
                if self.is_key_in_cache(key=key):
                    # Return the difficulty from the cache
                    return self.get_value_from_cache(key=key)

            # Get the difficulty with the given ID from the database
            model: Optional[DifficultyModel] = asyncio.run(
                DifficultyModel.get_by(
                    column="key",
                    database=Constants.DATABASE_PATH,
                    value=key,
                )
            )

            # Return the difficulty if it exists
            if model is not None:
                # Convert the DifficultyModel object to an ImmutableDifficulty object
                difficulty: ImmutableDifficulty = DifficultyFactory.create_difficulty(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the difficulty to the cache
                self.add_to_cache(
                    key=difficulty.key,
                    value=difficulty,
                )

                # Return the difficulty
                return difficulty
            else:
                # Return None indicating that the difficulty does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_key' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_difficulty_by_uuid(
        self,
        uuid: str,
        force_refetch: bool = False,
    ) -> Optional[ImmutableDifficulty]:
        """
        Returns a difficulty with the given UUID.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            uuid (str): The UUID of the difficulty.

        Returns:
            Optional[ImmutableDifficulty]: The difficulty with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if the difficulty is already in the cache
                if self.is_key_in_cache(key=uuid):
                    # Return the difficulty from the cache
                    return self.get_value_from_cache(key=uuid)

            # Get the difficulty with the given UUID from the database
            model: Optional[DifficultyModel] = asyncio.run(
                DifficultyModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the difficulty if it exists
            if model is not None:
                # Convert the DifficultyModel object to an ImmutableDifficulty object
                difficulty: ImmutableDifficulty = DifficultyFactory.create_difficulty(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the difficulty to the cache
                self.add_to_cache(
                    key=difficulty.key,
                    value=difficulty,
                )

                # Return the difficulty
                return difficulty
            else:
                # Return None indicating that the difficulty does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def search_difficulties(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[Union[List[ImmutableDifficulty]]]:
        """
        Searches for difficulties in the database.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            **kwargs: Any additional keyword arguments to be passed to the search method of the DifficultyModel class.

        Returns:
            Optional[Union[List[ImmutableDifficulty]]]: The found difficulties if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Search the stack for the passed keyword arguments
                cached_result: Optional[List[ImmutableDifficulty]] = self.search_cache(
                    **kwargs
                )

                # Check, if any cached results exist
                if cached_result:
                    # Return the cached results
                    return cached_result

            # Search for difficulties in the database
            models: Optional[List[DifficultyModel]] = asyncio.run(
                DifficultyModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found difficulties if any
            if models is not None and len(models) > 0:
                # Convert the models to ImmutableDifficulty objects
                difficulties: List[ImmutableDifficulty] = [
                    DifficultyFactory.create_difficulty(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                    for model in models
                ]

                # Add the difficulties to the cache
                self.add_to_cache(
                    key=[difficulty.key for difficulty in difficulties],
                    value=difficulties,
                )

                # Return the difficulties
                return difficulties
            else:
                # Return None indicating that no difficulties were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_difficulty(
        self,
        difficulty: ImmutableDifficulty,
    ) -> Optional[ImmutableDifficulty]:
        """
        Updates a difficulty with the given ID.

        Args:
            difficulty (ImmutableDifficulty): The difficulty to update.

        Returns:
            Optional[ImmutableDifficulty]: The updated difficulty if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the difficulty to an immutable difficulty and update the difficulty in the database
            model: Optional[DifficultyModel] = asyncio.run(
                DifficultyConverter.object_to_model(
                    object=ImmutableDifficulty(
                        **difficulty.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).update(
                    database=Constants.DATABASE_PATH,
                    **difficulty.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Return the updated difficulty if it exists
            if model is not None:
                # Convert the DifficultyModel object to an Difficulty object
                difficulty = ImmutableDifficulty(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the difficulty to the cache
                self.update_in_cache(
                    key=difficulty.key,
                    value=difficulty,
                )

                # Return the updated difficulty
                return difficulty
            else:
                # Return None indicating that the difficulty does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class DifficultyModel(ImmutableBaseModel):
    """
    A model class representing a difficulty.

    A difficulty has a value between 0 and 1 that represents the importance of an object.

    Attributes:
        id (int): The ID of the difficulty.
        created_at (datetime): The timestamp when the difficulty was created.
        description (str): The description of the difficulty.
        emoji (str): The emoji of the difficulty.
        icon (str): The icon of the difficulty. Defaults to "⭐".
        key (str): The key of the difficulty.
        metadata (Dict[str, Any]): The metadata of the difficulty.
        name (str): The name of the difficulty.
        value (float): The value of the difficulty.
        updated_at (datetime): The timestamp when the difficulty was last updated.
        uuid (str): The UUID of the difficulty.
    """

    table: Final[str] = Constants.DIFFICULTIES

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
        index=False,
        name="description",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=True,
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
        default="⭐",
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
        icon: Optional[str] = "⭐",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
        value: Optional[float] = None,
    ) -> None:
        """
        Initializes a new instance of the DifficultyModel class.

        Args:
            created_at (Optional[datetime]): The timestamp when the difficulty was created.
            description (Optional[str]): The description of the difficulty.
            emoji (Optional[str]): The emoji of the difficulty.
            icon (Optional[str]): The icon of the difficulty. Defaults to "⭐".
            id (Optional[int]): The ID of the difficulty.
            key (Optional[str]): The key of the difficulty.
            metadata (Optional[Dict[str, Any]]): The metadata of the difficulty.
            name (Optional[str]): The name of the difficulty.
            updated_at (Optional[datetime]): The timestamp when the difficulty was last updated.
            uuid (Optional[str]): The UUID of the difficulty.
            value (Optional[float]): The value of the difficulty.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            description=description,
            emoji=emoji,
            icon="⭐",
            id=id,
            key=key,
            metadata=metadata,
            name=name,
            table=Constants.DIFFICULTIES,
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )
