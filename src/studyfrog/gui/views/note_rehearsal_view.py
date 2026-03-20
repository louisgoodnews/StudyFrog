"""
Author: Louis Goodnews
Date: 2025-12-21
Description: The note rehearsal view of the application.
"""

from __future__ import annotations

import customtkinter as ctk

from tkinter.constants import DISABLED, NSEW
from typing import Any, Final, Optional

from studyfrog.gui.gui import get_center_frame
from studyfrog.models.models import Model
from studyfrog.utils.common import exists
from studyfrog.utils.gui import clear_center_frame, reset_center_frame_grid
from studyfrog.utils.logging import log_error, log_info


# ---------- Exports ---------- #

__all__: Final[list[str]] = ["get_note_rehearsal_view"]


# ---------- Constants ---------- #

_NOTE: Optional[Model] = None
_SUBSCRIPTION_IDS: Final[list[str]] = []


# ---------- Helper Functions ---------- #


def _get_note() -> Model:
    """
    Returns the note.

    Args:
        None

    Returns:
        Model: The note.

    Raises:
        ValueError: If the note is None.
    """

    if not exists(value=_NOTE):
        raise ValueError(
            "Note is None. Please provide a note to be rehearsed.",
            "",
        )

    return _NOTE


def _get_note_dict() -> dict[str, Any]:
    """
    Returns the note as a dictionary.

    Args:
        None

    Returns:
        dict[str, Any]: The note as a dictionary.

    Raises:
        ValueError: If the note is None.
    """

    if not exists(value=_NOTE):
        raise ValueError(
            "Note is None. Please provide a note to be rehearsed.",
            "",
        )

    return _get_note().to_dict()


def _set_note(note: Model) -> None:
    """
    Sets the note.

    Args:
        note (Model): The note to be rehearsed.

    Returns:
        None
    """

    global _NOTE

    _NOTE = note


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


# ---------- Public Functions ---------- #


def get_note_rehearsal_view(note: Model) -> None:
    """
    Gets the note rehearsal view of the application.

    Args:
        note (Model): The note to be rehearsed.

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
