"""
Author: Louis Goodnews
Date: 2025-12-13
Description: The stack create form of the application.
"""

import customtkinter as ctk

from tkinter.constants import NSEW, W
from typing import Any, Final, Union

from constants.events import (
    CLEAR_CREATE_FORM,
    DESTROY_STACK_CREATE_FORM,
    GET_ALL_SUBJECTS_FROM_DB,
    GET_ALL_TEACHERS_FROM_DB,
    GET_CREATE_FORM,
)
from constants.gui import READONLY
from utils.dispatcher import dispatch, subscribe, unsubscribe
from utils.gui import destroy_widget_children
from utils.logging import log_error, log_info


# ---------- Exports ---------- #


__all__: Final[list[str]] = ["get_stack_create_form"]


# ---------- Constants ---------- #


_FORM: Final[dict[str, Any]] = {}

_MASTER: Final[ctk.CTkScrollableFrame] = None

_SUBSCRIPTION_IDS: Final[list[str]] = []


# ---------- Helper Functions ---------- #


def _get_form() -> dict[str, Any]:
    """
    Returns the underlying dictionary 'serializing' the UI form.

    Args:
        None

    Returns:
        dict[str, Any]: The underlying dictionary 'serializing' the UI form.
    """

    return _FORM


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
    Clears the master frame.

    Args:
        None

    Returns:
        None
    """

    destroy_widget_children(widget=_get_master())


def _configure_grid() -> None:
    """
    Configures the grid of the stack create form.

    Args:
        None

    Returns:
        None
    """

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
        weight=0,
    )


def _create_widgets() -> None:
    """
    Creates the stack create form's widgets.

    Args:
        None

    Returns:
        None
    """

    ctk.CTkLabel(
        anchor=W,
        font=(
            "Helvetica",
            12,
            "bold",
        ),
        master=_get_master(),
        text="Name*: ",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    _update_form(
        key="name",
        value={
            "is_required": True,
            "variable": ctk.StringVar(),
        },
    )

    ctk.CTkEntry(
        master=_get_master(),
        placeholder_text="Enter stack name here...",
        textvariable=_get_form()["name"]["variable"],
    ).grid(
        column=1,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    ctk.CTkLabel(
        anchor=W,
        font=(
            "Helvetica",
            12,
            "bold",
        ),
        master=_get_master(),
        text="Description: ",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=1,
        sticky=NSEW,
    )

    _update_form(
        key="description",
        value={
            "is_required": False,
            "variable": ctk.StringVar(),
        },
    )

    description_textbox: ctk.CTkTextbox = ctk.CTkTextbox(master=_get_master())

    description_textbox.grid(
        column=1,
        padx=5,
        pady=5,
        row=1,
        sticky=NSEW,
    )

    description_textbox.bind(
        command=lambda event: _get_form()["description"]["variable"].set(
            value=description_textbox.get(
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
        text="Subject: ",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=2,
        sticky=NSEW,
    )

    subject_names: list[str] = [
        subject.get(
            "name",
            None,
        )
        for subject in (
            dispatch(
                event=GET_ALL_SUBJECTS_FROM_DB,
                namespace="GLOBAL",
                table_name="subjects",
            )
            .get(
                "get_all_entries",
                [{}],
            )[0]
            .get(
                "result",
                [],
            )
        )
    ]

    _update_form(
        key="subject",
        value={
            "is_required": True,
            "variable": ctk.StringVar(),
        },
    )

    subject_combobox: ctk.CTkComboBox = ctk.CTkComboBox(
        master=_get_master(),
        state=READONLY,
        values=subject_names,
        variable=_get_form()["subject"]["variable"],
    )

    subject_combobox.grid(
        column=1,
        padx=5,
        pady=5,
        row=2,
        sticky=NSEW,
    )

    ctk.CTkLabel(
        anchor=W,
        font=(
            "Helvetica",
            12,
            "bold",
        ),
        master=_get_master(),
        text="Teacher: ",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=3,
        sticky=NSEW,
    )

    teacher_names: list[str] = [
        teacher.get(
            "name",
            None,
        )
        for teacher in (
            dispatch(
                event=GET_ALL_TEACHERS_FROM_DB,
                namespace="GLOBAL",
                table_name="teachers",
            )
            .get(
                "get_all_entries",
                [{}],
            )[0]
            .get(
                "result",
                [],
            )
        )
    ]

    _update_form(
        key="teacher",
        value={
            "is_required": True,
            "variable": ctk.StringVar(),
        },
    )

    teacher_combobox: ctk.CTkComboBox = ctk.CTkComboBox(
        master=_get_master(),
        state=READONLY,
        values=teacher_names,
        variable=_get_form()["teacher"]["variable"],
    )

    teacher_combobox.grid(
        column=1,
        padx=5,
        pady=5,
        row=3,
        sticky=NSEW,
    )


def _get_master() -> ctk.CTkScrollableFrame:
    """
    Returns the master frame widget.

    Args:
        None

    Returns:
        ctk.CTkScrollableFrame: The master frame widget.
    """

    if _MASTER is None:
        raise ValueError(
            "The master frame has not been initialized yet."
            "The method '_set_master' must be executed first."
        )

    return _MASTER


def _on_clear_create_form() -> None:
    """
    Handles the 'CLEAR_CREATE_FORM' event.

    Args:
        None

    Returns:
        None
    """

    for value in _get_form().values():
        if isinstance(
            value["variable"],
            ctk.StringVar,
        ):
            value["variable"].set(value="")
        elif isinstance(
            value["variable"],
            ctk.BooleanVar,
        ):
            value["variable"].set(value=not value["variable"].get())


def _on_destroy() -> None:
    """
    Handles the 'DESTROY_STACK_CREATE_FORM' event.

    Args:
        None

    Returns:
        None
    """

    _unsubscribe_from_events()

    _clear_master()

    _get_form().clear()

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
        "origin": "stack_create_form",
    }


def _set_master(scrollable_frame: ctk.CTkScrollableFrame) -> None:
    """
    Sets the master frame widget.

    Args:
        scrollable_frame (ctk.CTkScrollableFrame): The scrollable frame to add the form to.

    Returns:
        None
    """

    global _MASTER

    _MASTER = scrollable_frame


def _subscribe_to_events() -> None:
    """
    Subscribes to events.

    Args:
        None

    Returns:
        None
    """

    subscriptions: list[dict[str, Any]] = [
        {
            "event": CLEAR_CREATE_FORM,
            "namespace": "GLOBAL",
            "function": _on_clear_create_form,
            "persistent": True,
            "priority": 1,
        },
        {
            "event": DESTROY_STACK_CREATE_FORM,
            "namespace": "GLOBAL",
            "function": _on_destroy,
            "persistent": True,
            "priority": 1,
        },
        {
            "event": GET_CREATE_FORM,
            "namespace": "GLOBAL",
            "function": _on_get_create_form,
            "persistent": True,
            "priority": 1,
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
    Unsubscribes from events.

    Args:
        None

    Returns:
        None
    """

    for uuid in _SUBSCRIPTION_IDS:
        unsubscribe(uuid=uuid)

    log_info(message="Unsubscribed from all events for the stack create form.")

    _SUBSCRIPTION_IDS.clear()


# ---------- Public Functions ---------- #


def get_stack_create_form(scrollable_frame: ctk.CTkScrollableFrame) -> None:
    """
    Gets the stack create form.

    Args:
        scrollable_frame (ctk.CTkScrollableFrame): The scrollable frame to add the form to.

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    try:
        _set_master(scrollable_frame)
        _clear_master()
        _create_widgets()
        _configure_grid()
        _subscribe_to_events()
    except Exception as e:
        log_error(message=f"Failed to get stack create form: {e}")
        raise e
