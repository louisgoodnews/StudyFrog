"""
Author: Louis Goodnews
Date: 2025-12-21
Description: The question rehearsal view of the application.
"""

import customtkinter as ctk

from tkinter.constants import NSEW
from typing import Any, Final, Literal, Optional

from gui.gui import get_center_frame
from models.models import Model
from utils.common import exists
from utils.gui import clear_center_frame, reset_center_frame_grid
from utils.logging import log_error, log_info


# ---------- Exports ---------- #

__all__: Final[list[str]] = ["get_question_rehearsal_view"]


# ---------- Constants ---------- #

_QUESTION: Optional[Model] = None
_SUBSCRIPTION_IDS: Final[list[str]] = []


# ---------- Helper Functions ---------- #


def _get_question() -> Model:
    """
    Returns the question.

    Args:
        None

    Returns:
        Model: The question.

    Raises:
        ValueError: If the question is None.
    """

    if not exists(value=_QUESTION):
        raise ValueError(
            "Question is None. Please provide a question to be rehearsed.",
            "",
        )

    return _QUESTION


def _set_question(question: Model) -> None:
    """
    Sets the question.

    Args:
        question (Model): The question to be rehearsed.

    Returns:
        None
    """

    global _QUESTION

    _QUESTION = question


# ---------- Private Functions ---------- #


def _configure_bottom_frame_grid(frame: ctk.CTkFrame) -> None:
    """
    Configures the grid configuration for the 'bottom' frame for the question rehearsal view.

    Args:
        frame (ctk.CTkFrame): The frame to configure the grid for.

    Returns:
        None
    """

    pass


def _configure_center_frame_grid(frame: ctk.CTkFrame) -> None:
    """
    Configures the grid configuration for the 'center' frame for the question rehearsal view.

    Args:
        frame (ctk.CTkFrame): The frame to configure the grid for.

    Returns:
        None
    """

    pass


def _configure_grid() -> None:
    """
    Configures the grid configuration for the question rehearsal view.

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
    Configures the grid configuration for the 'top' frame for the question rehearsal view.

    Args:
        frame (ctk.CTkFrame): The frame to configure the grid for.

    Returns:
        None
    """

    pass


def _create_bottom_frame_widgets(master: ctk.CTkFrame) -> None:
    """
    Creates the widgets for the 'bottom' frame for the question rehearsal view.

    Args:
        None

    Returns:
        None
    """

    pass


def _create_center_frame_widgets(master: ctk.CTkFrame) -> None:
    """
    Creates the widgets for the 'center' frame for the question rehearsal view.

    Args:
        None

    Returns:
        None
    """

    pass


def _create_top_frame_widgets(master: ctk.CTkFrame) -> None:
    """
    Creates the widgets for the 'top' frame for the question rehearsal view.

    Args:
        None

    Returns:
        None
    """

    pass


def _create_widgets() -> None:
    """
    Creates the widgets for the question rehearsal view.

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


def get_question_rehearsal_view(question: Model) -> None:
    """
    Gets the question rehearsal view of the application.

    Args:
        question (Model): The question to be rehearsed.

    Returns:
        None

    Raises:
        Exception: If any errors occur.
    """

    try:
        _set_question(question=question)

        clear_center_frame()
        reset_center_frame_grid()
        _configure_grid()
        _create_widgets()
    except Exception as e:
        log_error(
            message=f"Caught an exception while attempting to get question rehearsal view: {e}"
        )
        raise e
