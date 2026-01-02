"""
Author: Louis Goodnews
Date: 2025-12-12
Description: The create view of the application.
"""

import customtkinter as ctk

from tkinter.constants import NSEW, W
from typing import Any, Final, Optional

from constants.common import GLOBAL
from constants.events import (
    CLEAR_CREATE_FORM,
    DESTROY_CREATE_VIEW,
    GET_ALL_DIFFICULTIES_FROM_DB,
    GET_ALL_PRIORITIES_FROM_DB,
    GET_ALL_STACKS_FROM_DB,
    GET_CREATE_FORM,
    GET_STACK_CREATE_FORM,
    STACK_ADDED,
)
from constants.gui import READONLY, TOPLEVEL_GEOMETRY, WINDOW_TITLE
from gui.logic.create_view_logic import (
    on_create_button_click,
    on_cancel_button_click,
    on_type_combobox_select,
)
from models.models import ModelDict
from utils.dispatcher import dispatch, subscribe, unsubscribe
from utils.logging import log_error, log_info


# ---------- Exports ---------- #

__all__: Final[list[str]] = ["get_create_view"]


# ---------- Constants ---------- #

BOTTOM_FRAME: Optional[ctk.CTkFrame] = None

CENTER_FRAME: Optional[ctk.CTkFrame] = None

CREATE_VIEW_FORM_CONTAINER: Optional[ctk.CTkScrollableFrame] = None

FORM: Final[dict[str, Any]] = {}

MASTER: Optional[ctk.CTkToplevel] = None

STACKS: Final[list[str]] = [""]

SUBSCRIPTION_IDS: Final[list[str]] = []

TOP_FRAME: Optional[ctk.CTkFrame] = None


# ---------- Helper Functions ---------- #


# ---------- Private Functions ---------- #


def _configure_grid() -> None:
    """
    Configures the grid of the create view.

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


def _configure_bottom_frame_grid() -> None:
    """
    Configures the grid of the bottom frame widget.

    Args:
        None

    Returns:
        None
    """

    _get_bottom_frame().grid_columnconfigure(
        index=0,
        weight=0,
    )
    _get_bottom_frame().grid_columnconfigure(
        index=1,
        weight=1,
    )
    _get_bottom_frame().grid_columnconfigure(
        index=2,
        weight=0,
    )
    _get_bottom_frame().grid_columnconfigure(
        index=3,
        weight=0,
    )


def _configure_center_frame_grid() -> None:
    """
    Configures the grid of the center frame widget.

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
    Configures the grid of the top frame widget.

    Args:
        None

    Returns:
        None
    """

    _get_top_frame().grid_columnconfigure(
        index=0,
        weight=0,
    )
    _get_top_frame().grid_columnconfigure(
        index=1,
        weight=1,
    )
    _get_top_frame().grid_rowconfigure(
        index=0,
        weight=0,
    )


def _create_widgets() -> None:
    """
    Creates the widgets of the create view.

    Args:
        None

    Returns:
        None
    """

    bottom_frame: ctk.CTkFrame = ctk.CTkFrame(
        height=50,
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

    _create_bottom_frame_widgets()

    center_frame: ctk.CTkFrame = ctk.CTkFrame(
        height=50,
        master=_get_master(),
    )

    center_frame.grid(
        column=0,
        padx=5,
        pady=5,
        row=1,
        sticky=NSEW,
    )

    _set_center_frame(frame=center_frame)

    _create_center_frame_widgets()

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


def _create_bottom_frame_widgets() -> None:
    """
    Creates the bottom frame widgets.

    Args:
        None

    Returns:
        None
    """

    FORM["create_another"] = {
        "is_required": False,
        "variable": ctk.BooleanVar(),
    }

    ctk.CTkCheckBox(
        master=_get_bottom_frame(),
        text="Create another item",
        variable=FORM["create_another"]["variable"],
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
    )

    ctk.CTkButton(
        command=on_cancel_button_click,
        master=_get_bottom_frame(),
        text="Cancel",
    ).grid(
        column=2,
        padx=5,
        pady=5,
        row=0,
    )

    ctk.CTkButton(
        command=on_create_button_click,
        master=_get_bottom_frame(),
        text="Create",
    ).grid(
        column=3,
        padx=5,
        pady=5,
        row=0,
    )


def _create_center_frame_widgets() -> None:
    """
    Creates the center frame widgets.

    Args:
        None

    Returns:
        None
    """

    scrollable_frame: ctk.CTkScrollableFrame = ctk.CTkScrollableFrame(master=_get_center_frame())

    scrollable_frame.grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    _set_create_view_form_container(scrollable_frame=scrollable_frame)


def _create_top_frame_widgets() -> None:
    """
    Creates the top frame widgets.

    Args:
        None

    Returns:
        None
    """

    ctk.CTkLabel(
        anchor=W,
        font=(
            "Helvetica",
            20,
            "bold",
        ),
        master=_get_top_frame(),
        text="Create item",
    ).grid(
        column=0,
        columnspan=2,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    ctk.CTkLabel(
        anchor=W,
        font=(
            "Helvetica",
            16,
            "normal",
        ),
        master=_get_top_frame(),
        text="Fields marked with * are required.",
    ).grid(
        column=0,
        columnspan=2,
        padx=5,
        pady=5,
        row=1,
        sticky=NSEW,
    )

    ctk.CTkLabel(
        anchor=W,
        font=(
            "Helvetica",
            12,
            "bold",
        ),
        master=_get_top_frame(),
        text="Stack*: ",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=2,
        sticky=NSEW,
    )

    STACKS.extend(
        [
            stack.get(
                "name",
                None,
            )
            for stack in (
                dispatch(
                    event=GET_ALL_STACKS_FROM_DB,
                    namespace=GLOBAL,
                    table_name="stacks",
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
    )

    FORM["stack"] = {
        "is_required": True,
        "variable": ctk.StringVar(),
    }

    stack_combobox: ctk.CTkComboBox = ctk.CTkComboBox(
        master=_get_top_frame(),
        state=READONLY,
        values=STACKS,
        variable=FORM["stack"]["variable"],
    )

    stack_combobox.grid(
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
        master=_get_top_frame(),
        text="Type*: ",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=3,
        sticky=NSEW,
    )

    FORM["type"] = {
        "is_required": True,
        "variable": ctk.StringVar(),
    }

    type_combobox: ctk.CTkComboBox = ctk.CTkComboBox(
        command=lambda value: on_type_combobox_select(
            scrollable_frame=_get_create_view_form_container(),
            value=value,
        ),
        master=_get_top_frame(),
        state=READONLY,
        values=[
            "Flashcard",
            "Note",
            "Question",
            "Stack",
        ],
        variable=FORM["type"]["variable"],
    )

    type_combobox.set(value="Stack")

    type_combobox.grid(
        column=1,
        padx=5,
        pady=5,
        row=3,
        sticky=NSEW,
    )

    ctk.CTkLabel(
        anchor=W,
        font=(
            "Helvetica",
            12,
            "bold",
        ),
        master=_get_top_frame(),
        text="Difficulty*: ",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=4,
        sticky=NSEW,
    )

    FORM["difficulty"] = {
        "is_required": True,
        "variable": ctk.StringVar(),
    }

    difficulty_names: list[str] = [
        difficulty["display_name"]
        for difficulty in (
            dispatch(
                event=GET_ALL_DIFFICULTIES_FROM_DB,
                namespace=GLOBAL,
                table_name="difficulties",
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

    difficulty_combobox: ctk.CTkComboBox = ctk.CTkComboBox(
        master=_get_top_frame(),
        state=READONLY,
        values=difficulty_names,
        variable=FORM["difficulty"]["variable"],
    )

    difficulty_combobox.grid(
        column=1,
        padx=5,
        pady=5,
        row=4,
        sticky=NSEW,
    )

    ctk.CTkLabel(
        anchor=W,
        font=(
            "Helvetica",
            12,
            "bold",
        ),
        master=_get_top_frame(),
        text="Priority*: ",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=5,
        sticky=NSEW,
    )

    FORM["priority"] = {
        "is_required": True,
        "variable": ctk.StringVar(),
    }

    priority_names: list[str] = [
        priority["display_name"]
        for priority in (
            dispatch(
                event=GET_ALL_PRIORITIES_FROM_DB,
                namespace=GLOBAL,
                table_name="priorities",
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

    priority_combobox: ctk.CTkComboBox = ctk.CTkComboBox(
        master=_get_top_frame(),
        state=READONLY,
        values=priority_names,
        variable=FORM["priority"]["variable"],
    )

    priority_combobox.grid(
        column=1,
        padx=5,
        pady=5,
        row=5,
        sticky=NSEW,
    )


def _get_bottom_frame() -> ctk.CTkFrame:
    """
    Returns the bottom frame of the create view.

    Args:
        None

    Returns:
        ctk.CTkFrame: The bottom frame of the create view.

    Raises:
        ValueError: If the bottom frame has not been initialized yet.
    """

    if BOTTOM_FRAME is None:
        raise ValueError(
            "The bottom frame has not been initialized yet."
            "The method '_set_bottom_frame' must be executed first."
        )

    return BOTTOM_FRAME


def _get_center_frame() -> ctk.CTkFrame:
    """
    Returns the center frame of the create view.

    Args:
        None

    Returns:
        ctk.CTkFrame: The center frame of the create view.

    Raises:
        ValueError: If the center frame has not been initialized yet.
    """

    if CENTER_FRAME is None:
        raise ValueError(
            "The center frame has not been initialized yet."
            "The method '_set_center_frame' must be executed first."
        )

    return CENTER_FRAME


def _get_create_view_form_container() -> ctk.CTkScrollableFrame:
    """
    Retrieves the main scrollable container for create view forms.

    Raises:
        ValueError: If the container has not been initialized yet.

    Returns:
        ctk.CTkScrollableFrame: The scrollable frame instance.
    """

    if CREATE_VIEW_FORM_CONTAINER is None:
        raise ValueError(
            "The Create View Form Container has not yet been initialized."
            "The method '_set_create_view_form_container' must be executed first."
        )

    return CREATE_VIEW_FORM_CONTAINER


def _get_master() -> ctk.CTkToplevel:
    """
    Returns the toplevel window of the create view.

    Args:
        None

    Returns:
        ctk.CTkToplevel: The toplevel window of the create view.

    Raises:
        ValueError: If the master widget has not been initialized yet.
    """

    if MASTER is None:
        raise ValueError(
            "The master widget has not been initialized yet."
            "The method '_set_master' must be executed first."
        )

    return MASTER


def _get_top_frame() -> ctk.CTkFrame:
    """
    Returns the top frame of the create view.

    Args:
        None

    Returns:
        ctk.CTkFrame: The top frame of the create view.

    Raises:
        ValueError: If the top frame has not been initialized yet.
    """

    if TOP_FRAME is None:
        raise ValueError(
            "The top frame has not been initialized yet."
            "The method '_set_top_frame' must be executed first."
        )

    return TOP_FRAME


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
    Handles the 'DESTROY_CREATE_VIEW' event.

    Args:
        None

    Returns:
        None
    """

    global BOTTOM_FRAME, CENTER_FRAME, CREATE_VIEW_FORM_CONTAINER, MASTER, TOP_FRAME

    _unsubscribe_from_events()

    _get_master().destroy()

    FORM.clear()

    STACKS.clear()
    STACKS.append("")

    BOTTOM_FRAME = None
    CENTER_FRAME = None
    CREATE_VIEW_FORM_CONTAINER = None
    MASTER = None
    TOP_FRAME = None


def _on_get_create_form() -> dict[str, Any]:
    """
    Handles the 'GET_CREATE_FORM' event.

    Args:
        None

    Returns:
        dict[str, Any]: The create form data.
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


def _on_stack_added(stack: ModelDict) -> None:
    """
    Handles the 'STACK_ADDED' event.

    Args:
        stack (ModelDict): The stack to handle.

    Returns:
        None
    """

    STACKS.append(stack["metadata"]["name"])


def _set_bottom_frame(frame: ctk.CTkFrame) -> None:
    """
    Sets the bottom frame widget of the create view.

    Args:
        frame (ctk.CTkFrame): The frame to set as the bottom frame of the create view.

    Returns:
        None
    """

    global BOTTOM_FRAME

    BOTTOM_FRAME = frame


def _set_center_frame(frame: ctk.CTkFrame) -> None:
    """
    Sets the center frame widget of the create view.

    Args:
        frame (ctk.CTkFrame): The frame to set as the center frame of the create view.

    Returns:
        None
    """

    global CENTER_FRAME

    CENTER_FRAME = frame


def _set_create_view_form_container(scrollable_frame: ctk.CTkScrollableFrame) -> None:
    """
    Sets the main scrollable container for create view items.

    Args:
        scrollable_frame (ctk.CTkScrollableFrame): The CTkScrollableFrame instance to be set.

    Returns:
        None
    """

    global CREATE_VIEW_FORM_CONTAINER

    CREATE_VIEW_FORM_CONTAINER = scrollable_frame


def _set_master(toplevel: ctk.CTkToplevel) -> None:
    """
    Sets the master widget for the create view.

    Args:
        toplevel (ctk.CTkToplevel): The master window of the create view.

    Returns:
        None
    """

    global MASTER

    MASTER = toplevel


def _set_top_frame(frame: ctk.CTkFrame) -> None:
    """
    Sets the top frame widget of the create view.

    Args:
        frame (ctk.CTkFrame): The frame to set as the top frame of the create view.

    Returns:
        None
    """

    global TOP_FRAME

    TOP_FRAME = frame


def _subscribe_to_events() -> None:
    """
    Subscribes to events for the create view.

    Args:
        None

    Returns:
        None
    """

    subscriptions: list[dict[str, Any]] = [
        {
            "event": CLEAR_CREATE_FORM,
            "function": _on_clear_create_form,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": DESTROY_CREATE_VIEW,
            "function": _on_destroy,
            "namespace": GLOBAL,
            "persistent": False,
            "priority": 100,
        },
        {
            "event": GET_CREATE_FORM,
            "function": _on_get_create_form,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": STACK_ADDED,
            "function": _on_stack_added,
            "namespace": GLOBAL,
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

    log_info(message="Subscribed to all events for the create view.")


def _unsubscribe_from_events() -> None:
    """
    Unsubscribes from events for the create view.

    Args:
        None

    Returns:
        None
    """

    for uuid in SUBSCRIPTION_IDS:
        unsubscribe(uuid=uuid)

    log_info(message="Unsubscribed from all events for the create view.")

    SUBSCRIPTION_IDS.clear()


# ---------- Public Functions ---------- #


def get_create_view(toplevel: ctk.CTkToplevel) -> None:
    """
    Gets the create view of the application.

    Args:
        toplevel (ctk.CTkToplevel): The toplevel window of the create view.

    Returns:
        None
    """

    try:
        toplevel.geometry(geometry_string=TOPLEVEL_GEOMETRY)

        toplevel.title(string=WINDOW_TITLE)

        _set_master(toplevel=toplevel)
        _create_widgets()
        _configure_grid()
        _subscribe_to_events()

        dispatch(
            event=GET_STACK_CREATE_FORM,
            scrollable_frame=_get_create_view_form_container(),
        )
    except Exception as e:
        log_error(message=f"Caught an exception while attempting to get the create view: {e}")
        raise e
