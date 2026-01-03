"""
Author: Louis Goodnews
Date: 2025-12-12
Description: The create view of the application.
"""

import customtkinter as ctk

from tkinter.constants import NSEW, W
from typing import Any, Final, Optional, Union

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
    STACKS_ADDED,
)
from constants.gui import READONLY, TOPLEVEL_GEOMETRY, WINDOW_TITLE
from gui.logic.create_view_logic import (
    on_create_button_click,
    on_cancel_button_click,
    on_type_combobox_select,
)
from models.models import ModelDict
from utils.common import exists
from utils.dispatcher import dispatch, subscribe, unsubscribe
from utils.logging import log_error, log_info


# ---------- Exports ---------- #

__all__: Final[list[str]] = ["get_create_view"]


# ---------- Constants ---------- #

_BOTTOM_FRAME: Optional[ctk.CTkFrame] = None

_CENTER_FRAME: Optional[ctk.CTkFrame] = None

_CREATE_VIEW_FORM_CONTAINER: Optional[ctk.CTkScrollableFrame] = None

_FORM: Final[dict[str, Any]] = {}

_MASTER: Optional[ctk.CTkToplevel] = None

_STACKS: Final[list[str]] = [""]

_SUBSCRIPTION_IDS: Final[list[str]] = []

_TOP_FRAME: Optional[ctk.CTkFrame] = None


# ---------- Helper Functions ---------- #


def _get_bottom_frame() -> ctk.CTkFrame:
    """
    Returns the 'bottom' frame of the create view.

    Args:
        None

    Returns:
        ctk.CTkFrame: The 'bottom' frame of the create view.

    Raises:
        ValueError: If the 'bottom' frame has not been initialized.
    """

    if not exists(value=_BOTTOM_FRAME):
        raise ValueError(
            "'bottom' frame does not exist. Call the '_set_bottom_frame' method first."
        )

    return _BOTTOM_FRAME


def _get_center_frame() -> ctk.CTkFrame:
    """
    Returns the 'center' frame of the create view.

    Args:
        None

    Returns:
        ctk.CTkFrame: The 'center' frame of the create view.

    Raises:
        ValueError: If the 'center' frame has not been initialized.
    """

    if not exists(value=_CENTER_FRAME):
        raise ValueError(
            "'center' frame does not exist. Call the '_set_center_frame' method first."
        )

    return _CENTER_FRAME


def _get_create_view_form_container() -> ctk.CTkScrollableFrame:
    """
    Returns the 'create view form container' of the create view.

    Args:
        None

    Returns:
        ctk.CTkScrollableFrame: The 'create view form container' of the create view.

    Raises:
        ValueError: If the 'create view form container' has not been initialized.
    """

    if not exists(value=_CREATE_VIEW_FORM_CONTAINER):
        raise ValueError(
            "'create view form container' does not exist. Call the '_set_create_view_form_container' method first."
        )

    return _CREATE_VIEW_FORM_CONTAINER


def _get_form() -> dict[str, Any]:
    """
    Returns the underlying dictionary 'serializing' the UI form.

    Args:
        None

    Returns:
        dict[str, Any]: The underlying dictionary 'serializing' the UI form.
    """

    return _FORM


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

    if not exists(value=_MASTER):
        raise ValueError("The master widget does not exist. Call the '_set_master' method first.")

    return _MASTER


def _get_stacks_list() -> list[str]:
    """
    Returns the list of stack names.

    Args:
        None

    Returns:
        list[str]: The list of stack names.
    """

    return _STACKS


def _get_top_frame() -> ctk.CTkFrame:
    """
    Returns the 'top' frame of the create view.

    Args:
        None

    Returns:
        ctk.CTkFrame: The 'top' frame of the create view.

    Raises:
        ValueError: If the 'top' frame has not been initialized.
    """

    if not exists(value=_TOP_FRAME):
        raise ValueError("'top' frame does not exist. Call the '_set_top_frame' method first.")

    return _TOP_FRAME


def _set_bottom_frame(frame: ctk.CTkFrame) -> None:
    """
    Sets the 'bottom' frame of the create view.

    Args:
        frame (ctk.CTkFrame): The 'bottom' frame of the create view.

    Returns:
        None
    """

    global _BOTTOM_FRAME

    _BOTTOM_FRAME = frame


def _set_center_frame(frame: ctk.CTkFrame) -> None:
    """
    Sets the 'center' frame of the create view.

    Args:
        frame (ctk.CTkFrame): The 'center' frame of the create view.

    Returns:
        None
    """

    global _CENTER_FRAME

    _CENTER_FRAME = frame


def _set_create_view_form_container(scrollable_frame: ctk.CTkScrollableFrame) -> None:
    """
    Sets the 'create view form container' of the create view.

    Args:
        scrollable_frame (ctk.CTkScrollableFrame): The 'create view form container' of the create view.

    Returns:
        None
    """

    global _CREATE_VIEW_FORM_CONTAINER

    _CREATE_VIEW_FORM_CONTAINER = scrollable_frame


def _set_master(toplevel: ctk.CTkToplevel) -> None:
    """
    Sets the master widget for the create view.

    Args:
        toplevel (ctk.CTkToplevel): The master window of the create view.

    Returns:
        None
    """

    global _MASTER

    _MASTER = toplevel


def _set_top_frame(frame: ctk.CTkFrame) -> None:
    """
    Sets the 'top' frame of the create view.

    Args:
        frame (ctk.CTkFrame): The 'top' frame of the create view.

    Returns:
        None
    """

    global _TOP_FRAME

    _TOP_FRAME = frame


def _update_form(
    key: Union[list[str], str],
    value: Any,
) -> None:
    """
    Updates the underlying dictionary 'serializing' the UI form with the passed key and value pairs.

    Args:
        key (Union[list[str], str]): The key(s) to update with the passed value.
        value (Any): The value to update the passed key(s) with.

    Returns:
        None
    """

    if isinstance(
        key,
        list,
    ):
        for _key in key:
            _get_form()[_key] = value

        return

    _get_form()[key] = value


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

    _update_form(
        key="create_another",
        value={
            "is_required": False,
            "variable": ctk.BooleanVar(),
        },
    )

    ctk.CTkCheckBox(
        master=_get_bottom_frame(),
        text="Create another item",
        variable=_get_form()["create_another"]["variable"],
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

    _get_stacks_list().extend(
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

    _update_form(
        key="stack",
        value={
            "is_required": True,
            "variable": ctk.StringVar(),
        },
    )

    stack_combobox: ctk.CTkComboBox = ctk.CTkComboBox(
        master=_get_top_frame(),
        state=READONLY,
        values=_get_stacks_list(),
        variable=_get_form()["stack"]["variable"],
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

    _update_form(
        key="type",
        value={
            "is_required": True,
            "variable": ctk.StringVar(),
        },
    )

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
        variable=_get_form()["type"]["variable"],
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

    _update_form(
        key="difficulty",
        value={
            "is_required": True,
            "variable": ctk.StringVar(),
        },
    )

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
        variable=_get_form()["difficulty"]["variable"],
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

    _update_form(
        key="priority",
        value={
            "is_required": True,
            "variable": ctk.StringVar(),
        },
    )

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
        variable=_get_form()["priority"]["variable"],
    )

    priority_combobox.grid(
        column=1,
        padx=5,
        pady=5,
        row=5,
        sticky=NSEW,
    )


def _on_clear_create_form() -> None:
    """
    Handles the 'CLEAR_CREATE__FORM' event.

    Args:
        None

    Returns:
        None
    """

    for value in _get_form().values():
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

    global _BOTTOM_FRAME, _CENTER_FRAME, _CREATE_VIEW__FORM_CONTAINER, _MASTER, _TOP_FRAME

    _unsubscribe_from_events()

    _get_master().destroy()

    _get_form().clear()

    _get_stacks_list().clear()
    _get_stacks_list().append("")

    _BOTTOM_FRAME = None
    _CENTER_FRAME = None
    _CREATE_VIEW__FORM_CONTAINER = None
    _MASTER = None
    _TOP_FRAME = None


def _on_get_create_form() -> dict[str, Any]:
    """
    Handles the 'GET_CREATE_FORM' event.

    Args:
        None

    Returns:
        dict[str, Any]: The create form data.
    """

    return {
        "form_content": {
            key: {
                "is_required": value["is_required"],
                "value": value["variable"].get(),
            }
            for (
                key,
                value,
            ) in _get_form().items()
        },
        "origin": "create_view",
    }


def _on_stack_added(stack: ModelDict) -> None:
    """
    Handles the 'STACK_ADDED' event.

    Args:
        stack (ModelDict): The stack to handle.

    Returns:
        None
    """

    _get_stacks_list().append(stack["metadata"]["name"])


def _on_stacks_added(stacks: list[ModelDict]) -> None:
    """
    Handles the 'STACKS_ADDED' event.

    Args:
        stacks (list[ModelDict]): The stacks to handle.

    Returns:
        None
    """

    _get_stacks_list().extend([stack["metadata"]["name"] for stack in stacks])


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
        {
            "event": STACKS_ADDED,
            "function": _on_stacks_added,
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

    log_info(message="Subscribed to all events for the create view.")


def _unsubscribe_from_events() -> None:
    """
    Unsubscribes from events for the create view.

    Args:
        None

    Returns:
        None
    """

    for uuid in _SUBSCRIPTION_IDS:
        unsubscribe(uuid=uuid)

    log_info(message="Unsubscribed from all events for the create view.")

    _SUBSCRIPTION_IDS.clear()


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
