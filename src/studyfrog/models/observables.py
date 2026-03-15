"""
Author: Louis Goodnews
Date: 2026-01-04
Description: This module contains the definitions of the various observable models used in the application
"""

from __future__ import annotations

import customtkinter as ctk
import uuid

from typing import Any, Final, Optional, TypeAlias, Union

from studyfrog.utils.common import exists


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "AnswerObservableModel",
    "DifficultyObservableModel",
    "FlashcardObservableModel",
    "NoteObservableModel",
    "PriorityObservableModel",
    "QuestionObservableModel",
    "StackObservableModel",
    "SubjectObservableModel",
    "TagObservableModel",
    "TeacherObservableModel",
]


# ---------- Constants ---------- #

ObservableModel: TypeAlias = Union[
    "AnswerObservableModel",
    "DifficultyObservableModel",
    "FlashcardObservableModel",
    "NoteObservableModel",
    "PriorityObservableModel",
    "QuestionObservableModel",
    "StackObservableModel",
    "SubjectObservableModel",
    "TagObservableModel",
    "TeacherObservableModel",
]


# ---------- Helper Functions ---------- #


def _convert_to_dict(observable_model: ObservableModel) -> dict[str, Any]:
    """
    Converts the observable model to a dictionary.

    Args:
        observable_model (ObservableModel): The observable model to convert.

    Returns:
        dict[str, Any]: The observable model as a dictionary.
    """

    result: dict[str, Any] = {}

    for (
        key,
        value,
    ) in observable_model.__dict__.items():
        if isinstance(
            value,
            (
                ObservableModelIdentifiable,
                ObservableModelMetadata,
            ),
        ):
            result[key.strip("_")] = value.to_dict()

            continue

        result[key.strip("_")] = value

    return dict(sorted(result.items()))


def _reset_variables(
    observable_model: Union[
        AnswerObservableModel,
        FlashcardObservableModel,
        NoteObservableModel,
        QuestionObservableModel,
    ],
) -> None:
    """
    Resets the variables of the given observable model.

    Args:
        observable_model: The observable model to reset.

    Returns:
        None
    """

    for value in observable_model.__dict__.values():
        if not isinstance(value, ctk.Variable):
            continue

        if isinstance(
            value,
            ctk.BooleanVar,
        ):
            value.set(value=False)
        elif isinstance(
            value,
            ctk.DoubleVar,
        ):
            value.set(value=0.0)
        elif isinstance(
            value,
            ctk.IntVar,
        ):
            value.set(value=0)
        elif isinstance(
            value,
            ctk.StringVar,
        ):
            value.set(value="")


# ---------- Classes ---------- #


class AnswerObservableModel:
    """
    Represents an observable answer model within the application.

    An answer consists an associated metadata such as creation and update timestamps,
    difficulty, priority, and organizational attributes like tags, subjects, and
    teachers. This class utilizes composition by incorporating
    ObservableModelIdentifiable for identity management and
    ObservableModelMetadata for tracking lifecycle details.
    """

    def __init__(
        self,
        created_at: str = "",
        created_on: str = "",
        id_: Optional[Union[int, str]] = 0,
        is_correct: bool = False,
        key: Optional[str] = "",
        text: str = "",
        updated_at: str = "",
        updated_on: str = "",
        uuid_: Optional[Union[str, uuid.UUID]] = None,
    ) -> None:
        """
        Initializes an AnswerObservableModel instance.

        Args:
            created_at (str): The creation timestamp of the answer.
            created_on (str): The creation date of the answer.
            id_ (Optional[Union[int, str]]): The unique identifier of the answer.
            is_correct (bool): Flag indicating if this answer is correct.
            key (Optional[str]): The key of the answer.
            text (str): The actual text content of the answer.
            updated_at (str): The last update timestamp of the answer.
            updated_on (str): The last update date of the answer.
            uuid_ (Optional[Union[str, uuid.UUID]]): The UUID of the answer.

        Returns:
            None
        """

        self._identifiable: ObservableModelIdentifiable = ObservableModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._is_correct: ctk.BooleanVar = ctk.BooleanVar(value=is_correct)
        self._metadata: ObservableModelMetadata = ObservableModelMetadata(
            created_at=created_at,
            created_on=created_on,
            type_="OBSERVABLE_ANSWER",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._text: ctk.StringVar = ctk.StringVar(value=text)

    @property
    def created_at(self) -> ctk.StringVar:
        """
        The creation timestamp of the answer.

        Returns:
            ctk.StringVar: The creation timestamp of the answer.
        """
        return self._metadata.created_at

    @property
    def created_on(self) -> ctk.StringVar:
        """
        The creation date of the answer.

        Returns:
            ctk.StringVar: The creation date of the answer.
        """
        return self._metadata.created_on

    @property
    def id(self) -> ctk.StringVar:
        """
        The unique identifier of the answer.

        Returns:
            ctk.StringVar: The unique identifier of the answer.
        """
        return self._identifiable.id

    @property
    def is_correct(self) -> ctk.BooleanVar:
        """
        Flag indicating if this answer is correct.

        Returns:
            ctk.BooleanVar: Flag indicating if this answer is correct.
        """
        return self._is_correct

    @property
    def key(self) -> ctk.StringVar:
        """
        The key of the answer.

        Returns:
            ctk.StringVar: The key of the answer.
        """
        return self._identifiable.key

    @property
    def text(self) -> ctk.StringVar:
        """
        The actual text content of the answer.

        Returns:
            ctk.StringVar: The actual text content of the answer.
        """
        return self._text

    @property
    def type(self) -> ctk.StringVar:
        """
        The type of the answer.

        Returns:
            ctk.StringVar: The type of the answer.
        """
        return self._metadata.type

    @property
    def updated_at(self) -> ctk.StringVar:
        """
        The last update timestamp of the answer.

        Returns:
            ctk.StringVar: The last update timestamp of the answer.
        """
        return self._metadata.updated_at

    @property
    def updated_on(self) -> ctk.StringVar:
        """
        The last update date of the answer.

        Returns:
            ctk.StringVar: The last update date of the answer.
        """
        return self._metadata.updated_on

    @property
    def uuid(self) -> ctk.StringVar:
        """
        The UUID of the answer.

        Returns:
            ctk.StringVar: The UUID of the answer.
        """
        return self._identifiable.uuid

    def reset(self) -> None:
        """
        Resets the variables of the given observable model.

        Returns:
            None
        """
        _reset_variables(observable_model=self)

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the observable model.

        Returns:
            dict[str, Any]: The observable model as a dictionary.
        """
        return _convert_to_dict(observable_model=self)


class DifficultyObservableModel:

    def __init__(
        self,
        display_name: str = "",
        name: str = "",
        value: float = 0.0,
        created_at: str = "",
        created_on: str = "",
        id_: Union[int, str] = 0,
        key: str = "",
        updated_at: str = "",
        updated_on: str = "",
        uuid_: Optional[Union[str, uuid.UUID]] = None,
    ) -> None:

        self._display_name: ctk.StringVar = ctk.StringVar(value=display_name)
        self._identifiable: ObservableModelIdentifiable = ObservableModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._metadata: ObservableModelMetadata = ObservableModelMetadata(
            created_at=created_at,
            created_on=created_on,
            type_="OBSERVABLE_DIFFICULTY",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._name: ctk.StringVar = ctk.StringVar(value=name)
        self._value: ctk.DoubleVar = ctk.DoubleVar(value=value)

    @property
    def created_at(self) -> ctk.StringVar:
        """
        The creation timestamp of the DifficultyObservableModel.

        Returns:
            ctk.StringVar: The creation timestamp of the DifficultyObservableModel.
        """
        return self._metadata.created_at

    @property
    def created_on(self) -> ctk.StringVar:
        """
        The creation date of the DifficultyObservableModel.

        Returns:
            ctk.StringVar: The creation date of the DifficultyObservableModel.
        """
        return self._metadata.created_on

    @property
    def display_name(self) -> ctk.StringVar:
        """
        The display name of the DifficultyObservableModel.

        Returns:
            ctk.StringVar: The display name of the DifficultyObservableModel.
        """
        return self._display_name

    @display_name.setter
    def display_name(
        self,
        value: str,
    ) -> None:
        self._display_name.set(value=value)

    @property
    def id(self) -> ctk.StringVar:
        """
        The unique identifier of the DifficultyObservableModel.

        Returns:
            ctk.StringVar: The unique identifier of the DifficultyObservableModel.
        """
        return self._identifiable.id

    @property
    def key(self) -> ctk.StringVar:
        """
        The key of the DifficultyObservableModel.

        Returns:
            ctk.StringVar: The key of the DifficultyObservableModel.
        """
        return self._identifiable.key

    @property
    def name(self) -> ctk.StringVar:
        """
        The name of the DifficultyObservableModel.

        Returns:
            ctk.StringVar: The name of the DifficultyObservableModel.
        """
        return self._name

    @name.setter
    def name(
        self,
        value: str,
    ) -> None:
        self._name.set(value=value)

    @property
    def type(self) -> ctk.StringVar:
        """
        The type of the DifficultyObservableModel.

        Returns:
            ctk.StringVar: The type of the DifficultyObservableModel.
        """
        return self._metadata.type

    @property
    def updated_at(self) -> ctk.StringVar:
        """
        The last update timestamp of the DifficultyObservableModel.

        Returns:
            ctk.StringVar: The last update timestamp of the DifficultyObservableModel.
        """
        return self._metadata.updated_at

    @property
    def updated_on(self) -> ctk.StringVar:
        """
        The last update date of the DifficultyObservableModel.

        Returns:
            ctk.StringVar: The last update date of the DifficultyObservableModel.
        """
        return self._metadata.updated_on

    @property
    def uuid(self) -> ctk.StringVar:
        """
        The UUID of the DifficultyObservableModel.

        Returns:
            ctk.StringVar: The UUID of the DifficultyObservableModel.
        """
        return self._identifiable.uuid

    @property
    def value(self) -> ctk.DoubleVar:
        """
        The value of the DifficultyObservableModel.

        Returns:
            ctk.DoubleVar: The value of the DifficultyObservableModel.
        """
        return self._value

    @value.setter
    def value(
        self,
        value: float,
    ) -> None:
        self._value.set(value=value)

    def reset(self) -> None:
        """
        Resets the variables of the given observable model.

        Returns:
            None
        """
        _reset_variables(observable_model=self)

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the observable model.

        Returns:
            dict[str, Any]: The observable model as a dictionary.
        """
        return _convert_to_dict(observable_model=self)


class FlashcardObservableModel:

    def __init__(
        self,
        author: str = "",
        back: str = "",
        created_at: str = "",
        created_on: str = "",
        description: str = "",
        difficulty: str = "",
        front: str = "",
        id_: Optional[Union[int, str]] = 0,
        is_assigned_to_stack: bool = False,
        key: str = "",
        last_viewed_at: str = "",
        last_viewed_on: str = "",
        next_view_on: str = "",
        priority: str = "",
        subject: str = "",
        tags: Optional[list[str]] = None,
        teacher: str = "",
        updated_at: str = "",
        updated_on: str = "",
        uuid_: Optional[Union[str, uuid.UUID]] = "",
    ) -> None:
        """
        Initializes a new FlashcardObservableModel instance.

        Args:
            author (str): The name of the flashcard's author. Defaults to an empty string.
            back (str): The text on the back of the flashcard. Defaults to an empty string.
            created_at (str): The creation timestamp of the flashcard. Defaults to an empty string.
            created_on (str): The creation date of the flashcard. Defaults to an empty string.
            description (str): The description of the flashcard. Defaults to an empty string.
            difficulty (str): The difficulty level of the flashcard. Defaults to an empty string.
            front (str): The text on the front of the flashcard. Defaults to an empty string.
            id_ (Optional[Union[int, str]]): The database ID of the flashcard. Defaults to an empty string.
            is_assigned_to_stack (bool): Flag indicating if the flashcard is assigned to a stack. Defaults to an empty string.
            key (str): The key of the flashcard. Defaults to an empty string.
            last_viewed_at (str): The last time the flashcard was viewed. Defaults to an empty string.
            last_viewed_on (str): The last date the flashcard was viewed. Defaults to an empty string.
            next_view_on (str): The next time the flashcard is due to be reviewed. Defaults to an empty string.
            priority (str): The priority of the flashcard. Defaults to an empty string.
            subject (str): The subject of the flashcard. Defaults to an empty string.
            tags (Optional[list[str]]): A list of tags associated with the flashcard. Defaults to an empty string.
            teacher (str): The name of the teacher who created the flashcard. Defaults to an empty string.
            updated_at (str): The last update timestamp of the flashcard. Defaults to an empty string.
            updated_on (str): The last update date of the flashcard. Defaults to an empty string.
            uuid_ (Optional[Union[str, uuid.UUID]]): The UUID of the flashcard. Defaults to an empty string.

        Returns:
            None
        """

        self._author: ctk.StringVar = ctk.StringVar(value=author)
        self._back: ctk.StringVar = ctk.StringVar(value=back)
        self._description: ctk.StringVar = ctk.StringVar(value=description)
        self._difficulty: ctk.StringVar = ctk.StringVar(value=difficulty)
        self._front: ctk.StringVar = ctk.StringVar(value=front)
        self._identifiable: ObservableModelIdentifiable = ObservableModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._is_assigned_to_stack: ctk.BooleanVar = ctk.BooleanVar(value=is_assigned_to_stack)
        self._last_viewed_at: ctk.StringVar = ctk.StringVar(value=last_viewed_at)
        self._last_viewed_on: ctk.StringVar = ctk.StringVar(value=last_viewed_on)
        self._metadata: ObservableModelMetadata = ObservableModelMetadata(
            created_at=created_at,
            created_on=created_on,
            type_="OBSERVABLE_FLASHCARD",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._next_view_on: ctk.StringVar = ctk.StringVar(value=next_view_on)
        self._priority: ctk.StringVar = ctk.StringVar(value=priority)
        self._subject: ctk.StringVar = ctk.StringVar(value=subject)
        self._tags: ctk.StringVar = ctk.StringVar(
            value=",".join(tags) if exists(value=tags) else ""
        )
        self._teacher: ctk.StringVar = ctk.StringVar(value=teacher)

    @property
    def author(self) -> ctk.StringVar:
        """
        The author of the FlashcardObservableModel.

        Returns:
            ctk.StringVar: The author of the FlashcardObservableModel.
        """
        return self._author

    @property
    def back(self) -> ctk.StringVar:
        """
        The back of the FlashcardObservableModel.

        Returns:
            ctk.StringVar: The back of the FlashcardObservableModel.
        """
        return self._back

    @property
    def created_at(self) -> ctk.StringVar:
        """
        The creation timestamp of the FlashcardObservableModel.

        Returns:
            ctk.StringVar: The creation timestamp of the FlashcardObservableModel.
        """
        return self._metadata.created_at

    @property
    def created_on(self) -> ctk.StringVar:
        """
        The creation date of the FlashcardObservableModel.

        Returns:
            ctk.StringVar: The creation date of the FlashcardObservableModel.
        """
        return self._metadata.created_on

    @property
    def description(self) -> ctk.StringVar:
        """
        The description of the FlashcardObservableModel.

        Returns:
            ctk.StringVar: The description of the FlashcardObservableModel.
        """
        return self._description

    @property
    def difficulty(self) -> ctk.StringVar:
        """
        The difficulty of the FlashcardObservableModel.

        Returns:
            ctk.StringVar: The difficulty of the FlashcardObservableModel.
        """
        return self._difficulty

    @property
    def front(self) -> ctk.StringVar:
        """
        The front of the FlashcardObservableModel.

        Returns:
            ctk.StringVar: The front of the FlashcardObservableModel.
        """
        return self._front

    @property
    def id(self) -> ctk.StringVar:
        """
        The unique identifier of the FlashcardObservableModel.

        Returns:
            ctk.StringVar: The unique identifier of the FlashcardObservableModel.
        """
        return self._identifiable.id

    @property
    def is_assigned_to_stack(self) -> ctk.BooleanVar:
        """
        Whether the FlashcardObservableModel is assigned to a stack.

        Returns:
            ctk.BooleanVar: Whether the FlashcardObservableModel is assigned to a stack.
        """
        return self._is_assigned_to_stack

    @property
    def key(self) -> ctk.StringVar:
        """
        The key of the FlashcardObservableModel.

        Returns:
            ctk.StringVar: The key of the FlashcardObservableModel.
        """
        return self._identifiable.key

    @property
    def last_viewed_at(self) -> ctk.StringVar:
        """
        The last viewed timestamp of the FlashcardObservableModel.

        Returns:
            ctk.StringVar: The last viewed timestamp of the FlashcardObservableModel.
        """
        return self._last_viewed_at

    @property
    def last_viewed_on(self) -> ctk.StringVar:
        """
        The last viewed date of the FlashcardObservableModel.

        Returns:
            ctk.StringVar: The last viewed date of the FlashcardObservableModel.
        """
        return self._last_viewed_on

    @property
    def next_view_on(self) -> ctk.StringVar:
        """
        The next view date of the FlashcardObservableModel.

        Returns:
            ctk.StringVar: The next view date of the FlashcardObservableModel.
        """
        return self._next_view_on

    @property
    def priority(self) -> ctk.StringVar:
        """
        The priority of the FlashcardObservableModel.

        Returns:
            ctk.StringVar: The priority of the FlashcardObservableModel.
        """
        return self._priority

    @property
    def subject(self) -> ctk.StringVar:
        """
        The subject of the FlashcardObservableModel.

        Returns:
            ctk.StringVar: The subject of the FlashcardObservableModel.
        """
        return self._subject

    @property
    def tags(self) -> ctk.StringVar:
        """
        The tags of the FlashcardObservableModel.

        Returns:
            ctk.StringVar: The tags of the FlashcardObservableModel.
        """
        return self._tags

    @property
    def teacher(self) -> ctk.StringVar:
        """
        The teacher of the FlashcardObservableModel.

        Returns:
            ctk.StringVar: The teacher of the FlashcardObservableModel.
        """
        return self._teacher

    @property
    def type(self) -> ctk.StringVar:
        """
        The type of the FlashcardObservableModel.

        Returns:
            ctk.StringVar: The type of the FlashcardObservableModel.
        """
        return self._metadata.type

    @property
    def updated_at(self) -> ctk.StringVar:
        """
        The last update timestamp of the FlashcardObservableModel.

        Returns:
            ctk.StringVar: The last update timestamp of the FlashcardObservableModel.
        """
        return self._metadata.updated_at

    @property
    def updated_on(self) -> ctk.StringVar:
        """
        The last update date of the FlashcardObservableModel.

        Returns:
            ctk.StringVar: The last update date of the FlashcardObservableModel.
        """
        return self._metadata.updated_on

    @property
    def uuid(self) -> ctk.StringVar:
        """
        The UUID of the FlashcardObservableModel.

        Returns:
            ctk.StringVar: The UUID of the FlashcardObservableModel.
        """
        return self._identifiable.uuid

    def reset(self) -> None:
        """
        Resets the variables of the given observable model.

        Returns:
            None
        """
        _reset_variables(observable_model=self)

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the observable model.

        Returns:
            dict[str, Any]: The observable model as a dictionary.
        """
        return _convert_to_dict(observable_model=self)


class NoteObservableModel:

    def __init__(
        self,
        text: str = "",
        title: str = "",
        author: str = "",
        created_at: str = "",
        created_on: str = "",
        difficulty: str = "",
        id_: Optional[Union[int, str]] = 0,
        is_assigned_to_stack: bool = False,
        key: str = "",
        last_viewed_at: str = "",
        last_viewed_on: str = "",
        next_view_on: str = "",
        priority: str = "",
        subject: str = "",
        tags: Optional[list[str]] = None,
        teacher: str = "",
        updated_at: str = "",
        updated_on: str = "",
        uuid_: Optional[Union[str, uuid.UUID]] = None,
    ) -> None:

        self._author: ctk.StringVar = ctk.StringVar(value=author)
        self._difficulty: ctk.StringVar = ctk.StringVar(value=difficulty)
        self._identifiable: ObservableModelIdentifiable = ObservableModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._is_assigned_to_stack: ctk.StringVar = ctk.StringVar(value=is_assigned_to_stack)
        self._last_viewed_at: ctk.StringVar = ctk.StringVar(value=last_viewed_at)
        self._last_viewed_on: ctk.StringVar = ctk.StringVar(value=last_viewed_on)
        self._metadata: ObservableModelMetadata = ObservableModelMetadata(
            created_at=created_at,
            created_on=created_on,
            type_="OBSERVABLE_NOTE",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._next_view_on: ctk.StringVar = ctk.StringVar(value=next_view_on)
        self._priority: ctk.StringVar = ctk.StringVar(value=priority)
        self._subject: ctk.StringVar = ctk.StringVar(value=subject)
        self._tags: ctk.StringVar = ctk.StringVar(
            value=",".join(tags) if exists(value=tags) else ""
        )
        self._teacher: ctk.StringVar = ctk.StringVar(value=teacher)
        self._text: ctk.StringVar = ctk.StringVar(value=text)
        self._title: ctk.StringVar = ctk.StringVar(value=title)

    @property
    def author(self) -> ctk.StringVar:
        """
        Returns the author of the note.

        Returns:
            ctk.StringVar: The author of the note.
        """
        return self._author

    @author.setter
    def author(
        self,
        value: str,
    ) -> None:
        self._author.set(value=value)

    @property
    def created_at(self) -> ctk.StringVar:
        """
        Returns the creation timestamp of the note.

        Returns:
            ctk.StringVar: The creation timestamp of the note.
        """
        return self._metadata.created_at

    @created_at.setter
    def created_at(
        self,
        value: str,
    ) -> None:
        self._metadata.created_at.set(value=value)

    @property
    def difficulty(self) -> ctk.StringVar:
        """
        Returns the difficulty of the note.

        Returns:
            ctk.StringVar: The difficulty of the note.
        """
        return self._difficulty

    @difficulty.setter
    def difficulty(
        self,
        value: str,
    ) -> None:
        self._difficulty.set(value=value)

    @property
    def id(self) -> ctk.StringVar:
        """
        Returns the ID of the note.

        Returns:
            ctk.StringVar: The ID of the note.
        """
        return self._identifiable.id

    @id.setter
    def id(
        self,
        value: str,
    ) -> None:
        self._identifiable.id.set(value=value)

    @property
    def is_assigned_to_stack(self) -> ctk.BooleanVar:
        """
        Returns whether the note is assigned to a stack.

        Returns:
            ctk.BooleanVar: Whether the note is assigned to a stack.
        """
        return self._is_assigned_to_stack

    @is_assigned_to_stack.setter
    def is_assigned_to_stack(
        self,
        value: bool,
    ) -> None:
        self._is_assigned_to_stack.set(value=value)

    @property
    def key(self) -> ctk.StringVar:
        """
        Returns the key of the note.

        Returns:
            ctk.StringVar: The key of the note.
        """
        return self._identifiable.key

    @key.setter
    def key(
        self,
        value: str,
    ) -> None:
        self._identifiable.key.set(value=value)

    @property
    def last_viewed_at(self) -> ctk.StringVar:
        """
        Returns the last viewed at of the note.

        Returns:
            ctk.StringVar: The last viewed at of the note.
        """
        return self._last_viewed_at

    @last_viewed_at.setter
    def last_viewed_at(
        self,
        value: str,
    ) -> None:
        self._last_viewed_at.set(value=value)

    @property
    def last_viewed_on(self) -> ctk.StringVar:
        """
        Returns the last viewed on of the note.

        Returns:
            ctk.StringVar: The last viewed on of the note.
        """
        return self._last_viewed_on

    @last_viewed_on.setter
    def last_viewed_on(
        self,
        value: str,
    ) -> None:
        self._last_viewed_on.set(value=value)

    @property
    def next_view_on(self) -> ctk.StringVar:
        """
        Returns the next view on of the note.

        Returns:
            ctk.StringVar: The next view on of the note.
        """
        return self._next_view_on

    @next_view_on.setter
    def next_view_on(
        self,
        value: str,
    ) -> None:
        self._next_view_on.set(value=value)

    @property
    def priority(self) -> ctk.StringVar:
        """
        Returns the priority of the note.

        Returns:
            ctk.StringVar: The priority of the note.
        """
        return self._priority

    @priority.setter
    def priority(
        self,
        value: str,
    ) -> None:
        self._priority.set(value=value)

    @property
    def subject(self) -> ctk.StringVar:
        """
        Returns the subject of the note.

        Returns:
            ctk.StringVar: The subject of the note.
        """
        return self._subject

    @subject.setter
    def subject(
        self,
        value: str,
    ) -> None:
        self._subject.set(value=value)

    @property
    def tags(self) -> ctk.StringVar:
        """
        Returns the tags of the note.

        Returns:
            ctk.StringVar: The tags of the note.
        """
        return self._tags

    @tags.setter
    def tags(
        self,
        value: str,
    ) -> None:
        self._tags.set(value=value)

    @property
    def teacher(self) -> ctk.StringVar:
        """
        Returns the teacher of the note.

        Returns:
            ctk.StringVar: The teacher of the note.
        """
        return self._teacher

    @teacher.setter
    def teacher(
        self,
        value: str,
    ) -> None:
        self._teacher.set(value=value)

    @property
    def text(self) -> ctk.StringVar:
        """
        Returns the text of the note.

        Returns:
            ctk.StringVar: The text of the note.
        """
        return self._text

    @text.setter
    def text(
        self,
        value: str,
    ) -> None:
        self._text.set(value=value)

    @property
    def title(self) -> ctk.StringVar:
        """
        Returns the title of the note.

        Returns:
            ctk.StringVar: The title of the note.
        """
        return self._title

    @title.setter
    def title(
        self,
        value: str,
    ) -> None:
        self._title.set(value=value)

    @property
    def type_(self) -> ctk.StringVar:
        """
        Returns the type of the note.

        Returns:
            ctk.StringVar: The type of the note.
        """
        return self._metadata.type

    @type_.setter
    def type_(
        self,
        value: str,
    ) -> None:
        self._metadata.type.set(value=value)

    @property
    def updated_at(self) -> ctk.StringVar:
        """
        Returns the updated at of the note.

        Returns:
            ctk.StringVar: The updated at of the note.
        """
        return self._metadata._updated_at

    @updated_at.setter
    def updated_at(
        self,
        value: str,
    ) -> None:
        self._metadata._updated_at.set(value=value)

    @property
    def updated_on(self) -> ctk.StringVar:
        """
        Returns the updated on of the note.

        Returns:
            ctk.StringVar: The updated on of the note.
        """
        return self._metadata._updated_on

    @updated_on.setter
    def updated_on(
        self,
        value: str,
    ) -> None:
        self._metadata._updated_on.set(value=value)

    @property
    def uuid(self) -> ctk.StringVar:
        """
        Returns the UUID of the note.

        Returns:
            ctk.StringVar: The UUID of the note.
        """
        return self._identifiable.uuid

    @uuid.setter
    def uuid(
        self,
        value: str,
    ) -> None:
        self._identifiable.uuid.set(value=value)

    def reset(self) -> None:
        """
        Resets the variables of the given observable model.

        Returns:
            None
        """
        _reset_variables(observable_model=self)

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the observable model.

        Returns:
            dict[str, Any]: The observable model as a dictionary.
        """
        return _convert_to_dict(observable_model=self)


class ObservableModelIdentifiable:
    """
    Provides identification properties for an observable model object.

    This class handles the unique identity of an observable model by managing its
    database ID, a human-readable or system-generated key, and a universally
    unique identifier (UUID).
    """

    def __init__(
        self,
        id_: Optional[Union[int, str]] = 0,
        key: Optional[str] = "",
        uuid_: Optional[Union[str, uuid.UUID]] = None,
    ) -> None:
        """
        Initializes an ObservableModelIdentifiable instance.

        Args:
            id_ (Optional[Union[int, str]]): The internal database ID of the model.
            key (Optional[str]): A unique string identifier for the model.
            uuid_ (Optional[Union[str, uuid.UUID]]): A universally unique identifier.

        Returns:
            None
        """

        self._id: ctk.IntVar = ctk.IntVar(value=int(id_))
        self._key: ctk.StringVar = ctk.StringVar(value=key)
        self._uuid: ctk.StringVar = ctk.StringVar(value=str(uuid_) if uuid_ else "")

    @property
    def id(self) -> ctk.IntVar:
        """
        Returns the internal database ID of the ObservableModelIdentifiable.

        Returns:
            ctk.IntVar: The database ID if assigned, otherwise 0.
        """
        return self._id

    @property
    def key(self) -> ctk.StringVar:
        """
        Returns the unique string identifier of the ObservableModelIdentifiable.

        Returns:
            ctk.StringVar: The unique string identifier if assigned, otherwise an empty string.
        """
        return self._key

    @property
    def uuid(self) -> ctk.StringVar:
        """
        Returns the universally unique identifier (UUID) of the ObservableModelIdentifiable.

        Returns:
            ctk.StringVar: The instance's UUID if assigned, otherwise an empty string.
        """
        return self._uuid

    def reset(self) -> None:
        """
        Resets the variables of the given observable model.

        Returns:
            None
        """
        _reset_variables(observable_model=self)


class ObservableModelMetadata:
    """
    Provides observable metadata associated with a model dictionary.

    This class manages timestamps (creation and update dates/times) and the
    model type using `customtkinter.StringVar`. This allows UI elements
    to automatically reflect changes in the metadata.
    """

    def __init__(
        self,
        type_: str,
        created_at: str = "",
        created_on: str = "",
        updated_at: str = "",
        updated_on: str = "",
    ) -> None:
        """
        Initializes the ObservableModelMetadata instance.

        Args:
            type_ (str): The type of the model (e.g., 'STACK', 'FLASHCARD').
            created_at (str): The exact date and time of creation. Defaults to an empty string.
            created_on (str): The date of creation. Defaults to an empty string.
            updated_at (str): The exact date and time of the last update. Defaults to an empty string.
            updated_on (str): The date of the last update. Defaults to an empty string.

        Returns:
            None
        """

        self._created_at: ctk.StringVar = ctk.StringVar(value=created_at)
        self._created_on: ctk.StringVar = ctk.StringVar(value=created_on)
        self._type: ctk.StringVar = ctk.StringVar(value=type_)
        self._updated_at: ctk.StringVar = ctk.StringVar(value=updated_at)
        self._updated_on: ctk.StringVar = ctk.StringVar(value=updated_on)

    @property
    def created_at(self) -> ctk.StringVar:
        """
        The creation timestamp of the ObservableModelMetadata.

        Returns:
            ctk.StringVar: The creation timestamp of the ObservableModelMetadata.
        """
        return self._created_at

    @property
    def created_on(self) -> ctk.StringVar:
        """
        The creation date of the ObservableModelMetadata.

        Returns:
            ctk.StringVar: The creation date of the ObservableModelMetadata.
        """
        return self._created_on

    @property
    def type(self) -> ctk.StringVar:
        """
        The type of the ObservableModelMetadata.

        Returns:
            ctk.StringVar: The type of the ObservableModelMetadata.
        """
        return self._type

    @property
    def updated_at(self) -> ctk.StringVar:
        """
        The last update timestamp of the ObservableModelMetadata.

        Returns:
            ctk.StringVar: The last update timestamp of the ObservableModelMetadata.
        """
        return self._updated_at

    @property
    def updated_on(self) -> ctk.StringVar:
        """
        The last update date of the ObservableModelMetadata.

        Returns:
            ctk.StringVar: The last update date of the ObservableModelMetadata.
        """
        return self._updated_on

    def reset(self) -> None:
        """
        Resets the variables of the given observable model.

        Returns:
            None
        """
        _reset_variables(observable_model=self)

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the observable model.

        Returns:
            dict[str, Any]: The observable model as a dictionary.
        """
        return _convert_to_dict(observable_model=self)


class PriorityObservableModel:

    def __init__(
        self,
        display_name: str = "",
        name: str = "",
        value: float = 0.0,
        created_at: str = "",
        created_on: str = "",
        id_: Union[int, str] = 0,
        key: str = "",
        updated_at: str = "",
        updated_on: str = "",
        uuid_: Optional[Union[str, uuid.UUID]] = None,
    ) -> None:

        self._display_name: ctk.StringVar = ctk.StringVar(value=display_name)
        self._identifiable: ObservableModelIdentifiable = ObservableModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._metadata: ObservableModelMetadata = ObservableModelMetadata(
            created_at=created_at,
            created_on=created_on,
            type_="OBSERVABLE_PRIORITY",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._name: ctk.StringVar = ctk.StringVar(value=name)
        self._value: ctk.DoubleVar = ctk.DoubleVar(value=value)

    @property
    def created_at(self) -> ctk.StringVar:
        """
        The creation timestamp of the PriorityObservableModel.

        Returns:
            ctk.StringVar: The creation timestamp of the PriorityObservableModel.
        """
        return self._metadata.created_at

    @property
    def created_on(self) -> ctk.StringVar:
        """
        The creation date of the PriorityObservableModel.

        Returns:
            ctk.StringVar: The creation date of the PriorityObservableModel.
        """
        return self._metadata.created_on

    @property
    def display_name(self) -> ctk.StringVar:
        """
        The display name of the PriorityObservableModel.

        Returns:
            ctk.StringVar: The display name of the PriorityObservableModel.
        """
        return self._display_name

    @display_name.setter
    def display_name(
        self,
        value: str,
    ) -> None:
        self._display_name.set(value=value)

    @property
    def id(self) -> ctk.StringVar:
        """
        The unique identifier of the PriorityObservableModel.

        Returns:
            ctk.StringVar: The unique identifier of the PriorityObservableModel.
        """
        return self._identifiable.id

    @property
    def key(self) -> ctk.StringVar:
        """
        The key of the PriorityObservableModel.

        Returns:
            ctk.StringVar: The key of the PriorityObservableModel.
        """
        return self._identifiable.key

    @property
    def name(self) -> ctk.StringVar:
        """
        The name of the PriorityObservableModel.

        Returns:
            ctk.StringVar: The name of the PriorityObservableModel.
        """
        return self._name

    @name.setter
    def name(
        self,
        value: str,
    ) -> None:
        self._name.set(value=value)

    @property
    def type(self) -> ctk.StringVar:
        """
        The type of the PriorityObservableModel.

        Returns:
            ctk.StringVar: The type of the PriorityObservableModel.
        """
        return self._metadata.type

    @property
    def updated_at(self) -> ctk.StringVar:
        """
        The last update timestamp of the PriorityObservableModel.

        Returns:
            ctk.StringVar: The last update timestamp of the PriorityObservableModel.
        """
        return self._metadata.updated_at

    @property
    def updated_on(self) -> ctk.StringVar:
        """
        The last update date of the PriorityObservableModel.

        Returns:
            ctk.StringVar: The last update date of the PriorityObservableModel.
        """
        return self._metadata.updated_on

    @property
    def uuid(self) -> ctk.StringVar:
        """
        The UUID of the PriorityObservableModel.

        Returns:
            ctk.StringVar: The UUID of the PriorityObservableModel.
        """
        return self._identifiable.uuid

    @property
    def value(self) -> ctk.DoubleVar:
        """
        The value of the PriorityObservableModel.

        Returns:
            ctk.DoubleVar: The value of the PriorityObservableModel.
        """
        return self._value

    @value.setter
    def value(
        self,
        value: float,
    ) -> None:
        self._value.set(value=value)

    def reset(self) -> None:
        """
        Resets the variables of the given observable model.

        Returns:
            None
        """
        _reset_variables(observable_model=self)

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the observable model.

        Returns:
            dict[str, Any]: The observable model as a dictionary.
        """
        return _convert_to_dict(observable_model=self)


class QuestionObservableModel:
    """ """

    def __init__(
        self,
        answers: Union[list[str], str] = "",
        author: str = "",
        created_at: str = "",
        created_on: str = "",
        difficulty: str = "",
        id_: Union[int, str] = 0,
        is_assigned_to_stack: bool = False,
        key: str = "",
        last_viewed_at: str = "",
        last_viewed_on: str = "",
        next_view_on: str = "",
        priority: str = "",
        subject: str = "",
        tags: Union[list[str], str] = "",
        teacher: str = "",
        text: str = "",
        updated_at: str = "",
        updated_on: str = "",
        uuid_: Union[str, uuid.UUID] = "",
    ) -> None:

        self._answers: ctk.StringVar = ctk.StringVar(value=answers)
        self._author: ctk.StringVar = ctk.StringVar(value=author)
        self._difficulty: ctk.StringVar = ctk.StringVar(value=difficulty)
        self._identifiable: ObservableModelIdentifiable = ObservableModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._is_assigned_to_stack: ctk.BooleanVar = ctk.BooleanVar(value=is_assigned_to_stack)
        self._last_viewed_at: ctk.StringVar = ctk.StringVar(value=last_viewed_at)
        self._last_viewed_on: ctk.StringVar = ctk.StringVar(value=last_viewed_on)
        self._metadata: ObservableModelMetadata = ObservableModelMetadata(
            created_at=created_at,
            created_on=created_on,
            type_="OBSERVABLE_QUESTION",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._next_view_on: ctk.StringVar = ctk.StringVar(value=next_view_on)
        self._priority: ctk.StringVar = ctk.StringVar(value=priority)
        self._subject: ctk.StringVar = ctk.StringVar(value=subject)
        self._tags: ctk.StringVar = ctk.StringVar(value=tags)
        self._teacher: ctk.StringVar = ctk.StringVar(value=teacher)
        self._text: ctk.StringVar = ctk.StringVar(value=text)

    @property
    def answers(self) -> ctk.StringVar:
        """
        The answers of the QuestionObservableModel.

        Returns:
            ctk.StringVar: The answers of the QuestionObservableModel.
        """
        return self._answers

    @answers.setter
    def answers(
        self,
        value: Union[list[str], str],
    ) -> None:
        if isinstance(
            value,
            str,
        ):
            self._answers.set(
                value=", ".join(
                    (
                        self._answers.get(),
                        value,
                    )
                )
            )

            return

        self._answers.set(value=", ".join(value))

    @property
    def author(self) -> ctk.StringVar:
        """
        The author of the QuestionObservableModel.

        Returns:
            ctk.StringVar: The author of the QuestionObservableModel.
        """
        return self._author

    @author.setter
    def author(
        self,
        value: str,
    ) -> None:
        self._author.set(value=value)

    @property
    def created_at(self) -> ctk.StringVar:
        """
        The creation timestamp of the QuestionObservableModel.

        Returns:
            ctk.StringVar: The creation timestamp of the QuestionObservableModel.
        """
        return self._metadata.created_at

    @property
    def created_on(self) -> ctk.StringVar:
        """
        The creation date of the QuestionObservableModel.

        Returns:
            ctk.StringVar: The creation date of the QuestionObservableModel.
        """
        return self._metadata.created_on

    @property
    def difficulty(self) -> ctk.StringVar:
        """
        The difficulty level of the QuestionObservableModel.

        Returns:
            ctk.StringVar: The difficulty level of the QuestionObservableModel.
        """
        return self._difficulty

    @difficulty.setter
    def difficulty(
        self,
        value: str,
    ) -> None:
        self._difficulty.set(value=value)

    @property
    def id(self) -> ctk.StringVar:
        """
        The unique identifier of the QuestionObservableModel.

        Returns:
            ctk.StringVar: The unique identifier of the QuestionObservableModel.
        """
        return self._identifiable.id

    @property
    def key(self) -> ctk.StringVar:
        """
        The key of the QuestionObservableModel.

        Returns:
            ctk.StringVar: The key of the QuestionObservableModel.
        """
        return self._identifiable.key

    @property
    def priority(self) -> ctk.StringVar:
        """
        The priority of the QuestionObservableModel.

        Returns:
            ctk.StringVar: The priority of the QuestionObservableModel.
        """
        return self._priority

    @priority.setter
    def priority(
        self,
        value: str,
    ) -> None:
        self._priority.set(value=value)

    @property
    def subject(self) -> ctk.StringVar:
        """
        The subject of the QuestionObservableModel.

        Returns:
            ctk.StringVar: The subject of the QuestionObservableModel.
        """
        return self._subject

    @subject.setter
    def subject(
        self,
        value: str,
    ) -> None:
        self._subject.set(value=value)

    @property
    def tags(self) -> ctk.StringVar:
        """
        The tags of the QuestionObservableModel.

        Returns:
            ctk.StringVar: The tags of the QuestionObservableModel.
        """
        return self._tags

    @tags.setter
    def tags(
        self,
        value: Union[list[str], str],
    ) -> None:
        if isinstance(
            value,
            str,
        ):
            self._tags.set(
                value=", ".join(
                    (
                        self._tags.get(),
                        value,
                    )
                )
            )

            return

        self._tags.set(value=", ".join(value))

    @property
    def teacher(self) -> ctk.StringVar:
        """
        The teacher of the QuestionObservableModel.

        Returns:
            ctk.StringVar: The teacher of the QuestionObservableModel.
        """
        return self._teacher

    @teacher.setter
    def teacher(
        self,
        value: str,
    ) -> None:
        self._teacher.set(value=value)

    @property
    def text(self) -> ctk.StringVar:
        """
        Returns the text of the QuestionObservableModel.

        Returns:
            ctk.StringVar: The text of the QuestionObservableModel.
        """
        return self._text

    @text.setter
    def text(
        self,
        value: str,
    ) -> None:
        self._text.set(value=value)

    @property
    def type(self) -> ctk.StringVar:
        """
        The type of the QuestionObservableModel.

        Returns:
            ctk.StringVar: The type of the QuestionObservableModel.
        """
        return self._metadata.type

    @property
    def updated_at(self) -> ctk.StringVar:
        """
        The last update timestamp of the QuestionObservableModel.

        Returns:
            ctk.StringVar: The last update timestamp of the QuestionObservableModel.
        """
        return self._metadata.updated_at

    @property
    def updated_on(self) -> ctk.StringVar:
        """
        The last update date of the QuestionObservableModel.

        Returns:
            ctk.StringVar: The last update date of the QuestionObservableModel.
        """
        return self._metadata.updated_on

    @property
    def uuid(self) -> ctk.StringVar:
        """
        The UUID of the QuestionObservableModel.

        Returns:
            ctk.StringVar: The UUID of the QuestionObservableModel.
        """
        return self._identifiable.uuid

    def reset(self) -> None:
        """
        Resets the variables of the given observable model.

        Returns:
            None
        """
        _reset_variables(observable_model=self)

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the observable model.

        Returns:
            dict[str, Any]: The observable model as a dictionary.
        """
        return _convert_to_dict(observable_model=self)


class StackObservableModel:
    """
    Represents a stack entity within the application.

    A stack is a collection of flashcards, questions, or notes that are
    grouped together for organization and management. This class utilizes
    composition by incorporating ObservableModelIdentifiable for identity
    management and ObservableModelMetadata for tracking lifecycle details.
    """

    def __init__(
        self,
        author: str = "",
        children: Union[list[str], str] = "",
        created_at: str = "",
        created_on: str = "",
        description: str = "",
        difficulty: str = "",
        id_: Union[int, str] = 0,
        items: Union[list[str], str] = "",
        key: str = "",
        name: str = "",
        parent: str = "",
        priority: str = "",
        subject: str = "",
        tags: Union[list[str], str] = "",
        teacher: str = "",
        updated_at: str = "",
        updated_on: str = "",
        uuid_: Union[str, uuid.UUID] = "",
    ) -> None:
        """
        Initializes a new StackObservableModel instance.

        Args:
            author (str): The name of the author of the stack. Defaults to an empty string.
            children (Union[list[str], str]): A list of keys representing the child stacks. Defaults to an empty string.
            created_at (str): The creation timestamp of the stack. Defaults to an empty string.
            created_on (str): The creation date of the stack. Defaults to an empty string.
            description (str): The description of the stack. Defaults to an empty string.
            difficulty (str): The difficulty level of the stack. Defaults to an empty string.
            id_ (Union[int, str]): The database ID of the stack. Defaults to an empty string.
            items (Union[list[str], str]): A list of keys representing the items in the stack. Defaults to an empty string.
            key (str): The key of the stack. Defaults to an empty string.
            name (str): The name of the stack. Defaults to an empty string.
            parent (str): The key of the parent stack. Defaults to an empty string.
            priority (str): The priority level of the stack. Defaults to an empty string.
            subject (str): The subject of the stack. Defaults to an empty string.
            tags (Union[list[str], str]): A list of tags associated with the stack. Defaults to an empty string.
            teacher (str): The name of the teacher who created the stack. Defaults to an empty string.
            updated_at (str): The last update timestamp of the stack. Defaults to an empty string.
            updated_on (str): The last update date of the stack. Defaults to an empty string.
            uuid_ (Union[str, uuid.UUID]): The universally unique identifier of the stack. Defaults to an empty string.

        Returns:
            None
        """

        self._author: ctk.StringVar = ctk.StringVar(value=author)
        self._children: ctk.StringVar = ctk.StringVar(value=children)
        self._description: ctk.StringVar = ctk.StringVar(value=description)
        self._difficulty: ctk.StringVar = ctk.StringVar(value=difficulty)
        self._identifiable: ObservableModelIdentifiable = ObservableModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._items: ctk.StringVar = ctk.StringVar(value=items)
        self._metadata: ObservableModelMetadata = ObservableModelMetadata(
            created_at=created_at,
            created_on=created_on,
            type_="OBSERVABLE_STACK",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._name: ctk.StringVar = ctk.StringVar(value=name)
        self._parent: ctk.StringVar = ctk.StringVar(value=parent)
        self._priority: ctk.StringVar = ctk.StringVar(value=priority)
        self._subject: ctk.StringVar = ctk.StringVar(value=subject)
        self._tags: ctk.StringVar = ctk.StringVar(value=tags)
        self._teacher: ctk.StringVar = ctk.StringVar(value=teacher)

    @property
    def author(self) -> ctk.StringVar:
        """
        The author of the StackObservableModel.

        Returns:
            ctk.StringVar: The author of the StackObservableModel.
        """
        return self._author

    @author.setter
    def author(
        self,
        value: str,
    ) -> None:
        self._author.set(value=value)

    @property
    def children(self) -> ctk.StringVar:
        """
        The children of the StackObservableModel.

        Returns:
            ctk.StringVar: The children of the StackObservableModel.
        """
        return self._children

    @children.setter
    def children(
        self,
        value: Union[list[str], str],
    ) -> None:
        if isinstance(
            value,
            str,
        ):
            self._children.set(
                value=", ".join(
                    (
                        self._children.get(),
                        value,
                    )
                )
            )

            return

        self._children.set(value=", ".join(value))

    @property
    def created_at(self) -> ctk.StringVar:
        """
        The creation timestamp of the StackObservableModel.

        Returns:
            ctk.StringVar: The creation timestamp of the StackObservableModel.
        """
        return self._metadata.created_at

    @property
    def created_on(self) -> ctk.StringVar:
        """
        The creation date of the StackObservableModel.

        Returns:
            ctk.StringVar: The creation date of the StackObservableModel.
        """
        return self._metadata.created_on

    @property
    def description(self) -> ctk.StringVar:
        """
        The description of the StackObservableModel.

        Returns:
            ctk.StringVar: The description of the StackObservableModel.
        """
        return self._description

    @description.setter
    def description(
        self,
        value: str,
    ) -> None:
        self._description.set(value=value)

    @property
    def difficulty(self) -> ctk.StringVar:
        """
        The difficulty level of the StackObservableModel.

        Returns:
            ctk.StringVar: The difficulty level of the StackObservableModel.
        """
        return self._difficulty

    @difficulty.setter
    def difficulty(
        self,
        value: str,
    ) -> None:
        self._difficulty.set(value=value)

    @property
    def id(self) -> ctk.StringVar:
        """
        The unique identifier of the StackObservableModel.

        Returns:
            ctk.StringVar: The unique identifier of the StackObservableModel.
        """
        return self._identifiable.id

    @property
    def items(self) -> ctk.StringVar:
        """
        The items of the StackObservableModel.

        Returns:
            ctk.StringVar: The items of the StackObservableModel.
        """
        return self._items

    @items.setter
    def items(
        self,
        value: Union[list[str], str],
    ) -> None:
        if isinstance(
            value,
            str,
        ):
            self._items.set(
                value=", ".join(
                    (
                        self._items.get(),
                        value,
                    )
                )
            )

            return

        self._items.set(value=", ".join(value))

    @property
    def key(self) -> ctk.StringVar:
        """
        The key of the StackObservableModel.

        Returns:
            ctk.StringVar: The key of the StackObservableModel.
        """
        return self._identifiable.key

    @property
    def name(self) -> ctk.StringVar:
        """
        The name of the StackObservableModel.

        Returns:
            ctk.StringVar: The name of the StackObservableModel.
        """
        return self._name

    @name.setter
    def name(
        self,
        value: str,
    ) -> None:
        self._name.set(value=value)

    @property
    def parent(self) -> ctk.StringVar:
        """
        The parent of the StackObservableModel.

        Returns:
            ctk.StringVar: The parent of the StackObservableModel.
        """
        return self._parent

    @parent.setter
    def parent(
        self,
        value: str,
    ) -> None:
        self._parent.set(value=value)

    @property
    def priority(self) -> ctk.StringVar:
        """
        The priority of the StackObservableModel.

        Returns:
            ctk.StringVar: The priority of the StackObservableModel.
        """
        return self._priority

    @priority.setter
    def priority(
        self,
        value: str,
    ) -> None:
        self._priority.set(value=value)

    @property
    def subject(self) -> ctk.StringVar:
        """
        The subject of the StackObservableModel.

        Returns:
            ctk.StringVar: The subject of the StackObservableModel.
        """
        return self._subject

    @subject.setter
    def subject(
        self,
        value: str,
    ) -> None:
        self._subject.set(value=value)

    @property
    def tags(self) -> ctk.StringVar:
        """
        The tags of the StackObservableModel.

        Returns:
            ctk.StringVar: The tags of the StackObservableModel.
        """
        return self._tags

    @tags.setter
    def tags(
        self,
        value: Union[list[str], str],
    ) -> None:
        if isinstance(
            value,
            str,
        ):
            self._tags.set(
                value=", ".join(
                    (
                        self._tags.get(),
                        value,
                    )
                )
            )

            return

        self._tags.set(value=", ".join(value))

    @property
    def teacher(self) -> ctk.StringVar:
        """
        The teacher of the StackObservableModel.

        Returns:
            ctk.StringVar: The teacher of the StackObservableModel.
        """
        return self._teacher

    @teacher.setter
    def teacher(
        self,
        value: str,
    ) -> None:
        self._teacher.set(value=value)

    @property
    def type(self) -> ctk.StringVar:
        """
        The type of the StackObservableModel.

        Returns:
            ctk.StringVar: The type of the StackObservableModel.
        """
        return self._metadata.type

    @property
    def updated_at(self) -> ctk.StringVar:
        """
        The last update timestamp of the StackObservableModel.

        Returns:
            ctk.StringVar: The last update timestamp of the StackObservableModel.
        """
        return self._metadata.updated_at

    @property
    def updated_on(self) -> ctk.StringVar:
        """
        The last update date of the StackObservableModel.

        Returns:
            ctk.StringVar: The last update date of the StackObservableModel.
        """
        return self._metadata.updated_on

    @property
    def uuid(self) -> ctk.StringVar:
        """
        The UUID of the StackObservableModel.

        Returns:
            ctk.StringVar: The UUID of the StackObservableModel.
        """
        return self._identifiable.uuid

    def reset(self) -> None:
        """
        Resets the variables of the given observable model.

        Returns:
            None
        """
        _reset_variables(observable_model=self)

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the observable model.

        Returns:
            dict[str, Any]: The observable model as a dictionary.
        """
        return _convert_to_dict(observable_model=self)


class SubjectObservableModel:
    """
    Represents a subject entity within the application.

    A subject represents a specific area of study, such as a language, a
    programming framework, or a scientific discipline. It acts as an
    organizational unit that can group various models such as
    flashcards, questions, or notes. This class utilizes composition by
    incorporating ObservableModelIdentifiable for identity management and
    ObservableModelMetadata for tracking lifecycle details.
    """

    def __init__(
        self,
        created_at: str = "",
        created_on: str = "",
        difficulty: str = "",
        id_: Optional[Union[int, str]] = None,
        key: str = "",
        name: str = "",
        priority: str = "",
        updated_at: str = "",
        updated_on: str = "",
        uuid_: Optional[Union[str, uuid.UUID]] = None,
    ) -> None:
        """
        Initialize a new SubjectObservableModel instance.

        Args:
            created_at (Optional[str]): The creation timestamp of the subject.
            created_on (Optional[str]): The creation date of the subject.
            difficulty (Optional[str]): The difficulty level of the subject.
            id_ (Optional[Union[int, str]]): The unique identifier of the subject.
            key (Optional[str]): The key of the subject.
            name (Optional[str]): The name of the subject.
            priority (Optional[str]): The priority of the subject.
            updated_at (Optional[str]): The last update timestamp of the subject.
            updated_on (Optional[str]): The last update date of the subject.
            uuid_ (Optional[uuid.UUID]): The UUID of the subject.

        Returns:
            None
        """

        self._difficulty: ctk.StringVar = ctk.StringVar(value=difficulty)
        self._identifiable: ObservableModelIdentifiable = ObservableModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._metadata: ObservableModelMetadata = ObservableModelMetadata(
            created_at=created_at,
            created_on=created_on,
            type_="OBSERVABLE_SUBJECT",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._name: ctk.StringVar = ctk.StringVar(value=name)
        self._priority: ctk.StringVar = ctk.StringVar(value=priority)

    @property
    def created_at(self) -> ctk.StringVar:
        """
        The creation timestamp of the SubjectObservableModel.

        Returns:
            ctk.StringVar: The creation timestamp of the SubjectObservableModel.
        """
        return self._metadata.created_at

    @property
    def created_on(self) -> ctk.StringVar:
        """
        The creation date of the SubjectObservableModel.

        Returns:
            ctk.StringVar: The creation date of the SubjectObservableModel.
        """
        return self._metadata.created_on

    @property
    def difficulty(self) -> ctk.StringVar:
        """
        The difficulty level of the SubjectObservableModel.

        Returns:
            ctk.StringVar: The difficulty level of the SubjectObservableModel.
        """
        return self._difficulty

    @property
    def id(self) -> ctk.StringVar:
        """
        The unique identifier of the SubjectObservableModel.

        Returns:
            ctk.StringVar: The unique identifier of the SubjectObservableModel.
        """
        return self._identifiable.id

    @property
    def key(self) -> ctk.StringVar:
        """
        The key of the SubjectObservableModel.

        Returns:
            ctk.StringVar: The key of the SubjectObservableModel.
        """
        return self._identifiable.key

    @property
    def name(self) -> ctk.StringVar:
        """
        The name of the SubjectObservableModel.

        Returns:
            ctk.StringVar: The name of the SubjectObservableModel.
        """
        return self._name

    @property
    def priority(self) -> ctk.StringVar:
        """
        The priority of the SubjectObservableModel.

        Returns:
            ctk.StringVar: The priority of the SubjectObservableModel.
        """
        return self._priority

    @property
    def type(self) -> ctk.StringVar:
        """
        The type of the SubjectObservableModel.

        Returns:
            ctk.StringVar: The type of the SubjectObservableModel.
        """
        return self._metadata.type

    @property
    def updated_at(self) -> ctk.StringVar:
        """
        The last update timestamp of the SubjectObservableModel.

        Returns:
            ctk.StringVar: The last update timestamp of the SubjectObservableModel.
        """
        return self._metadata.updated_at

    @property
    def updated_on(self) -> ctk.StringVar:
        """
        The last update date of the SubjectObservableModel.

        Returns:
            ctk.StringVar: The last update date of the SubjectObservableModel.
        """
        return self._metadata.updated_on

    @property
    def uuid(self) -> ctk.StringVar:
        """
        The UUID of the SubjectObservableModel.

        Returns:
            ctk.StringVar: The UUID of the SubjectObservableModel.
        """
        return self._identifiable.uuid

    def reset(self) -> None:
        """
        Resets the variables of the given observable model.

        Returns:
            None
        """
        _reset_variables(observable_model=self)

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the observable model.

        Returns:
            dict[str, Any]: The observable model as a dictionary.
        """
        return _convert_to_dict(observable_model=self)


class TagObservableModel:
    """
    Represents a tag entity within the application.

    A tag is an arbitrary, user-defined label that can be associated with
    subjects, students, or other educational content. This class utilizes
    composition by incorporating ObservableModelIdentifiable for identity
    management and ObservableModelMetadata for tracking lifecycle details.
    """

    def __init__(
        self,
        created_at: str = "",
        created_on: str = "",
        id_: Optional[Union[int, str]] = None,
        key: str = "",
        updated_at: str = "",
        updated_on: str = "",
        uuid_: Optional[Union[str, uuid.UUID]] = None,
        value: str = "",
    ) -> None:
        """
        Initializes a TagObservableModel instance.

        Args:
        created_at (str): The creation timestamp of the TagObservableModel.
        created_on (str): The creation date of the TagObservableModel.
        id_ (Optional[Union[int, str]]): The unique identifier of the TagObservableModel.
        key (str): The key of the TagObservableModel.
        updated_at (str): The last update timestamp of the TagObservableModel.
        updated_on (str): The last update date of the TagObservableModel.
        uuid_ (Optional[Union[str, uuid.UUID]]): The UUID of the TagObservableModel.
        value (str): The value of the TagObservableModel.

        Returns:
            None
        """

        self._identifiable = ObservableModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._metadata = ObservableModelMetadata(
            created_at=created_at,
            created_on=created_on,
            type_="OBSERVABLE_TAG",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._value = ctk.StringVar(value=value)

    @property
    def created_at(self) -> ctk.StringVar:
        """
        The creation timestamp of the TagObservableModel.

        Returns:
            ctk.StringVar: The creation timestamp of the TagObservableModel.
        """
        return self._metadata.created_at

    @property
    def created_on(self) -> ctk.StringVar:
        """
        The creation date of the TagObservableModel.

        Returns:
            ctk.StringVar: The creation date of the TagObservableModel.
        """
        return self._metadata.created_on

    @property
    def id(self) -> ctk.StringVar:
        """
        The unique identifier of the TagObservableModel.

        Returns:
            ctk.StringVar: The unique identifier of the TagObservableModel.
        """
        return self._identifiable.id

    @property
    def key(self) -> ctk.StringVar:
        """
        The key of the TagObservableModel.

        Returns:
            ctk.StringVar: The key of the TagObservableModel.
        """
        return self._identifiable.key

    @property
    def type(self) -> ctk.StringVar:
        """
        The type of the TagObservableModel.

        Returns:
            ctk.StringVar: The type of the TagObservableModel.
        """
        return self._metadata.type

    @property
    def updated_at(self) -> ctk.StringVar:
        """
        The last update timestamp of the TagObservableModel.

        Returns:
            ctk.StringVar: The last update timestamp of the TagObservableModel.
        """
        return self._metadata.updated_at

    @property
    def updated_on(self) -> ctk.StringVar:
        """
        The last update date of the TagObservableModel.

        Returns:
            ctk.StringVar: The last update date of the TagObservableModel.
        """
        return self._metadata.updated_on

    @property
    def uuid(self) -> ctk.StringVar:
        """
        The UUID of the TagObservableModel.

        Returns:
            ctk.StringVar: The UUID of the TagObservableModel.
        """
        return self._identifiable.uuid

    @property
    def value(self) -> ctk.StringVar:
        """
        The value of the TagObservableModel.

        Returns:
            ctk.StringVar: The value of the TagObservableModel.
        """
        return self._value

    def reset(self) -> None:
        """
        Resets the variables of the given observable model.

        Returns:
            None
        """
        _reset_variables(observable_model=self)

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the observable model.

        Returns:
            dict[str, Any]: The observable model as a dictionary.
        """
        return _convert_to_dict(observable_model=self)


class TeacherObservableModel:
    """
    Represents a teacher entity within the application.

    A teacher represents an instructor or educator who can be associated with
    subjects, students, or other educational content. This class utilizes
    composition by incorporating ObservableModelIdentifiable for identity
    management and ObservableModelMetadata for tracking lifecycle details.
    """

    def __init__(
        self,
        created_at: str = "",
        created_on: str = "",
        difficulty: str = "",
        id_: Optional[Union[int, str]] = None,
        key: str = "",
        name: str = "",
        priority: str = "",
        updated_at: str = "",
        updated_on: str = "",
        uuid_: Optional[Union[str, uuid.UUID]] = None,
    ) -> None:
        """
        Initialize a new TeacherObservableModel instance.

        Args:
            created_at (Optional[str]): The creation timestamp of the teacher.
            created_on (Optional[str]): The creation date of the teacher.
            difficulty (Optional[str]): The difficulty level of the teacher.
            id_ (Optional[Union[int, str]]): The unique identifier of the teacher.
            key (Optional[str]): The key of the teacher.
            name (Optional[str]): The name of the teacher.
            priority (Optional[str]): The priority of the teacher.
            updated_at (Optional[str]): The last update timestamp of the teacher.
            updated_on (Optional[str]): The last update date of the teacher.
            uuid_ (Optional[Union[str, uuid.UUID]]): The UUID of the teacher.

        Returns:
            None
        """

        self._difficulty: ctk.StringVar = ctk.StringVar(value=difficulty)
        self._identifiable: ObservableModelIdentifiable = ObservableModelIdentifiable(
            id_=id_,
            key=key,
            uuid_=uuid_,
        )
        self._metadata: ObservableModelMetadata = ObservableModelMetadata(
            created_at=created_at,
            created_on=created_on,
            type_="OBSERVABLE_TEACHER",
            updated_at=updated_at,
            updated_on=updated_on,
        )
        self._name: ctk.StringVar = ctk.StringVar(value=name)
        self._priority: ctk.StringVar = ctk.StringVar(value=priority)

    @property
    def created_at(self) -> ctk.StringVar:
        """
        The creation timestamp of the TeacherObservableModel.

        Returns:
            ctk.StringVar: The creation timestamp of the TeacherObservableModel.
        """
        return self._metadata.created_at

    @property
    def created_on(self) -> ctk.StringVar:
        """
        The creation date of the TeacherObservableModel.

        Returns:
            ctk.StringVar: The creation date of the TeacherObservableModel.
        """
        return self._metadata.created_on

    @property
    def difficulty(self) -> ctk.StringVar:
        """
        The difficulty level of the TeacherObservableModel.

        Returns:
            ctk.StringVar: The difficulty level of the TeacherObservableModel.
        """
        return self._difficulty

    @property
    def id(self) -> ctk.StringVar:
        """
        The unique identifier of the TeacherObservableModel.

        Returns:
            ctk.StringVar: The unique identifier of the TeacherObservableModel.
        """
        return self._identifiable.id

    @property
    def key(self) -> ctk.StringVar:
        """
        The key of the TeacherObservableModel.

        Returns:
            ctk.StringVar: The key of the TeacherObservableModel.
        """
        return self._identifiable.key

    @property
    def name(self) -> ctk.StringVar:
        """
        The name of the TeacherObservableModel.

        Returns:
            ctk.StringVar: The name of the TeacherObservableModel.
        """
        return self._name

    @property
    def priority(self) -> ctk.StringVar:
        """
        The priority of the TeacherObservableModel.

        Returns:
            ctk.StringVar: The priority of the TeacherObservableModel.
        """
        return self._priority

    @property
    def type(self) -> ctk.StringVar:
        """
        The type of the TeacherObservableModel.

        Returns:
            ctk.StringVar: The type of the TeacherObservableModel.
        """
        return self._metadata.type

    @property
    def updated_at(self) -> ctk.StringVar:
        """
        The last update timestamp of the TeacherObservableModel.

        Returns:
            ctk.StringVar: The last update timestamp of the TeacherObservableModel.
        """
        return self._metadata.updated_at

    @property
    def updated_on(self) -> ctk.StringVar:
        """
        The last update date of the TeacherObservableModel.

        Returns:
            ctk.StringVar: The last update date of the TeacherObservableModel.
        """
        return self._metadata.updated_on

    @property
    def uuid(self) -> ctk.StringVar:
        """
        The UUID of the TeacherObservableModel.

        Returns:
            ctk.StringVar: The UUID of the TeacherObservableModel.
        """
        return self._identifiable.uuid

    def reset(self) -> None:
        """
        Resets the variables of the given observable model.

        Returns:
            None
        """
        _reset_variables(observable_model=self)

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the observable model.

        Returns:
            dict[str, Any]: The observable model as a dictionary.
        """
        return _convert_to_dict(observable_model=self)
