"""
Author: Louis Goodnews
Date: 2025-11-16
"""

import tkinter

from tkinter.constants import NSEW
from typing import Any, Final, Literal, Optional

from common.events import GET_FORM
from gui.factory import get_entry, get_label
from utils.utils import destroy_widget_children, log_exception, log_info, register_subscription


# ---------- Constants ---------- #

FORM_VARIABLES: Final[dict[str, tkinter.Widget]] = {}

NAME: Final[Literal["gui.views.forms.stack_create_form"]] = "gui.views.forms.stack_create_form"

SUBSCRIPTION: Optional[str] = None


# ---------- Functions ---------- #


def clear_master_frame(master: tkinter.Frame) -> None:
    """
    Clear the master frame.

    Args:
        master (tkinter.Frame): The master frame.

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """
    try:
        destroy_widget_children(master)
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to clear master frame",
            name=NAME,
        )
        raise Exception(f"Failed to clear master frame: {e}") from e


def configure_master_grid(master: tkinter.Frame) -> None:
    """
    Configure the master grid.

    Args:
        master (tkinter.Frame): The master frame.

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """
    try:
        master.grid_columnconfigure(
            index=0,
            weight=0,
        )
        master.grid_columnconfigure(
            index=1,
            weight=1,
        )
        master.grid_rowconfigure(
            index=0,
            weight=0,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to configure master grid",
            name=NAME,
        )
        raise Exception(f"Failed to configure master grid: {e}") from e


def create_widgets(master: tkinter.Frame) -> None:
    """
    Create the widgets.

    Args:
        master (tkinter.Frame): The master frame.

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """
    try:
        name_label: tkinter.Label = get_label(
            master=master,
            text="Name*: ",
        )

        name_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        name_var: tkinter.StringVar = tkinter.StringVar()

        name_entry: tkinter.Entry = get_entry(
            master=master,
            textvariable=name_var,
        )

        name_entry.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        FORM_VARIABLES["name"] = name_var
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to create widgets",
            name=NAME,
        )
        raise Exception(f"Failed to create widgets: {e}") from e


def get_stack_create_form(master: tkinter.Frame) -> None:
    """
    Get the stack create form.

    Args:
        master (tkinter.Frame): The master frame.

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    global SUBSCRIPTION

    try:
        log_info(
            message="Getting stack create form",
            name=NAME,
        )

        clear_master_frame(master=master)
        configure_master_grid(master=master)
        create_widgets(master=master)

        SUBSCRIPTION = register_subscription(
            event=GET_FORM,
            function=on_get_form,
            namespace="CREATE_FORMS",
            persistent=False,
        )

        log_info(
            message="Got stack create form successfully",
            name=NAME,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get stack create form",
            name=NAME,
        )
        raise Exception(f"Failed to get stack create form: {e}") from e


def get_form() -> dict[str, Any]:
    """
    Get the form.

    Args:
        None

    Returns:
        dict[str, Any]: The form.

    Raises:
        Exception: If an error occurs.
    """

    try:
        result: dict[str, Any] = {"what": "stack"}

        result.update(
            {
                key: value.get()
                for (
                    key,
                    value,
                ) in FORM_VARIABLES.items()
            }
        )

        return result
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get form",
            name=NAME,
        )
        raise Exception(f"Failed to get form: {e}") from e


def on_get_form() -> dict[str, Any]:
    """
    Handle the get form event.

    Args:
        None

    Returns:
        dict[str, Any]: The form.

    Raises:
        Exception: If an error occurs.
    """

    try:
        return get_form()
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to handle get form event",
            name=NAME,
        )
        raise Exception(f"Failed to handle get form event: {e}") from e


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
