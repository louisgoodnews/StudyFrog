"""
Author: Louis Goodnews
Date: 2025-11-16
"""

from typing import Final, Literal

from gui.factory import get_toplevel
from gui.gui import get_root
from gui.views.create_view import get_create_view
from gui.views.edit_view import get_edit_view
from utils.utils import log_exception


# ---------- Constants ---------- #

NAME: Final[Literal["gui.views.logic.dashboard_view_logic"]] = (
    "gui.views.logic.dashboard_view_logic"
)


# ---------- Functions ---------- #


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
        get_create_view(master=get_toplevel(master=get_root()))
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to create view",
            name=NAME,
        )
        raise e


def on_delete_button_click() -> None:
    """
    Handles the delete button click event.

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
            message="Failed to delete view",
            name=NAME,
        )
        raise e


def on_edit_button_click() -> None:
    """
    Handles the edit button click event.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    try:
        get_edit_view(master=get_toplevel(master=get_root()))
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to edit view",
            name=NAME,
        )
        raise e


def on_view_button_click() -> None:
    """
    Handles the view button click event.

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
            message="Failed to view view",
            name=NAME,
        )
        raise e


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
