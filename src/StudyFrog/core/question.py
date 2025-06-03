"""
Author: lodego
Date: 2025-02-05
"""

import asyncio
import traceback

from datetime import datetime
from enum import Enum
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
    "ImmutableQuestion",
    "MutableQuestion",
    "QuestionConverter",
    "QuestionFactory",
    "QuestionManager",
    "QuestionModel",
    "QuestionTypes",
]


class QuestionTypes(Enum):
    """
    An enum representing the types of questions.

    Attributes:
        CLOZE (str): The type of the question.
        MULTIPLE_CHOICE (str): The type of the question.
        MULTIPLE_SELECT (str): The type of the question.
        OPEN_ANSWER (str): The type of the question.
        TRUE_FALSE (str): The type of the question.
    """

    CLOZE: Literal["CLOZE"] = "CLOZE"
    MULTIPLE_CHOICE: Literal["MULTIPLE_CHOICE"] = "MULTIPLE_CHOICE"
    MULTIPLE_SELECT: Literal["MULTIPLE_SELECT"] = "MULTIPLE_SELECT"
    OPEN_ANSWER: Literal["OPEN_ANSWER"] = "OPEN_ANSWER"
    TRUE_FALSE: Literal["TRUE_FALSE"] = "TRUE_FALSE"

    @classmethod
    def get(
        cls,
        value: Literal[
            "CLOZE",
            "MULTIPLE_CHOICE",
            "MULTIPLE_SELECT",
            "OPEN_ANSWER",
            "TRUE_FALSE",
        ],
    ) -> Literal["QuestionTypes"]:
        """
        Gets the type of the question.

        Args:
            value (Literal["CLOZE", "MULTIPLE_CHOICE", "MULTIPLE_SELECT", "OPEN_ANSWER", "TRUE_FALSE"]: The type of the question.

        Returns:
            Literal[QuestionTypes]: The type of the question.
        """

        # Return the type of the question
        return cls(value)


class ImmutableQuestion(ImmutableBaseObject):
    """
    An immutable class representing a question.

    Attributes:
        answers (List[str]): The answers to the question.
        correct_answers (List[str]): The correct answers to the question.
        created_at (datetime): The timestamp when the question was created.
        custom_field_values (List[Dict[str, Any]]): The values of the custom fields.
        difficulty (int): The difficulty of the question.
        due_by (datetime): The timestamp when the question is due.
        familiarity (float): The familiarity of the question.
        icon (str): The icon of the question.
        id (int): The ID of the question.
        interval (Optional[int]): The interval of the question.
        key (str): The key of the question.
        last_viewed_at (datetime): The timestamp when the question was last viewed.
        metadata (Optional[Dict[str, Any]]): The metadata of the question.
        priority (int): The priority of the question.
        status (int): The status of the question.
        question_text (str): The text of the question.
        question_type (Literal[QuestionTypes]): The type of the question.
        status (int): The status of the question.
        tags (Optional[List[str]]): The tags associated with the question.
        updated_at (datetime): The timestamp when the question was last updated.
        uuid (str): The UUID of the question.
    """

    def __init__(
        self,
        question_text: str,
        question_type: Literal[QuestionTypes],
        answers: Optional[List[str]] = None,
        correct_answers: Optional[List[str]] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        difficulty: Optional[int] = None,
        due_by: Optional[datetime] = None,
        familiarity: Optional[float] = None,
        icon: Optional[str] = "❓",
        id: Optional[int] = None,
        interval: Optional[int] = None,
        key: Optional[str] = None,
        last_viewed_at: Optional[datetime] = None,
        metadata: Optional[Dict[str, Any]] = None,
        priority: Optional[int] = None,
        question_text_word_count: Optional[int] = None,
        status: Optional[int] = None,
        tags: Optional[List[str]] = None,
        total_word_count: Optional[int] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableQuestion class.

        Args:
            question_text (str): The text of the question.
            question_type (Literal[QuestionTypes]): The type of the question.
            answers (Optional[List[str]]): The answers to the question.
            correct_answers (Optional[List[str]]): The correct answers to the question.
            created_at (Optional[datetime]): The timestamp when the question was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): The values of the custom fields.
            difficulty (Optional[int]): The difficulty of the question.
            due_by (Optional[datetime]): The timestamp when the question is due.
            familiarity (Optional[float]): The familiarity of the question.
            icon (Optional[str]): The icon of the question. Defaults to "❓".
            id (Optional[int]): The ID of the question.
            interval (Optional[int]): The interval of the question.
            key (Optional[str]): The key of the question.
            last_viewed_at (Optional[datetime]): The timestamp when the question was last viewed.
            metadata (Optional[Dict[str, Any]]): The metadata of the question.
            priority (Optional[int]): The priority of the question.
            question_text_word_count (Optional[int]): The word count of the question text.
            status (Optional[int]): The status of the question.
            tags (Optional[List[str]]): The tags associated with the question.
            total_word_count (Optional[int]): The total word count of the question.
            updated_at (Optional[datetime]): The timestamp when the question was last updated.
            uuid (Optional[str]): The UUID of the question.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            answers=answers,
            correct_answers=correct_answers,
            created_at=created_at,
            custom_field_values=custom_field_values,
            difficulty=difficulty,
            due_by=due_by,
            familiarity=familiarity,
            hide_attributes=True,
            icon=icon,
            id=id,
            interval=interval,
            key=key,
            last_viewed_at=last_viewed_at,
            metadata=metadata,
            priority=priority,
            question_text=question_text,
            question_text_word_count=question_text_word_count,
            question_type=question_type,
            status=status,
            tags=tags,
            total_word_count=total_word_count,
            updated_at=updated_at,
            uuid=uuid,
        )

    @property
    def created_at(self) -> datetime:
        """
        Gets the created_at timestamp of the question.

        Returns:
            datetime: The created_at timestamp of the question.
        """

        # Return the created_at timestamp of the question
        return self._created_at

    @property
    def custom_field_values(self) -> List[Dict[str, Any]]:
        """
        Gets the custom field values of the question.

        Returns:
            List[Dict[str, Any]]: The custom field values of the question.
        """

        # Return the custom field values of the question
        return self._custom_field_values

    @property
    def difficulty(self) -> int:
        """
        Gets the difficulty of the question.

        Returns:
            int: The difficulty of the question.
        """

        # Return the difficulty of the question
        return self._difficulty

    @property
    def due_by(self) -> datetime:
        """
        Gets the due_by timestamp of the question.

        Returns:
            datetime: The due_by timestamp of the question.
        """

        # Return the due_by timestamp of the question
        return self._due_by

    @property
    def familiarity(self) -> float:
        """
        Gets the familiarity of the question.

        Returns:
            float: The familiarity of the question.
        """

        # Return the familiarity of the question
        return self._familiarity

    @property
    def icon(self) -> str:
        """
        Gets the icon of the question

        Returns:
            str: The icon of the question
        """

        # Return the icon of the question
        return self._icon

    @property
    def id(self) -> int:
        """
        Gets the ID of the question.

        Returns:
            int: The ID of the question.
        """

        # Return the ID of the question
        return self._id

    @property
    def interval(self) -> int:
        """
        Gets the interval of the question.

        Returns:
            int: The interval of the question.
        """

        # Return the interval of the question
        return self._interval

    @property
    def key(self) -> str:
        """
        Gets the key of the question.

        Returns:
            str: The key of the question.
        """

        # Return the key of the question
        return self._key

    @property
    def last_viewed_at(self) -> datetime:
        """
        Gets the last_viewed_at timestamp of the question.

        Returns:
            datetime: The last_viewed_at timestamp of the question.
        """

        # Return the last_viewed_at timestamp of the question
        return self._last_viewed_at

    @property
    def metadata(self) -> Dict[str, Any]:
        """
        Gets the metadata of the question.

        Returns:
            Dict[str, Any]: The metadata of the question.
        """

        # Return the metadata of the question
        return self._metadata

    @property
    def priority(self) -> int:
        """
        Gets the priority of the question.

        Returns:
            int: The priority of the question.
        """

        # Return the priority of the question
        return self._priority

    @property
    def question_text(self) -> str:
        """
        Gets the text of the question.

        Returns:
            str: The text of the question.
        """

        # Return the text of the question
        return self._question_text

    @property
    def question_text_word_count(self) -> int:
        """
        Gets the word count of the question text.

        Returns:
            int: The word count of the question text.
        """

        # Return the word count of the question text
        return self._question_text_word_count

    @property
    def question_type(self) -> Literal[QuestionTypes]:
        """
        Gets the type of the question.

        Returns:
            Literal[QuestionTypes]: The type of the question.
        """

        # Return the type of the question
        return self._question_type

    @property
    def status(self) -> int:
        """
        Gets the status of the question.

        Returns:
            int: The status of the question.
        """

        # Return the status of the question
        return self._status

    @property
    def tags(self) -> List[str]:
        """
        Gets the tags of the question.

        Returns:
            List[str]: The tags of the question.
        """

        # Return the tags of the question
        return self._tags

    @property
    def total_word_count(self) -> int:
        """
        Gets the total word count of the question.

        Returns:
            int: The total word count of the question.
        """

        # Return the total word count of the question
        return self._total_word_count

    @property
    def updated_at(self) -> datetime:
        """
        Gets the updated_at timestamp of the question.

        Returns:
            datetime: The updated_at timestamp of the question.
        """

        # Return the updated_at timestamp of the question
        return self._updated_at

    @property
    def uuid(self) -> str:
        """
        Gets the UUID of the question.

        Returns:
            str: The UUID of the question.
        """

        # Return the UUID of the question
        return self._uuid

    def to_mutable(self) -> "MutableQuestion":
        """
        Converts the immutable question to a mutable question.

        Returns:
            MutableQuestion: The mutable version of the immutable question.
        """
        try:
            # Create a new MutableQuestion instance from the dictionary representation of the ImmutableQuestion instance
            return MutableQuestion(
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

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None


class MutableQuestion(MutableBaseObject):
    """
    A mutable class representing a question.

    Attributes:
        answers (List[str]): The answers to the question.
        correct_answers (List[str]): The correct answers to the question.
        created_at (datetime): The timestamp when the question was created.
        custom_field_values (List[Dict[str, Any]]): The values of the custom fields.
        difficulty (int): The difficulty of the question.
        due_by (datetime): The timestamp when the question is due.
        familiarity (float): The familiarity of the question.
        icon (str): The icon of the question.
        id (int): The ID of the question.
        interval (Optional[int]): The repetition interval of the question in days.
        key (str): The key of the question.
        last_viewed_at (datetime): The timestamp when the question was last viewed.
        metadata (Optional[Dict[str, Any]]): The metadata of the question.
        priority (int): The priority of the question.
        question_text_word_count (Optional[int]): The word count of the question text.
        status (int): The status of the question.
        question_text (str): The text of the question.
        question_type (Literal[QuestionTypes]): The type of the question.
        status (int): The status of the question.
        tags (Optional[List[str]]): The tags associated with the question.
        total_word_count (Optional[int]): The total word count of the question.
        updated_at (datetime): The timestamp when the question was last updated.
        uuid (str): The UUID of the question.
    """

    def __init__(
        self,
        question_text: str,
        question_type: Literal[QuestionTypes],
        answers: Optional[List[str]] = None,
        correct_answers: Optional[List[str]] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        difficulty: Optional[int] = None,
        due_by: Optional[datetime] = None,
        familiarity: Optional[float] = None,
        icon: Optional[str] = "❓",
        id: Optional[int] = None,
        interval: Optional[int] = None,
        key: Optional[str] = None,
        last_viewed_at: Optional[datetime] = None,
        metadata: Optional[Dict[str, Any]] = None,
        priority: Optional[int] = None,
        question_text_word_count: Optional[int] = None,
        status: Optional[int] = None,
        tags: Optional[List[str]] = None,
        total_word_count: Optional[int] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableQuestion class.

        Args:
            question_text (str): The text of the question.
            question_type (Literal[QuestionTypes]): The type of the question.
            answers (Optional[List[str]]): The answers to the question.
            correct_answers (Optional[List[str]]): The correct answers to the question.
            created_at (Optional[datetime]): The timestamp when the question was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): The values of the custom fields.
            difficulty (Optional[int]): The difficulty of the question.
            due_by (Optional[datetime]): The timestamp when the question is due.
            familiarity (Optional[float]): The familiarity of the question.
            icon (Optional[str]): The icon of the question. Defaults to "❓".
            id (Optional[int]): The ID of the question.
            interval (Optional[int]): The repetition interval of the question in days.
            key (Optional[str]): The key of the question.
            last_viewed_at (Optional[datetime]): The timestamp when the question was last viewed.
            metadata (Optional[Dict[str, Any]]): The metadata of the question.
            priority (Optional[int]): The priority of the question.
            question_text_word_count (Optional[int]): The word count of the question text.
            status (Optional[int]): The status of the question.
            tags (Optional[List[str]]): The tags associated with the question.
            total_word_count (Optional[int]): The total word count of the question.
            updated_at (Optional[datetime]): The timestamp when the question was last updated.
            uuid (Optional[str]): The UUID of the question.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            answers=answers,
            correct_answers=correct_answers,
            created_at=created_at,
            custom_field_values=custom_field_values,
            difficulty=difficulty,
            due_by=due_by,
            familiarity=familiarity,
            hide_attributes=True,
            icon=icon,
            id=id,
            interval=interval,
            key=key,
            last_viewed_at=last_viewed_at,
            metadata=metadata,
            priority=priority,
            question_text=question_text,
            question_text_word_count=question_text_word_count,
            question_type=question_type,
            status=status,
            tags=tags,
            total_word_count=total_word_count,
            updated_at=updated_at,
            uuid=uuid,
        )

    @property
    def created_at(self) -> datetime:
        """
        Gets the created_at timestamp of the question.

        Returns:
            datetime: The created_at timestamp of the question.
        """

        # Return the created_at timestamp of the question
        return self._created_at

    @created_at.setter
    def created_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the created_at timestamp of the question.

        Args:
            value (datetime): The new created_at timestamp of the question.

        Returns:
            None
        """

        # Set the created_at timestamp of the question
        self._created_at = value

    @property
    def custom_field_values(self) -> List[Dict[str, Any]]:
        """
        Gets the custom field values of the question.

        Returns:
            List[Dict[str, Any]]: The custom field values of the question.
        """

        # Return the custom field values of the question
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
        Gets the difficulty of the question.

        Returns:
            int: The difficulty of the question.
        """

        # Return the difficulty of the question
        return self._difficulty

    @difficulty.setter
    def difficulty(
        self,
        value: int,
    ) -> None:
        """
        Sets the difficulty of the question.

        Args:
            value (int): The new difficulty of the question.

        Returns:
            None
        """

        # Set the difficulty of the question
        self._difficulty = value

    @property
    def due_by(self) -> datetime:
        """
        Gets the due_by timestamp of the question.

        Returns:
            datetime: The due_by timestamp of the question.
        """

        # Return the due_by timestamp of the question
        return self._due_by

    @due_by.setter
    def due_by(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the due_by timestamp of the question.

        Args:
            value (datetime): The new due_by timestamp of the question.

        Returns:
            None
        """

        # Set the due_by timestamp of the question
        self._due_by = value

    @property
    def familiarity(self) -> float:
        """
        Gets the familiarity of the question.

        Returns:
            float: The familiarity of the question.
        """

        # Return the familiarity of the question
        return self._familiarity

    @familiarity.setter
    def familiarity(
        self,
        value: float,
    ) -> None:
        """
        Sets the familiarity of the question.

        Args:
            value (float): The new familiarity of the question.

        Returns:
            None
        """

        # Set the familiarity of the question
        self._familiarity = value

    @property
    def icon(self) -> str:
        """
        Gets the icon of the question

        Returns:
            str: The icon of the question
        """

        # Return the icon of the question
        return self._icon

    @icon.setter
    def icon(
        self,
        value: str,
    ) -> None:
        """
        Sets the icon of the question.

        Args:
            value (str): The new icon of the question.

        Returns:
            None
        """

        # Set the icon of the question
        self._icon = value

    @property
    def id(self) -> int:
        """
        Gets the ID of the question.

        Returns:
            int: The ID of the question.
        """

        # Return the ID of the question
        return self._id

    @id.setter
    def id(
        self,
        value: int,
    ) -> None:
        """
        Sets the ID of the question.

        Args:
            value (int): The new ID of the question.

        Returns:
            None
        """

        # Set the ID of the question
        self._id = value

    @property
    def interval(self) -> int:
        """
        Gets the interval of the question.

        Returns:
            int: The interval of the question.
        """

        # Return the interval of the question
        return self._interval

    @interval.setter
    def interval(
        self,
        value: int,
    ) -> None:
        """
        Sets the interval of the question.

        Args:
            value (int): The new interval of the question.

        Returns:
            None
        """

        # Set the interval of the question
        self._interval = value

    @property
    def key(self) -> str:
        """
        Gets the key of the question.

        Returns:
            str: The key of the question.
        """

        # Return the key of the question
        return self._key

    @key.setter
    def key(
        self,
        value: str,
    ) -> None:
        """
        Sets the key of the question.

        Args:
            value (str): The new key of the question.

        Returns:
            None
        """

        # Set the key of the question
        self._key = value

    @property
    def last_viewed_at(self) -> datetime:
        """
        Gets the last_viewed_at timestamp of the question.

        Returns:
            datetime: The last_viewed_at timestamp of the question.
        """

        # Return the last_viewed_at timestamp of the question
        return self._last_viewed_at

    @last_viewed_at.setter
    def last_viewed_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the last_viewed_at timestamp of the question.

        Args:
            value (datetime): The new last_viewed_at timestamp of the question.

        Returns:
            None
        """

        # Set the last_viewed_at timestamp of the question
        self._last_viewed_at = value

    @property
    def metadata(self) -> Dict[str, Any]:
        """
        Gets the metadata of the question.

        Returns:
            Dict[str, Any]: The metadata of the question.
        """

        # Return the metadata of the question
        return self._metadata

    @metadata.setter
    def metadata(
        self,
        **kwargs,
    ) -> None:
        """
        Updates the metadata of the question.

        Args:
            **kwargs (Dict[str, Any]): The new metadata of the question.

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
        Gets the priority of the question.

        Returns:
            int: The priority of the question.
        """

        # Return the priority of the question
        return self._priority

    @priority.setter
    def priority(
        self,
        value: int,
    ) -> None:
        """
        Sets the priority of the question.

        Args:
            value (int): The new priority of the question.

        Returns:
            None
        """

        # Set the priority of the question
        self._priority = value

    @property
    def question_text(self) -> str:
        """
        Gets the text of the question.

        Returns:
            str: The text of the question.
        """

        # Return the text of the question
        return self._question_text

    @question_text.setter
    def question_text(
        self,
        value: str,
    ) -> None:
        """
        Sets the text of the question.

        Args:
            value (str): The new text of the question.

        Returns:
            None
        """

        # Set the text of the question
        self._question_text = value

    @property
    def question_text_word_count(self) -> int:
        """
        Gets the word count of the question text.

        Returns:
            int: The word count of the question text.
        """

        # Return the word count of the question text
        return self._question_text_word_count

    @question_text_word_count.setter
    def question_text_word_count(
        self,
        value: int,
    ) -> None:
        """
        Sets the word count of the question text.

        Args:
            value (int): The new word count of the question text.

        Returns:
            None
        """

        # Set the word count of the question text
        self._question_text_word_count = value

    @property
    def question_type(self) -> Literal[QuestionTypes]:
        """
        Gets the type of the question.

        Returns:
            Literal[QuestionTypes]: The type of the question.
        """

        # Return the type of the question
        return self._question_type

    @question_type.setter
    def question_type(
        self,
        value: Literal[QuestionTypes],
    ) -> None:
        """
        Sets the type of the question.

        Args:
            value (Literal[QuestionTypes]): The new type of the question.

        Returns:
            None
        """

        # Set the type of the question
        self._question_type = value

    @property
    def status(self) -> int:
        """
        Gets the status of the question.

        Returns:
            int: The status of the question.
        """

        # Return the status of the question
        return self._status

    @status.setter
    def status(
        self,
        value: int,
    ) -> None:
        """
        Sets the status of the question.

        Args:
            value (int): The new status of the question.

        Returns:
            None
        """

        # Set the status of the question
        self._status = value

    @property
    def tags(self) -> Optional[List[str]]:
        """
        Gets the tags of the question.

        Returns:
            Optional[List[str]]: The tags of the question.
        """

        # Return the tags of the question
        return self._tags

    @tags.setter
    def tags(
        self,
        value: Union[List[str], str],
    ) -> None:
        """
        Sets the tags of the question.

        Args:
            value (Union[List[str], str]): The new tags of the question.

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
        Gets the total word count of the question.

        Returns:
            int: The total word count of the question.
        """

        # Return the total word count of the question
        return self._total_word_count

    @total_word_count.setter
    def total_word_count(
        self,
        value: int,
    ) -> None:
        """
        Sets the total word count of the question.

        Args:
            value (int): The new total word count of the question.

        Returns:
            None
        """

        # Set the total word count of the question
        self._total_word_count = value

    @property
    def updated_at(self) -> datetime:
        """
        Gets the updated_at timestamp of the question.

        Returns:
            datetime: The updated_at timestamp of the question.
        """

        # Return the updated_at timestamp of the question
        return self._updated_at

    @updated_at.setter
    def updated_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the updated_at timestamp of the question.

        Args:
            value (datetime): The new updated_at timestamp of the question.

        Returns:
            None
        """

        # Set the updated_at timestamp of the question
        self._updated_at = value

    @property
    def uuid(self) -> str:
        """
        Gets the UUID of the question.

        Returns:
            str: The UUID of the question.
        """

        # Return the UUID of the question
        return self._uuid

    @uuid.setter
    def uuid(
        self,
        value: str,
    ) -> None:
        """
        Sets the UUID of the question.

        Args:
            value (str): The new UUID of the question.

        Returns:
            None
        """

        # Set the UUID of the question
        self._uuid = value

    def add_to_answers(
        self,
        answer: Any,
    ) -> None:
        """
        Adds the given answer key to the list of answers.

        Args:
            answer (Any): The answer to be added to the list of answers.
        """

        # Check, if the answers list exists
        if not self.get(
            default=None,
            name="answers",
        ):
            # Initialize the answers list as an empty list
            self.answers = []

        # Append the answer key to the list of answers
        self.answers.append(answer["key"])

    def add_to_correct_answers(
        self,
        answer: Any,
    ) -> None:
        """
        Adds the given correct answer key to the list of correct answers.

        Args:
            answer (Any): The correct answer to be added to the list of correct answers.
        """

        # Check if the correct_answers list exists
        if not self.get(
            default=None,
            name="correct_answers",
        ):
            # Initialize the correct_answers list as an empty list
            self.correct_answers = []

        # Append the correct answer key to the list of correct answers
        self.correct_answers.append(answer["key"])

    def remove_from_answers(
        self,
        answer: Any,
    ) -> None:
        """
        Removes the given answer key from the list of answers.

        Args:
            answer (Any): The answer to be removed from the list of answers.
        """

        # Check if the answers list is empty
        if not self.get(
            default=None,
            name="answers",
        ):
            # Return early if there are no answers to remove
            return

        # Remove the answer key from the list of answers
        self.answers.remove(answer["key"])

    def remove_from_correct_answers(
        self,
        answer: Any,
    ) -> None:
        """
        Removes the given correct answer key from the list of correct answers.

        Args:
            answer (Any): The correct answer to be removed from the list of correct answers.
        """

        # Check if the correct_answers list is empty
        if not self.get(
            default=None,
            name="correct_answers",
        ):
            # Return early if there are no correct answers to remove
            return

        # Remove the correct answer key from the list of correct answers
        self.correct_answers.remove(answer["key"])

    def set_difficulty(
        self,
        difficulty: Union[
            ImmutableDifficulty,
            MutableDifficulty,
        ],
    ) -> None:
        """
        Sets the difficulty of the question.

        Args:
            difficulty (Union[ImmutableDifficulty, MutableDifficulty]): The difficulty of the question.

        Returns:
            None
        """

        # Set the difficulty of the question
        self.difficulty = difficulty.id

    def set_priority(
        self,
        priority: Union[
            ImmutablePriority,
            MutablePriority,
        ],
    ) -> None:
        """
        Sets the priority of the question.

        Args:
            priority (Union[ImmutablePriority, MutablePriority]): The priority of the question.

        Returns:
            None
        """

        # Set the priority of the question
        self.priority = priority.id

    def to_immutable(self) -> ImmutableQuestion:
        """
        Converts the mutable question to an immutable question.

        Returns:
            ImmutableQuestion: The immutable version of the mutable question.
        """
        try:
            # Create a new ImmutableQuestion instance from the dictionary representation of the MutableQuestion instance
            return ImmutableQuestion(
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

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None


class QuestionConverter:
    """
    A converter class for transforming between QuestionModel and ImmutableQuestion instances.

    This class provides methods to convert a QuestionModel instance to an ImmutableQuestion instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the QuestionConverter class.
    """

    logger: Final[Logger] = Logger.get_logger(name="QuestionConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "QuestionModel",
    ) -> Optional[ImmutableQuestion]:
        """
        Converts a given QuestionModel instance to an ImmutableQuestion instance.

        Args:
            model (QuestionModel): The QuestionModel instance to be converted.

        Returns:
            ImmutableQuestion: The converted ImmutableQuestion instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the QuestionModel instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableQuestion class from the dictionary representation of the QuestionModel instance
            return ImmutableQuestion(
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
        object: ImmutableQuestion,
    ) -> Optional["QuestionModel"]:
        """
        Converts a given ImmutableQuestion instance to a QuestionModel instance.

        Args:
            object (ImmutableQuestion): The ImmutableQuestion instance to be converted.

        Returns:
            QuestionModel: The converted QuestionModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ImmutableQuestion instance.
        """
        try:
            # Attempt to create and return a new instance of the QuestionModel class from the dictionary representation of the ImmutableQuestion instance
            return QuestionModel(
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


class QuestionFactory:
    """
    A factory class for creating question objects.

    Attributes:
        logger (Logger): The logger instance associated with the QuestionFactory class.
    """

    logger: Final[Logger] = Logger.get_logger(name="QuestionFactory")

    @classmethod
    def create_question(
        cls,
        question_text: str,
        question_type: Literal[QuestionTypes],
        answers: Optional[List[str]] = None,
        correct_answers: Optional[List[str]] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        difficulty: Optional[int] = None,
        icon: Optional[str] = "❓",
        id: Optional[int] = None,
        key: Optional[str] = None,
        last_viewed_at: Optional[datetime] = None,
        metadata: Optional[Dict[str, Any]] = None,
        priority: Optional[int] = None,
        question_text_word_count: Optional[int] = None,
        status: Optional[int] = None,
        tags: Optional[List[str]] = None,
        total_word_count: Optional[int] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> MutableQuestion:
        """
        Creates a new instance of the MutableQuestion class.

        Args:
            question_text (str): The text of the question.
            question_type (Literal[QuestionTypes]): The type of the question.
            answers (Optional[List[str]]): The answers to the question.
            correct_answers (Optional[List[str]]): The correct answers to the question.
            created_at (Optional[datetime]): The timestamp when the question was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): The values of the custom fields.
            difficulty (Optional[int]): The difficulty of the question.
            icon (Optional[str]): The icon of the question. Defaults to "❓".
            id (Optional[int]): The ID of the question.
            key (Optional[str]): The key of the question.
            last_viewed_at (Optional[datetime]): The timestamp when the question was last viewed.
            metadata (Optional[Dict[str, Any]]): The metadata of the question.
            priority (Optional[int]): The priority of the question.
            question_text_word_count (Optional[int]): The word count of the question text.
            status (Optional[int]): The status of the question.
            tags (Optional[List[str]]): The tags associated with the question.
            total_word_count (Optional[int]): The total word count of the question.
            updated_at (Optional[datetime]): The timestamp when the question was last updated.
            uuid (Optional[str]): The UUID of the question.

        Returns:
            MutableQuestion: A new instance of the MutableQuestion class.
        """
        try:
            # Attempt to create an d return an MutableQuestion object
            return MutableQuestion(
                answers=answers,
                correct_answers=correct_answers,
                created_at=created_at,
                custom_field_values=custom_field_values,
                difficulty=difficulty,
                icon=icon,
                id=id,
                key=key,
                last_viewed_at=last_viewed_at,
                metadata=metadata,
                priority=priority,
                question_text=question_text,
                question_text_word_count=question_text_word_count,
                question_type=question_type,
                status=status,
                tags=tags,
                total_word_count=total_word_count,
                updated_at=updated_at,
                uuid=uuid,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_question' method from '{cls.__name__}': {e}"
            )

            # Log the traceback
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None


class QuestionBuilder(BaseObjectBuilder):
    """
    A builder class for creating question objects.

    This class extends the BaseObjectBuilder class and provides a builder pattern
    for creating question objects.

    Attributes:
        logger (Logger): The logger instance associated with the QuestionBuilder class.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the QuestionBuilder class.

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
            ImmutableQuestion,
            MutableQuestion,
        ]
    ]:
        """
        Builds an instance of the ImmutableQuestion or MutableQuestion class
        using the configuration dictionary.

        Args:
            as_mutable (bool): A flag indicating whether the question should be mutable.

        Returns:
            Optional[Union[ImmutableQuestion, MutableQuestion]]: An instance of the
            ImmutableQuestion or MutableQuestion class if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to build the question.
        """
        try:
            # Attempt to create an ImmutableQuestion using the configuration dictionary
            question: Optional[ImmutableQuestion] = QuestionFactory.create_question(
                **self.configuration
            )

            if not question:
                # Log an error message indicating an exception has occurred
                self.logger.error(
                    message=f"Failed to build an instance of the ImmutableQuestion or MutableQuestion class from '{self.__class__.__name__}'"
                )

                # Return early
                return

            # Check if the question should be mutable
            if as_mutable:
                # Convert the ImmutableQuestion to a MutableQuestion
                return question.to_mutable()

            # Return the instance of the ImmutableQuestion
            return question
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'build' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def answers(
        self,
        value: Union[List[str], str],
    ) -> Self:
        """
        Sets the answers for the builder.

        Args:
            value (Union[List[str], str]): The answers to set.

        Returns:
            Self: The builder instance.
        """

        # Check, if the 'answers' key exists in the configuration dictionary
        if "answers" not in self.configuration:
            # Set the 'answers' key in the configuration dictionary
            self.configuration["answers"] = []

        # Check, if the value is a string
        if isinstance(
            value,
            str,
        ):
            # Append the value to the 'answers' list
            self.configuration["answers"].append(value)
        # Check, if the value is a list
        elif isinstance(
            value,
            list,
        ):
            # Extend the 'answers' list with the new values
            self.configuration["answers"].extend(value)

        # Return the builder instance
        return self

    def correct_answers(
        self,
        value: Union[List[str], str],
    ) -> Self:
        """
        Sets the correct answers for the builder.

        Args:
            value (Union[List[str], str]): The correct answers to set.

        Returns:
            Self: The builder instance.
        """

        # Check, if the 'correct answers' key exists in the configuration dictionary
        if "correct_answers" not in self.configuration:
            # Set the 'correct answers' key in the configuration dictionary
            self.configuration["correct_answers"] = []

        # Check, if the value is a string
        if isinstance(
            value,
            str,
        ):
            # Append the value to the 'correct answers' list
            self.configuration["correct_answers"].append(value)
        # Check, if the value is a list
        elif isinstance(
            value,
            list,
        ):
            # Extend the 'correct answers' list with the new values
            self.configuration["correct_answers"].extend(value)

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
            # Extend the 'custom field values' list with the new values
            self.configuration["custom_field_values"].extend(value)

        # Return the builder instance
        return self

    def difficulty(
        self,
        value: int,
    ) -> Self:
        """
        Sets the difficulty of the flashcard.

        Args:
            value (int): The difficulty of the flashcard.

        Returns:
            Self: The builder instance.
        """

        # Set the difficulty value in the configuration dictionary
        self.configuration["difficulty"] = value

        # Return the builder instance
        return self

    def last_viewed_at(
        self,
        value: datetime,
    ) -> Self:
        """
        Sets the last viewed at timestamp of the flashcard.

        Args:
            value (datetime): The last viewed at timestamp of the flashcard.

        Returns:
            Self: The builder instance.
        """

        # Set the last_viewed_at value in the configuration dictionary
        self.configuration["last_viewed_at"] = value

        # Return the builder instance
        return self

    def metadata(
        self,
        **kwargs,
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
        self.configuration["metadata"].update(kwargs)

        # Return the builder instance
        return self

    def priority(
        self,
        value: int,
    ) -> Self:
        """
        Sets the priority of the flashcard.

        Args:
            value (int): The priority of the flashcard.

        Returns:
            Self: The builder instance.
        """

        # Set the priority value in the configuration dictionary
        self.configuration["priority"] = value

        # Set the question text wordcount
        self.question_text_wordcount(value=len(value.split(" ")))

        # Set the total wordcount
        self.total_wordcount(value=len(value.split(" ")))

        # Return the builder instance
        return self

    def question_text(
        self,
        value: str,
    ) -> Self:
        """
        Sets the question text of the flashcard.

        Args:
            value (str): The question text of the flashcard.

        Returns:
            Self: The builder instance.
        """

        # Set the question_text value in the configuration dictionary
        self.configuration["question_text"] = value

        # Return the builder instance
        return self

    def question_text_word_count(
        self,
        value: int,
    ) -> Self:
        """
        Sets the question text word count of the flashcard.

        Args:
            value (int): The question text word count of the flashcard.

        Returns:
            Self: The builder instance.
        """

        # Set the question_text_word_count value in the configuration dictionary
        self.configuration["question_text_word_count"] = value

        # Return the builder instance
        return self

    def question_type(
        self,
        value: Literal[QuestionTypes],
    ) -> Self:
        """
        Sets the question type of the flashcard.

        Args:
            value (Literal[QuestionTypes]): The question type of the flashcard.

        Returns:
            Self: The builder instance.
        """

        # Set the question_type value in the configuration dictionary
        self.configuration["question_type"] = value

        # Return the builder instance
        return self

    def status(
        self,
        value: int,
    ) -> Self:
        """
        Sets the status of the flashcard.

        Args:
            value (int): The status of the flashcard.

        Returns:
            Self: The builder instance.
        """

        # Set the status value in the configuration dictionary
        self.configuration["status"] = value

        # Return the builder instance
        return self

    def tags(
        self,
        value: Union[List[str], str],
    ) -> Self:
        """
        Sets the tags of the flashcard.

        Args:
            value (Union[List[str], str]): The tags of the flashcard.

        Returns:
            Self: The builder instance.
        """

        # Check, if the 'tags' key exists in the configuration dictionary
        if "tags" not in self.configuration:
            # Set the 'tags' key in the configuration dictionary
            self.configuration["tags"] = []

        # Check, if the value is a string
        if isinstance(
            value,
            str,
        ):
            # Append the value to the 'tags' list
            self.configuration["tags"].append(value)
        # Check, if the value is a list
        elif isinstance(
            value,
            list,
        ):
            # Extend the 'tags' list with the new values
            self.configuration["tags"].extend(value)

        # Return the builder instance
        return self

    def total_word_count(
        self,
        value: int,
    ) -> Self:
        """
        Sets the total word count of the flashcard.

        Args:
            value (int): The total word count of the flashcard.

        Returns:
            Self: The builder instance.
        """

        # Set the total_word_count value in the configuration dictionary
        self.configuration["total_word_count"] = value

        # Return the builder instance
        return self


class QuestionManager(BaseObjectManager):
    """
    A manager class for managing questions in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for questions.

    Attributes:
        cache: (List[Any]): The cache for storing questions.
        logger (Logger): The logger instance associated with the object.
    """

    _shared_instance: Optional["QuestionManager"] = None

    def __new__(cls) -> "QuestionManager":
        """
        Creates and returns a new instance of the QuestionManager class.

        If the instance does not exist, creates a new one by calling the parent class
        constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Returns:
            QuestionManager: The created or existing instance of QuestionManager class.
        """
        if cls._shared_instance is None:
            # Create a new instance by calling the parent class constructor
            cls._shared_instance = super(QuestionManager, cls).__new__(cls)
            # Initialize the instance
            cls._shared_instance.init()
        # Return the shared instance
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes a new instance of the QuestionManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def _run_pre_create_tasks(
        self,
        question: Union[
            ImmutableQuestion,
            MutableQuestion,
        ],
    ) -> MutableQuestion:
        """
        Runs pre-create tasks for the question.

        Args:
            question (Union[ImmutableQuestion, MutableQuestion]): The question to run pre-create tasks for.

        Returns:
            MutableQuestion: The question with pre-create tasks run.
        """

        # Check if the question object is immutable
        if not question.is_mutable():
            # If it is, convert it to a mutable question
            question = question.to_mutable()

        # Set the created_at timestamp of the question
        question.created_at = Miscellaneous.get_current_datetime()

        # Set the custom_field_values of the question
        question.custom_field_values = [] or question.custom_field_values

        # Set the key of the question
        question.key = f"QUESTION_{self.count_questions() + 1}"

        # Set the metadata of the question
        question.metadata = {} or question.metadata

        # Set the tags of the question
        question.tags = [] or question.tags

        # Set the updated_at timestamp of the question
        question.updated_at = Miscellaneous.get_current_datetime()

        # Set the uuid of the question
        question.uuid = Miscellaneous.get_uuid()

        # Return the mutable question
        return question

    def count_questions(self) -> int:
        """
        Returns the number of questions in the database.

        Returns:
            int: The number of questions in the database.
        """
        try:
            # Count and return the number of questions in the database
            return asyncio.run(QuestionModel.count(database=Constants.DATABASE_PATH))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_question(
        self,
        question: Union[ImmutableQuestion, MutableQuestion],
    ) -> Optional[ImmutableQuestion]:
        """
        Creates a new question in the database.

        Args:
            question (Union[ImmutableQuestion, MutableQuestion]): The question to be created.

        Returns:
            Optional[ImmutableQuestion]: The newly created immutable question if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the question.
        """
        try:
            # Initialize the result (optional) ImmutableQuestion to none
            result: Optional[ImmutableQuestion] = None

            # Run pre-create tasks
            question: MutableQuestion = self._run_pre_create_tasks(question=question)

            # Convert the question object to a QuestionModel object
            model: QuestionModel = QuestionConverter.object_to_model(object=question)

            # Create a new question in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            # Check, if the ID is not None
            if not id:
                # Log a warning message indicating an error has occurred
                self.logger.warning(
                    message=f"It seems that an error has occured while attempting to create a question ({question.__repr__()}) in the database."
                )

                # Return early
                return

            # Convert the question to a dictionary
            kwargs: Dict[str, Any] = question.to_dict(
                exclude=[
                    "_logger",
                ]
            )

            # Set the ID of the question
            kwargs["id"] = id

            # Create a new ImmutableQuestion object
            result = QuestionFactory.create_question(**kwargs)

            # Check, if the result is not None
            if not result:
                # Log an error message indicating an error has occurred
                self.logger.error(
                    message=f"It seems that there was an error while attempting to create an ImmutableQuestion from the dictionary ({kwargs}) returned by the database. This is likely a serious issue."
                )

                # Return early
                return

            # Add the question to the cache
            self.add_to_cache(
                key=result.key,
                value=result,
            )

            # Return the newly created ImmutableQuestion instance
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_question' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete_question(
        self,
        question: Union[ImmutableQuestion, MutableQuestion],
    ) -> bool:
        """
        Deletes a question from the database.

        Args:
            question (Union[ImmutableQuestion, MutableQuestion]): The question to be deleted.

        Returns:
            bool: True if the question was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the question to an immutable question and delete the question from the database
            result: bool = asyncio.run(
                QuestionConverter.object_to_model(
                    object=QuestionFactory.create_question(
                        **question.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).delete()
            )

            # Remove the question from the cache
            self.remove_from_cache(key=question.key)

            # Return True if the question was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all_questions(self) -> Optional[List[ImmutableQuestion]]:
        """
        Returns a list of all questions in the database.

        Returns:
            Optional[List[ImmutableQuestion]]: A list of all questions in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if cache and table size are equal
            if self.cache and len(self._cache) == self.count_questions():
                # Return the list of immutable questions from the cache
                return self.get_cache_values()

            # Get all questions from the database
            models: List[QuestionModel] = asyncio.run(
                QuestionModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of QuestionModel objects to a list of ImmutableQuestion objects
            questions: List[ImmutableQuestion] = [
                QuestionFactory.create_question(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable questions
            for question in questions:
                # Add the immutable question to the cache
                self.add_to_cache(
                    key=question.key,
                    value=question,
                )

            # Return the list of immutable questions
            return questions
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_question_by(
        self,
        field: str,
        value: Any,
    ) -> Optional[ImmutableQuestion]:
        """
        Retrieves a question by the given field and value.

        Args:
            field (str): The field to search by.
            value (Any): The value to search for.

        Returns:
            Optional[ImmutableQuestion]: The question with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the question is already in the cache
            if self.is_key_in_cache(key=field):
                # Return the question from the cache
                return self.get_value_from_cache(key=field)

            # Get the question with the given field and value from the database
            model: Optional[QuestionModel] = asyncio.run(
                QuestionModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Return the question if it exists
            if model is not None:
                # Convert the QuestionModel object to an ImmutableQuestion object
                question: ImmutableQuestion = QuestionFactory.create_question(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the question to the cache
                self.add_to_cache(
                    key=question.key,
                    value=question,
                )

                # Return the question
                return question
            else:
                # Return None indicating that the question does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_question_by_id(
        self,
        id: int,
    ) -> Optional[ImmutableQuestion]:
        """
        Returns a question with the given ID.

        Args:
            id (int): The ID of the question.

        Returns:
            Optional[ImmutableQuestion]: The question with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the question is already in the cache
            if self.is_key_in_cache(key=f"QUESTION_{id}"):
                # Return the question from the cache
                return self.get_value_from_cache(key=f"QUESTION_{id}")

            # Get the question with the given ID from the database
            model: Optional[QuestionModel] = asyncio.run(
                QuestionModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the question if it exists
            if model is not None:
                # Convert the QuestionModel object to an ImmutableQuestion object
                question: ImmutableQuestion = QuestionFactory.create_question(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the question to the cache
                self.add_to_cache(
                    key=question.key,
                    value=question,
                )

                # Return the question
                return question
            else:
                # Return None indicating that the question does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_question_by_key(
        self,
        key: str,
    ) -> Optional[ImmutableQuestion]:
        """
        Returns a question with the given key.

        Args:
            key (str): The key of the question.

        Returns:
            Optional[ImmutableQuestion]: The question with the given key if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the question is already in the cache
            if self.is_key_in_cache(key=key):
                # Return the question from the cache
                return self.get_value_from_cache(key=key)

            # Get the question with the given key from the database
            model: Optional[QuestionModel] = asyncio.run(
                QuestionModel.get_by(
                    column="key",
                    database=Constants.DATABASE_PATH,
                    value=key,
                )
            )

            # Return the question if it exists
            if model is not None:
                # Convert the QuestionModel object to an ImmutableQuestion object
                question: ImmutableQuestion = QuestionFactory.create_question(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the question to the cache
                self.add_to_cache(
                    key=question.key,
                    value=question,
                )

                # Return the question
                return question
            else:
                # Return None indicating that the question does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_question_by_uuid(
        self,
        uuid: str,
    ) -> Optional[ImmutableQuestion]:
        """
        Returns a question with the given UUID.

        Args:
            uuid (str): The UUID of the question.

        Returns:
            Optional[ImmutableQuestion]: The question with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the question is already in the cache
            if self.is_key_in_cache(key=uuid):
                # Return the question from the cache
                return self.get_value_from_cache(key=uuid)

            # Get the question with the given UUID from the database
            model: Optional[QuestionModel] = asyncio.run(
                QuestionModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the question if it exists
            if model is not None:
                # Convert the QuestionModel object to an ImmutableQuestion object
                return QuestionFactory.create_question(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the question does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def search_questions(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[Union[List[ImmutableQuestion]]]:
        """
        Searches for questions in the database.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            **kwargs: Any additional keyword arguments to be passed to the search method of the QuestionModel class.

        Returns:
            Optional[Union[List[ImmutableQuestion]]]: The found questions if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Search the stack for the passed keyword arguments
                cached_result: Optional[List[ImmutableQuestion]] = self.search_cache(
                    **kwargs
                )

                # Check, if any cached results exist
                if cached_result:
                    # Return the cached results
                    return cached_result

            # Search for questions in the database
            models: Optional[List[QuestionModel]] = asyncio.run(
                QuestionModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found questions if any
            if models is not None and len(models) > 0:
                questions: List[ImmutableQuestion] = [
                    QuestionFactory.create(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                    for model in models
                ]

                # Iterate over the found questions
                for question in questions:
                    # Add the question to the cache
                    self.add_to_cache(
                        key=question.key,
                        value=question,
                    )

                # Return the found questions
                return questions
            else:
                # Return None indicating that no questions were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_question(
        self,
        question: Union[ImmutableQuestion, MutableQuestion],
    ) -> Optional[ImmutableQuestion]:
        """
        Updates a question with the given ID.

        Args:
            question (Union[ImmutableQuestion, MutableQuestion]): The question to update.

        Returns:
            Optional[ImmutableQuestion]: The updated question if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the question object is immutable
            if isinstance(
                question,
                ImmutableQuestion,
            ):
                # If it is, convert it to a mutable question
                question = question.to_mutable()

            # Update the updated_at timestamp of the question
            question.updated_at = Miscellaneous.get_current_datetime()

            # Convert the question to an immutable question and update the question in the database
            result: bool = asyncio.run(
                QuestionConverter.object_to_model(
                    object=QuestionFactory.create_question(
                        **question.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).update(
                    database=Constants.DATABASE_PATH,
                    **question.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Check, if the question was updated successfully
            if result:
                # Update the question in the cache
                self.update_in_cache(
                    key=question.key,
                    value=question,
                )

                # Return the updated question
                return question.to_immutable()
            else:
                # Return None indicating that the question does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class QuestionModel(ImmutableBaseModel):
    """
    Represents the structure of a question model.

    Attributes:
        id (Field): The ID field of the question.
        answers (Field): The answers of the question.
        correct_answers (Field): The correct answers of the question.
        created_at (Field): The timestamp when the question was created.
        difficulty (Field): The difficulty of the question.
        due_by (Field): The due date of the question.
        familiarity (Field): The familiarity of the question.
        icon (Field): The icon of the question. Defaults to "❓".
        interval (Field): The interval of the question.
        key (Field): The key of the question.
        last_viewed_at (Field): The timestamp when the question was last viewed.
        priority (Field): The priority of the question.
        question_text (Field): The text of the question.
        question_text_word_count (Field): The word count of the question text.
        question_type (Field): The type of the question.
        status (Field): The status of the question.
        tags (Field): The tags associated with the question.
        total_word_count (Field): The total word count of the question.
        updated_at (Field): The timestamp when the question was last updated.
        uuid (Field): The UUID of the question.
    """

    table: Final[str] = Constants.QUESTIONS

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

    answers: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="answers",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
        unique=False,
    )

    correct_answers: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="correct_answers",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
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
        on_delete="CASCADE",
        on_update="CASCADE",
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

    icon: Field = Field(
        autoincrement=False,
        default="❓",
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
        on_delete="CASCADE",
        on_update="CASCADE",
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    question_text: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="question_text",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="TEXT",
        unique=False,
    )

    question_text_word_count: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="question_text_word_count",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    question_type: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="question_type",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
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
        answers: Optional[List[str]] = None,
        correct_answers: Optional[List[str]] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[Dict[str, Any]] = None,
        difficulty: Optional[int] = None,
        due_by: Optional[datetime] = None,
        familiarity: Optional[float] = None,
        icon: Optional[str] = "❓",
        id: Optional[int] = None,
        key: Optional[str] = None,
        last_viewed_at: Optional[datetime] = None,
        metadata: Optional[Dict[str, Any]] = None,
        priority: Optional[int] = None,
        question_text: Optional[str] = None,
        question_text_word_count: Optional[int] = None,
        question_type: Optional[
            Literal[
                "CLOZE",
                "MULTIPLE_CHOICE",
                "OPEN_ANSWER",
                "TRUE_FALSE",
            ]
        ] = None,
        status: Optional[int] = None,
        tags: Optional[List[str]] = None,
        total_word_count: Optional[int] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableQuestion class.

        Args:
            answers (Optional[List[str]]): The answers to the question.
            correct_answers (Optional[List[str]]): The correct answers to the question.
            created_at (Optional[datetime]): The timestamp when the question was created.
            custom_field_values (Optional[Dict[str, Any]]): The values of the custom fields.
            difficulty (Optional[int]): The difficulty of the question.
            due_by (Optional[datetime]): The due date of the question.
            familiarity (Optional[float]): The familiarity of the question.
            icon (Optional[str]): The icon of the question. Defaults to "❓".
            id (Optional[int]): The ID of the question.
            key (Optional[str]): The key of the question.
            last_viewed_at (Optional[datetime]): The timestamp when the question was last viewed.
            metadata (Optional[Dict[str, Any]]): The metadata of the question.
            priority (Optional[int]): The priority of the question.
            question_text (Optional[str]): The text of the question.
            question_text_word_count (Optional[int]): The word count of the question text.
            question_type (Optional[Literal["CLOZE", "MULTIPLE_CHOICE", "OPEN_ANSWER", "TRUE_FALSE"]]): The type of the question.
            status (Optional[int]): The ID of the status of the question.
            tags (Optional[List[str]]): The tags associated with the question.
            total_word_count (Optional[int]): The total word count of the question.
            updated_at (Optional[datetime]): The timestamp when the question was last updated.
            uuid (Optional[str]): The UUID of the question.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            answers=answers,
            correct_answers=correct_answers,
            created_at=created_at,
            custom_field_values=custom_field_values,
            difficulty=difficulty,
            due_by=due_by,
            familiarity=familiarity,
            icon="❓",
            id=id,
            key=key,
            last_viewed_at=last_viewed_at,
            metadata=metadata,
            priority=priority,
            question_text=question_text,
            question_text_word_count=question_text_word_count,
            question_type=question_type,
            status=status,
            table=Constants.QUESTIONS,
            tags=tags,
            total_word_count=total_word_count,
            updated_at=updated_at,
            uuid=uuid,
        )
