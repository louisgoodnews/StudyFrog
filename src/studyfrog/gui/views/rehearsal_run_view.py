"""
Author: Louis Goodnews
Date: 2025-12-12
Description: The rehearsal run view of the application.
"""

import customtkinter as ctk

from tkinter.constants import DISABLED, NORMAL, NSEW, W
from typing import Any, Callable, Final, Literal, Optional

from constants.common import GLOBAL
from constants.events import (
    DESTROY_REHEARSAL_RUN_VIEW,
    LOAD_REHEARSAL_VIEW_FORM,
    REHEARSAL_RUN_INDEX_DECREMENTED,
    REHEARSAL_RUN_INDEX_INCREMENTED,
    REHEARSAL_RUN_INDEX_MAX_REACHED,
    REHEARSAL_RUN_INDEX_MIN_REACHED,
)
from gui.gui import get_bottom_frame, get_center_frame, get_top_frame
from gui.logic.rehearsal_run_view_logic import (
    end_rehearsal_run,
    on_cancel_button_click,
    on_easy_button_click,
    on_edit_button_click,
    on_hard_button_click,
    on_medium_button_click,
    on_next_button_click,
    on_previous_button_click,
    start_rehearsal_run,
)
from models.models import Model
from gui.views.flashcard_rehearsal_view import get_flashcard_rehearsal_view, set_flip_side
from gui.views.note_rehearsal_view import get_note_rehearsal_view
from gui.views.question_rehearsal_view import get_question_rehearsal_view
from utils.common import exists
from utils.dispatcher import subscribe, unsubscribe
from utils.gui import clear_bottom_frame, clear_center_frame, clear_top_frame
from utils.logging import log_error, log_info


# ---------- Exports ---------- #


__all__: Final[list[str]] = ["get_rehearsal_run_view"]


# ---------- Constants ---------- #

_EASY_BUTTON: Optional[ctk.CTkButton] = None
_HARD_BUTTON: Optional[ctk.CTkButton] = None
_MEDIUM_BUTTON: Optional[ctk.CTkButton] = None
_NEXT_BUTTON: Optional[ctk.CTkButton] = None
_PREVIOUS_BUTTON: Optional[ctk.CTkButton] = None
_REHEARSAL_RUN: Optional[Model] = None
_SUBSCRIPTION_IDS: Final[list[str]] = []


# ---------- Helper Functions ---------- #


def _get_rehearsal_run() -> Model:
    """
    Returns the rehearsal run.

    Args:
        None

    Returns:
        Model: The rehearsal run.
    """

    if not exists(value=_REHEARSAL_RUN):
        raise ValueError("Rehearsal run not found. Call 'set_rehearsal_run' first.")

    return _REHEARSAL_RUN


def _set_rehearsal_run(model: Model) -> None:
    """
    Sets the rehearsal run.

    Args:
        model (Model): The model to set.

    Returns:
        None
    """

    global _REHEARSAL_RUN

    _REHEARSAL_RUN = model


# ---------- Private Functions ---------- #


def _clear_widgets() -> None:
    """
    Clears the 'bottom', 'center' and 'top' frames.

    Args:
        None

    Returns:
        None
    """

    clear_bottom_frame()
    clear_center_frame()
    clear_top_frame()


def _configure_bottom_frame_grid() -> None:
    """
    Configure the grid of the bottom frame.

    Args:
        None

    Returns:
        None
    """

    get_bottom_frame().grid_columnconfigure(
        index=0,
        weight=0,
    )
    get_bottom_frame().grid_columnconfigure(
        index=1,
        weight=1,
    )
    get_bottom_frame().grid_columnconfigure(
        index=2,
        weight=0,
    )
    get_bottom_frame().grid_columnconfigure(
        index=2,
        weight=0,
    )

    get_bottom_frame().grid_columnconfigure(
        index=3,
        weight=0,
    )

    get_bottom_frame().grid_columnconfigure(
        index=4,
        weight=0,
    )
    get_bottom_frame().grid_columnconfigure(
        index=5,
        weight=1,
    )
    get_bottom_frame().grid_columnconfigure(
        index=6,
        weight=0,
    )
    get_bottom_frame().grid_rowconfigure(
        index=0,
        weight=0,
    )


def _configure_center_frame_grid() -> None:
    """
    Configure the grid of the center frame.

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
    Configure the grid of the top frame.

    Args:
        None

    Returns:
        None
    """

    get_top_frame().grid_columnconfigure(
        index=0,
        weight=1,
    )
    get_top_frame().grid_columnconfigure(
        index=1,
        weight=1,
    )
    get_top_frame().grid_columnconfigure(
        index=2,
        weight=0,
    )
    get_top_frame().grid_columnconfigure(
        index=3,
        weight=0,
    )
    get_top_frame().grid_rowconfigure(
        index=0,
        weight=0,
    )


def _configure_grid() -> None:
    """
    Configure the grid of the rehearsal run view.

    Args:
        None

    Returns:
        None
    """

    _configure_bottom_frame_grid()
    _configure_center_frame_grid()
    _configure_top_frame_grid()


def _create_bottom_frame_widgets() -> None:
    """
    Creates the bottom frame widgets.

    Args:
        None

    Returns:
        None
    """

    global _EASY_BUTTON, _HARD_BUTTON, _MEDIUM_BUTTON, _NEXT_BUTTON, _PREVIOUS_BUTTON

    previous_button: ctk.CTkButton = ctk.CTkButton(
        command=on_previous_button_click,
        master=get_bottom_frame(),
        state=DISABLED,
        text="Previous",
    )

    previous_button.grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
    )

    _PREVIOUS_BUTTON = previous_button

    easy_button: ctk.CTkButton = ctk.CTkButton(
        command=on_easy_button_click,
        master=get_bottom_frame(),
        text="Easy",
    )

    easy_button.grid(
        column=2,
        padx=5,
        pady=5,
        row=0,
    )

    _EASY_BUTTON = easy_button

    medium_button: ctk.CTkButton = ctk.CTkButton(
        command=on_medium_button_click,
        master=get_bottom_frame(),
        text="Medium",
    )

    medium_button.grid(
        column=3,
        padx=5,
        pady=5,
        row=0,
    )

    _MEDIUM_BUTTON = medium_button

    hard_button: ctk.CTkButton = ctk.CTkButton(
        command=on_hard_button_click,
        master=get_bottom_frame(),
        text="Hard",
    )

    hard_button.grid(
        column=4,
        padx=5,
        pady=5,
        row=0,
    )

    _HARD_BUTTON = hard_button

    next_button: ctk.CTkButton = ctk.CTkButton(
        command=on_next_button_click,
        master=get_bottom_frame(),
        text="Next",
    )

    next_button.grid(
        column=6,
        padx=5,
        pady=5,
        row=0,
    )

    _NEXT_BUTTON = next_button


def _create_center_frame_widgets() -> None:
    """
    Creates the center frame widgets.

    Args:
        None

    Returns:
        None
    """

    pass


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
        text="Running rehearsal...",
    ).grid(
        column=1,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    ctk.CTkButton(
        command=on_cancel_button_click,
        master=get_top_frame(),
        text="Cancel",
    ).grid(
        column=2,
        padx=5,
        pady=5,
        row=0,
    )

    ctk.CTkButton(
        command=on_edit_button_click,
        master=get_top_frame(),
        text="Edit",
    ).grid(
        column=3,
        padx=5,
        pady=5,
        row=0,
    )


def _create_widgets() -> None:
    """
    Creates the widgets of the rehearsal run view.

    Args:
        None

    Returns:
        None
    """

    _create_bottom_frame_widgets()
    _create_center_frame_widgets()
    _create_top_frame_widgets()


def _load_rehearsal_view_form(
    model: Model,
    model_type: Literal[
        "flashcard",
        "note",
        "question",
    ],
) -> None:
    """
    Loads the rehearsal view form corresponding to the passed model type.

    Args:
        model_dict (ModelDict): The entity to load the rehearsal view form for.
        model_type (Literal["flashcard", "note", "question"]: The model type.

    Returns:
        None
    """

    model_type_to_rehearsal_form_getter: dict[
        Literal[
            "flashcard",
            "note",
            "question",
        ],
        Callable[[Model], None],
    ] = {
        "flashcard": get_flashcard_rehearsal_view,
        "note": get_note_rehearsal_view,
        "question": get_question_rehearsal_view,
    }

    if model_type == "flashcard":
        set_flip_side(flip_side="front")

    model_type_to_rehearsal_form_getter[model_type](**{model_type: model})


def _on_destroy() -> None:
    """
    Handles the 'DESTROY__REHEARSAL_RUN_VIEW' event.

    Args:
        None

    Returns:
        None
    """

    global _EASY_BUTTON, _HARD_BUTTON, _MEDIUM_BUTTON, _NEXT_BUTTON, _PREVIOUS_BUTTON, _REHEARSAL_RUN

    _clear_widgets()
    _unsubscribe_from_events()

    _SUBSCRIPTION_IDS.clear()

    _EASY_BUTTON = None

    _HARD_BUTTON = None

    _MEDIUM_BUTTON = None

    _NEXT_BUTTON = None

    _PREVIOUS_BUTTON = None

    _REHEARSAL_RUN = None


def _on_load_rehearsal_view_form(model: Model) -> None:
    """
    Handles the 'LOAD_REHEARSAL_VIEW_FORM' event.

    Args:
        model (Model): The model to load the rehearsal view form for.

    Returns:
        None
    """

    for button in (
        _EASY_BUTTON,
        _HARD_BUTTON,
        _MEDIUM_BUTTON,
        _NEXT_BUTTON,
        _PREVIOUS_BUTTON,
    ):
        button.configure(state=NORMAL)

    _load_rehearsal_view_form(
        model=model,
        model_type=model.type_.lower(),
    )


def _on_rehearsal_run_index_decremented() -> None:
    """
    Handles the '_REHEARSAL_RUN_INDEX_DECREMENTED' event.

    Args:
        None

    Result:
        None
    """

    _NEXT_BUTTON.configure(state=NORMAL)
    _PREVIOUS_BUTTON.configure(state=NORMAL)


def _on_rehearsal_run_index_incremented() -> None:
    """
    Handles the '_REHEARSAL_RUN_INDEX_INCREMENTED' event.

    Args:
        None

    Result:
        None
    """

    _NEXT_BUTTON.configure(state=NORMAL)
    _PREVIOUS_BUTTON.configure(state=NORMAL)


def _on_rehearsal_run_max_index_reached() -> None:
    """
    Handles the '_REHEARSAL_RUN_INDEX_MAX_REACHED' event.

    Args:
        None

    Result:
        None
    """

    _NEXT_BUTTON.configure(state=DISABLED)

    end_rehearsal_run(rehearsal_run=_get_rehearsal_run())


def _on_rehearsal_run_min_index_reached() -> None:
    """
    Handles the '_REHEARSAL_RUN_INDEX_MIN_REACHED' event.

    Args:
        None

    Result:
        None
    """

    _PREVIOUS_BUTTON.configure(state=DISABLED)


def _subscribe_to_events() -> None:
    """
    Subscribes to events in the rehearsal run view.

    Args:
        None

    Returns:
        None
    """

    subscriptions: list[dict[str, Any]] = [
        {
            "event": DESTROY_REHEARSAL_RUN_VIEW,
            "function": _on_destroy,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": LOAD_REHEARSAL_VIEW_FORM,
            "function": _on_load_rehearsal_view_form,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": REHEARSAL_RUN_INDEX_DECREMENTED,
            "function": _on_rehearsal_run_index_decremented,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": REHEARSAL_RUN_INDEX_INCREMENTED,
            "function": _on_rehearsal_run_index_incremented,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": REHEARSAL_RUN_INDEX_MAX_REACHED,
            "function": _on_rehearsal_run_max_index_reached,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": REHEARSAL_RUN_INDEX_MIN_REACHED,
            "function": _on_rehearsal_run_min_index_reached,
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

    log_info(message="Subscribed to events in the rehearsal run view.")


def _unsubscribe_from_events() -> None:
    """
    Unsubscribes from events in the rehearsal run view.

    Args:
        None

    Returns:
        None
    """

    for uuid in _SUBSCRIPTION_IDS:
        unsubscribe(uuid=uuid)

    log_info(message="Unsubscribed from all events in the rehearsal run view.")


# ---------- Public Functions ---------- #


def get_rehearsal_run_view(model: Model) -> None:
    """
    Gets the rehearsal run view of the application.

    Args:
        model (Model): The model to display.

    Returns:
        None
    """

    try:
        _set_rehearsal_run(model=model)

        _clear_widgets()
        _configure_grid()
        _create_widgets()
        _subscribe_to_events()

        start_rehearsal_run(model=model)
    except Exception as e:
        log_error(message=f"Failed to get rehearsal run view: {e}")
        raise e
