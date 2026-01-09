"""
Author: Louis Goodnews
Date: 2026-01-09
Description: This module contains the factory methods for creating model instances
"""

from datetime import date, datetime
from typing import Any, Final, Optional, Union
import uuid

from models.models import (
    Answer,
    Association,
    Customfield,
    Difficulty,
    Flashcard,
    Image,
    Model,
    Note,
    Option,
    Priority,
    Question,
    RehearsalAction,
    RehearsalRun,
    RehearsalRunItem,
    Stack,
    Subject,
    Tag,
    Teacher,
    User,
)
from utils.common import date_from_string, datetime_from_string, exists, uuid_from_string

# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "get_answer_model",
    "get_association_model",
    "get_customfield_model",
    "get_difficulty_model",
    "get_flashcard_model",
    "get_image_model",
    "get_model_model",
    "get_note_model",
    "get_option_model",
    "get_priority_model",
    "get_question_model",
    "get_rehearsal_action_model",
    "get_rehearsal_run_model",
    "get_rehearsal_run_item_model",
    "get_stack_model",
    "get_subject_model",
    "get_tag_model",
    "get_teacher_model",
    "get_user_model",
]


# ---------- Helper Functions ---------- #


def _convert_parameters(**kwargs) -> dict[str, Any]:
    """
    Converts model parameters from strings to their appropriate types.

    This function iterates over the given keyword arguments and checks
    if the value is a string. If it is, it attempts to convert the
    string to the appropriate type (datetime or date) depending on the
    key. If the conversion is successful, it updates the dictionary
    with the converted value.

    Args:
        **kwargs: A dictionary of keyword arguments.

    Returns:
        dict[str, Any]: The updated dictionary with converted values.
    """

    for (
        key,
        value,
    ) in kwargs.items():
        if key in {
            "created_at",
            "updated_at",
        }:
            if not exists(value=value):
                continue

            if isinstance(
                value,
                datetime,
            ):
                continue

            kwargs[key] = datetime_from_string(string=value)

        elif key in {
            "created_on",
            "updated_on",
        }:
            if not exists(value=value):
                continue

            if isinstance(
                value,
                date,
            ):
                continue

            kwargs[key] = date_from_string(string=value)

        elif key == "uuid_":
            if not exists(value=value):
                continue

            if isinstance(
                value,
                uuid.UUID,
            ):
                continue

            kwargs[key] = uuid_from_string(string=value)

    return kwargs


# ---------- Public Functions ---------- #


def get_answer_model(
    is_correct: bool,
    text: str,
    created_at: Optional[Union[datetime, str]] = None,
    created_on: Optional[Union[date, str]] = None,
    customfields: Optional[list[dict[str, Any]]] = None,
    id_: Optional[Union[int, str]] = None,
    key: Optional[str] = None,
    updated_at: Optional[Union[datetime, str]] = None,
    updated_on: Optional[Union[date, str]] = None,
    uuid_: Optional[Union[str, uuid.UUID]] = None,
) -> Model:
    """
    Creates and returns an instance of the Answer model with full metadata support.

    This factory method encapsulates the instantiation of the Answer class. It allows
    for the creation of simple answer objects as well as complex ones with pre-defined
    lifecycle metadata, identifiers, and custom fields, ensuring consistency across
    the application's data layer.

    Args:
        is_correct (bool): Indicates whether this answer is considered correct.
        text (str): The actual text content of the answer.
        created_at (Optional[str]): ISO-formatted timestamp of when the answer was created.
        created_on (Optional[str]): ISO-formatted date of when the answer was created.
        customfields (Optional[list[dict[str, Any]]]): A list of dictionaries containing
            user-defined metadata fields.
        id_ (Optional[Union[int, str]]): The internal database ID for the answer.
        key (Optional[str]): A unique string identifier for the model.
        updated_at (Optional[str]): ISO-formatted timestamp of the last modification.
        updated_on (Optional[str]): ISO-formatted date of the last modification.
        uuid_ (Optional[str]): A string representation of the universally unique identifier.

    Returns:
        Model: An instance of the Answer class, typed as the Model alias.
    """

    parameters: dict[str, Any] = _convert_parameters(**locals().copy())

    return Answer(**parameters)


def get_association_model(
    answer: Optional[Union[int, str]] = None,
    created_at: Optional[Union[datetime, str]] = None,
    created_on: Optional[Union[date, str]] = None,
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
    updated_at: Optional[Union[datetime, str]] = None,
    updated_on: Optional[Union[date, str]] = None,
    user: Optional[Union[int, str]] = None,
    uuid_: Optional[Union[str, uuid.UUID]] = None,
) -> Association:
    """
    Creates and returns an instance of the Association model.

    This factory method facilitates the creation of Association entities, which link
    various models within the application (e.g., connecting a Flashcard to a Tag
    or a Question to a Subject). It automatically handles the conversion of
    string-based metadata into the appropriate Python objects.

    Args:
        answer (Optional[Union[int, str]]): Reference to an Answer model.
        created_at (Optional[str]): ISO-formatted creation timestamp.
        created_on (Optional[str]): ISO-formatted creation date.
        customfield (Optional[Union[int, str]]): Reference to a Customfield model.
        difficulty (Optional[Union[int, str]]): Reference to a Difficulty model.
        flashcard (Optional[Union[int, str]]): Reference to a Flashcard model.
        id_ (Optional[Union[int, str]]): Internal database identifier.
        image (Optional[Union[int, str]]): Reference to an Image model.
        key (Optional[str]): Unique model key identifier.
        note (Optional[Union[int, str]]): Reference to a Note model.
        option (Optional[Union[int, str]]): Reference to an Option model.
        question (Optional[Union[int, str]]): Reference to a Question model.
        rehearsal_run (Optional[Union[int, str]]): Reference to a RehearsalRun model.
        rehearsal_run_item (Optional[Union[int, str]]): Reference to a RehearsalRunItem model.
        stack (Optional[Union[int, str]]): Reference to a Stack model.
        subject (Optional[Union[int, str]]): Reference to a Subject model.
        tag (Optional[Union[int, str]]): Reference to a Tag model.
        teacher (Optional[Union[int, str]]): Reference to a Teacher model.
        updated_at (Optional[str]): ISO-formatted last update timestamp.
        updated_on (Optional[str]): ISO-formatted last update date.
        uuid_ (Optional[str]): Universally unique identifier string.

    Returns:
        Model: An instance of the Association class.
    """

    parameters: dict[str, Any] = _convert_parameters(**locals().copy())

    return Association(**parameters)


def get_customfield_model(
    name: str,
    created_at: Optional[Union[datetime, str]] = None,
    created_on: Optional[Union[date, str]] = None,
    id_: Optional[Union[int, str]] = None,
    key: Optional[str] = None,
    options: Optional[list[str]] = None,
    updated_at: Optional[Union[datetime, str]] = None,
    updated_on: Optional[Union[date, str]] = None,
    uuid_: Optional[Union[str, uuid.UUID]] = None,
) -> Customfield:
    """
    Creates and returns an instance of the Customfield model.

    This factory method initializes a Customfield entity, which defines dynamic
    metadata structures for other models. It supports predefined options (e.g.,
    for dropdown selections) and automatically converts string-based lifecycle
    metadata and identifiers into their proper Python types.

    Args:
        name (str): The display name or label of the custom field.
        created_at (Optional[str]): ISO-formatted creation timestamp.
        created_on (Optional[str]): ISO-formatted creation date.
        id_ (Optional[Union[int, str]]): Internal database identifier.
        key (Optional[str]): Unique model key identifier.
        options (Optional[list[str]]): A list of available choices or
            configuration strings for the field.
        updated_at (Optional[str]): ISO-formatted last update timestamp.
        updated_on (Optional[str]): ISO-formatted last update date.
        uuid_ (Optional[str]): Universally unique identifier string.

    Returns:
        Model: An instance of the Customfield class.
    """

    parameters: dict[str, Any] = _convert_parameters(**locals().copy())

    return Customfield(**parameters)


def get_difficulty_model(
    display_name: str,
    name: str,
    value: float,
    created_at: Optional[Union[datetime, str]] = None,
    created_on: Optional[Union[date, str]] = None,
    id_: Optional[Union[int, str]] = None,
    key: Optional[str] = None,
    updated_at: Optional[Union[datetime, str]] = None,
    updated_on: Optional[Union[date, str]] = None,
    uuid_: Optional[Union[str, uuid.UUID]] = None,
) -> Difficulty:
    """
    Creates and returns an instance of the Difficulty model.

    This factory method initializes a Difficulty entity, which is used to categorize
    the complexity of learning materials. It maps a human-readable display name
    and an internal name to a numeric weight (value). Lifecycle metadata and
    identifiers are automatically converted from strings to their appropriate
    Python types.

    Args:
        display_name (str): The localized or user-friendly name of the difficulty level.
        name (str): The internal unique name or identifier for the difficulty level.
        value (float): The numeric weight or score representing the difficulty.
        created_at (Optional[str]): ISO-formatted creation timestamp.
        created_on (Optional[str]): ISO-formatted creation date.
        id_ (Optional[Union[int, str]]): Internal database identifier.
        key (Optional[str]): Unique model key identifier.
        updated_at (Optional[str]): ISO-formatted last update timestamp.
        updated_on (Optional[str]): ISO-formatted last update date.
        uuid_ (Optional[str]): Universally unique identifier string.

    Returns:
        Model: An instance of the Difficulty class.
    """

    parameters: dict[str, Any] = _convert_parameters(**locals().copy())

    return Difficulty(**parameters)


def get_flashcard_model(
    back: str,
    front: str,
    author: Optional[str] = None,
    created_at: Optional[Union[datetime, str]] = None,
    created_on: Optional[Union[date, str]] = None,
    customfields: Optional[list[dict[str, Any]]] = None,
    difficulty: Optional[str] = None,
    id_: Optional[Union[int, str]] = None,
    is_assigned_to_stack: bool = False,
    key: Optional[str] = None,
    last_viewed_at: Optional[str] = None,
    last_viewed_on: Optional[str] = None,
    next_view_on: Optional[str] = None,
    priority: Optional[str] = None,
    subject: Optional[str] = None,
    tags: Optional[list[str]] = None,
    teacher: Optional[str] = None,
    updated_at: Optional[Union[datetime, str]] = None,
    updated_on: Optional[Union[date, str]] = None,
    uuid_: Optional[Union[str, uuid.UUID]] = None,
) -> Flashcard:
    """
    Creates and returns an instance of the Flashcard model with comprehensive metadata.

    This factory method initializes a Flashcard entity, which represents the primary
    learning unit. It handles the core content (front and back) along with
    associative data (subject, teacher, tags), scheduling information (next view date),
    and standard lifecycle metadata. String-based timestamps and identifiers are
    automatically converted into appropriate Python objects.

    Args:
        back (str): The content on the back of the flashcard (usually the answer).
        front (str): The content on the front of the flashcard (usually the question).
        author (Optional[str]): The identifier of the user who created the card.
        created_at (Optional[str]): ISO-formatted creation timestamp.
        created_on (Optional[str]): ISO-formatted creation date.
        customfields (Optional[list[dict[str, Any]]]): List of custom metadata dictionaries.
        difficulty (Optional[str]): Reference key for the associated Difficulty level.
        id_ (Optional[Union[int, str]]): Internal database identifier.
        is_assigned_to_stack (bool): Indicates if the card belongs to a specific stack.
        key (Optional[str]): Unique model key identifier.
        last_viewed_at (Optional[str]): ISO-formatted timestamp of the last review.
        last_viewed_on (Optional[str]): ISO-formatted date of the last review.
        next_view_on (Optional[str]): ISO-formatted date for the next scheduled review.
        priority (Optional[str]): Reference key for the associated Priority level.
        subject (Optional[str]): Reference key for the associated Subject.
        tags (Optional[list[str]]): A list of tag keys associated with this card.
        teacher (Optional[str]): Reference key for the associated Teacher.
        updated_at (Optional[str]): ISO-formatted last update timestamp.
        updated_on (Optional[str]): ISO-formatted last update date.
        uuid_ (Optional[str]): Universally unique identifier string.

    Returns:
        Model: An instance of the Flashcard class.
    """

    parameters: dict[str, Any] = _convert_parameters(**locals().copy())

    return Flashcard(**parameters)


def get_image_model(
    name: str,
    path: Path,
    created_at: Optional[Union[datetime, str]] = None,
    created_on: Optional[Union[date, str]] = None,
    fields: Optional[dict[str, Any]] = None,
    id_: Optional[Union[int, str]] = None,
    key: Optional[str] = None,
    updated_at: Optional[Union[datetime, str]] = None,
    updated_on: Optional[Union[date, str]] = None,
    uuid_: Optional[Union[str, uuid.UUID]] = None,
) -> Image:
    """
    Creates and returns an instance of the Image model.

    This factory method initializes an Image entity, which serves as a container
    for visual resource references. It automatically processes string-based
    lifecycle metadata and identifiers, converting them into their appropriate
    Python types via internal helper functions.

    Args:
        name (str): The descriptive name or label for the image.
        path (Path): The file system path where the image is located.
        created_at (Optional[str]): ISO-formatted creation timestamp.
        created_on (Optional[str]): ISO-formatted creation date.
        fields (Optional[dict[str, Any]]): A dictionary containing dynamic
            metadata or additional properties.
        id_ (Optional[Union[int, str]]): Internal database identifier.
        key (Optional[str]): Unique model key identifier.
        updated_at (Optional[str]): ISO-formatted last update timestamp.
        updated_on (Optional[str]): ISO-formatted last update date.
        uuid_ (Optional[str]): Universally unique identifier string.

    Returns:
        Image: An instance of the Image class.
    """

    parameters: dict[str, Any] = _convert_parameters(**locals().copy())

    return Image(**parameters)


def _get_note_model(
    text: str,
    title: str,
    author: Optional[str] = None,
    created_at: Optional[Union[datetime, str]] = None,
    created_on: Optional[Union[date, str]] = None,
    customfields: Optional[list[dict[str, Any]]] = None,
    difficulty: Optional[str] = None,
    id_: Optional[Union[int, str]] = None,
    is_assigned_to_stack: bool = False,
    key: Optional[str] = None,
    last_viewed_at: Optional[str] = None,
    last_viewed_on: Optional[str] = None,
    next_view_on: Optional[str] = None,
    priority: Optional[str] = None,
    subject: Optional[str] = None,
    tags: Optional[list[str]] = None,
    teacher: Optional[str] = None,
    updated_at: Optional[Union[datetime, str]] = None,
    updated_on: Optional[Union[date, str]] = None,
    uuid_: Optional[Union[str, uuid.UUID]] = None,
) -> Note:
    """
    Creates and returns an instance of the Note model.

    This method handles the instantiation of a Note entity, which represents
    longer educational texts or annotations. It processes the core content
    (title and text), organizational links (subject, teacher, tags), and
    scheduling metadata. String-based identifiers and timestamps are
    automatically converted into their corresponding Python types.

    Args:
        text (str): The main body content of the note.
        title (str): The title or headline of the note.
        author (Optional[str]): Identifier of the user who created the note.
        created_at (Optional[str]): ISO-formatted creation timestamp.
        created_on (Optional[str]): ISO-formatted creation date.
        customfields (Optional[list[dict[str, Any]]]): Custom metadata list.
        difficulty (Optional[str]): Reference key for the difficulty level.
        id_ (Optional[Union[int, str]]): Internal database identifier.
        is_assigned_to_stack (bool): Whether the note belongs to a stack.
        key (Optional[str]): Unique model key identifier.
        last_viewed_at (Optional[str]): ISO-formatted last review timestamp.
        last_viewed_on (Optional[str]): ISO-formatted last review date.
        next_view_on (Optional[str]): ISO-formatted next scheduled review date.
        priority (Optional[str]): Reference key for the priority level.
        subject (Optional[str]): Reference key for the associated subject.
        tags (Optional[list[str]]): List of tag keys associated with the note.
        teacher (Optional[str]): Reference key for the associated teacher.
        updated_at (Optional[str]): ISO-formatted last update timestamp.
        updated_on (Optional[str]): ISO-formatted last update date.
        uuid_ (Optional[str]): Universally unique identifier string.

    Returns:
        Note: A fully initialized instance of the Note class.
    """

    parameters: dict[str, Any] = _convert_parameters(**locals().copy())

    return Note(**parameters)


def get_option_model(
    value: Any,
    created_at: Optional[Union[datetime, str]] = None,
    created_on: Optional[Union[date, str]] = None,
    id_: Optional[Union[int, str]] = None,
    key: Optional[str] = None,
    updated_at: Optional[Union[datetime, str]] = None,
    updated_on: Optional[Union[date, str]] = None,
    uuid_: Optional[Union[str, uuid.UUID]] = None,
) -> Option:
    """
    Creates and returns an instance of the Option model.

    This factory method initializes an Option entity, typically used as a choice
    within a question or a selection list. It handles the core value of the
    option and ensures that all lifecycle metadata and identifiers are
    properly converted from strings into their respective Python types.

    Args:
        value (Any): The content or value of the option (e.g., a string or number).
        created_at (Optional[str]): ISO-formatted creation timestamp.
        created_on (Optional[str]): ISO-formatted creation date.
        id_ (Optional[Union[int, str]]): Internal database identifier.
        key (Optional[str]): Unique model key identifier.
        updated_at (Optional[str]): ISO-formatted last update timestamp.
        updated_on (Optional[str]): ISO-formatted last update date.
        uuid_ (Optional[str]): Universally unique identifier string.

    Returns:
        Option: A fully initialized instance of the Option class.
    """

    parameters: dict[str, Any] = _convert_parameters(**locals().copy())

    return Option(**parameters)


def get_priority_model(
    display_name: str,
    name: str,
    value: float,
    created_at: Optional[Union[datetime, str]] = None,
    created_on: Optional[Union[date, str]] = None,
    id_: Optional[Union[int, str]] = None,
    key: Optional[str] = None,
    updated_at: Optional[Union[datetime, str]] = None,
    updated_on: Optional[Union[date, str]] = None,
    uuid_: Optional[Union[str, uuid.UUID]] = None,
) -> Priority:
    """
    Creates and returns an instance of the Priority model.

    This factory method initializes a Priority entity, which is used to categorize
    the complexity of learning materials. It maps a human-readable display name
    and an internal name to a numeric weight (value). Lifecycle metadata and
    identifiers are automatically converted from strings to their appropriate
    Python types.

    Args:
        display_name (str): The localized or user-friendly name of the priority level.
        name (str): The internal unique name or identifier for the priority level.
        value (float): The numeric weight or score representing the priority.
        created_at (Optional[str]): ISO-formatted creation timestamp.
        created_on (Optional[str]): ISO-formatted creation date.
        id_ (Optional[Union[int, str]]): Internal database identifier.
        key (Optional[str]): Unique model key identifier.
        updated_at (Optional[str]): ISO-formatted last update timestamp.
        updated_on (Optional[str]): ISO-formatted last update date.
        uuid_ (Optional[str]): Universally unique identifier string.

    Returns:
        Model: An instance of the Priority class.
    """

    parameters: dict[str, Any] = _convert_parameters(**locals().copy())

    return Priority(**parameters)


def get_question_model(
    text: str,
    answers: Optional[list[str]] = None,
    author: Optional[str] = None,
    created_at: Optional[Union[datetime, str]] = None,
    created_on: Optional[Union[date, str]] = None,
    customfields: Optional[list[dict[str, Any]]] = None,
    difficulty: Optional[str] = None,
    id_: Optional[Union[int, str]] = None,
    is_assigned_to_stack: bool = False,
    key: Optional[str] = None,
    last_viewed_at: Optional[str] = None,
    last_viewed_on: Optional[str] = None,
    next_view_on: Optional[str] = None,
    priority: Optional[str] = None,
    subject: Optional[str] = None,
    tags: Optional[list[str]] = None,
    teacher: Optional[str] = None,
    updated_at: Optional[Union[datetime, str]] = None,
    updated_on: Optional[Union[date, str]] = None,
    uuid_: Optional[Union[str, uuid.UUID]] = None,
) -> Question:
    """
    Creates and returns an instance of the Question model.

    This factory method initializes a Question entity, which represents an
    interrogative learning unit. It manages the association with multiple
    answers, organizational categories (subject, teacher, tags), and
    learning progress data (scheduling and difficulty). String-based
    lifecycle metadata and identifiers are automatically converted into
    the appropriate Python types.

    Args:
        text (str): The actual text of the question.
        answers (Optional[list[str]]): A list of keys referring to the associated Answer models.
        author (Optional[str]): Identifier of the user who created the question.
        created_at (Optional[str]): ISO-formatted creation timestamp.
        created_on (Optional[str]): ISO-formatted creation date.
        customfields (Optional[list[dict[str, Any]]]): A list of custom metadata dictionaries.
        difficulty (Optional[str]): Reference key for the associated Difficulty level.
        id_ (Optional[Union[int, str]]): Internal database identifier.
        is_assigned_to_stack (bool): Indicates if the question is currently part of a stack.
        key (Optional[str]): Unique model key identifier.
        last_viewed_at (Optional[str]): ISO-formatted timestamp of the last time this question was seen.
        last_viewed_on (Optional[str]): ISO-formatted date of the last time this question was seen.
        next_view_on (Optional[str]): ISO-formatted date for the next scheduled review.
        priority (Optional[str]): Reference key for the associated Priority level.
        subject (Optional[str]): Reference key for the associated Subject.
        tags (Optional[list[str]]): A list of tag keys associated with this question.
        teacher (Optional[str]): Reference key for the associated Teacher.
        updated_at (Optional[str]): ISO-formatted timestamp of the last modification.
        updated_on (Optional[str]): ISO-formatted date of the last modification.
        uuid_ (Optional[str]): Universally unique identifier string.

    Returns:
        Question: A fully initialized instance of the Question class.
    """

    parameters: dict[str, Any] = _convert_parameters(**locals().copy())

    return Question(**parameters)


def get_rehearsal_action_model(
    action_data: dict[str, Any],
    message: str,
    timestamp: str,
    created_at: Optional[Union[datetime, str]] = None,
    created_on: Optional[Union[date, str]] = None,
    id_: Optional[Union[int, str]] = None,
    key: Optional[str] = None,
    updated_at: Optional[Union[datetime, str]] = None,
    updated_on: Optional[Union[date, str]] = None,
    uuid_: Optional[Union[str, uuid.UUID]] = None,
) -> RehearsalAction:
    """
    Creates and returns an instance of the RehearsalAction model.

    This factory method initializes a RehearsalAction entity, which logs a specific
    event or user interaction during a learning session. It stores structured
    data about the action, a descriptive message, and the exact timing of the
    event. String-based timestamps and identifiers are automatically converted
    into their corresponding Python types.

    Args:
        action_data (dict[str, Any]): A dictionary containing specific data or
            parameters related to the logged action.
        message (str): A human-readable description of the action.
        timestamp (str): ISO-formatted string representing when the action occurred.
        created_at (Optional[str]): ISO-formatted creation timestamp.
        created_on (Optional[str]): ISO-formatted creation date.
        id_ (Optional[Union[int, str]]): Internal database identifier.
        key (Optional[str]): Unique model key identifier.
        updated_at (Optional[str]): ISO-formatted last update timestamp.
        updated_on (Optional[str]): ISO-formatted last update date.
        uuid_ (Optional[str]): Universally unique identifier string.

    Returns:
        RehearsalAction: A fully initialized instance of the RehearsalAction class.
    """

    parameters: dict[str, Any] = _convert_parameters(**locals().copy())

    return RehearsalAction(**parameters)


def get_rehearsal_run_item(
    item: str,
    actions: Optional[list[str]] = None,
    completed_at: Optional[Union[datetime, str]] = None,
    created_at: Optional[Union[datetime, str]] = None,
    created_on: Optional[Union[date, str]] = None,
    id_: Optional[Union[int, str]] = None,
    key: Optional[str] = None,
    result: Optional[str] = None,
    started_at: Optional[Union[datetime, str]] = None,
    updated_at: Optional[Union[datetime, str]] = None,
    updated_on: Optional[Union[date, str]] = None,
    uuid_: Optional[Union[str, uuid.UUID]] = None,
) -> RehearsalRunItem:
    """
    Creates and returns an instance of the RehearsalRunItem model.

    This factory method initializes a RehearsalRunItem, which tracks the progress
    and outcome of a specific learning unit (like a Flashcard or Question) within
    a rehearsal session. It records timing data, the resulting performance, and
    associated actions. String-based timestamps and identifiers are
    automatically converted into their appropriate Python types.

    Args:
        item (str): Reference key to the model being rehearsed (e.g., a Flashcard key).
        actions (Optional[list[str]]): A list of keys referring to RehearsalAction logs.
        completed_at (Optional[str]): ISO-formatted timestamp of when the item was finished.
        created_at (Optional[str]): ISO-formatted creation timestamp.
        created_on (Optional[str]): ISO-formatted creation date.
        id_ (Optional[Union[int, str]]): Internal database identifier.
        key (Optional[str]): Unique model key identifier.
        result (Optional[str]): The outcome of the rehearsal (e.g., 'correct', 'wrong').
        started_at (Optional[str]): ISO-formatted timestamp of when the item was started.
        updated_at (Optional[str]): ISO-formatted last update timestamp.
        updated_on (Optional[str]): ISO-formatted last update date.
        uuid_ (Optional[str]): Universally unique identifier string.

    Returns:
        RehearsalRunItem: A fully initialized instance of the RehearsalRunItem class.
    """

    parameters: dict[str, Any] = _convert_parameters(**locals().copy())

    return RehearsalRunItem(**parameters)


def get_rehearsal_run_model(
    stacks: list[str],
    configuration: dict[str, Any],
    author: Optional[str] = None,
    completed_at: Optional[Union[datetime, str]] = None,
    completed_on: Optional[Union[date, str]] = None,
    created_at: Optional[Union[datetime, str]] = None,
    created_on: Optional[Union[date, str]] = None,
    customfields: Optional[list[dict[str, Any]]] = None,
    duration: Optional[dict[str, float]] = None,
    id_: Optional[Union[int, str]] = None,
    is_finished: bool = False,
    items: Optional[dict[str, str]] = None,
    key: Optional[str] = None,
    scheduled_at: Optional[Union[datetime, str]] = None,
    scheduled_on: Optional[Union[date, str]] = None,
    started_at: Optional[Union[datetime, str]] = None,
    started_on: Optional[Union[date, str]] = None,
    updated_at: Optional[Union[datetime, str]] = None,
    updated_on: Optional[Union[date, str]] = None,
    uuid_: Optional[Uninon[str, uid.UUID]] = None,
) -> RehearsalRun:
    """
    Creates and returns an instance of the RehearsalRun model.

    This factory method initializes a RehearsalRun entity, which represents a complete
    learning session. It manages the session configuration, the associated stacks,
    and tracks the overall progress including start, completion, and duration.
    String-based timestamps and identifiers are automatically converted into
    their appropriate Python objects.

    Args:
        stacks (list[str]): A list of keys referring to the Stacks included in this run.
        configuration (dict[str, Any]): Dictionary containing session-specific settings.
        author (Optional[str]): Identifier of the user who initiated the run.
        completed_at (Optional[str]): ISO-formatted timestamp of session completion.
        completed_on (Optional[str]): ISO-formatted date of session completion.
        created_at (Optional[str]): ISO-formatted creation timestamp.
        created_on (Optional[str]): ISO-formatted creation date.
        customfields (Optional[list[dict[str, Any]]]): List of custom metadata dictionaries.
        duration (Optional[dict[str, float]]): Dictionary tracking time spent in the session.
        id_ (Optional[Union[int, str]]): Internal database identifier.
        is_finished (bool): Flag indicating if the rehearsal session has ended.
        items (Optional[dict[str, str]]): Mapping of RehearsalRunItem keys within this run.
        key (Optional[str]): Unique model key identifier.
        scheduled_at (Optional[str]): ISO-formatted timestamp for the scheduled start.
        scheduled_on (Optional[str]): ISO-formatted date for the scheduled start.
        started_at (Optional[str]): ISO-formatted timestamp of when the session actually began.
        started_on (Optional[str]): ISO-formatted date of when the session actually began.
        updated_at (Optional[str]): ISO-formatted last update timestamp.
        updated_on (Optional[str]): ISO-formatted last update date.
        uuid_ (Optional[str]): Universally unique identifier string.

    Returns:
        RehearsalRun: A fully initialized instance of the RehearsalRun class.
    """

    parameters: dict[str, Any] = _convert_parameters(**locals().copy())

    return RehearsalRun(**parameters)


def get_stack_model(
    name: str,
    author: Optional[str] = None,
    children: Optional[list[str]] = None,
    created_at: Optional[Union[datetime, str]] = None,
    created_on: Optional[Union[date, str]] = None,
    customfields: Optional[list[dict[str, Any]]] = None,
    difficulty: Optional[str] = None,
    id_: Optional[Union[int, str]] = None,
    items: Optional[list[str]] = None,
    key: Optional[str] = None,
    parent: Optional[str] = None,
    priority: Optional[str] = None,
    updated_at: Optional[Union[datetime, str]] = None,
    updated_on: Optional[Union[date, str]] = None,
    uuid_: Optional[Uninon[str, uid.UUID]] = None,
) -> Stack:
    """
    Creates and returns an instance of the Stack model.

    This factory method initializes a Stack entity, which acts as a container for
    learning items (Flashcards, Questions) and can be organized into a hierarchical
    tree structure using parent and child references. It automatically processes
    and converts string-based lifecycle metadata and identifiers into their
    respective Python objects.

    Args:
        name (str): The display name of the stack.
        author (Optional[str]): Identifier of the user who owns or created the stack.
        children (Optional[list[str]]): A list of keys referring to sub-stacks.
        created_at (Optional[Union[datetime, str]]): ISO-formatted creation timestamp.
        created_on (Optional[Union[date, str]]): ISO-formatted creation date.
        customfields (Optional[list[dict[str, Any]]]): A list of custom metadata dictionaries.
        difficulty (Optional[str]): Reference key for the associated difficulty level.
        id_ (Optional[Union[int, str]]): Internal database identifier.
        items (Optional[list[str]]): A list of keys referring to the learning units
            (e.g., Flashcards) within this stack.
        key (Optional[str]): Unique model key identifier.
        parent (Optional[str]): Reference key to a parent stack, if applicable.
        priority (Optional[str]): Reference key for the associated priority level.
        updated_at (Optional[Union[datetime, str]]): ISO-formatted last update timestamp.
        updated_on (Optional[Union[date, str]]): ISO-formatted last update date.
        uuid_ (Optional[Uninon[str, uid.UUID]]): Universally unique identifier.

    Returns:
        Stack: A fully initialized instance of the Stack class.
    """

    parameters: dict[str, Any] = _convert_parameters(**locals().copy())

    return Stack(**parameters)


def get_subject_model(
    name: str,
    created_at: Optional[Union[datetime, str]] = None,
    created_on: Optional[Union[date, str]] = None,
    customfields: Optional[list[dict[str, Any]]] = None,
    difficulty: Optional[str] = None,
    id_: Optional[Union[int, str]] = None,
    key: Optional[str] = None,
    priority: Optional[str] = None,
    updated_at: Optional[Union[datetime, str]] = None,
    updated_on: Optional[Union[date, str]] = None,
    uuid_: Optional[Uninon[str, uid.UUID]] = None,
) -> Subject:
    """
    Creates and returns an instance of the Subject model.

    This factory method initializes a Subject entity, which represents a specific
    field of study or academic discipline. It allows for the categorization of
    learning materials and can be associated with default difficulty levels
    or priorities. String-based lifecycle metadata and identifiers are
    automatically converted into their corresponding Python types.

    Args:
        name (str): The name of the subject (e.g., 'Mathematics', 'History').
        created_at (Optional[Union[datetime, str]]): ISO-formatted creation timestamp.
        created_on (Optional[Union[date, str]]): ISO-formatted creation date.
        customfields (Optional[list[dict[str, Any]]]): A list of dictionaries
            containing user-defined metadata.
        difficulty (Optional[str]): Reference key for the default difficulty
            level assigned to this subject.
        id_ (Optional[Union[int, str]]): Internal database identifier.
        key (Optional[str]): Unique model key identifier.
        priority (Optional[str]): Reference key for the default priority level
            assigned to this subject.
        updated_at (Optional[Union[datetime, str]]): ISO-formatted last update timestamp.
        updated_on (Optional[Union[date, str]]): ISO-formatted last update date.
        uuid_ (Optional[Uninon[str, uid.UUID]]): Universally unique identifier.

    Returns:
        Subject: A fully initialized instance of the Subject class.
    """

    parameters: dict[str, Any] = _convert_parameters(**locals().copy())

    return Subject(**parameters)


def get_tag_model(
    value: str,
    created_at: Optional[Union[datetime, str]] = None,
    created_on: Optional[Union[date, str]] = None,
    id_: Optional[Union[int, str]] = None,
    key: Optional[str] = None,
    updated_at: Optional[Union[datetime, str]] = None,
    updated_on: Optional[Union[date, str]] = None,
    uuid_: Optional[Uninon[str, uid.UUID]] = None,
) -> Tag:
    """
    Creates and returns an instance of the Tag model.

    This factory method initializes a Tag entity, used for flexible categorization
    and filtering of various learning materials across the application. It
    ensures that the descriptive tag value is stored correctly and that all
    associated lifecycle metadata and identifiers are converted from strings
    into their appropriate Python types.

    Args:
        value (str): The actual label or text of the tag (e.g., 'Exam2024', 'Urgent').
        created_at (Optional[Union[datetime, str]]): ISO-formatted creation timestamp.
        created_on (Optional[Union[date, str]]): ISO-formatted creation date.
        id_ (Optional[Union[int, str]]): Internal database identifier.
        key (Optional[str]): Unique model key identifier.
        updated_at (Optional[Union[datetime, str]]): ISO-formatted last update timestamp.
        updated_on (Optional[Union[date, str]]): ISO-formatted last update date.
        uuid_ (Optional[Uninon[str, uid.UUID]]): Universally unique identifier.

    Returns:
        Tag: A fully initialized instance of the Tag class.
    """

    parameters: dict[str, Any] = _convert_parameters(**locals().copy())

    return Tag(**parameters)


def get_teacher_model(
    name: str,
    created_at: Optional[Union[datetime, str]] = None,
    created_on: Optional[Union[date, str]] = None,
    customfields: Optional[list[dict[str, Any]]] = None,
    difficulty: Optional[str] = None,
    id_: Optional[Union[int, str]] = None,
    key: Optional[str] = None,
    priority: Optional[str] = None,
    subjects: Optional[list[str]] = None,
    updated_at: Optional[Union[datetime, str]] = None,
    updated_on: Optional[Union[date, str]] = None,
    uuid_: Optional[Uninon[str, uid.UUID]] = None,
) -> Teacher:
    """
    Creates and returns an instance of the Teacher model.

    This factory method initializes a Teacher entity, which represents an instructor,
    content creator, or mentor within the learning system. It manages the
    teacher's profile, including their areas of expertise (subjects) and default
    educational preferences. String-based lifecycle metadata and identifiers are
    automatically converted into their corresponding Python types.

    Args:
        name (str): The full name or display name of the teacher.
        created_at (Optional[Union[datetime, str]]): ISO-formatted creation timestamp.
        created_on (Optional[Union[date, str]]): ISO-formatted creation date.
        customfields (Optional[list[dict[str, Any]]]): A list of dictionaries
            containing additional user-defined attributes.
        difficulty (Optional[str]): Reference key for the default difficulty
            level associated with this teacher's content.
        id_ (Optional[Union[int, str]]): Internal database identifier.
        key (Optional[str]): Unique model key identifier.
        priority (Optional[str]): Reference key for the default priority level
            assigned to this teacher's tasks or materials.
        subjects (Optional[list[str]]): A list of keys referring to the subjects
            this teacher is associated with.
        updated_at (Optional[Union[datetime, str]]): ISO-formatted last update timestamp.
        updated_on (Optional[Union[date, str]]): ISO-formatted last update date.
        uuid_ (Optional[Uninon[str, uid.UUID]]): Universally unique identifier.

    Returns:
        Teacher: A fully initialized instance of the Teacher class.
    """

    parameters: dict[str, Any] = _convert_parameters(**locals().copy())

    return Teacher(**parameters)


def get_user_model(
    name: str,
    created_at: Optional[Union[datetime, str]] = None,
    created_on: Optional[Union[date, str]] = None,
    id_: Optional[Union[int, str]] = None,
    key: Optional[str] = None,
    updated_at: Optional[Union[datetime, str]] = None,
    updated_on: Optional[Union[date, str]] = None,
    uuid_: Optional[Uninon[str, uid.UUID]] = None,
) -> User:
    """
    Creates and returns an instance of the User model.

    This factory method initializes a User entity, representing an individual
    account holder within the system. It serves as the primary reference for
    content ownership, tracking who created or modified specific learning materials.
    Standard lifecycle metadata and identifiers are automatically processed and
    converted from strings into their appropriate Python types.

    Args:
        name (str): The unique display name or username of the user.
        created_at (Optional[Union[datetime, str]]): ISO-formatted creation timestamp.
        created_on (Optional[Union[date, str]]): ISO-formatted creation date.
        id_ (Optional[Union[int, str]]): Internal database identifier.
        key (Optional[str]): Unique model key identifier used for references.
        updated_at (Optional[Union[datetime, str]]): ISO-formatted last update timestamp.
        updated_on (Optional[Union[date, str]]): ISO-formatted last update date.
        uuid_ (Optional[Uninon[str, uid.UUID]]): Universally unique identifier.

    Returns:
        User: A fully initialized instance of the User class.
    """

    parameters: dict[str, Any] = _convert_parameters(**locals().copy())

    return User(**parameters)
