"""
Author: Louis Goodnews
Date: 2026-01-05
Description: The delete confirmation view of the application.
"""

import customtkinter as ctk

from tkinter.constants import CENTER, NSEW, W
from typing import Any, Final, Optional

from constants.common import GLOBAL
from constants.events import DESTROY_DELETE_CONFIRMATION_VIEW
from constants.gui import TOPLEVEL_GEOMETRY, WINDOW_TITLE
from gui.logic.delete_confirmation_view_logic import on_cancel_button_click, on_okay_button_click
from utils.common import exists
from utils.dispatcher import subscribe, unsubscribe
from utils.logging import log_error, log_info


# ---------- Exports ---------- #

__all__: Final[list[str]] = ["get_delete_confirmation_view"]


# ---------- Constants ---------- #

_BOTTOM_FRAME: Optional[ctk.CTkFrame] = None

_CENTER_FRAME: Optional[ctk.CTkFrame] = None

_MASTER: Optional[ctk.CTkToplevel] = None

_OBJECT: Optional[dict[str, Any]] = None

_SUBSCRIPTION_IDS: Final[list[str]] = []

_TOP_FRAME: Optional[ctk.CTkFrame] = None


# ---------- Helper Functions ---------- #


def _get_bottom_frame() -> ctk.CTkFrame:
    """
    Returns the delete confirmation view's 'bottom frame' ctk.Frame widget.

    Args:
        None

    Returns:
        ctk.CTkFrame: The delete confirmation view's 'bottom frame' ctk.Frame widget.

    Raises:
        ValueError: If the 'bottom frame' ctk.Frame widget does not exist.
    """

    if not exists(value=_BOTTOM_FRAME):
        raise ValueError(
            "'bottom' frame does not exist. Call the '_set_bottom_frame' method first."
        )

    return _BOTTOM_FRAME


def _get_center_frame() -> ctk.CTkFrame:
    """
    Returns the delete confirmation view's 'center frame' ctk.Frame widget.

    Args:
        None

    Returns:
        ctk.CTkFrame: The delete confirmation view's 'center frame' ctk.Frame widget.

    Raises:
        ValueError: If the 'center frame' ctk.Frame widget does not exist.
    """

    if not exists(value=_CENTER_FRAME):
        raise ValueError(
            "'center' frame does not exist. Call the '_set_center_frame' method first."
        )

    return _CENTER_FRAME


def _get_master() -> ctk.CTkToplevel:
    """
    Returns the delete confirmation view's master ctk.Toplevel widget.

    Args:
        None

    Returns:
        ctk.CTkToplevel: The delete confirmation view's master ctk.Toplevel widget.

    Raises:
        ValueError: If the master ctk.Toplevel widget does not exist.
    """

    if not exists(value=_MASTER):
        raise ValueError("master does not exist. Call the '_set_master' method first.")

    return _MASTER


def _get_object() -> Optional[dict[str, Any]]:
    """
    Returns the object to be deleted.

    Args:
        None

    Returns:
        Optional[dict[str, Any]]: The object to be deleted.

    Raises:
        ValueError: If the object does not exist.
    """

    if not exists(value=_OBJECT):
        raise ValueError("object does not exist. Call the '_set_object' method first.")

    return _OBJECT


def _get_subscription_ids() -> list[str]:
    """
    Returns the subscription IDs for subscriptions in the delete confirmation view.

    Args:
        None

    Returns:
        list[str]: The subscription IDs for subscriptions in the delete confirmation view.
    """

    return list(_SUBSCRIPTION_IDS)


def _get_top_frame() -> ctk.CTkFrame:
    """
    Returns the delete confirmation view's 'top frame' ctk.Frame widget.

    Args:
        None

    Returns:
        ctk.CTkFrame: The delete confirmation view's 'bottom frame' ctk.Frame widget.

    Raises:
        ValueError: If the 'top frame' ctk.Frame widget does not exist.
    """

    if not exists(value=_TOP_FRAME):
        raise ValueError("'top' frame does not exist. Call the '_set_top_frame' method first.")

    return _TOP_FRAME


def _set_bottom_frame(frame: ctk.CTkFrame) -> None:
    """
    Sets the delete confirmation view's 'bottom frame' ctk.Frame widget.

    Args:
        toplevel (ctk.CTkToplevel): The delete confirmation view's 'bottom frame' ctk.Frame widget.

    Returns:
        None
    """

    global _BOTTOM_FRAME

    if exists(value=_BOTTOM_FRAME):
        return

    _BOTTOM_FRAME = frame


def _set_center_frame(frame: ctk.CTkFrame) -> None:
    """
    Sets the delete confirmation view's 'center frame' ctk.Frame widget.

    Args:
        toplevel (ctk.CTkToplevel): The delete confirmation view's 'center frame' ctk.Frame widget.

    Returns:
        None
    """

    global _CENTER_FRAME

    if exists(value=_CENTER_FRAME):
        return

    _CENTER_FRAME = frame


def _set_master(toplevel: ctk.CTkToplevel) -> None:
    """
    Sets the delete confirmation view's 'master' ctk.Toplevel widget.

    Args:
        toplevel (ctk.CTkToplevel): The delete confirmation view's 'master' ctk.Toplevel widget.

    Returns:
        None
    """

    global _MASTER

    if exists(value=_MASTER):
        return

    _MASTER = toplevel


def _set_object(obj: Any) -> None:
    """
    Sets the object to be deleted.

    Args:
        obj (Any): The object to be deleted.

    Returns:
        None
    """

    global _OBJECT

    if exists(value=_OBJECT):
        return

    _OBJECT = obj


def _set_top_frame(frame: ctk.CTkFrame) -> None:
    """
    Sets the delete confirmation view's 'top frame' ctk.Frame widget.

    Args:
        toplevel (ctk.CTkToplevel): The delete confirmation view's 'top frame' ctk.Frame widget.

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
    Configures the grid of the delete confirmation view's 'bottom frame' ctk.Frame widget.

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
    _get_bottom_frame().grid_rowconfigure(
        index=1,
        weight=0,
    )
    _get_bottom_frame().grid_rowconfigure(
        index=2,
        weight=0,
    )


def _configure_center_frame_grid() -> None:
    """
    Configures the grid of the delete confirmation view's 'center frame' ctk.Frame widget.

    Args:
        None

    Returns:
        None
    """

    _get_center_frame().grid_columnconfigure(
        index=0,
        weight=1,
    )
    _get_center_frame().grid_rowconfigure(
        index=0,
        weight=1,
    )


def _configure_top_frame_grid() -> None:
    """
    Configures the grid of the delete confirmation view's 'top frame' ctk.Frame widget.

    Args:
        None

    Returns:
        None
    """

    _get_top_frame().grid_columnconfigure(
        index=0,
        weight=1,
    )
    _get_top_frame().grid_rowconfigure(
        index=0,
        weight=1,
    )


def _configure_grid() -> None:
    """
    Configures the grid of the delete confirmation view.

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

    _configure_bottom_frame_grid()
    _configure_center_frame_grid()
    _configure_top_frame_grid()


def _create_bottom_frame_widgets() -> None:
    """
    Creates widgets for the delete confirmation view's 'bottom frame' ctk.Frame widget.

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
        command=lambda: on_okay_button_click(obj=_get_object()),
        master=_get_bottom_frame(),
        text="Okay",
    ).grid(
        column=2,
        padx=5,
        pady=5,
        row=0,
    )


def _create_center_frame_widgets() -> None:
    """
    Creates widgets for the delete confirmation view's 'center frame' ctk.Frame widget.

    Args:
        None

    Returns:
        None
    """

    ctk.CTkLabel(
        anchor=CENTER,
        font=(
            "Helvetica",
            24,
        ),
        master=_get_center_frame(),
        text=f"Do you really want to delete this {_get_object()['metadata']['type'].title()} with ID {_get_object()['metadata']['id']}?",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )


def _create_top_frame_widgets() -> None:
    """
    Creates widgets for the delete confirmation view's 'top frame' ctk.Frame widget.

    Args:
        None

    Returns:
        None
    """

    ctk.CTkLabel(
        anchor=W,
        font=(
            "Helvetica",
            16,
            "bold",
        ),
        master=_get_top_frame(),
        text="Confirm deletion",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )


def _create_widgets() -> None:
    """
    Creates widgets for the delete confirmation view.

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

    _create_bottom_frame_widgets()
    _create_center_frame_widgets()
    _create_top_frame_widgets()


def _on_destroy() -> None:
    """
    Handles the 'DESTROY_DELETE_CONFIRMATION_VIEW'event.

    Args:
        None

    Returns:
        None
    """

    global _BOTTOM_FRAME, _CENTER_FRAME, _MASTER, _OBJECT, _TOP_FRAME

    _MASTER.destroy()

    _unsubscribe_from_events()

    _BOTTOM_FRAME = None
    _CENTER_FRAME = None
    _MASTER = None
    _OBJECT = None
    _TOP_FRAME = None


def _subscribe_to_events() -> None:
    """
    Subscribes to events in the delete confirmation view.

    Args:
        None

    Returns:
        None
    """

    subscriptions: list[dict[str, Any]] = [
        {
            "event": DESTROY_DELETE_CONFIRMATION_VIEW,
            "function": _on_destroy,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        }
    ]

    for subscription in subscriptions:
        _get_subscription_ids().append(
            subscribe(
                event=subscription["event"],
                function=subscription["function"],
                namespace=subscription["namespace"],
                persistent=subscription["persistent"],
                priority=subscription["priority"],
            )
        )

    log_info(message="Subscribed all events for the delete confirmation view.")


def _unsubscribe_from_events() -> None:
    """
    Unsubscribes from events in the delete confirmation view.

    Args:
        None

    Returns:
        None
    """

    for uuid in _get_subscription_ids():
        unsubscribe(uuid=uuid)

    log_info(message="Unsubscribed from all events for the delete confirmation view.")

    _get_subscription_ids().clear()


# ---------- Public Functions ---------- #


def get_delete_confirmation_view(
    toplevel: ctk.CTkToplevel,
    obj: Optional[dict[str, Any]] = None,
) -> None:
    """
    Gets the delete confirmation view.

    Args:
        toplevel (ctk.CTkToplevel): The toplevel window.
        obj (Optional[dict[str, Any]]): The object to delete.

    Returns:
        None

    Raises:
        Exception: If any error occurs.
    """

    try:
        toplevel.geometry(geometry_string=TOPLEVEL_GEOMETRY)

        toplevel.title(string=WINDOW_TITLE)

        toplevel.protocol(
            func=_on_destroy,
            name="WM_DELETE_WINDOW",
        )

        _set_master(toplevel=toplevel)
        _set_object(obj=obj)
        _create_widgets()
        _configure_grid()
        _subscribe_to_events()
    except Exception as e:
        log_error(
            message=f"Failed to get delete confirmation view: {e}",
        )

        raise e
