"""
Author: Louis Goodnews
Date: 2025-12-21
Description: The note rehearsal view of the application.
"""

import customtkinter as ctk

from tkinter.constants import DISABLED, NSEW
from typing import Any, Final, Literal, Optional

from gui.gui import get_center_frame
from utils.gui import clear_center_frame, reset_center_frame_grid
from utils.logging import log_error, log_info


# ---------- Exports ---------- #

__all__: Final[list[str]] = ["get_note_rehearsal_view"]


# ---------- Constants ---------- #

NOTE: Optional[dict[str, Any]] = None

FLIP_SIDE: Literal["front", "back"] = "front"

SUBSCRIPTION_IDS: Final[list[str]] = []


# ---------- Helper Functions ---------- #


# ---------- Private Functions ---------- #


def _configure_bottom_frame_grid(frame: ctk.CTkFrame) -> None:
    """
    Configures the grid configuration for the 'bottom' frame for the note rehearsal view.

    Args:
        frame (ctk.CTkFrame): The frame to configure the grid for.

    Returns:
        None
    """

    pass


def _configure_center_frame_grid(frame: ctk.CTkFrame) -> None:
    """
    Configures the grid configuration for the 'center' frame for the note rehearsal view.

    Args:
        frame (ctk.CTkFrame): The frame to configure the grid for.

    Returns:
        None
    """

    pass


def _configure_grid() -> None:
    """
    Configures the grid configuration for the note rehearsal view.

    Args:
        None

    Returns:
        None
    """

    get_center_frame().grid_columnconfigure(
        0,
        weight=1,
    )
    get_center_frame().grid_rowconfigure(
        0,
        weight=0,
    )
    get_center_frame().grid_rowconfigure(
        1,
        weight=1,
    )
    get_center_frame().grid_rowconfigure(
        2,
        weight=0,
    )


def _configure_top_frame_grid(frame: ctk.CTkFrame) -> None:
    """
    Configures the grid configuration for the 'top' frame for the note rehearsal view.

    Args:
        frame (ctk.CTkFrame): The frame to configure the grid for.

    Returns:
        None
    """

    pass


def _create_bottom_frame_widgets(master: ctk.CTkFrame) -> None:
    """
    Creates the widgets for the 'bottom' frame for the note rehearsal view.

    Args:
        None

    Returns:
        None
    """

    pass


def _create_center_frame_widgets(master: ctk.CTkFrame) -> None:
    """
    Creates the widgets for the 'center' frame for the note rehearsal view.

    Args:
        None

    Returns:
        None
    """

    ctk.CTkLabel(
        master=master,
        text=_get_note()["title"],
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    textbox: ctk.CTkTextbox = ctk.CTkTextbox(
        master=master,
        state=DISABLED,
    )

    textbox.grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    textbox.insert(
        index="1.0",
        text=_get_note()["text"],
    )


def _create_top_frame_widgets(master: ctk.CTkFrame) -> None:
    """
    Creates the widgets for the 'top' frame for the note rehearsal view.

    Args:
        None

    Returns:
        None
    """

    pass


def _create_widgets() -> None:
    """
    Creates the widgets for the note rehearsal view.

    Args:
        None

    Returns:
        None
    """

    bottom_frame: ctk.CTkFrame = ctk.CTkFrame(master=get_center_frame())

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

    top_frame: ctk.CTkFrame = ctk.CTkFrame(master=get_center_frame())

    top_frame.grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    _configure_top_frame_grid(frame=top_frame)
    _create_top_frame_widgets(master=top_frame)


def _get_note() -> dict[str, Any]:
    """
    Returns the note.

    Args:
        None

    Returns:
        dict[str, Any]: The note.

    Raises:
        ValueError: If the note is None.
    """

    if NOTE is None:
        raise ValueError(
            "Note is None. Please provide a note to be rehearsed.",
            "",
        )

    return NOTE


def _set_note(note: dict[str, Any]) -> None:
    """
    Sets the note.

    Args:
        note (dict[str, Any]): The note to be rehearsed.

    Returns:
        None
    """

    global NOTE

    NOTE = note


# ---------- Public Functions ---------- #


def get_note_rehearsal_view(note: dict[str, Any]) -> None:
    """
    Gets the note rehearsal view of the application.

    Args:
        note (dict[str, Any]): The note to be rehearsed.

    Returns:
        None

    Raises:
        Exception: If any errors occur.
    """

    try:
        _set_note(note=note)

        clear_center_frame()
        reset_center_frame_grid()
        _configure_grid()
        _create_widgets()
    except Exception as e:
        log_error(message=f"Caught an exception while attempting to get note rehearsal view: {e}")
        raise e
