"""
Author: Louis Goodnews
Date: 2025-12-13
Description: The question create form of the application.
"""

import tkinter
import customtkinter as ctk

from tkinter.constants import NSEW, W
from typing import Any, Callable, Final, Literal, Optional, Union

from constants.common import GLOBAL, QUESTION_TYPES
from constants.events import (
    DESTROY_ANSWER_CREATE_FORM,
    DESTROY_QUESTION_CREATE_FORM,
    GET_CREATE_FORM,
)
from gui.forms.answer_create_form import (
    get_answer_choice_create_form,
    get_answer_open_ended_create_form,
    get_answer_true_false_create_form,
)
from utils.dispatcher import dispatch, subscribe, unsubscribe
from utils.gui import destroy_widget_children, reset_widget_grid
from utils.logging import log_error, log_info


# ---------- Exports ---------- #


__all__: Final[list[str]] = ["get_question_create_form"]


# ---------- Constants ---------- #

_ANSWER_FRAME: Optional[ctk.CTkFrame] = None

_FORM: Final[dict[str, Any]] = {}

_MASTER: Optional[ctk.CTkScrollableFrame] = None

_SUBSCRIPTION_IDS: Final[list[str]] = []


# ---------- Helper Functions ---------- #


def _get_answer_frame() -> ctk.CTkFrame:
    """
    Returns the ctk.CTkFrame answer frame widget.

    Args:
        None

    Returns:
        ctk.CTkFrame: The answer frame widget.
    """

    if _ANSWER_FRAME is None:
        raise ValueError(
            "Answer frame is None. Please provide an answer frame (call '_set_answer_frame' function first)."
        )

    return _ANSWER_FRAME


def _get_form() -> dict[str, Any]:
    """
    Returns the underlying dictionary 'serializing' the UI form.

    Args:
        None

    Returns:
        dict[str, Any]: The underlying dictionary 'serializing' the UI form.

    Raises:
        ValueError: If the form is None.
    """

    if _FORM is None:
        raise ValueError(
            "Form is None. This should never happen and likely is the result of a serious error."
        )

    return _FORM


def _get_master() -> ctk.CTkScrollableFrame:
    """
    Returns the ctk.CTkScrollableFrame master widget.

    Args:
        None

    Returns:
        ctk.CTkScrollableFrame: The master frame widget.
    """

    if _MASTER is None:
        raise ValueError(
            "Master is None. Please provide a master frame (call '_set_master' function first)."
        )

    return _MASTER


def _set_answer_frame(frame: ctk.CTkFrame) -> None:
    """
    Sets the ctk.CTkFrame answer frame widget.

    Args:
        frame (ctk.CTkFrame): The frame to set as the answer frame.

    Returns:
        None
    """

    global _ANSWER_FRAME

    _ANSWER_FRAME = frame

    log_info(message="ctk.CTkFrame answer frame widget set successfully.")


def _set_master(scrollable_frame: ctk.CTkScrollableFrame) -> None:
    """
    Sets the ctk.CTkScrollableFrame master widget.

    Args:
        scrollable_frame (ctk.CTkScrollableFrame): The scrollable frame to add the form to.

    Returns:
        None
    """

    global _MASTER

    _MASTER = scrollable_frame

    log_info(message="ctk.CTkScrollableFrame master widget set successfully.")


def _update_form(
    key: Union[list[str], str],
    value: Any,
) -> None:
    """
    Updates the underlying dictionary 'serializing' the UI form with the passed key and value pairs.

    Args:
        key (Union[list[str], str]): The key(s) to update with the passed value.
        value (Any): The value to update the passed key(s) with.

    Returns:
        None
    """

    if isinstance(
        key,
        list,
    ):
        for _key in key:
            _get_form()[_key] = value

        return

    _get_form()[key] = value


# ---------- Private Functions ---------- #


def _clear_master() -> None:
    """
    Clears the ctk.CTkScrollableFrame master widget.

    Args:
        None

    Returns:
        None
    """

    destroy_widget_children(widget=_get_master())


def _configure_grid() -> None:
    """
    Configures the ctk.CTkScrollableFrame master widget's grid.

    Args:
        None

    Returns:
        None
    """

    reset_widget_grid(widget=_get_master())

    _get_master().grid_columnconfigure(
        index=0,
        weight=0,
    )
    _get_master().grid_columnconfigure(
        index=1,
        weight=1,
    )
    _get_master().grid_rowconfigure(
        index=0,
        weight=1,
    )
    _get_master().grid_rowconfigure(
        index=1,
        weight=0,
    )
    _get_master().grid_rowconfigure(
        index=2,
        weight=1,
    )


def _create_widgets() -> None:
    """
    Creates the widgets of the question create form.

    Args:
        None

    Returns:
        None
    """

    question_frame: ctk.CTkFrame = ctk.CTkFrame(master=_get_master())

    question_frame.grid_columnconfigure(
        index=0,
        weight=0,
    )
    question_frame.grid_columnconfigure(
        index=1,
        weight=1,
    )
    question_frame.grid_rowconfigure(
        index=0,
        weight=1,
    )

    question_frame.grid(
        column=0,
        columnspan=2,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    _update_form(
        key="text",
        value={
            "is_required": True,
            "variable": ctk.StringVar(),
        },
    )

    ctk.CTkLabel(
        anchor=W,
        font=(
            "Helvetica",
            12,
            "bold",
        ),
        master=question_frame,
        text="Question text*: ",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    text_box: ctk.CTkTextbox = ctk.CTkTextbox(master=question_frame)

    text_box.grid(
        column=1,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    text_box.bind(
        command=lambda event: _get_form()["text"]["variable"].set(
            value=text_box.get(
                index1="1.0",
                index2="end-1c",
            )
        ),
        sequence="<KeyRelease>",
    )

    ctk.CTkLabel(
        anchor=W,
        font=(
            "Helvetica",
            12,
            "bold",
        ),
        master=_get_master(),
        text="Select answer type*: ",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=1,
        sticky=NSEW,
    )

    _update_form(
        key="answer_type",
        value={
            "is_required": True,
            "variable": ctk.StringVar(),
        },
    )

    ctk.CTkComboBox(
        command=_on_combobox_select,
        font=(
            "Helvetica",
            12,
            "bold",
        ),
        master=_get_master(),
        values=QUESTION_TYPES,
        variable=_get_form()["answer_type"]["variable"],
    ).grid(
        column=1,
        padx=5,
        pady=5,
        row=1,
        sticky=NSEW,
    )

    answer_frame: ctk.CTkFrame = ctk.CTkFrame(master=_get_master())

    answer_frame.grid(
        column=0,
        columnspan=2,
        padx=5,
        pady=5,
        row=2,
        sticky=NSEW,
    )

    _set_answer_frame(frame=answer_frame)


def _on_combobox_select(value: str) -> None:
    """
    Handles the Combobox widget#s <<ComboboxSelected>> event.

    Args:
        value (str): The value of the selected item.

    Returns:
        None
    """

    dispatch(
        event=DESTROY_ANSWER_CREATE_FORM,
        namespace=GLOBAL,
    )

    value_to_answer_type: dict[
        Literal[
            "Multiple or single choice answer",
            "Open answer",
            "True or false",
        ],
        Callable[[tkinter.Widget], None],
    ] = {
        "Multiple or single choice answer": get_answer_choice_create_form,
        "Open answer": get_answer_open_ended_create_form,
        "True or false": get_answer_true_false_create_form,
    }

    destroy_widget_children(widget=_get_answer_frame())
    reset_widget_grid(widget=_get_answer_frame())

    value_to_answer_type[value](_get_answer_frame())


def _on_destroy() -> None:
    """
    Handles the 'DESTROY_QUESTION_CREATE_FORM' event.

    Args:
        None

    Returns:
        None
    """

    global _MASTER

    _unsubscribe_from_events()

    _MASTER = None


def _on_get_create_form() -> dict[str, Any]:
    """
    Handles the 'GET_CREATE_FORM' event.

    Args:
        None

    Returns:
        dict[str, Any]: The form.
    """

    return {
        "form_content": {
            key: {
                "is_required": value["is_required"],
                "value": value["variable"].get(),
            }
            for (
                key,
                value,
            ) in _get_form().items()
        },
        "origin": "question_create_form",
    }


def _subscribe_to_events() -> None:
    """
    Subscribes to events for the question create form.

    Agrs:
        None

    Returns:
        None
    """

    subscriptions: list[dict[str, Any]] = [
        {
            "event": DESTROY_QUESTION_CREATE_FORM,
            "function": _on_destroy,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": GET_CREATE_FORM,
            "function": _on_get_create_form,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
    ]

    for subscription in subscriptions:
        _SUBSCRIPTION_IDS.append(
            subscribe(
                event=subscription["event"],
                function=subscription["function"],
                namespace=subscription["namespace"],
                persistent=subscription["persistent"],
                priority=subscription["priority"],
            )
        )


def _unsubscribe_from_events() -> None:
    """
    Unsubscribes from events for the question create form.

    Agrs:
        None

    Returns:
        None
    """

    for uuid in _SUBSCRIPTION_IDS:
        unsubscribe(uuid=uuid)

    log_info(message="Unsubscribed from all events for the question create form.")

    _SUBSCRIPTION_IDS.clear()


# ---------- Public Functions ---------- #


def get_question_create_form(scrollable_frame: ctk.CTkScrollableFrame) -> None:
    """
    Gets the question create form.

    Args:
        scrollable_frame (ctk.CTkScrollableFrame): The scrollable frame to add the form to.

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    try:
        _set_master(scrollable_frame=scrollable_frame)
        _clear_master()
        _configure_grid()
        _create_widgets()
        _subscribe_to_events()
    except Exception as e:
        log_error(message=f"Failed to get question create form: {e}")
        raise e
