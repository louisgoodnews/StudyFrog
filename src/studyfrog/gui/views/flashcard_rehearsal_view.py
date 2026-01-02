"""
Author: Louis Goodnews
Date: 2025-12-21
Description: The flashcard rehearsal view of the application.
"""

import customtkinter as ctk

from tkinter.constants import NSEW
from typing import Any, Final, Literal, Optional

from constants.common import GLOBAL
from constants.events import FLASHCARD_FLIPPED
from gui.gui import get_center_frame
from utils.dispatcher import dispatch
from utils.gui import clear_center_frame, reset_center_frame_grid
from utils.logging import log_error


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "get_flashcard_rehearsal_view",
    "set_flip_side",
]


# ---------- Constants ---------- #

FLASHCARD: Optional[dict[str, Any]] = None

FLIP_SIDE: Literal["front", "back"] = "front"

SUBSCRIPTION_IDS: Final[list[str]] = []


# ---------- Helper Functions ---------- #


def _toggle_flip_side() -> Literal["front", "back"]:
    """
    Toggles the flip side and returns the new side.

    Args:
        None

    Returns:
        Literal["front", "back"]: The new side.
    """

    global FLIP_SIDE

    FLIP_SIDE = "front" if FLIP_SIDE == "back" else "back"

    return FLIP_SIDE


# ---------- Private Functions ---------- #


def _configure_bottom_frame_grid(frame: ctk.CTkFrame) -> None:
    """
    Configures the grid configuration for the 'bottom' frame for the flashcard rehearsal view.

    Args:
        frame (ctk.CTkFrame): The frame to configure the grid for.

    Returns:
        None
    """

    pass


def _configure_center_frame_grid(frame: ctk.CTkFrame) -> None:
    """
    Configures the grid configuration for the 'center' frame for the flashcard rehearsal view.

    Args:
        frame (ctk.CTkFrame): The frame to configure the grid for.

    Returns:
        None
    """

    frame.grid_columnconfigure(
        index=0,
        weight=1,
    )
    frame.grid_rowconfigure(
        index=0,
        weight=1,
    )


def _configure_grid() -> None:
    """
    Configures the grid configuration for the flashcard rehearsal view.

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
        weight=0,
    )
    get_center_frame().grid_rowconfigure(
        index=1,
        weight=1,
    )
    get_center_frame().grid_rowconfigure(
        index=2,
        weight=0,
    )


def _configure_top_frame_grid(frame: ctk.CTkFrame) -> None:
    """
    Configures the grid configuration for the 'top' frame for the flashcard rehearsal view.

    Args:
        frame (ctk.CTkFrame): The frame to configure the grid for.

    Returns:
        None
    """

    pass


def _create_bottom_frame_widgets(master: ctk.CTkFrame) -> None:
    """
    Creates the widgets for the 'bottom' frame for the flashcard rehearsal view.

    Args:
        None

    Returns:
        None
    """

    pass


def _create_center_frame_widgets(master: ctk.CTkFrame) -> None:
    """
    Creates the widgets for the 'center' frame for the flashcard rehearsal view.

    Args:
        None

    Returns:
        None
    """

    def on_label_click() -> None:
        """
        Handles the click event on the label.

        Args:
            None

        Returns:
            None
        """

        _toggle_flip_side()

        label.configure(text=_get_flashcard()[FLIP_SIDE])

        dispatch(
            event=FLASHCARD_FLIPPED,
            namespace=GLOBAL,
        )

    label: ctk.CTkLabel = ctk.CTkLabel(
        master=master,
        text=_get_flashcard()[FLIP_SIDE],
    )

    label.grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    label.bind(
        command=lambda event: on_label_click(),
        sequence="<ButtonRelease-1>",
    )


def _create_top_frame_widgets(master: ctk.CTkFrame) -> None:
    """
    Creates the widgets for the 'top' frame for the flashcard rehearsal view.

    Args:
        None

    Returns:
        None
    """

    pass


def _create_widgets() -> None:
    """
    Creates the widgets for the flashcard rehearsal view.

    Args:
        None

    Returns:
        None
    """

    bottom_frame: ctk.CTkFrame = ctk.CTkFrame(
        height=25,
        master=get_center_frame(),
    )

    bottom_frame.grid(
        column=0,
        padx=5,
        pady=5,
        row=2,
        sticky=NSEW,
    )

    _configure_bottom_frame_grid(frame=bottom_frame)
    _create_bottom_frame_widgets(master=bottom_frame)

    center_frame: ctk.CTkFrame = ctk.CTkFrame(master=get_center_frame())

    center_frame.grid(
        column=0,
        padx=5,
        pady=5,
        row=1,
        sticky=NSEW,
    )

    _configure_center_frame_grid(frame=center_frame)
    _create_center_frame_widgets(master=center_frame)

    top_frame: ctk.CTkFrame = ctk.CTkFrame(
        height=50,
        master=get_center_frame(),
    )

    top_frame.grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    _configure_top_frame_grid(frame=top_frame)
    _create_top_frame_widgets(master=top_frame)


def _get_flashcard() -> dict[str, Any]:
    """
    Returns the flashcard.

    Args:
        None

    Returns:
        dict[str, Any]: The flashcard.

    Raises:
        ValueError: If the flashcard is None.
    """

    if FLASHCARD is None:
        raise ValueError(
            "Flashcard is None. Please provide a flashcard to be rehearsed.",
            "",
        )

    return FLASHCARD


def _set_flashcard(flashcard: dict[str, Any]) -> None:
    """
    Sets the flashcard.

    Args:
        flashcard (dict[str, Any]): The flashcard to be rehearsed.

    Returns:
        None
    """

    global FLASHCARD

    FLASHCARD = flashcard


# ---------- Public Functions ---------- #


def get_flashcard_rehearsal_view(flashcard: dict[str, Any]) -> None:
    """
    Gets the flashcard rehearsal view of the application.

    Args:
        flashcard (dict[str, Any]): The flashcard to be rehearsed.

    Returns:
        None

    Raises:
        Exception: If any errors occur.
    """

    try:
        _set_flashcard(flashcard=flashcard)

        clear_center_frame()
        reset_center_frame_grid()
        _configure_grid()
        _create_widgets()
    except Exception as e:
        log_error(
            message=f"Caught an exception while attempting to get flashcard rehearsal view: {e}"
        )
        raise e


def set_flip_side(flip_side: Optional[Literal["back", "front"]] = "back") -> None:
    """
    Sets the flip side of the flashcard rehearsal view.

    Args:
        flip_side (Optional[Literal["back", "front"]], optional): The flip side to set. Defaults to "back".

    Returns:
        None
    """

    global FLIP_SIDE

    FLIP_SIDE = flip_side
