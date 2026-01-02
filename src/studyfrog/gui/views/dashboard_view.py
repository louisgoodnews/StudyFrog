"""
Author: Louis Goodnews
Date: 2025-12-12
Description: The dashboard view of the application.
"""

import customtkinter as ctk

from tkinter.constants import NSEW, TOP, VERTICAL, W, X, YES
from typing import Any, Final, Optional

from constants.events import (
    DESTROY_DASHBOARD_VIEW,
    GET_ALL_STACKS_FROM_DB,
    STACK_ADDED,
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
from utils.dispatcher import dispatch, subscribe, unsubscribe
from utils.gui import (
    clear_bottom_frame,
    clear_center_frame,
    clear_top_frame,
    count_widget_children,
)
from utils.logging import log_error, log_info


# ---------- Exports ---------- #

__all__: Final[list[str]] = ["get_dashboard_view"]


# ---------- Constants ---------- #

DASHBOARD_ITEM_CONTAINER: Optional[ctk.CTkScrollableFrame] = None

SUBSCRIPTION_IDS: Final[list[str]] = []


# ---------- Helper Functions ---------- #


def _get_dashboard_item_container_children_count() -> int:
    """
    Retrieves the number of children in the dashboard item container.

    Args:
        None

    Returns:
        int: The number of children in the dashboard item container.
    """

    return count_widget_children(widget=_get_dashboard_item_container())


# ---------- Private Functions ---------- #


def _clear_widgets() -> None:
    """
    Clears all widgets from the dashboard view.

    Args:
        None

    Returns:
        None
    """

    clear_bottom_frame()
    clear_center_frame()
    clear_top_frame()


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

    pass


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

    pass


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


def _create_dashboard_item_widgets(stack: dict[str, Any]) -> None:
    """
    Creates the dashboard item widgets.

    Args:
        stack (dict[str, Any]): The stack to create the dashboard item widgets for.

    Returns:
        None
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
        column=1,
        padx=5,
        pady=5,
        row=0,
    )


def _get_dashboard_item_container() -> ctk.CTkScrollableFrame:
    """
    Retrieves the main scrollable container for dashboard items.

    Raises:
        ValueError: If the container has not been initialized yet.

    Returns:
        ctk.CTkScrollableFrame: The scrollable frame instance.
    """

    if DASHBOARD_ITEM_CONTAINER is None:
        raise ValueError(
            "The Dashboard Item Container has not yet been initialized."
            "The method '_set_dashboard_item_container' must be executed first."
        )

    return DASHBOARD_ITEM_CONTAINER


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
            namespace="GLOBAL",
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

    if not stacks:
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

    global DASHBOARD_ITEM_CONTAINER

    _clear_widgets()
    _unsubscribe_from_events()

    DASHBOARD_ITEM_CONTAINER = None


def _on_stack_added(stack: dict[str, Any]) -> None:
    """
    Handler for the 'STACK_ADDED' event.

    Args:
        stack (dict[str, Any]): The stack that was added.

    Returns:
        None
    """

    _create_dashboard_item_widgets(stack=stack)


def _on_stacks_added(stacks: list[dict[str, Any]]) -> None:
    """
    Handler for the 'STACKS_ADDED' event.

    Args:
        stacks (list[dict[str, Any]]): The stacks that were added.

    Returns:
        None
    """

    for stack in stacks:
        _create_dashboard_item_widgets(stack=stack)


def _set_dashboard_item_container(scrollable_frame: ctk.CTkScrollableFrame) -> None:
    """
    Sets the main scrollable frame for dashboard items.

    Args:
        scrollable_frame (ctk.CTkScrollableFrame): The CTkScrollableFrame instance to be set.

    Returns:
        None
    """

    global DASHBOARD_ITEM_CONTAINER

    DASHBOARD_ITEM_CONTAINER = scrollable_frame


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
            "namespace": "GLOBAL",
            "persistent": False,
            "priority": 100,
        },
        {
            "event": STACK_ADDED,
            "function": _on_stack_added,
            "namespace": "GLOBAL",
            "persistent": True,
            "priority": 100,
        },
        {
            "event": STACKS_ADDED,
            "function": _on_stacks_added,
            "namespace": "GLOBAL",
            "persistent": True,
            "priority": 100,
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

    log_info(message="Subscribed to all events for the dashboard view.")


def _unsubscribe_from_events() -> None:
    """
    Unsubscribes from events for the dashboard view.

    Args:
        None

    Returns:
        None
    """

    for uuid in SUBSCRIPTION_IDS:
        unsubscribe(uuid=uuid)

    log_info(message="Unsubscribed from all events for the dashboard view.")

    SUBSCRIPTION_IDS.clear()


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
        _clear_widgets()
        _configure_widget_grids()
        _create_widgets()
        _subscribe_to_events()
        _load_stacks()
    except Exception as e:
        log_error(message=f"Caught an exception while attempting to get the dashboard view: {e}")
        raise e
