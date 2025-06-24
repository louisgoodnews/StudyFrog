"""
Author: lodego
Date: 2025-02-05
"""

import asyncio
import traceback

from datetime import datetime

from typing import *

from core.difficulty import DifficultyManager, ImmutableDifficulty, MutableDifficulty
from core.priority import PriorityManager, ImmutablePriority, MutablePriority
from core.status import StatusManager, ImmutableStatus, MutableStatus

from utils.builder import BaseObjectBuilder
from utils.constants import Constants
from utils.field import Field
from utils.logger import Logger
from utils.manager import BaseObjectManager
from utils.miscellaneous import Miscellaneous
from utils.model import ImmutableBaseModel
from utils.object import MutableBaseObject, ImmutableBaseObject


__all__: Final[List[str]] = [
    "ImmutableFlashcard",
    "MutableFlashcard",
    "FlashcardConverter",
    "FlashcardFactory",
    "FlashcardBuilder",
    "FlashcardManager",
    "FlashcardModel",
    "Flashcards",
]


class ImmutableFlashcard(ImmutableBaseObject):
    """
    An immutable class representing a flashcard.

    A flashcard is a learning tool used to aid memorization by providing a question on one side and the answer on the other.

    Attributes:
        back_text (str): The back side of the flashcard.
        back_word_count (int): The word count of the back side of the flashcard.
        created_at (datetime): The timestamp when the flashcard was created.
        custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
        difficulty (int): The ID of the difficulty the flashcard is associated with.
        due_by (datetime): The timestamp when the flashcard is due.
        familiarity (float): The familiarity of the flashcard.
        front_text (str): The front side of the flashcard.
        front_word_count (int): The word count of the front side of the flashcard.
        icon (str): The icon of the flashcard.
        id (int): The ID of the flashcard.
        interval (Optional[int]): The repetition interval of the flashcard in days.
        key (str): The key of the flashcard.
        last_viewed_at (datetime): The timestamp when the flashcard was last viewed.
        metadata (Optional[Dict[str, Any]]): The metadata of the flashcard.
        priority (int): The ID of the priority the flashcard is associated with.
        status (int): The ID of the status the flashcard is associated with.
        tags (Optional[List[str]]): The keys of the tags associated with the flashcard.
        total_word_count (int): The word count of the flashcard.
        updated_at (datetime): The timestamp when the flashcard was last updated.
        uuid (str): The UUID of the flashcard.
    """

    def __init__(
        self,
        back_text: str,
        front_text: str,
        back_word_count: Optional[int] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        difficulty: Optional[int] = None,
        due_by: Optional[datetime] = None,
        familiarity: Optional[float] = None,
        front_word_count: Optional[int] = None,
        icon: Optional[str] = "📇",
        id: Optional[int] = None,
        interval: Optional[int] = None,
        key: Optional[str] = None,
        last_viewed_at: Optional[datetime] = None,
        metadata: Optional[Dict[str, Any]] = None,
        priority: Optional[int] = None,
        status: Optional[int] = None,
        tags: Optional[List[str]] = None,
        total_word_count: Optional[int] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableFlashcard class.

        Args:
            back_text (str): The back side of the flashcard.
            back_word_count (Optional[int]): The word count of the back side of the flashcard.
            created_at (Optional[datetime]): The timestamp when the flashcard was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
            difficulty (Optional[int]): The ID of the difficulty the flashcard is associated with.
            due_by (Optional[datetime]): The timestamp when the flashcard is due.
            familiarity (Optional[float]): The familiarity of the flashcard.
            front_text (str): The front side of the flashcard.
            front_word_count (Optional[int]): The word count of the front side of the flashcard.
            icon (Optional[str]): The icon of the flashcard. Defaults to "📇".
            id (Optional[int]): The ID of the flashcard.
            interval (Optional[int]): The repetition interval of the flashcard in days.
            key (Optional[str]): The key of the flashcard.
            last_viewed_at (Optional[datetime]): The timestamp when the flashcard was last viewed.
            metadata (Optional[Dict[str, Any]]): The metadata of the flashcard.
            priority (Optional[int]): The ID of the priority the flashcard is associated with.
            status (Optional[int]): The ID of the status the flashcard is associated with.
            tags (Optional[List[str]]): The keys of the tags associated with the flashcard.
            total_word_count (Optional[int]): The word count of the flashcard.
            updated_at (Optional[datetime]): The timestamp when the flashcard was last updated.
            uuid (Optional[str]): The UUID of the flashcard.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            back_text=back_text,
            back_word_count=back_word_count,
            created_at=created_at,
            custom_field_values=custom_field_values,
            difficulty=difficulty,
            due_by=due_by,
            familiarity=familiarity,
            front_text=front_text,
            front_word_count=front_word_count,
            hide_attributes=True,
            icon="📇",
            id=id,
            interval=interval,
            key=key,
            last_viewed_at=last_viewed_at,
            metadata=metadata,
            priority=priority,
            status=status,
            tags=tags,
            total_word_count=total_word_count,
            updated_at=updated_at,
            uuid=uuid,
        )

    @property
    def back_text(self) -> str:
        """
        Gets the back side of the flashcard.

        Returns:
            str: The back side of the flashcard.
        """
        return self._back_text

    @property
    def back_word_count(self) -> int:
        """
        Gets the word count of the back side of the flashcard.

        Returns:
            int: The word count of the back side of the flashcard.
        """
        return self._back_word_count

    @property
    def created_at(self) -> datetime:
        """
        Gets the timestamp when the flashcard was created.

        Returns:
            datetime: The timestamp when the flashcard was created.
        """
        return self._created_at

    @property
    def custom_field_values(self) -> List[Dict[str, Any]]:
        """
        Gets the custom field values of the flashcard.

        Returns:
            List[Dict[str, Any]]: The custom field values of the flashcard.
        """
        return self._custom_field_values

    @property
    def difficulty(self) -> int:
        """
        Gets the difficulty of the flashcard.

        Returns:
            int: The difficulty of the flashcard.
        """
        return self._difficulty

    @property
    def due_by(self) -> datetime:
        """
        Gets the due date of the flashcard.

        Returns:
            datetime: The due date of the flashcard.
        """
        return self._due_by

    @property
    def familiarity(self) -> float:
        """
        Gets the familiarity of the flashcard.

        Returns:
            float: The familiarity of the flashcard.
        """
        return self._familiarity

    @property
    def front_text(self) -> str:
        """
        Gets the front side of the flashcard.

        Returns:
            str: The front side of the flashcard.
        """
        return self._front_text

    @property
    def front_word_count(self) -> int:
        """
        Gets the word count of the front side of the flashcard.

        Returns:
            int: The word count of the front side of the flashcard.
        """
        return self._front_word_count

    @property
    def icon(self) -> str:
        """
        Gets the icon of the flashcard.

        Returns:
            str: The icon of the flashcard.
        """
        return self._icon

    @property
    def id(self) -> int:
        """
        Gets the ID of the flashcard.

        Returns:
            int: The ID of the flashcard.
        """
        return self._id

    @property
    def interval(self) -> int:
        """
        Gets the interval of the flashcard.

        Returns:
            int: The interval of the flashcard.
        """
        return self._interval

    @property
    def key(self) -> str:
        """
        Gets the key of the flashcard.

        Returns:
            str: The key of the flashcard.
        """
        return self._key

    @property
    def last_viewed_at(self) -> datetime:
        """
        Gets the timestamp when the flashcard was last viewed.

        Returns:
            datetime: The timestamp when the flashcard was last viewed.
        """
        return self._last_viewed_at

    @property
    def metadata(self) -> Dict[str, Any]:
        """
        Gets the metadata of the flashcard.

        Returns:
            Dict[str, Any]: The metadata of the flashcard.
        """
        return self._metadata

    @property
    def priority(self) -> int:
        """
        Gets the priority of the flashcard.

        Returns:
            int: The priority of the flashcard.
        """
        return self._priority

    @property
    def status(self) -> int:
        """
        Gets the status of the flashcard.

        Returns:
            int: The status of the flashcard.
        """
        return self._status

    @property
    def tags(self) -> List[str]:
        """
        Gets the tags of the flashcard.

        Returns:
            List[str]: The tags of the flashcard.
        """
        return self._tags

    @property
    def total_word_count(self) -> int:
        """
        Gets the total word count of the flashcard.

        Returns:
            int: The total word count of the flashcard.
        """
        return self._total_word_count

    @property
    def updated_at(self) -> datetime:
        """
        Gets the timestamp when the flashcard was last updated.

        Returns:
            datetime: The timestamp when the flashcard was last updated.
        """
        return self._updated_at

    @property
    def uuid(self) -> str:
        """
        Gets the UUID of the flashcard.

        Returns:
            str: The UUID of the flashcard.
        """
        return self._uuid

    def get_custom_field_value(
        self,
        custom_field_id: str,
    ) -> Optional[Any]:
        """
        Retrieves the value of a custom field by its ID.

        Args:
            custom_field_id (str): The ID of the custom field to retrieve.

        Returns:
            Optional[Any]: The value of the custom field if found, otherwise None.
        """
        try:
            # Iterate over the custom field values and return the value for the matching custom_field_id
            return next(
                item["value"]
                for item in self.custom_field_values
                if item["custom_field_id"] == custom_field_id
            )
        except StopIteration as e:
            # Log an error message to indicate that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_custom_field_value' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    def to_mutable(self) -> "MutableFlashcard":
        """
        Returns a mutable copy of the ImmutableFlashcard instance.

        Returns:
            MutableFlashcard: A mutable copy of the ImmutableFlashcard instance.
        """
        try:
            # Create a new MutableFlashcard instance from the dictionary representation of the ImmutableFlashcard instance
            return MutableFlashcard(
                **self.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message to indicate that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_mutable' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None


class MutableFlashcard(MutableBaseObject):
    """
    A mutable class representing a flashcard.

    A flashcard is a learning tool used to aid memorization by providing a question on one side and the answer on the other.

    Attributes:
        back_text (str): The back side of the flashcard.
        back_word_count (int): The word count of the back side of the flashcard.
        created_at (datetime): The timestamp when the flashcard was created.
        custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
        difficulty (int): The ID of the difficulty the flashcard is associated with.
        due_by (datetime): The timestamp when the flashcard is due.
        familiarity (float): The familiarity of the flashcard.
        front_text (str): The front side of the flashcard.
        front_word_count (int): The word count of the front side of the flashcard.
        icon (str): The icon of the flashcard.
        id (int): The ID of the flashcard.
        interval (Optional[int]): The repetition interval of the flashcard in days.
        key (str): The key of the flashcard.
        last_viewed_at (datetime): The timestamp when the flashcard was last viewed.
        metadata (Optional[Dict[str, Any]]): The metadata of the flashcard.
        priority (int): The ID of the priority the flashcard is associated with.
        status (int): The ID of the status the flashcard is associated with.
        tags (Optional[List[str]]): The keys of the tags associated with the flashcard.
        total_word_count (int): The word count of the back side of the flashcard.
        updated_at (datetime): The timestamp when the flashcard was last updated.
        uuid (str): The UUID of the flashcard.
    """

    def __init__(
        self,
        back_text: str,
        front_text: str,
        back_word_count: Optional[int] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        difficulty: Optional[int] = None,
        due_by: Optional[datetime] = None,
        familiarity: Optional[float] = None,
        front_word_count: Optional[int] = None,
        icon: Optional[str] = "📇",
        id: Optional[int] = None,
        interval: Optional[int] = None,
        key: Optional[str] = None,
        last_viewed_at: Optional[datetime] = None,
        metadata: Optional[Dict[str, Any]] = None,
        priority: Optional[int] = None,
        status: Optional[int] = None,
        tags: Optional[List[str]] = None,
        total_word_count: Optional[int] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableFlashcard class.

        Args:
            back_text (str): The back side of the flashcard.
            back_word_count (Optional[int]): The word count of the back side of the flashcard.
            created_at (Optional[datetime]): The timestamp when the flashcard was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
            difficulty (Optional[int]): The ID of the difficulty the flashcard is associated with.
            due_by (Optional[datetime]): The timestamp when the flashcard is due.
            familiarity (Optional[float]): The familiarity of the flashcard.
            front_text (str): The front side of the flashcard.
            front_word_count (Optional[int]): The word count of the front side of the flashcard.
            icon (Optional[str]): The icon of the flashcard. Defaults to "📇".
            id (Optional[int]): The ID of the flashcard.
            interval (Optional[int]): The repetition interval of the flashcard in days.
            key (Optional[str]): The key of the flashcard.
            last_viewed_at (Optional[datetime]): The timestamp when the flashcard was last viewed.
            metadata (Optional[Dict[str, Any]]): The metadata of the flashcard.
            priority (Optional[int]): The ID of the priority the flashcard is associated with.
            status (Optional[int]): The ID of the status the flashcard is associated with.
            tags (Optional[List[str]]): The keys of the tags associated with the flashcard.
            total_word_count (Optional[int]): The word count of the flashcard.
            updated_at (Optional[datetime]): The timestamp when the flashcard was last updated.
            uuid (Optional[str]): The UUID of the flashcard.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            back_text=back_text,
            back_word_count=back_word_count,
            created_at=created_at,
            custom_field_values=custom_field_values,
            difficulty=difficulty,
            due_by=due_by,
            familiarity=familiarity,
            front_text=front_text,
            front_word_count=front_word_count,
            hide_attributes=True,
            icon="📇",
            id=id,
            interval=interval,
            key=key,
            last_viewed_at=last_viewed_at,
            metadata=metadata,
            priority=priority,
            status=status,
            tags=tags,
            total_word_count=total_word_count,
            updated_at=updated_at,
            uuid=uuid,
        )

    @property
    def back_text(self) -> str:
        """
        Gets the back side of the flashcard.

        Returns:
            str: The back side of the flashcard.
        """
        return self._back_text

    @back_text.setter
    def back_text(
        self,
        value: str,
    ) -> None:
        """
        Sets the back side of the flashcard.

        Args:
            value (str): The new back side of the flashcard.

        Returns:
            None
        """
        self._back_text = value

    @property
    def back_word_count(self) -> int:
        """
        Gets the word count of the back side of the flashcard.

        Returns:
            int: The word count of the back side of the flashcard.
        """
        return self._back_word_count

    @back_word_count.setter
    def back_word_count(
        self,
        value: int,
    ) -> None:
        """
        Sets the word count of the back side of the flashcard.

        Args:
            value (int): The new word count of the back side of the flashcard.

        Returns:
            None
        """
        self._back_word_count = value

    @property
    def created_at(self) -> datetime:
        """
        Gets the timestamp when the flashcard was created.

        Returns:
            datetime: The timestamp when the flashcard was created.
        """
        return self._created_at

    @created_at.setter
    def created_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the timestamp when the flashcard was created.

        Args:
            value (datetime): The new timestamp when the flashcard was created.

        Returns:
            None
        """
        self._created_at = value

    @property
    def custom_field_values(self) -> List[Dict[str, Any]]:
        """
        Gets the custom field values of the flashcard.

        Returns:
            List[Dict[str, Any]]: The custom field values of the flashcard.
        """
        return self._custom_field_values

    @custom_field_values.setter
    def custom_field_values(
        self,
        value: Union[Dict[str, Any], List[Dict[str, Any]]],
    ) -> None:
        """
        Sets the custom field values of the flashcard.

        Args:
            value (Union[Dict[str, Any], List[Dict[str, Any]]): The new custom field values of the flashcard.

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
        Gets the difficulty of the flashcard.

        Returns:
            int: The difficulty of the flashcard.
        """
        return self._difficulty

    @difficulty.setter
    def difficulty(
        self,
        value: int,
    ) -> None:
        """
        Sets the difficulty of the flashcard.

        Args:
            value (int): The new difficulty of the flashcard.

        Returns:
            None
        """
        self._difficulty = value

    @property
    def due_by(self) -> datetime:
        """
        Gets the due date of the flashcard.

        Returns:
            datetime: The due date of the flashcard.
        """
        return self._due_by

    @due_by.setter
    def due_by(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the due date of the flashcard.

        Args:
            value (datetime): The new due date of the flashcard.

        Returns:
            None
        """
        self._due_by = value

    @property
    def familiarity(self) -> float:
        """
        Gets the familiarity of the flashcard.

        Returns:
            float: The familiarity of the flashcard.
        """
        return self._familiarity

    @familiarity.setter
    def familiarity(
        self,
        value: float,
    ) -> None:
        """
        Sets the familiarity of the flashcard.

        Args:
            value (float): The new familiarity of the flashcard.

        Returns:
            None
        """
        self._familiarity = value

    @property
    def front_text(self) -> str:
        """
        Gets the front side of the flashcard.

        Returns:
            str: The front side of the flashcard.
        """
        return self._front_text

    @front_text.setter
    def front_text(
        self,
        value: str,
    ) -> None:
        """
        Sets the front side of the flashcard.

        Args:
            value (str): The new front side of the flashcard.

        Returns:
            None
        """
        self._front_text = value

    @property
    def front_word_count(self) -> int:
        """
        Gets the word count of the front side of the flashcard.

        Returns:
            int: The word count of the front side of the flashcard.
        """
        return self._front_word_count

    @front_word_count.setter
    def front_word_count(
        self,
        value: int,
    ) -> None:
        """
        Sets the word count of the front side of the flashcard.

        Args:
            value (int): The new word count of the front side of the flashcard.

        Returns:
            None
        """
        self._front_word_count = value

    @property
    def icon(self) -> str:
        """
        Gets the icon of the flashcard.

        Returns:
            str: The icon of the flashcard.
        """
        return self._icon

    @icon.setter
    def icon(
        self,
        value: str,
    ) -> None:
        """
        Sets the icon of the flashcard.

        Args:
            value (str): The new icon of the flashcard.

        Returns:
            None
        """
        self._icon = value

    @property
    def id(self) -> int:
        """
        Gets the ID of the flashcard.

        Returns:
            int: The ID of the flashcard.
        """
        return self._id

    @id.setter
    def id(
        self,
        value: int,
    ) -> None:
        """
        Sets the ID of the flashcard.

        Args:
            value (int): The new ID of the flashcard.

        Returns:
            None
        """
        self._id = value

    @property
    def interval(self) -> int:
        """
        Gets the interval of the flashcard.

        Returns:
            int: The interval of the flashcard.
        """
        return self._interval

    @interval.setter
    def interval(
        self,
        value: int,
    ) -> None:
        """
        Sets the interval of the flashcard.

        Args:
            value (int): The new interval of the flashcard.

        Returns:
            None
        """
        self._interval = value

    @property
    def key(self) -> str:
        """
        Gets the key of the flashcard.

        Returns:
            str: The key of the flashcard.
        """
        return self._key

    @key.setter
    def key(
        self,
        value: str,
    ) -> None:
        """
        Sets the key of the flashcard.

        Args:
            value (str): The new key of the flashcard.

        Returns:
            None
        """
        self._key = value

    @property
    def last_viewed_at(self) -> datetime:
        """
        Gets the timestamp when the flashcard was last viewed.

        Returns:
            datetime: The timestamp when the flashcard was last viewed.
        """
        return self._last_viewed_at

    @last_viewed_at.setter
    def last_viewed_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the timestamp when the flashcard was last viewed.

        Args:
            value (datetime): The new timestamp when the flashcard was last viewed.

        Returns:
            None
        """
        self._last_viewed_at = value

    @property
    def metadata(self) -> Dict[str, Any]:
        """
        Gets the metadata of the flashcard.

        Returns:
            Dict[str, Any]: The metadata of the flashcard.
        """
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
            # Set the metadata of the flashcard to an empty dictionary
            self._metadata = {}

        # Update the metadata of the flashcard
        self._metadata.update(**kwargs)

    @property
    def priority(self) -> int:
        """
        Gets the priority of the flashcard.

        Returns:
            int: The priority of the flashcard.
        """
        return self._priority

    @priority.setter
    def priority(
        self,
        value: int,
    ) -> None:
        """
        Sets the priority of the flashcard.

        Args:
            value (int): The new priority of the flashcard.

        Returns:
            None
        """
        self._priority = value

    @property
    def status(self) -> int:
        """
        Gets the status of the flashcard.

        Returns:
            int: The status of the flashcard.
        """
        return self._status

    @status.setter
    def status(
        self,
        value: int,
    ) -> None:
        """
        Sets the status of the flashcard.

        Args:
            value (int): The new status of the flashcard.

        Returns:
            None
        """
        self._status = value

    @property
    def tags(self) -> List[str]:
        """
        Gets the tags of the flashcard.

        Returns:
            List[str]: The tags of the flashcard.
        """
        return self._tags

    @tags.setter
    def tags(
        self,
        value: Union[List[str], str],
    ) -> None:
        """
        Sets the tags of the flashcard.

        Args:
            value (Union[List[str], str]): The new tags of the flashcard.

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
    def total_word_count(self) -> int:
        """
        Gets the total word count of the flashcard.

        Returns:
            int: The total word count of the flashcard.
        """
        return self._total_word_count

    @total_word_count.setter
    def total_word_count(
        self,
        value: int,
    ) -> None:
        """
        Sets the total word count of the flashcard.

        Args:
            value (int): The new total word count of the flashcard.

        Returns:
            None
        """
        self._total_word_count = value

    @property
    def updated_at(self) -> datetime:
        """
        Gets the timestamp when the flashcard was last updated.

        Returns:
            datetime: The timestamp when the flashcard was last updated.
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the timestamp when the flashcard was last updated.

        Args:
            value (datetime): The new timestamp when the flashcard was last updated.

        Returns:
            None
        """
        self._updated_at = value

    @property
    def uuid(self) -> str:
        """
        Gets the UUID of the flashcard.

        Returns:
            str: The UUID of the flashcard.
        """
        return self._uuid

    @uuid.setter
    def uuid(
        self,
        value: str,
    ) -> None:
        """
        Sets the UUID of the flashcard.

        Args:
            value (str): The new UUID of the flashcard.

        Returns:
            None
        """
        self._uuid = value

    def get_custom_field_value(
        self,
        custom_field_id: str,
    ) -> Optional[Any]:
        """
        Retrieves the value of a custom field by its ID.

        Args:
            custom_field_id (str): The ID of the custom field to retrieve.

        Returns:
            Optional[Any]: The value of the custom field if found, otherwise None.
        """
        try:
            # Iterate over the custom field values and return the value for the matching custom_field_id
            return next(
                item["value"]
                for item in self.custom_field_values
                if item["custom_field_id"] == custom_field_id
            )
        except StopIteration as e:
            # Log an error message to indicate that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_custom_field_value' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    def remove_custom_field_value(
        self,
        custom_field_id: str,
    ) -> None:
        """
        Removes a custom field value by its ID.

        Args:
            custom_field_id (str): The ID of the custom field to remove.

        Returns:
            None
        """
        try:
            # Iterate over the custom field values and remove the value for the matching custom_field_id
            self.custom_field_values = [
                item
                for item in self.custom_field_values
                if item["custom_field_id"] != custom_field_id
            ]

            # Return indicating success
            return
        except Exception as e:
            # Log an error message to indicate that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'remove_custom_field_value' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return indicating an error has occurred
            return

    def set_custom_field_value(
        self,
        custom_field_id: str,
        value: Any,
    ) -> None:
        """
        Sets the value of a custom field by its ID.

        Args:
            custom_field_id (str): The ID of the custom field to set.
            value (Any): The value to set for the custom field.

        Returns:
            None
        """
        try:
            # Get the custom field value by its ID
            entry: Optional[Dict[str, Any]] = next(
                (
                    item
                    for item in self.custom_field_values
                    if item["custom_field_id"] == custom_field_id
                ),
                None,
            )

            # Check, if the item is None
            if entry is None:
                # Append the new custom field value to the list
                self.custom_field_values.append(
                    {
                        "custom_field_id": custom_field_id,
                        "value": value,
                    }
                )

                # Return early
                return

            # Update the value of the custom field
            entry["value"] = value

            # Return indicating success
            return
        except Exception as e:
            # Log an error message to indicate that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'set_custom_field_value' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return indicating an error has occurred
            return

    def set_difficulty(
        self,
        difficulty: Union[
            ImmutableDifficulty,
            MutableDifficulty,
        ],
    ) -> None:
        """
        Sets the difficulty of the flashcard.

        Args:
            difficulty (Union[ImmutableDifficulty, MutableDifficulty]): The difficulty of the flashcard.

        Returns:
            None
        """

        # Set the difficulty of the flashcard
        self.difficulty = difficulty.id

    def set_priority(
        self,
        priority: Union[
            ImmutablePriority,
            MutablePriority,
        ],
    ) -> None:
        """
        Sets the priority of the flashcard.

        Args:
            priority (Union[ImmutablePriority, MutablePriority]): The priority of the flashcard.

        Returns:
            None
        """

        # Set the priority of the flashcard
        self.priority = priority.id

    def to_immutable(self) -> ImmutableFlashcard:
        """
        Returns an immutable copy of the MutableFlashcard instance.

        Returns:
            ImmutableFlashcard: An immutable copy of the MutableFlashcard instance.
        """
        try:
            # Create a new ImmutableFlashcard instance from the dictionary representation of the MutableFlashcard instance
            return ImmutableFlashcard(
                **self.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message to indicate that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_immutable' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None


class FlashcardConverter:
    """
    A converter class for transforming between FlashcardModel and ImmutableFlashcard instances.

    This class provides methods to convert a FlashcardModel instance to an ImmutableFlashcard instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the FlashcardConverter class.
    """

    logger: Final[Logger] = Logger.get_logger(name="FlashcardConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "FlashcardModel",
    ) -> Optional[ImmutableFlashcard]:
        """
        Converts a given FlashcardModel instance to an ImmutableFlashcard instance.

        Args:
            model (FlashcardModel): The FlashcardModel instance to be converted.

        Returns:
            ImmutableFlashcard: The converted ImmutableFlashcard instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the FlashcardModel instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableFlashcard class from the dictionary representation of the FlashcardModel instance
            return ImmutableFlashcard(
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
        object: ImmutableFlashcard,
    ) -> Optional["FlashcardModel"]:
        """
        Converts a given ImmutableFlashcard instance to a FlashcardModel instance.

        Args:
            object (ImmutableFlashcard): The ImmutableFlashcard instance to be converted.

        Returns:
            FlashcardModel: The converted FlashcardModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ImmutableFlashcard instance.
        """
        try:
            # Attempt to create and return a new instance of the FlashcardModel class from the dictionary representation of the ImmutableFlashcard instance
            return FlashcardModel(
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


class FlashcardFactory:
    """
    A factory class used to create instances of ImmutableFlashcard class.

    Attributes:
        logger (Logger): The logger instance associated with the object.
    """

    logger: Final[Logger] = Logger.get_logger(name="FlashcardFactory")

    @classmethod
    def create_flashcard(
        cls,
        back_text: str,
        front_text: str,
        back_word_count: Optional[int] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        difficulty: Optional[int] = None,
        due_by: Optional[datetime] = None,
        familiarity: Optional[float] = None,
        front_word_count: Optional[int] = None,
        icon: Optional[str] = "📇",
        id: Optional[int] = None,
        interval: Optional[int] = None,
        key: Optional[str] = None,
        last_viewed_at: Optional[datetime] = None,
        metadata: Optional[Dict[str, Any]] = None,
        priority: Optional[int] = None,
        status: Optional[int] = None,
        tags: Optional[List[str]] = None,
        total_word_count: Optional[int] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutableFlashcard]:
        """
        Creates and returns a new instance of ImmutableFlashcard class.

        Args:
            back_text (str): The back side of the flashcard.
            back_word_count (Optional[int]): The word count of the back side of the flashcard.
            created_at (Optional[datetime]): The timestamp when the flashcard was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
            difficulty (Optional[int]): The ID of the difficulty the flashcard is associated with.
            due_by (Optional[datetime]): The timestamp when the flashcard is due.
            familiarity (Optional[float]): The familiarity of the flashcard.
            front_text (str): The front side of the flashcard.
            front_word_count (Optional[int]): The word count of the front side of the flashcard.
            icon (Optional[str]): The icon of the flashcard. Defaults to "📇".
            id (Optional[int]): The ID of the flashcard.
            interval (Optional[int]): The repetition interval of the flashcard in days.
            key (Optional[str]): The key of the flashcard.
            last_viewed_at (Optional[datetime]): The timestamp when the flashcard was last viewed.
            metadata (Optional[Dict[str, Any]]): The metadata of the flashcard.
            priority (Optional[int]): The ID of the priority the flashcard is associated with.
            status (Optional[int]): The ID of the status the flashcard is associated with.
            tags (Optional[List[str]]): The keys of the tags associated with the flashcard.
            total_word_count (Optional[int]): The word count of the flashcard.
            updated_at (Optional[datetime]): The timestamp when the flashcard was last updated.
            uuid (Optional[str]): The UUID of the flashcard.

        Returns:
            Optional[ImmutableFlashcard]: The created flashcard object if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the flashcard.
        """
        try:
            # Attempt to create and return an ImmutableFlashcard object
            return ImmutableFlashcard(
                back_text=back_text,
                back_word_count=back_word_count,
                created_at=created_at,
                custom_field_values=custom_field_values,
                difficulty=difficulty,
                due_by=due_by,
                familiarity=familiarity,
                front_text=front_text,
                front_word_count=front_word_count,
                id=id,
                icon=icon,
                interval=interval,
                key=key,
                last_viewed_at=last_viewed_at,
                metadata=metadata,
                priority=priority,
                status=status,
                tags=tags,
                total_word_count=total_word_count,
                updated_at=updated_at,
                uuid=uuid,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_flashcard' method from '{cls.__name__}': {e}"
            )

            # Log the traceback of the exception
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def create_default_flashcard(
        cls,
        back_text: str,
        front_text: str,
        as_mutable: bool = False,
    ) -> Optional[ImmutableFlashcard]:
        """
        Creates and returns a new instance of ImmutableFlashcard class.

        This method creates a new flashcard with default values.

        Args:
            back_text (str): The back side of the flashcard.
            front_text (str): The front side of the flashcard.
            as_mutable (bool): Whether to return the flashcard as a MutableFlashcard object. Defaults to False.

        Returns:
            Optional[ImmutableFlashcard]: The created flashcard object if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the flashcard.
        """
        try:
            # Attempt to obtain the 'Medium' difficulty from the database
            difficulty: Optional[
                ImmutableDifficulty
            ] = DifficultyManager().get_difficulty_by(
                field="name",
                value=Constants.MEDIUM,
            )

            # Check, if the difficulty was found
            if not difficulty:
                # Log a warning message
                cls.logger.warning(
                    message=f"Difficulty '{Constants.MEDIUM}' not found. Aborting..."
                )

                # Return None indicating an exception has occurred
                return None

            # Attempt to obtain the 'Medium' priority from the database
            priority: Optional[ImmutablePriority] = PriorityManager().get_priority_by(
                field="name",
                value=Constants.MEDIUM,
            )

            # Check, if the priority was found
            if not priority:
                # Log a warning message
                cls.logger.warning(
                    message=f"Priority '{Constants.MEDIUM}' not found. Aborting..."
                )

                # Return None indicating an exception has occurred
                return None

            # Attempt to get the 'New' status
            status: Optional[ImmutableStatus] = StatusManager().get_status_by(
                field="name",
                value=Constants.NEW,
            )

            # Check, if the status was found
            if not status:
                # Log a warning message
                cls.logger.warning(
                    message=f"Status '{Constants.NEW}' not found. Aborting..."
                )

                # Return None indicating an exception has occurred
                return None

            # Attempt to create an ImmutableFlashcard object
            flashcard: Optional[ImmutableFlashcard] = cls.create_flashcard(
                back_text=back_text,
                back_word_count=len(back_text.split(" ")),
                front_text=front_text,
                front_word_count=len(front_text.split(" ")),
                difficulty=difficulty.id,
                metadata={"created_by": "FlashcardFactory"},
                priority=priority.id,
                status=status.id,
                total_word_count=len(back_text.split(" ")) + len(front_text.split(" ")),
            )

            # Check, if the flashcard was created
            if not flashcard:
                # Log a warning message
                cls.logger.warning(message="Flashcard not created. Aborting...")

                # Return None indicating an exception has occurred
                return None

            # Check, if the 'as_mutable' flag is set
            if as_mutable:
                # Return the flashcard as a MutableFlashcard object
                return flashcard.to_mutable()

            # Return the flashcard
            return flashcard
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_default_flashcard' method from '{cls.__name__}': {e}"
            )

            # Log the traceback of the exception
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None


class FlashcardBuilder(BaseObjectBuilder):
    """
    A builder class for creating instances of ImmutableFlashcard class.

    Attributes:
        configuration (Dict[str, Any]): The dictionary containing the configuration of the object to be built.
        logger (Logger): The logger instance associated with the object.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the FlashcardBuilder class.

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
            ImmutableFlashcard,
            MutableFlashcard,
        ]
    ]:
        """
        Builds an instance of the ImmutableFlashcard or MutableFlashcard class using the configuration dictionary.

        This method is responsible for creating an instance of the ImmutableFlashcard or MutableFlashcard class based on the configuration dictionary
        passed to the constructor. If an exception occurs while creating the instance, this method will log an error message
        and return None.

        Args:
            as_mutable (bool): A flag indicating whether the flashcard should be mutable.

        Returns:
            Optional[Union[ImmutableFlashcard, MutableFlashcard]]: An instance of the ImmutableFlashcard or MutableFlashcard class if no exception occurs. Otherwise, None.
        """

        try:
            # Attempt to create an instance of the ImmutableFlashcard class using the configuration dictionary
            flashcard: Optional[ImmutableFlashcard] = FlashcardFactory.create_flashcard(
                **self.configuration
            )

            if not flashcard:
                # Log a warning message indicating an exception has occurred
                self.logger.warning(
                    message=f"Failed to build an instance of the ImmutableFlashcard or MutableFlashcard class from '{self.__class__.__name__}'"
                )

                # Raise an exception
                raise Exception(
                    f"Failed to build an instance of the ImmutableFlashcard or MutableFlashcard class from '{self.__class__.__name__}'"
                )

            # Check if the flashcard should be mutable
            if as_mutable:
                # Return a mutable copy of the flashcard
                return flashcard.to_mutable()

            # Return the instance of the ImmutableFlashcard class
            return flashcard
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'build' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def back_text(
        self,
        value: str,
    ) -> Self:
        """
        Sets the back text of the flashcard.

        Args:
            value (str): The back text of the flashcard.

        Returns:
            Self: The builder instance.
        """

        # Set the back_text value in the configuration dictionary
        self.configuration["back_text"] = value

        # Set the back_text wordcount
        self.back_text_wordcount(value=len(value.split(" ")))

        # Set the total wordcount
        self.total_wordcount(
            value=self.configuration.get(
                "front_word_count",
                0,
            )
            + self.configuration.get(
                "back_word_count",
                0,
            )
        )

        # Return the builder instance
        return self

    def back_word_count(
        self,
        value: int,
    ) -> Self:
        """
        Sets the back wordcount of the flashcard.

        Args:
            value (int): The back wordcount of the flashcard.

        Returns:
            Self: The builder instance.
        """

        # Set the back_word_count value in the configuration dictionary
        self.configuration["back_word_count"] = value

        # Return the builder instance
        return self

    def custom_field_values(
        self,
        value: Optional[List[Dict[str, Any]]] = None,
    ) -> Self:
        """
        Sets the custom field values of the flashcard.

        Args:
            value (Optional[List[Dict[str, Any]]]): The custom field values of the flashcard.

        Returns:
            Self: The builder instance.
        """

        # Set the custom_field_values value in the configuration dictionary
        self.configuration["custom_field_values"] = value

        # Return the builder instance
        return self

    def difficulty(
        self,
        value: Optional[int] = None,
    ) -> Self:
        """
        Sets the difficulty of the flashcard.

        Args:
            value (Optional[int]): The difficulty of the flashcard.

        Returns:
            Self: The builder instance.
        """

        # Set the difficulty value in the configuration dictionary
        self.configuration["difficulty"] = value

        # Return the builder instance
        return self

    def due_by(
        self,
        value: Optional[datetime] = None,
    ) -> Self:
        """
        Sets the due by of the flashcard.

        Args:
            value (Optional[datetime]): The due by of the flashcard.

        Returns:
            Self: The builder instance.
        """

        # Set the due_by value in the configuration dictionary
        self.configuration["due_by"] = value

        # Return the builder instance
        return self

    def familiarity(
        self,
        value: Optional[float] = None,
    ) -> Self:
        """
        Sets the familiarity of the flashcard.

        Args:
            value (Optional[float]): The familiarity of the flashcard.

        Returns:
            Self: The builder instance.
        """

        # Set the familiarity value in the configuration dictionary
        self.configuration["familiarity"] = value

        # Return the builder instance
        return self

    def front_text(
        self,
        value: str,
    ) -> Self:
        """
        Sets the front text of the flashcard.

        Args:
            value (str): The front text of the flashcard.

        Returns:
            Self: The builder instance.
        """

        # Set the front_text value in the configuration dictionary
        self.configuration["front_text"] = value

        # Set the front_text wordcount
        self.front_text_wordcount(value=len(value.split(" ")))

        # Set the total wordcount
        self.total_wordcount(
            value=self.configuration.get(
                "front_word_count",
                0,
            )
            + self.configuration.get(
                "back_word_count",
                0,
            )
        )

        # Return the builder instance
        return self

    def front_word_count(
        self,
        value: int,
    ) -> Self:
        """
        Sets the front wordcount of the flashcard.

        Args:
            value (int): The front wordcount of the flashcard.

        Returns:
            Self: The builder instance.
        """

        # Set the front_word_count value in the configuration dictionary
        self.configuration["front_word_count"] = value

        # Return the builder instance
        return self

    def interval(
        self,
        value: Optional[int] = None,
    ) -> Self:
        """
        Sets the interval of the flashcard.

        Args:
            value (Optional[int]): The interval of the flashcard.

        Returns:
            Self: The builder instance.
        """

        # Set the interval value in the configuration dictionary
        self.configuration["interval"] = value

        # Return the builder instance
        return self

    def last_viewed_at(
        self,
        value: Optional[datetime] = None,
    ) -> Self:
        """
        Sets the last viewed at of the flashcard.

        Args:
            value (Optional[datetime]): The last viewed at of the flashcard.

        Returns:
            Self: The builder instance.
        """

        # Set the last_viewed_at value in the configuration dictionary
        self.configuration["last_viewed_at"] = value

        # Return the builder instance
        return self

    def metadata(
        self,
        value: Dict[str, Any],
    ) -> Self:
        """
        Sets the metadata of the flashcard.

        Args:
            value (Dict[str, Any]): The metadata of the flashcard.

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
        value: Optional[int] = None,
    ) -> Self:
        """
        Sets the priority of the flashcard.

        Args:
            value (Optional[int]): The priority of the flashcard.

        Returns:
            Self: The builder instance.
        """

        # Set the priority value in the configuration dictionary
        self.configuration["priority"] = value

        # Return the builder instance
        return self

    def status(
        self,
        value: Optional[int] = None,
    ) -> Self:
        """
        Sets the status of the flashcard.

        Args:
            value (Optional[int]): The status of the flashcard.

        Returns:
            Self: The builder instance.
        """

        # Set the status value in the configuration dictionary
        self.configuration["status"] = value

        # Return the builder instance
        return self

    def tags(
        self,
        value: Optional[List[str]] = None,
    ) -> Self:
        """
        Sets the tags of the flashcard.

        Args:
            value (Optional[List[str]]): The tags of the flashcard.

        Returns:
            Self: The builder instance.
        """

        # Set the tags value in the configuration dictionary
        self.configuration["tags"] = value

        # Return the builder instance
        return self

    def total_word_count(
        self,
        value: int,
    ) -> Self:
        """
        Sets the total wordcount of the flashcard.

        Args:
            value (int): The total wordcount of the flashcard.

        Returns:
            Self: The builder instance.
        """

        # Set the total_word_count value in the configuration dictionary
        self.configuration["total_word_count"] = value

        # Return the builder instance
        return self


class FlashcardManager(BaseObjectManager):
    """
    A manager class for managing flashcards in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for flashcards.

    Attributes:
        cache: (List[Any]): The cache for storing flashcards.
        logger (Logger): The logger instance associated with the object.
    """

    _shared_instance: Optional["FlashcardManager"] = None

    def __new__(cls) -> "FlashcardManager":
        """
        Creates and returns a new instance of the FlashcardManager class.

        If the instance does not exist, creates a new one by calling the parent class
        constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Returns:
            FlashcardManager: The created or existing instance of FlashcardManager class.
        """

        # Check if the shared instance does not exist
        if cls._shared_instance is None:
            # Create a new instance by calling the parent class constructor
            cls._shared_instance = super(FlashcardManager, cls).__new__(cls)
            # Initialize the instance
            cls._shared_instance.init()

        # Return the shared instance
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes a new instance of the FlashcardManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def _run_pre_create_tasks(
        self,
        flashcard: Union[
            ImmutableFlashcard,
            MutableFlashcard,
        ],
    ) -> MutableFlashcard:
        """
        Runs pre-create tasks for the flashcard.

        Args:
            flashcard (Union[ImmutableFlashcard, MutableFlashcard]): The flashcard to run pre-create tasks on.

        Returns:
            MutableFlashcard: The flashcard with pre-create tasks run.
        """

        # Check if the flashcard object is immutable
        if not flashcard.is_mutable():
            # If it is, convert it to a mutable flashcard
            flashcard = flashcard.to_mutable()

        # Set the created_at timestamp of the flashcard
        flashcard.created_at = Miscellaneous.get_current_datetime()

        # Set the custom_field_values of the flashcard
        flashcard.custom_field_values = flashcard.custom_field_values or []

        # Set the due_by timestamp of the flashcard
        flashcard.due_by = flashcard.due_by or Miscellaneous.get_date_increment(
            days=flashcard.interval or Constants.BASE_REPETITION_INTERVAL_DAYS
        )

        # Set the familiarity of the flashcard
        flashcard.familiarity = flashcard.familiarity or 0.0

        # Set the repetition interval (in days) of the flashcard
        flashcard.interval = (
            flashcard.interval or Constants.BASE_REPETITION_INTERVAL_DAYS
        )

        # Set the key of the flashcard
        flashcard.key = f"FLASHCARD_{self.count_flashcards() + 1}"

        # Set the metadata of the flashcard
        flashcard.metadata = flashcard.metadata or {}

        # Set the tags of the flashcard
        flashcard.tags = flashcard.tags or []

        # Set the updated_at timestamp of the flashcard
        flashcard.updated_at = Miscellaneous.get_current_datetime()

        # Set the uuid of the flashcard
        flashcard.uuid = Miscellaneous.get_uuid()

        # Return the flashcard to the caller
        return flashcard

    def count_flashcards(self) -> int:
        """
        Returns the number of flashcards in the database.

        Returns:
            int: The number of flashcards in the database.
        """
        try:
            # Count and return the number of flashcards in the database
            return asyncio.run(FlashcardModel.count(database=Constants.DATABASE_PATH))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_flashcard(
        self,
        flashcard: Union[ImmutableFlashcard, MutableFlashcard],
    ) -> Optional[ImmutableFlashcard]:
        """
        Creates a new flashcard in the database.

        Args:
            flashcard (Union[ImmutableFlashcard, MutableFlashcard]): The flashcard to be created.

        Returns:
            Optional[ImmutableFlashcard]: The newly created immutable flashcard if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the flashcard.
        """
        try:
            # Initialize the result (optional) ImmutableFlashcard to none
            result: Optional[ImmutableFlashcard] = None

            # Run pre-create tasks
            flashcard: MutableFlashcard = self._run_pre_create_tasks(
                flashcard=flashcard
            )

            # Convert the flashcard object to a FlashcardModel object
            model: FlashcardModel = FlashcardConverter.object_to_model(object=flashcard)

            # Create a new flashcard in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            # Check, if the ID is not None
            if not id:
                # Log a warning message indicating an error has occurred
                self.logger.warning(
                    message=f"It seems that an error has occured while attempting to create a flashcard ({flashcard.__repr__()}) in the database."
                )

                # Return early
                return

            # Convert the flashcard to a dictionary
            kwargs: Dict[str, Any] = flashcard.to_dict(
                exclude=[
                    "_logger",
                ]
            )

            # Set the ID of the flashcard
            kwargs["id"] = id

            # Create a new ImmutableFlashcard object
            result = FlashcardFactory.create_flashcard(**kwargs)

            # Check, if the result is not None
            if not result:
                # Log an error message indicating an error has occurred
                self.logger.error(
                    message=f"It seems that there was an error while attempting to create an ImmutableFlashcard from the dictionary ({kwargs}) returned by the database. This is likely a serious issue."
                )

                # Return early
                return

            # Add the flashcard to the cache
            self.add_to_cache(
                key=result.key,
                value=result,
            )

            # Return the newly created ImmutableFlashcard instance
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_flashcard' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete_flashcard(
        self,
        flashcard: Union[ImmutableFlashcard, MutableFlashcard],
    ) -> bool:
        """
        Deletes a flashcard from the database.

        Args:
            flashcard (Union[ImmutableFlashcard, MutableFlashcard]): The flashcard to be deleted.

        Returns:
            bool: True if the flashcard was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the flashcard to an immutable flashcard and delete the flashcard from the database
            result: bool = asyncio.run(
                FlashcardConverter.object_to_model(
                    object=FlashcardFactory.create_flashcard(
                        **flashcard.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).delete()
            )

            # Remove the flashcard from the cache
            self.remove_from_cache(key=flashcard.key)

            # Return True if the flashcard was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all_flashcards(
        self,
        force_refetch: bool = False,
    ) -> Optional[List[ImmutableFlashcard]]:
        """
        Returns a list of all flashcards in the database.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.

        Returns:
            Optional[List[ImmutableFlashcard]]: A list of all flashcards in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if cache and table size are equal
                if self.cache and len(self._cache) == self.count_flashcards():
                    # Return the list of immutable flashcards from the cache
                    return self.get_cache_values()

            # Get all flashcards from the database
            models: List[FlashcardModel] = asyncio.run(
                FlashcardModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of FlashcardModel objects to a list of ImmutableFlashcard objects
            flashcards: List[ImmutableFlashcard] = [
                FlashcardFactory.create_flashcard(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable flashcards
            for flashcard in flashcards:
                # Add the immutable flashcard to the cache
                self.add_to_cache(
                    key=flashcard.key,
                    value=flashcard,
                )

            # Return the list of immutable flashcards
            return flashcards
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_flashcard_by(
        self,
        field: str,
        value: Any,
        force_refetch: bool = False,
    ) -> Optional[ImmutableFlashcard]:
        """
        Retrieves a flashcard by the given field and value.

        Args:
            field (str): The field to search by.
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            value (Any): The value to search for.

        Returns:
            Optional[ImmutableFlashcard]: The flashcard with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if the flashcard is already in the cache
                if self.is_key_in_cache(key=field):
                    # Return the flashcard from the cache
                    return self.get_value_from_cache(key=field)

            # Get the flashcard with the given field and value from the database
            model: Optional[FlashcardModel] = asyncio.run(
                FlashcardModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Return the flashcard if it exists
            if model is not None:
                # Convert the FlashcardModel object to an ImmutableFlashcard object
                flashcard: ImmutableFlashcard = FlashcardFactory.create_flashcard(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the flashcard to the cache
                self.add_to_cache(
                    key=flashcard.key,
                    value=flashcard,
                )

                # Return the flashcard
                return flashcard
            else:
                # Return None indicating that the flashcard does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_flashcard_by_id(
        self,
        id: int,
        force_refetch: bool = False,
    ) -> Optional[ImmutableFlashcard]:
        """
        Returns a flashcard with the given ID.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            id (int): The ID of the flashcard.

        Returns:
            Optional[ImmutableFlashcard]: The flashcard with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if the flashcard is already in the cache
                if self.is_key_in_cache(key=f"FLASHCARD_{id}"):
                    # Return the flashcard from the cache
                    return self.get_value_from_cache(key=f"FLASHCARD_{id}")

            # Get the flashcard with the given ID from the database
            model: Optional[FlashcardModel] = asyncio.run(
                FlashcardModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the flashcard if it exists
            if model is not None:
                # Convert the FlashcardModel object to an ImmutableFlashcard object
                flashcard: ImmutableFlashcard = FlashcardFactory.create_flashcard(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the flashcard to the cache
                self.add_to_cache(
                    key=flashcard.key,
                    value=flashcard,
                )

                # Return the flashcard
                return flashcard
            else:
                # Return None indicating that the flashcard does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_flashcard_by_key(
        self,
        key: str,
        force_refetch: bool = False,
    ) -> Optional[ImmutableFlashcard]:
        """
        Returns a flashcard with the given key.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            key (str): The key of the flashcard.

        Returns:
            Optional[ImmutableFlashcard]: The flashcard with the given key if no exception occurs. Otherwise, None.

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
            model: Optional[FlashcardModel] = asyncio.run(
                FlashcardModel.get_by(
                    column="key",
                    database=Constants.DATABASE_PATH,
                    value=key,
                )
            )

            # Return the flashcard if it exists
            if model is not None:
                # Convert the FlashcardModel object to an ImmutableFlashcard object
                flashcard: ImmutableFlashcard = FlashcardFactory.create_flashcard(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the flashcard to the cache
                self.add_to_cache(
                    key=flashcard.key,
                    value=flashcard,
                )

                # Return the flashcard
                return flashcard
            else:
                # Return None indicating that the flashcard does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_key' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_flashcard_by_uuid(
        self,
        uuid: str,
        force_refetch: bool = False,
    ) -> Optional[ImmutableFlashcard]:
        """
        Returns a flashcard with the given UUID.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            uuid (str): The UUID of the flashcard.

        Returns:
            Optional[ImmutableFlashcard]: The flashcard with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if the flashcard is already in the cache
                if self.is_key_in_cache(key=uuid):
                    # Return the flashcard from the cache
                    return self.get_value_from_cache(key=uuid)

            # Get the flashcard with the given UUID from the database
            model: Optional[FlashcardModel] = asyncio.run(
                FlashcardModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the flashcard if it exists
            if model is not None:
                # Convert the FlashcardModel object to an ImmutableFlashcard object
                flashcard: ImmutableFlashcard = FlashcardFactory.create_flashcard(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the flashcard to the cache
                self.add_to_cache(
                    key=flashcard.key,
                    value=flashcard,
                )

                # Return the flashcard
                return flashcard
            else:
                # Return None indicating that the flashcard does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_from_flashcards(
        self,
        condition: Callable[[ImmutableFlashcard], bool],
        limit: Optional[int] = None,
    ) -> Optional[List[ImmutableFlashcard]]:
        """
        Returns a list of flashcards from the cache that match the given condition.

        Args:
            condition (Callable[[ImmutableFlashcard], bool]): A function that takes an ImmutableFlashcard instance and returns a boolean value.
            limit (Optional[int]): The maximum number of flashcards to return.

        Returns:
            Optional[List[ImmutableFlashcard]]: The list of flashcards that match the given condition if no exception occurs. Otherwise, None.
        """
        try:
            # Initialize an empty list to store matching flashcards
            result: List[ImmutableFlashcard] = []

            # Get all flashcards from the cache
            flashcards: List[ImmutableFlashcard] = self.get_all_flashcards()

            # Iterate over the list of immutable flashcards in the cache
            for flashcard in flashcards:
                # Check if the flashcard matches the given condition
                if condition(flashcard):
                    # Add the flashcard that matches the given condition to the result list
                    result.append(flashcard)

            # Check if the limit is specified and if the result list exceeds the limit
            if limit is not None and len(result) > limit:
                # Return the first 'limit' number of flashcards
                return result[:limit]

            # Return the list of matching flashcards
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_from_flashcards' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def search_flashcards(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[Union[List[ImmutableFlashcard]]]:
        """
        Searches for flashcards in the database.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            **kwargs: Any additional keyword arguments to be passed to the search method of the FlashcardModel class.

        Returns:
            Optional[Union[List[ImmutableFlashcard]]]: The found flashcards if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Search the stack for the passed keyword arguments
                cached_result: Optional[List[ImmutableFlashcard]] = self.search_cache(
                    **kwargs
                )

                # Check, if any cached results exist
                if cached_result:
                    # Return the cached results
                    return cached_result

            # Search for flashcards in the database
            models: Optional[List[FlashcardModel]] = asyncio.run(
                FlashcardModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found flashcards if any
            if models is not None and len(models) > 0:
                flashcards: List[ImmutableFlashcard] = [
                    FlashcardFactory.create(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                    for model in models
                ]

                # Add the flashcards to the cache
                self.add_to_cache(
                    key=[flashcard.key for flashcard in flashcards],
                    value=flashcards,
                )

                # Return the found flashcards
                return flashcards
            else:
                # Return None indicating that no flashcards were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_flashcard(
        self,
        flashcard: Union[ImmutableFlashcard, MutableFlashcard],
    ) -> Optional[ImmutableFlashcard]:
        """
        Updates a flashcard with the given ID.

        Args:
            flashcard (Union[ImmutableFlashcard, MutableFlashcard]): The flashcard to update.

        Returns:
            Optional[ImmutableFlashcard]: The updated flashcard if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the flashcard object is immutable
            if not flashcard.is_mutable():
                # If it is, convert it to a mutable flashcard
                flashcard = flashcard.to_mutable()

            # Update the updated_at timestamp of the flashcard
            flashcard.updated_at = Miscellaneous.get_current_datetime()

            # Convert the flashcard to an immutable flashcard and update the flashcard in the database
            result: bool = asyncio.run(
                FlashcardConverter.object_to_model(
                    object=FlashcardFactory.create_flashcard(
                        **flashcard.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).update(
                    database=Constants.DATABASE_PATH,
                    **flashcard.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Check, if the flashcard was updated successfully
            if result:
                # Update the flashcard in the cache
                self.update_in_cache(
                    key=flashcard.key,
                    value=flashcard,
                )

                # Return the updated flashcard
                return flashcard.to_immutable()
            else:
                # Return None indicating that the flashcard does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class FlashcardModel(ImmutableBaseModel):
    """
    Represents the structure of a flashcard model.

    Attributes:
        back_text (Field): The back side of the flashcard.
        back_word_count (Field): The word count of the back side of the flashcard.
        created_at (Field): The timestamp when the flashcard was created.
        custom_field_values (Field): The custom field values of the flashcard.
        difficulty (Field): The difficulty of the flashcard.
        due_by (Field): The timestamp when the flashcard is due.
        familiarity (Field): The familiarity of the flashcard.
        front_text (Field): The front side of the flashcard.
        front_word_count (Field): The word count of the front side of the flashcard.
        icon (Field): The icon of the flashcard. Defaults to "📇".
        id (Field): The ID of the flashcard.
        interval (Field): The repetition interval of the flashcard in days.
        key (Field): The key of the flashcard.
        last_viewed_at (Field): The timestamp when the flashcard was last viewed.
        metadata (Field): A dictionary of metadata.
        priority (Field): The priority of the flashcard.
        status (Field): The status of the flashcard.
        tags (Field): The tags of the flashcard.
        total_word_count (Field): The word count of the back side of the flashcard.
        updated_at (Field): The timestamp when the flashcard was last updated.
        uuid (Field): The UUID of the flashcard.
    """

    table: Final[str] = Constants.FLASHCARDS

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

    back_text: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="back_text",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="TEXT",
        unique=False,
    )

    back_word_count: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="back_word_count",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
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
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="DATETIME",
        unique=False,
    )

    familiarity: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="familiarity",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="FLOAT",
        unique=False,
    )

    front_text: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="front_text",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="TEXT",
        unique=True,
    )

    front_word_count: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="front_word_count",
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
        default="📇",
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
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="INTEGER",
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
        nullable=True,
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

    total_word_count: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="total_word_count",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="INTEGER",
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
        back_text: Optional[str] = None,
        back_word_count: Optional[int] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        difficulty: Optional[int] = None,
        due_by: Optional[datetime] = None,
        familiarity: Optional[float] = None,
        front_text: Optional[str] = None,
        front_word_count: Optional[int] = None,
        icon: Optional[str] = "📇",
        id: Optional[int] = None,
        interval: Optional[int] = None,
        key: Optional[str] = None,
        last_viewed_at: Optional[datetime] = None,
        metadata: Optional[Dict[str, Any]] = None,
        priority: Optional[int] = None,
        status: Optional[int] = None,
        tags: Optional[List[str]] = None,
        total_word_count: Optional[int] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the FlashcardModel class.

        Args:
            back_text (Optional[str]): The back side of the flashcard.
            back_word_count (Optional[int]): The word count of the back side of the flashcard.
            created_at (Optional[datetime]): The timestamp when the flashcard was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
            difficulty (Optional[int]): The difficulty of the flashcard.
            due_by (Optional[datetime]): The timestamp when the flashcard is due.
            familiarity (Optional[float]): The familiarity of the flashcard.
            front_text (Optional[str]): The front side of the flashcard.
            front_word_count (Optional[int]): The word count of the front side of the flashcard.
            icon (Optional[str]): The icon of the flashcard. Defaults to "📇".
            id (Optional[int]): The ID of the flashcard.
            interval (Optional[int]): The repetition interval of the flashcard in days.
            key (Optional[str]): The key of the flashcard.
            last_viewed_at (Optional[datetime]): The timestamp when the flashcard was last viewed.
            metadata (Optional[Dict[str, Any]]): A dictionary of metadata.
            priority (Optional[int]): The priority of the flashcard.
            status (Optional[int]): The status of the flashcard.
            tags (Optional[List[str]]): The tags of the flashcard.
            total_word_count (Optional[int]): The total word count of the flashcard.
            updated_at (Optional[datetime]): The timestamp when the flashcard was last updated.
            uuid (Optional[str]): The UUID of the flashcard.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            back_text=back_text,
            back_word_count=back_word_count,
            created_at=created_at,
            custom_field_values=custom_field_values,
            difficulty=difficulty,
            due_by=due_by,
            familiarity=familiarity,
            front_text=front_text,
            front_word_count=front_word_count,
            icon="📇",
            id=id,
            interval=interval,
            last_viewed_at=last_viewed_at,
            key=key,
            metadata=metadata,
            priority=priority,
            status=status,
            tags=tags,
            total_word_count=total_word_count,
            table=Constants.FLASHCARDS,
            updated_at=updated_at,
            uuid=uuid,
        )


class Flashcards:
    """
    A utility class for managing flashcards.

    This class provides a set of methods for retrieving and saving flashcards.
    """

    configuration: Final[Dict[str, Any]] = {}

    # Initialize this class's Logger instance
    logger: Final[Logger] = Logger.get_logger(name="Flashcards")

    # Initialize this class's FlashcardManager instance
    manager: Final[FlashcardManager] = FlashcardManager()

    @classmethod
    def build(
        cls,
        as_mutable: bool = False,
    ) -> Optional[
        Union[
            ImmutableFlashcard,
            MutableFlashcard,
        ]
    ]:
        """
        Builds a flashcard and returns it.

        Args:
            as_mutable (bool, optional): Whether to build the flashcard as mutable. Defaults to False.

        Returns:
            Optional[Union[ImmutableFlashcard, MutableFlashcard,]]: The flashcard if no exception occurs. Otherwise, None.
        """
        try:
            # Check, if the configuration dictionary is empty
            if not cls.configuration:
                # Log a warning message
                cls.logger.warning(
                    message="Configuration dictionary is empty. Use this class' 'set' method to set the configuration dictionary."
                )

                # Return early
                return None

            # Initialize the builder
            builder: FlashcardBuilder = FlashcardBuilder()

            # Update the builder's configuration
            builder.configuration.update(cls.configuration)

            # Build the flashcard
            flashcard: Union[ImmutableFlashcard, MutableFlashcard] = builder.build(
                as_mutable=as_mutable
            )

            # Clear the configuration
            cls.configuration.clear()

            # Return the flashcard
            return flashcard
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'build' method from '{cls.__name__}': {e}"
            )

            # Log the traceback of the exception
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def clear(cls) -> None:
        """
        Clears the configuration dictionary.

        Args:
            None

        Returns:
            None
        """

        # Clear the configuration dictionary
        cls.configuration.clear()

    @classmethod
    def create(
        cls,
        **kwargs,
    ) -> Optional[ImmutableFlashcard]:
        """
        Creates a new flashcard and returns it.

        Args:
            **kwargs: Additional keyword arguments to pass to the create_flashcard method.

        Returns:
            Optional[ImmutableFlashcard]: The flashcard if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            return FlashcardFactory.create_flashcard(**kwargs)
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create' method from '{cls.__name__}': {e}"
            )

            # Log the traceback of the exception
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def create_default(
        cls,
        back_text: str,
        front_text: str,
        as_mutable: bool = False,
    ) -> Optional[ImmutableFlashcard]:
        """
        Creates a new flashcard and returns it.

        Args:
            as_mutable (bool, optional): Whether to create the flashcard as mutable. Defaults to False.
            back_text (str): The back side of the flashcard.
            front_text (str): The front side of the flashcard.

        Returns:
            Optional[ImmutableFlashcard]: The flashcard if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            return FlashcardFactory.create_default_flashcard(
                as_mutable=as_mutable,
                back_text=back_text,
                front_text=front_text,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_default' method from '{cls.__name__}': {e}"
            )

            # Log the traceback of the exception
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def get(
        cls,
        id: Optional[int] = None,
        key: Optional[str] = None,
        **kwargs,
    ) -> Optional[ImmutableFlashcard]:
        """
        Retrieves a flashcard by the given ID, key, or other fields.

        Args:
            id (Optional[int]): The ID of the flashcard.
            key (Optional[str]): The key of the flashcard.
            **kwargs: Additional keyword arguments to pass to the get_flashcard_by method.

        Returns:
            Optional[ImmutableFlashcard]: The flashcard with the given ID, key, or other fields if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            if id:
                return cls.manager.get_flashcard_by_id(
                    force_refetch=True,
                    id=id,
                )
            elif key:
                return cls.manager.get_flashcard_by_key(
                    force_refetch=True,
                    key=key,
                )
            else:
                return cls.manager.get_flashcard_by(
                    force_refetch=True,
                    **kwargs,
                )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get' method from '{cls.__name__}': {e}"
            )

            # Log the traceback of the exception
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def get_all(cls) -> Optional[List[ImmutableFlashcard]]:
        """
        Returns a list of all flashcards in the database.

        Returns:
            Optional[List[ImmutableFlashcard]]: The flashcards if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            return cls.manager.get_all_flashcards(force_refetch=True)
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{cls.__name__}': {e}"
            )

            # Log the traceback of the exception
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def save(
        cls,
        flashcard: Union[
            ImmutableFlashcard,
            MutableFlashcard,
        ],
    ) -> ImmutableFlashcard:
        """
        Saves the passed flashcard to the database and returns it.

        Args:
            flashcard (Union[ImmutableFlashcard, MutableFlashcard]): The flashcard to save.

        Returns:
            ImmutableFlashcard: The saved flashcard if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            return cls.manager.create_flashcard(flashcard=flashcard)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'save' method from '{cls.__name__}': {e}"
            )

            # Log the traceback of the exception
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def search(
        cls,
        **kwargs,
    ) -> Optional[List[ImmutableFlashcard]]:
        """
        Searches for flashcards in the database and returns them.

        Args:
            **kwargs: Additional keyword arguments to pass to the search_flashcards method.

        Returns:
            Optional[List[ImmutableFlashcard]]: The flashcards if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            return cls.manager.search_flashcards(
                force_refetch=True,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{cls.__name__}': {e}"
            )

            # Log the traceback of the exception
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def set(
        cls,
        key: str,
        value: Optional[Any] = None,
    ) -> None:
        """
        Sets a configuration value.

        Args:
            key (str): The key of the configuration value.
            value (Optional[Any]): The value of the configuration value.

        Returns:
            None
        """

        # Check, if the key is already contained within the configuration dictionary
        if key in cls.configuration:
            # Log a warning message indicating that the key is already contained within the configuration dictionary
            cls.logger.warning(
                message=f"Key '{key}' is already contained within the configuration dictionary. Overwriting..."
            )

        # Set the configuration value corresponding to the passed key
        cls.configuration[key] = value
