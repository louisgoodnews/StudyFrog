"""
Author: Louis Goodnews
Date: 2026-01-08
Description: The edit view of the application.
"""

import customtkinter as ctk

from tkinter.constants import NSEW, W
from typing import Any, Final, Optional

from constants.common import GLOBAL
from constants.events import DESTROY_EDIT_VIEW
from constants.gui import WINDOW_GEOMETRY, WINDOW_TITLE
from gui.logic.edit_view_logic import (
    on_cancel_button_click,
    on_delete_button_click,
    on_save_button_click,
)
from utils.dispatcher import subscribe, unsubscribe
from utils.common import exists
from utils.logging import log_error


# ---------- Exports ---------- #

__all__: Final[list[str]] = ["get_edit_view"]


# ---------- Constants ---------- #

_BOTTOM_FRAME: Optional[ctk.CTkFrame] = None

_CENTER_FRAME: Optional[ctk.CTkFrame] = None

_MASTER: Optional[ctk.CTkScrollableFrame] = None

_OBJECT: Optional[dict[str, Any]] = None

_SUBSCRIPTION_IDS: Final[list[str]] = []

_TABVIEW: Optional[ctk.CTkTabview] = None

_TOP_FRAME: Optional[ctk.CTkFrame] = None


# ---------- Helper Functions ---------- #


def _append_subscription(uuid: str) -> None:
    """
    Appends a passed subscription UUID to the list of subscription IDs.

    Args:
        uuid (str): The subscription UUID to append.

    Returns:
        None
    """

    _get_subscription_ids().append(uuid)


def _clear_subscription_ids() -> None:
    """
    Clears the list of subscription IDs for the edit view.

    Args:
        None

    Returns:
        None
    """

    _SUBSCRIPTION_IDS.clear()


def _get_bottom_frame() -> ctk.CTkFrame:
    """
    Returns the 'bottom' frame widget for the edit view.

    Args:
        None

    Returns:
        ctk.CTkFrame: The 'bottom' frame widget for the edit view.

    Raises:
        ValueError: If the 'bottom' frame has not been initialized yet. Call '_set_bottom_frame' first.
    """

    if not exists(value=_BOTTOM_FRAME):
        raise ValueError(
            "'bottom' frame has not been initialized yet. Call '_set_bottom_frame' first."
        )

    return _BOTTOM_FRAME


def _get_center_frame() -> ctk.CTkFrame:
    """
    Returns the 'center' frame widget for the edit view.

    Args:
        None

    Returns:
        ctk.CTkFrame: The 'center' frame widget for the edit view.

    Raises:
        ValueError: If the 'center' frame has not been initialized yet. Call '_set_center_frame' first.
    """

    if not exists(value=_CENTER_FRAME):
        raise ValueError(
            "'center' frame has not been initialized yet. Call '_set_center_frame' first."
        )

    return _CENTER_FRAME


def _get_master() -> ctk.CTkToplevel:
    """
    Returns the master widget of the edit view.

    Args:
        None

    Returns:
        ctk.CTkToplevel: The master widget of the edit view.

    Raises:
        ValueError: If the master widget has not been initialized yet.
            Call '_set_master' first.
    """

    if not exists(value=_MASTER):
        raise ValueError("Master has not been initialized yet. Call '_set_master' first.")

    return _MASTER


def _get_object() -> dict[str, Any]:
    """
    Returns the object that is being edited in the edit view.

    Args:
        None

    Returns:
        dict[str, Any]: The object that is being edited in the edit view.

    Raises:
        ValueError: If the object has not been initialized yet. Call '_set_object' first.
    """

    if not exists(value=_OBJECT):
        raise ValueError("Object has not been initialized yet. Call '_set_object' first.")

    return _OBJECT


def _get_subscription_ids() -> list[str]:
    """
    Returns the subscription IDs for the edit view.

    Args:
        None

    Returns:
        list[str]: The subscription IDs for the edit view.
    """

    return _SUBSCRIPTION_IDS


def _get_tabview() -> ctk.CTkTabview:
    """
    Returns the tabview widget of the edit view.

    Args:
        None

    Returns:
        ctk.CTkTabview: The tabview widget of the edit view.

    Raises:
        ValueError: If the tabview widget has not been initialized yet.
            Call '_set_tabview' first.
    """

    if not exists(value=_TABVIEW):
        raise ValueError("tabview has not been initialized yet. Call '_set_tabview' first.")

    return _TABVIEW


def _get_top_frame() -> ctk.CTkFrame:
    """
    Returns the 'top' frame widget for the edit view.

    Args:
        None

    Returns:
        ctk.CTkFrame: The 'top' frame widget for the edit view.

    Raises:
        ValueError: If the 'top' frame has not been initialized yet. Call '_set_top_frame' first.
    """

    if not exists(value=_TOP_FRAME):
        raise ValueError("'top' frame has not been initialized yet. Call '_set_top_frame' first.")

    return _TOP_FRAME


def _reset_constants() -> None:
    """
    Resets the global constants used in the edit view module.

    Args:
        None

    Returns:
        None
    """

    global _BOTTOM_FRAME, _CENTER_FRAME, _MASTER, _OBJECT, _TABVIEW, _TOP_FRAME

    _BOTTOM_FRAME = None
    _CENTER_FRAME = None
    _MASTER = None
    _OBJECT = None
    _TABVIEW = None
    _TOP_FRAME = None


def _set_bottom_frame(frame: ctk.CTkFrame) -> None:
    """
    Sets the 'bottom' frame widget for the edit view.

    Args:
        frame (ctk.CTkFrame): The 'bottom' frame widget for the edit view.

    Returns:
        None
    """

    global _BOTTOM_FRAME

    if exists(value=_BOTTOM_FRAME):
        return

    _BOTTOM_FRAME = frame


def _set_center_frame(frame: ctk.CTkFrame) -> None:
    """
    Sets the 'center' frame widget for the edit view.

    Args:
        frame (ctk.CTkFrame): The 'center' frame widget for the edit view.

    Returns:
        None
    """

    global _CENTER_FRAME

    if exists(value=_CENTER_FRAME):
        return

    _CENTER_FRAME = frame


def _set_master(toplevel: ctk.CTkToplevel) -> None:
    """
    Sets the master widget for the edit view.

    Args:
        toplevel (ctk.CTkToplevel): The master widget for the edit view.

    Returns:
        None
    """

    global _MASTER

    if exists(value=_MASTER):
        return

    _MASTER = toplevel


def _set_object(dictionary: dict[str, Any]) -> None:
    """
    Sets the object to be edited.

    Args:
        dictionary (dict[str, Any]): The object to be edited.

    Returns:
        None
    """

    global _OBJECT

    if exists(value=_OBJECT):
        return

    _OBJECT = dictionary


def _set_tabview(tabview: ctk.CTkTabview) -> None:
    """
    Sets the tabview widget for the edit view.

    Args:
        tabview (ctk.CTkTabview): The tabview widget for the edit view.

    Returns:
        None
    """

    global _TABVIEW

    if exists(value=_TABVIEW):
        return

    _TABVIEW = tabview


def _set_top_frame(frame: ctk.CTkFrame) -> None:
    """
    Sets the 'top' frame widget for the edit view.

    Args:
        frame (ctk.CTkFrame): The 'top' frame widget for the edit view.

    Returns:
        None
    """

    global _TOP_FRAME

    if exists(value=_TOP_FRAME):
        return

    _TOP_FRAME = frame


# ---------- Private Functions ---------- #


def _configure_bottom_frame_grid() -> None:
    """
    Configures the grid of the 'bottom frame' of the edit view.

    Args:
        None

    Returns:
        None
    """

    _get_bottom_frame().grid_columnconfigure(
        index=0,
        weight=1,
    )
    _get_bottom_frame().grid_rowconfigure(
        index=0,
        weight=1,
    )


def _configure_center_frame_grid() -> None:
    """
    Configures the grid of the 'center frame' of the edit view.

    Args:
        None

    Returns:
        None
    """

    _get_center_frame().grid_columnconfigure(
        index=0,
        weight=1,
    )
    _get_center_frame().grid_columnconfigure(
        index=1,
        weight=0,
    )
    _get_center_frame().grid_columnconfigure(
        index=2,
        weight=0,
    )
    _get_center_frame().grid_rowconfigure(
        index=0,
        weight=1,
    )


def _configure_top_frame_grid() -> None:
    """
    Configures the grid of the 'top frame' of the edit view.

    Args:
        None

    Returns:
        None
    """

    _get_top_frame().grid_columnconfigure(
        index=0,
        weight=1,
    )
    _get_top_frame().grid_columnconfigure(
        index=1,
        weight=0,
    )
    _get_top_frame().grid_rowconfigure(
        index=0,
        weight=1,
    )


def _configure_grid() -> None:
    """
    Configures the grid of the edit view.

    Args:
        None

    Returns:
        None
    """

    _get_master().grid_columnconfigure(
        index=0,
        weight=1,
    )
    _get_master().grid_rowconfigure(
        index=0,
        weight=0,
    )
    _get_master().grid_rowconfigure(
        index=1,
        weight=1,
    )
    _get_master().grid_rowconfigure(
        index=2,
        weight=0,
    )

    _configure_top_frame_grid()
    _configure_center_frame_grid()
    _configure_bottom_frame_grid()


def _create_bottom_frame_widgets() -> None:
    """
    Creates the 'bottom frame' widgets of the edit view.

    Args:
        None

    Returns:
        None
    """

    ctk.CTkButton(
        command=on_cancel_button_click,
        master=_get_bottom_frame(),
        text="Cancel",
    ).grid(
        column=1,
        padx=5,
        pady=5,
        row=0,
    )

    ctk.CTkButton(
        command=on_save_button_click,
        master=_get_bottom_frame(),
        text="Save",
    ).grid(
        column=2,
        padx=5,
        pady=5,
        row=0,
    )


def _create_center_frame_widgets() -> None:
    """
    Creates the 'center frame' widgets of the edit view.

    Args:
        None

    Returns:
        None
    """

    tabview: ctk.CTkTabview = ctk.CTkTabview(master=_get_center_frame())

    tabview.grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    _set_tabview(tabview=tabview)


def _create_top_frame_widgets() -> None:
    """
    Creates the 'top frame' widgets of the edit view.

    Args:
        None

    Returns:
        None
    """

    ctk.CTkLabel(
        anchor=W,
        font=(
            "Helvetica",
            24,
        ),
        master=_get_top_frame(),
        text=f"Edit {_get_object()['metadata']['type'].title()} with ID ({_get_object()['metadata']['id']})",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    ctk.CTkButton(
        command=lambda: on_delete_button_click(obj=_get_object()),
        master=_get_top_frame(),
        text="Delete",
    ).grid(
        column=1,
        padx=5,
        pady=5,
        row=0,
    )


def _create_widgets() -> None:
    """
    Creates the widgets of the edit view.

    Args:
        None

    Returns:
        None
    """

    bottom_frame: ctk.CTkFrame = ctk.CTkFrame(
        height=25,
        master=_get_master(),
    )

    bottom_frame.grid(
        column=0,
        padx=5,
        pady=5,
        row=2,
        sticky=NSEW,
    )

    _set_bottom_frame(frame=bottom_frame)

    center_frame: ctk.CTkFrame = ctk.CTkFrame(master=_get_master())

    center_frame.grid(
        column=0,
        padx=5,
        pady=5,
        row=1,
        sticky=NSEW,
    )

    _set_center_frame(frame=center_frame)

    top_frame: ctk.CTkFrame = ctk.CTkFrame(
        height=50,
        master=_get_master(),
    )

    top_frame.grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    _set_top_frame(frame=top_frame)

    _create_top_frame_widgets()
    _create_center_frame_widgets()
    _create_bottom_frame_widgets()


def _on_destroy() -> None:
    """
    Handles the 'DESTROY_EDIT_VIEW' event.

    Args:
        None

    Returns:
        None
    """

    _unsubscribe_from_events()

    _get_master().destroy()

    _reset_constants()


def _subscribe_to_events() -> None:
    """
    Subscribes to events for the edit view.

    The edit view currently only subscribes to the 'DESTROY_EDIT_VIEW' event.

    Args:
        None

    Returns:
        None
    """

    subscriptions: list[dict[str, Any]] = [
        {
            "event": DESTROY_EDIT_VIEW,
            "function": _on_destroy,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        }
    ]

    for subscription in subscriptions:
        _append_subscription(
            uuid=subscribe(
                event=subscription["event"],
                function=subscription["function"],
                namespace=subscription["namespace"],
                persistent=subscription["persistent"],
                priority=subscription["priority"],
            )
        )


def _unsubscribe_from_events() -> None:
    """
    Unsubscribes from all currently active event subscriptions.

    Iterates through the subscription IDs returned by `_get_subscription_ids()`
    and calls `unsubscribe(uuid=uuid)` for each ID.

    Args:
        None

    Returns:
        None
    """

    for uuid in _get_subscription_ids():
        unsubscribe(uuid=uuid)

    _clear_subscription_ids()


# ---------- Public Functions ---------- #


def get_edit_view(
    obj: dict[str, Any],
    toplevel: ctk.CTkToplevel,
) -> ctk.CTkFrame:
    """
    Gets the edit view of the application.

    Args:
        obj (dict[str, Any]): The object to edit.
        toplevel (ctk.CTkToplevel): The toplevel window of the application.

    Returns:
        ctk.CTkFrame: The edit view of the application.

    Raises:
        Exception: If any exception is caught while attempting to execute the 'get_edit_view' function.
    """

    try:
        toplevel.geometry(geometry_string=WINDOW_GEOMETRY)
        toplevel.title(string=WINDOW_TITLE)

        _set_master(toplevel=toplevel)
        _set_object(dictionary=obj)

        _create_widgets()
        _configure_grid()

        _subscribe_to_events()
    except Exception as e:
        log_error(
            message=f"Caught an exception while attepting to execute the 'get_edit_view' function: {e}"
        )

        raise e
