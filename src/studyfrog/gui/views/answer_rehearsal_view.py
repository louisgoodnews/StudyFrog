"""
Author: Louis Goodnews
Date: 2025-12-21
Description: The answer rehearsal view of the application.
"""

import customtkinter as ctk

from tkinter.constants import NSEW
from typing import Any, Final, Optional

from gui.gui import get_center_frame
from utils.gui import clear_center_frame, reset_center_frame_grid
from utils.logging import log_error, log_info


# ---------- Exports ---------- #

__all__: Final[list[str]] = ["get_answer_rehearsal_view"]


# ---------- Constants ---------- #

ANSWER: Optional[dict[str, Any]] = None

SUBSCRIPTION_IDS: Final[list[str]] = []


# ---------- Helper Functions ---------- #


# ---------- Private Functions ---------- #


def _configure_bottom_frame_grid(frame: ctk.CTkFrame) -> None:
    """
    Configures the grid configuration for the 'bottom' frame for the answer rehearsal view.

    Args:
        frame (ctk.CTkFrame): The frame to configure the grid for.

    Returns:
        None
    """

    pass


def _configure_center_frame_grid(frame: ctk.CTkFrame) -> None:
    """
    Configures the grid configuration for the 'center' frame for the answer rehearsal view.

    Args:
        frame (ctk.CTkFrame): The frame to configure the grid for.

    Returns:
        None
    """

    pass


def _configure_grid() -> None:
    """
    Configures the grid configuration for the answer rehearsal view.

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
    Configures the grid configuration for the 'top' frame for the answer rehearsal view.

    Args:
        frame (ctk.CTkFrame): The frame to configure the grid for.

    Returns:
        None
    """

    pass


def _create_bottom_frame_widgets(master: ctk.CTkFrame) -> None:
    """
    Creates the widgets for the 'bottom' frame for the answer rehearsal view.

    Args:
        None

    Returns:
        None
    """

    pass


def _create_center_frame_widgets(master: ctk.CTkFrame) -> None:
    """
    Creates the widgets for the 'center' frame for the answer rehearsal view.

    Args:
        None

    Returns:
        None
    """

    pass


def _create_top_frame_widgets(master: ctk.CTkFrame) -> None:
    """
    Creates the widgets for the 'top' frame for the answer rehearsal view.

    Args:
        None

    Returns:
        None
    """

    pass


def _create_widgets() -> None:
    """
    Creates the widgets for the answer rehearsal view.

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


def _get_answer() -> dict[str, Any]:
    """
    Returns the answer.

    Args:
        None

    Returns:
        dict[str, Any]: The answer.

    Raises:
        ValueError: If the answer is None.
    """

    if ANSWER is None:
        raise ValueError(
            "Answer is None. Please provide a answer to be rehearsed.",
            "",
        )

    return ANSWER


def _set_answer(answer: dict[str, Any]) -> None:
    """
    Sets the answer.

    Args:
        answer (dict[str, Any]): The answer to be rehearsed.

    Returns:
        None
    """

    global ANSWER

    ANSWER = answer


# ---------- Public Functions ---------- #


def get_answer_rehearsal_view(answer: dict[str, Any]) -> None:
    """
    Gets the answer rehearsal view of the application.

    Args:
        answer (dict[str, Any]): The answer to be rehearsed.

    Returns:
        None

    Raises:
        Exception: If any errors occur.
    """

    try:
        _set_answer(answer=answer)

        clear_center_frame()
        reset_center_frame_grid()
        _configure_grid()
        _create_widgets()
    except Exception as e:
        log_error(message=f"Caught an exception while attempting to get answer rehearsal view: {e}")
        raise e
