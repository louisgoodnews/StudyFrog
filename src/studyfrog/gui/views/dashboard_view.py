"""
Author: Louis Goodnews
Date: 2025-12-12
Description: The dashboard view of the application.
"""

import customtkinter as ctk

from tkinter.constants import NSEW, TOP, VERTICAL, W, X, YES
from typing import Any, Final, Optional

from constants.common import GLOBAL
from constants.events import (
    DESTROY_DASHBOARD_VIEW,
    GET_ALL_STACKS_FROM_DB,
    STACK_ADDED,
    STACK_DELETED,
    STACKS_ADDED,
)
from gui.gui import (
    get_bottom_frame,
    get_center_frame,
    get_top_frame,
)
from gui.logic.dashboard_view_logic import (
    on_create_button_click,
    on_delete_button_click,
    on_edit_button_click,
    on_rehearse_button_click,
    on_view_button_click,
)
from utils.common import exists
from utils.dispatcher import dispatch, subscribe, unsubscribe
from utils.gui import (
    clear_bottom_frame,
    clear_center_frame,
    clear_frames,
    clear_top_frame,
    reset_frame_grids,
)
from utils.logging import log_debug, log_error, log_info


# ---------- Exports ---------- #

__all__: Final[list[str]] = ["get_dashboard_view"]


# ---------- Constants ---------- #

_DASHBOARD_ITEM_CONTAINER: Optional[ctk.CTkScrollableFrame] = None

_DASHBOARD_ITEMS: dict[str, ctk.CTkFrame] = {}

_SUBSCRIPTION_IDS: Final[list[str]] = []


# ---------- Helper Functions ---------- #


def _get_dashboard_item_container() -> ctk.CTkScrollableFrame:
    """
    Retrieves the main scrollable container for dashboard items.

    Raises:
        ValueError: If the container has not been initialized yet.

    Returns:
        ctk.CTkScrollableFrame: The scrollable frame instance.
    """

    if not exists(value=_DASHBOARD_ITEM_CONTAINER):
        raise ValueError(
            "The Dashboard Item Container has not yet been initialized."
            "The method '_set_dashboard_item_container' must be executed first."
        )

    return _DASHBOARD_ITEM_CONTAINER


def _register_dashboard_item(frame: ctk.CTkFrame, key: str) -> None:
    """
    Registers a dashboard item.

    Args:
        frame (ctk.CTkFrame): The dashboard item to register.
        key (str): The key under which to register the passed ctk.CTkFrame object.

    Retturns:
        None
    """

    _DASHBOARD_ITEMS[key] = frame


def _set_dashboard_item_container(scrollable_frame: ctk.CTkScrollableFrame) -> None:
    """
    Sets the main scrollable frame for dashboard items.

    Args:
        scrollable_frame (ctk.CTkScrollableFrame): The CTkScrollableFrame instance to be set.

    Returns:
        None
    """

    global _DASHBOARD_ITEM_CONTAINER

    if exists(value=_DASHBOARD_ITEM_CONTAINER):
        return

    _DASHBOARD_ITEM_CONTAINER = scrollable_frame


def _unregister_dashboard_item(key: str) -> None:
    """
    Unregisters a dashboard item.

    Args:
        key (str): The key under which the dashboard item is registered.

    Retturns:
        None
    """

    _DASHBOARD_ITEMS.pop(key, None)


# ---------- Private Functions ---------- #


def _configure_widget_grids() -> None:
    """
    Configures the grid of the widgets of the dashboard view.

    Args:
        None

    Returns:
        None
    """

    _configure_top_frame_grid()
    _configure_center_frame_grid()
    _configure_bottom_frame_grid()


def _configure_bottom_frame_grid() -> None:
    """
    Configures the bottom frame's grid.

    Args:
        None

    Returns:
        None
    """

    get_bottom_frame().grid_columnconfigure(
        index=0,
        weight=1,
    )
    get_bottom_frame().grid_columnconfigure(
        index=1,
        weight=0,
    )
    get_bottom_frame().grid_columnconfigure(
        index=2,
        weight=1,
    )
    get_bottom_frame().grid_rowconfigure(
        index=0,
        weight=1,
    )


def _configure_center_frame_grid() -> None:
    """
    Configures the center frame's grid.

    Args:
        None

    Returns:
        None
    """

    get_center_frame().grid_columnconfigure(
        index=0,
        weight=1,
    )
    get_center_frame().grid_rowconfigure(
        index=0,
        weight=1,
    )


def _configure_top_frame_grid() -> None:
    """
    Configures the top frame's grid.

    Args:
        None

    Returns:
        None
    """

    get_top_frame().grid_columnconfigure(
        index=0,
        weight=0,
    )
    get_top_frame().grid_columnconfigure(
        index=1,
        weight=1,
    )
    get_top_frame().grid_rowconfigure(
        index=0,
        weight=1,
    )


def _create_widgets() -> None:
    """
    Creates the widgets of the dashboard view.

    Args:
        None

    Returns:
        None
    """

    _create_bottom_frame_widgets()
    _create_center_frame_widgets()
    _create_top_frame_widgets()


def _create_bottom_frame_widgets() -> None:
    """
    Creates the bottom frame widgets of the dashboard view.

    Args:
        None

    Returns:
        None
    """

    get_bottom_frame().grid_columnconfigure(
        index=0,
        weight=1,
    )
    get_bottom_frame().grid_rowconfigure(
        index=0,
        weight=1,
    )


def _create_center_frame_widgets() -> None:
    """
    Creates the center frame widgets of the dashboard view.

    Args:
        None

    Returns:
        None
    """

    scrollable_frame: ctk.CTkScrollableFrame = ctk.CTkScrollableFrame(
        master=get_center_frame(),
        orientation=VERTICAL,
    )

    scrollable_frame.grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    _set_dashboard_item_container(scrollable_frame=scrollable_frame)


def _create_dashboard_item_widgets(stack: dict[str, Any]) -> ctk.CTkFrame:
    """
    Creates the dashboard item widgets.

    Args:
        stack (dict[str, Any]): The stack to create the dashboard item widgets for.

    Returns:
        ctk.CTkFrame: The created dashboard item frame.
    """

    frame: ctk.CTkFrame = ctk.CTkFrame(master=_get_dashboard_item_container())

    frame.pack(
        expand=YES,
        fill=X,
        padx=5,
        pady=5,
        side=TOP,
    )

    frame.grid_columnconfigure(
        index=0,
        weight=1,
    )
    frame.grid_columnconfigure(
        index=1,
        weight=0,
    )
    frame.grid_columnconfigure(
        index=2,
        weight=0,
    )
    frame.grid_columnconfigure(
        index=3,
        weight=0,
    )
    frame.grid_columnconfigure(
        index=4,
        weight=0,
    )

    ctk.CTkLabel(
        anchor=W,
        master=frame,
        text=stack["name"],
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=1,
        sticky=NSEW,
    )

    ctk.CTkButton(
        command=lambda: on_delete_button_click(stack=stack),
        master=frame,
        text="Delete",
        width=75,
    ).grid(
        column=1,
        padx=5,
        pady=5,
        row=1,
    )

    ctk.CTkButton(
        command=lambda: on_edit_button_click(stack=stack),
        master=frame,
        text="Edit",
        width=75,
    ).grid(
        column=2,
        padx=5,
        pady=5,
        row=1,
    )

    ctk.CTkButton(
        command=lambda: on_rehearse_button_click(stack=stack),
        master=frame,
        text="Rehearse",
        width=75,
    ).grid(
        column=3,
        padx=5,
        pady=5,
        row=1,
    )

    ctk.CTkButton(
        command=lambda: on_view_button_click(stack=stack),
        master=frame,
        text="View",
        width=75,
    ).grid(
        column=4,
        padx=5,
        pady=5,
        row=1,
    )

    return frame


def _create_top_frame_widgets() -> None:
    """
    Creates the top frame widgets of the dashboard view.

    Args:
        None

    Returns:
        None
    """

    ctk.CTkButton(
        command=on_create_button_click,
        master=get_top_frame(),
        text="Create",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
    )


def _load_stacks() -> None:
    """
    Retrieves the stacks from the database and creates the dashboard item widgets for each stack.

    Args:
        None

    Returns:
        None
    """

    stacks: Optional[list[dict[str, Any]]] = (
        dispatch(
            event=GET_ALL_STACKS_FROM_DB,
            namespace=GLOBAL,
            table_name="stacks",
        )
        .get(
            "get_all_entries",
            {},
        )[0]
        .get(
            "result",
            [{}],
        )
    )

    if not exists(value=stacks):
        return

    for stack in stacks:
        _create_dashboard_item_widgets(stack=stack)


def _on_destroy() -> None:
    """
    Handles the 'DESTROY_DASHBOARD_VIEW' event.

    Args:
        None

    Returns:
        None
    """

    global _DASHBOARD_ITEM_CONTAINER

    _unsubscribe_from_events()

    _DASHBOARD_ITEMS.clear()

    _DASHBOARD_ITEM_CONTAINER = None


def _on_stack_added(stack: dict[str, Any]) -> None:
    """
    Handler for the 'STACK_ADDED' event.

    Args:
        stack (dict[str, Any]): The stack that was added.

    Returns:
        None
    """

    frame: ctk.CTkFrame = _create_dashboard_item_widgets(stack=stack)

    _register_dashboard_item(
        frame=frame,
        key=stack["metadata"]["key"],
    )


def _on_stack_deleted(stack: dict[str, Any]) -> None:
    """
    Handler for the 'STACK_DELETED' event.

    Args:
        stack (dict[str, Any]): The stack that was added.

    Returns:
        None
    """

    _DASHBOARD_ITEMS[stack["metadata"]["key"]].destroy()

    _unregister_dashboard_item(key=stack["metadata"]["key"])


def _on_stacks_added(stacks: list[dict[str, Any]]) -> None:
    """
    Handler for the 'STACKS_ADDED' event.

    Args:
        stacks (list[dict[str, Any]]): The stacks that were added.

    Returns:
        None
    """

    for stack in stacks:
        frame: ctk.CTkFrame = _create_dashboard_item_widgets(stack=stack)

        _register_dashboard_item(
            frame=frame,
            key=stack["metadata"]["key"],
        )


def _subscribe_to_events() -> None:
    """
    Subscribes to events for the dashboard view.

    Args:
        None

    Returns:
        None
    """

    subscriptions: list[dict[str, Any]] = [
        {
            "event": DESTROY_DASHBOARD_VIEW,
            "function": _on_destroy,
            "namespace": GLOBAL,
            "persistent": False,
            "priority": 100,
        },
        {
            "event": STACK_ADDED,
            "function": _on_stack_added,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": STACKS_ADDED,
            "function": _on_stacks_added,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": STACK_DELETED,
            "function": _on_stack_deleted,
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

    log_info(message="Subscribed to all events for the dashboard view.")


def _unsubscribe_from_events() -> None:
    """
    Unsubscribes from events for the dashboard view.

    Args:
        None

    Returns:
        None
    """

    for uuid in _SUBSCRIPTION_IDS:
        unsubscribe(uuid=uuid)

    log_info(message="Unsubscribed from all events for the dashboard view.")

    _SUBSCRIPTION_IDS.clear()


# ---------- Public Functions ---------- #


def get_dashboard_view() -> None:
    """
    Gets the dashboard view of the application.

    Args:
        None

    Returns:
        None
    """

    try:
        clear_frames()
        reset_frame_grids()

        _configure_widget_grids()
        _create_widgets()
        _subscribe_to_events()
        _load_stacks()
    except Exception as e:
        log_error(message=f"Caught an exception while attempting to get the dashboard view: {e}")
        raise e
