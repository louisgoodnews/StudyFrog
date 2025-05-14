"""
Author: lodego
Date: 2025-02-05
"""

import asyncio

from datetime import datetime

from typing import *

from core.difficulty import ImmutableDifficulty, MutableDifficulty
from core.priority import ImmutablePriority, MutablePriority

from utils.builder import BaseObjectBuilder
from utils.constants import Constants
from utils.field import Field
from utils.logger import Logger
from utils.manager import BaseObjectManager
from utils.miscellaneous import Miscellaneous
from utils.model import ImmutableBaseModel
from utils.object import MutableBaseObject, ImmutableBaseObject


__all__: Final[List[str]] = [
    "ImmutableNote",
    "MutableNote",
    "NoteConverter",
    "NoteFactory",
    "Notebuilder",
    "NoteManager",
    "NoteModel",
]


class ImmutableNote(ImmutableBaseObject):
    """
    An immutable class representing a Note.

    A Note is a learning tool used to aid memorization by providing a question on one side and the answer on the other.

    Attributes:
        body_text (str): The body of the Note.
        created_at (datetime): The timestamp when the Note was created.
        custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
        difficulty (int): The difficulty of the Note.
        due_by (datetime): The due date of the Note.
        icon (str): The icon of the Note.
        id (int): The ID of the Note.
        interval (float): The review interval of the Note.
        key (str): The key of the Note.
        last_viewed_at (datetime): The timestamp when the Note was last viewed.
        metadata (Optional[Dict[str, Any]]): The metadata of the Note.
        priority (int): The priority of the Note.
        status (int): The status of the Note.
        tags (Optional[List[str]]): The key of the tags associated with the Note.
        title_text (str): The title of the Note.
        updated_at (datetime): The timestamp when the Note was last updated.
        uuid (str): The UUID of the Note.
    """

    def __init__(
        self,
        body_text: str,
        title_text: str,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        difficulty: Optional[int] = None,
        due_by: Optional[datetime] = None,
        icon: Optional[str] = "📝",
        id: Optional[int] = None,
        interval: Optional[float] = None,
        key: Optional[str] = None,
        last_viewed_at: Optional[datetime] = None,
        metadata: Optional[Dict[str, Any]] = None,
        priority: Optional[int] = None,
        status: Optional[int] = None,
        tags: Optional[List[str]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableNote class.

        Args:
            body_text (str): The body of the Note.
            created_at (datetime): The timestamp when the Note was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
            difficulty (Optional[int]): The difficulty of the Note.
            due_by (datetime): The due date of the Note.
            icon (str): The icon of the Note. Defaults to "📝".
            id (int): The ID of the Note.
            interval (float): The review interval of the Note.
            key (str): The key of the Note.
            last_viewed_at (datetime): The timestamp when the Note was last viewed.
            metadata (Optional[Dict[str, Any]]): The metadata of the Note.
            priority (int): The priority of the Note.
            status (int): The status of the Note.
            tags (Optional[List[str]]): The key of the tags associated with the Note.
            title_text (str): The title of the Note.
            updated_at (datetime): The timestamp when the Note was last updated.
            uuid (str): The UUID of the Note.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            body_text=body_text,
            created_at=created_at,
            custom_field_values=custom_field_values,
            difficulty=difficulty,
            due_by=due_by,
            hide_attributes=True,
            icon=icon,
            id=id,
            interval=interval,
            key=key,
            last_viewed_at=last_viewed_at,
            metadata=metadata,
            priority=priority,
            status=status,
            tags=tags,
            title_text=title_text,
            updated_at=updated_at,
            uuid=uuid,
        )

    @property
    def created_at(self) -> datetime:
        """
        Returns the timestamp when the Note was created.

        Returns:
            datetime: The timestamp when the Note was created.
        """

        # Return the ImmutableNote instance's created_at attribute
        return self._created_at

    @property
    def custom_field_values(self) -> Optional[List[Dict[str, Any]]]:
        """
        Returns the custom field values of the Note.

        Returns:
            Optional[List[Dict[str, Any]]]: The custom field values of the Note.
        """

        # Return the ImmutableNote instance's custom_field_values attribute
        return self._custom_field_values

    @property
    def difficulty(self) -> int:
        """
        Returns the difficulty of the Note.

        Returns:
            int: The difficulty of the Note.
        """

        # Return the ImmutableNote instance's difficulty attribute
        return self._difficulty

    @property
    def due_by(self) -> datetime:
        """
        Returns the due date of the Note.

        Returns:
            datetime: The due date of the Note.
        """

        # Return the ImmutableNote instance's due_by attribute
        return self._due_by

    @property
    def icon(self) -> str:
        """
        Returns the icon of the Note.

        Returns:
            str: The icon of the Note.
        """

        # Return the ImmutableNote instance's icon attribute
        return self._icon

    @property
    def id(self) -> int:
        """
        Returns the ID of the Note.

        Returns:
            int: The ID of the Note.
        """

        # Return the ImmutableNote instance's id attribute
        return self._id

    @property
    def interval(self) -> float:
        """
        Returns the review interval of the Note.

        Returns:
            float: The review interval of the Note.
        """

        # Return the ImmutableNote instance's interval attribute
        return self._interval

    @property
    def key(self) -> str:
        """
        Returns the key of the Note.

        Returns:
            str: The key of the Note.
        """

        # Return the ImmutableNote instance's key attribute
        return self._key

    @property
    def last_viewed_at(self) -> datetime:
        """
        Returns the timestamp when the Note was last viewed.

        Returns:
            datetime: The timestamp when the Note was last viewed.
        """

        # Return the ImmutableNote instance's last_viewed_at attribute
        return self._last_viewed_at

    @property
    def metadata(self) -> Optional[Dict[str, Any]]:
        """
        Returns the metadata of the Note.

        Returns:
            Optional[Dict[str, Any]]: The metadata of the Note.
        """

        # Return the ImmutableNote instance's metadata attribute
        return self._metadata

    @property
    def priority(self) -> int:
        """
        Returns the priority of the Note.

        Returns:
            int: The priority of the Note.
        """

        # Return the ImmutableNote instance's priority attribute
        return self._priority

    @property
    def status(self) -> int:
        """
        Returns the status of the Note.

        Returns:
            int: The status of the Note.
        """

        # Return the ImmutableNote instance's status attribute
        return self._status

    @property
    def tags(self) -> Optional[List[str]]:
        """
        Returns the tags associated with the Note.

        Returns:
            Optional[List[str]]: The tags associated with the Note.
        """

        # Return the ImmutableNote instance's tags attribute
        return self._tags

    @property
    def title_text(self) -> str:
        """
        Returns the title of the Note.

        Returns:
            str: The title of the Note.
        """

        # Return the ImmutableNote instance's title_text attribute
        return self._title_text

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp when the Note was last updated.

        Returns:
            datetime: The timestamp when the Note was last updated.
        """

        # Return the ImmutableNote instance's updated_at attribute
        return self._updated_at

    @property
    def uuid(self) -> str:
        """
        Returns the UUID of the Note.

        Returns:
            str: The UUID of the Note.
        """

        # Return the ImmutableNote instance's uuid attribute
        return self._uuid

    def to_mutable(self) -> Optional["MutableNote"]:
        """
        Returns a mutable copy of the ImmutableNote instance.

        Returns:
            Optional[MutableNote]: A mutable copy of the ImmutableNote instance.
        """
        try:
            # Create a new MutableNote instance from the dictionary representation of the ImmutableNote instance
            return MutableNote(
                **self.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_mutable' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating that an exception has occurred
            return None


class MutableNote(MutableBaseObject):
    """
    An immutable class representing a Note.

    A Note is a learning tool used to aid memorization by providing a question on one side and the answer on the other.

    Attributes:
        body_text (str): The body of the Note.
        created_at (datetime): The timestamp when the Note was created.
        custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
        difficulty (int): The difficulty of the Note.
        due_by (datetime): The due date of the Note.
        icon (str): The icon of the Note.
        id (int): The ID of the Note.
        interval (float): The review interval of the Note.
        key (str): The key of the Note.
        last_viewed_at (datetime): The timestamp when the Note was last viewed.
        metadata (Optional[Dict[str, Any]]): The metadata of the Note.
        priority (int): The priority of the Note.
        status (int): The status of the Note.
        tags (Optional[List[str]]): The key of the tags associated with the Note.
        title_text (str): The title of the Note.
        updated_at (datetime): The timestamp when the Note was last updated.
        uuid (str): The UUID of the Note.
    """

    def __init__(
        self,
        body_text: str,
        title_text: str,
        ancestor: Optional[int] = None,
        children: Optional[List[int]] = None,
        created_at: Optional[datetime] = None,
        difficulty: Optional[int] = None,
        due_by: Optional[datetime] = None,
        icon: Optional[str] = "📝",
        id: Optional[int] = None,
        interval: Optional[float] = None,
        key: Optional[str] = None,
        last_viewed_at: Optional[datetime] = None,
        metadata: Optional[Dict[str, Any]] = None,
        priority: Optional[int] = None,
        status: Optional[int] = None,
        tags: Optional[List[str]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableNote class.

        Args:
            body_text (str): The body of the Note.
            ancestor (int): The ID of the ancestor Note.
            children (List[int]): The IDs of the children Notes.
            created_at (datetime): The timestamp when the Note was created.
            difficulty (int): The difficulty of the Note.
            due_by (datetime): The due date of the Note.
            icon (str): The icon of the Note. Defaults to "📝".
            id (int): The ID of the Note.
            interval (float): The review interval of the Note.
            key (str): The key of the Note.
            last_viewed_at (datetime): The timestamp when the Note was last viewed.
            metadata (Optional[Dict[str, Any]]): The metadata of the Note.
            priority (int): The priority of the Note.
            status (int): The status of the Note.
            tags (Optional[List[str]]): The key of the tags associated with the Note.
            title_text (str): The title of the Note.
            updated_at (datetime): The timestamp when the Note was last updated.
            uuid (str): The UUID of the Note.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            body_text=body_text,
            ancestor=ancestor,
            children=children,
            created_at=created_at,
            difficulty=difficulty,
            due_by=due_by,
            hide_attributes=True,
            icon=icon,
            id=id,
            interval=interval,
            key=key,
            last_viewed_at=last_viewed_at,
            metadata=metadata,
            priority=priority,
            status=status,
            tags=tags,
            title_text=title_text,
            updated_at=updated_at,
            uuid=uuid,
        )

    @property
    def created_at(self) -> datetime:
        """
        Returns the timestamp when the Note was created.

        Returns:
            datetime: The timestamp when the Note was created.
        """

        # Return the ImmutableNote instance's created_at attribute
        return self._created_at

    @created_at.setter
    def created_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the timestamp when the Note was created.

        Args:
            value (datetime): The timestamp when the Note was created.

        Returns:
            None
        """

        # Set the created_at attribute
        self._created_at = value

    @property
    def custom_field_values(self) -> Optional[List[Dict[str, Any]]]:
        """
        Returns the custom field values of the Note.

        Returns:
            Optional[List[Dict[str, Any]]]: The custom field values of the Note.
        """

        # Return the ImmutableNote instance's custom_field_values attribute
        return self._custom_field_values

    @custom_field_values.setter
    def custom_field_values(
        self,
        value: Union[Dict[str, Any], List[Dict[str, Any]]],
    ) -> None:
        """
        Sets the custom field values of the Note.

        Args:
            value (Union[Dict[str, Any], List[Dict[str, Any]]): The new custom field values of the Note.

        Returns:
            None
        """

        # Check, if the custom_field_values list exists
        if not self.get(
            default=None,
            name="custom_field_values",
        ):
            # Initialize the custom_field_values list as an empty list
            self._custom_field_values = []

        # Check, if the passed value is a dictionary
        if isinstance(
            value,
            dict,
        ):
            # Append the passed value to the list
            self._custom_field_values.append(value)
        # Check, if the passed value is a list
        elif isinstance(
            value,
            list,
        ):
            # Extend the list with the passed value
            self._custom_field_values.extend(value)

    @property
    def difficulty(self) -> int:
        """
        Returns the difficulty of the Note.

        Returns:
            int: The difficulty of the Note.
        """

        # Return the ImmutableNote instance's difficulty attribute
        return self._difficulty

    @difficulty.setter
    def difficulty(
        self,
        value: int,
    ) -> None:
        """
        Sets the difficulty of the Note.

        Args:
            value (int): The new difficulty of the Note.

        Returns:
            None
        """

        # Set the difficulty attribute
        self._difficulty = value

    @property
    def due_by(self) -> datetime:
        """
        Returns the due date of the Note.

        Returns:
            datetime: The due date of the Note.
        """

        # Return the ImmutableNote instance's due_by attribute
        return self._due_by

    @due_by.setter
    def due_by(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the due date of the Note.

        Args:
            value (datetime): The new due date of the Note.

        Returns:
            None
        """

        # Set the due_by attribute
        self._due_by = value

    @property
    def icon(self) -> str:
        """
        Returns the icon of the Note.

        Returns:
            str: The icon of the Note.
        """

        # Return the ImmutableNote instance's icon attribute
        return self._icon

    @icon.setter
    def icon(
        self,
        value: str,
    ) -> None:
        """
        Sets the icon of the Note.

        Args:
            value (str): The new icon of the Note.

        Returns:
            None
        """

        # Set the icon attribute
        self._icon = value

    @property
    def id(self) -> int:
        """
        Returns the ID of the Note.

        Returns:
            int: The ID of the Note.
        """

        # Return the ImmutableNote instance's id attribute
        return self._id

    @id.setter
    def id(
        self,
        value: int,
    ) -> None:
        """
        Sets the ID of the Note.

        Args:
            value (int): The new ID of the Note.

        Returns:
            None
        """

        # Set the id attribute
        self._id = value

    @property
    def interval(self) -> float:
        """
        Returns the review interval of the Note.

        Returns:
            float: The review interval of the Note.
        """

        # Return the ImmutableNote instance's interval attribute
        return self._interval

    @interval.setter
    def interval(
        self,
        value: float,
    ) -> None:
        """
        Sets the review interval of the Note.

        Args:
            value (float): The new review interval of the Note.

        Returns:
            None
        """

        # Set the interval attribute
        self._interval = value

    @property
    def key(self) -> str:
        """
        Returns the key of the Note.

        Returns:
            str: The key of the Note.
        """

        # Return the ImmutableNote instance's key attribute
        return self._key

    @key.setter
    def key(
        self,
        value: str,
    ) -> None:
        """
        Sets the key of the Note.

        Args:
            value (str): The new key of the Note.

        Returns:
            None
        """

        # Set the key attribute
        self._key = value

    @property
    def last_viewed_at(self) -> datetime:
        """
        Returns the timestamp when the Note was last viewed.

        Returns:
            datetime: The timestamp when the Note was last viewed.
        """

        # Return the ImmutableNote instance's last_viewed_at attribute
        return self._last_viewed_at

    @last_viewed_at.setter
    def last_viewed_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the timestamp when the Note was last viewed.

        Args:
            value (datetime): The new timestamp when the Note was last viewed.

        Returns:
            None
        """

        # Set the last_viewed_at attribute
        self._last_viewed_at = value

    @property
    def metadata(self) -> Optional[Dict[str, Any]]:
        """
        Returns the metadata of the Note.

        Returns:
            Optional[Dict[str, Any]]: The metadata of the Note.
        """

        # Return the ImmutableNote instance's metadata attribute
        return self._metadata

    @metadata.setter
    def metadata(
        self,
        **kwargs,
    ) -> None:
        """
        Updates the metadata of the flashcard.

        Args:
            **kwargs (Dict[str, Any]): The new metadata of the flashcard.

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
    def priority(self) -> int:
        """
        Gets the priority of the Note.

        Returns:
            int: The priority of the Note.
        """
        return self._priority

    @priority.setter
    def priority(
        self,
        value: int,
    ) -> None:
        """
        Sets the priority of the Note.

        Args:
            value (int): The new priority of the Note.

        Returns:
            None
        """
        self._priority = value

    @property
    def status(self) -> int:
        """
        Gets the status of the Note.

        Returns:
            int: The status of the Note.
        """
        return self._status

    @status.setter
    def status(
        self,
        value: int,
    ) -> None:
        """
        Sets the status of the Note.

        Args:
            value (int): The new status of the Note.

        Returns:
            None
        """
        self._status = value

    @property
    def tags(self) -> Optional[List[str]]:
        """
        Returns the tags associated with the Note.

        Returns:
            Optional[List[str]]: The tags associated with the Note.
        """

        # Return the ImmutableNote instance's tags attribute
        return self._tags

    @tags.setter
    def tags(
        self,
        value: Union[List[str], str],
    ) -> None:
        """
        Sets the tags of the Note.

        Args:
            value (Union[List[str], str]): The new tags of the Note.

        Returns:
            None
        """

        # Check, if the passed value is a string
        if isinstance(
            value,
            str,
        ):
            # Append the passed value to the list
            self._tags.append(value)
        # Check, if the passed value is a list
        elif isinstance(
            value,
            list,
        ):
            # Extend the list with the passed value
            self._tags.extend(value)

    @property
    def title_text(self) -> str:
        """
        Returns the title of the Note.

        Returns:
            str: The title of the Note.
        """

        # Return the ImmutableNote instance's title_text attribute
        return self._title_text

    @title_text.setter
    def title_text(
        self,
        value: str,
    ) -> None:
        """
        Sets the title of the Note.

        Args:
            value (str): The new title of the Note.

        Returns:
            None
        """
        self._title_text = value

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp when the Note was last updated.

        Returns:
            datetime: The timestamp when the Note was last updated.
        """

        # Return the ImmutableNote instance's updated_at attribute
        return self._updated_at

    @updated_at.setter
    def updated_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the timestamp when the Note was last updated.

        Args:
            value (datetime): The new timestamp when the Note was last updated.

        Returns:
            None
        """
        self._updated_at = value

    @property
    def uuid(self) -> str:
        """
        Returns the UUID of the Note.

        Returns:
            str: The UUID of the Note.
        """

        # Return the ImmutableNote instance's uuid attribute
        return self._uuid

    @uuid.setter
    def uuid(
        self,
        value: str,
    ) -> None:
        """
        Sets the UUID of the Note.

        Args:
            value (str): The new UUID of the Note.

        Returns:
            None
        """
        self._uuid = value

    def add_child(
        self,
        child: Union[
            ImmutableNote,
            "MutableNote",
        ],
    ) -> None:
        """
        Adds a child Note to the Note.

        Args:
            child (Union[ImmutableNote, MutableNote]): The child Note to be added.

        Returns:
            None
        """

        # Add the child to the list of children
        self.children.append(child.id)

    def remove_child(
        self,
        child: Union[
            ImmutableNote,
            "MutableNote",
        ],
    ) -> None:
        """
        Removes a child Note from the Note.

        Args:
            child (Union[ImmutableNote, MutableNote]): The child Note to be removed.

        Returns:
            None
        """

        # Check if the child is already in the list of children
        if child.id not in self.children:
            # Log a warning message
            self.logger.warning(
                f"Child with ID {child.id} not found in list of children for {self.__class__.__name__} with ID {self.id}"
            )

            # Return if the child is not in the list of children
            return

        # Remove the child from the list of children
        self.children.remove(child.id)

    def set_ancestor(
        self,
        ancestor: Union[
            ImmutableNote,
            "MutableNote",
        ],
    ) -> None:
        """
        Sets the ancestor of the Note.

        Args:
            ancestor (Union[ImmutableNote, MutableNote]): The ancestor of the Note.

        Returns:
            None
        """

        # Set the ancestor of the Note
        self.ancestor = ancestor.id

    def set_difficulty(
        self,
        difficulty: Union[
            ImmutableDifficulty,
            MutableDifficulty,
        ],
    ) -> None:
        """
        Sets the difficulty of the Note.

        Args:
            difficulty (Union[ImmutableDifficulty, MutableDifficulty]): The difficulty of the Note.

        Returns:
            None
        """

        # Set the difficulty of the Note
        self.difficulty = difficulty.id

    def set_priority(
        self,
        priority: Union[
            ImmutablePriority,
            MutablePriority,
        ],
    ) -> None:
        """
        Sets the priority of the Note.

        Args:
            priority (Union[ImmutablePriority, MutablePriority]): The priority of the Note.

        Returns:
            None
        """

        # Set the priority of the Note
        self.priority = priority.id

    def to_immutable(self) -> Optional[ImmutableNote]:
        """
        Returns an immutable copy of the MutableNote instance.

        Returns:
            Optional[ImmutableNote]: An immutable copy of the MutableNote instance.
        """
        try:
            # Create a new ImmutableNote instance from the dictionary representation of the MutableNote instance
            return ImmutableNote(
                **self.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_immutable' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating that an exception has occurred
            return None


class NoteConverter:
    """
    A converter class for transforming between NoteModel and ImmutableNote instances.

    This class provides methods to convert a NoteModel instance to an ImmutableNote instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the NoteConverter class.
    """

    logger: Final[Logger] = Logger.get_logger(name="NoteConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "NoteModel",
    ) -> Optional[ImmutableNote]:
        """
        Converts a given NoteModel instance to an ImmutableNote instance.

        Args:
            model (NoteModel): The NoteModel instance to be converted.

        Returns:
            ImmutableNote: The converted ImmutableNote instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the NoteModel instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableNote class from the dictionary representation of the NoteModel instance
            return ImmutableNote(
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
        object: ImmutableNote,
    ) -> Optional["NoteModel"]:
        """
        Converts a given ImmutableNote instance to a NoteModel instance.

        Args:
            object (ImmutableNote): The ImmutableNote instance to be converted.

        Returns:
            NoteModel: The converted NoteModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ImmutableNote instance.
        """
        try:
            # Attempt to create and return a new instance of the NoteModel class from the dictionary representation of the ImmutableNote instance
            return NoteModel(
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


class NoteFactory:
    """
    A factory class used to create instances of ImmutableNote class.

    Attributes:
        logger (Logger): The logger instance associated with the object.
    """

    logger: Final[Logger] = Logger.get_logger(name="NoteFactory")

    @classmethod
    def create_Note(
        cls,
        body_text: str,
        title_text: str,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        difficulty: Optional[int] = None,
        due_by: Optional[datetime] = None,
        icon: Optional[str] = "📝",
        id: Optional[int] = None,
        interval: Optional[float] = None,
        key: Optional[str] = None,
        last_viewed_at: Optional[datetime] = None,
        metadata: Optional[Dict[str, Any]] = None,
        priority: Optional[int] = None,
        status: Optional[int] = None,
        tags: Optional[List[str]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutableNote]:
        """
        Creates and returns a new instance of ImmutableNote class.

        Args:
            body_text (str): The body of the Note.
            title_text (str): The title of the Note.
            created_at (Optional[datetime]): The timestamp when the Note was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
            difficulty (Optional[int]): The difficulty of the Note.
            due_by (Optional[datetime]): The due date of the Note.
            icon (Optional[str]): The icon of the Note. Defaults to "📝".
            id (Optional[int]): The ID of the Note.
            interval (Optional[float]): The review interval of the Note.
            key (Optional[str]): The key of the Note.
            last_viewed_at (Optional[datetime]): The timestamp when the Note was last viewed.
            metadata (Optional[Dict[str, Any]]): The metadata of the Note.
            priority (Optional[int]): The priority of the Note.
            status (Optional[int]): The status of the Note.
            tags (Optional[List[str]]): The key of the tags associated with the Note.
            updated_at (Optional[datetime]): The timestamp when the Note was last updated.
            uuid (Optional[str]): The UUID of the Note.

        Returns:
            Optional[ImmutableNote]: The created Note object if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the Note.
        """
        try:
            # Attempt to create an d return an ImmutableNote object
            return ImmutableNote(
                body_text=body_text,
                created_at=created_at,
                custom_field_values=custom_field_values,
                difficulty=difficulty,
                due_by=due_by,
                icon=icon,
                id=id,
                interval=interval,
                key=key,
                last_viewed_at=last_viewed_at,
                metadata=metadata,
                priority=priority,
                status=status,
                tags=tags,
                title_text=title_text,
                updated_at=updated_at,
                uuid=uuid,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_Note' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class NoteBuilder(BaseObjectBuilder):
    """
    A builder class used to create instances of ImmutableNote class.

    Attributes:
        configuration (Dict[str, Any]): The dictionary containing the configuration of the object to be built.
        logger (Logger): The logger instance associated with the object.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the NoteBuilder class.

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
            ImmutableNote,
            MutableNote,
        ]
    ]:
        """
        Builds an instance of the ImmutableNote or MutableNote class using the configuration dictionary.

        This method is responsible for creating an instance of the ImmutableNote or MutableNote class based on the configuration dictionary
        passed to the constructor. If an exception occurs while creating the instance, this method will log an error message
        and return None.

        Args:
            as_mutable (bool): A flag indicating whether the note should be mutable.

        Returns:
            Optional[Union[ImmutableNote, MutableNote]]: An instance of the ImmutableNote or MutableNote class if no exception occurs. Otherwise, None.
        """
        try:
            # Attempt to create an instance of the ImmutableNote class using the configuration dictionary
            note: Optional[ImmutableNote] = NoteFactory.create_note(
                **self.configuration
            )

            if not note:
                # Log an error message indicating an exception has occurred
                self.logger.error(
                    message=f"Failed to build an instance of the ImmutableNote or MutableNote class from '{self.__class__.__name__}'"
                )

                # Raise an exception
                raise Exception(
                    f"Failed to build an instance of the ImmutableNote or MutableNote class from '{self.__class__.__name__}'"
                )

            # Check if the instance should be mutable
            if as_mutable:
                # Convert the instance to a MutableNote
                return note.to_mutable()

            # Return the instance
            return note
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'build' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def body_text(
        self,
        value: str,
    ) -> Self:
        """
        Sets the body text of the note.

        Args:
            value (str): The body text of the note.

        Returns:
            Self: The builder instance.
        """

        # Set the body_text value in the configuration dictionary
        self.configuration["body_text"] = value

        # Return the builder instance
        return self

    def custom_field_values(
        self,
        value: Union[Dict[str, Any], List[Dict[str, Any]]],
    ) -> Self:
        """
        Sets the custom field values for the builder.

        Args:
            value (Union[Dict[str, Any], List[Dict[str, Any]]]): The custom field values to set.

        Returns:
            Self: The builder instance with the custom field values set.
        """

        # Check, if the 'custom field values' key exists in the Builder instance's configuration dictionary
        if "custom_field_values" not in self.configuration:
            # Initialize the 'custom field values' key with an empty list
            self.configuration["custom_field_values"] = []

        # Check, if the passed value is a dictionary
        if isinstance(
            value,
            dict,
        ):
            # Convert the dictionary to a list of dictionaries
            value = [value]
        # Check, if the passed value is a list
        elif isinstance(
            value,
            list,
        ):
            # Update the 'custom field values' list with the new values
            self.configuration["custom_field_values"] = value

        # Return the builder instance
        return self

    def difficulty(
        self,
        value: int,
    ) -> Self:
        """
        Sets the difficulty of the note.

        Args:
            value (int): The difficulty of the note.

        Returns:
            Self: The builder instance.
        """

        # Set the difficulty value in the configuration dictionary
        self.configuration["difficulty"] = value

        # Return the builder instance
        return self

    def metadata(
        self,
        value: Dict[str, Any],
    ) -> Self:
        """
        Sets the metadata of the note.

        Args:
            value (Dict[str, Any]): The metadata of the note.

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

    def priority(
        self,
        value: int,
    ) -> Self:
        """
        Sets the priority of the note.

        Args:
            value (int): The priority of the note.

        Returns:
            Self: The builder instance.
        """

        # Set the priority value in the configuration dictionary
        self.configuration["priority"] = value

        # Return the builder instance
        return self

    def status(
        self,
        value: int,
    ) -> Self:
        """
        Sets the status of the note.

        Args:
            value (int): The status of the note.

        Returns:
            Self: The builder instance.
        """

        # Set the status value in the configuration dictionary
        self.configuration["status"] = value

        # Return the builder instance
        return self

    def tags(
        self,
        value: List[str],
    ) -> Self:
        """
        Sets the tags of the note.

        Args:
            value (List[str]): The tags of the note.

        Returns:
            Self: The builder instance.
        """

        # Set the tags value in the configuration dictionary
        self.configuration["tags"] = value

        # Return the builder instance
        return self

    def title_text(
        self,
        value: str,
    ) -> Self:
        """
        Sets the title text of the note.

        Args:
            value (str): The title text of the note.

        Returns:
            Self: The builder instance.
        """

        # Set the title_text value in the configuration dictionary
        self.configuration["title_text"] = value

        # Return the builder instance
        return self


class NoteManager(BaseObjectManager):
    """
    A manager class for managing notes in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for notes.

    Attributes:
        cache: (List[Any]): The cache for storing notes.
        logger (Logger): The logger instance associated with the object.
    """

    _shared_instance: Optional["NoteManager"] = None

    def __new__(cls) -> "NoteManager":
        """
        Creates and returns a new instance of the NoteManager class.

        If the instance does not exist, creates a new one by calling the parent class
        constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Returns:
            NoteManager: The created or existing instance of NoteManager class.
        """
        if cls._shared_instance is None:
            # Create a new instance by calling the parent class constructor
            cls._shared_instance = super(NoteManager, cls).__new__(cls)
            # Initialize the instance
            cls._shared_instance.init()
        # Return the shared instance
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes a new instance of the NoteManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def _run_pre_create_tasks(
        self,
        note: Union[
            ImmutableNote,
            MutableNote,
        ],
    ) -> MutableNote:
        """
        Runs pre-create tasks for the note.

        Args:
            note (Union[ImmutableNote, MutableNote]): The note to run pre-create tasks for.

        Returns:
            MutableNote: The note with pre-create tasks run.
        """

        # Check if the note object is immutable
        if not note.is_mutable():
            # If it is, convert it to a mutable note
            note: MutableNote = note.to_mutable()

        # Set the created_at timestamp of the note
        note.created_at = Miscellaneous.get_current_datetime()

        # Set the custom_field_values of the note
        note.custom_field_values = [] or note.custom_field_values

        # Set the key of the note
        note.key = f"NOTE_{self.count_notes() + 1}"

        # Set the metadata of the note
        note.metadata = {} or note.metadata

        # Set the tags of the note
        note.tags = [] or note.tags

        # Set the updated_at timestamp of the note
        note.updated_at = Miscellaneous.get_current_datetime()

        # Set the uuid of the note
        note.uuid = Miscellaneous.get_uuid()

        # Return the mutable note
        return note

    def count_notes(self) -> int:
        """
        Returns the number of notes in the database.

        Returns:
            int: The number of notes in the database.
        """
        try:
            # Count and return the number of notes in the database
            return asyncio.run(NoteModel.count(database=Constants.DATABASE_PATH))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_note(
        self,
        note: Union[ImmutableNote, MutableNote],
    ) -> Optional[ImmutableNote]:
        """
        Creates a new note in the database.

        Args:
            note (Union[ImmutableNote, MutableNote]): The note to be created.

        Returns:
            Optional[ImmutableNote]: The newly created immutable note if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the note.
        """
        try:
            # Initialize the result (optional) ImmutableNote to none
            result: Optional[ImmutableNote] = None

            # Run pre-create tasks
            note: MutableNote = self._run_pre_create_tasks(note=note)

            # Convert the note object to a NoteModel object
            model: NoteModel = NoteConverter.object_to_model(object=note)

            # Create a new note in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            # Check, if the ID is not None
            if not id:
                # Log a warning message indicating an error has occurred
                self.logger.warning(
                    message=f"It seems that an error has occured while attempting to create a note ({note.__repr__()}) in the database."
                )

                # Return early
                return

            # Convert the note to a dictionary
            kwargs: Dict[str, Any] = note.to_dict(
                exclude=[
                    "_logger",
                ]
            )

            # Set the ID of the note
            kwargs["id"] = id

            # Create a new ImmutableNote object
            result = NoteFactory.create_note(**kwargs)

            # Check, if the result is not None
            if not result:
                # Log an error message indicating an error has occurred
                self.logger.error(
                    message=f"It seems that there was an error while attempting to create an ImmutableNote from the dictionary ({kwargs}) returned by the database. This is likely a serious issue."
                )

                # Return early
                return

            # Add the note to the cache
            self.add_to_cache(
                key=result.key,
                value=result,
            )

            # Return the newly created immutable note
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_note' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete_note(
        self,
        note: Union[ImmutableNote, MutableNote],
    ) -> bool:
        """
        Deletes a note from the database.

        Args:
            note (Union[ImmutableNote, MutableNote]): The note to be deleted.

        Returns:
            bool: True if the note was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the note to an immutable note and delete the note from the database
            result: bool = asyncio.run(
                NoteConverter.object_to_model(
                    object=ImmutableNote(
                        **note.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).delete()
            )

            # Return True if the note was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all_notes(self) -> Optional[List[ImmutableNote]]:
        """
        Returns a list of all notes in the database.

        Returns:
            Optional[List[ImmutableNote]]: A list of all notes in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if cache and table size are equal
            if self.cache and len(self._cache) == self.count_notes():
                # Return the list of immutable notes from the cache
                return self.get_cache_values()

            # Get all notes from the database
            models: List[NoteModel] = asyncio.run(
                NoteModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of NoteModel objects to a list of ImmutableNote objects
            notes: List[ImmutableNote] = [
                ImmutableNote(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable notes
            for note in notes:
                if not self.is_key_in_cache(key=note.key):
                    # Add the immutable note to the cache
                    self.add_to_cache(
                        key=note.key,
                        value=note,
                    )
                else:
                    # Update the immutable note in the cache
                    self.update_in_cache(
                        key=note.key,
                        value=note,
                    )

            # Return the list of immutable notes
            return notes
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_from_notes(
        self,
        condition: Callable[[ImmutableNote], bool],
        limit: Optional[int] = None,
    ) -> Optional[List[ImmutableNote]]:
        """
        Returns a list of notes from the cache that match the given condition.

        Args:
            condition (Callable[[ImmutableNote], bool]): A function that takes an ImmutableNote instance and returns a boolean value.
            limit (Optional[int]): The maximum number of notes to return.

        Returns:
            Optional[List[ImmutableNote]]: The list of notes that match the given condition if no exception occurs. Otherwise, None.
        """
        try:
            # Initialize an empty list to store matching notes
            result: List[ImmutableNote] = []

            # Get all notes from the cache
            notes: List[ImmutableNote] = self.get_all_notes()

            # Iterate over the list of immutable notes in the cache
            for note in notes:
                # Check if the note matches the given condition
                if condition(note):
                    # Add the note that matches the given condition to the result list
                    result.append(note)

            # Check if the limit is specified and if the result list exceeds the limit
            if limit is not None and len(result) > limit:
                # Return the first 'limit' number of notes
                return result[:limit]

            # Return the list of matching notes
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_from_notes' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_note_by(
        self,
        field: str,
        value: Any,
    ) -> Optional[ImmutableNote]:
        """
        Retrieves a note by the given field and value.

        Args:
            field (str): The field to search by.
            value (Any): The value to search for.

        Returns:
            Optional[ImmutableNote]: The note with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the note is already in the cache
            if self.is_key_in_cache(key=field):
                # Return the note from the cache
                return self.get_value_from_cache(key=field)

            # Get the note with the given field and value from the database
            model: Optional[NoteModel] = asyncio.run(
                NoteModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Return the note if it exists
            if model is not None:
                # Convert the NoteModel object to an ImmutableNote object
                return ImmutableNote(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the note does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_note_by_id(
        self,
        id: int,
    ) -> Optional[ImmutableNote]:
        """
        Returns a note with the given ID.

        Args:
            id (int): The ID of the note.

        Returns:
            Optional[ImmutableNote]: The note with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the note is already in the cache
            if self.is_key_in_cache(key=f"NOTE_{id}"):
                # Return the note from the cache
                return self.get_value_from_cache(key=f"NOTE_{id}")

            # Get the note with the given ID from the database
            model: Optional[NoteModel] = asyncio.run(
                NoteModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the note if it exists
            if model is not None:
                # Convert the NoteModel object to an ImmutableNote object
                return ImmutableNote(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the note does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_note_by_uuid(
        self,
        uuid: str,
    ) -> Optional[ImmutableNote]:
        """
        Returns a note with the given UUID.

        Args:
            uuid (str): The UUID of the note.

        Returns:
            Optional[ImmutableNote]: The note with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the note is already in the cache
            if self.is_key_in_cache(key=uuid):
                # Return the note from the cache
                return self.get_value_from_cache(key=uuid)

            # Get the note with the given UUID from the database
            model: Optional[NoteModel] = asyncio.run(
                NoteModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the note if it exists
            if model is not None:
                # Convert the NoteModel object to an ImmutableNote object
                return ImmutableNote(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the note does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def search_notes(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[Union[List[ImmutableNote]]]:
        """
        Searches for notes in the database.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            **kwargs: Any additional keyword arguments to be passed to the search method of the NoteModel class.

        Returns:
            Optional[Union[List[ImmutableNote]]]: The found notes if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Search the stack for the passed keyword arguments
                cached_result: Optional[List[ImmutableNote]] = self.search_cache(
                    **kwargs
                )

                # Check, if any cached results exist
                if cached_result:
                    # Return the cached results
                    return cached_result

            # Search for notes in the database
            models: Optional[List[NoteModel]] = asyncio.run(
                NoteModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found notes if any
            if models is not None and len(models) > 0:
                return [
                    ImmutableNote(
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
                # Return None indicating that no notes were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_note(
        self,
        note: Union[ImmutableNote, MutableNote],
    ) -> Optional[ImmutableNote]:
        """
        Updates a note with the given ID.

        Args:
            note (Union[ImmutableNote, MutableNote]): The note to update.

        Returns:
            Optional[ImmutableNote]: The updated note if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the note to an immutable note and update the note in the database
            model: Optional[NoteModel] = asyncio.run(
                NoteConverter.object_to_model(
                    object=ImmutableNote(
                        **note.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).update(
                    database=Constants.DATABASE_PATH,
                    **note.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Return the updated note if it exists
            if model is not None:
                # Convert the NoteModel object to an ImmutableNote object
                note = ImmutableNote(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the note to the cache
                self.update_in_cache(
                    key=note.key,
                    value=note,
                )

                # Return the updated note
                return note
            else:
                # Return None indicating that the note does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class NoteModel(ImmutableBaseModel):
    """
    Represents the structure of a Note model.

    Attributes:
        body_text (Optional[str]): The body of the Note.
        created_at (Optional[datetime]): The timestamp when the Note was created.
        custom_field_values (Optional[List[Dict[str, Any]]]): The custom fields of the Note.
        difficulty (Optional[int]): The difficulty of the Note.
        due_by (Optional[datetime]): The due date of the Note.
        icon (Optional[str]): The icon of the Note. Defaults to "📝".
        id (Optional[int]): The ID of the Note.
        interval (Optional[float]): The review interval of the Note.
        key (Optional[str]): The key of the Note.
        last_viewed_at (Optional[datetime]): The timestamp when the Note was last viewed.
        metadata (Optional[Dict[str, Any]]): The metadata of the Note.
        priority (Optional[int]): The priority of the Note.
        status (Optional[int]): The status of the Note.
        tags (Optional[List[str]]): The tags associated with the Note.
        title_text (Optional[str]): The title of the Note.
        updated_at (Optional[datetime]): The timestamp when the Note was last updated.
        uuid (Optional[str]): The UUID of the Note.
    """

    table: Final[str] = Constants.NOTES

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

    body_text: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="body_text",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
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
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
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

    due_by: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="due_by",
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
        default="📝",
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

    interval: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="interval",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="FLOAT",
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

    last_viewed_at: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="last_viewed_at",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="DATETIME",
        unique=False,
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

    status: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.STATUSES}(id)",
        index=False,
        name="status",
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

    title_text: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="title_text",
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
        body_text: Optional[str] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        difficulty: Optional[int] = None,
        due_by: Optional[datetime] = None,
        icon: Optional[str] = "📝",
        id: Optional[int] = None,
        interval: Optional[float] = None,
        key: Optional[str] = None,
        last_viewed_at: Optional[datetime] = None,
        metadata: Optional[Dict[str, Any]] = None,
        priority: Optional[int] = None,
        status: Optional[int] = None,
        tags: Optional[List[str]] = None,
        title_text: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the NoteModel class.

        Args:
            body_text (Optional[str]): The body of the Note.
            created_at (Optional[datetime]): The timestamp when the Note was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): The custom fields of the Note.
            difficulty (Optional[int]): The difficulty of the Note.
            due_by (Optional[datetime]): The due date of the Note.
            icon (Optional[str]): The icon of the Note. Defaults to "📝".
            id (Optional[int]): The ID of the Note.
            interval (Optional[float]): The review interval of the Note.
            key (Optional[str]): The key of the Note.
            last_viewed_at (Optional[datetime]): The timestamp when the Note was last viewed.
            metadata (Optional[Dict[str, Any]]): The metadata of the Note.
            priority (Optional[int]): The priority of the Note.
            status (Optional[int]): The status of the Note.
            tags (Optional[List[str]]): The tags associated with the Note.
            title_text (Optional[str]): The title of the Note.
            updated_at (Optional[datetime]): The timestamp when the Note was last updated.
            uuid (Optional[str]): The UUID of the Note.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            body_text=body_text,
            created_at=created_at,
            custom_field_values=custom_field_values,
            difficulty=difficulty,
            due_by=due_by,
            icon="📝",
            id=id,
            interval=interval,
            key=key,
            last_viewed_at=last_viewed_at,
            metadata=metadata,
            priority=priority,
            status=status,
            table=Constants.NOTES,
            tags=tags,
            title_text=title_text,
            updated_at=updated_at,
            uuid=uuid,
        )
