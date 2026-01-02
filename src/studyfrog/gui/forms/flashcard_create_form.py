"""
Author: Louis Goodnews
Date: 2025-12-13
Description: The flashcard create form of the application.
"""

import customtkinter as ctk

from tkinter.constants import NSEW, W
from typing import Any, Final

from constants.events import (
    CLEAR_CREATE_FORM,
    DESTROY_FLASHCARD_CREATE_FORM,
    GET_ALL_SUBJECTS_FROM_DB,
    GET_ALL_TEACHERS_FROM_DB,
    GET_CREATE_FORM,
)
from constants.gui import READONLY
from utils.dispatcher import dispatch, subscribe, unsubscribe
from utils.gui import destroy_widget_children
from utils.logging import log_error, log_info


# ---------- Exports ---------- #


__all__: Final[list[str]] = ["get_flashcard_create_form"]


# ---------- Constants ---------- #


FORM: Final[dict[str, Any]] = {}

MASTER: Final[ctk.CTkScrollableFrame] = None

SUBSCRIPTION_IDS: Final[list[str]] = []


# ---------- Helper Functions ---------- #


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
    Configures the grid of the flashcard create form.

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
        weight=1,
    )
    _get_master().grid_rowconfigure(
        index=1,
        weight=1,
    )
    _get_master().grid_rowconfigure(
        index=2,
        weight=0,
    )
    _get_master().grid_rowconfigure(
        index=3,
        weight=0,
    )


def _create_widgets() -> None:
    """
    Creates the flashcard create form's widgets.

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
        text="Front Text*: ",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    FORM["front"] = {
        "is_required": True,
        "variable": ctk.StringVar(),
    }

    font_textbox: ctk.CTkTextbox = ctk.CTkTextbox(
        master=_get_master(),
    )

    font_textbox.grid(
        column=1,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    font_textbox.bind(
        command=lambda event: FORM["front"]["variable"].set(
            value=font_textbox.get(
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
        text="Back Text*: ",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=1,
        sticky=NSEW,
    )

    FORM["back"] = {
        "is_required": True,
        "variable": ctk.StringVar(),
    }

    back_textbox: ctk.CTkTextbox = ctk.CTkTextbox(master=_get_master())

    back_textbox.grid(
        column=1,
        padx=5,
        pady=5,
        row=1,
        sticky=NSEW,
    )

    back_textbox.bind(
        command=lambda event: FORM["back"]["variable"].set(
            value=back_textbox.get(
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

    FORM["subject"] = {
        "is_required": True,
        "variable": ctk.StringVar(),
    }

    subject_combobox: ctk.CTkComboBox = ctk.CTkComboBox(
        master=_get_master(),
        values=subject_names,
        variable=FORM["subject"]["variable"],
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

    FORM["teacher"] = {
        "is_required": True,
        "variable": ctk.StringVar(),
    }

    teacher_combobox: ctk.CTkComboBox = ctk.CTkComboBox(
        master=_get_master(),
        values=teacher_names,
        variable=FORM["teacher"]["variable"],
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

    if MASTER is None:
        raise ValueError(
            "The master frame has not been initialized yet."
            "The method '_set_master' must be executed first."
        )

    return MASTER


def _on_clear_create_form() -> None:
    """
    Handles the 'CLEAR_CREATE_FORM' event.

    Args:
        None

    Returns:
        None
    """

    for value in FORM.values():
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
    Handles the 'DESTROY_FLASHCARD_CREATE_FORM' event.

    Args:
        None

    Returns:
        None
    """

    _unsubscribe_from_events()

    _clear_master()

    FORM.clear()

    MASTER = None


def _on_get_create_form() -> dict[str, Any]:
    """
    Handles the 'GET_CREATE_FORM' event.

    Args:
        None

    Returns:
        dict[str, Any]: The form.
    """

    return {
        key: {
            "is_required": value["is_required"],
            "value": value["variable"].get(),
        }
        for (
            key,
            value,
        ) in FORM.items()
    }


def _set_master(scrollable_frame: ctk.CTkScrollableFrame) -> None:
    """
    Sets the master frame widget.

    Args:
        scrollable_frame (ctk.CTkScrollableFrame): The scrollable frame to add the form to.

    Returns:
        None
    """

    global MASTER

    MASTER = scrollable_frame


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
            "event": DESTROY_FLASHCARD_CREATE_FORM,
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
        SUBSCRIPTION_IDS.append(
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

    for uuid in SUBSCRIPTION_IDS:
        unsubscribe(uuid=uuid)

    log_info(message="Unsubscribed from all events for the flashcard create form.")

    SUBSCRIPTION_IDS.clear()


# ---------- Public Functions ---------- #


def get_flashcard_create_form(scrollable_frame: ctk.CTkScrollableFrame) -> None:
    """
    Gets the flashcard create form.

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
        log_error(message=f"Failed to get flashcard create form: {e}")
        raise e
