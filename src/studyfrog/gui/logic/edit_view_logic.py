"""
Author: Louis Goodnews
Date: 2026-01-09
Description: The logic of the edit view of the application.
"""

import customtkinter as ctk

from typing import Any, Final

from constants.common import GLOBAL
from constants.events import DESTROY_EDIT_VIEW, GET_DELETE_CONFIRMATION_VIEW
from utils.dispatcher import dispatch

# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "on_cancel_button_click",
    "on_delete_button_click",
    "on_save_button_click",
]


# ---------- Helper Functions ---------- #


# ---------- Private Functions ---------- #


# ---------- Public Functions ---------- #


def on_cancel_button_click() -> None:
    """
    Handles the 'cancel' button click.

    Args:
        None

    Returns:
        None
    """

    dispatch(
        event=DESTROY_EDIT_VIEW,
        namespace=GLOBAL,
    )


def on_delete_button_click(obj: dict[str, Any]) -> None:
    """
    Handles the 'delete' button click.

    Args:
        obj (dict[str, Any]): The object to delete.

    Returns:
        None
    """

    dispatch(
        event=GET_DELETE_CONFIRMATION_VIEW,
        namespace=GLOBAL,
        obj=obj,
        toplevel=ctk.CTkToplevel(),
    )

    # TODO:
    #   - catch 'delete' event from database and check, if it corresponds to the passed object's ID
    #   - dispatch edit view destruction, if it corresponds, else, do nothing

    dispatch(
        event=DESTROY_EDIT_VIEW,
        namespace=GLOBAL,
    )


def on_save_button_click() -> None:
    """
    Handles the 'save' button click.

    Args:
        None

    Returns:
        None
    """

    dispatch(
        event=DESTROY_EDIT_VIEW,
        namespace=GLOBAL,
    )
