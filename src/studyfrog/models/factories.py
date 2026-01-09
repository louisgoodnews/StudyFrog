"""
Author: Louis Goodnews
Date: 2025-12-11
"""

from typing import Any, Final, Optional, TypeAlias

from utils.common import get_now_str, get_today_str, generate_uuid4_str


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "get_answer_model_dict",
    "get_association_model_dict",
    "get_customfield_model_dict",
    "get_difficulty_model_dict",
    "get_flashcard_model_dict",
    "get_image_model_dict",
    "get_note_model_dict",
    "get_option_model_dict",
    "get_priority_model_dict",
    "get_question_model_dict",
    "get_rehearsal_run_model_dict",
    "get_rehearsal_run_item_model_dict",
    "get_stack_model_dict",
    "get_subject_model_dict",
    "get_tag_model_dict",
    "get_teacher_model_dict",
    "get_user_model_dict",
]


# ---------- Type Aliases ---------- #

ModelDict: TypeAlias = dict[str, Any]


# ---------- Helper Functions ---------- #


def _generate_model_dict(
    model_type: str,
    **kwargs: dict[str, Any],
) -> ModelDict:
    """
    Returns a model dictionary, a dictionary representing a model.

    Args:
        model_type (str): The type of the model.
        **kwargs (dict[str, Any]): Additional keyword arguments to add to the dictionary model.

    Returns:
        ModelDict: The model dictionary, a dictionary representing a model.
    """

    kwargs.pop(
        "id",
        None,
    )
    kwargs.pop(
        "key",
        None,
    )

    model: ModelDict = {
        "metadata": {
            "created_at": get_now_str(),
            "created_od": get_today_str(),
            "fields": {
                "fields": [],
                "total": 0,
            },
            "type": model_type.upper(),
            "updated_at": get_now_str(),
            "updated_on": get_today_str(),
            "uuid": generate_uuid4_str(),
        },
        **kwargs,
    }

    model["metadata"]["fields"]["fields"] = list(model.keys())
    model["metadata"]["fields"]["total"] = len(model["metadata"]["fields"]["fields"])

    return model


# ---------- Functions ---------- #


def get_answer_model_dict(
    text: str,
    is_assigned_to_question: bool = False,
    is_correct: bool = False,
    subject: Optional[str] = None,
    tags: Optional[list[str]] = None,
    teacher: Optional[str] = None,
) -> ModelDict:
    """
    Constructs a standardized dictionary representation (ModelDict) for an answer associated with a question.

    This function serves as a factory to create answer models, which are typically part
    of a larger flashcard or quiz item. It includes the content of the answer and a flag
    indicating its correctness, essential for multiple-choice or true/false questions.

    Args:
        is_assigned_to_question (bool, optional): Flag indicating whether this answer option is assigned to a
                                                question. Defaults to False.
        is_correct (bool, optional): Flag indicating whether this answer option is the
                                     correct response to the associated question. Defaults to False.
        subject (Optional[str], optional): The subject of the answer. Defaults to None.
        tags (Optional[list[str]], optional): A list of tags associated with the answer. Defaults to None.
        text (str): The textual content of the answer option.
        teacher (Optional[str], optional): The teacher of the answer. Defaults to None.

    Returns:
        ModelDict: A dictionary object conforming to the application's ModelDict
                   structure for an answer model, suitable for database serialization.
    """

    kwargs: dict[str, Any] = dict(locals())

    kwargs["model_type"] = "answer"

    return _generate_model_dict(**kwargs)


def get_association_model_dict(
    answer: Optional[str] = None,
    customfield: Optional[str] = None,
    difficulty: Optional[str] = None,
    flashcard: Optional[str] = None,
    image: Optional[str] = None,
    note: Optional[str] = None,
    option: Optional[str] = None,
    priority: Optional[str] = None,
    question: Optional[str] = None,
    rehearsal_run: Optional[str] = None,
    rehearsal_run_item: Optional[str] = None,
    stack: Optional[str] = None,
    subject: Optional[str] = None,
    tag: Optional[str] = None,
    teacher: Optional[str] = None,
) -> ModelDict:
    """
    Constructs a standardized dictionary representation (ModelDict) for an association.

    This function serves as a factory to create association models, which are used to
    establish relationships between different data models in the application.

    Args:
        answer (str): The key of the answer to create an association with.
        customfield (str): The key of the customfield to create an association with.
        difficulty (str): The key of the difficulty to create an association with.
        flashcard (str): The key of the flashcard to create an association with.
        image (str): The key of the image to create an association with.
        note (str): The note of the flashcard to create an association with.
        option (str): The key of the option to create an association with.
        priority (str): The key of the priority to create an association with.
        question (str): The key of the question to create an association with.
        rehearsal_run (str): The key of the rehearsal run to create an association with.
        rehearsal_run_item (str): The key of the rehearsal run item to create an association with.
        stack (str): The key of the stack to create an association with.
        subject (str): The key of the subject to create an association with.
        tag (str): The key of the tag to create an association with.
        teacher (str): The key of the teacher to create an association with.

    Returns:
        ModelDict: A dictionary object conforming to the application's ModelDict
                   structure for an association model, suitable for database serialization.
    """

    kwargs: dict[str, Any] = dict(locals())

    kwargs["model_type"] = "association"

    return _generate_model_dict(**kwargs)


def get_customfield_model_dict(
    name: str,
    author: Optional[str] = None,
    options: Optional[list] = None,
) -> ModelDict:
    """
    Constructs a standardized dictionary representation (ModelDict) for a custom field definition.

    This function serves as a factory for defining user-created metadata fields
    that can be attached to various data models (like flashcards or notes). This
    allows the application to be flexible beyond its core schema.

    Args:
        name (str): The unique name or label of the custom field (e.g., "Source URL").
        author (Optional[str], optional): The identifier of the user or entity who defined this custom field. Defaults to None.
        options (Optional[list], optional): A list of possible values or constraints for this custom field, typically containing
                                            ModelDicts generated by get_option_model_dict(). Defaults to [].

    Returns:
        ModelDict: A dictionary object conforming to the application's ModelDict
                   structure for a custom field definition, suitable for database serialization.
    """

    if not options:
        options = []

    kwargs: dict[str, Any] = dict(locals())

    kwargs["model_type"] = "customfield"

    return _generate_model_dict(**kwargs)


def get_difficulty_model_dict(
    display_name: str,
    name: str,
    value: float,
) -> ModelDict:
    """
    Constructs a standardized dictionary representation (ModelDict) for a difficulty setting.

    This function serves as a factory to create models for classifying item difficulty
    (e.g., Easy, Medium, Hard). The 'value' typically represents a numerical factor
    used in spaced repetition algorithms (like SM-2) to adjust the time interval
    between reviews.

    Args:
        display_name (str): The human-readable name of the difficulty level (e.g., "Hard").
        name (str): The internal name of the difficulty level (e.g., "hard").
        value (float): The numerical factor associated with this difficulty, used
                       for scheduling reviews.

    Returns:
        ModelDict: A dictionary object conforming to the application's ModelDict
                   structure for a difficulty model, suitable for database serialization.
    """

    kwargs: dict[str, Any] = dict(locals())

    kwargs["model_type"] = "difficulty"

    return _generate_model_dict(**kwargs)


def get_flashcard_model_dict(
    back: str,
    front: str,
    author: Optional[str] = None,
    customfields: Optional[list[dict[str, Any]]] = None,
    difficulty: Optional[str] = None,
    is_assigned_to_stack: bool = False,
    last_viewed_at: Optional[str] = None,
    next_view_at: Optional[str] = None,
    priority: Optional[str] = None,
    subject: Optional[str] = None,
    tags: Optional[list[str]] = None,
    teacher: Optional[str] = None,
) -> ModelDict:
    """
    Constructs a standardized dictionary representation (ModelDict) for a flashcard object.

    This method serves as a factory function to ensure all flashcard models adhere
    to a consistent structure before being stored or processed by the application.
    It automatically sets the 'model_type' to "flashcard" and handles default
    initialization for optional fields like 'customfields'.

    Args:
        back (str): The content displayed on the back side of the flashcard (the answer).
        front (str): The content displayed on the front side of the flashcard (the question).
        author (Optional[str], optional): The identifier of the user or entity that created the flashcard. Defaults to None.
        customfields (Optional[list[dict[str, Any]]], optional): A list of dictionaries for arbitrary, non-standardized data fields. Defaults to [].
        difficulty (Optional[str], optional): The perceived difficulty level of the flashcard. Defaults to None.
        is_assigned_to_stack (bool, optional): Flag indicating whether this flashcard is assigned to a stack. Defaults to False.
        last_viewed_at (Optional[str], optional): Timestamp indicating the last time the flashcard was viewed (ISO format expected). Defaults to None.
        next_view_at (Optional[str], optional): Timestamp indicating the next scheduled review time (ISO format expected). Defaults to None.
        priority (Optional[str], optional): The assigned priority level of the flashcard. Defaults to None.
        subject (Optional[str], optional): The subject of the flashcard. Defaults to None.
        tags (Optional[list[str]], optional): A list of tags associated with the flashcard. Defaults to None.
        teacher (Optional[str], optional): The teacher of the flashcard. Defaults to None.

    Returns:
        ModelDict: A dictionary object conforming to the application's ModelDict
                   structure for a flashcard, suitable for database serialization.
    """

    if not customfields:
        customfields = []

    kwargs: dict[str, Any] = dict(locals())

    kwargs["model_type"] = "flashcard"

    return _generate_model_dict(**kwargs)


def get_image_model_dict() -> ModelDict:
    """
    Constructs a standardized dictionary representation (ModelDict) for an image object.

    This method serves as a factory function to ensure all image models adhere
    to a consistent structure before being stored or processed by the application.
    It automatically sets the 'model_type' to "image".

    Args:
        None

    Returns:
        ModelDict: A dictionary object conforming to the application's ModelDict
                   structure for an image, suitable for database serialization.
    """

    kwargs: dict[str, Any] = dict(locals())

    kwargs["model_type"] = "image"

    return _generate_model_dict(**kwargs)


def get_note_model_dict(
    text: str,
    title: str,
    author: Optional[str] = None,
    customfields: Optional[list[dict[str, Any]]] = None,
    difficulty: Optional[str] = None,
    is_assigned_to_stack: bool = False,
    last_viewed_at: Optional[str] = None,
    next_view_at: Optional[str] = None,
    priority: Optional[str] = None,
    subject: Optional[str] = None,
    tags: Optional[list[str]] = None,
    teacher: Optional[str] = None,
) -> ModelDict:
    """
    Constructs a standardized dictionary representation (ModelDict) for a general study note.

    This method serves as a factory function to create note models, ensuring they adhere
    to a consistent structure with content, metadata, and scheduling fields. It is designed
    to manage general textual information within the application.

    Args:
        text (str): The main body content of the note.
        title (str): The title or heading of the note.
        author (Optional[str], optional): The identifier of the user or entity that created the note. Defaults to None.
        customfields (Optional[list[dict[str, Any]]], optional): A list of dictionaries for arbitrary, non-standardized data fields. Defaults to None.
        difficulty (Optional[str], optional): The perceived difficulty level associated with the note's topic. Defaults to None.
        is_assigned_to_stack (bool, optional): Flag indicating whether this note is assigned to a stack. Defaults to False.
        last_viewed_at (Optional[str], optional): Timestamp indicating the last time the note was viewed (ISO format expected). Defaults to None.
        next_view_at (Optional[str], optional): Timestamp indicating the next scheduled review time (ISO format expected). Defaults to None.
        priority (Optional[str], optional): The assigned priority level of the note. Defaults to None.
        subject (Optional[str], optional): The subject of the note. Defaults to None.
        tags (Optional[list[str]], optional): A list of tags associated with the note. Defaults to None.
        teacher (Optional[str], optional): The teacher of the note. Defaults to None.

    Returns:
        ModelDict: A dictionary object conforming to the application's ModelDict
                   structure for a note, suitable for database serialization.
    """

    if not customfields:
        customfields = []

    kwargs: dict[str, Any] = dict(locals())

    kwargs["model_type"] = "note"

    return _generate_model_dict(**kwargs)


def get_option_model_dict(
    customfield: str,
    value: Any,
    author: Optional[str] = None,
) -> ModelDict:
    """
    Constructs a standardized dictionary representation (ModelDict) for a generic option or setting.

    This function serves as a flexible factory, primarily used to create model dictionaries
    for configuration settings, custom key-value pairs, or non-standardized attributes
    that need to be stored within the application's data structure.

    Args:
        customfield (str): The name or key of the option or setting being defined.
        value (Any): The corresponding value associated with the customfield. This can be of any serializable type (str, int, float, list, dict, etc.).
        author (Optional[str], optional): The identifier of the user or entity that defined this option. Defaults to None.

    Returns:
        ModelDict: A dictionary object conforming to the application's ModelDict
                   structure for a generic option, suitable for database serialization.
    """

    kwargs: dict[str, Any] = dict(locals())

    kwargs["model_type"] = "option"

    return _generate_model_dict(**kwargs)


def get_priority_model_dict(
    display_name: str,
    name: str,
    value: float,
) -> ModelDict:
    """
    Constructs a standardized dictionary representation (ModelDict) for a priority setting.

    This function serves as a factory to create models used for classifying the
    importance or urgency of an item (e.g., Low, Medium, High). The 'value'
    typically represents a numerical weight used to influence selection or sorting
    algorithms within the application.

    Args:
        display_name (str): The human-readable name of the priority level (e.g., "High").
        name (str): The internal name of the priority level (e.g., "high").
        value (float): The numerical weight or factor associated with this priority.

    Returns:
        ModelDict: A dictionary object conforming to the application's ModelDict
                   structure for a priority model, suitable for database serialization.
    """

    kwargs: dict[str, Any] = dict(locals())

    kwargs["model_type"] = "priority"

    return _generate_model_dict(**kwargs)


def get_question_model_dict(
    text: str,
    author: Optional[str] = None,
    customfields: Optional[list[dict[str, Any]]] = None,
    difficulty: Optional[str] = None,
    is_assigned_to_stack: bool = False,
    last_viewed_at: Optional[str] = None,
    next_view_at: Optional[str] = None,
    priority: Optional[str] = None,
    subject: Optional[str] = None,
    tags: Optional[list[str]] = None,
    teacher: Optional[str] = None,
) -> ModelDict:
    """
    Constructs a standardized dictionary representation (ModelDict) for a question object.

    This function serves as a factory to create question models, which often form
    the front side of a flashcard or a component in a quiz item. It ensures the
    question model includes the main textual content along with relevant metadata
    and scheduling information.

    Args:
        text (str): The main textual content of the question.
        author (Optional[str], optional): The identifier of the user or entity that created the question. Defaults to None.
        customfields (Optional[list[dict[str, Any]]], optional): A list of dictionaries for arbitrary, non-standardized data fields. Defaults to None.
        difficulty (Optional[str], optional): The perceived difficulty level associated with the question. Defaults to None.
        is_assigned_to_stack (bool, optional): Flag indicating whether this question is assigned to a stack. Defaults to False.
        last_viewed_at (Optional[str], optional): Timestamp indicating the last time the question was viewed (ISO format expected). Defaults to None.
        next_view_at (Optional[str], optional): Timestamp indicating the next scheduled review time (ISO format expected). Defaults to None.
        priority (Optional[str], optional): The assigned priority level of the question. Defaults to None.
        subject (Optional[str], optional): The subject of the question. Defaults to None.
        tags (Optional[list[str]], optional): A list of tags associated with the question. Defaults to None.
        teacher (Optional[str], optional): The teacher of the question. Defaults to None.

    Returns:
        ModelDict: A dictionary object conforming to the application's ModelDict
                   structure for a question model, suitable for database serialization.
    """

    if not customfields:
        customfields = []

    kwargs: dict[str, Any] = dict(locals())

    kwargs["model_type"] = "question"

    return _generate_model_dict(**kwargs)


def get_rehearsal_run_model_dict(
    stacks: list[str],
    author: Optional[str] = None,
    configuration: Optional[dict[str, Any]] = None,
    duration: Optional[float] = None,
    end: Optional[str] = None,
    items: Optional[list[str]] = None,
    start: Optional[str] = None,
) -> ModelDict:
    """
    Constructs a standardized dictionary representation (ModelDict) for a rehearsal run.

    This function serves as a factory for tracking a specific study session where
    the user reviews a set of material. It records which stacks were involved,
    the settings used, and the temporal metrics of the session.

    Args:
        stacks (list[str]): A list of IDs (UUIDs) of the study stacks included in this rehearsal run.
        author (Optional[str], optional): The identifier of the user who performed the rehearsal run. Defaults to None.
        configuration (Optional[dict[str, Any]], optional): Settings used for this run (e.g., number of items, scheduling algorithm version). Defaults to None.
        duration (Optional[float], optional): The total length of the session in seconds. Defaults to None.
        end (Optional[str], optional): Timestamp indicating when the rehearsal run was finished (ISO format expected). Defaults to None.
        start (Optional[str], optional): Timestamp indicating when the rehearsal run was started (ISO format expected). Defaults to None.

    Returns:
        ModelDict: A dictionary object conforming to the application's ModelDict
                   structure for a rehearsal run, suitable for database serialization.
    """

    if not configuration:
        configuration = {}

    if not items:
        items = []

    kwargs: dict[str, Any] = dict(locals())

    kwargs["model_type"] = "rehearsal_run"

    return _generate_model_dict(**kwargs)


def get_rehearsal_run_item_model_dict(
    item: str,
    actions: Optional[list[dict[str, Any]]] = None,
    duration: Optional[float] = None,
    end: Optional[str] = None,
    start: Optional[str] = None,
) -> ModelDict:
    """
    Constructs a standardized dictionary representation (ModelDict) for a rehearsal run item.

    This function serves as a factory for tracking a specific study session where
    the user reviews a set of material. It records which stacks were involved,
    the settings used, and the temporal metrics of the session.

    Args:
        actions (Optional[list[dict[str, Any]]], optional): List of actions taken during the study item session. Defaults to None.
        duration (Optional[float], optional): Duration of time spent on the study item in seconds. Defaults to None.
        end (Optional[str], optional): Timestamp indicating when the study item was finished (ISO format expected). Defaults to None.
        item (str): The ID (key) of the study item (flashcard, note, question) included in this rehearsal run.
        start (Optional[str], optional): Timestamp indicating when the study item was started (ISO format expected). Defaults to None.

    Returns:
        ModelDict: A dictionary object conforming to the application's ModelDict
                   structure for a rehearsal run item, suitable for database serialization.
    """

    if not actions:
        actions = []

    kwargs: dict[str, Any] = dict(locals())

    kwargs["model_type"] = "rehearsal_run_item"

    return _generate_model_dict(**kwargs)


def get_stack_model_dict(
    name: str,
    author: Optional[str] = None,
    children: Optional[list[str]] = None,
    customfields: Optional[list[dict[str, Any]]] = None,
    description: Optional[str] = None,
    difficulty: Optional[str] = None,
    items: Optional[list[str]] = None,
    last_viewed_at: Optional[str] = None,
    next_view_at: Optional[str] = None,
    parent: Optional[str] = None,
    priority: Optional[str] = None,
    subject: Optional[str] = None,
    tags: Optional[list[str]] = None,
    teacher: Optional[str] = None,
) -> ModelDict:
    """
    Constructs a standardized dictionary representation (ModelDict) for a study stack or collection.

    This function serves as a factory to create stack models, which act as containers
    or groupings for individual study items (flashcards, notes, questions). It organizes
    the stack with its name and links to related entities and scheduling metadata.

    Args:
        author (Optional[str], optional): The identifier of the user or entity that created the stack. Defaults to None.
        children (Optional[list[str, Any]], optional): A list of IDs (UUIDs) referencing child stacks contained in this stack. Defaults to [].
        customfields (Optional[list[dict[str, Any]]], optional): A list of dictionaries for arbitrary, non-standardized data fields. Defaults to [].
        description (Optional[str], optional): A description of the stack. Defaults to None.
        difficulty (Optional[str], optional): The perceived difficulty level of the stack's content as a whole. Defaults to None.
        items (Optional[list[str]], optional): A list of IDs (UUIDs) referencing the individual study items (flashcards, notes) contained in this stack. Defaults to [].
        last_viewed_at (Optional[str], optional): Timestamp indicating the last time the stack was reviewed (ISO format expected). Defaults to None.
        name (str): The unique, human-readable name of the stack (e.g., "Biology Chapter 3").
        next_view_at (Optional[str], optional): Timestamp indicating the next scheduled review time for the stack. Defaults to None.
        parent (Optional[str], optional): The ID (UUID) of the parent stack this stack belongs to. Defaults to None.
        priority (Optional[str], optional): The assigned priority level of the stack. Defaults to None.
        subject (Optional[str], optional): The ID (UUID) of the subject this stack belongs to. Defaults to None.
        tags (Optional[list[str]], optional): A list of IDs (UUIDs) of tags applied to this stack. Defaults to [].
        teacher (Optional[str], optional): The ID (UUID) of the teacher/instructor associated with the stack's content. Defaults to None.

    Returns:
        ModelDict: A dictionary object conforming to the application's ModelDict
                   structure for a stack model, suitable for database serialization.
    """

    if not children:
        children = []

    if not customfields:
        customfields = []

    if not items:
        items = []

    if not tags:
        tags = []

    kwargs: dict[str, Any] = dict(locals())

    kwargs["model_type"] = "stack"

    return _generate_model_dict(**kwargs)


def get_subject_model_dict(
    name: str,
    author: Optional[str] = None,
    customfields: Optional[list[dict[str, Any]]] = None,
    difficulty: Optional[str] = None,
    priority: Optional[str] = None,
    tags: Optional[list[str]] = None,
    teacher: Optional[str] = None,
) -> ModelDict:
    """
    Constructs a standardized dictionary representation (ModelDict) for a study subject.

    This function serves as a factory to create subject models, which act as the highest
    level of categorization for study materials (e.g., "Mathematics," "History," "Physics").
    It ensures the subject model includes the name and links to relevant metadata.

    Args:
        name (str): The unique, human-readable name of the subject.
        author (Optional[str], optional): The identifier of the user or entity that created the subject entry. Defaults to None.
        customfields (Optional[list[dict[str, Any]]], optional): A list of dictionaries for arbitrary, non-standardized data fields. Defaults to [].
        difficulty (Optional[str], optional): The perceived inherent difficulty level of the subject. Defaults to None.
        priority (Optional[str], optional): The assigned priority level for studying this subject. Defaults to None.
        tags (Optional[list[str]], optional): A list of IDs (UUIDs) of tags applied to this subject. Defaults to None.
        teacher (Optional[str], optional): The ID (UUID) of the teacher/instructor primarily associated with the subject. Defaults to None.

    Returns:
        ModelDict: A dictionary object conforming to the application's ModelDict
                   structure for a subject model, suitable for database serialization.
    """

    if not customfields:
        customfields = []

    kwargs: dict[str, Any] = dict(locals())

    kwargs["model_type"] = "subject"

    return _generate_model_dict(**kwargs)


def get_tag_model_dict(
    name: str,
    author: Optional[str] = None,
) -> ModelDict:
    """
    Constructs a standardized dictionary representation (ModelDict) for a categorical tag.

    This function serves as a factory to create tag models, which are used for
    flexible, arbitrary classification and grouping of study items across subjects
    and stacks (e.g., "High-Yield," "Exam Prep," "Needs Review").

    Args:
        name (str): The unique name or label of the tag (e.g., "Calculus").
        author (Optional[str], optional): The identifier of the user or entity that created the tag. Defaults to None.

    Returns:
        ModelDict: A dictionary object conforming to the application's ModelDict
                   structure for a tag model, suitable for database serialization.
    """

    kwargs: dict[str, Any] = dict(locals())

    kwargs["model_type"] = "tag"

    return _generate_model_dict(**kwargs)


def get_teacher_model_dict(
    name: str,
    author: Optional[str] = None,
    customfields: Optional[list[dict[str, Any]]] = None,
    difficulty: Optional[str] = None,
    priority: Optional[str] = None,
    tags: Optional[list[str]] = None,
    teacher: Optional[str] = None,
) -> ModelDict:
    """
    Constructs a standardized dictionary representation (ModelDict) for an instructor or teacher entity.

    This function serves as a factory to create teacher models, allowing study items
    to be categorized or filtered based on the associated lecturer or course creator.

    Args:
        name (str): The full name or identifier of the teacher/instructor.
        author (Optional[str], optional): The identifier of the user or entity that created this teacher record. Defaults to None.
        customfields (Optional[list[dict[str, Any]]], optional): A list of dictionaries for arbitrary, non-standardized data fields. Defaults to [].
        difficulty (Optional[str], optional): A general difficulty rating associated with the teacher's course material. Defaults to None.
        priority (Optional[str], optional): The priority level associated with the teacher's content. Defaults to None.
        tags (Optional[list[str]], optional): A list of IDs (UUIDs) of tags relevant to the teacher's subjects. Defaults to None.
        teacher (Optional[str], optional): Included for consistency, but typically unused for the teacher model itself. Defaults to None.

    Returns:
        ModelDict: A dictionary object conforming to the application's ModelDict
                   structure for a teacher model, suitable for database serialization.
    """

    if not customfields:
        customfields = []

    kwargs: dict[str, Any] = dict(locals())

    kwargs["model_type"] = "teacher"

    return _generate_model_dict(**kwargs)


def get_user_model_dict(
    name: str,
    author: Optional[str] = None,
) -> ModelDict:
    """
    Constructs a standardized dictionary representation (ModelDict) for a user or profile entity.

    This function serves as a factory to create models for tracking user-specific
    information, profiles, or basic configuration settings within the application.
    It ensures the user model adheres to the base structural requirements.

    Args:
        name (str): The display name or unique identifier of the user (e.g., username).
        author (Optional[str], optional): The identifier of the user who created this
                                          user record (often redundant, but included
                                          for model consistency). Defaults to None.

    Returns:
        ModelDict: A dictionary object conforming to the application's ModelDict
                   structure for a user model, suitable for database serialization.
    """

    kwargs: dict[str, Any] = dict(locals())

    kwargs["model_type"] = "user"

    return _generate_model_dict(**kwargs)
