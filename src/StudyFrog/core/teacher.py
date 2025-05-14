"""
Author: lodego
Date: 2025-04-23
"""

import asyncio
import json
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
    "ImmutableTeacher",
    "MutableTeacher",
    "TeacherConverter",
    "TeacherFactory",
    "TeacherBuilder",
    "TeacherManager",
    "TeacherModel",
]


class ImmutableTeacher(ImmutableBaseObject):
    """
    An immutable class representing a teacher.

    A teacher is a category or topic that a teacher, note or question (incl. Answer) belongs to.

    Attributes:
        name (str): The name of the teacher.
        created_at (Optional[datetime], optional): The creation date and time of the teacher. Defaults to None.
        custom_field_values (Optional[List[Dict[str, Any]]], optional): The custom field values of the teacher. Defaults to None.
        description (Optional[str], optional): The description of the teacher. Defaults to None.
        difficulty (Optional[int], optional): The teacher level of the teacher. Defaults to None.
        icon (Optional[str], optional): The icon associated with the teacher. Defaults to "🧑‍🏫".
        id (Optional[int], optional): The unique identifier of the teacher. Defaults to None.
        key (Optional[str], optional): The key associated with the teacher. Defaults to None.
        metadata (Optional[Dict[str, Any]], optional): The meta data of the teacher. Defaults to None.
        priority (Optional[int], optional): The priority level of the teacher. Defaults to None.
        subjects (Optional[List[str]], optional): The subjects associated with the teacher. Defaults to None.
        tags (Optional[List[str]], optional): The tags associated with the teacher. Defaults to None.
        updated_at (Optional[datetime], optional): The last update date and time of the teacher. Defaults to None.
        uuid (Optional[str], optional): The unique identifier of the teacher. Defaults to None.
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
        subjects: Optional[List[str]] = None,
        tags: Optional[List[str]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableTeacher class.

        Args:
            name (str): The name of the teacher.
            created_at (Optional[datetime], optional): The creation date and time of the teacher. Defaults to None.
            custom_field_values (Optional[List[Dict[str, Any]], optional): The custom field values of the teacher. Defaults to None.
            description (Optional[str], optional): The description of the teacher. Defaults to None.
            difficulty (Optional[int], optional): The teacher level of the teacher. Defaults to None.
            icon (Optional[str], optional): The icon associated with the teacher. Defaults to "🧑‍🏫".
            id (Optional[int], optional): The unique identifier of the teacher. Defaults to None.
            key (Optional[str], optional): The key associated with the teacher. Defaults to None.
            metadata (Optional[Dict[str, Any]], optional): The meta data of the teacher. Defaults to None.
            priority (Optional[int], optional): The priority level of the teacher. Defaults to None.
            subjects (Optional[List[str]], optional): The subjects associated with the teacher. Defaults to None.
            tags (Optional[List[str]], optional): The tags associated with the teacher. Defaults to None.
            updated_at (Optional[datetime], optional): The last update date and time of the teacher. Defaults to None.
            uuid (Optional[str], optional): The unique identifier of the teacher. Defaults to None.

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
            subjects=subjects,
            tags=tags,
            updated_at=updated_at,
            uuid=uuid,
        )

    @property
    def created_at(self) -> datetime:
        """
        Returns the creation date and time of the teacher.

        Returns:
            datetime: The creation date and time of the teacher.
        """

        # Return the creation date and time of the teacher
        return self._created_at

    @property
    def custom_field_values(self) -> List[Dict[str, Any]]:
        """
        Returns the custom field values of the teacher.

        Returns:
            List[Dict[str, Any]]: The custom field values of the teacher.
        """

        # Return the custom field values of the teacher
        return self._custom_field_values

    @property
    def description(self) -> str:
        """
        Returns the description of the teacher.

        Returns:
            str: The description of the teacher.
        """

        # Return the description of the teacher
        return self._description

    @property
    def difficulty(self) -> int:
        """
        Returns the difficulty of the teacher.

        Returns:
            int: The difficulty of the teacher.
        """

        # Return the difficulty of the teacher
        return self._difficulty

    @property
    def icon(self) -> str:
        """
        Returns the icon of the teacher.

        Returns:
            str: The icon of the teacher.
        """

        # Return the icon of the teacher
        return self._icon

    @property
    def id(self) -> int:
        """
        Returns the ID of the teacher.

        Returns:
            int: The ID of the teacher.
        """

        # Return the ID of the teacher
        return self._id

    @property
    def key(self) -> str:
        """
        Returns the key of the teacher.

        Returns:
            str: The key of the teacher.
        """

        # Return the key of the teacher
        return self._key

    @property
    def metadata(self) -> Dict[str, Any]:
        """
        Returns the metadata of the teacher.

        Returns:
            Dict[str, Any]: The metadata of the teacher.
        """

        # Return the metadata of the teacher
        return self._metadata

    @property
    def name(self) -> str:
        """
        Returns the name of the teacher.

        Returns:
            str: The name of the teacher.
        """

        # Return the name of the teacher
        return self._name

    @property
    def priority(self) -> int:
        """
        Returns the priority of the teacher.

        Returns:
            int: The priority of the teacher.
        """

        # Return the priority of the teacher
        return self._priority

    @property
    def subjects(self) -> List[str]:
        """
        Returns the subjects of the teacher.

        Returns:
            List[str]: The subjects of the teacher.
        """

        # Return the subjects of the teacher
        return self._subjects

    @property
    def tags(self) -> List[str]:
        """
        Returns the tags of the teacher.

        Returns:
            List[str]: The tags of the teacher.
        """

        # Return the tags of the teacher
        return self._tags

    @property
    def updated_at(self) -> datetime:
        """
        Returns the last update date and time of the teacher.

        Returns:
            datetime: The last update date and time of the teacher.
        """

        # Return the last update date and time of the teacher
        return self._updated_at

    @property
    def uuid(self) -> str:
        """
        Returns the unique identifier of the teacher.

        Returns:
            str: The unique identifier of the teacher.
        """

        # Return the unique identifier of the teacher
        return self._uuid

    def has_subject(
        self,
        subject: Any,
    ) -> bool:
        """
        Checks if the teacher has a given subject.

        Args:
            subject (Any): The subject to check.

        Returns:
            bool: True if the teacher has the subject, False otherwise.
        """

        # Check, if the subject is an instance of string
        if isinstance(
            subject,
            str,
        ):
            # Return True if the subject is in the subjects list
            return subject in self.subjects

        # Return True if the key of the subject is in the subjects list
        return subject.get(name="key") in self.subjects

    def has_tag(
        self,
        tag: Any,
    ) -> bool:
        """
        Checks if the teacher has a given tag.

        Args:
            tag (Any): The tag to check.

        Returns:
            bool: True if the teacher has the tag, False otherwise.
        """

        # Check, if the tag is an instance of string
        if isinstance(
            tag,
            str,
        ):
            # Return True if the tag is in the tags list
            return tag in self.tags

        # Return True if the key of the tag is in the tags list
        return tag.get(name="key") in self.tags

    def to_mutable(self) -> "MutableTeacher":
        """
        Creates a new MutableTeacher instance from this instance's attributes.

        This method creates a new MutableTeacher instance from this instance's attributes and returns it.

        Args:
            None

        Returns:
            MutableTeacher: A MutableTeacher instance created from this instance's attributes

        Raises:
            Exception: If an exception occurs during the creation of the MutableTeacher instance
        """
        try:
            # Attempt to create and return a MutableTeacher instance from this instance's attributes
            return MutableTeacher(
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


class MutableTeacher(MutableBaseObject):
    """
    A mutable class representing a teacher.

    A teacher is a category or topic that a teacher, note or question (incl. Answer) belongs to.

    Attributes:
        name (str): The name of the teacher.
        created_at (Optional[datetime], optional): The creation date and time of the teacher. Defaults to None.
        custom_field_values (Optional[List[Dict[str, Any]]], optional): The custom field values of the teacher. Defaults to None.
        description (Optional[str], optional): The description of the teacher. Defaults to None.
        difficulty (Optional[int], optional): The teacher level of the teacher. Defaults to None.
        icon (Optional[str], optional): The icon associated with the teacher. Defaults to "🧑‍🏫".
        id (Optional[int], optional): The unique identifier of the teacher. Defaults to None.
        key (Optional[str], optional): The key associated with the teacher. Defaults to None.
        metadata (Optional[Dict[str, Any]], optional): The meta data of the teacher. Defaults to None.
        priority (Optional[int], optional): The priority level of the teacher. Defaults to None.
        subjects (Optional[List[str]], optional): The subjects associated with the teacher. Defaults to None.
        tags (Optional[List[str]], optional): The tags associated with the teacher. Defaults to None.
        updated_at (Optional[datetime], optional): The last update date and time of the teacher. Defaults to None.
        uuid (Optional[str], optional): The unique identifier of the teacher. Defaults to None.
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
        subjects: Optional[List[str]] = None,
        tags: Optional[List[str]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableTeacher class.

        Args:
            name (str): The name of the teacher.
            created_at (Optional[datetime], optional): The creation date and time of the teacher. Defaults to None.
            custom_field_values (Optional[List[Dict[str, Any]]], optional): The custom field values of the teacher. Defaults to None.
            description (Optional[str], optional): The description of the teacher. Defaults to None.
            difficulty (Optional[int], optional): The teacher level of the teacher. Defaults to None.
            icon (Optional[str], optional): The icon associated with the teacher. Defaults to "🧑‍🏫".
            id (Optional[int], optional): The unique identifier of the teacher. Defaults to None.
            key (Optional[str], optional): The key associated with the teacher. Defaults to None.
            metadata (Optional[Dict[str, Any]], optional): The meta data of the teacher. Defaults to None.
            priority (Optional[int], optional): The priority level of the teacher. Defaults to None.
            subjects (Optional[List[str]], optional): The subjects associated with the teacher. Defaults to None.
            tags (Optional[List[str]], optional): The tags associated with the teacher. Defaults to None.
            updated_at (Optional[datetime], optional): The last update date and time of the teacher. Defaults to None.
            uuid (Optional[str], optional): The unique identifier of the teacher. Defaults to None.

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
            subjects=subjects,
            tags=tags,
            updated_at=updated_at,
            uuid=uuid,
        )

    @property
    def created_at(self) -> datetime:
        """
        Returns the creation date and time of the teacher.

        Returns:
            datetime: The creation date and time of the teacher.
        """

        # Return the creation date and time of the teacher
        return self._created_at

    @created_at.setter
    def created_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the creation date and time of the teacher.

        Args:
            value (datetime): The creation date and time of the teacher.

        Returns:
            None
        """

        # Set the creation date and time of the teacher
        self._created_at = value

    @property
    def custom_field_values(self) -> List[Dict[str, Any]]:
        """
        Returns the custom field values of the teacher.

        Returns:
            List[Dict[str, Any]]: The custom field values of the teacher.
        """

        # Return the custom field values of the teacher
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
        Sets the custom field values of the teacher.

        Args:
            value (Union[Dict[str, Any], List[Dict[str, Any]]]): The custom field values of the teacher.

        Returns:
            None
        """

        # Check, if the 'custom_field_values' list exists
        if not self.get(
            default=None,
            name="custom_field_values",
        ):
            # Initialize the 'custom_field_values' list
            self._custom_field_values = []

        # Check, if the value is a list
        if isinstance(
            value,
            list,
        ):
            # Extend the custom field values list with the value
            self._custom_field_values.extend(value)

        # Check, if the value (assuming a dictionary) is already in the list
        if value not in self._custom_field_values:
            # Append the value to the custom field values list
            self._custom_field_values.append(value)

        else:
            # Replace the value in the custom field values list
            self._custom_field_values[self._custom_field_values.index(value)] = value

    @property
    def description(self) -> str:
        """
        Returns the description of the teacher.

        Returns:
            str: The description of the teacher.
        """

        # Return the description of the teacher
        return self._description

    @description.setter
    def description(
        self,
        value: str,
    ) -> None:
        """
        Sets the description of the teacher.

        Args:
            value (str): The description of the teacher.

        Returns:
            None
        """

        # Set the description of the teacher
        self._description = value

    @property
    def difficulty(self) -> int:
        """
        Returns the difficulty of the teacher.

        Returns:
            int: The difficulty of the teacher.
        """

        # Return the difficulty of the teacher
        return self._difficulty

    @difficulty.setter
    def difficulty(
        self,
        value: int,
    ) -> None:
        """
        Sets the difficulty of the teacher.

        Args:
            value (int): The difficulty of the teacher.

        Returns:
            None
        """

        # Set the difficulty of the teacher
        self._difficulty = value

    @property
    def icon(self) -> str:
        """
        Returns the icon of the teacher.

        Returns:
            str: The icon of the teacher.
        """

        # Return the icon of the teacher
        return self._icon

    @icon.setter
    def icon(
        self,
        value: str,
    ) -> None:
        """
        Sets the icon of the teacher.

        Args:
            value (str): The icon of the teacher.

        Returns:
            None
        """

        # Set the icon of the teacher
        self._icon = value

    @property
    def id(self) -> int:
        """
        Returns the ID of the teacher.

        Returns:
            int: The ID of the teacher.
        """

        # Return the ID of the teacher
        return self._id

    @id.setter
    def id(
        self,
        value: int,
    ) -> None:
        """
        Sets the ID of the teacher.

        Args:
            value (int): The ID of the teacher.

        Returns:
            None
        """

        # Set the ID of the teacher
        self._id = value

    @property
    def key(self) -> str:
        """
        Returns the key of the teacher.

        Returns:
            str: The key of the teacher.
        """

        # Return the key of the teacher
        return self._key

    @key.setter
    def key(
        self,
        value: str,
    ) -> None:
        """
        Sets the key of the teacher.

        Args:
            value (str): The key of the teacher.

        Returns:
            None
        """

        # Set the key of the teacher
        self._key = value

    @property
    def metadata(self) -> Dict[str, Any]:
        """
        Returns the metadata of the teacher.

        Returns:
            Dict[str, Any]: The metadata of the teacher.
        """

        # Return the metadata of the teacher
        return self._metadata

    @metadata.setter
    def metadata(
        self,
        **kwargs,
    ) -> None:
        """
        Sets the metadata of the teacher.

        Args:
            **kwargs (Dict[str, Any]): The metadata of the teacher.

        Returns:
            None
        """

        # Check, if the 'metadata' dictionary exists
        if not self.get(
            default=None,
            name="metadata",
        ):
            # Initialize the 'metadata' dictionary
            self._metadata = {}

        # Set the metadata of the teacher
        self._metadata.update(kwargs)

    @property
    def name(self) -> str:
        """
        Returns the name of the teacher.

        Returns:
            str: The name of the teacher.
        """

        # Return the name of the teacher
        return self._name

    @name.setter
    def name(
        self,
        value: str,
    ) -> None:
        """
        Sets the name of the teacher.

        Args:
            value (str): The name of the teacher.

        Returns:
            None
        """

        # Set the name of the teacher
        self._name = value

    @property
    def priority(self) -> int:
        """
        Returns the priority of the teacher.

        Returns:
            int: The priority of the teacher.
        """

        # Return the priority of the teacher
        return self._priority

    @priority.setter
    def priority(
        self,
        value: int,
    ) -> None:
        """
        Sets the priority of the teacher.

        Args:
            value (int): The priority of the teacher.

        Returns:
            None
        """

        # Set the priority of the teacher
        self._priority = value

    @property
    def subjects(self) -> List[str]:
        """
        Returns the subjects of the teacher.

        Returns:
            List[str]: The subjects of the teacher.
        """

        # Return the subjects of the teacher
        return self._subjects

    @subjects.setter
    def subjects(
        self,
        value: Union[
            List[str],
            str,
        ],
    ) -> None:
        """
        Sets the subjects of the teacher.

        Args:
            value (Union[List[str], str]): The subjects of the teacher.

        Returns:
            None
        """

        # Check, if the 'subjects' list exists
        if not self.get(
            default=None,
            name="subjects",
        ):
            # Initialize the 'subjects' list
            self._subjects = []

        # Check, if the value is a string
        if isinstance(
            value,
            str,
        ):
            # Append the value to the subjects list
            self._subjects.append(value)

        # Check, if the value is a list
        elif isinstance(
            value,
            list,
        ):
            # Extend the subjects list with the value
            self._subjects.extend(value)

    @property
    def tags(self) -> List[str]:
        """
        Returns the tags of the teacher.

        Returns:
            List[str]: The tags of the teacher.
        """

        # Return the tags of the teacher
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
        Sets the tags of the teacher.

        Args:
            value (Union[List[str], str]): The tags of the teacher.

        Returns:
            None
        """

        # Check, if the 'tags' list exists
        if not self.get(
            default=None,
            name="tags",
        ):
            # Initialize the 'tags' list
            self._tags = []

        # Check, if the value is a string
        if isinstance(
            value,
            str,
        ):
            # Append the value to the tags list
            self._tags.append(value)

        # Check, if the value is a list
        elif isinstance(
            value,
            list,
        ):
            # Extend the tags list with the value
            self._tags.extend(value)

    @property
    def updated_at(self) -> datetime:
        """
        Returns the last update date and time of the teacher.

        Returns:
            datetime: The last update date and time of the teacher.
        """

        # Return the last update date and time of the teacher
        return self._updated_at

    @updated_at.setter
    def updated_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the last update date and time of the teacher.

        Args:
            value (datetime): The last update date and time of the teacher.

        Returns:
            None
        """

        # Set the last update date and time of the teacher
        self._updated_at = value

    @property
    def uuid(self) -> str:
        """
        Returns the unique identifier of the teacher.

        Returns:
            str: The unique identifier of the teacher.
        """

        # Return the unique identifier of the teacher
        return self._uuid

    @uuid.setter
    def uuid(
        self,
        value: str,
    ) -> None:
        """
        Sets the unique identifier of the teacher.

        Args:
            value (str): The unique identifier of the teacher.

        Returns:
            None
        """

        # Set the unique identifier of the teacher
        self._uuid = value

    def add_subject(
        self,
        subject: Any,
    ) -> None:
        """
        Adds a given subject to the subjects of the teacher.

        Args:
            subject (Any): The subject to add to the subjects of the teacher.

        Returns:
            None
        """

        # If the teacher currently has no subjects, create an empty list
        if not self.subjects:
            # Initialize the subjects list as an empty list
            self.subjects = []

        # Check, if the subjects is an instance of string
        if isinstance(
            self.subjects,
            str,
        ):
            # Convert the subjects string into a list
            self.subjects = json.loads(self.subjects)

        # Append the key of the given object to the subjects
        self.subjects.append(subject.get(name="key"))

    def add_tag(
        self,
        tag: Any,
    ) -> None:
        """
        Adds a given tag to the tags of the teacher.

        Args:
            tag (Any): The tag to add to the tags of the teacher.

        Returns:
            None
        """

        # If the teacher currently has no tags, create an empty list
        if not self.tags:
            # Initialize the tags list as an empty list
            self.tags = []

        # Check, if the tags is an instance of string
        if isinstance(
            self.tags,
            str,
        ):
            # Convert the tags string into a list
            self.tags = json.loads(self.tags)

        # Append the key of the given object to the tags
        self.tags.append(tag.get(name="key"))

    def has_subject(
        self,
        subject: Any,
    ) -> bool:
        """
        Checks if the teacher has a given subject.

        Args:
            subject (Any): The subject to check.

        Returns:
            bool: True if the teacher has the subject, False otherwise.
        """

        # Check, if the subject is an instance of string
        if isinstance(
            subject,
            str,
        ):
            # Return True if the subject is in the subjects list
            return subject in self.subjects

        # Return True if the key of the subject is in the subjects list
        return subject.get(name="key") in self.subjects

    def has_tag(
        self,
        tag: Any,
    ) -> bool:
        """
        Checks if the teacher has a given tag.

        Args:
            tag (Any): The tag to check.

        Returns:
            bool: True if the teacher has the tag, False otherwise.
        """

        # Check, if the tag is an instance of string
        if isinstance(
            tag,
            str,
        ):
            # Return True if the tag is in the tags list
            return tag in self.tags

        # Return True if the key of the tag is in the tags list
        return tag.get(name="key") in self.tags

    def remove_subject(
        self,
        subject: Any,
    ) -> None:
        """
        Removes a given subject from the subjects of the teacher.

        Args:
            subject (Any): The subject to remove from the subjects of the teacher.

        Returns:
            None
        """

        # Check, if the subject is an instance of string
        if isinstance(
            subject,
            str,
        ):
            # Remove the subject from the subjects list
            self.subjects.remove(subject)

        # Remove the key of the subject from the subjects list
        self.subjects.remove(subject.get(name="key"))

    def remove_tag(
        self,
        tag: Any,
    ) -> None:
        """
        Removes a given tag from the tags of the teacher.

        Args:
            tag (Any): The tag to remove from the tags of the teacher.

        Returns:
            None
        """

        # Check, if the tag is an instance of string
        if isinstance(
            tag,
            str,
        ):
            # Remove the tag from the tags list
            self.tags.remove(tag)

        # Remove the key of the tag from the tags list
        self.tags.remove(tag.get(name="key"))

    def to_immutable(self) -> ImmutableTeacher:
        """
        Creates a new ImmutableTeacher instance from this instance's attributes.

        This method creates a new ImmutableTeacher instance from this instance's attributes and returns it.

        Args:
            None

        Returns:
            ImmutableTeacher: A ImmutableTeacher instance created from this instance's attributes

        Raises:
            Exception: If an exception occurs during the creation of the ImmutableTeacher instance
        """
        try:
            # Attempt to create and return an ImmutableTeacher instance from this instance's attributes
            return ImmutableTeacher(
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


class TeacherConverter:
    """
    A converter class for transforming between TeacherModel and ImmutableTeacher instances.

    This class provides methods to convert a TeacherModel instance to an ImmutableTeacher instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the TeacherConverter class.
    """

    logger: Final[Logger] = Logger.get_logger(name="TeacherConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "TeacherModel",
    ) -> Optional[ImmutableTeacher]:
        """
        Converts a given TeacherModel instance to an ImmutableTeacher instance.

        Args:
            model (TeacherModel): The TeacherModel instance to be converted.

        Returns:
            ImmutableTeacher: The converted ImmutableTeacher instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the TeacherModel instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableTeacher class from the dictionary representation of the TeacherModel instance
            return ImmutableTeacher(
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
        object: ImmutableTeacher,
    ) -> Optional["TeacherModel"]:
        """
        Converts a given ImmutableTeacher instance to a TeacherModel instance.

        Args:
            object (ImmutableTeacher): The ImmutableTeacher instance to be converted.

        Returns:
            TeacherModel: The converted TeacherModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ImmutableTeacher instance.
        """
        try:
            # Attempt to create and return a new instance of the TeacherModel class from the dictionary representation of the ImmutableTeacher instance
            return TeacherModel(
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


class TeacherFactory:
    """
    A factory class for creating instances of the ImmutableTeacher class.

    This class provides a method to create a new instance of the ImmutableTeacher class.

    Attributes:
        logger (Logger): The logger instance associated with the TeacherFactory class.
    """

    logger: Final[Logger] = Logger.get_logger(name="TeacherFactory")

    @classmethod
    def create_teacher(
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
        subjects: Optional[List[str]] = None,
        tags: Optional[List[str]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutableTeacher]:
        """
        Creates and returns a new instance of ImmutableTeacher class.

        Args:
            name (str): The name of the teacher.
            created_at (Optional[datetime], optional): The creation date and time of the teacher. Defaults to None.
            custom_field_values (Optional[List[Dict[str, Any]]], optional): The custom field values of the teacher. Defaults to None.
            description (Optional[str], optional): The description of the teacher. Defaults to None.
            difficulty (Optional[int], optional): The teacher level of the teacher. Defaults to None.
            icon (Optional[str], optional): The icon associated with the teacher. Defaults to "🧑‍🏫".
            id (Optional[int], optional): The unique identifier of the teacher. Defaults to None.
            key (Optional[str], optional): The key associated with the teacher. Defaults to None.
            metadata (Optional[Dict[str, Any]], optional): The meta data of the teacher. Defaults to None.
            priority (Optional[int], optional): The priority level of the teacher. Defaults to None.
            subjects (Optional[List[str]], optional): The subjects associated with the teacher. Defaults to None.
            tags (Optional[List[str]], optional): The tags associated with the teacher. Defaults to None.
            updated_at (Optional[datetime], optional): The last update date and time of the teacher. Defaults to None.
            uuid (Optional[str], optional): The unique identifier of the teacher. Defaults to None.

        Returns:
            Optional[ImmutableTeacher]: The created teacher object if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the teacher.
        """
        try:
            # Attempt to create and return an ImmutableTeacher instance
            return ImmutableTeacher(
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
                subjects=subjects,
                tags=tags,
                updated_at=updated_at,
                uuid=uuid,
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_teacher' method from '{cls.__name__}': {e}"
            )

            # Log the traceback
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e


class TeacherBuilder(BaseObjectBuilder):
    """
    A builder class for creating instances of the ImmutableTeacher class.

    This class provides a method to create a new instance of the ImmutableTeacher class.

    Attributes:
        logger (Logger): The logger instance associated with the TeacherBuilder class.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the TeacherBuilder class.

        This constructor calls the parent class constructor and initializes the configuration dictionary.

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
            ImmutableTeacher,
            MutableTeacher,
        ]
    ]:
        """
        Builds and returns an instance of the ImmutableTeacher class using the configuration dictionary.

        This method attempts to create an instance of the ImmutableTeacher class using the configuration dictionary passed to the constructor.
        If an exception occurs while creating the instance, this method will log an error message and return None.

        Args:
            as_mutable (bool, optional): A flag indicating whether to return the teacher as a mutable instance. Defaults to False.

        Returns:
            Optional[Union[ImmutableTeacher, MutableTeacher]]: The created teacher object if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to run 'build' method from '{self.__class__.__name__}'
        """
        try:
            # Attempt to create and return a new ImmutableTeacher instance
            teacher: Optional[ImmutableTeacher] = TeacherFactory.create_teacher(
                **self.configuration
            )

            # Check, if the teacher exists
            if not teacher:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create teacher from configuration: {self.configuration}"
                )

                # Return early
                return

            # Check, if the 'as_mutable' flag is set
            if as_mutable:
                # Return the teacher as a mutable instance
                return teacher.to_mutable()

            # Return the teacher as an immutable instance
            return teacher
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
        Sets the custom field values of the teacher.

        Args:
            value (Union[Dict[str, Any], List[Dict[str, Any]]]): The custom field values of the teacher.

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
        Sets the description of the teacher.

        Args:
            value (str): The description of the teacher.

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
        Sets the difficulty of the teacher.

        Args:
            value (int): The difficulty of the teacher.

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
        Sets the metadata of the teacher.

        Args:
            value (Dict[str, Any]): The metadata of the teacher.

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
        Sets the name of the teacher.

        Args:
            value (str): The name of the teacher.

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
        Sets the priority of the teacher.

        Args:
            value (int): The priority of the teacher.

        Returns:
            Self: The builder instance.
        """

        self.configuration["priority"] = value
        return self

    def subjects(
        self,
        value: Union[List[str], str],
    ) -> Self:
        """
        Sets the subjects of the teacher.

        Args:
            value (Union[List[str], str]): The subjects of the teacher.

        Returns:
            Self: The builder instance.
        """

        if "subjects" not in self.configuration:
            self.configuration["subjects"] = []

        if isinstance(
            value,
            list,
        ):
            self.configuration["subjects"].extend(value)
        elif isinstance(
            value,
            str,
        ):
            self.configuration["subjects"].append(value)

        return self

    def tags(
        self,
        value: Union[List[str], str],
    ) -> Self:
        """
        Sets the tags of the teacher.

        Args:
            value (Union[List[str], str]): The tags of the teacher.

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


class TeacherManager(BaseObjectManager):
    """
    A manager class for managing teachers in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for teachers.

    Attributes:
        cache: (List[Any]): The cache for storing teachers.
        logger (Logger): The logger instance associated with the object.
    """

    _shared_instance: Optional["TeacherManager"] = None

    def __new__(cls) -> "TeacherManager":
        """
        Creates and returns a new instance of the TeacherManager class.

        If the instance does not exist, creates a new one by calling the parent class
        constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Returns:
            TeacherManager: The created or existing instance of TeacherManager class.
        """
        if cls._shared_instance is None:
            # Create a new instance by calling the parent class constructor
            cls._shared_instance = super(TeacherManager, cls).__new__(cls)
            # Initialize the instance
            cls._shared_instance.init()
        # Return the shared instance
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes a new instance of the TeacherManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def _run_pre_create_tasks(
        self,
        teacher: Union[
            ImmutableTeacher,
            MutableTeacher,
        ],
    ) -> MutableTeacher:
        """
        Runs pre-create tasks for the teacher.

        Args:
            teacher (Union[ImmutableTeacher, MutableTeacher]): The teacher to run pre-create tasks for.

        Returns:
            MutableTeacher: The teacher with pre-create tasks run.
        """

        # Check, if the teacher is not mutable
        if not teacher.is_mutable():
            # Convert the teacher to mutable
            teacher: MutableTeacher = teacher.to_mutable()

        # Set the created_at timestamp of the teacher
        teacher.created_at = teacher.created_at or Miscellaneous.get_current_datetime()

        # Set the key of the teacher
        teacher.key = f"TEACHER_{self.count_teachers() + 1}"

        # Set the updated_at timestamp of the teacher
        teacher.updated_at = teacher.updated_at or Miscellaneous.get_current_datetime()

        # Set the uuid of the teacher
        teacher.uuid = Miscellaneous.get_uuid()

        # Return the teacher
        return teacher

    def count_teachers(self) -> int:
        """
        Returns the number of teachers in the database.

        Returns:
            int: The number of teachers in the database.
        """
        try:
            # Count and return the number of teachers in the database
            return asyncio.run(TeacherModel.count(database=Constants.DATABASE_PATH))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_teacher(
        self,
        teacher: ImmutableTeacher,
    ) -> Optional[ImmutableTeacher]:
        """
        Creates a new teacher in the database.

        Args:
            difficulty (ImmutableTeacher): The teacher to be created.

        Returns:
            Optional[ImmutableTeacher]: The newly created immutable teacher if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the teacher.
        """
        try:
            # Initialize the result (optional) ImmutableTeacher to none
            result: Optional[ImmutableTeacher] = None

            # Run pre-create tasks
            teacher: MutableTeacher = self._run_pre_create_tasks(
                teacher=teacher
            )

            # Convert the teacher object to a TeacherModel object
            model: TeacherModel = TeacherConverter.object_to_model(object=teacher)

            # Create a new teacher in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            # Check, if the ID is not None
            if not id:
                # Log a warning message indicating an error has occurred
                self.logger.warning(
                    message=f"It seems that an error has occured while attempting to create a teacher ({teacher.__repr__()}) in the database."
                )

                # Return early
                return

            # Convert the teacher to a dictionary
            kwargs: Dict[str, Any] = teacher.to_dict(
                exclude=[
                    "_logger",
                ]
            )

            # Set the ID of the teacher
            kwargs["id"] = id

            # Create a new ImmutableTeacher object
            result = TeacherFactory.create_teacher(**kwargs)

            # Check, if the result is not None
            if not result:
                # Log an error message indicating an error has occurred
                self.logger.error(
                    message=f"It seems that there was an error while attempting to create an ImmutableTeacher from the dictionary ({kwargs}) returned by the database. This is likely a serious issue."
                )

                # Return early
                return

            # Add the teacher to the cache
            self.add_to_cache(
                key=result.key,
                value=result,
            )

            # Return the newly created ImmutableTeacher instance
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_teacher' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete_teacher(
        self,
        teacher: ImmutableTeacher,
    ) -> bool:
        """
        Deletes a teacher from the database.

        Args:
            difficulty (ImmutableTeacher): The teacher to be deleted.

        Returns:
            bool: True if the teacher was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the teacher to an immutable teacher and delete the teacher from the database
            result: bool = asyncio.run(
                TeacherConverter.object_to_model(
                    object=ImmutableTeacher(
                        **teacher.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).delete()
            )

            # Return True if the teacher was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all_teachers(
        self,
        force_refetch: bool = False,
    ) -> Optional[List[ImmutableTeacher]]:
        """
        Returns a list of all teachers in the database.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.

        Returns:
            Optional[List[ImmutableTeacher]]: A list of all teachers in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if cache and table size are equal
                if self.cache and len(self._cache) == self.count_teachers():
                    # Return the list of immutable teachers from the cache
                    return self.get_cache_values()

            # Get all teachers from the database
            models: List[TeacherModel] = asyncio.run(
                TeacherModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of TeacherModel objects to a list of Teacher objects
            teachers: List[ImmutableTeacher] = [
                ImmutableTeacher(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable teachers
            for teacher in teachers:
                if not self.is_key_in_cache(key=teacher.key):
                    # Add the immutable teacher to the cache
                    self.add_to_cache(
                        key=teacher.key,
                        value=teacher,
                    )
                else:
                    # Update the immutable teacher in the cache
                    self.update_in_cache(
                        key=teacher.key,
                        value=teacher,
                    )

            # Return the list of immutable teachers
            return teachers
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_teacher_by(
        self,
        field: str,
        value: Any,
        force_refetch: bool = False,
    ) -> Optional[ImmutableTeacher]:
        """
        Retrieves a teacher by the given field and value.

        Args:
            field (str): The field to search by.
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            value (Any): The value to search for.

        Returns:
            Optional[ImmutableTeacher]: The teacher with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if the teacher is already in the cache
                if self.is_key_in_cache(key=field):
                    # Return the teacher from the cache
                    return self.get_value_from_cache(key=field)

            # Get the teacher with the given field and value from the database
            model: Optional[TeacherModel] = asyncio.run(
                TeacherModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Return the teacher if it exists
            if model is not None:
                # Convert the TeacherModel object to an Teacher object
                return ImmutableTeacher(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the teacher does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_teacher_by_id(
        self,
        id: int,
        force_refetch: bool = False,
    ) -> Optional[ImmutableTeacher]:
        """
        Returns a teacher with the given ID.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            id (int): The ID of the teacher.

        Returns:
            Optional[ImmutableTeacher]: The teacher with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if the teacher is already in the cache
                if self.is_key_in_cache(key=f"TEACHER_{id}"):
                    # Return the teacher from the cache
                    return self.get_value_from_cache(key=f"TEACHER_{id}")

            # Get the teacher with the given ID from the database
            model: Optional[TeacherModel] = asyncio.run(
                TeacherModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the teacher if it exists
            if model is not None:
                # Convert the TeacherModel object to an Teacher object
                return ImmutableTeacher(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the teacher does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_teacher_by_id(
        self,
        key: str,
        force_refetch: bool = False,
    ) -> Optional[ImmutableTeacher]:
        """
        Returns a teacher with the given key.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            key (str): The ID of the teacher.

        Returns:
            Optional[ImmutableTeacher]: The teacher with the given key if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if the teacher is already in the cache
                if self.is_key_in_cache(key=key):
                    # Return the teacher from the cache
                    return self.get_value_from_cache(key=key)

            # Get the teacher with the given ID from the database
            model: Optional[TeacherModel] = asyncio.run(
                TeacherModel.get_by(
                    column="key",
                    database=Constants.DATABASE_PATH,
                    value=key,
                )
            )

            # Return the teacher if it exists
            if model is not None:
                # Convert the TeacherModel object to an Teacher object
                return ImmutableTeacher(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the teacher does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_key' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_teacher_by_uuid(
        self,
        uuid: str,
        force_refetch: bool = False,
    ) -> Optional[ImmutableTeacher]:
        """
        Returns a teacher with the given UUID.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            uuid (str): The UUID of the teacher.

        Returns:
            Optional[ImmutableTeacher]: The teacher with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if the teacher is already in the cache
                if self.is_key_in_cache(key=uuid):
                    # Return the teacher from the cache
                    return self.get_value_from_cache(key=uuid)

            # Get the teacher with the given UUID from the database
            model: Optional[TeacherModel] = asyncio.run(
                TeacherModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the teacher if it exists
            if model is not None:
                # Convert the TeacherModel object to an Teacher object
                return ImmutableTeacher(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the teacher does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def search_teachers(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[Union[List[ImmutableTeacher]]]:
        """
        Searches for teachers in the database.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            **kwargs: Any additional keyword arguments to be passed to the search method of the TeacherModel class.

        Returns:
            Optional[Union[List[ImmutableTeacher]]]: The found teachers if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Search the stack for the passed keyword arguments
                cached_result: Optional[List[ImmutableTeacher]] = self.search_cache(
                    **kwargs
                )

                # Check, if any cached results exist
                if cached_result:
                    # Return the cached results
                    return cached_result

            # Search for teachers in the database
            models: Optional[List[TeacherModel]] = asyncio.run(
                TeacherModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found teachers if any
            if models is not None and len(models) > 0:
                return [
                    ImmutableTeacher(
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
                # Return None indicating that no teachers were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_teacher(
        self,
        teacher: ImmutableTeacher,
    ) -> Optional[ImmutableTeacher]:
        """
        Updates a teacher with the given ID.

        Args:
            difficulty (ImmutableTeacher): The teacher to update.

        Returns:
            Optional[ImmutableTeacher]: The updated teacher if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the teacher to an immutable teacher and update the teacher in the database
            model: Optional[TeacherModel] = asyncio.run(
                TeacherConverter.object_to_model(
                    object=ImmutableTeacher(
                        **teacher.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).update(
                    database=Constants.DATABASE_PATH,
                    **teacher.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Return the updated teacher if it exists
            if model is not None:
                # Convert the TeacherModel object to an Teacher object
                teacher = ImmutableTeacher(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the teacher to the cache
                self.update_in_cache(
                    key=teacher.key,
                    value=teacher,
                )

                # Return the updated teacher
                return teacher
            else:
                # Return None indicating that the teacher does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class TeacherModel(ImmutableBaseModel):
    """
    Represents the structure of a teacher model.

    Attributes:
        created_at (datetime): The timestamp when the teacher was created.
        custom_field_values (List[Dict[str, Any]]): The custom field values of the teacher.
        description (str): The description of the teacher.
        difficulty (int): The teacher level of the teacher.
        icon (str): The icon associated with the teacher. Defaults to "🧑‍🏫".
        id (int): The unique identifier of the teacher.
        key (str): The key associated with the teacher.
        metadata (Dict[str, Any]): The meta data of the teacher.
        name (str): The name of the teacher.
        priority (int): The priority level of the teacher.
        subjects (List[str]): The subjects associated with the teacher.
        table (str, final): The (immutable) table name of the teacher. Defaults to "teachers".
        tags (List[str]): The tags associated with the teacher.
        updated_at (datetime): The timestamp when the teacher was last updated.
        uuid (str): The unique identifier of the teacher.
    """

    table: Final[str] = Constants.TEACHERS

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

    subjects: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="subjects",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
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
        subjects: Optional[List[str]] = None,
        tags: Optional[List[str]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the Teacher class.

        Args:
            created_at (Optional[datetime], optional): The creation date and time of the teacher. Defaults to None.
            custom_field_values (Optional[List[Dict[str, Any]]], optional): The custom field values of the teacher. Defaults to None.
            description (Optional[str], optional): The description of the teacher. Defaults to None.
            difficulty (Optional[int], optional): The teacher level of the teacher. Defaults to None.
            icon (Optional[str], optional): The icon associated with the teacher. Defaults to "🧑‍🏫".
            id (Optional[int], optional): The unique identifier of the teacher. Defaults to None.
            key (Optional[str], optional): The key associated with the teacher. Defaults to None.
            metadata (Optional[Dict[str, Any]], optional): The meta data of the teacher. Defaults to None.
            name (Optional[str], optional): The name of the teacher. Defaults to None.
            priority (Optional[int], optional): The priority level of the teacher. Defaults to None.
            subjects (Optional[List[str]], optional): The subjects associated with the teacher. Defaults to None.
            tags (Optional[List[str]], optional): The tags associated with the teacher. Defaults to None.
            updated_at (Optional[datetime], optional): The last update date and time of the teacher. Defaults to None.
            uuid (Optional[str], optional): The unique identifier of the teacher. Defaults to None.

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
            name=name,
            priority=priority,
            subjects=subjects,
            table=Constants.TEACHERS,
            tags=tags,
            updated_at=updated_at,
            uuid=uuid,
        )
