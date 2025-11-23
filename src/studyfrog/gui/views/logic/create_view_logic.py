"""
Author: Louis Goodnews
Date: 2025-11-16
"""

import tkinter

from typing import Any, Callable, Final, Literal, Type

from common.events import (
    ADDED_FLASHCARD,
    ADDED_NOTE,
    ADDED_QUESTION,
    ADDED_STACK,
    ADDED_SUBJECT,
    ADDED_TEACHER,
    GET_FORM,
)
from core.models import (
    get_flashcard_model,
    get_note_model,
    get_question_model,
    get_stack_model,
    get_subject_model,
    get_teacher_model,
)
from core.objects import (
    add_flashcard,
    add_note,
    add_question,
    add_stack,
    add_subject,
    add_teacher,
    get_difficulty,
    get_flashcard,
    get_note,
    get_priority,
    get_question,
    get_stack,
    get_subject,
    get_teacher,
)
from gui.factory import get_error_toast, get_success_toast
from gui.views.forms.flashcard_create_form import get_flashcard_create_form
from gui.views.forms.note_create_form import get_note_create_form
from gui.views.forms.question_create_form import get_question_create_form
from gui.views.forms.stack_create_form import get_stack_create_form
from gui.views.forms.subject_create_form import get_subject_create_form
from gui.views.forms.teacher_create_form import get_teacher_create_form
from utils.utils import (
    is_dict_empty,
    is_key_in_dict,
    log_exception,
    log_info,
    publish_event,
)


# ---------- Types ---------- #

WhatType: Type[
    Literal[
        "flashcard",
        "note",
        "question",
        "stack",
        "subject",
        "teacher",
    ]
] = Literal[
    "flashcard",
    "note",
    "question",
    "stack",
    "subject",
    "teacher",
]


# ---------- Constants ---------- #

NAME: Final[Literal["gui.views.logic.create_view_logic"]] = "gui.views.logic.create_view_logic"

NAMESPACE: Final[Literal["CREATE_FORMS"]] = "CREATE_FORMS"

WHAT_TYPE_TO_ADDED_EVENT: dict[
    WhatType,
    Literal[
        "added_flashcard",
        "added_note",
        "added_question",
        "added_stack",
        "added_subject",
        "added_teacher",
    ],
] = {
    "flashcard": ADDED_FLASHCARD,
    "note": ADDED_NOTE,
    "question": ADDED_QUESTION,
    "stack": ADDED_STACK,
    "subject": ADDED_SUBJECT,
    "teacher": ADDED_TEACHER,
}

WHAT_TYPE_TO_FORM_GETTER: dict[
    WhatType,
    Callable[[tkinter.Frame], None],
] = {
    "flashcard": get_flashcard_create_form,
    "note": get_note_create_form,
    "question": get_question_create_form,
    "stack": get_stack_create_form,
    "subject": get_subject_create_form,
    "teacher": get_teacher_create_form,
}

WHAT_TYPE_TO_DATABASE_ADDER: dict[
    WhatType,
    Callable[[dict[str, Any]], None],
] = {
    "flashcard": add_flashcard,
    "note": add_note,
    "question": add_question,
    "stack": add_stack,
    "subject": add_subject,
    "teacher": add_teacher,
}

WHAT_TYPE_TO_DATABASE_GETTER: dict[
    WhatType,
    Callable[[dict[str, Any]], None],
] = {
    "flashcard": get_flashcard,
    "note": get_note,
    "question": get_question,
    "stack": get_stack,
    "subject": get_subject,
    "teacher": get_teacher,
}

WHAT_TYPE_TO_MODEL_GETTER: dict[
    WhatType,
    Callable[[Any], None],
] = {
    "flashcard": get_flashcard_model,
    "note": get_note_model,
    "question": get_question_model,
    "stack": get_stack_model,
    "subject": get_subject_model,
    "teacher": get_teacher_model,
}


# ---------- Functions ---------- #


def get_form_getter(what: WhatType) -> Callable[[tkinter.Frame], None]:
    """
    Returns the getter for the specified type.

    Args:
        what (WhatType): The type of entity to create.

    Returns:
        Callable[[tkinter.Frame], None]: The getter for the specified type.

    Raises:
        Exception: If the specified type is not supported.
    """

    try:
        return WHAT_TYPE_TO_FORM_GETTER[what]
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get getter",
            name=NAME,
        )
        raise Exception(f"Failed to get getter: {e}") from e


def on_cancel_button_click() -> None:
    """
    Handles the cancel button click event.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    try:
        pass
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to handle cancel button click event",
            name=NAME,
        )
        raise Exception(f"Failed to handle cancel button click event: {e}") from e


def on_combobox_change(
    master: tkinter.Frame,
    value: WhatType,
) -> None:
    """
    Handles the combobox change event.

    Args:
        master (tkinter.Frame): The master frame.
        value (WhatType): The value of the combobox.

    Returns:
        None

    Raises:
        Exception: If the specified type is not supported.
    """

    try:
        get_form_getter(what=value.lower())(master=master)
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to handle combobox change event",
            name=NAME,
        )
        raise Exception(f"Failed to handle combobox change event: {e}") from e


def on_create_button_click() -> None:
    """
    Handles the create button click event.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    try:
        form_data: dict[str, Any] = next(
            (
                dictionary
                for dictionary in publish_event(
                    event=GET_FORM,
                    namespace=NAMESPACE,
                )["on_get_form"]
            ),
            {},
        ).get(
            "result",
            {},
        )

        what: Literal[
            "flashcard",
            "note",
            "question",
            "stack",
            "subject",
            "teacher",
        ] = form_data.pop(
            "what",
            "flashcard",
        )

        if is_dict_empty(dictionary=form_data):
            raise Exception("Form data is empty")

        if not is_key_in_dict(
            dictionary=form_data,
            key="difficulty",
        ):
            form_data["difficulty"] = get_difficulty(entry_id=3).get("key")

        if not is_key_in_dict(
            dictionary=form_data,
            key="priority",
        ):
            form_data["priority"] = get_priority(entry_id=5).get("key")

        id: int = WHAT_TYPE_TO_DATABASE_ADDER[what](
            entry=WHAT_TYPE_TO_MODEL_GETTER[what](**form_data)
        )

        log_info(
            message=f"{what.title()} created successfully",
            name=NAME,
        )

        get_success_toast(
            message=f"{what.title()} created successfully",
            title=f"{what.title()} created successfully",
        )

        publish_event(
            event=WHAT_TYPE_TO_ADDED_EVENT[what],
            namespace="GLOBAL",
            **{
                "what": what,
                "model": WHAT_TYPE_TO_DATABASE_GETTER[what](entry_id=id),
            },
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to handle create button click event",
            name=NAME,
        )
        get_error_toast(
            message=f"Failed to create {what.title()}: {e}",
            title=f"Failed to create {what.title()}",
        )
        raise Exception(f"Failed to handle create button click event: {e}") from e


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
