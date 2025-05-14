"""
Author: lodego
Date: 2025-04-23
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
    "ImmutableSubject",
    "MutableSubject",
    "SubjectConverter",
    "SubjectFactory",
    "SubjectBuilder",
    "SubjectManager",
    "SubjectModel",
]


class ImmutableSubject(ImmutableBaseObject):
    """
    An immutable class representing a subject.

    A subject is a category or topic that a subject, note or question (incl. Answer) belongs to.

    Attributes:
        name (str): The name of the subject.
        created_at (Optional[datetime], optional): The creation date and time of the subject. Defaults to None.
        custom_field_values (Optional[List[Dict[str, Any]]], optional): The custom field values of the subject. Defaults to None.
        description (Optional[str], optional): The description of the subject. Defaults to None.
        difficulty (Optional[int], optional): The subject level of the subject. Defaults to None.
        icon (Optional[str], optional): The icon associated with the subject. Defaults to "🧑‍🏫".
        id (Optional[int], optional): The unique identifier of the subject. Defaults to None.
        key (Optional[str], optional): The key associated with the subject. Defaults to None.
        metadata (Optional[Dict[str, Any]], optional): The metadata of the subject. Defaults to None.
        priority (Optional[int], optional): The priority level of the subject. Defaults to None.
        tags (Optional[List[str]], optional): The tags associated with the subject. Defaults to None.
        updated_at (Optional[datetime], optional): The last update date and time of the subject. Defaults to None.
        uuid (Optional[str], optional): The unique identifier of the subject. Defaults to None.
    """

    def __init__(
        self,
        name: str,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        description: Optional[str] = None,
        difficulty: Optional[int] = None,
        icon: Optional[str] = "🧑‍🏫",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        priority: Optional[int] = None,
        tags: Optional[List[str]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableSubject class.

        Args:
            name (str): The name of the subject.
            created_at (Optional[datetime], optional): The creation date and time of the subject. Defaults to None.
            custom_field_values (Optional[List[Dict[str, Any]], optional): The custom field values of the subject. Defaults to None.
            description (Optional[str], optional): The description of the subject. Defaults to None.
            difficulty (Optional[int], optional): The subject level of the subject. Defaults to None.
            icon (Optional[str], optional): The icon associated with the subject. Defaults to "🧑‍🏫".
            id (Optional[int], optional): The unique identifier of the subject. Defaults to None.
            key (Optional[str], optional): The key associated with the subject. Defaults to None.
            metadata (Optional[Dict[str, Any]], optional): The metadata of the subject. Defaults to None.
            priority (Optional[int], optional): The priority level of the subject. Defaults to None.
            tags (Optional[List[str]], optional): The tags associated with the subject. Defaults to None.
            updated_at (Optional[datetime], optional): The last update date and time of the subject. Defaults to None.
            uuid (Optional[str], optional): The unique identifier of the subject. Defaults to None.

        Returns:
            None
        """

        # Call the parent class constructor with the passed arguments
        super().__init__(
            created_at=created_at,
            custom_field_values=custom_field_values,
            description=description,
            difficulty=difficulty,
            hide_attributes=True,
            icon=icon,
            id=id,
            key=key,
            metadata=metadata,
            name=name,
            priority=priority,
            tags=tags,
            updated_at=updated_at,
            uuid=uuid,
        )

    @property
    def created_at(self) -> datetime:
        """
        Gets the creation date and time of the subject.

        Returns:
            datetime: The creation date and time of the subject
        """

        return self._created_at

    @property
    def custom_field_values(self) -> List[Dict[str, Any]]:
        """
        Gets the custom field values of the subject.

        Returns:
            List[Dict[str, Any]]: The custom field values of the subject
        """

        return self._custom_field_values

    @property
    def description(self) -> str:
        """
        Gets the description of the subject.

        Returns:
            str: The description of the subject
        """

        return self._description

    @property
    def difficulty(self) -> int:
        """
        Gets the difficulty level of the subject.

        Returns:
            int: The difficulty level of the subject.
        """

        return self._difficulty

    @property
    def icon(self) -> str:
        """
        Gets the icon of the subject.

        Returns:
            str: The icon of the subject
        """

        return self._icon

    @property
    def id(self) -> int:
        """
        Gets the ID of the subject.

        Returns:
            int: The ID of the subject
        """

        return self._id

    @property
    def key(self) -> str:
        """
        Gets the key of the subject.

        Returns:
            str: The key of the subject
        """

        return self._key

    @property
    def metadata(self) -> Dict[str, Any]:
        """
        Gets the metadata of the subject.

        Returns:
            Dict[str, Any]: The metadata of the subject
        """

        return self._metadata

    @property
    def name(self) -> str:
        """
        Gets the name of the subject.

        Returns:
            str: The name of the subject
        """

        return self._name

    @property
    def priority(self) -> int:
        """
        Gets the priority of the subject.

        Returns:
            int: The priority of the subject
        """

        return self._priority

    @property
    def tags(self) -> List[str]:
        """
        Gets the tags of the subject.

        Returns:
            List[str]: The tags of the subject
        """

        return self._tags

    @property
    def updated_at(self) -> datetime:
        """
        Gets the timestamp when the subject was last updated.

        Returns:
            datetime: The timestamp when the subject was last updated.
        """

        return self._updated_at

    @property
    def uuid(self) -> str:
        """
        Gets the UUID of the subject.

        Returns:
            str: The UUID of the subject
        """

        return self._uuid

    def to_mutable(self) -> "MutableSubject":
        """
        Creates a new MutableSubject instance from this instance's attributes.

        This method creates a new MutableSubject instance from this instance's attributes and returns it.

        Args:
            None

        Returns:
            MutableSubject: A MutableSubject instance created from this instance's attributes

        Raises:
            Exception: If an exception occurs during the creation of the MutableSubject instance
        """
        try:
            # Attempt to create and return a MutableSubject instance from this instance's attributes
            return MutableSubject(
                **self.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_mutable' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e


class MutableSubject(MutableBaseObject):
    """
    A mutable class representing a subject.

    A subject is a category or topic that a subject, note or question (incl. Answer) belongs to.

    Attributes:
        name (str): The name of the subject.
        created_at (Optional[datetime], optional): The creation date and time of the subject. Defaults to None.
        custom_field_values (Optional[List[Dict[str, Any]]], optional): The custom field values of the subject. Defaults to None.
        description (Optional[str], optional): The description of the subject. Defaults to None.
        difficulty (Optional[int], optional): The subject level of the subject. Defaults to None.
        icon (Optional[str], optional): The icon associated with the subject. Defaults to "🧑‍🏫".
        id (Optional[int], optional): The unique identifier of the subject. Defaults to None.
        key (Optional[str], optional): The key associated with the subject. Defaults to None.
        metadata (Optional[Dict[str, Any]], optional): The metadata of the subject. Defaults to None.
        priority (Optional[int], optional): The priority level of the subject. Defaults to None.
        tags (Optional[List[str]], optional): The tags associated with the subject. Defaults to None.
        updated_at (Optional[datetime], optional): The last update date and time of the subject. Defaults to None.
        uuid (Optional[str], optional): The unique identifier of the subject. Defaults to None.
    """

    def __init__(
        self,
        name: str,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        description: Optional[str] = None,
        difficulty: Optional[int] = None,
        icon: Optional[str] = "🧑‍🏫",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        priority: Optional[int] = None,
        tags: Optional[List[str]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableSubject class.

        Args:
            name (str): The name of the subject.
            created_at (Optional[datetime], optional): The creation date and time of the subject. Defaults to None.
            custom_field_values (Optional[List[Dict[str, Any]]], optional): The custom field values of the subject. Defaults to None.
            description (Optional[str], optional): The description of the subject. Defaults to None.
            difficulty (Optional[int], optional): The subject level of the subject. Defaults to None.
            icon (Optional[str], optional): The icon associated with the subject. Defaults to "🧑‍🏫".
            id (Optional[int], optional): The unique identifier of the subject. Defaults to None.
            key (Optional[str], optional): The key associated with the subject. Defaults to None.
            metadata (Optional[Dict[str, Any]], optional): The metadata of the subject. Defaults to None.
            priority (Optional[int], optional): The priority level of the subject. Defaults to None.
            tags (Optional[List[str]], optional): The tags associated with the subject. Defaults to None.
            updated_at (Optional[datetime], optional): The last update date and time of the subject. Defaults to None.
            uuid (Optional[str], optional): The unique identifier of the subject. Defaults to None.

        Returns:
            None
        """

        # Call the parent class constructor with the passed arguments
        super().__init__(
            created_at=created_at,
            custom_field_values=custom_field_values,
            description=description,
            difficulty=difficulty,
            hide_attributes=True,
            icon=icon,
            id=id,
            key=key,
            metadata=metadata,
            name=name,
            priority=priority,
            tags=tags,
            updated_at=updated_at,
            uuid=uuid,
        )

    @property
    def created_at(self) -> datetime:
        """
        Gets the creation date and time of the subject.

        Returns:
            datetime: The creation date and time of the subject
        """

        return self._created_at

    @created_at.setter
    def created_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the creation date and time of the subject.

        Args:
            value (datetime): The new creation date and time of the subject.

        Returns:
            None
        """

        self._created_at = value

    @property
    def custom_field_values(self) -> List[Dict[str, Any]]:
        """
        Gets the custom field values of the subject.

        Returns:
            List[Dict[str, Any]]: The custom field values of the subject
        """

        return self._custom_field_values

    @custom_field_values.setter
    def custom_field_values(
        self,
        value: Union[
            Dict[str, Any],
            List[Dict[str, Any]],
        ],
    ) -> None:
        """
        Sets the custom field values of the subject.

        Args:
            value (Union[Dict[str, Any], List[Dict[str, Any]]]): The new custom field values of the scubject.

        Returns:
            None
        """

        # Check, if the 'custom_field_values' attribute exists
        if not self._custom_field_values:
            # Initialize the 'custom_field_values' attribute as an empty list
            self._custom_field_values = []

        # Check, if the passed value is a dictionary
        if isinstance(
            value,
            dict,
        ):
            # Append the passed value to the 'custom_field_values' list attribute
            self._custom_field_values.append(value)
        # Check, if the passed value is a list
        elif isinstance(
            value,
            list,
        ):
            # Update the 'custom_field_values' attribute list with the passed value list
            self._custom_field_values = value

    @property
    def description(self) -> str:
        """
        Gets the description of the subject.

        Returns:
            str: The description of the subject
        """

        return self._description

    @description.setter
    def description(
        self,
        value: str,
    ) -> None:
        """
        Sets the description of the subject.

        Args:
            value (str): The description of the subject.

        Returns:
            None
        """

        self._description = value

    @property
    def difficulty(self) -> int:
        """
        Gets the difficulty level of the subject.

        Returns:
            int: The difficulty level of the subject.
        """

        return self._difficulty

    @difficulty.setter
    def difficulty(
        self,
        value: int,
    ) -> None:
        """
        Sets the difficulty level of the subject.

        Args:
            value (int): The new difficulty level to be set.

        Returns:
            None
        """

        self._difficulty = value

    @property
    def icon(self) -> str:
        """
        Gets the icon of the subject.

        Returns:
            str: The icon of the subject
        """

        return self._icon

    @property
    def id(self) -> int:
        """
        Gets the ID of the subject.

        Returns:
            int: The ID of the subject
        """

        return self._id

    @property
    def key(self) -> str:
        """
        Gets the key of the subject.

        Returns:
            str: The key of the subject
        """

        return self._key

    @property
    def metadata(self) -> Dict[str, Any]:
        """
        Gets the metadata of the subject.

        Returns:
            Dict[str, Any]: The metadata of the subject
        """

        return self._metadata

    @metadata.setter
    def metadata(
        self,
        **kwargs,
    ) -> None:
        """
        Sets the metadata of the subject.

        Args:
            **kwargs: The keyword arguments representing the metadata key-value pairs.

        Returns:
            None
        """

        # Check, if the 'metadata' attribute exists
        if not self._metadata:
            # Initialize the 'metadata' attribute as an empty dictionary
            self._metadata = {}

        # Update the 'metadata' attribute with the passed keyword arguments
        self._metadata.update(**kwargs)

    @property
    def name(self) -> str:
        """
        Gets the name of the subject.

        Returns:
            str: The name of the subject
        """

        return self._name

    @name.setter
    def name(
        self,
        value: str,
    ) -> None:
        """
        Sets the name of the subject.

        Args:
            value (str): The new name of the subject.

        Returns:
            None
        """

        self._name = value

    @property
    def priority(self) -> int:
        """
        Gets the priority of the subject.

        Returns:
            int: The priority of the subject
        """

        return self._priority

    @priority.setter
    def priority(
        self,
        value: int,
    ) -> None:
        """
        Sets the priority of the subject.

        Args:
            value (int): The new priority of the subject.

        Returns:
            None
        """

        self._priority = value

    @property
    def tags(self) -> List[str]:
        """
        Gets the tags of the subject.

        Returns:
            List[str]: The tags of the subject
        """

        return self._tags

    @tags.setter
    def tags(
        self,
        value: Union[
            List[str],
            str,
        ],
    ) -> None:
        """
        Sets the tags of the subject.

        Args:
            value (Union[List[str], str]): The tags of the subject.

        Returns:
            None
        """

        # Check, if the 'tags' attribute exists
        if not self._tags:
            # Initialize the 'tags' attribute as an empty list
            self._tags = []

        # Check, if the passed value is a list
        if isinstance(
            value,
            list,
        ):
            # Update the 'tags' attribute list with the passed value list
            self._tags = value
        # Check, if the passed value is a string
        if isinstance(
            value,
            str,
        ):
            # Append the passed value to the 'tags' list attribute
            self._tags.append(value)

    @property
    def updated_at(self) -> datetime:
        """
        Gets the timestamp when the subject was last updated.

        Returns:
            datetime: The timestamp when the subject was last updated.
        """

        return self._updated_at

    @updated_at.setter
    def updated_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the timestamp when the subject was last updated.

        Args:
            value (datetime): The new timestamp when the subject was last updated.

        Returns:
            None
        """

        self._updated_at = value

    @property
    def uuid(self) -> str:
        """
        Gets the UUID of the subject.

        Returns:
            str: The UUID of the subject
        """

        return self._uuid

    @uuid.setter
    def uuid(
        self,
        value: str,
    ) -> None:
        """
        Sets the UUID of the subject.

        Args:
            value (str): The new UUID of the subject.

        Returns:
            None
        """

        self._uuid = value

    def to_immutable(self) -> ImmutableSubject:
        """
        Creates a new ImmutableSubject instance from this instance's attributes.

        This method creates a new ImmutableSubject instance from this instance's attributes and returns it.

        Args:
            None

        Returns:
            ImmutableSubject: A ImmutableSubject instance created from this instance's attributes

        Raises:
            Exception: If an exception occurs during the creation of the ImmutableSubject instance
        """
        try:
            # Attempt to create and return an ImmutableSubject instance from this instance's attributes
            return ImmutableSubject(
                **self.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_immutable' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e


class SubjectConverter:
    """
    A converter class for transforming between SubjectModel and ImmutableSubject instances.

    This class provides methods to convert a SubjectModel instance to an ImmutableSubject instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the SubjectConverter class.
    """

    logger: Final[Logger] = Logger.get_logger(name="SubjectConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "SubjectModel",
    ) -> Optional[ImmutableSubject]:
        """
        Converts a given SubjectModel instance to an ImmutableSubject instance.

        Args:
            model (SubjectModel): The SubjectModel instance to be converted.

        Returns:
            ImmutableSubject: The converted ImmutableSubject instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the SubjectModel instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableSubject class from the dictionary representation of the SubjectModel instance
            return ImmutableSubject(
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
        object: ImmutableSubject,
    ) -> Optional["SubjectModel"]:
        """
        Converts a given ImmutableSubject instance to a SubjectModel instance.

        Args:
            object (ImmutableSubject): The ImmutableSubject instance to be converted.

        Returns:
            SubjectModel: The converted SubjectModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ImmutableSubject instance.
        """
        try:
            # Attempt to create and return a new instance of the SubjectModel class from the dictionary representation of the ImmutableSubject instance
            return SubjectModel(
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


class SubjectFactory:
    """
    A factory class for creating instances of the ImmutableSubject class.

    This class provides a method to create a new instance of the ImmutableSubject class.

    Attributes:
        logger (Logger): The logger instance associated with the SubjectFactory class.
    """

    logger: Final[Logger] = Logger.get_logger(name="SubjectFactory")

    @classmethod
    def create_subject(
        cls,
        name: str,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        description: Optional[str] = None,
        difficulty: Optional[int] = None,
        icon: Optional[str] = "🧑‍🏫",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        priority: Optional[int] = None,
        tags: Optional[List[str]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutableSubject]:
        """
        Creates and returns a new instance of ImmutableSubject class.

        Args:
            name (str): The name of the subject.
            created_at (Optional[datetime], optional): The creation date and time of the subject. Defaults to None.
            custom_field_values (Optional[List[Dict[str, Any]]], optional): The custom field values of the subject. Defaults to None.
            description (Optional[str], optional): The description of the subject. Defaults to None.
            difficulty (Optional[int], optional): The subject level of the subject. Defaults to None.
            icon (Optional[str], optional): The icon associated with the subject. Defaults to "🧑‍🏫".
            id (Optional[int], optional): The unique identifier of the subject. Defaults to None.
            key (Optional[str], optional): The key associated with the subject. Defaults to None.
            metadata (Optional[Dict[str, Any]], optional): The metadata of the subject. Defaults to None.
            priority (Optional[int], optional): The priority level of the subject. Defaults to None.
            tags (Optional[List[str]], optional): The tags associated with the subject. Defaults to None.
            updated_at (Optional[datetime], optional): The last update date and time of the subject. Defaults to None.
            uuid (Optional[str], optional): The unique identifier of the subject. Defaults to None.

        Returns:
            Optional[ImmutableSubject]: The created subject object if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the subject.
        """
        try:
            # Attempt to create and return an ImmutableSubject instance
            return ImmutableSubject(
                created_at=created_at,
                custom_field_values=custom_field_values,
                description=description,
                difficulty=difficulty,
                icon=icon,
                id=id,
                key=key,
                metadata=metadata,
                name=name,
                priority=priority,
                tags=tags,
                updated_at=updated_at,
                uuid=uuid,
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_subject' method from '{cls.__name__}': {e}"
            )

            # Log the traceback
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @classmethod
    def create_default_subject(
        cls,
        name: str,
    ) -> Optional[ImmutableSubject]:
        """
        Creates and returns a new instance of the ImmutableSubject class with default values.

        Args:
            name (str): The name of the subject.

        Returns:
            Optional[ImmutableSubject]: The created subject object if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the subject.
        """
        try:
            # Import the DifficultyManager locally
            from core.difficulty import DifficultyManager

            # Import the PriorityManager locally
            from core.priority import PriorityManager

            # Attempt to create and return a subject with (most) default attributes
            return ImmutableSubject(
                created_at=Miscellaneous.get_current_datetime(),
                custom_field_values=[],
                description=f"Default subject '{name}' created at {Miscellaneous.datetime_to_string(datetime=Miscellaneous.get_current_datetime())}",
                difficulty=DifficultyManager()
                .get_difficulty_by(
                    field="name",
                    value="Medium",
                )
                .get(
                    default=None,
                    name="id",
                ),
                icon="🧑‍🏫",
                metadata={},
                name=name,
                priority=PriorityManager()
                .get_priority_by(
                    field="name",
                    value="Medium",
                )
                .get(
                    default=None,
                    name="id",
                ),
                tags=[],
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_default_subject' method from '{cls.__name__}': {e}"
            )

            # Log the traceback
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e


class SubjectBuilder(BaseObjectBuilder):
    """
    A builder class for creating instances of the ImmutableSubject class.

    This class provides a method to create a new instance of the ImmutableSubject class.

    Attributes:
        logger (Logger): The logger instance associated with the SubjectBuilder class.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the SubjectBuilder class.

        This constructor calls the parent class constructor and initializes the configuration dictionary.

        Args:
            None

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    @override
    def build(self) -> Optional[ImmutableSubject]:
        """
        Builds and returns an instance of the ImmutableSubject class using the configuration dictionary.

        This method attempts to create an instance of the ImmutableSubject class using the configuration dictionary passed to the constructor.
        If an exception occurs while creating the instance, this method will log an error message and return None.

        Returns:
            Optional[ImmutableSubject]: The created subject object if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to run 'build' method from '{self.__class__.__name__}'
        """
        try:
            # Attempt to create and return a new ImmutableSubject instance
            return SubjectFactory.create_subject(**self.configuration)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'build' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def custom_field_values(
        self,
        value: Union[Dict[str, Any], List[Dict[str, Any]]],
    ) -> Self:
        """
        Sets the custom field values of the subject.

        Args:
            value (Union[Dict[str, Any], List[Dict[str, Any]]]): The custom field values of the subject.

        Returns:
            Self: The builder instance.
        """

        if "custom_field_values" not in self.configuration:
            self.configuration["custom_field_values"] = []

        if isinstance(
            value,
            list,
        ):
            self.configuration["custom_field_values"].extend(value)
        elif isinstance(
            value,
            dict,
        ):
            self.configuration["custom_field_values"].append(value)

        return self

    def description(
        self,
        value: str,
    ) -> Self:
        """
        Sets the description of the subject.

        Args:
            value (str): The description of the subject.

        Returns:
            Self: The builder instance.
        """

        self.configuration["description"] = value
        return self

    def difficulty(
        self,
        value: int,
    ) -> Self:
        """
        Sets the difficulty of the subject.

        Args:
            value (int): The difficulty of the subject.

        Returns:
            Self: The builder instance.
        """

        self.configuration["difficulty"] = value
        return self

    def metadata(
        self,
        value: Dict[str, Any],
    ) -> Self:
        """
        Sets the metadata of the subject.

        Args:
            value (Dict[str, Any]): The metadata of the subject.

        Returns:
            Self: The builder instance.
        """

        # Check, if the 'metadata' key exists in the 'configuration' dictionary
        if "metadata" not in self.configuration:
            self.configuration["metadata"] = {}

        # Update the 'metadata' dictionary with the new values
        self.configuration["metadata"].update(value)

        # Return the builder instance
        return self

    def name(
        self,
        value: str,
    ) -> Self:
        """
        Sets the name of the subject.

        Args:
            value (str): The name of the subject.

        Returns:
            Self: The builder instance.
        """

        self.configuration["name"] = value
        return self

    def priority(
        self,
        value: int,
    ) -> Self:
        """
        Sets the priority of the subject.

        Args:
            value (int): The priority of the subject.

        Returns:
            Self: The builder instance.
        """

        self.configuration["priority"] = value
        return self

    def tags(
        self,
        value: Union[List[str], str],
    ) -> Self:
        """
        Sets the tags of the subject.

        Args:
            value (Union[List[str], str]): The tags of the subject.

        Returns:
            Self: The builder instance.
        """

        if "tags" not in self.configuration:
            self.configuration["tags"] = []

        if isinstance(
            value,
            list,
        ):
            self.configuration["tags"].extend(value)
        elif isinstance(
            value,
            str,
        ):
            self.configuration["tags"].append(value)

        return self


class SubjectManager(BaseObjectManager):
    """
    A manager class for managing subjects in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for subjects.

    Attributes:
        cache: (List[Any]): The cache for storing subjects.
        logger (Logger): The logger instance associated with the object.
    """

    _shared_instance: Optional["SubjectManager"] = None

    def __new__(cls) -> "SubjectManager":
        """
        Creates and returns a new instance of the SubjectManager class.

        If the instance does not exist, creates a new one by calling the parent class
        constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Returns:
            SubjectManager: The created or existing instance of SubjectManager class.
        """
        if cls._shared_instance is None:
            # Create a new instance by calling the parent class constructor
            cls._shared_instance = super(SubjectManager, cls).__new__(cls)
            # Initialize the instance
            cls._shared_instance.init()
        # Return the shared instance
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes a new instance of the SubjectManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def count_subjects(self) -> int:
        """
        Returns the number of subjects in the database.

        Returns:
            int: The number of subjects in the database.
        """
        try:
            # Count and return the number of subjects in the database
            return asyncio.run(SubjectModel.count(database=Constants.DATABASE_PATH))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_subject(
        self,
        subject: ImmutableSubject,
    ) -> Optional[ImmutableSubject]:
        """
        Creates a new subject in the database.

        Args:
            difficulty (ImmutableSubject): The subject to be created.

        Returns:
            Optional[ImmutableSubject]: The newly created immutable subject if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the subject.
        """
        try:
            # Check if the subject object is immutable
            if isinstance(
                subject,
                ImmutableSubject,
            ):
                # If it is, convert it to a mutable subject
                subject = MutableSubject(
                    **subject.to_dict(
                        exclude=[
                            "_logger",
                        ]
                    )
                )

            # Set the created_at timestamp of the subject
            subject.created_at = Miscellaneous.get_current_datetime()

            # Set the key of the subject
            subject.key = f"SUBJECT_{self.count_subjects() + 1}"

            # Set the updated_at timestamp of the subject
            subject.updated_at = Miscellaneous.get_current_datetime()

            # Set the uuid of the subject
            subject.uuid = Miscellaneous.get_uuid()

            # Convert the subject object to a SubjectModel object
            model: SubjectModel = SubjectConverter.object_to_model(object=subject)

            # Create a new subject in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            if id:
                # Set the ID of the subject
                subject.id = id

                # Convert the subject to an immutable subject
                subject = ImmutableSubject(
                    **subject.to_dict(
                        exclude=[
                            "_logger",
                        ]
                    )
                )

                # Add the subject to the cache
                self.add_to_cache(
                    key=subject.key,
                    value=subject,
                )

                # Return the newly created immutable subject
                return subject

            # Log a warning message indicating an error has occurred
            self.logger.warning(
                message=f"It seems that an error has occured while attempting to create a difficulty ({subject}) in the database."
            )

            # Return None indicating an error has occurred
            return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_subject' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete_subject(
        self,
        subject: ImmutableSubject,
    ) -> bool:
        """
        Deletes a subject from the database.

        Args:
            difficulty (ImmutableSubject): The subject to be deleted.

        Returns:
            bool: True if the subject was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the subject to an immutable subject and delete the subject from the database
            result: bool = asyncio.run(
                SubjectConverter.object_to_model(
                    object=ImmutableSubject(
                        **subject.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).delete()
            )

            # Return True if the subject was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all_subjects(
        self,
        force_refetch: bool = False,
    ) -> Optional[List[ImmutableSubject]]:
        """
        Returns a list of all subjects in the database.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.

        Returns:
            Optional[List[ImmutableSubject]]: A list of all subjects in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if cache and table size are equal
                if self.cache and len(self._cache) == self.count_subjects():
                    # Return the list of immutable subjects from the cache
                    return self.get_cache_values()

            # Get all subjects from the database
            models: List[SubjectModel] = asyncio.run(
                SubjectModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of SubjectModel objects to a list of Subject objects
            subjects: List[ImmutableSubject] = [
                ImmutableSubject(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable subjects
            for subject in subjects:
                if not self.is_key_in_cache(key=subject.key):
                    # Add the immutable subject to the cache
                    self.add_to_cache(
                        key=subject.key,
                        value=subject,
                    )
                else:
                    # Update the immutable subject in the cache
                    self.update_in_cache(
                        key=subject.key,
                        value=subject,
                    )

            # Return the list of immutable subjects
            return subjects
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_subject_by(
        self,
        field: str,
        value: Any,
        force_refetch: bool = False,
    ) -> Optional[ImmutableSubject]:
        """
        Retrieves a subject by the given field and value.

        Args:
            field (str): The field to search by.
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            value (Any): The value to search for.

        Returns:
            Optional[ImmutableSubject]: The subject with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if the subject is already in the cache
                if self.is_key_in_cache(key=field):
                    # Return the subject from the cache
                    return self.get_value_from_cache(key=field)

            # Get the subject with the given field and value from the database
            model: Optional[SubjectModel] = asyncio.run(
                SubjectModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Return the subject if it exists
            if model is not None:
                # Convert the SubjectModel object to an Subject object
                return ImmutableSubject(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the subject does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_subject_by_id(
        self,
        id: int,
        force_refetch: bool = False,
    ) -> Optional[ImmutableSubject]:
        """
        Returns a subject with the given ID.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            id (int): The ID of the subject.

        Returns:
            Optional[ImmutableSubject]: The subject with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if the subject is already in the cache
                if self.is_key_in_cache(key=f"SUBJECT_{id}"):
                    # Return the subject from the cache
                    return self.get_value_from_cache(key=f"SUBJECT_{id}")

            # Get the subject with the given ID from the database
            model: Optional[SubjectModel] = asyncio.run(
                SubjectModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the subject if it exists
            if model is not None:
                # Convert the SubjectModel object to an Subject object
                return ImmutableSubject(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the subject does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_subject_by_id(
        self,
        key: str,
        force_refetch: bool = False,
    ) -> Optional[ImmutableSubject]:
        """
        Returns a subject with the given key.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            key (str): The ID of the subject.

        Returns:
            Optional[ImmutableSubject]: The subject with the given key if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if the subject is already in the cache
                if self.is_key_in_cache(key=key):
                    # Return the subject from the cache
                    return self.get_value_from_cache(key=key)

            # Get the subject with the given ID from the database
            model: Optional[SubjectModel] = asyncio.run(
                SubjectModel.get_by(
                    column="key",
                    database=Constants.DATABASE_PATH,
                    value=key,
                )
            )

            # Return the subject if it exists
            if model is not None:
                # Convert the SubjectModel object to an Subject object
                return ImmutableSubject(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the subject does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_key' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_subject_by_uuid(
        self,
        uuid: str,
        force_refetch: bool = False,
    ) -> Optional[ImmutableSubject]:
        """
        Returns a subject with the given UUID.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            uuid (str): The UUID of the subject.

        Returns:
            Optional[ImmutableSubject]: The subject with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if the subject is already in the cache
                if self.is_key_in_cache(key=uuid):
                    # Return the subject from the cache
                    return self.get_value_from_cache(key=uuid)

            # Get the subject with the given UUID from the database
            model: Optional[SubjectModel] = asyncio.run(
                SubjectModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the subject if it exists
            if model is not None:
                # Convert the SubjectModel object to an Subject object
                return ImmutableSubject(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the subject does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def search_subjects(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[Union[List[ImmutableSubject]]]:
        """
        Searches for subjects in the database.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            **kwargs: Any additional keyword arguments to be passed to the search method of the SubjectModel class.

        Returns:
            Optional[Union[List[ImmutableSubject]]]: The found subjects if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Search the stack for the passed keyword arguments
                cached_result: Optional[List[ImmutableSubject]] = self.search_cache(
                    **kwargs
                )

                # Check, if any cached results exist
                if cached_result:
                    # Return the cached results
                    return cached_result

            # Search for subjects in the database
            models: Optional[List[SubjectModel]] = asyncio.run(
                SubjectModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found subjects if any
            if models is not None and len(models) > 0:
                return [
                    ImmutableSubject(
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
                # Return None indicating that no subjects were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_subject(
        self,
        subject: ImmutableSubject,
    ) -> Optional[ImmutableSubject]:
        """
        Updates a subject with the given ID.

        Args:
            difficulty (ImmutableSubject): The subject to update.

        Returns:
            Optional[ImmutableSubject]: The updated subject if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the subject to an immutable subject and update the subject in the database
            model: Optional[SubjectModel] = asyncio.run(
                SubjectConverter.object_to_model(
                    object=ImmutableSubject(
                        **subject.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).update(
                    database=Constants.DATABASE_PATH,
                    **subject.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Return the updated subject if it exists
            if model is not None:
                # Convert the SubjectModel object to an Subject object
                subject = ImmutableSubject(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the subject to the cache
                self.update_in_cache(
                    key=subject.key,
                    value=subject,
                )

                # Return the updated subject
                return subject
            else:
                # Return None indicating that the subject does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class SubjectModel(ImmutableBaseModel):
    """
    Represents the structure of a subject model.

    Attributes:
        created_at (datetime): The timestamp when the subject was created.
        custom_field_values (List[Dict[str, Any]]): The custom field values of the subject.
        description (str): The description of the subject.
        difficulty (int): The subject level of the subject.
        icon (str): The icon associated with the subject. Defaults to "🧑‍🏫".
        id (int): The unique identifier of the subject.
        key (str): The key associated with the subject.
        metadata (Dict[str, Any]): The metadata of the subject.
        name (str): The name of the subject.
        priority (int): The priority level of the subject.
        table (str, final): The (immutable) table name of the subject. Defaults to "subjects".
        tags (List[str]): The tags associated with the subject.
        updated_at (datetime): The timestamp when the subject was last updated.
        uuid (str): The unique identifier of the subject.
    """

    table: Final[str] = Constants.SUBJECTS

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

    custom_field_values: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="custom_field_values",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
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
        size=None,
        type="TEXT",
        unique=False,
    )

    difficulty: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.DIFFICULTIES}(id)",
        index=False,
        name="difficulty",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    icon: Field = Field(
        autoincrement=False,
        default="🧑‍🏫",
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

    priority: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.PRIORITIES}(id)",
        index=False,
        name="priority",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    tags: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="tags",
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

    def __init__(
        self,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        description: Optional[str] = None,
        difficulty: Optional[int] = None,
        icon: Optional[str] = "🧑‍🏫",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        priority: Optional[int] = None,
        tags: Optional[List[str]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the Subject class.

        Args:
            created_at (Optional[datetime], optional): The creation date and time of the subject. Defaults to None.
            custom_field_values (Optional[List[Dict[str, Any]]], optional): The custom field values of the subject. Defaults to None.
            description (Optional[str], optional): The description of the subject. Defaults to None.
            difficulty (Optional[int], optional): The subject level of the subject. Defaults to None.
            icon (Optional[str], optional): The icon associated with the subject. Defaults to "🧑‍🏫".
            id (Optional[int], optional): The unique identifier of the subject. Defaults to None.
            key (Optional[str], optional): The key associated with the subject. Defaults to None.
            metadata (Optional[Dict[str, Any]], optional): The metadata of the subject. Defaults to None.
            name (Optional[str], optional): The name of the subject. Defaults to None.
            priority (Optional[int], optional): The priority level of the subject. Defaults to None.
            tags (Optional[List[str]], optional): The tags associated with the subject. Defaults to None.
            updated_at (Optional[datetime], optional): The last update date and time of the subject. Defaults to None.
            uuid (Optional[str], optional): The unique identifier of the subject. Defaults to None.

        Returns:
            None
        """

        # Call the parent class constructor with the passed arguments
        super().__init__(
            created_at=created_at,
            custom_field_values=custom_field_values,
            description=description,
            difficulty=difficulty,
            icon="🧑‍🏫",
            id=id,
            key=key,
            metadata=metadata,
            name=name,
            priority=priority,
            table=Constants.SUBJECTS,
            tags=tags,
            updated_at=updated_at,
            uuid=uuid,
        )
