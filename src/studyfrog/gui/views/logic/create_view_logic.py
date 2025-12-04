"""
Author: Louis Goodnews
Date: 2025-11-16
"""

import tkinter

from typing import Any, Callable, Final, Literal, TypeAlias, Union

from common.events import (
    ADDED_FLASHCARD,
    ADDED_NOTE,
    ADDED_QUESTION,
    ADDED_STACK,
    ADDED_SUBJECT,
    ADDED_TEACHER,
    CALL_FUNCTION,
    FILTER_STACKS,
    GET_FORM,
    UPDATE_STACK,
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
    filter_stacks,
    get_difficulty,
    get_flashcard,
    get_note,
    get_priority,
    get_question,
    get_stack,
    get_subject,
    get_teacher,
    update_stack,
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
    log_debug,
    log_exception,
    log_info,
    publish_event,
)


# ---------- Types ---------- #

WhatType: TypeAlias = Literal[
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
    Callable[[dict[str, Any]], int],
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
    Callable[[Union[int, str]], dict[str, Any]],
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
    Callable[[Any], dict[str, Any]],
] = {
    "flashcard": get_flashcard_model,
    "note": get_note_model,
    "question": get_question_model,
    "stack": get_stack_model,
    "subject": get_subject_model,
    "teacher": get_teacher_model,
}


# ---------- Functions ---------- #


def append_to_stack(
    item: dict[str, Any],
    stack_key: str,
) -> None:
    """
    Appends the item to the stack.

    Args:
        item (dict[str, Any]): The item to append.
        stack_key (str): The key of the stack to append to.

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    try:
        stack: dict[str, Any] = (
            publish_event(
                event=FILTER_STACKS,
                namespace="GLOBAL",
                **{"key": stack_key},
            )
            .get(
                "filter_entries",
                {},
            )[0]
            .get(
                "result",
                {},
            )[0]
        )

        stack["items"]["items"].append(item["key"])

        stack["items"]["total"] += 1

        publish_event(
            event=UPDATE_STACK,
            namespace="GLOBAL",
            **{
                "entry": stack,
                "entry_id": stack["id"],
            },
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to append to stack",
            name=NAME,
        )
        raise Exception(f"Failed to append to stack: {e}") from e


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


def handle_answer_creation(form: dict[str, Any]) -> dict[str, Any]:
    """
    Handles the creation of a new answer.

    Args:
        form (dict[str, Any]): The form data for the answer.

    Returns:
        dict[str, Any]: The answer data.

    Raises:
        Exception: If the answer creation fails.
    """

    try:
        id: int = WHAT_TYPE_TO_DATABASE_ADDER["answer"](
            entry=WHAT_TYPE_TO_MODEL_GETTER["answer"](**form)
        )

        publish_event(
            event=WHAT_TYPE_TO_ADDED_EVENT["answer"],
            namespace="GLOBAL",
            **{
                "what": "answer",
                "model": WHAT_TYPE_TO_DATABASE_GETTER["answer"](entry_id=id),
            },
        )

        return WHAT_TYPE_TO_DATABASE_GETTER["answer"](entry_id=id)
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to handle answer creation",
            name=NAME,
        )
        raise Exception(f"Failed to handle answer creation: {e}") from e


def handle_flashcard_creation() -> None:
    """
    Handles the creation of a new flashcard.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If the flashcard creation fails.
    """

    try:
        form: dict[str, Any] = (
            publish_event(
                event=GET_FORM,
                namespace="FLASHCARD_CREATE_FORM",
            )
            .get(
                "on_get_form",
                {},
            )[0]
            .get(
                "result",
                {},
            )
        )

        if is_dict_empty(dictionary=form):
            raise Exception(
                f"Form data is empty - no data was retrieved from the form event. Check if the form event was published correctly and the namespace is correct. Received form: {form}"
            )

        id: int = WHAT_TYPE_TO_DATABASE_ADDER["flashcard"](
            entry=WHAT_TYPE_TO_MODEL_GETTER["flashcard"](**form)
        )

        log_info(
            message=f"Flashcard created successfully",
            name=NAME,
        )

        append_to_stack(
            item=WHAT_TYPE_TO_DATABASE_GETTER["flashcard"](entry_id=id),
            stack_key=form["stack"],
        )

        get_success_toast(
            message=f"Flashcard created successfully",
            title=f"Flashcard created successfully",
        )

        publish_event(
            event=WHAT_TYPE_TO_ADDED_EVENT["flashcard"],
            namespace="GLOBAL",
            **{
                "what": "flashcard",
                "model": WHAT_TYPE_TO_DATABASE_GETTER["flashcard"](entry_id=id),
            },
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to handle flashcard creation",
            name=NAME,
        )
        raise Exception(f"Failed to handle flashcard creation: {e}") from e


def handle_note_creation() -> None:
    """
    Handles the creation of a new note.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If the note creation fails.
    """

    try:
        form: dict[str, Any] = (
            publish_event(
                event=GET_FORM,
                namespace="NOTE_CREATE_FORM",
            )
            .get(
                "on_get_form",
                {},
            )[0]
            .get(
                "result",
                {},
            )
        )

        if is_dict_empty(dictionary=form):
            raise Exception(
                f"Form data is empty - no data was retrieved from the form event. Check if the form event was published correctly and the namespace is correct. Received form: {form}"
            )

        id: int = WHAT_TYPE_TO_DATABASE_ADDER["note"](
            entry=WHAT_TYPE_TO_MODEL_GETTER["note"](**form)
        )

        log_info(
            message=f"Note created successfully",
            name=NAME,
        )

        get_success_toast(
            message=f"Note created successfully",
            title=f"Note created successfully",
        )

        publish_event(
            event=WHAT_TYPE_TO_ADDED_EVENT["note"],
            namespace="GLOBAL",
            **{
                "what": "note",
                "model": WHAT_TYPE_TO_DATABASE_GETTER["note"](entry_id=id),
            },
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to handle note creation",
            name=NAME,
        )
        raise Exception(f"Failed to handle note creation: {e}") from e


def handle_question_creation() -> None:
    """
    Handles the creation of a new question.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If the question creation fails.
    """

    try:
        form: dict[str, Any] = (
            publish_event(
                event=GET_FORM,
                namespace="QUESTION_CREATE_FORM",
            )
            .get(
                "on_get_form",
                {},
            )[0]
            .get(
                "result",
                {},
            )
        )

        if is_dict_empty(dictionary=form):
            raise Exception(
                f"Form data is empty - no data was retrieved from the form event. Check if the form event was published correctly and the namespace is correct. Received form: {form}"
            )

        id: int = WHAT_TYPE_TO_DATABASE_ADDER["question"](
            entry=WHAT_TYPE_TO_MODEL_GETTER["question"](**form)
        )

        log_info(
            message=f"Question created successfully",
            name=NAME,
        )

        get_success_toast(
            message=f"Question created successfully",
            title=f"Question created successfully",
        )

        publish_event(
            event=WHAT_TYPE_TO_ADDED_EVENT["question"],
            namespace="GLOBAL",
            **{
                "what": "question",
                "model": WHAT_TYPE_TO_DATABASE_GETTER["question"](entry_id=id),
            },
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to handle question creation",
            name=NAME,
        )
        raise Exception(f"Failed to handle question creation: {e}") from e


def handle_stack_creation() -> None:
    """
    Handles the creation of a new stack.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If the stack creation fails.
    """

    try:
        form: dict[str, Any] = (
            publish_event(
                event=GET_FORM,
                namespace="STACK_CREATE_FORM",
            )
            .get(
                "on_get_form",
                {},
            )[0]
            .get(
                "result",
                {},
            )
        )

        if is_dict_empty(dictionary=form):
            raise Exception(
                f"Form data is empty - no data was retrieved from the form event. Check if the form event was published correctly and the namespace is correct. Received form: {form}"
            )

        id: int = WHAT_TYPE_TO_DATABASE_ADDER["stack"](
            entry=WHAT_TYPE_TO_MODEL_GETTER["stack"](**form)
        )

        log_info(
            message=f"Stack created successfully",
            name=NAME,
        )

        get_success_toast(
            message=f"Stack created successfully",
            title=f"Stack created successfully",
        )

        publish_event(
            event=WHAT_TYPE_TO_ADDED_EVENT["stack"],
            namespace="GLOBAL",
            **{
                "what": "stack",
                "model": WHAT_TYPE_TO_DATABASE_GETTER["stack"](entry_id=id),
            },
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to handle stack creation",
            name=NAME,
        )
        raise Exception(f"Failed to handle stack creation: {e}") from e


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
        publish_event(
            function="destroy",
            event=CALL_FUNCTION,
            namespace="CREATE_VIEW",
        )
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
        previous_what: WhatType = publish_event(
            event=CALL_FUNCTION,
            namespace="CREATE_VIEW",
            function="get_what",
        )["on_call_function"][0]["result"]

        publish_event(
            event=CALL_FUNCTION,
            namespace=f"{previous_what.upper()}_CREATE_FORM",
            function="handle_destruction",
        )

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
        what_type: WhatType = publish_event(
            event=CALL_FUNCTION,
            namespace="CREATE_VIEW",
            function="get_what",
        )["on_call_function"][0]["result"]

        what_type_to_handler: dict[WhatType, Callable[[], None]] = {
            "flashcard": handle_flashcard_creation,
            "note": handle_note_creation,
            "question": handle_question_creation,
            "stack": handle_stack_creation,
            "answer": handle_answer_creation,
        }

        what_type_to_handler[what_type.lower()]()

        publish_event(
            function="destroy",
            event=CALL_FUNCTION,
            namespace="CREATE_VIEW",
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to handle create button click event",
            name=NAME,
        )
        get_error_toast(
            message=f"Failed to create {what_type.title()}: {e}",
            title=f"Failed to create {what_type.title()}",
        )
        raise Exception(f"Failed to handle create button click event: {e}") from e


# ---------- Auto-Export ---------- #

# Auto-export all non-private symbols
__all__: Final[list[str]] = [
    "get_form_getter",
    "on_cancel_button_click",
    "on_combobox_change",
    "on_create_button_click",
]
