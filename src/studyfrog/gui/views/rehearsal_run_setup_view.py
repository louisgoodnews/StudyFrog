"""
Author: Louis Goodnews
Date: 2025-12-19
Description: The rehearsal run setup view of the application.
"""

from __future__ import annotations

import customtkinter as ctk

from tkinter.constants import NSEW, TOP, VERTICAL, W, X, YES
from typing import Any, Final, Optional

from studyfrog.constants.common import GLOBAL
from studyfrog.constants.events import (
    CLEAR_REHEARSAL_RUN_SETUP_FORM,
    DESTROY_REHEARSAL_RUN_SETUP_VIEW,
    GET_ALL_DIFFICULTIES_FROM_DB,
    GET_ALL_PRIORITIES_FROM_DB,
    GET_ALL_STACKS_FROM_DB,
    GET_REHEARSAL_RUN_SETUP_FORM,
)
from studyfrog.gui.gui import get_bottom_frame, get_center_frame, get_top_frame
from studyfrog.gui.logic.rehearsal_run_setup_view_logic import on_cancel_button_click, on_start_button_click
from studyfrog.models.models import Model
from studyfrog.utils.common import exists
from studyfrog.utils.dispatcher import dispatch, subscribe, unsubscribe
from studyfrog.utils.gui import (
    clear_bottom_frame,
    clear_center_frame,
    clear_top_frame,
    count_widget_children,
    destroy_widget_children,
)
from studyfrog.utils.logging import log_error, log_info


# ---------- Exports ---------- #

__all__: Final[list[str]] = ["get_rehearsal_run_setup_view"]


# ---------- Constants ---------- #

_FORM: Final[dict[str, Any]] = {}
_SUBSCRIPTION_IDS: Final[list[str]] = []


# ---------- Helper Functions ---------- #


def _on_time_limit_enabled_checkbox_click(frame: ctk.CTkFrame) -> None:
    """
    Handles the 'time limit enabled' checkbox click event.

    Args:
        frame (ctk.CTkFrame): The frame widget.

    Returns:
        None
    """

    if _FORM["time_limit_enabled"]["variable"].get():
        frame.pack(
            expand=YES,
            fill=X,
            padx=5,
            pady=5,
            side=TOP,
        )
        _create_time_limit_form_widgets(master=frame)
    else:
        frame.pack_forget()
        destroy_widget_children(widget=frame)


# ---------- Private Functions ---------- #


def _clear_widgets() -> None:
    """
    Clears the widgets of the rehearsal run setup view.

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
    Configures the grid of the widgets of the rehearsal run setup view.

    Args:
        None

    Returns:
        None
    """

    _configure_bottom_frame_grid()
    _configure_center_frame_grid()
    _configure_top_frame_grid()


def _configure_bottom_frame_grid() -> None:
    """
    Configures the grid of the bottom frame.

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
        weight=0,
    )
    get_bottom_frame().grid_rowconfigure(
        index=0,
        weight=0,
    )


def _configure_center_frame_grid() -> None:
    """
    Configures the grid of the center frame.

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
    Configures the grid of the top frame.

    Args:
        None

    Returns:
        None
    """

    get_top_frame().grid_columnconfigure(
        index=0,
        weight=1,
    )
    get_top_frame().grid_rowconfigure(
        index=0,
        weight=0,
    )


def _create_widgets() -> None:
    """
    Creates the widgets of the rehearsal run setup view.

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
    Creates the bottom frame widgets.

    Args:
        None

    Returns:
        None
    """

    ctk.CTkButton(
        command=on_cancel_button_click,
        master=get_bottom_frame(),
        text="Cancel",
    ).grid(
        column=1,
        padx=5,
        pady=5,
        row=0,
    )

    ctk.CTkButton(
        command=on_start_button_click,
        master=get_bottom_frame(),
        text="Start",
    ).grid(
        column=2,
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

    _create_difficulty_form_widgets(master=scrollable_frame)
    _create_priority_form_widgets(master=scrollable_frame)
    _create_randomization_form_widgets(master=scrollable_frame)
    _create_stack_selection_form_widgets(master=scrollable_frame)
    _create_time_counter_selection_form_widgets(master=scrollable_frame)
    _create_time_limit_selection_form_widgets(master=scrollable_frame)


def _create_difficulty_form_widgets(master: ctk.CTkScrollableFrame) -> None:
    """
    Creates the 'difficulty' form widgets.

    Args:
        master (ctk.CTkScrollableFrame): The master widget.

    Returns:
        None
    """

    _FORM["difficulty"] = {
        "is_required": False,
        "variable": ctk.StringVar(),
    }

    frame: ctk.CTkFrame = ctk.CTkFrame(master=master)

    frame.pack(
        expand=YES,
        fill=X,
        padx=5,
        pady=5,
        side=TOP,
    )

    frame.grid_columnconfigure(
        index=0,
        weight=0,
    )
    frame.grid_columnconfigure(
        index=1,
        weight=1,
    )
    frame.grid_rowconfigure(
        index=0,
        weight=0,
    )
    frame.grid_rowconfigure(
        index=1,
        weight=0,
    )

    ctk.CTkLabel(
        master=frame,
        text="Filter by difficulty: ",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    difficulties: list[str] = [" "] + [
        difficulty.display_name
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

    ctk.CTkComboBox(
        master=frame,
        values=difficulties,
        variable=_FORM["difficulty"]["variable"],
    ).grid(
        column=1,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    ctk.CTkLabel(
        anchor=W,
        master=frame,
        text="Leave empty to include all difficulties.",
    ).grid(
        column=1,
        padx=5,
        pady=5,
        row=1,
        sticky=NSEW,
    )


def _create_priority_form_widgets(master: ctk.CTkScrollableFrame) -> None:
    """
    Creates the 'priority' form widgets.

    Args:
        master (ctk.CTkScrollableFrame): The master widget.

    Returns:
        None
    """

    _FORM["priority"] = {
        "is_required": False,
        "variable": ctk.StringVar(),
    }

    frame: ctk.CTkFrame = ctk.CTkFrame(master=master)

    frame.pack(
        expand=YES,
        fill=X,
        padx=5,
        pady=5,
        side=TOP,
    )

    frame.grid_columnconfigure(
        index=0,
        weight=0,
    )
    frame.grid_columnconfigure(
        index=1,
        weight=1,
    )
    frame.grid_rowconfigure(
        index=0,
        weight=0,
    )
    frame.grid_rowconfigure(
        index=1,
        weight=0,
    )

    ctk.CTkLabel(
        master=frame,
        text="Filter by priority: ",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    priorities: list[str] = [" "] + [
        priority.display_name
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

    ctk.CTkComboBox(
        master=frame,
        values=priorities,
        variable=_FORM["priority"]["variable"],
    ).grid(
        column=1,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    ctk.CTkLabel(
        anchor=W,
        master=frame,
        text="Leave empty to include all priorities.",
    ).grid(
        column=1,
        padx=5,
        pady=5,
        row=1,
        sticky=NSEW,
    )


def _create_randomization_form_widgets(master: ctk.CTkScrollableFrame) -> None:
    """
    Creates the 'randomization' form widgets.

    Args:
        master (ctk.CTkScrollableFrame): The master widget.

    Returns:
        None
    """

    _FORM["item_order_randomization_enabled"] = {
        "is_required": False,
        "variable": ctk.BooleanVar(),
    }

    frame: ctk.CTkFrame = ctk.CTkFrame(master=master)

    frame.pack(
        expand=YES,
        fill=X,
        padx=5,
        pady=5,
        side=TOP,
    )

    frame.grid_columnconfigure(
        index=0,
        weight=0,
    )
    frame.grid_columnconfigure(
        index=1,
        weight=1,
    )
    frame.grid_rowconfigure(
        index=0,
        weight=0,
    )
    frame.grid_rowconfigure(
        index=1,
        weight=0,
    )

    ctk.CTkLabel(
        master=frame,
        text="Enable randomization of item order? ",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    ctk.CTkCheckBox(
        master=frame,
        text="",
        variable=_FORM["item_order_randomization_enabled"]["variable"],
    ).grid(
        column=1,
        padx=5,
        pady=5,
        row=0,
        sticky=W,
    )


def _create_stack_selection_form_widgets(master: ctk.CTkScrollableFrame) -> None:
    """
    Creates the 'stack selection' form widgets.

    Args:
        master (ctk.CTkScrollableFrame): The master widget.

    Returns:
        None
    """

    stacks: list[str] = [" "] + [
        stack.name
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

    selected: list[str] = _FORM["stacks"]["variable"].get().split(", ")

    outer_frame: ctk.CTkFrame = ctk.CTkFrame(master=master)

    outer_frame.pack(
        expand=YES,
        fill=X,
        padx=5,
        pady=5,
        side=TOP,
    )

    outer_frame.grid_columnconfigure(
        index=0,
        weight=1,
    )

    def create_widgets() -> None:
        """
        Creates the 'stack selection' form widgets.

        Args:
            None

        Returns:
            None
        """

        inner_frame: ctk.CTkFrame = ctk.CTkFrame(master=outer_frame)

        inner_frame.grid(
            column=0,
            padx=5,
            pady=5,
            row=count_widget_children(widget=outer_frame),
            sticky=NSEW,
        )

        inner_frame.grid_columnconfigure(
            index=0,
            weight=0,
        )
        inner_frame.grid_columnconfigure(
            index=1,
            weight=1,
        )
        inner_frame.grid_rowconfigure(
            index=0,
            weight=0,
        )
        inner_frame.grid_rowconfigure(
            index=1,
            weight=0,
        )

        ctk.CTkLabel(
            master=inner_frame,
            text="Select a stack: ",
        ).grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        ctk.CTkComboBox(
            command=lambda value: (
                selected.append(value),
                _FORM["stacks"]["variable"].set(value=", ".join(list(set(selected)))),
            ),
            master=inner_frame,
            values=stacks,
        ).grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        ctk.CTkButton(
            command=create_widgets,
            master=inner_frame,
            text="Select another stack",
        ).grid(
            column=1,
            padx=5,
            pady=5,
            row=1,
        )

        outer_frame.grid_rowconfigure(
            index=count_widget_children(widget=outer_frame),
            weight=1,
        )

    create_widgets()


def _create_time_counter_selection_form_widgets(master: ctk.CTkScrollableFrame) -> None:
    """
    Creates the 'time counter selection' form widgets.

    Args:
        master (ctk.CTkScrollableFrame): The master widget.

    Returns:
        None
    """

    _FORM["time_counter_enabled"] = {
        "is_required": True,
        "variable": ctk.BooleanVar(value=False),
    }

    frame: ctk.CTkFrame = ctk.CTkFrame(master=master)

    frame.pack(
        expand=YES,
        fill=X,
        padx=5,
        pady=5,
        side=TOP,
    )

    frame.grid_columnconfigure(
        index=0,
        weight=0,
    )
    frame.grid_columnconfigure(
        index=1,
        weight=1,
    )
    frame.grid_rowconfigure(
        index=0,
        weight=0,
    )
    frame.grid_rowconfigure(
        index=1,
        weight=0,
    )

    ctk.CTkLabel(
        master=frame,
        text="Enable time counter?* ",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    ctk.CTkCheckBox(
        master=frame,
        text="",
        variable=_FORM["time_counter_enabled"]["variable"],
    ).grid(
        column=1,
        padx=5,
        pady=5,
        row=0,
        sticky=W,
    )


def _create_time_limit_selection_form_widgets(master: ctk.CTkScrollableFrame) -> None:
    """
    Creates the 'time limit selection' form widgets.

    Args:
        master (ctk.CTkScrollableFrame): The master widget.

    Returns:
        None
    """

    _FORM["time_limit_enabled"] = {
        "is_required": True,
        "variable": ctk.BooleanVar(value=False),
    }

    frame: ctk.CTkFrame = ctk.CTkFrame(master=master)

    frame.pack(
        expand=YES,
        fill=X,
        padx=5,
        pady=5,
        side=TOP,
    )

    frame.grid_columnconfigure(
        index=0,
        weight=0,
    )
    frame.grid_columnconfigure(
        index=1,
        weight=1,
    )
    frame.grid_rowconfigure(
        index=0,
        weight=0,
    )
    frame.grid_rowconfigure(
        index=1,
        weight=0,
    )

    container: ctk.CTkFrame = ctk.CTkFrame(master=master)

    container.grid_columnconfigure(
        index=0,
        weight=0,
    )
    container.grid_columnconfigure(
        index=1,
        weight=1,
    )
    container.grid_columnconfigure(
        index=2,
        weight=0,
    )
    container.grid_rowconfigure(
        index=0,
        weight=0,
    )
    container.grid_rowconfigure(
        index=1,
        weight=0,
    )

    ctk.CTkLabel(
        master=frame,
        text="Enable time limit?* ",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    ctk.CTkCheckBox(
        command=lambda: _on_time_limit_enabled_checkbox_click(frame=container),
        master=frame,
        text="",
        variable=_FORM["time_limit_enabled"]["variable"],
    ).grid(
        column=1,
        padx=5,
        pady=5,
        row=0,
        sticky=W,
    )


def _create_time_limit_form_widgets(master: ctk.CTkFrame) -> None:
    """
    Creates the 'time limit' form widgets.

    Args:
        master (ctk.CTkScrollableFrame): The master widget.

    Returns:
        None
    """

    def on_slider_change() -> None:
        """
        Handles the slider's value change.

        Args:
            None

        Returns:
            None
        """

        label.configure(text=f"{_FORM['time_limit']['variable'].get()} minutes")

    _FORM["time_limit"] = {
        "is_required": False,
        "variable": ctk.IntVar(value=60),
    }

    ctk.CTkLabel(
        master=master,
        text="Time limit (minutes):* ",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    label: ctk.CTkLabel = ctk.CTkLabel(
        master=master,
        text=f"{_FORM['time_limit']['variable'].get()} minutes",
    )

    label.grid(
        column=2,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    ctk.CTkSlider(
        command=lambda value: on_slider_change(),
        master=master,
        number_of_steps=8,
        to=480,
        variable=_FORM["time_limit"]["variable"],
    ).grid(
        column=1,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    ctk.CTkLabel(
        anchor=W,
        master=master,
        text="You can set a time limit between 1 and 480 minutes for the rehearsal run.",
    ).grid(
        column=1,
        padx=5,
        pady=5,
        row=1,
        sticky=NSEW,
    )


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
        master=get_top_frame(),
        text=f"Rehearsal run setup for {_FORM['stacks']['variable'].get()}",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )


def _on_clear_rehearsal_run_setup_form() -> None:
    """
    Handles the 'CLEAR_REHEARSAL_RUN_SETUP_FORM' event.

    Args:
        None

    Returns:
        None
    """

    _FORM.clear()


def _on_destroy() -> None:
    """
    Handles the 'DESTROY_REHEARSAL_RUN_SETUP_VIEW' event.

    Args:
        None

    Returns:
        None
    """

    _unsubscribe_from_events()

    _FORM.clear()


def _on_get_rehearsal_run_setup_form() -> dict[str, Any]:
    """
    Handles the 'GET_REHEARSAL_RUN_SETUP_FORM' event.

    Args:
        None

    Returns:
        dict[str, Any]: The form.
    """

    return {
        key: {
            "is_required": value["is_required"],
            "value": value["variable"].get(),
        }
        for (
            key,
            value,
        ) in _FORM.items()
    }


def _subscribe_to_events() -> None:
    """
    Subscribes to events.

    Args:
        None

    Returns:
        None
    """

    subscriptions: list[dict[str, Any]] = [
        {
            "event": CLEAR_REHEARSAL_RUN_SETUP_FORM,
            "function": _on_clear_rehearsal_run_setup_form,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": DESTROY_REHEARSAL_RUN_SETUP_VIEW,
            "function": _on_destroy,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": GET_REHEARSAL_RUN_SETUP_FORM,
            "function": _on_get_rehearsal_run_setup_form,
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


def _unsubscribe_from_events() -> None:
    """
    Unsubscribes from events.

    Args:
        None

    Returns:
        None
    """

    for uuid in _SUBSCRIPTION_IDS:
        unsubscribe(uuid=uuid)

    log_info(message="Unsubscribed from all events for the rehearsal run setup view.")

    _SUBSCRIPTION_IDS.clear()


# ---------- Public Functions ---------- #


def get_rehearsal_run_setup_view(
    model: Optional[Model] = None,
    models: Optional[list[Model]] = None,
) -> None:
    """
    Gets the rehearsal run setup view of the application.

    Args:
        model (Optional[Model], optional): The model to rehearse. Defaults to None.
        models (Optional[list[Model]], optional): The models to rehearse. Defaults to None.

    Returns:
        None
    """

    try:
        if exists(value=model):
            _FORM["stacks"] = {
                "is_required": True,
                "variable": ctk.StringVar(value=model.name),
            }

        elif exists(value=models):
            _FORM["stacks"] = {
                "is_required": True,
                "variable": ctk.StringVar(
                    value=", ".join(list(set([model.name for model in models])))
                ),
            }

        else:
            _FORM["stacks"] = {
                "is_required": True,
                "variable": ctk.StringVar(value=""),
            }

        _clear_widgets()
        _configure_widget_grids()
        _create_widgets()
        _subscribe_to_events()
    except Exception as e:
        log_error(message=f"Failed to get rehearsal run setup view: {e}")
        raise e
