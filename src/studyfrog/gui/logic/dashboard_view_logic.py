"""
Author: Louis Goodnews
Date: 2025-12-12
Description: The logic of the dashboard view of the application.
"""

import customtkinter as ctk

from typing import Any, Final

from constants.common import GLOBAL
from constants.events import (
    DESTROY_DASHBOARD_VIEW,
    GET_CREATE_VIEW,
    GET_DELETE_CONFIRMATION_VIEW,
    GET_EDIT_VIEW,
    GET_REHEARSAL_RUN_SETUP_VIEW,
    GET_VIEW_VIEW,
)
from utils.dispatcher import dispatch
from utils.logging import log_error


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "on_create_button_click",
    "on_delete_button_click",
    "on_edit_button_click",
    "on_view_button_click",
]


# ---------- Functions ---------- #


def on_create_button_click() -> None:
    """
    Handler triggered when the create button is clicked.

    Args:
        None

    Returns:
        None
    """

    try:
        dispatch(
            event=GET_CREATE_VIEW,
            namespace=GLOBAL,
            toplevel=ctk.CTkToplevel(),
        )
    except Exception as e:
        log_error(message=f"Caught an exception while attempting to create a new stack: {e}")
        raise e


def on_delete_button_click(stack: dict[str, Any]) -> None:
    """
    Handler triggered when the delete button is clicked.

    Args:
        stack (dict[str, Any]): The stack to delete.

    Returns:
        None
    """

    try:
        dispatch(
            event=GET_DELETE_CONFIRMATION_VIEW,
            namespace=GLOBAL,
            model_dict=stack,
            toplevel=ctk.CTkToplevel(),
        )
    except Exception as e:
        log_error(message=f"Caught an exception while attempting to create a new stack: {e}")
        raise e


def on_edit_button_click(stack: dict[str, Any]) -> None:
    """
    Handler triggered when the edit button is clicked.

    Args:
        stack (dict[str, Any]): The stack to edit.

    Returns:
        None
    """

    try:
        dispatch(
            event=GET_EDIT_VIEW,
            obj=stack,
            namespace=GLOBAL,
            toplevel=ctk.CTkToplevel(),
        )
    except Exception as e:
        log_error(message=f"Caught an exception while attempting to create a new stack: {e}")
        raise e


def on_rehearse_button_click(stack: dict[str, Any]) -> None:
    """
    Handler triggered when the rehearse button is clicked.

    Args:
        stack (dict[str, Any]): The stack to rehearse.

    Returns:
        None
    """

    try:
        dispatch(
            event=DESTROY_DASHBOARD_VIEW,
            namespace=GLOBAL,
        )
        dispatch(
            event=GET_REHEARSAL_RUN_SETUP_VIEW,
            namespace=GLOBAL,
            stack=stack,
        )
    except Exception as e:
        log_error(message=f"Caught an exception while attempting to create a new stack: {e}")
        raise e


def on_view_button_click(stack: dict[str, Any]) -> None:
    """
    Handler triggered when the view button is clicked.

    Args:
        stack (dict[str, Any]): The stack to view.

    Returns:
        None
    """

    try:
        dispatch(
            event=GET_VIEW_VIEW,
            namespace=GLOBAL,
            stack=stack,
            toplevel=ctk.CTkToplevel(),
        )
    except Exception as e:
        log_error(message=f"Caught an exception while attempting to create a new stack: {e}")
        raise e
