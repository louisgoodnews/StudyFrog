"""
Author: Louis Goodnews
Date: 2026-01-04
Description: This module contains the definitions of the various models used in the application
"""

import uuid

from pathlib import Path
from datetime import date, datetime

from typing import Any, Final, Optional, TypeAlias, Union

from utils.common import (
    date_from_string,
    datetime_from_string,
    exists,
    generate_uuid4,
    get_now,
    get_today,
)


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "Answer",
    "Association",
    "Customfield",
    "Difficulty",
    "Flashcard",
    "Image",
    "Model",
    "Note",
    "Option",
    "Priority",
    "Question",
    "RehearsalRunItem",
    "RehearsalRun",
    "Stack",
    "Subject",
    "Tag",
    "Teacher",
    "User",
]


# ---------- Constant ---------- #

Model: TypeAlias = Union[
    "Answer",
    "Association",
    "Customfield",
    "Difficulty",
    "Flashcard",
    "Image",
    "ModelIdentifiable",
    "ModelMetadata",
    "Note",
    "Option",
    "Priority",
    "Question",
    "RehearsalRunItem",
    "RehearsalRun",
    "Stack",
    "Subject",
    "Tag",
    "Teacher",
    "User",
]


# ---------- Helper Functions ---------- #


def _convert_to_dict(model: Model) -> dict[str, Any]:
    """
    Converts a passed Model instance into a dictionary.

    Args:
        model (Model): The model instance to convert.

    Returns:
        dict[str, Any]: The dictionary representation of the model.
    """

    result: dict[str, Any] = {}

    for (
        key,
        value,
    ) in model.__dict__.items():
        if isinstance(
            value,
            (
                ModelIdentifiable,
                ModelMetadata,
            ),
        ):
            result[key] = value.to_dict()

            continue

        result[key] = value

    return result


# ---------- Classes ---------- #


class Answer:
    """
    Represents an answer entity within the application.

    Answers are typically associated with questions or flashcards and indicate
    whether a specific response is correct. This class utilizes composition by
    incorporating ModelIdentifiable for identity management and ModelMetadata
    for tracking lifecycle details.
    """

    def __init__(
        self,
        is_correct: bool,
        text: str,
        created_at: Optional[datetime] = None,
        created_on: Optional[date] = None,
        customfields: Optional[list[dict[str, Any]]] = None,
        id_: Optional[Union[int, str]] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        updated_on: Optional[date] = None,
        uuid_: Optional[uuid.UUID] = None,
    ) -> None:
        """
        Initializes an Answer instance.

        Args:
            is_correct (bool): Flag indicating if this answer is correct.
            text (str): The actual text content of the answer.
            created_at (Optional[datetime]): Specific timestamp of creation.
            created_on (Optional[date]): Specific date of creation.
            id_ (Optional[Union[int, str]]): Database ID for the entity.
            key (Optional[str]): Unique model key identifier.
            updated_at (Optional[datetime]): Timestamp of the last update.
            updated_on (Optional[date]): Date of the last update.
            uuid_ (Optional[uuid.UUID]): Universally unique identifier.

        Returns:
            None
        """

        self._customfields: list[dict[str, Any]] = (
            customfields if exists(value=customfields) else []
        )
        self._identifiable: Final[ModelIdentifiable] = ModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._is_correct: Final[bool] = is_correct
        self._metadata: Final[ModelMetadata] = ModelMetadata(
            created_at=created_at,
            created_on=created_on,
            fields={
                "total": len(list(locals().keys())),
                "values": list(locals().keys()),
            },
            type_="ANSWER",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._text: Final[str] = text

    @property
    def created_at(self) -> datetime:
        """
        Returns the exact date and time when the answer was created.

        Returns:
            datetime: The creation timestamp.
        """

        return self._metadata.created_at

    @property
    def created_on(self) -> date:
        """
        Returns the date when the answer was created.

        Returns:
            date: The creation date.
        """

        return self._metadata.created_on

    @property
    def customfields(self) -> list[dict[str, Any]]:
        """
        Returns the list of custom fields associated with the answer.

        Returns:
            list[dict[str, Any]]: A list containing custom data dictionaries.
        """

        return self._customfields

    @customfields.setter
    def customfields(
        self,
        value: Union[
            dict[str, Any],
            list[dict[str, Any]],
        ],
    ) -> None:
        if isinstance(
            value,
            dict,
        ):
            self._customfields.append(value)

            return

        self._customfields.extend(value)

    @property
    def fields(self) -> dict[str, Any]:
        """
        Returns a copy of the dynamic metadata fields from the metadata component.

        Returns:
            dict[str, Any]: A dictionary containing additional metadata field information.
        """

        return dict(self._metadata.fields)

    @property
    def id_(self) -> Optional[Union[int, str]]:
        """
        Returns the internal database ID of the answer.

        Returns:
            Optional[Union[int, str]]: The database ID if assigned, otherwise None.
        """

        return self._identifiable.id_

    @property
    def key(self) -> Optional[str]:
        """
        Returns the unique string identifier (key) of the answer.

        Returns:
            Optional[str]: The model key if assigned, otherwise None.
        """
        return self._identifiable.key

    @property
    def is_correct(self) -> bool:
        """
        Returns whether the answer is correct.

        Returns:
            bool: Whether the answer is correct.
        """

        return self._is_correct

    @property
    def text(self) -> str:
        """
        Returns the text of the answer.

        Returns:
            str: The text of the answer.
        """

        return self._text

    @property
    def type_(self) -> str:
        """
        Returns the type of the model (ANSWER).

        Returns:
            str: The model type string.
        """

        return self._metadata.type_

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp of the last update.

        Returns:
            datetime: The last update timestamp.
        """

        return self._metadata.updated_at

    @property
    def updated_on(self) -> date:
        """
        Returns the date of the last update.

        Returns:
            date: The last update date.
        """

        return self._metadata.updated_on

    @property
    def uuid_(self) -> uuid.UUID:
        """
        Returns the universally unique identifier (UUID) of the answer.

        Returns:
            uuid.UUID: The instance's UUID.
        """

        return self._identifiable.uuid_

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the model.

        Args:
            None

        Returns:
            dict[str, Any]: The dictionary representation of the model.
        """

        return _convert_to_dict(self)


class Association:
    """
    Represents an association entity within the application.

    Associations are used to link different models together, such as connecting
    questions with specific answers or options. This class utilizes composition
    by incorporating ModelIdentifiable for identity management and ModelMetadata
    for tracking lifecycle details.
    """

    def __init__(
        self,
        answer: Optional[Union[int, str]] = None,
        created_at: Optional[datetime] = None,
        created_on: Optional[date] = None,
        customfield: Optional[Union[int, str]] = None,
        difficulty: Optional[Union[int, str]] = None,
        flashcard: Optional[Union[int, str]] = None,
        id_: Optional[Union[int, str]] = None,
        image: Optional[Union[int, str]] = None,
        key: Optional[str] = None,
        note: Optional[Union[int, str]] = None,
        option: Optional[Union[int, str]] = None,
        question: Optional[Union[int, str]] = None,
        rehearsal_run: Optional[Union[int, str]] = None,
        rehearsal_run_item: Optional[Union[int, str]] = None,
        stack: Optional[Union[int, str]] = None,
        subject: Optional[Union[int, str]] = None,
        tag: Optional[Union[int, str]] = None,
        teacher: Optional[Union[int, str]] = None,
        updated_at: Optional[datetime] = None,
        updated_on: Optional[date] = None,
        user: Optional[Union[int, str]] = None,
        uuid_: Optional[uuid.UUID] = None,
    ) -> None:
        """
        Initializes an Association instance.

        Args:
            answer (Optional[Union[int, str]]): The ID or key of the associated answer.
            created_at (Optional[datetime]): Specific timestamp of creation.
            created_on (Optional[date]): Specific date of creation.
            id_ (Optional[Union[int, str]]): Database ID for the entity.
            key (Optional[str]): Unique model key identifier.
            option (Optional[Union[int, str]]): The ID or key of the associated option.
            question (Optional[Union[int, str]]): The ID or key of the associated question.
            updated_at (Optional[datetime]): Timestamp of the last update.
            updated_on (Optional[date]): Date of the last update.
            uuid_ (Optional[uuid.UUID]): Universally unique identifier.

        Returns:
            None
        """

        self._answer: Optional[Union[int, str]] = answer
        self._customfield: Optional[Union[int, str]] = customfield
        self._difficulty: Optional[Union[int, str]] = difficulty
        self._flashcard: Optional[Union[int, str]] = flashcard
        self._identifiable: Final[ModelIdentifiable] = ModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._image: Optional[Union[int, str]] = image
        self._metadata: Final[ModelMetadata] = ModelMetadata(
            created_at=created_at,
            created_on=created_on,
            fields={
                "total": len(list(locals().keys())),
                "values": list(locals().keys()),
            },
            type_="ASSOCIATION",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._note: Optional[Union[int, str]] = note
        self._option: Optional[Union[int, str]] = option
        self._question: Optional[Union[int, str]] = question
        self._rehearsal_run: Optional[Union[int, str]] = rehearsal_run
        self._rehearsal_run_item: Optional[Union[int, str]] = rehearsal_run_item
        self._stack: Optional[Union[int, str]] = stack
        self._subject: Optional[Union[int, str]] = subject
        self._tag: Optional[Union[int, str]] = tag
        self._teacher: Optional[Union[int, str]] = teacher
        self._user: Optional[Union[int, str]] = user

    @property
    def answer(self) -> Optional[str]:
        """
        Returns the answer key of the association.

        Returns:
            Optional[str]: The internal key representing the answer.
        """

        return self._answer

    @answer.setter
    def answer(
        self,
        value: str,
    ) -> None:
        self._answer = value

    @property
    def created_at(self) -> datetime:
        """
        Returns the exact date and time when the association was created.

        Returns:
            datetime: The creation timestamp.
        """

        return self._metadata.created_at

    @property
    def created_on(self) -> date:
        """
        Returns the date when the association was created.

        Returns:
            date: The creation date.
        """

        return self._metadata.created_on

    @property
    def customfield(self) -> Optional[str]:
        """
        Returns the customfield key of the association.

        Returns:
            Optional[str]: The internal key representing the customfield.
        """

        return self._customfield

    @customfield.setter
    def customfield(
        self,
        value: str,
    ) -> None:
        self._customfield = value

    @property
    def difficulty(self) -> Optional[str]:
        """
        Returns the difficulty key of the association.

        Returns:
            Optional[str]: The internal key representing the difficulty.
        """

        return self._difficulty

    @difficulty.setter
    def difficulty(
        self,
        value: str,
    ) -> None:
        self._difficulty = value

    @property
    def fields(self) -> dict[str, Any]:
        """
        Returns a copy of the dynamic metadata fields from the metadata component.

        Returns:
            dict[str, Any]: A dictionary containing additional metadata field information.
        """

        return dict(self._metadata.fields)

    @property
    def flashcard(self) -> Optional[str]:
        """
        Returns the flashcard key of the association.

        Returns:
            Optional[str]: The internal key representing the flashcard.
        """

        return self._flashcard

    @flashcard.setter
    def flashcard(
        self,
        value: str,
    ) -> None:
        self._flashcard = value

    @property
    def id_(self) -> Optional[Union[int, str]]:
        """
        Returns the internal database ID of the association.

        Returns:
            Optional[Union[int, str]]: The database ID if assigned, otherwise None.
        """

        return self._identifiable.id_

    @property
    def key(self) -> Optional[str]:
        """
        Returns the unique string identifier (key) of the association.

        Returns:
            Optional[str]: The model key if assigned, otherwise None.
        """
        return self._identifiable.key

    @property
    def note(self) -> Optional[str]:
        """
        Returns the note key of the association.

        Returns:
            Optional[str]: The internal key representing the note.
        """

        return self._note

    @note.setter
    def note(
        self,
        value: str,
    ) -> None:
        self._note = value

    @property
    def option(self) -> Optional[str]:
        """
        Returns the option key of the association.

        Returns:
            Optional[str]: The internal key representing the option.
        """

        return self._option

    @option.setter
    def option(
        self,
        value: str,
    ) -> None:
        self._option = value

    @property
    def priority(self) -> Optional[str]:
        """
        Returns the priority key of the association.

        Returns:
            Optional[str]: The internal key representing the priority.
        """

        return self._priority

    @priority.setter
    def priority(
        self,
        value: str,
    ) -> None:
        self._priority = value

    @property
    def question(self) -> Optional[str]:
        """
        Returns the question key of the association.

        Returns:
            Optional[str]: The internal key representing the question.
        """

        return self._question

    @question.setter
    def question(
        self,
        value: str,
    ) -> None:
        self._question = value

    @property
    def rehearsal_run(self) -> Optional[str]:
        """
        Returns the rehearsal_run key of the association.

        Returns:
            Optional[str]: The internal key representing the rehearsal_run.
        """

        return self._rehearsal_run

    @rehearsal_run.setter
    def rehearsal_run(
        self,
        value: str,
    ) -> None:
        self._rehearsal_run = value

    @property
    def rehearsal_run_item(self) -> Optional[str]:
        """
        Returns the rehearsal_run_item key of the association.

        Returns:
            Optional[str]: The internal key representing the rehearsal_run_item.
        """

        return self._rehearsal_run_item

    @rehearsal_run_item.setter
    def rehearsal_run_item(
        self,
        value: str,
    ) -> None:
        self._rehearsal_run_item = value

    @property
    def stack(self) -> Optional[str]:
        """
        Returns the stack key of the association.

        Returns:
            Optional[str]: The internal key representing the stack.
        """

        return self._stack

    @stack.setter
    def stack(
        self,
        value: str,
    ) -> None:
        self._stack = value

    @property
    def subject(self) -> Optional[str]:
        """
        Returns the subject key of the association.

        Returns:
            Optional[str]: The internal key representing the subject.
        """

        return self._subject

    @subject.setter
    def subject(
        self,
        value: str,
    ) -> None:
        self._subject = value

    @property
    def tag(self) -> Optional[str]:
        """
        Returns the tag key of the association.

        Returns:
            Optional[str]: The internal key representing the tag.
        """

        return self._tag

    @tag.setter
    def tag(
        self,
        value: str,
    ) -> None:
        self._tag = value

    @property
    def teacher(self) -> Optional[str]:
        """
        Returns the teacher key of the association.

        Returns:
            Optional[str]: The internal key representing the teacher.
        """

        return self._teacher

    @teacher.setter
    def teacher(
        self,
        value: str,
    ) -> None:
        self._teacher = value

    @property
    def type_(self) -> str:
        """
        Returns the type of the model (ASSOCIATION).

        Returns:
            str: The model type string.
        """

        return self._metadata.type_

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp of the last update.

        Returns:
            datetime: The last update timestamp.
        """

        return self._metadata.updated_at

    @property
    def updated_on(self) -> date:
        """
        Returns the date of the last update.

        Returns:
            date: The last update date.
        """

        return self._metadata.updated_on

    @property
    def user(self) -> Optional[str]:
        """
        Returns the user key of the association.

        Returns:
            Optional[str]: The internal key representing the user.
        """

        return self._user

    @user.setter
    def user(
        self,
        value: str,
    ) -> None:
        self._user = value

    @property
    def uuid_(self) -> uuid.UUID:
        """
        Returns the universally unique identifier (UUID) of the association.

        Returns:
            uuid.UUID: The instance's UUID.
        """

        return self._identifiable.uuid_

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the model.

        Args:
            None

        Returns:
            dict[str, Any]: The dictionary representation of the model.
        """

        return _convert_to_dict(self)


class Customfield:
    """
    Represents a custom field entity within the application.

    Custom fields allow for the attachment of arbitrary key-value pairs to other models,
    providing a flexible way to extend data structures. This class utilizes
    composition by incorporating ModelIdentifiable for identity management and
    ModelMetadata for tracking lifecycle details.
    """

    def __init__(
        self,
        name: str,
        created_at: Optional[datetime] = None,
        created_on: Optional[date] = None,
        id_: Optional[Union[int, str]] = None,
        key: Optional[str] = None,
        options: Optional[list[str]] = None,
        updated_at: Optional[datetime] = None,
        updated_on: Optional[date] = None,
        uuid_: Optional[uuid.UUID] = None,
    ) -> None:
        """
        Initializes a Customfield instance.

        Args:
            name (str): The name or label of the custom field.
            created_at (Optional[datetime]): Specific timestamp of creation.
            created_on (Optional[date]): Specific date of creation.
            id_ (Optional[Union[int, str]]): Database ID for the entity.
            key (Optional[str]): Unique model key identifier.
            updated_at (Optional[datetime]): Timestamp of the last update.
            updated_on (Optional[date]): Date of the last update.
            uuid_ (Optional[uuid.UUID]): Universally unique identifier.

        Returns:
            None
        """

        self._identifiable: Final[ModelIdentifiable] = ModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._metadata: Final[ModelMetadata] = ModelMetadata(
            created_at=created_at,
            created_on=created_on,
            fields={
                "total": len(list(locals().keys())),
                "values": list(locals().keys()),
            },
            type_="CUSTOMFIELD",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._name: str = name
        self._options: list[str] = options if exists(value=options) else []

    @property
    def created_at(self) -> datetime:
        """
        Returns the exact date and time when the customfield was created.

        Returns:
            datetime: The creation timestamp.
        """

        return self._metadata.created_at

    @property
    def created_on(self) -> date:
        """
        Returns the date when the customfield was created.

        Returns:
            date: The creation date.
        """

        return self._metadata.created_on

    @property
    def fields(self) -> dict[str, Any]:
        """
        Returns a copy of the dynamic metadata fields from the metadata component.

        Returns:
            dict[str, Any]: A dictionary containing additional metadata field information.
        """

        return dict(self._metadata.fields)

    @property
    def id_(self) -> Optional[Union[int, str]]:
        """
        Returns the internal database ID of the customfield.

        Returns:
            Optional[Union[int, str]]: The database ID if assigned, otherwise None.
        """

        return self._identifiable.id_

    @property
    def key(self) -> Optional[str]:
        """
        Returns the unique string identifier (key) of the customfield.

        Returns:
            Optional[str]: The model key if assigned, otherwise None.
        """
        return self._identifiable.key

    @property
    def name(self) -> str:
        """
        Returns the name of the customfield.

        Returns:
            str: The name of the customfield.
        """

        return self._name

    @name.setter
    def name(
        self,
        value: str,
    ) -> None:
        self._name = value

    @property
    def options(self) -> list[str]:
        """
        Returns the options of the customfield.

        Returns:
            list[str]: The options of the customfield.
        """
        return self._options

    @options.setter
    def options(
        self,
        value: Union[
            list[str],
            str,
        ],
    ) -> None:
        if isinstance(
            value,
            list,
        ):
            self._options.extend(value)

            return

        self._options.append(value)

    @property
    def type_(self) -> str:
        """
        Returns the type of the model (CUSTOMFIELD).

        Returns:
            str: The model type string.
        """

        return self._metadata.type_

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp of the last update.

        Returns:
            datetime: The last update timestamp.
        """

        return self._metadata.updated_at

    @property
    def updated_on(self) -> date:
        """
        Returns the date of the last update.

        Returns:
            date: The last update date.
        """

        return self._metadata.updated_on

    @property
    def uuid_(self) -> uuid.UUID:
        """
        Returns the universally unique identifier (UUID) of the customfield.

        Returns:
            uuid.UUID: The instance's UUID.
        """

        return self._identifiable.uuid_

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the model.

        Args:
            None

        Returns:
            dict[str, Any]: The dictionary representation of the model.
        """

        return _convert_to_dict(self)


class Difficulty:
    """
    Represents a difficulty level entity within the application.

    This class defines the complexity of learning materials using a display name,
    an internal name, and a numerical value. It utilizes composition for
    identification and metadata management.
    """

    def __init__(
        self,
        display_name: str,
        name: str,
        value: float,
        created_at: Optional[datetime] = None,
        created_on: Optional[date] = None,
        id_: Optional[Union[int, str]] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        updated_on: Optional[date] = None,
        uuid_: Optional[uuid.UUID] = None,
    ) -> None:
        """
        Initializes a Difficulty instance.

        Args:
            display_name (str): The human-readable name of the difficulty level.
            name (str): The internal technical name of the difficulty level.
            value (float): The numerical weight or value of this difficulty.
            created_at (Optional[datetime]): Specific timestamp of creation.
            created_on (Optional[date]): Specific date of creation.
            id_ (Optional[Union[int, str]]): Database ID for the entity.
            key (Optional[str]): Unique model key identifier.
            updated_at (Optional[datetime]): Timestamp of the last update.
            updated_on (Optional[date]): Date of the last update.
            uuid_ (Optional[uuid.UUID]): Universally unique identifier.

        Returns:
            None
        """

        self._display_name: Final[str] = display_name
        self._identifiable: Final[ModelIdentifiable] = ModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._metadata: Final[ModelMetadata] = ModelMetadata(
            created_at=created_at,
            created_on=created_on,
            fields={
                "total": len(list(locals().keys())),
                "values": list(locals().keys()),
            },
            type_="DIFFICULTY",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._name: Final[str] = name
        self._value: Final[float] = value

    @property
    def created_at(self) -> datetime:
        """
        Returns the exact date and time when the difficulty was created.

        Returns:
            datetime: The creation timestamp.
        """

        return self._metadata.created_at

    @property
    def created_on(self) -> date:
        """
        Returns the date when the difficulty was created.

        Returns:
            date: The creation date.
        """

        return self._metadata.created_on

    @property
    def display_name(self) -> str:
        """
        Returns the display name of the difficulty.

        Returns:
            str: The display name of the difficulty.
        """

        return self._display_name

    @property
    def fields(self) -> dict[str, Any]:
        """
        Returns a copy of the dynamic metadata fields from the metadata component.

        Returns:
            dict[str, Any]: A dictionary containing additional metadata field information.
        """

        return dict(self._metadata.fields)

    @property
    def id_(self) -> Optional[Union[int, str]]:
        """
        Returns the internal database ID of the difficulty.

        Returns:
            Optional[Union[int, str]]: The database ID if assigned, otherwise None.
        """

        return self._identifiable.id_

    @property
    def key(self) -> Optional[str]:
        """
        Returns the unique string identifier (key) of the difficulty.

        Returns:
            Optional[str]: The model key if assigned, otherwise None.
        """
        return self._identifiable.key

    @property
    def name(self) -> str:
        """
        Returns the name of the difficulty.

        Returns:
            str: The name of the difficulty.
        """

        return self._name

    @property
    def type_(self) -> str:
        """
        Returns the type of the model (DIFFICULTY).

        Returns:
            str: The model type string.
        """

        return self._metadata.type_

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp of the last update.

        Returns:
            datetime: The last update timestamp.
        """

        return self._metadata.updated_at

    @property
    def updated_on(self) -> date:
        """
        Returns the date of the last update.

        Returns:
            date: The last update date.
        """

        return self._metadata.updated_on

    @property
    def uuid_(self) -> uuid.UUID:
        """
        Returns the universally unique identifier (UUID) of the difficulty.

        Returns:
            uuid.UUID: The instance's UUID.
        """

        return self._identifiable.uuid_

    @property
    def value(self) -> float:
        """
        Returns the value of the difficulty.

        Returns:
            float: The value of the difficulty.
        """

        return self._value

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the model.

        Args:
            None

        Returns:
            dict[str, Any]: The dictionary representation of the model.
        """

        return _convert_to_dict(self)


class Flashcard:
    """
    Represents a flashcard entity within the application.

    A flashcard consists of a front and back side for learning, associated
    metadata (like difficulty and priority), and organizational attributes
    such as tags, subjects, and teachers.
    """

    def __init__(
        self,
        back: str,
        front: str,
        author: Optional[str] = None,
        created_at: Optional[datetime] = None,
        created_on: Optional[date] = None,
        customfields: Optional[list[dict[str, Any]]] = None,
        difficulty: Optional[str] = None,
        id_: Optional[Union[int, str]] = None,
        is_assigned_to_stack: bool = False,
        key: Optional[str] = None,
        last_viewed_at: Optional[datetime] = None,
        last_viewed_on: Optional[datetime] = None,
        next_view_on: Optional[date] = None,
        priority: Optional[str] = None,
        subject: Optional[str] = None,
        tags: Optional[list[str]] = None,
        teacher: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        updated_on: Optional[date] = None,
        uuid_: Optional[uuid.UUID] = None,
    ) -> None:
        """
        Initializes a Flashcard instance.

        Args:
            back (str): The content on the back of the card.
            front (str): The content on the front of the card.
            author (Optional[str]): The creator of the flashcard.
            created_at (Optional[datetime]): Specific timestamp of creation.
            created_on (Optional[date]): Specific date of creation.
            customfields (Optional[list[dict[str, Any]]]): List of custom data fields.
            difficulty (Optional[str]): Difficulty level key.
            id_ (Optional[Union[int, str]]): Database ID.
            is_assigned_to_stack (bool): Whether the card belongs to a stack.
            key (Optional[str]): Unique model key.
            last_viewed_at (Optional[datetime]): Last time the card was seen.
            last_viewed_on (Optional[datetime]): Last date the card was seen.
            next_view_on (Optional[date]): Scheduled date for next review.
            priority (Optional[str]): Priority level key.
            subject (Optional[str]): Associated subject key.
            tags (Optional[list[str]]): List of associated tags.
            teacher (Optional[str]): Associated teacher key.
            updated_at (Optional[datetime]): Last update timestamp.
            updated_on (Optional[date]): Last update date.
            uuid_ (Optional[uuid.UUID]): Unique identifier.

        Returns:
            None
        """

        self._author: Optional[str] = author
        self._back: str = back
        self._front: str = front
        self._customfields: list[dict[str, Any]] = customfields or []
        self._difficulty: Optional[str] = difficulty
        self._identifiable: Final[ModelIdentifiable] = ModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._is_assigned_to_stack: bool = is_assigned_to_stack
        self._last_viewed_at: Optional[datetime] = last_viewed_at
        self._last_viewed_on: Optional[datetime] = last_viewed_on
        self._metadata: Final[ModelMetadata] = ModelMetadata(
            created_at=created_at,
            created_on=created_on,
            fields={
                "total": len(list(locals().keys())),
                "values": list(locals().keys()),
            },
            type_="FLASHCARD",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._next_view_on: Optional[date] = next_view_on
        self._priority: Optional[str] = priority
        self._subject: Optional[str] = subject
        self._tags: list[str] = tags or []
        self._teacher: Optional[str] = teacher

    @property
    def author(self) -> Optional[str]:
        """
        Returns the author of the flashcard.

        Returns:
            Optional[str]: The name or identifier of the flashcard's author.
        """

        return self._author

    @author.setter
    def author(
        self,
        value: str,
    ) -> None:
        self._author = value

    @property
    def back(self) -> str:
        """
        Returns the backside text of the flashcard.

        Returns:
            str: The text or content displayed on the back of the card.
        """

        return self._back

    @back.setter
    def back(
        self,
        value: str,
    ) -> None:
        self._back = value

    @property
    def created_at(self) -> datetime:
        """
        Returns the exact date and time when the flashcard was created.

        Returns:
            datetime: The creation timestamp.
        """

        return self._metadata.created_at

    @property
    def created_on(self) -> date:
        """
        Returns the date when the flashcard was created.

        Returns:
            date: The creation date.
        """

        return self._metadata.created_on

    @property
    def customfields(self) -> list[dict[str, Any]]:
        """
        Returns the list of custom fields associated with the flashcard.

        Returns:
            list[dict[str, Any]]: A list containing custom data dictionaries.
        """

        return self._customfields

    @customfields.setter
    def customfields(
        self,
        value: Union[
            dict[str, Any],
            list[dict[str, Any]],
        ],
    ) -> None:
        if isinstance(
            value,
            dict,
        ):
            self._customfields.append(value)

            return

        self._customfields.extend(value)

    @property
    def difficulty(self) -> Optional[str]:
        """
        Returns the difficulty key of the flashcard.

        Returns:
            Optional[str]: The internal key representing the difficulty level.
        """

        return self._difficulty

    @difficulty.setter
    def difficulty(
        self,
        value: str,
    ) -> None:
        self._difficulty = value

    @property
    def fields(self) -> dict[str, Any]:
        """
        Returns a copy of the dynamic metadata fields from the metadata component.

        Returns:
            dict[str, Any]: A dictionary containing additional metadata field information.
        """

        return dict(self._metadata.fields)

    @property
    def front(self) -> str:
        """
        Returns the frontside text of the flashcard.

        Returns:
            str: The text or content displayed on the front of the card.
        """

        return self._front

    @front.setter
    def front(
        self,
        value: str,
    ) -> None:
        self._front = value

    @property
    def id_(self) -> Optional[Union[int, str]]:
        """
        Returns the internal database ID of the flashcard.

        Returns:
            Optional[Union[int, str]]: The database ID if assigned, otherwise None.
        """

        return self._identifiable.id_

    @property
    def is_assigned_to_stack(self) -> bool:
        """
        Returns whether the flashcard is currently assigned to a stack.

        Returns:
            bool: True if assigned, False otherwise.
        """

        return self._is_assigned_to_stack

    @is_assigned_to_stack.setter
    def is_assigned_to_stack(
        self,
        value: bool,
    ) -> None:
        self._is_assigned_to_stack = value

    @property
    def key(self) -> Optional[str]:
        """
        Returns the unique string identifier (key) of the flashcard.

        Returns:
            Optional[str]: The model key if assigned, otherwise None.
        """
        return self._identifiable.key

    @property
    def last_viewed_at(self) -> Optional[datetime]:
        return self._last_viewed_at

    @last_viewed_at.setter
    def last_viewed_at(
        self,
        value: datetime,
    ) -> None:
        """
        Returns the timestamp when the flashcard was last viewed.

        Returns:
            Optional[datetime]: The last viewing timestamp if available.
        """

        self._last_viewed_at = value

    @property
    def next_view_on(self) -> Optional[date]:
        """
        Returns the date when the flashcard was last viewed.

        Returns:
            Optional[date]: The last viewing date if available.
        """

        return self._next_view_on

    @next_view_on.setter
    def next_view_on(self, value: Optional[date]) -> None:
        """
        Returns the date for the next scheduled review of the flashcard.

        Returns:
            Optional[date]: The scheduled date for the next rehearsal.
        """

        self._next_view_on = value

    @property
    def priority(self) -> Optional[str]:
        """
        Returns the priority key of the flashcard.

        Returns:
            Optional[str]: The internal key representing the priority level.
        """

        return self._priority

    @priority.setter
    def priority(
        self,
        value: str,
    ) -> None:
        self._priority = value

    @property
    def subject(self) -> Optional[str]:
        """
        Returns the subject key associated with the flashcard.

        Returns:
            Optional[str]: The internal key for the associated subject.
        """

        return self._subject

    @subject.setter
    def subject(
        self,
        value: str,
    ) -> None:
        self._subject = value

    @property
    def tags(self) -> list[str]:
        """
        Returns the list of tags associated with the flashcard.

        Returns:
            list[str]: A list of tag strings.
        """

        return self._tags

    @tags.setter
    def tags(
        self,
        value: list[str],
    ) -> None:
        self._tags = value

    @property
    def teacher(self) -> Optional[str]:
        """
        Returns the teacher key associated with the flashcard.

        Returns:
            Optional[str]: The internal key for the associated teacher.
        """

        return self._teacher

    @teacher.setter
    def teacher(
        self,
        value: str,
    ) -> None:
        self._teacher = value

    @property
    def type_(self) -> str:
        """
        Returns the type of the model (FLASHCARD).

        Returns:
            str: The model type string.
        """

        return self._metadata.type_

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp of the last update.

        Returns:
            datetime: The last update timestamp.
        """

        return self._metadata.updated_at

    @property
    def updated_on(self) -> date:
        """
        Returns the date of the last update.

        Returns:
            date: The last update date.
        """

        return self._metadata.updated_on

    @property
    def uuid_(self) -> uuid.UUID:
        """
        Returns the universally unique identifier (UUID) of the flashcard.

        Returns:
            uuid.UUID: The instance's UUID.
        """

        return self._identifiable.uuid_

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the model.

        Args:
            None

        Returns:
            dict[str, Any]: The dictionary representation of the model.
        """

        return _convert_to_dict(self)


class Image:
    """
    Represents an image entity within the application.

    This class manages image data including its name and filesystem path.
    It utilizes composition by incorporating ModelIdentifiable for
    identity management and ModelMetadata for tracking creation and
    update information.
    """

    def __init__(
        self,
        name: str,
        path: Path,
        created_at: Optional[datetime] = None,
        created_on: Optional[date] = None,
        fields: Optional[dict[str, Any]] = None,
        id_: Optional[Union[int, str]] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        updated_on: Optional[date] = None,
        uuid_: Optional[uuid.UUID] = None,
    ) -> None:
        """
        Initializes an Image instance.

        Args:
            name (str): The descriptive name of the image.
            path (Path): The filesystem path where the image is stored.
            created_at (Optional[datetime]): Specific timestamp of creation.
            created_on (Optional[date]): Specific date of creation.
            fields (Optional[dict[str, Any]]): Additional dynamic metadata fields.
            id_ (Optional[Union[int, str]]): Database ID for the entity.
            key (Optional[str]): Unique model key identifier.
            updated_at (Optional[datetime]): Timestamp of the last update.
            updated_on (Optional[date]): Date of the last update.
            uuid_ (Optional[uuid.UUID]): Universally unique identifier.

        Returns:
            None
        """

        self._identifiable: Final[ModelIdentifiable] = ModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._metadata: Final[ModelMetadata] = ModelMetadata(
            created_at=created_at,
            created_on=created_on,
            fields={
                "total": len(list(locals().keys())),
                "values": list(locals().keys()),
            },
            type_="IMAGE",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._name: Final[str] = name
        self._path: Final[Path] = path

    @property
    def created_at(self) -> datetime:
        """
        Returns the exact date and time when the image was created.

        Returns:
            datetime: The creation timestamp.
        """

        return self._metadata.created_at

    @property
    def created_on(self) -> date:
        """
        Returns the date when the image was created.

        Returns:
            date: The creation date.
        """

        return self._metadata.created_on

    @property
    def fields(self) -> dict[str, Any]:
        """
        Returns a copy of the dynamic metadata fields from the metadata component.

        Returns:
            dict[str, Any]: A dictionary containing additional metadata field information.
        """

        return dict(self._metadata.fields)

    @property
    def id_(self) -> Optional[Union[int, str]]:
        """
        Returns the internal database ID of the image.

        Returns:
            Optional[Union[int, str]]: The database ID if assigned, otherwise None.
        """

        return self._identifiable.id_

    @property
    def key(self) -> Optional[str]:
        """
        Returns the unique string identifier (key) of the image.

        Returns:
            Optional[str]: The model key if assigned, otherwise None.
        """
        return self._identifiable.key

    @property
    def name(self) -> str:
        """
        Returns the name of the image.

        Returns:
            str: The image name.
        """

        return self._name

    @property
    def path(self) -> Path:
        """
        Returns the path of the image.

        Returns:
            Path: The path of the image.
        """

        return self._path

    @property
    def type_(self) -> str:
        """
        Returns the type of the model (IMAGE).

        Returns:
            str: The model type string.
        """

        return self._metadata.type_

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp of the last update.

        Returns:
            datetime: The last update timestamp.
        """

        return self._metadata.updated_at

    @property
    def updated_on(self) -> date:
        """
        Returns the date of the last update.

        Returns:
            date: The last update date.
        """

        return self._metadata.updated_on

    @property
    def uuid_(self) -> uuid.UUID:
        """
        Returns the universally unique identifier (UUID) of the image.

        Returns:
            uuid.UUID: The instance's UUID.
        """

        return self._identifiable.uuid_

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the model.

        Args:
            None

        Returns:
            dict[str, Any]: The dictionary representation of the model.
        """

        return _convert_to_dict(self)


class ModelIdentifiable:
    """
    Provides identification properties for a model dictionary.

    This class handles the unique identity of an object by managing its
    database ID, a human-readable or system-generated key, and a
    universally unique identifier (UUID).
    """

    def __init__(
        self,
        id_: Optional[Union[int, str]] = None,
        key: Optional[str] = None,
        uuid_: Optional[uuid.UUID] = None,
    ) -> None:
        """
        Initializes the ModelIdentifiable instance.

        Args:
            id_ (Optional[Union[int, str]]): The internal database ID.
                Defaults to None for new entries.
            key (Optional[str]): A unique string identifier for the model
                (e.g., 'FLASHCARD_1'). Defaults to None.
            uuid_ (Optional[uuid.UUID]): A unique UUID for the instance.
                If None, a new UUID4 will be generated.

        Returns:
            None
        """

        self._id: Final[Union[int, str]] = id_
        self._key: Final[str] = key
        self._uuid: Final[uuid.UUID] = uuid.UUID(uuid_) if exists(value=uuid_) else generate_uuid4()

    @property
    def id_(self) -> Optional[Union[int, str]]:
        """
        Returns the internal database ID of the model.

        Returns:
            Optional[Union[int, str]]: The database ID if assigned, otherwise None.
        """

        return self._id

    @property
    def key(self) -> Optional[str]:
        """
        Returns the unique string identifier (key) of the model.

        Returns:
            Optional[str]: The model key if assigned, otherwise None.
        """

        return self._key

    @property
    def uuid_(self) -> uuid.UUID:
        """
        Returns the universally unique identifier (UUID) of the model.

        Returns:
            uuid.UUID: The instance's UUID.
        """

        return self._uuid

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the model.

        Args:
            None

        Returns:
            dict[str, Any]: The dictionary representation of the model.
        """

        return _convert_to_dict(self)


class ModelMetadata:
    """
    Represents the metadata associated with a model dictionary.

    This class manages timestamps (creation and update dates/times),
    the model type, and any additional dynamic fields. It ensures
    that essential metadata is initialized either from provided values
    or using system defaults.
    """

    def __init__(
        self,
        type_: str,
        created_at: Optional[datetime] = None,
        created_on: Optional[date] = None,
        fields: Optional[dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        updated_on: Optional[date] = None,
    ) -> None:
        """
        Initializes the ModelMetadata instance.

        Args:
            type_ (str): The type of the model (e.g., 'STACK', 'FLASHCARD').
            created_at (Optional[datetime]): The exact date and time of creation.
                Defaults to current system time if None.
            created_on (Optional[date]): The date of creation.
                Defaults to today's date if None.
            fields (Optional[dict[str, Any]]): A dictionary of additional metadata fields.
                Defaults to a structure with empty values and zero total.
            updated_at (Optional[datetime]): The exact date and time of the last update.
                Defaults to current system time if None.
            updated_on (Optional[date]): The date of the last update.
                Defaults to today's date if None.

        Returns:
            None
        """

        self._created_at: Final[datetime] = (
            datetime_from_string(string=created_at) if exists(value=created_at) else get_now()
        )
        self._created_on: Final[date] = (
            date_from_string(string=created_on) if exists(value=created_on) else get_today()
        )
        self._fields: Final[dict[str, Any]] = (
            fields
            if exists(value=fields)
            else {
                "values": [],
                "total": 0,
            }
        )
        self._type: Final[str] = type_.upper()
        self._updated_at: Final[datetime] = (
            datetime_from_string(string=updated_at) if exists(value=updated_at) else get_now()
        )
        self._updated_on: Final[date] = (
            date_from_string(string=updated_on) if exists(value=updated_on) else get_today()
        )

    @property
    def created_at(self) -> datetime:
        """
        Returns the exact date and time when the model was created.

        Returns:
            datetime: The creation timestamp.
        """

        return self._created_at

    @property
    def created_on(self) -> date:
        """
        Returns the date when the model was created.

        Returns:
            date: The creation date.
        """

        return self._created_on

    @property
    def fields(self) -> dict[str, Any]:
        """
        Returns a copy of the additional metadata fields.

        Returns:
            dict[str, Any]: A dictionary containing dynamic metadata fields.
        """

        return dict(self._fields)

    @property
    def type_(self) -> str:
        """
        Returns the type of the model.

        Returns:
            str: The model type in uppercase.
        """

        return self._type

    @property
    def updated_at(self) -> datetime:
        """
        Returns the exact date and time of the last update.

        Returns:
            datetime: The last update timestamp.
        """

        return self._updated_at

    @property
    def updated_on(self) -> date:
        """
        Returns the date of the last update.

        Returns:
            date: The last update date.
        """

        return self._updated_on

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the model.

        Args:
            None

        Returns:
            dict[str, Any]: The dictionary representation of the model.
        """

        return _convert_to_dict(self)


class Note:
    """
    Represents a note entity within the application.

    Notes provide a way to store additional text-based information or remarks
    associated with other entities. This class utilizes composition by
    incorporating ModelIdentifiable for identity management and ModelMetadata
    for tracking lifecycle details.
    """

    def __init__(
        self,
        text: str,
        title: str,
        author: Optional[str] = None,
        created_at: Optional[datetime] = None,
        created_on: Optional[date] = None,
        customfields: Optional[list[dict[str, Any]]] = None,
        difficulty: Optional[str] = None,
        id_: Optional[Union[int, str]] = None,
        is_assigned_to_stack: bool = False,
        key: Optional[str] = None,
        last_viewed_at: Optional[datetime] = None,
        last_viewed_on: Optional[datetime] = None,
        next_view_on: Optional[date] = None,
        priority: Optional[str] = None,
        subject: Optional[str] = None,
        tags: Optional[list[str]] = None,
        teacher: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        updated_on: Optional[date] = None,
        uuid_: Optional[uuid.UUID] = None,
    ) -> None:
        """
        Initializes a Note instance.

        Args:
            value (str): The text content of the note.
            created_at (Optional[datetime]): Specific timestamp of creation.
            created_on (Optional[date]): Specific date of creation.
            id_ (Optional[Union[int, str]]): Database ID for the entity.
            key (Optional[str]): Unique model key identifier.
            updated_at (Optional[datetime]): Timestamp of the last update.
            updated_on (Optional[date]): Date of the last update.
            uuid_ (Optional[uuid.UUID]): Universally unique identifier.

        Returns:
            None
        """
        self._author: Optional[str] = author
        self._customfields: list[dict[str, Any]] = customfields or []
        self._difficulty: Optional[str] = difficulty
        self._identifiable: Final[ModelIdentifiable] = ModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._is_assigned_to_stack: bool = is_assigned_to_stack
        self._last_viewed_at: Optional[datetime] = last_viewed_at
        self._last_viewed_on: Optional[datetime] = last_viewed_on
        self._metadata: Final[ModelMetadata] = ModelMetadata(
            created_at=created_at,
            created_on=created_on,
            fields={
                "total": len(list(locals().keys())),
                "values": list(locals().keys()),
            },
            type_="NOTE",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._next_view_on: Optional[date] = next_view_on
        self._priority: Optional[str] = priority
        self._subject: Optional[str] = subject
        self._tags: list[str] = tags or []
        self._teacher: Optional[str] = teacher
        self._text: str = text
        self._title: str = title

    @property
    def author(self) -> Optional[str]:
        """
        Returns the author of the note.

        Returns:
            Optional[str]: The name or identifier of the note's author.
        """

        return self._author

    @author.setter
    def author(
        self,
        value: str,
    ) -> None:
        self._author = value

    @property
    def created_at(self) -> datetime:
        """
        Returns the exact date and time when the note was created.

        Returns:
            datetime: The creation timestamp.
        """

        return self._metadata.created_at

    @property
    def created_on(self) -> date:
        """
        Returns the date when the note was created.

        Returns:
            date: The creation date.
        """

        return self._metadata.created_on

    @property
    def customfields(self) -> list[dict[str, Any]]:
        """
        Returns the list of custom fields associated with the note.

        Returns:
            list[dict[str, Any]]: A list containing custom data dictionaries.
        """

        return self._customfields

    @customfields.setter
    def customfields(
        self,
        value: Union[
            dict[str, Any],
            list[dict[str, Any]],
        ],
    ) -> None:
        if isinstance(
            value,
            dict,
        ):
            self._customfields.append(value)

            return

        self._customfields.extend(value)

    @property
    def difficulty(self) -> Optional[str]:
        """
        Returns the difficulty key of the note.

        Returns:
            Optional[str]: The internal key representing the difficulty level.
        """

        return self._difficulty

    @difficulty.setter
    def difficulty(
        self,
        value: str,
    ) -> None:
        self._difficulty = value

    @property
    def fields(self) -> dict[str, Any]:
        """
        Returns a copy of the dynamic metadata fields from the metadata component.

        Returns:
            dict[str, Any]: A dictionary containing additional metadata field information.
        """

        return dict(self._metadata.fields)

    @property
    def id_(self) -> Optional[Union[int, str]]:
        """
        Returns the internal database ID of the note.

        Returns:
            Optional[Union[int, str]]: The database ID if assigned, otherwise None.
        """

        return self._identifiable.id_

    @property
    def is_assigned_to_stack(self) -> bool:
        """
        Returns whether the note is currently assigned to a stack.

        Returns:
            bool: True if assigned, False otherwise.
        """

        return self._is_assigned_to_stack

    @is_assigned_to_stack.setter
    def is_assigned_to_stack(
        self,
        value: bool,
    ) -> None:
        self._is_assigned_to_stack = value

    @property
    def key(self) -> Optional[str]:
        """
        Returns the unique string identifier (key) of the note.

        Returns:
            Optional[str]: The model key if assigned, otherwise None.
        """
        return self._identifiable.key

    @property
    def last_viewed_at(self) -> Optional[datetime]:
        return self._last_viewed_at

    @last_viewed_at.setter
    def last_viewed_at(
        self,
        value: datetime,
    ) -> None:
        """
        Returns the timestamp when the note was last viewed.

        Returns:
            Optional[datetime]: The last viewing timestamp if available.
        """

        self._last_viewed_at = value

    @property
    def next_view_on(self) -> Optional[date]:
        """
        Returns the date when the note was last viewed.

        Returns:
            Optional[date]: The last viewing date if available.
        """

        return self._next_view_on

    @next_view_on.setter
    def next_view_on(self, value: Optional[date]) -> None:
        """
        Returns the date for the next scheduled review of the note.

        Returns:
            Optional[date]: The scheduled date for the next rehearsal.
        """

        self._next_view_on = value

    @property
    def priority(self) -> Optional[str]:
        """
        Returns the priority key of the note.

        Returns:
            Optional[str]: The internal key representing the priority level.
        """

        return self._priority

    @priority.setter
    def priority(
        self,
        value: str,
    ) -> None:
        self._priority = value

    @property
    def subject(self) -> Optional[str]:
        """
        Returns the subject key associated with the note.

        Returns:
            Optional[str]: The internal key for the associated subject.
        """

        return self._subject

    @subject.setter
    def subject(
        self,
        value: str,
    ) -> None:
        self._subject = value

    @property
    def tags(self) -> list[str]:
        """
        Returns the list of tags associated with the note.

        Returns:
            list[str]: A list of tag strings.
        """

        return self._tags

    @tags.setter
    def tags(
        self,
        value: list[str],
    ) -> None:
        self._tags = value

    @property
    def teacher(self) -> Optional[str]:
        """
        Returns the teacher key associated with the note.

        Returns:
            Optional[str]: The internal key for the associated teacher.
        """

        return self._teacher

    @teacher.setter
    def teacher(
        self,
        value: str,
    ) -> None:
        self._teacher = value

    @property
    def text(self) -> str:
        """
        Returns the text body of the note.

        Returns:
            str: The text or content of the note.
        """

        return self._text

    @text.setter
    def text(
        self,
        value: str,
    ) -> None:
        self._text = value

    @property
    def title(self) -> str:
        """
        Returns the title of the note.

        Returns:
            str: The title of the note.
        """

        return self._title

    @title.setter
    def title(
        self,
        value: str,
    ) -> None:
        self._title = value

    @property
    def type_(self) -> str:
        """
        Returns the type of the model (NOTE).

        Returns:
            str: The model type string.
        """

        return self._metadata.type_

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp of the last update.

        Returns:
            datetime: The last update timestamp.
        """

        return self._metadata.updated_at

    @property
    def updated_on(self) -> date:
        """
        Returns the date of the last update.

        Returns:
            date: The last update date.
        """

        return self._metadata.updated_on

    @property
    def uuid_(self) -> uuid.UUID:
        """
        Returns the universally unique identifier (UUID) of the note.

        Returns:
            uuid.UUID: The instance's UUID.
        """

        return self._identifiable.uuid_

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the model.

        Args:
            None

        Returns:
            dict[str, Any]: The dictionary representation of the model.
        """

        return _convert_to_dict(self)


class Option:
    """
    Represents an individual option within a customfield or setting.

    This class holds the content of an option and tracks whether it is
    the correct choice. Like other models in the system, it maintains
    identity through ModelIdentifiable and lifecycle data via ModelMetadata.
    """

    def __init__(
        self,
        value: Any,
        created_at: Optional[datetime] = None,
        created_on: Optional[date] = None,
        id_: Optional[Union[int, str]] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        updated_on: Optional[date] = None,
        uuid_: Optional[uuid.UUID] = None,
    ) -> None:
        """
        Initializes an Option instance.

        Args:
            value (Any): The value of the option.
            created_at (Optional[datetime]): Specific timestamp of creation.
            created_on (Optional[date]): Specific date of creation.
            id_ (Optional[Union[int, str]]): Database ID for the entity.
            key (Optional[str]): Unique model key identifier.
            updated_at (Optional[datetime]): Timestamp of the last update.
            updated_on (Optional[date]): Date of the last update.
            uuid_ (Optional[uuid.UUID]): Universally unique identifier.

        Returns:
            None
        """

        self._identifiable: Final[ModelIdentifiable] = ModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._metadata: Final[ModelMetadata] = ModelMetadata(
            created_at=created_at,
            created_on=created_on,
            fields={
                "total": len(list(locals().keys())),
                "values": list(locals().keys()),
            },
            type_="OPTION",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._value: Any = value

    @property
    def created_at(self) -> datetime:
        """
        Returns the exact date and time when the option was created.

        Returns:
            datetime: The creation timestamp.
        """

        return self._metadata.created_at

    @property
    def created_on(self) -> date:
        """
        Returns the date when the option was created.

        Returns:
            date: The creation date.
        """

        return self._metadata.created_on

    @property
    def fields(self) -> dict[str, Any]:
        """
        Returns a copy of the dynamic metadata fields from the metadata component.

        Returns:
            dict[str, Any]: A dictionary containing additional metadata field information.
        """

        return dict(self._metadata.fields)

    @property
    def id_(self) -> Optional[Union[int, str]]:
        """
        Returns the internal database ID of the option.

        Returns:
            Optional[Union[int, str]]: The database ID if assigned, otherwise None.
        """

        return self._identifiable.id_

    @property
    def key(self) -> Optional[str]:
        """
        Returns the unique string identifier (key) of the option.

        Returns:
            Optional[str]: The model key if assigned, otherwise None.
        """
        return self._identifiable.key

    @property
    def type_(self) -> str:
        """
        Returns the type of the model (OPTION).

        Returns:
            str: The model type string.
        """

        return self._metadata.type_

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp of the last update.

        Returns:
            datetime: The last update timestamp.
        """

        return self._metadata.updated_at

    @property
    def updated_on(self) -> date:
        """
        Returns the date of the last update.

        Returns:
            date: The last update date.
        """

        return self._metadata.updated_on

    @property
    def uuid_(self) -> uuid.UUID:
        """
        Returns the universally unique identifier (UUID) of the option.

        Returns:
            uuid.UUID: The instance's UUID.
        """

        return self._identifiable.uuid_

    @property
    def value(self) -> Any:
        """
        Returns the value of the option.

        Returns:
            float: The value of the option.
        """

        return self._value

    @value.setter
    def value(
        self,
        value: Any,
    ) -> None:
        self._value = value

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the model.

        Args:
            None

        Returns:
            dict[str, Any]: The dictionary representation of the model.
        """

        return _convert_to_dict(self)


class Priority:
    """
    Represents a priority level entity within the application.

    This class defines the complexity of learning materials using a display name,
    an internal name, and a numerical value. It utilizes composition for
    identification and metadata management.
    """

    def __init__(
        self,
        display_name: str,
        name: str,
        value: float,
        created_at: Optional[datetime] = None,
        created_on: Optional[date] = None,
        id_: Optional[Union[int, str]] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        updated_on: Optional[date] = None,
        uuid_: Optional[uuid.UUID] = None,
    ) -> None:
        """
        Initializes a Priority instance.

        Args:
            display_name (str): The human-readable name of the priority level.
            name (str): The internal technical name of the priority level.
            value (float): The numerical weight or value of this priority.
            created_at (Optional[datetime]): Specific timestamp of creation.
            created_on (Optional[date]): Specific date of creation.
            id_ (Optional[Union[int, str]]): Database ID for the entity.
            key (Optional[str]): Unique model key identifier.
            updated_at (Optional[datetime]): Timestamp of the last update.
            updated_on (Optional[date]): Date of the last update.
            uuid_ (Optional[uuid.UUID]): Universally unique identifier.

        Returns:
            None
        """

        self._display_name: Final[str] = display_name
        self._identifiable: Final[ModelIdentifiable] = ModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._metadata: Final[ModelMetadata] = ModelMetadata(
            created_at=created_at,
            created_on=created_on,
            fields={
                "total": len(list(locals().keys())),
                "values": list(locals().keys()),
            },
            type_="PRIORITY",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._name: Final[str] = name
        self._value: Final[float] = value

    @property
    def created_at(self) -> datetime:
        """
        Returns the exact date and time when the priority was created.

        Returns:
            datetime: The creation timestamp.
        """

        return self._metadata.created_at

    @property
    def created_on(self) -> date:
        """
        Returns the date when the priority was created.

        Returns:
            date: The creation date.
        """

        return self._metadata.created_on

    @property
    def display_name(self) -> str:
        """
        Returns the display name of the priority.

        Returns:
            str: The display name of the priority.
        """

        return self._display_name

    @property
    def fields(self) -> dict[str, Any]:
        """
        Returns a copy of the dynamic metadata fields from the metadata component.

        Returns:
            dict[str, Any]: A dictionary containing additional metadata field information.
        """

        return dict(self._metadata.fields)

    @property
    def id_(self) -> Optional[Union[int, str]]:
        """
        Returns the internal database ID of the priority.

        Returns:
            Optional[Union[int, str]]: The database ID if assigned, otherwise None.
        """

        return self._identifiable.id_

    @property
    def key(self) -> Optional[str]:
        """
        Returns the unique string identifier (key) of the priority.

        Returns:
            Optional[str]: The model key if assigned, otherwise None.
        """
        return self._identifiable.key

    @property
    def name(self) -> str:
        """
        Returns the name of the priority.

        Returns:
            str: The name of the priority.
        """

        return self._name

    @property
    def type_(self) -> str:
        """
        Returns the type of the model (PRIORITY).

        Returns:
            str: The model type string.
        """

        return self._metadata.type_

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp of the last update.

        Returns:
            datetime: The last update timestamp.
        """

        return self._metadata.updated_at

    @property
    def updated_on(self) -> date:
        """
        Returns the date of the last update.

        Returns:
            date: The last update date.
        """

        return self._metadata.updated_on

    @property
    def uuid_(self) -> uuid.UUID:
        """
        Returns the universally unique identifier (UUID) of the priority.

        Returns:
            uuid.UUID: The instance's UUID.
        """

        return self._identifiable.uuid_

    @property
    def value(self) -> float:
        """
        Returns the value of the priority.

        Returns:
            float: The value of the priority.
        """

        return self._value

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the model.

        Args:
            None

        Returns:
            dict[str, Any]: The dictionary representation of the model.
        """

        return _convert_to_dict(self)


class Question:
    """
    Represents a question entity within the application.

    A question typically consists of the inquiry text and is associated with
    various metadata such as difficulty, priority, and organizational attributes
    like tags, subjects, and teachers. This class utilizes composition by
    incorporating ModelIdentifiable for identity management and ModelMetadata
    for tracking lifecycle details.
    """

    def __init__(
        self,
        text: str,
        answers: Optional[list[str]] = None,
        author: Optional[str] = None,
        created_at: Optional[datetime] = None,
        created_on: Optional[date] = None,
        customfields: Optional[list[dict[str, Any]]] = None,
        difficulty: Optional[str] = None,
        id_: Optional[Union[int, str]] = None,
        is_assigned_to_stack: bool = False,
        key: Optional[str] = None,
        last_viewed_at: Optional[datetime] = None,
        last_viewed_on: Optional[datetime] = None,
        next_view_on: Optional[date] = None,
        priority: Optional[str] = None,
        subject: Optional[str] = None,
        tags: Optional[list[str]] = None,
        teacher: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        updated_on: Optional[date] = None,
        uuid_: Optional[uuid.UUID] = None,
    ) -> None:
        """
        Initializes a Question instance.

        Args:
            text (str): The actual text content of the question.
            author (Optional[str]): The creator of the question.
            created_at (Optional[datetime]): Specific timestamp of creation.
            created_on (Optional[date]): Specific date of creation.
            customfields (Optional[list[dict[str, Any]]]): List of custom data fields.
            difficulty (Optional[str]): Difficulty level key.
            id_ (Optional[Union[int, str]]): Database ID for the entity.
            is_assigned_to_stack (bool): Whether the question belongs to a stack.
            key (Optional[str]): Unique model key identifier.
            last_viewed_at (Optional[datetime]): Last time the question was seen.
            last_viewed_on (Optional[datetime]): Last date the question was seen.
            next_view_on (Optional[date]): Scheduled date for next review.
            priority (Optional[str]): Priority level key.
            subject (Optional[str]): Associated subject key.
            tags (Optional[list[str]]): List of associated tags.
            teacher (Optional[str]): Associated teacher key.
            updated_at (Optional[datetime]): Timestamp of the last update.
            updated_on (Optional[date]): Date of the last update.
            uuid_ (Optional[uuid.UUID]): Universally unique identifier.

        Returns:
            None
        """

        self._answers: Optional[list[str]] = answers or []
        self._author: Optional[str] = author
        self._customfields: Optional[list[dict[str, Any]]] = customfields or []
        self._difficulty: Final[Optional[str]] = difficulty
        self._identifiable: Final[ModelIdentifiable] = ModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._metadata: Final[ModelMetadata] = ModelMetadata(
            created_at=created_at,
            created_on=created_on,
            fields={
                "total": len(list(locals().keys())),
                "values": list(locals().keys()),
            },
            type_="QUESTION",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._priority: Optional[str] = priority
        self._subject: Optional[str] = subject
        self._tags: Optional[list[str]] = tags
        self._teacher: Optional[str] = teacher
        self._text: Final[str] = text

    @property
    def author(self) -> Optional[str]:
        """
        Returns the author of the question.

        Returns:
            Optional[str]: The name or identifier of the question's author.
        """
        return self._author

    @author.setter
    def author(
        self,
        value: str,
    ) -> None:
        self._author = value

    @property
    def created_at(self) -> datetime:
        """
        Returns the exact date and time when the question was created.

        Returns:
            datetime: The creation timestamp.
        """
        return self._metadata.created_at

    @property
    def created_on(self) -> date:
        """
        Returns the date when the question was created.

        Returns:
            date: The creation date.
        """
        return self._metadata.created_on

    @property
    def customfields(self) -> list[dict[str, Any]]:
        """
        Returns the list of custom fields associated with the question.

        Returns:
            list[dict[str, Any]]: A list containing custom data dictionaries.
        """
        return self._customfields

    @customfields.setter
    def customfields(
        self,
        value: Union[
            dict[str, Any],
            list[dict[str, Any]],
        ],
    ) -> None:
        if isinstance(
            value,
            dict,
        ):
            self._customfields.append(value)
            return

        self._customfields.extend(value)

    @property
    def difficulty(self) -> Optional[str]:
        """
        Returns the difficulty key of the question.

        Returns:
            Optional[str]: The internal key representing the difficulty level.
        """
        return self._difficulty

    @difficulty.setter
    def difficulty(
        self,
        value: str,
    ) -> None:
        self._difficulty = value

    @property
    def fields(self) -> dict[str, Any]:
        """
        Returns a copy of the dynamic metadata fields from the metadata component.

        Returns:
            dict[str, Any]: A dictionary containing additional metadata field information.
        """
        return dict(self._metadata.fields)

    @property
    def id_(self) -> Optional[Union[int, str]]:
        """
        Returns the internal database ID of the question.

        Returns:
            Optional[Union[int, str]]: The database ID if assigned, otherwise None.
        """
        return self._identifiable.id_

    @property
    def is_assigned_to_stack(self) -> bool:
        """
        Returns whether the question is currently assigned to a stack.

        Returns:
            bool: True if assigned, False otherwise.
        """
        return self._is_assigned_to_stack

    @is_assigned_to_stack.setter
    def is_assigned_to_stack(
        self,
        value: bool,
    ) -> None:
        self._is_assigned_to_stack = value

    @property
    def key(self) -> Optional[str]:
        """
        Returns the unique string identifier (key) of the question.

        Returns:
            Optional[str]: The model key if assigned, otherwise None.
        """
        return self._identifiable.key

    @property
    def last_viewed_at(self) -> Optional[datetime]:
        """
        Returns the timestamp when the question was last viewed.

        Returns:
            Optional[datetime]: The last viewing timestamp if available.
        """
        return self._last_viewed_at

    @last_viewed_at.setter
    def last_viewed_at(
        self,
        value: datetime,
    ) -> None:
        self._last_viewed_at = value

    @property
    def next_view_on(self) -> Optional[date]:
        """
        Returns the date for the next scheduled review of the question.

        Returns:
            Optional[date]: The scheduled date for the next rehearsal.
        """
        return self._next_view_on

    @next_view_on.setter
    def next_view_on(
        self,
        value: date,
    ) -> None:
        self._next_view_on = value

    @property
    def priority(self) -> Optional[str]:
        """
        Returns the priority key of the question.

        Returns:
            Optional[str]: The internal key representing the priority level.
        """
        return self._priority

    @priority.setter
    def priority(
        self,
        value: str,
    ) -> None:
        self._priority = value

    @property
    def subject(self) -> Optional[str]:
        """
        Returns the subject key associated with the question.

        Returns:
            Optional[str]: The internal key for the associated subject.
        """
        return self._subject

    @subject.setter
    def subject(
        self,
        value: str,
    ) -> None:
        self._subject = value

    @property
    def tags(self) -> list[str]:
        """
        Returns the list of tags associated with the question.

        Returns:
            list[str]: A list of tag strings.
        """
        return self._tags

    @tags.setter
    def tags(
        self,
        value: list[str],
    ) -> None:
        self._tags = value

    @property
    def teacher(self) -> Optional[str]:
        """
        Returns the teacher key associated with the question.

        Returns:
            Optional[str]: The internal key for the associated teacher.
        """
        return self._teacher

    @teacher.setter
    def teacher(
        self,
        value: str,
    ) -> None:
        self._teacher = value

    @property
    def text(self) -> str:
        """
        Returns the text of the question.

        Returns:
            str: The question text.
        """
        return self._text

    @text.setter
    def text(
        self,
        value: str,
    ) -> None:
        self._text = value

    @property
    def type_(self) -> str:
        """
        Returns the type of the model (QUESTION).

        Returns:
            str: The model type string.
        """
        return self._metadata.type_

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp of the last update.

        Returns:
            datetime: The last update timestamp.
        """
        return self._metadata.updated_at

    @property
    def updated_on(self) -> date:
        """
        Returns the date of the last update.

        Returns:
            date: The last update date.
        """
        return self._metadata.updated_on

    @property
    def uuid_(self) -> uuid.UUID:
        """
        Returns the universally unique identifier (UUID) of the question.

        Returns:
            uuid.UUID: The instance's UUID.
        """
        return self._identifiable.uuid_

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the model.

        Args:
            None

        Returns:
            dict[str, Any]: The dictionary representation of the model.
        """

        return _convert_to_dict(self)


class RehearsalAction:
    """
    Represents a single performed action within a study session.

    This class captures the interaction logic when a user engages with a
    specific item (like a Flashcard or Question). It records the performance
    metrics, specifically the result and the duration of the action, and
    provides the necessary metadata to track the study progress.
    """

    def __init__(
        self,
        action_data: dict[str, Any],
        message: str,
        timestamp: datetime,
        created_at: Optional[datetime] = None,
        created_on: Optional[date] = None,
        id_: Optional[Union[int, str]] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        updated_on: Optional[date] = None,
        uuid_: Optional[uuid.UUID] = None,
    ) -> None:
        """
        Initializes a RehearsalAction instance.

        Args:
            item (str): The key of the model being practiced.
            rehearsal_run (str): The key of the RehearsalRun this action belongs to.
            author (Optional[str]): The identifier of the user performing the action.
            created_at (Optional[datetime]): Specific timestamp of creation.
            created_on (Optional[date]): Specific date of creation.
            customfields (Optional[list[dict[str, Any]]]): Custom metadata for this action.
            duration (Optional[int]): Time spent on this action in seconds.
            id_ (Optional[Union[int, str]]): Database ID for the entity.
            key (Optional[str]): Unique model key identifier for the action itself.
            result (Optional[str]): The outcome of the action (e.g., success level).
            updated_at (Optional[datetime]): Timestamp of the last update.
            updated_on (Optional[date]): Date of the last update.
            uuid_ (Optional[uuid.UUID]): Universally unique identifier.

        Returns:
            None
        """

        self._action_data: Final[dict[str, Any]] = action_data
        self._identifiable: Final[ModelIdentifiable] = ModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._message: Final[str] = message
        self._metadata: Final[ModelMetadata] = ModelMetadata(
            created_at=created_at,
            created_on=created_on,
            fields={
                "total": len(list(locals().keys())),
                "values": list(locals().keys()),
            },
            type_="REHEARSAL_ACTION",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._timestamp: Final[datetime] = timestamp

    @property
    def action_data(self) -> dict[str, Any]:
        """
        Returns the action data of the rehearsal action.

        Returns:
            dict[str, Any]: The action data.
        """
        return dict(self._action_data)

    @property
    def created_at(self) -> datetime:
        """
        Returns the exact date and time when the rehearsal action was created.

        Returns:
            datetime: The creation timestamp.
        """
        return self._metadata.created_at

    @property
    def created_on(self) -> date:
        """
        Returns the date when the rehearsal action was created.

        Returns:
            date: The creation date.
        """
        return self._metadata.created_on

    @property
    def id_(self) -> Optional[Union[int, str]]:
        """
        Returns the internal database ID of the rehearsal action.

        Returns:
            Optional[Union[int, str]]: The database ID if assigned, otherwise None.
        """
        return self._identifiable.id_

    @property
    def key(self) -> Optional[str]:
        """
        Returns the unique string identifier (key) of the rehearsal action.

        Returns:
            Optional[str]: The model key if assigned, otherwise None.
        """
        return self._identifiable.key

    @property
    def message(self) -> str:
        """
        Returns the message of the rehearsal action.

        Returns:
            str: The message.
        """
        return self._message

    @property
    def timestamp(self) -> datetime:
        """
        Returns the timestamp of the rehearsal action.

        Returns:
            datetime: The timestamp.
        """
        return self._timestamp

    @property
    def type_(self) -> str:
        """
        Returns the type of the model (REHEARSAL_ACTION).

        Returns:
            str: The model type string.
        """
        return self._metadata.type_

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp of the last update.

        Returns:
            datetime: The last update timestamp.
        """
        return self._metadata.updated_at

    @property
    def updated_on(self) -> date:
        """
        Returns the date of the last update.

        Returns:
            date: The last update date.
        """
        return self._metadata.updated_on

    @property
    def uuid_(self) -> uuid.UUID:
        """
        Returns the universally unique identifier (UUID) of the rehearsal action.

        Returns:
            uuid.UUID: The instance's UUID.
        """
        return self._identifiable.uuid_

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the model.

        Args:
            None

        Returns:
            dict[str, Any]: The dictionary representation of the model.
        """

        return _convert_to_dict(self)


class RehearsalRunItem:
    """
    Represents an individual item within a rehearsal session.

    This class serves as a link between a specific rehearsal run and the
    actual content being reviewed (e.g., a flashcard or question). It tracks
    the result of the rehearsal action, the timing of the response, and
    maintains its own identity and metadata for audit trails.
    """

    def __init__(
        self,
        item: str,
        actions: Optional[list[str]] = None,
        completed_at: Optional[datetime] = None,
        created_at: Optional[datetime] = None,
        created_on: Optional[date] = None,
        id_: Optional[Union[int, str]] = None,
        key: Optional[str] = None,
        result: Optional[str] = None,
        started_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        updated_on: Optional[date] = None,
        uuid_: Optional[uuid.UUID] = None,
    ) -> None:
        """
        Initializes a RehearsalRunItem instance.

        Args:
            item (str): The key of the model being rehearsed (e.g., Flashcard key).
            rehearsal_run (str): The key of the associated RehearsalRun.
            author (Optional[str]): The identifier of the user performing the action.
            created_at (Optional[datetime]): Specific timestamp of creation.
            created_on (Optional[date]): Specific date of creation.
            customfields (Optional[list[dict[str, Any]]]): Custom metadata for this action.
            duration (Optional[int]): Time spent on this item in seconds.
            id_ (Optional[Union[int, str]]): Database ID for the entity.
            key (Optional[str]): Unique model key identifier.
            result (Optional[str]): The outcome of the rehearsal (e.g., 'correct', 'wrong').
            updated_at (Optional[datetime]): Timestamp of the last update.
            updated_on (Optional[date]): Date of the last update.
            uuid_ (Optional[uuid.UUID]): Universally unique identifier.

        Returns:
            None
        """

        self._actions: list[str] = actions if exists(value=actions) else []
        self._completed_at: Optional[datetime] = completed_at
        self._identifiable: Final[ModelIdentifiable] = ModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._item: Final[str] = item
        self._metadata: Final[ModelMetadata] = ModelMetadata(
            created_at=created_at,
            created_on=created_on,
            fields={
                "total": len(list(locals().keys())),
                "values": list(locals().keys()),
            },
            type_="REHEARSAL_RUN_ITEM",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._result: Optional[str] = result
        self._started_at: Optional[datetime] = started_at

    @property
    def actions(self) -> list[str]:
        """
        Returns the actions taken during the rehearsal run item.

        Returns:
            list[str]: The actions taken.
        """
        return list(self._actions)

    @actions.setter
    def actions(
        self,
        value: Union[
            list[str],
            str,
        ],
    ) -> None:
        if isinstance(value, list):
            self._actions.extend(value)

            return

        self._actions.append(value)

    @property
    def completed_at(self) -> datetime:
        """
        Returns the exact date and time when the rehearsal run item was completed.

        Returns:
            datetime: The completion timestamp.
        """

        return self._completed_at

    @property
    def created_at(self) -> datetime:
        """
        Returns the exact date and time when the rehearsal run item was created.

        Returns:
            datetime: The creation timestamp.
        """
        return self._metadata.created_at

    @property
    def created_on(self) -> date:
        """
        Returns the date when the rehearsal run item was created.

        Returns:
            date: The creation date.
        """
        return self._metadata.created_on

    @property
    def id_(self) -> Optional[Union[int, str]]:
        """
        Returns the internal database ID of the rehearsal run item.

        Returns:
            Optional[Union[int, str]]: The database ID if assigned, otherwise None.
        """
        return self._identifiable.id_

    @property
    def item(self) -> str:
        """
        Returns the item associated with the rehearsal run item.

        Returns:
            str: The item.
        """
        return self._item

    @property
    def key(self) -> Optional[str]:
        """
        Returns the unique string identifier (key) of the rehearsal run item.

        Returns:
            Optional[str]: The model key if assigned, otherwise None.
        """
        return self._identifiable.key

    @property
    def result(self) -> Optional[str]:
        """
        Returns the result of the rehearsal run item.

        Returns:
            Optional[str]: The result.
        """
        return self._result

    @result.setter
    def result(
        self,
        value: str,
    ) -> None:
        self._result = value

    @property
    def started_at(self) -> datetime:
        """
        Returns the timestamp when the rehearsal run item was started.

        Returns:
            datetime: The start timestamp.
        """
        return self._started_at

    @started_at.setter
    def started_at(
        self,
        value: datetime,
    ) -> None:
        self._started_at = value

    @property
    def type_(self) -> str:
        """
        Returns the type of the model (REHEARSAL_RUN_ITEM).

        Returns:
            str: The model type string.
        """
        return self._metadata.type_

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp of the last update.

        Returns:
            datetime: The last update timestamp.
        """
        return self._metadata.updated_at

    @property
    def updated_on(self) -> date:
        """
        Returns the date of the last update.

        Returns:
            date: The last update date.
        """
        return self._metadata.updated_on

    @property
    def uuid_(self) -> uuid.UUID:
        """
        Returns the universally unique identifier (UUID) of the rehearsal run item.

        Returns:
            uuid.UUID: The instance's UUID.
        """
        return self._identifiable.uuid_

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the model.

        Args:
            None

        Returns:
            dict[str, Any]: The dictionary representation of the model.
        """

        return _convert_to_dict(self)


class RehearsalRun:
    """
    Represents a specific rehearsal session or study run.

    This class tracks the lifecycle of a study session, including its timing
    (scheduled, started, finished), its completion status, and the collection
    of items being practiced. It uses ModelIdentifiable for identity management
    and ModelMetadata for lifecycle tracking.
    """

    def __init__(
        self,
        stacks: list[str],
        configuration: dict[str, Any],
        author: Optional[str] = None,
        completed_at: Optional[datetime] = None,
        completed_on: Optional[date] = None,
        created_at: Optional[datetime] = None,
        created_on: Optional[date] = None,
        customfields: Optional[list[dict[str, Any]]] = None,
        duration: Optional[dict[str, float]] = None,
        id_: Optional[Union[int, str]] = None,
        is_finished: bool = False,
        items: Optional[dict[str, str]] = None,
        key: Optional[str] = None,
        scheduled_at: Optional[datetime] = None,
        scheduled_on: Optional[date] = None,
        started_at: Optional[datetime] = None,
        started_on: Optional[date] = None,
        updated_at: Optional[datetime] = None,
        updated_on: Optional[date] = None,
        uuid_: Optional[uuid.UUID] = None,
    ) -> None:
        """
        Initializes a RehearsalRun instance.

        Args:
            author (Optional[str]): The identifier of the user who created the run.
            created_at (Optional[datetime]): The exact timestamp of creation.
            created_on (Optional[date]): The date of creation.
            customfields (Optional[list[dict[str, Any]]]): A list of custom metadata fields.
            finished_at (Optional[datetime]): The timestamp when the rehearsal was completed.
            id_ (Optional[Union[int, str]]): The internal database ID.
            is_finished (bool): Indicates whether the rehearsal run is marked as completed.
            items (Optional[dict[str, str]]): A mapping of item keys to their corresponding order number included in this run.
            key (Optional[str]): The unique model key.
            scheduled_at (Optional[datetime]): The timestamp for which the run was planned.
            started_at (Optional[datetime]): The timestamp when the rehearsal actually began.
            updated_at (Optional[datetime]): The timestamp of the last modification.
            updated_on (Optional[date]): The date of the last modification.
            uuid_ (Optional[uuid.UUID]): The universally unique identifier.

        Returns:
            None
        """

        self._author: Optional[str] = author
        self._completed_at: Optional[datetime] = completed_at
        self._completed_on: Optional[datetime] = completed_on
        self._configuration: Final[dict[str, Any]] = configuration
        self._customfields: list[dict[str, Any]] = customfields or []
        self._duration: Optional[dict[str, float]] = duration or {}
        self._identifiable: Final[ModelIdentifiable] = ModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._is_finished: bool = is_finished
        self._items: list[dict[str, str]] = items or {}
        self._metadata: Final[ModelMetadata] = ModelMetadata(
            created_at=created_at,
            created_on=created_on,
            fields={
                "total": len(list(locals().keys())),
                "values": list(locals().keys()),
            },
            type_="REHEARSAL_RUN",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._scheduled_at: Optional[datetime] = scheduled_at
        self._scheduled_on: Optional[date] = scheduled_on
        self._started_at: Optional[datetime] = started_at
        self._started_on: Optional[date] = started_on

    @property
    def author(self) -> Optional[str]:
        """
        Returns the author of the rehearsal run.

        Returns:
            Optional[str]: The name or identifier of the author.
        """
        return self._author

    @author.setter
    def author(
        self,
        value: str,
    ) -> None:
        self._author = value

    @property
    def created_at(self) -> datetime:
        """
        Returns the exact date and time when the rehearsal run was created.

        Returns:
            datetime: The creation timestamp.
        """
        return self._metadata.created_at

    @property
    def created_on(self) -> date:
        """
        Returns the date when the rehearsal run was created.

        Returns:
            date: The creation date.
        """
        return self._metadata.created_on

    @property
    def customfields(self) -> list[dict[str, Any]]:
        """
        Returns the list of custom fields associated with the run.

        Returns:
            list[dict[str, Any]]: A list containing custom data dictionaries.
        """
        return self._customfields

    @customfields.setter
    def customfields(
        self,
        value: Union[
            dict[str, Any],
            list[dict[str, Any]],
        ],
    ) -> None:
        if isinstance(
            value,
            dict,
        ):
            self._customfields.append(value)

            return

        self._customfields.extend(value)

    @property
    def fields(self) -> dict[str, Any]:
        """
        Returns a copy of the dynamic metadata fields.

        Returns:
            dict[str, Any]: A dictionary containing additional metadata information.
        """
        return dict(self._metadata.fields)

    @property
    def finished_at(self) -> Optional[datetime]:
        """
        Returns the timestamp when the rehearsal was finished.

        Returns:
            Optional[datetime]: The completion timestamp if finished, otherwise None.
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(
        self,
        value: datetime,
    ) -> None:
        self._finished_at = value

    @property
    def id_(self) -> Optional[Union[int, str]]:
        """
        Returns the internal database ID of the rehearsal run.

        Returns:
            Optional[Union[int, str]]: The database ID if assigned, otherwise None.
        """
        return self._identifiable.id_

    @property
    def is_finished(self) -> bool:
        """
        Returns whether the rehearsal run is completed.

        Returns:
            bool: True if finished, False otherwise.
        """
        return self._is_finished

    @is_finished.setter
    def is_finished(
        self,
        value: bool,
    ) -> None:
        self._is_finished = value

    @property
    def items(self) -> dict[str, str]:
        """
        Returns the mapping of item keys (e.g., flashcards, questions) corresponding to their order number in this run.

        Returns:
            dict[str, str]: A mapping of item keys (e.g., flashcards, questions) corresponding to their order number in this run.
        """
        return self._items

    @items.setter
    def items(
        self,
        value: Union[list[dict[str, str]], dict[str, str]],
    ) -> None:
        if isinstance(
            value,
            list,
        ):
            self._items.extend(value)

            return

        self._items.append(value)

    @property
    def key(self) -> Optional[str]:
        """
        Returns the unique string identifier (key) of the rehearsal run.

        Returns:
            Optional[str]: The model key if assigned, otherwise None.
        """
        return self._identifiable.key

    @property
    def scheduled_at(self) -> Optional[datetime]:
        """
        Returns the timestamp for which the run was scheduled.

        Returns:
            Optional[datetime]: The scheduled timestamp.
        """
        return self._scheduled_at

    @scheduled_at.setter
    def scheduled_at(
        self,
        value: datetime,
    ) -> None:
        self._scheduled_at = value

    @property
    def started_at(self) -> Optional[datetime]:
        """
        Returns the timestamp when the rehearsal started.

        Returns:
            Optional[datetime]: The starting timestamp.
        """
        return self._started_at

    @started_at.setter
    def started_at(
        self,
        value: datetime,
    ) -> None:
        self._started_at = value

    @property
    def type_(self) -> str:
        """
        Returns the type of the model (REHEARSAL_RUN).

        Returns:
            str: The model type string.
        """
        return self._metadata.type_

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp of the last update.

        Returns:
            datetime: The last update timestamp.
        """
        return self._metadata.updated_at

    @property
    def updated_on(self) -> date:
        """
        Returns the date of the last update.

        Returns:
            date: The last update date.
        """
        return self._metadata.updated_on

    @property
    def uuid_(self) -> uuid.UUID:
        """
        Returns the universally unique identifier (UUID) of the rehearsal run.

        Returns:
            uuid.UUID: The instance's UUID.
        """
        return self._identifiable.uuid_

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the model.

        Args:
            None

        Returns:
            dict[str, Any]: The dictionary representation of the model.
        """

        return _convert_to_dict(self)


class Stack:
    """
    Represents a collection or container (stack) of study materials.

    A stack acts as an organizational unit that can group various models
    such as flashcards, questions, or notes. It manages metadata related
    to its content, such as the associated subject, teacher, and overall
    priority or difficulty, while providing tracking for its lifecycle
    through ModelMetadata.
    """

    def __init__(
        self,
        name: str,
        author: Optional[str] = None,
        children: Optional[list[str]] = None,
        created_at: Optional[datetime] = None,
        created_on: Optional[date] = None,
        customfields: Optional[list[dict[str, Any]]] = None,
        difficulty: Optional[str] = None,
        id_: Optional[Union[int, str]] = None,
        items: Optional[list[str]] = None,
        key: Optional[str] = None,
        parent: Optional[str] = None,
        priority: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        updated_on: Optional[date] = None,
        uuid_: Optional[uuid.UUID] = None,
    ) -> None:
        """
        Initializes a Stack instance.

        Args:
            name (str): The display name of the stack.
            author (Optional[str]): The creator of the stack.
            children (Optional[list[str]]): A list of keys representing the child stacks.
            created_at (Optional[datetime]): Specific timestamp of creation.
            created_on (Optional[date]): Specific date of creation.
            customfields (Optional[list[dict[str, Any]]]): List of custom data fields.
            difficulty (Optional[str]): Difficulty level key associated with this stack.
            id_ (Optional[Union[int, str]]): Database ID for the entity.
            key (Optional[str]): Unique model key identifier.
            last_viewed_at (Optional[datetime]): Last time the stack was accessed.
            last_viewed_on (Optional[date]): Last date the stack was accessed.
            next_view_on (Optional[date]): Scheduled date for next rehearsal of this stack.
            parent (Optional[str]): The key of the parent stack.
            priority (Optional[str]): Priority level key for the stack.
            subject (Optional[str]): Associated subject key.
            tags (Optional[list[str]]): List of associated tags for categorization.
            teacher (Optional[str]): Associated teacher key.
            updated_at (Optional[datetime]): Timestamp of the last update.
            updated_on (Optional[date]): Date of the last update.
            uuid_ (Optional[uuid.UUID]): Universally unique identifier.

        Returns:
            None
        """

        self._author: Optional[str] = author
        self._children: list[str] = children or []
        self._customfields: list[dict[str, Any]] = customfields or []
        self._identifiable: Final[ModelIdentifiable] = ModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._metadata: Final[ModelMetadata] = ModelMetadata(
            created_at=created_at,
            created_on=created_on,
            fields={
                "total": len(list(locals().keys())),
                "values": list(locals().keys()),
            },
            type_="STACK",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._name: str = name
        self._parent: Optional[str] = parent

    @property
    def author(self) -> Optional[str]:
        """
        Returns the author of the stack.

        Returns:
            Optional[str]: The name or identifier of the stack's author.
        """
        return self._author

    @author.setter
    def author(
        self,
        value: str,
    ) -> None:
        self._author = value

    @property
    def children(self) -> list[str]:
        """
        Returns the list of keys for the child stacks.

        Returns:
            list[str]: A list of keys representing sub-stacks.
        """
        return self._children

    @children.setter
    def children(
        self,
        value: Union[
            list[str],
            str,
        ],
    ) -> None:
        """
        Sets or appends child stack keys.

        Args:
            value (Union[list[str], str]): A single stack key or a list of keys.
        """
        if isinstance(
            value,
            list,
        ):
            self._children.extend(value)

            return

        self._children.append(value)

    @property
    def created_at(self) -> datetime:
        """
        Returns the exact date and time when the stack was created.

        Returns:
            datetime: The creation timestamp.
        """
        return self._metadata.created_at

    @property
    def created_on(self) -> date:
        """
        Returns the date when the stack was created.

        Returns:
            date: The creation date.
        """
        return self._metadata.created_on

    @property
    def customfields(self) -> list[dict[str, Any]]:
        """
        Returns the list of custom fields associated with the stack.

        Returns:
            list[dict[str, Any]]: A list containing custom data dictionaries.
        """
        return self._customfields

    @customfields.setter
    def customfields(
        self,
        value: Union[
            dict[str, Any],
            list[dict[str, Any]],
        ],
    ) -> None:
        if isinstance(value, dict):
            self._customfields.append(
                value,
            )
            return
        self._customfields.extend(value)

    @property
    def difficulty(self) -> Optional[str]:
        """
        Returns the difficulty key associated with the stack.

        Returns:
            Optional[str]: The internal key representing the difficulty level.
        """
        return self._difficulty

    @difficulty.setter
    def difficulty(
        self,
        value: str,
    ) -> None:
        self._difficulty = value

    @property
    def fields(self) -> dict[str, Any]:
        """
        Returns a copy of the dynamic metadata fields from the metadata component.

        Returns:
            dict[str, Any]: A dictionary containing additional metadata field information.
        """
        return dict(self._metadata.fields)

    @property
    def id_(self) -> Optional[Union[int, str]]:
        """
        Returns the internal database ID of the stack.

        Returns:
            Optional[Union[int, str]]: The database ID if assigned, otherwise None.
        """
        return self._identifiable.id_

    @property
    def key(self) -> Optional[str]:
        """
        Returns the unique string identifier (key) of the stack.

        Returns:
            Optional[str]: The model key if assigned, otherwise None.
        """
        return self._identifiable.key

    @property
    def last_viewed_at(self) -> Optional[datetime]:
        """
        Returns the timestamp when the stack was last accessed.

        Returns:
            Optional[datetime]: The last viewing timestamp if available.
        """
        return self._last_viewed_at

    @last_viewed_at.setter
    def last_viewed_at(
        self,
        value: datetime,
    ) -> None:
        self._last_viewed_at = value

    @property
    def name(self) -> str:
        """
        Returns the display name of the stack.

        Returns:
            str: The stack name.
        """
        return self._name

    @name.setter
    def name(
        self,
        value: str,
    ) -> None:
        self._name = value

    @property
    def next_view_on(self) -> Optional[date]:
        """
        Returns the date for the next scheduled rehearsal of the stack.

        Returns:
            Optional[date]: The scheduled date for the next rehearsal.
        """
        return self._next_view_on

    @next_view_on.setter
    def next_view_on(
        self,
        value: date,
    ) -> None:
        self._next_view_on = value

    @property
    def parent(self) -> Optional[str]:
        """
        Returns the key of the parent stack.

        Returns:
            Optional[str]: The key of the parent stack if assigned, otherwise None.
        """
        return self._parent

    @parent.setter
    def parent(
        self,
        value: str,
    ) -> None:
        """
        Sets the key of the parent stack.

        Args:
            value (str): The key to be set as parent.
        """
        self._parent = value

    @property
    def priority(self) -> Optional[str]:
        """
        Returns the priority key of the stack.

        Returns:
            Optional[str]: The internal key representing the priority level.
        """
        return self._priority

    @priority.setter
    def priority(
        self,
        value: str,
    ) -> None:
        self._priority = value

    @property
    def subject(self) -> Optional[str]:
        """
        Returns the subject key associated with the stack.

        Returns:
            Optional[str]: The internal key for the associated subject.
        """
        return self._subject

    @subject.setter
    def subject(
        self,
        value: str,
    ) -> None:
        self._subject = value

    @property
    def tags(self) -> list[str]:
        """
        Returns the list of tags associated with the stack.

        Returns:
            list[str]: A list of tag strings.
        """
        return self._tags

    @tags.setter
    def tags(
        self,
        value: list[str],
    ) -> None:
        self._tags = value

    @property
    def teacher(self) -> Optional[str]:
        """
        Returns the teacher key associated with the stack.

        Returns:
            Optional[str]: The internal key for the associated teacher.
        """
        return self._teacher

    @teacher.setter
    def teacher(
        self,
        value: str,
    ) -> None:
        self._teacher = value

    @property
    def type_(self) -> str:
        """
        Returns the type of the model (STACK).

        Returns:
            str: The model type string.
        """
        return self._metadata.type_

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp of the last update.

        Returns:
            datetime: The last update timestamp.
        """
        return self._metadata.updated_at

    @property
    def updated_on(self) -> date:
        """
        Returns the date of the last update.

        Returns:
            date: The last update date.
        """
        return self._metadata.updated_on

    @property
    def uuid_(self) -> uuid.UUID:
        """
        Returns the universally unique identifier (UUID) of the stack.

        Returns:
            uuid.UUID: The instance's UUID.
        """
        return self._identifiable.uuid_

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the model.

        Args:
            None

        Returns:
            dict[str, Any]: The dictionary representation of the model.
        """

        return _convert_to_dict(self)


class Subject:
    """
    Represents a subject entity within the application.

    Subjects are used to categorize educational content. This class utilizes
    composition by incorporating ModelIdentifiable for identity management
    and ModelMetadata for tracking creation and update details.
    """

    def __init__(
        self,
        name: str,
        created_at: Optional[datetime] = None,
        created_on: Optional[date] = None,
        customfields: Optional[list[dict[str, Any]]] = None,
        difficulty: Optional[str] = None,
        id_: Optional[Union[int, str]] = None,
        key: Optional[str] = None,
        priority: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        updated_on: Optional[date] = None,
        uuid_: Optional[uuid.UUID] = None,
    ) -> None:
        """
        Initializes a Subject instance.

        Args:
            name (str): The string name of the subject.
            created_at (Optional[datetime]): Specific timestamp of creation.
            created_on (Optional[date]): Specific date of creation.
            customfields (Optional[list[dict[str, Any]]]): List of custom data fields.
            difficulty (Optional[str]): Difficulty level key.
            id_ (Optional[Union[int, str]]): Database ID for the entity.
            key (Optional[str]): Unique model key identifier.
            priority (Optional[str]): Priority level key.
            updated_at (Optional[datetime]): Timestamp of the last update.
            updated_on (Optional[date]): Date of the last update.
            uuid_ (Optional[uuid.UUID]): Universally unique identifier.

        Returns:
            None
        """

        self._customfields: Optional[list[dict[str, Any]]] = customfields or []
        self._difficulty: Final[Optional[str]] = difficulty
        self._identifiable: Final[ModelIdentifiable] = ModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._metadata: Final[ModelMetadata] = ModelMetadata(
            created_at=created_at,
            created_on=created_on,
            fields={
                "total": len(list(locals().keys())),
                "values": list(locals().keys()),
            },
            type_="SUBJECT",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._name: Final[str] = name
        self._priority: Final[Optional[str]] = priority

    @property
    def created_at(self) -> datetime:
        """
        Returns the exact date and time when the subject was created.

        Returns:
            datetime: The creation timestamp.
        """

        return self._metadata.created_at

    @property
    def created_on(self) -> date:
        """
        Returns the date when the subject was created.

        Returns:
            date: The creation date.
        """

        return self._metadata.created_on

    @property
    def customfields(self) -> list[dict[str, Any]]:
        """
        Returns the list of custom fields associated with the subject.

        Returns:
            list[dict[str, Any]]: A list containing custom data dictionaries.
        """

        return self._customfields

    @customfields.setter
    def customfields(
        self,
        value: Union[
            dict[str, Any],
            list[dict[str, Any]],
        ],
    ) -> None:
        if isinstance(
            value,
            dict,
        ):
            self._customfields.append(value)

            return

        self._customfields.extend(value)

    @property
    def difficulty(self) -> Optional[str]:
        """
        Returns the difficulty key of the subject.

        Returns:
            Optional[str]: The internal key representing the difficulty level.
        """

        return self._difficulty

    @difficulty.setter
    def difficulty(
        self,
        value: str,
    ) -> None:
        self._difficulty = value

    @property
    def fields(self) -> dict[str, Any]:
        """
        Returns a copy of the dynamic metadata fields from the metadata component.

        Returns:
            dict[str, Any]: A dictionary containing additional metadata field information.
        """

        return dict(self._metadata.fields)

    @property
    def id_(self) -> Optional[Union[int, str]]:
        """
        Returns the internal database ID of the subject.

        Returns:
            Optional[Union[int, str]]: The database ID if assigned, otherwise None.
        """

        return self._identifiable.id_

    @property
    def key(self) -> Optional[str]:
        """
        Returns the unique string identifier (key) of the subject.

        Returns:
            Optional[str]: The model key if assigned, otherwise None.
        """
        return self._identifiable.key

    @property
    def name(self) -> str:
        """
        Returns the name of the subject.

        Returns:
            str: The name of the subject.
        """

        return self._name

    @property
    def priority(self) -> Optional[str]:
        """
        Returns the priority key of the subject.

        Returns:
            Optional[str]: The internal key representing the priority level.
        """

        return self._priority

    @priority.setter
    def priority(
        self,
        value: str,
    ) -> None:
        self._priority = value

    @property
    def type_(self) -> str:
        """
        Returns the type of the model (SUBJECT).

        Returns:
            str: The model type string.
        """

        return self._metadata.type_

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp of the last update.

        Returns:
            datetime: The last update timestamp.
        """

        return self._metadata.updated_at

    @property
    def updated_on(self) -> date:
        """
        Returns the date of the last update.

        Returns:
            date: The last update date.
        """

        return self._metadata.updated_on

    @property
    def uuid_(self) -> str:
        """
        Returns the universally unique identifier (UUID) of the subject.

        Returns:
            uuid.UUID: The instance's UUID.
        """

        return self._identifiable.uuid_


class Tag:
    """
    Represents a tag entity within the application.

    Tags are used for categorizing and filtering various models. This class
    utilizes composition by incorporating ModelIdentifiable for identity
    management and ModelMetadata for tracking creation and update details.
    """

    def __init__(
        self,
        value: str,
        created_at: Optional[datetime] = None,
        created_on: Optional[date] = None,
        id_: Optional[Union[int, str]] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        updated_on: Optional[date] = None,
        uuid_: Optional[uuid.UUID] = None,
    ) -> None:
        """
        Initializes a Tag instance.

        Args:
            value (str): The string value of the tag.
            created_at (Optional[datetime]): Specific timestamp of creation.
            created_on (Optional[date]): Specific date of creation.
            id_ (Optional[Union[int, str]]): Database ID for the entity.
            key (Optional[str]): Unique model key identifier.
            updated_at (Optional[datetime]): Timestamp of the last update.
            updated_on (Optional[date]): Date of the last update.
            uuid_ (Optional[uuid.UUID]): Universally unique identifier.

        Returns:
            None
        """

        self._identifiable: Final[ModelIdentifiable] = ModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._metadata: Final[ModelMetadata] = ModelMetadata(
            created_at=created_at,
            created_on=created_on,
            fields={
                "total": len(list(locals().keys())),
                "values": list(locals().keys()),
            },
            type_="TAG",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._value: Final[str] = value

    @property
    def created_at(self) -> datetime:
        """
        Returns the exact date and time when the tag was created.

        Returns:
            datetime: The creation timestamp.
        """

        return self._metadata.created_at

    @property
    def created_on(self) -> date:
        """
        Returns the date when the tag was created.

        Returns:
            date: The creation date.
        """

        return self._metadata.created_on

    @property
    def fields(self) -> dict[str, Any]:
        """
        Returns a copy of the dynamic metadata fields from the metadata component.

        Returns:
            dict[str, Any]: A dictionary containing additional metadata field information.
        """

        return dict(self._metadata.fields)

    @property
    def id_(self) -> Optional[Union[int, str]]:
        """
        Returns the internal database ID of the tag.

        Returns:
            Optional[Union[int, str]]: The database ID if assigned, otherwise None.
        """

        return self._identifiable.id_

    @property
    def key(self) -> Optional[str]:
        """
        Returns the unique string identifier (key) of the tag.

        Returns:
            Optional[str]: The model key if assigned, otherwise None.
        """
        return self._identifiable.key

    @property
    def type_(self) -> str:
        """
        Returns the type of the model (TAG).

        Returns:
            str: The model type string.
        """

        return self._metadata.type_

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp of the last update.

        Returns:
            datetime: The last update timestamp.
        """

        return self._metadata.updated_at

    @property
    def updated_on(self) -> date:
        """
        Returns the date of the last update.

        Returns:
            date: The last update date.
        """

        return self._metadata.updated_on

    @property
    def uuid_(self) -> uuid.UUID:
        """
        Returns the universally unique identifier (UUID) of the tag.

        Returns:
            uuid.UUID: The instance's UUID.
        """

        return self._identifiable.uuid_

    @property
    def value(self) -> str:
        """
        Returns the value of the tag.

        Returns:
            str: The value of the tag.
        """

        return self._value

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the model.

        Args:
            None

        Returns:
            dict[str, Any]: The dictionary representation of the model.
        """

        return _convert_to_dict(self)


class Teacher:
    """
    Represents a teacher entity within the application.

    Teachers can be associated with learning materials to provide educational context.
    This class utilizes composition by incorporating ModelIdentifiable for
    identity management and ModelMetadata for tracking lifecycle information.
    """

    def __init__(
        self,
        name: str,
        created_at: Optional[datetime] = None,
        created_on: Optional[date] = None,
        customfields: Optional[list[dict[str, Any]]] = None,
        difficulty: Optional[str] = None,
        id_: Optional[Union[int, str]] = None,
        key: Optional[str] = None,
        priority: Optional[str] = None,
        subjects: Optional[list[str]] = None,
        updated_at: Optional[datetime] = None,
        updated_on: Optional[date] = None,
        uuid_: Optional[uuid.UUID] = None,
    ) -> None:
        """
        Initializes a Teacher instance.

        Args:
            name (str): The string name of the teacher.
            created_at (Optional[datetime]): Specific timestamp of creation.
            created_on (Optional[date]): Specific date of creation.
            customfields (Optional[list[dict[str, Any]]]): List of custom data fields.
            difficulty (Optional[str]): Difficulty level key.
            id_ (Optional[Union[int, str]]): Database ID for the entity.
            key (Optional[str]): Unique model key identifier.
            priority (Optional[str]): Priority level key.
            subjects (Optional[list[str]]): List of subject keys this teacher is associated with.
            updated_at (Optional[datetime]): Timestamp of the last update.
            updated_on (Optional[date]): Date of the last update.
            uuid_ (Optional[uuid.UUID]): Universally unique identifier.

        Returns:
            None
        """

        self._customfields: Optional[list[dict[str, Any]]] = customfields or []
        self._difficulty: Final[Optional[str]] = difficulty
        self._identifiable: Final[ModelIdentifiable] = ModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._metadata: Final[ModelMetadata] = ModelMetadata(
            created_at=created_at,
            created_on=created_on,
            fields={
                "total": len(list(locals().keys())),
                "values": list(locals().keys()),
            },
            type_="TEACHER",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._name: Final[str] = name
        self._priority: Final[Optional[str]] = priority
        self._subjects: Final[list[str]] = subjects or []

    @property
    def created_at(self) -> datetime:
        """
        Returns the exact date and time when the teacher was created.

        Returns:
            datetime: The creation timestamp.
        """

        return self._metadata.created_at

    @property
    def created_on(self) -> date:
        """
        Returns the date when the teacher was created.

        Returns:
            date: The creation date.
        """

        return self._metadata.created_on

    @property
    def customfields(self) -> list[dict[str, Any]]:
        """
        Returns the list of custom fields associated with the teacher.

        Returns:
            list[dict[str, Any]]: A list containing custom data dictionaries.
        """

        return self._customfields

    @customfields.setter
    def customfields(
        self,
        value: Union[
            dict[str, Any],
            list[dict[str, Any]],
        ],
    ) -> None:
        if isinstance(
            value,
            dict,
        ):
            self._customfields.append(value)

            return

        self._customfields.extend(value)

    @property
    def difficulty(self) -> Optional[str]:
        """
        Returns the difficulty key of the teacher.

        Returns:
            Optional[str]: The internal key representing the difficulty level.
        """

        return self._difficulty

    @difficulty.setter
    def difficulty(
        self,
        value: str,
    ) -> None:
        self._difficulty = value

    @property
    def fields(self) -> dict[str, Any]:
        """
        Returns a copy of the dynamic metadata fields from the metadata component.

        Returns:
            dict[str, Any]: A dictionary containing additional metadata field information.
        """

        return dict(self._metadata.fields)

    @property
    def id_(self) -> Optional[Union[int, str]]:
        """
        Returns the internal database ID of the teacher.

        Returns:
            Optional[Union[int, str]]: The database ID if assigned, otherwise None.
        """

        return self._identifiable.id_

    @property
    def key(self) -> Optional[str]:
        """
        Returns the unique string identifier (key) of the teacher.

        Returns:
            Optional[str]: The model key if assigned, otherwise None.
        """
        return self._identifiable.key

    @property
    def name(self) -> str:
        """
        Returns the name of the teacher.

        Returns:
            str: The name of the teacher.
        """

        return self._name

    @property
    def priority(self) -> Optional[str]:
        """
        Returns the priority key of the teacher.

        Returns:
            Optional[str]: The internal key representing the priority level.
        """

        return self._priority

    @priority.setter
    def priority(
        self,
        value: str,
    ) -> None:
        self._priority = value

    @property
    def subjects(self) -> list[str]:
        """
        Returns a list of subject keys this teacher is associated with.

        Returns:
            list[str]: A list of subject keys.
        """

        return list(self._subjects)

    @subjects.setter
    def subjects(
        self,
        value: Union[
            list[str],
            str,
        ],
    ) -> None:
        if isinstance(
            value,
            str,
        ):
            self._subjects.append(value)

            return

        self._subjects.extend(value)

    @property
    def type_(self) -> str:
        """
        Returns the type of the model (TEACHER).

        Returns:
            str: The model type string.
        """

        return self._metadata.type_

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp of the last update.

        Returns:
            datetime: The last update timestamp.
        """

        return self._metadata.updated_at

    @property
    def updated_on(self) -> date:
        """
        Returns the date of the last update.

        Returns:
            date: The last update date.
        """

        return self._metadata.updated_on

    @property
    def uuid_(self) -> str:
        """
        Returns the universally unique identifier (UUID) of the teacher.

        Returns:
            uuid.UUID: The instance's UUID.
        """

        return self._identifiable.uuid_


class User:
    """
    Represents a user entity within the application.

    This class manages user-specific data, such as the username (value).
    It utilizes composition by incorporating ModelIdentifiable for
    identity management and ModelMetadata for tracking creation and
    update details.
    """

    def __init__(
        self,
        name: str,
        created_at: Optional[datetime] = None,
        created_on: Optional[date] = None,
        id_: Optional[Union[int, str]] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        updated_on: Optional[date] = None,
        uuid_: Optional[uuid.UUID] = None,
    ) -> None:
        """
        Initializes a User instance.

        Args:
            name (str): The string name of the user.
            created_at (Optional[datetime]): Specific timestamp of creation.
            created_on (Optional[date]): Specific date of creation.
            id_ (Optional[Union[int, str]]): Database ID for the entity.
            key (Optional[str]): Unique model key identifier.
            updated_at (Optional[datetime]): Timestamp of the last update.
            updated_on (Optional[date]): Date of the last update.
            uuid_ (Optional[uuid.UUID]): Universally unique identifier.

        Returns:
            None
        """

        self._identifiable: Final[ModelIdentifiable] = ModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._metadata: Final[ModelMetadata] = ModelMetadata(
            created_at=created_at,
            created_on=created_on,
            fields={
                "total": len(list(locals().keys())),
                "values": list(locals().keys()),
            },
            type_="USER",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._name: Final[str] = name

    @property
    def created_at(self) -> datetime:
        """
        Returns the exact date and time when the user was created.

        Returns:
            datetime: The creation timestamp.
        """

        return self._metadata.created_at

    @property
    def created_on(self) -> date:
        """
        Returns the date when the user was created.

        Returns:
            date: The creation date.
        """

        return self._metadata.created_on

    @property
    def fields(self) -> dict[str, Any]:
        """
        Returns a copy of the dynamic metadata fields from the metadata component.

        Returns:
            dict[str, Any]: A dictionary containing additional metadata field information.
        """

        return dict(self._metadata.fields)

    @property
    def id_(self) -> Optional[Union[int, str]]:
        """
        Returns the internal database ID of the user.

        Returns:
            Optional[Union[int, str]]: The database ID if assigned, otherwise None.
        """

        return self._identifiable.id_

    @property
    def key(self) -> Optional[str]:
        """
        Returns the unique string identifier (key) of the user.

        Returns:
            Optional[str]: The model key if assigned, otherwise None.
        """
        return self._identifiable.key

    @property
    def name(self) -> str:
        """
        Returns the name of the user.

        Returns:
            str: The name of the user.
        """

        return self._name

    @property
    def type_(self) -> str:
        """
        Returns the type of the model (USER).

        Returns:
            str: The model type string.
        """

        return self._metadata.type_

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp of the last update.

        Returns:
            datetime: The last update timestamp.
        """

        return self._metadata.updated_at

    @property
    def updated_on(self) -> date:
        """
        Returns the date of the last update.

        Returns:
            date: The last update date.
        """

        return self._metadata.updated_on

    @property
    def uuid_(self) -> uuid.UUID:
        """
        Returns the universally unique identifier (UUID) of the user.

        Returns:
            uuid.UUID: The instance's UUID.
        """

        return self._identifiable.uuid_

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the model.

        Args:
            None

        Returns:
            dict[str, Any]: The dictionary representation of the model.
        """

        return _convert_to_dict(self)
