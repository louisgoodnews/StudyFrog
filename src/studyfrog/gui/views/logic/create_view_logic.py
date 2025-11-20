"""
Author: Louis Goodnews
Date: 2025-11-16
"""

import tkinter

from typing import Callable, Final, Literal, Type

from gui.views.forms.flashcard_create_form import get_flashcard_create_form
from gui.views.forms.note_create_form import get_note_create_form
from gui.views.forms.question_create_form import get_question_create_form
from gui.views.forms.stack_create_form import get_stack_create_form
from gui.views.forms.subject_create_form import get_subject_create_form
from gui.views.forms.teacher_create_form import get_teacher_create_form
from utils.utils import log_exception


# ---------- Constants ---------- #

NAME: Final[Literal["gui.views.logic.create_view_logic"]] = "gui.views.logic.create_view_logic"

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


# ---------- Functions ---------- #


def get_form_getter(what: WhatType) -> Callable[[tkinter.Frame], None]:
    """
    Returns the getter for the specified type.

    Args:
        what (WhatType): The type of entity to create.

    Returns:
        Callable[[tkinter.Frame], None]: The getter for the specified type.
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
    """

    try:
        get_form_getter(value)(master=master)
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to handle combobox change event",
            name=NAME,
        )
        raise Exception(f"Failed to handle combobox change event: {e}") from e


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
