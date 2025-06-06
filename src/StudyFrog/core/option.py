"""
Author: lodego
Date: 2025-02-09
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
    "ImmutableOption",
    "MutableOption",
    "OptionConverter",
    "OptionFactory",
    "OptionManager",
    "OptionModel",
]


class ImmutableOption(ImmutableBaseObject):
    """
    An immutable class representing an Option.

    Attributes:
        created_at (Optional[datetime]): The timestamp when the Option was created.
        icon (Optional[str]): The icon of the Option.
        id (Optional[int]): The ID of the Option.
        key (Optional[str]): The key of the Option.
        metadata (Optional[Dict[str, Any]]): The metadata of the Option.
        updated_at (Optional[datetime]): The timestamp when the Option was last updated.
        uuid (Optional[str]): The UUID of the Option.
        value (Union[float, int, str]): The value of the Option.
    """

    def __init__(
        self,
        value: Union[float, int, str],
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "🎚️",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableOption class.

        Args:
            value (Union[float, int, str]): The value of the instance.
            created_at (Optional[datetime]): The timestamp when the instance was created.
            icon (Optional[str]): The icon of the instance. Defaults to "🎚️".
            id (Optional[int]): The ID of the instance.
            key (Optional[str]): The key of the instance.
            metadata (Optional[Dict[str, Any]]): The metadata of the instance.
            updated_at (Optional[datetime]): The timestamp when the instance was last updated.
            uuid (Optional[str]): The UUID of the instance.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            hide_attributes=True,
            icon=icon,
            id=id,
            key=key,
            metadata=metadata,
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )

    @property
    def created_at(self) -> datetime:
        """
        Returns the timestamp when the Option was created.

        Returns:
            datetime: The timestamp when the Option was created.
        """

        # Return the created_at attribute
        return self._created_at

    @property
    def icon(self) -> str:
        """
        Returns the icon of the Option.

        Returns:
            str: The icon of the Option.
        """

        # Return the icon attribute
        return self._icon

    @property
    def id(self) -> int:
        """
        Returns the ID of the Option.

        Returns:
            int: The ID of the Option.
        """

        # Return the id attribute
        return self._id

    @property
    def key(self) -> str:
        """
        Returns the key of the Option.

        Returns:
            str: The key of the Option.
        """

        # Return the key attribute
        return self._key

    @property
    def metadata(self) -> Dict[str, Any]:
        """
        Returns the metadata of the Option.

        Returns:
            Dict[str, Any]: The metadata of the Option.
        """

        # Return the metadata attribute
        return self._metadata

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp when the Option was last updated.

        Returns:
            datetime: The timestamp when the Option was last updated.
        """

        # Return the updated_at attribute
        return self._updated_at

    @property
    def uuid(self) -> str:
        """
        Returns the UUID of the Option.

        Returns:
            str: The UUID of the Option.
        """

        # Return the uuid attribute
        return self._uuid

    @property
    def value(self) -> Union[float, int, str]:
        """
        Returns the value of the Option.

        Returns:
            Union[float, int, str]: The value of the Option.
        """

        # Return the value attribute
        return self._value

    def to_mutable(self) -> "MutableOption":
        """
        Returns a new instance of the MutableOption class with the same attributes as this instance.

        Returns:
            MutableOption: A new instance of the MutableOption class with the same attributes as this instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of the MutableOption class.
        """
        try:
            # Attempt to create and return a new instance of the MutableOption class with the same attributes as this instance
            return MutableOption(
                **self.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log the exception
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_mutable' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None
            return None


class MutableOption(MutableBaseObject):
    """
    A mutable class representing an Option.

    Attributes:
        created_at (Optional[datetime]): The timestamp when the Option was created.
        icon (Optional[str]): The icon of the Option.
        id (Optional[int]): The ID of the Option.
        key (Optional[str]): The key of the Option.
        metadata (Optional[Dict[str, Any]]): The metadata of the Option.
        updated_at (Optional[datetime]): The timestamp when the Option was last updated.
        uuid (Optional[str]): The UUID of the Option.
        value (Union[float, int, str]): The value of the Option.
    """

    def __init__(
        self,
        value: Union[float, int, str],
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "🎚️",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableOption class.

        Args:
            value (Union[float, int, str]): The value of the instance.
            created_at (Optional[datetime]): The timestamp when the instance was created.
            icon (Optional[str]): The icon of the instance. Defaults to "🎚️".
            id (Optional[int]): The ID of the instance.
            key (Optional[str]): The key of the instance.
            metadata (Optional[Dict[str, Any]]): The metadata of the instance.
            updated_at (Optional[datetime]): The timestamp when the instance was last updated.
            uuid (Optional[str]): The UUID of the instance.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            hide_attributes=True,
            icon=icon,
            id=id,
            key=key,
            metadata=metadata,
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )

    @property
    def created_at(self) -> datetime:
        """
        Returns the timestamp when the Option was created.

        Returns:
            datetime: The timestamp when the Option was created.
        """

        # Return the created_at attribute
        return self._created_at

    @created_at.setter
    def created_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the timestamp when the Option was created.

        Args:
            value (datetime): The timestamp when the Option was created.

        Returns:
            None
        """

        # Set the created_at attribute
        self._created_at = value

    @property
    def icon(self) -> str:
        """
        Returns the icon of the Option.

        Returns:
            str: The icon of the Option.
        """

        # Return the icon attribute
        return self._icon

    @icon.setter
    def icon(
        self,
        value: str,
    ) -> None:
        """
        Sets the icon of the Option.

        Args:
            value (str): The icon of the Option.

        Returns:
            None
        """

        # Set the icon attribute
        self._icon = value

    @property
    def id(self) -> int:
        """
        Returns the ID of the Option.

        Returns:
            int: The ID of the Option.
        """

        # Return the id attribute
        return self._id

    @id.setter
    def id(
        self,
        value: int,
    ) -> None:
        """
        Sets the ID of the Option.

        Args:
            value (int): The ID of the Option.

        Returns:
            None
        """

        # Set the id attribute
        self._id = value

    @property
    def key(self) -> str:
        """
        Returns the key of the Option.

        Returns:
            str: The key of the Option.
        """

        # Return the key attribute
        return self._key

    @key.setter
    def key(
        self,
        value: str,
    ) -> None:
        """
        Sets the key of the Option.

        Args:
            value (str): The key of the Option.

        Returns:
            None
        """

        # Set the key attribute
        self._key = value

    @property
    def metadata(self) -> Dict[str, Any]:
        """
        Returns the metadata of the Option.

        Returns:
            Dict[str, Any]: The metadata of the Option.
        """

        # Return the metadata attribute
        return self._metadata

    @metadata.setter
    def metadata(
        self,
        **kwargs,
    ) -> None:
        """
        Updates the metadata of the Option.

        Args:
            **kwargs (Dict[str, Any]): The new metadata of the Option.

        Returns:
            None
        """

        # Check, if the metadata dictionary exists
        if not self.get(
            default=None,
            name="metadata",
        ):
            # Set the metadata of the learning session to an empty dictionary
            self._metadata = {}

        # Update the metadata of the learning session
        self._metadata.update(**kwargs)

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp when the Option was last updated.

        Returns:
            datetime: The timestamp when the Option was last updated.
        """

        # Return the updated_at attribute
        return self._updated_at

    @updated_at.setter
    def updated_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the timestamp when the Option was last updated.

        Args:
            value (datetime): The timestamp when the Option was last updated.

        Returns:
            None
        """

        # Set the updated_at attribute
        self._updated_at = value

    @property
    def uuid(self) -> str:
        """
        Returns the UUID of the Option.

        Returns:
            str: The UUID of the Option.
        """

        # Return the uuid attribute
        return self._uuid

    @uuid.setter
    def uuid(
        self,
        value: str,
    ) -> None:
        """
        Sets the UUID of the Option.

        Args:
            value (str): The UUID of the Option.

        Returns:
            None
        """

        # Set the uuid attribute
        self._uuid = value

    @property
    def value(self) -> Union[float, int, str]:
        """
        Returns the value of the Option.

        Returns:
            Union[float, int, str]: The value of the Option.
        """

        # Return the value attribute
        return self._value

    @value.setter
    def value(
        self,
        value: Union[float, int, str],
    ) -> None:
        """
        Sets the value of the Option.

        Args:
            value (Union[float, int, str]): The value of the Option.

        Returns:
            None
        """

        # Set the value attribute
        self._value = value

    def to_immutable(self) -> ImmutableOption:
        """
        Returns a new instance of the ImmutableOption class with the same attributes as this instance.

        Returns:
            ImmutableOption: A new instance of the ImmutableOption class with the same attributes as this instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableOption class with the same attributes as this instance
            return ImmutableOption(
                **self.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log the exception
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_immutable' method from '{self.__class__.__name__}' class: {e}",
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None
            return None


class OptionConverter:
    """
    A converter class for transforming between OptionModel and ImmutableOption instances.

    This class provides methods to convert a OptionModel instance to an ImmutableOption instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the OptionConverter class.
    """

    logger: Final[Logger] = Logger.get_logger(name="OptionConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "OptionModel",
    ) -> Optional[ImmutableOption]:
        """
        Converts a given OptionModel instance to an ImmutableOption instance.

        Args:
            model (OptionModel): The OptionModel instance to be converted.

        Returns:
            ImmutableOption: The converted ImmutableOption instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the OptionModel instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableOption class from the dictionary representation of the OptionModel instance
            return ImmutableOption(
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
        object: ImmutableOption,
    ) -> Optional["OptionModel"]:
        """
        Converts a given ImmutableOption instance to a OptionModel instance.

        Args:
            object (ImmutableOption): The ImmutableOption instance to be converted.

        Returns:
            OptionModel: The converted OptionModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ImmutableOption instance.
        """
        try:
            # Attempt to create and return a new instance of the OptionModel class from the dictionary representation of the ImmutableOption instance
            return OptionModel(
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


class OptionFactory:
    """
    A factory class for creating Option instances.

    Attributes:
        logger (Logger): The logger instance associated with the OptionFactory class.
    """

    logger: Final[Logger] = Logger.get_logger(name="OptionFactory")

    @classmethod
    def create_option(
        cls,
        value: str,
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "🎚️",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutableOption]:
        """
        Creates an ImmutableOption instance with the given parameters.

        Args:
            value (str): The value of the Option.
            created_at (Optional[datetime]): The timestamp when the Option was created.
            icon (Optional[str]): The icon of the Option. Defaults to "🎚️".
            id (Optional[int]): The ID of the Option.
            key (Optional[str]): The key of the Option.
            metadata (Optional[Dict[str, Any]]): The metadata of the Option.
            updated_at (Optional[datetime]): The timestamp when the Option was last updated.
            uuid (Optional[str]): The UUID of the Option.

        Returns:
            Optional[ImmutableOption]: A new instance of the ImmutableOption class if the creation was successful, otherwise None.

        Raises:
            Exception: If an exception occurs while creating the ImmutableOption instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableOption class
            return ImmutableOption(
                value=value,
                created_at=created_at,
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
                message=f"Caught an exception while attempting to run 'create_option' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class OptionBuilder(BaseObjectBuilder):
    """
    A builder class for creating Option instances.

    This class extends the BaseObjectBuilder class and provides a method for creating Option instances.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the OptionBuilder class.

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
            ImmutableOption,
            MutableOption,
        ]
    ]:
        """
        Creates an Option instance with the given parameters.

        Args:
            as_mutable (bool): A flag indicating whether to create a MutableOption instance or an ImmutableOption instance. Defaults to False.

        Returns:
            Optional[Union[ImmutableOption, MutableOption]]: A new instance of the Option class if the creation was successful, otherwise None.

        Raises:
            Exception: If an exception occurs while creating the Option instance.
        """
        try:
            # Attempt to create a new ImmutableOption instance
            option: Optional[ImmutableOption] = OptionFactory.create_option(
                **self.configuration
            )

            # Check, if the ImmutableOption instance exists
            if not option:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create an instance of 'ImmutableOption' from '{self.__class__.__name__}' class"
                )

                # Return early
                return None

            # Check, if the 'as_mutable' flag is set to True
            if as_mutable:
                # Convert the option to a MutableOption instance and return it
                return option.to_mutable()

            # Return the Option instance
            return option
        except Exception as e:
            # Log an error message
            self.logger.error(
                message=f"Caught an exception while attempting to run 'build' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None
            return None

    def created_at(
        self,
        value: datetime,
    ) -> Self:
        """ """

        # Set the 'created_at' attribute
        self.configuration["created_at"] = value

        # Return the builder instance
        return self

    def metadata(
        self,
        value: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Self:
        """
        Sets the metadata of the Option.

        Args:
            value (Optional[Dict[str, Any]]): The metadata of the Option.
            **kwargs (Dict[str, Any]): The metadata of the Option.

        Returns:
            Self: The builder instance.
        """

        # Check, if the 'metadata' exists in the configuration dictionary
        if "metadata" not in self.configuration:
            # Set the 'metadata' attribute
            self.configuration["metadata"] = {}

        # Check, if the 'value' argument exists
        if value:
            # Set the 'metadata' attribute
            self.configuration["metadata"] = value

            # Return the builder instance early
            return self

        # Update the 'metadata' attribute with the keyword arguments
        self.configuration["metadata"].update(kwargs)

        # Return the builder instance
        return self

    def updated_at(
        self,
        value: datetime,
    ) -> Self:
        """
        Sets the timestamp when the Option was last updated.

        Args:
            value (datetime): The timestamp when the Option was last updated.

        Returns:
            Self: The builder instance.
        """

        # Set the 'updated_at' attribute
        self.configuration["updated_at"] = value

        # Return the builder instance
        return self


class OptionManager(BaseObjectManager):
    """
    A manager class for managing options in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for options.

    Attributes:
        cache: (List[Any]): The cache for storing options.
        logger (Logger): The logger instance associated with the object.
    """

    _shared_instance: Optional["OptionManager"] = None

    def __new__(cls) -> "OptionManager":
        """
        Creates and returns a new instance of the OptionManager class.

        If the instance does not exist, creates a new one by calling the parent class
        constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Returns:
            OptionManager: The created or existing instance of OptionManager class.
        """
        if cls._shared_instance is None:
            # Create a new instance by calling the parent class constructor
            cls._shared_instance = super(OptionManager, cls).__new__(cls)
            # Initialize the instance
            cls._shared_instance.init()
        # Return the shared instance
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes a new instance of the OptionManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def _run_pre_create_tasks(
        self,
        option: Union[
            ImmutableOption,
            MutableOption,
        ],
    ) -> MutableOption:
        """
        Runs pre-create tasks for the given option.

        Args:
            option (Union[ImmutableOption, MutableOption]): The option to run pre-create tasks for.

        Returns:
            MutableOption: The option with pre-create tasks run.
        """

        # Check if the option object is immutable
        if not option.is_mutable():
            # If it is, convert it to a mutable option
            option: MutableOption = option.to_mutable()

        # Set the created_at timestamp of the option
        option.created_at = Miscellaneous.get_current_datetime()

        # Set the key of the option
        option.key = f"OPTION_{self.count_options() + 1}"

        # Set the metadata of the option
        option.metadata = {} or option.metadata

        # Set the updated_at timestamp of the option
        option.updated_at = Miscellaneous.get_current_datetime()

        # Set the uuid of the option
        option.uuid = Miscellaneous.get_uuid()

        # Return the option
        return option

    def count_options(self) -> int:
        """
        Returns the number of options in the database.

        Returns:
            int: The number of options in the database.
        """
        try:
            # Count and return the number of options in the database
            return asyncio.run(OptionModel.count(database=Constants.DATABASE_PATH))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_option(
        self,
        option: Union[ImmutableOption, MutableOption],
    ) -> Optional[ImmutableOption]:
        """
        Creates a new option in the database.

        Args:
            option (Union[ImmutableOption, MutableOption]): The option to be created.

        Returns:
            Optional[ImmutableOption]: The newly created immutable option if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the option.
        """
        try:
            # Initialize the result (optional) ImmutableOption to none
            result: Optional[ImmutableOption] = None

            # Run pre-create tasks
            option: MutableOption = self._run_pre_create_tasks(option=option)

            # Convert the option object to a OptionModel object
            model: OptionModel = OptionConverter.object_to_model(object=option)

            # Create a new option in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            # Check, if the ID is not None
            if not id:
                # Log a warning message indicating an error has occurred
                self.logger.warning(
                    message=f"It seems that an error has occured while attempting to create an option ({option.__repr__()}) in the database."
                )

                # Return early
                return

            # Convert the option to a dictionary
            kwargs: Dict[str, Any] = option.to_dict(
                exclude=[
                    "_logger",
                ]
            )

            # Set the ID of the option
            kwargs["id"] = id

            # Create a new ImmutableOption object
            result = OptionFactory.create_option(**kwargs)

            # Check, if the result is not None
            if not result:
                # Log an error message indicating an error has occurred
                self.logger.error(
                    message=f"It seems that there was an error while attempting to create an ImmutableOption from the dictionary ({kwargs}) returned by the database. This is likely a serious issue."
                )

                # Return early
                return

            # Add the option to the cache
            self.add_to_cache(
                key=result.key,
                value=result,
            )

            # Return the newly created ImmutableOption instance
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_option' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete_option(
        self,
        option: Union[ImmutableOption, MutableOption],
    ) -> bool:
        """
        Deletes a option from the database.

        Args:
            option (Union[ImmutableOption, MutableOption]): The option to be deleted.

        Returns:
            bool: True if the option was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the option to an immutable option and delete the option from the database
            result: bool = asyncio.run(
                OptionConverter.object_to_model(
                    object=ImmutableOption(
                        **option.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).delete()
            )

            # Return True if the option was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all_options(self) -> Optional[List[ImmutableOption]]:
        """
        Returns a list of all options in the database.

        Returns:
            Optional[List[ImmutableOption]]: A list of all options in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if cache and table size are equal
            if self.cache and len(self._cache) == self.count_options():
                # Return the list of immutable options from the cache
                return self.get_cache_values()

            # Get all options from the database
            models: List[OptionModel] = asyncio.run(
                OptionModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of OptionModel objects to a list of ImmutableOption objects
            options: List[ImmutableOption] = [
                ImmutableOption(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable options
            for option in options:
                if not self.is_key_in_cache(key=option.key):
                    # Add the immutable option to the cache
                    self.add_to_cache(
                        key=option.key,
                        value=option,
                    )
                else:
                    # Update the immutable option in the cache
                    self.update_in_cache(
                        key=option.key,
                        value=option,
                    )

            # Return the list of immutable options
            return options
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_option_by(
        self,
        field: str,
        value: Any,
    ) -> Optional[ImmutableOption]:
        """
        Retrieves a option by the given field and value.

        Args:
            field (str): The field to search by.
            value (Any): The value to search for.

        Returns:
            Optional[ImmutableOption]: The option with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the option is already in the cache
            if self.is_key_in_cache(key=field):
                # Return the option from the cache
                return self.get_value_from_cache(key=field)

            # Get the option with the given field and value from the database
            model: Optional[OptionModel] = asyncio.run(
                OptionModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Return the option if it exists
            if model is not None:
                # Convert the OptionModel object to an ImmutableOption object
                return ImmutableOption(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the option does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_option_by_id(
        self,
        id: int,
    ) -> Optional[ImmutableOption]:
        """
        Returns a option with the given ID.

        Args:
            id (int): The ID of the option.

        Returns:
            Optional[ImmutableOption]: The option with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the option is already in the cache
            if self.is_key_in_cache(key=f"OPTION_{id}"):
                # Return the option from the cache
                return self.get_value_from_cache(key=f"OPTION_{id}")

            # Get the option with the given ID from the database
            model: Optional[OptionModel] = asyncio.run(
                OptionModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the option if it exists
            if model is not None:
                # Convert the OptionModel object to an ImmutableOption object
                return ImmutableOption(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the option does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_option_by_uuid(
        self,
        uuid: str,
    ) -> Optional[ImmutableOption]:
        """
        Returns a option with the given UUID.

        Args:
            uuid (str): The UUID of the option.

        Returns:
            Optional[ImmutableOption]: The option with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the option is already in the cache
            if self.is_key_in_cache(key=uuid):
                # Return the option from the cache
                return self.get_value_from_cache(key=uuid)

            # Get the option with the given UUID from the database
            model: Optional[OptionModel] = asyncio.run(
                OptionModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the option if it exists
            if model is not None:
                # Convert the OptionModel object to an ImmutableOption object
                return ImmutableOption(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the option does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def search_options(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[Union[List[ImmutableOption]]]:
        """
        Searches for options in the database.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            **kwargs: Any additional keyword arguments to be passed to the search method of the OptionModel class.

        Returns:
            Optional[Union[List[ImmutableOption]]]: The found options if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Search the stack for the passed keyword arguments
                cached_result: Optional[List[ImmutableOption]] = self.search_cache(
                    **kwargs
                )

                # Check, if any cached results exist
                if cached_result:
                    # Return the cached results
                    return cached_result

            # Search for options in the database
            models: Optional[List[OptionModel]] = asyncio.run(
                OptionModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found options if any
            if models is not None and len(models) > 0:
                return [
                    ImmutableOption(
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
                # Return None indicating that no options were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_option(
        self,
        option: Union[ImmutableOption, MutableOption],
    ) -> Optional[ImmutableOption]:
        """
        Updates a option with the given ID.

        Args:
            option (Union[ImmutableOption, MutableOption]): The option to update.

        Returns:
            Optional[ImmutableOption]: The updated option if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the option to an immutable option and update the option in the database
            model: Optional[OptionModel] = asyncio.run(
                OptionConverter.object_to_model(
                    object=ImmutableOption(
                        **option.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).update(
                    database=Constants.DATABASE_PATH,
                    **option.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Return the updated option if it exists
            if model is not None:
                # Convert the OptionModel object to an ImmutableOption object
                option = ImmutableOption(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the option to the cache
                self.update_in_cache(
                    key=option.key,
                    value=option,
                )

                # Return the updated option
                return option
            else:
                # Return None indicating that the option does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class OptionModel(ImmutableBaseModel):
    """
    Represents the structure of the option model.

    Attributes:
        created_at (Optional[datetime]): The timestamp when the option was created.
        icon (Optional[str]): The icon of the option. Defaults to "🎚️".
        id (Optional[int]): The ID of the option.
        key (Optional[str]): The key of the option.
        metadata (Optional[Dict[str, Any]]): The metadata of the option.
        updated_at (Optional[datetime]): The timestamp when the option was last updated.
        uuid (Optional[str]): The UUID of the option.
        value (Optional[str]): The value of the option.
    """

    table: Final[str] = Constants.OPTIONS

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
        default="🎚️",
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
        unique=True,
    )

    def __init__(
        self,
        id: Optional[int] = None,
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "🎚️",
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
        value: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the OptionModel class.

        Args:
            id (Optional[int]): The ID of the option.
            created_at (Optional[datetime]): The timestamp when the option was created.
            icon (Optional[str]): The icon of the option. Defaults to "🎚️".
            key (Optional[str]): The key of the option.
            metadata (Optional[Dict[str, Any]]): The metadata of the option.
            updated_at (Optional[datetime]): The timestamp when the option was last updated.
            uuid (Optional[str]): The UUID of the option.
            value (Optional[str]): The value of the option.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            icon="🎚️",
            id=id,
            key=key,
            metadata=metadata,
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )
