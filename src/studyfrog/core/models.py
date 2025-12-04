"""
Author: Louis Goodnews
Date: 2025-11-17
Description: This module contains functions for creating various objects.
"""

from typing import Any, Final, Literal, Optional, Union

from utils.utils import get_now_str, get_today_str, get_uuid_str


# ---------- Constants ---------- #


# ---------- Functions ---------- #


def _get_object_dict(**kwargs) -> dict[str, Any]:
    """
    Returns a dictionary containing an object's attributes.

    This function ensures that all required fields are present in the returned dictionary,
    including timestamps, metadata, and a default UUID.

    Args:
        **kwargs (dict[str, Any]): Additional keywords to pass to the object's attributes.

    Returns:
        dict[str, Any]: A dictionary containing an object's attributes.
    """

    defaults_for_arguments: dict[str, Any] = {
        "created_at": get_now_str(),
        "created_on": get_today_str(),
        "id": None,
        "key": None,
        "metadata": {},
        "updated_at": get_now_str(),
        "updated_on": get_today_str(),
        "uuid": get_uuid_str(),
    }

    for (
        key,
        value,
    ) in defaults_for_arguments.items():
        if key in kwargs:
            continue

        kwargs[key] = value

    fields_list: list[str] = sorted(list(kwargs.keys()))

    kwargs["fields"] = {
        "fields": fields_list,
        "total": len(fields_list),
    }

    return dict(sorted(kwargs.items()))


def get_answer_model(
    text: str,
    customfields: Optional[dict[str, Any]] = None,
    **kwargs,
) -> dict[str, Any]:
    """
    Returns a dictionary containing an answer's attributes.

    Args:
        customfields (Optional[dict[str, Any]]): The answer's custom fields.
        text (str): The answer's text.
        **kwargs (dict[str, Any]): Additional keywords to pass to the answer's attributes.

    Returns:
        dict[str, Any]: A dictionary containing an answer's attributes.
    """

    if not customfields:
        customfields = {}

    kwargs["customfields"] = {
        "customfields": customfields,
        "total": len(customfields),
    }
    kwargs["text"] = text
    kwargs["type"] = "ANSWER"

    return _get_object_dict(**kwargs)


def get_association_model(
    answer: Union[int, list[Union[int, str]], str],
    customfield: Union[int, list[Union[int, str]], str],
    difficulty: Union[int, list[Union[int, str]], str],
    flashcard: Union[int, list[Union[int, str]], str],
    image: Union[int, list[Union[int, str]], str],
    note: Union[int, list[Union[int, str]], str],
    option: Union[int, list[Union[int, str]], str],
    priority: Union[int, list[Union[int, str]], str],
    question: Union[int, list[Union[int, str]], str],
    rehearsal_run: Union[int, list[Union[int, str]], str],
    rehearsal_run_item: Union[int, list[Union[int, str]], str],
    stack: Union[int, list[Union[int, str]], str],
    subject: Union[int, list[Union[int, str]], str],
    teacher: Union[int, list[Union[int, str]], str],
    **kwargs,
) -> dict[str, Any]:
    """
    Returns a dictionary containing an association's attributes.

    Args:
        answer (Union[int, list[Union[int, str]], str]): The association's answer.
        customfield (Union[int, list[Union[int, str]], str]): The association's custom field.
        difficulty (Union[int, list[Union[int, str]], str]): The association's difficulty.
        flashcard (Union[int, list[Union[int, str]], str]): The association's flashcard.
        image (Union[int, list[Union[int, str]], str]): The association's image.
        note (Union[int, list[Union[int, str]], str]): The association's note.
        option (Union[int, list[Union[int, str]], str]): The association's option.
        priority (Union[int, list[Union[int, str]], str]): The association's priority.
        question (Union[int, list[Union[int, str]], str]): The association's question.
        rehearsal_run (Union[int, list[Union[int, str]], str]): The association's rehearsal run.
        rehearsal_run_item (Union[int, list[Union[int, str]], str]): The association's rehearsal run item.
        stack (Union[int, list[Union[int, str]], str]): The association's stack.
        subject (Union[int, list[Union[int, str]], str]): The association's subject.
        teacher (Union[int, list[Union[int, str]], str]): The association's teacher.
        **kwargs (dict[str, Any]): Additional keywords to pass to the association's attributes.

    Returns:
        dict[str, Any]: A dictionary containing an association's attributes.
    """

    kwargs["answer"] = answer
    kwargs["customfield"] = customfield
    kwargs["difficulty"] = difficulty
    kwargs["flashcard"] = flashcard
    kwargs["image"] = image
    kwargs["note"] = note
    kwargs["option"] = option
    kwargs["priority"] = priority
    kwargs["question"] = question
    kwargs["rehearsal_run"] = rehearsal_run
    kwargs["rehearsal_run_item"] = rehearsal_run_item
    kwargs["stack"] = stack
    kwargs["subject"] = subject
    kwargs["teacher"] = teacher
    kwargs["type"] = "ASSOCIATION"

    return _get_object_dict(**kwargs)


def get_customfield_model(
    name: str,
    customfields: Optional[dict[str, Any]] = None,
    **kwargs,
) -> dict[str, Any]:
    """
    Returns a dictionary containing a custom field's attributes.

    Args:
        customfields (Optional[dict[str, Any]]): The custom field's custom fields.
        name (str): The custom field's name.
        **kwargs (dict[str, Any]): Additional keywords to pass to the custom field's attributes.

    Returns:
        dict[str, Any]: A dictionary containing a custom field's attributes.
    """

    if not customfields:
        customfields = {}

    kwargs["customfields"] = {
        "customfields": customfields,
        "total": len(customfields),
    }
    kwargs["name"] = name
    kwargs["type"] = "CUSTOMFIELD"

    return _get_object_dict(**kwargs)


def get_difficulty_model(
    name: str,
    value: int,
    customfields: Optional[dict[str, Any]] = None,
    **kwargs,
) -> dict[str, Any]:
    """
    Returns a dictionary containing a difficulty's attributes.

    Args:
        customfields (Optional[dict[str, Any]]): The difficulty's custom fields.
        name (str): The difficulty's name.
        value (int): The difficulty's value.
        **kwargs (dict[str, Any]): Additional keywords to pass to the difficulty's attributes.

    Returns:
        dict[str, Any]: A dictionary containing a difficulty's attributes.
    """

    if not customfields:
        customfields = {}

    kwargs["customfields"] = {"customfields": customfields, "total": len(customfields)}
    kwargs["name"] = name
    kwargs["type"] = "DIFFICULTY"
    kwargs["value"] = value

    return _get_object_dict(**kwargs)


def get_flashcard_model(
    back_text: str,
    front_text: str,
    customfields: Optional[dict[str, Any]] = None,
    difficulty: Optional[str] = None,
    last_viewed_at: Optional[str] = None,
    priority: Optional[str] = None,
    **kwargs,
) -> dict[str, Any]:
    """
    Returns a dictionary containing a flashcard's attributes.

    Args:
        back_text (str): The flashcard's back text.
        customfields (Optional[dict[str, Any]]): The flashcard's custom fields.
        difficulty (Optional[str]): The flashcard's difficulty.
        front_text (str): The flashcard's front text.
        last_viewed_at (Optional[str]): The datetime when the flashcard was last viewed.
        priority (Optional[str]): The flashcard's priority.
        **kwargs (dict[str, Any]): Additional keywords to pass to the flashcard's attributes.

    Returns:
        dict[str, Any]: A dictionary containing a flashcard's attributes.
    """

    if not customfields:
        customfields = {}

    kwargs["customfields"] = {
        "customfields": customfields,
        "total": len(customfields),
    }
    kwargs["back_text"] = back_text
    kwargs["front_text"] = front_text

    if not difficulty:
        difficulty = ""

    kwargs["difficulty"] = difficulty
    kwargs["last_viewed_at"] = last_viewed_at

    if not priority:
        priority = ""

    kwargs["priority"] = priority
    kwargs["type"] = "FLASHCARD"

    return _get_object_dict(**kwargs)


def get_image_model(
    customfields: Optional[dict[str, Any]] = None,
    **kwargs,
) -> dict[str, Any]:
    """
    Returns a dictionary containing an image's attributes.

    Args:
        customfields (Optional[dict[str, Any]]): The image's custom fields.
        **kwargs (dict[str, Any]): Additional keywords to pass to the image's attributes.

    Returns:
        dict[str, Any]: A dictionary containing an image's attributes.
    """

    if not customfields:
        customfields = {}

    kwargs["customfields"] = {
        "customfields": customfields,
        "total": len(customfields),
    }
    kwargs["type"] = "IMAGE"

    return _get_object_dict(**kwargs)


def get_note_model(
    text: str,
    title: str,
    customfields: Optional[dict[str, Any]] = None,
    **kwargs,
) -> dict[str, Any]:
    """
    Returns a dictionary containing a note's attributes.

    Args:
        customfields (Optional[dict[str, Any]]): The note's custom fields.
        text (str): The note's text.
        title (str): The note's title.
        **kwargs (dict[str, Any]): Additional keywords to pass to the note's attributes.

    Returns:
        dict[str, Any]: A dictionary containing a note's attributes.
    """

    if not customfields:
        customfields = {}

    kwargs["customfields"] = {
        "customfields": customfields,
        "total": len(customfields),
    }
    kwargs["text"] = text
    kwargs["title"] = title
    kwargs["type"] = "NOTE"

    return _get_object_dict(**kwargs)


def get_option_model(
    name: str,
    value: Union[
        bool,
        float,
        int,
        str,
    ],
    customfields: Optional[list[str]] = None,
    **kwargs,
) -> dict[str, Any]:
    """
    Returns a dictionary containing an option's attributes.

    Args:
        customfields (Optional[list[str]]): The option's custom fields.
        name (str): The option's name.
        value (Union[bool, float, int, str]): The option's value.
        **kwargs (dict[str, Any]): Additional keywords to pass to the option's attributes.

    Returns:
        dict[str, Any]: A dictionary containing an option's attributes.
    """

    if not customfields:
        customfields = []

    kwargs["customfields"] = {
        "customfields": customfields,
        "total": len(customfields),
    }
    kwargs["name"] = name
    kwargs["type"] = "OPTION"
    kwargs["value"] = value

    return _get_object_dict(**kwargs)


def get_priority_model(
    name: str,
    value: int,
    customfields: Optional[dict[str, Any]] = None,
    **kwargs,
) -> dict[str, Any]:
    """
    Returns a dictionary containing a priority's attributes.

    Args:
        customfields (Optional[dict[str, Any]]): The priority's custom fields.
        name (str): The priority's name.
        value (int): The priority's value.
        **kwargs (dict[str, Any]): Additional keywords to pass to the priority's attributes.

    Returns:
        dict[str, Any]: A dictionary containing a priority's attributes.
    """

    if not customfields:
        customfields = {}

    kwargs["customfields"] = {
        "customfields": customfields,
        "total": len(customfields),
    }
    kwargs["name"] = name
    kwargs["type"] = "PRIORITY"
    kwargs["value"] = value

    return _get_object_dict(**kwargs)


def get_question_model(
    question_type: Literal["multiple_choice", "open", "true_false"],
    text: str,
    answers: Optional[list[str]] = None,
    customfields: Optional[dict[str, Any]] = None,
    **kwargs,
) -> dict[str, Any]:
    """
    Returns a dictionary containing a question's attributes.

    Args:
        customfields (Optional[dict[str, Any]]): The question's custom fields.
        question_type (Literal["multiple_choice", "open", "true_false"]): The question's type.
        text (str): The question's text.
        **kwargs (dict[str, Any]): Additional keywords to pass to the question's attributes.

    Returns:
        dict[str, Any]: A dictionary containing a question's attributes.
    """

    if not answers:
        answers = {
            "correct": [],
            "items": [],
            "total": 0,
        }

    kwargs["answers"] = answers

    if not customfields:
        customfields = {}

    kwargs["customfields"] = {
        "customfields": customfields,
        "total": len(customfields),
    }
    kwargs["question_type"] = question_type
    kwargs["text"] = text
    kwargs["type"] = "QUESTION"

    return _get_object_dict(**kwargs)


def get_rehearsal_run_model(
    rehearsal_run_items: Optional[list[str]] = None,
    customfields: Optional[dict[str, Any]] = None,
    **kwargs,
) -> dict[str, Any]:
    """
    Returns a dictionary containing a rehearsal run's attributes.

    Args:
        customfields (Optional[dict[str, Any]]): The rehearsal run's custom fields.
        rehearsal_run_items (Optional[list[str]]): The rehearsal run items.
        **kwargs (dict[str, Any]): Additional keywords to pass to the rehearsal run's attributes.

    Returns:
        dict[str, Any]: A dictionary containing a rehearsal run's attributes.
    """

    if not customfields:
        customfields = {}

    kwargs["customfields"] = {
        "customfields": customfields,
        "total": len(customfields),
    }

    if not rehearsal_run_items:
        rehearsal_run_items = []

    kwargs["rehearsal_run_items"] = rehearsal_run_items
    kwargs["type"] = "REHEARSAL_RUN"

    return _get_object_dict(**kwargs)


def get_rehearsal_run_item_model(
    customfields: Optional[dict[str, Any]] = None,
    **kwargs,
) -> dict[str, Any]:
    """
    Returns a dictionary containing a rehearsal run item's attributes.

    Args:
        customfields (Optional[dict[str, Any]]): The rehearsal run item's custom fields.
        **kwargs (dict[str, Any]): Additional keywords to pass to the rehearsal run item's attributes.

    Returns:
        dict[str, Any]: A dictionary containing a rehearsal run item's attributes.
    """

    if not customfields:
        customfields = {}

    kwargs["customfields"] = {
        "customfields": customfields,
        "total": len(customfields),
    }
    kwargs["type"] = "REHEARSAL_RUN_ITEM"

    return _get_object_dict(**kwargs)


def get_stack_model(
    difficulty: str,
    name: str,
    priority: str,
    customfields: Optional[dict[str, Any]] = None,
    description: Optional[str] = None,
    due_date: Optional[str] = None,
    items: Optional[list[str]] = None,
    **kwargs,
) -> dict[str, Any]:
    """
    Returns a dictionary containing a stack's attributes.

    Args:
        customfields (Optional[dict[str, Any]]): The stack's custom fields.
        description (Optional[str]): The stack's description.
        difficulty (str): The stack's difficulty.
        due_date (Optional[str]): The stack's due date.
        items (Optional[list[str]]): The stack's items.
        name (str): The stack's name.
        priority (str): The stack's priority.
        **kwargs (dict[str, Any]): Additional keywords to pass to the stack's attributes.

    Returns:
        dict[str, Any]: A dictionary containing a stack's attributes.
    """

    if not customfields:
        customfields = {}

    kwargs["customfields"] = {
        "customfields": customfields,
        "total": len(customfields),
    }

    kwargs["description"] = description
    kwargs["difficulty"] = difficulty
    kwargs["due_date"] = due_date

    if not items:
        items = []

    kwargs["items"] = {
        "items": items,
        "total": len(items),
    }
    kwargs["name"] = name
    kwargs["priority"] = priority
    kwargs["type"] = "STACK"

    return _get_object_dict(**kwargs)


def get_subject_model(
    difficulty: str,
    name: str,
    priority: str,
    customfields: Optional[dict[str, Any]] = None,
    teacher: Optional[str] = None,
    **kwargs,
) -> dict[str, Any]:
    """
    Returns a dictionary containing a subject's attributes.

    Args:
        customfields (Optional[dict[str, Any]]): The subject's custom fields.
        difficulty (str): The subject's difficulty.
        name (str): The subject's name.
        priority (str): The subject's priority.
        teacher (Optional[str]): The subject's teacher.
        **kwargs (dict[str, Any]): Additional keywords to pass to the subject's attributes.

    Returns:
        dict[str, Any]: A dictionary containing a subject's attributes.
    """

    if not customfields:
        customfields = {}

    kwargs["customfields"] = {
        "customfields": customfields,
        "total": len(customfields),
    }
    kwargs["difficulty"] = difficulty
    kwargs["name"] = name
    kwargs["priority"] = priority
    kwargs["teacher"] = teacher
    kwargs["type"] = "SUBJECT"

    return _get_object_dict(**kwargs)


def get_tag_model(
    name: str,
    customfields: Optional[dict[str, Any]] = None,
    **kwargs,
) -> dict[str, Any]:
    """
    Returns a dictionary containing a tag's attributes.

    Args:
        name (str): The tag's name.
        **kwargs (dict[str, Any]): Additional keywords to pass to the tag's attributes.

    Returns:
        dict[str, Any]: A dictionary containing a tag's attributes.
    """

    if not customfields:
        customfields = {}

    kwargs["customfields"] = {
        "customfields": customfields,
        "total": len(customfields),
    }
    kwargs["name"] = name
    kwargs["type"] = "TAG"

    return _get_object_dict(**kwargs)


def get_teacher_model(
    difficulty: str,
    name: str,
    priority: str,
    subjects: Optional[list[str]] = None,
    customfields: Optional[dict[str, Any]] = None,
    **kwargs,
) -> dict[str, Any]:
    """
    Returns a dictionary containing a teacher's attributes.

    Args:
        customfields (Optional[dict[str, Any]]): The teacher's custom fields.
        difficulty (str): The teacher's difficulty.
        name (str): The teacher's name.
        priority (str): The teacher's priority.
        subjects (Optional[list[str]]): The teacher's subjects.
        **kwargs (dict[str, Any]): Additional keywords to pass to the teacher's attributes.

    Returns:
        dict[str, Any]: A dictionary containing a teacher's attributes.
    """

    if not customfields:
        customfields = {}

    kwargs["customfields"] = {
        "customfields": customfields,
        "total": len(customfields),
    }
    kwargs["difficulty"] = difficulty
    kwargs["name"] = name
    kwargs["priority"] = priority

    if not subjects:
        subjects = []

    kwargs["subjects"] = subjects
    kwargs["type"] = "TEACHER"

    return _get_object_dict(**kwargs)


def get_user_model(
    name: str,
    customfields: Optional[dict[str, Any]] = None,
    **kwargs,
) -> dict[str, Any]:
    """
    Returns a dictionary containing a user's attributes.

    Args:
        customfields (Optional[dict[str, Any]]): The user's custom fields.
        name (str): The user's name.
        **kwargs (dict[str, Any]): Additional keywords to pass to the user's attributes.

    Returns:
        dict[str, Any]: A dictionary containing a user's attributes.
    """

    if not customfields:
        customfields = {}

    kwargs["customfields"] = {
        "customfields": customfields,
        "total": len(customfields),
    }
    kwargs["name"] = name
    kwargs["type"] = "USER"

    return _get_object_dict(**kwargs)


# ---------- Auto-Export ---------- #

# Auto-export all non-private symbols
__all__: Final[list[str]] = [
    key
    for (
        key,
        value,
    ) in globals().items()
    if not key.startswith("_") and callable(value)
]
