"""
Author: Louis Goodnews
Date: 2025-12-10
"""

import customtkinter as ctk

from tkinter.constants import NSEW

from typing import Final, Optional

from constants.gui import WINDOW_GEOMETRY, WINDOW_TITLE


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "get_bottom_frame",
    "get_center_frame",
    "get_root",
    "get_top_frame",
]


# ---------- Constants ---------- #

_BOTTOM_FRAME: Optional[ctk.CTkFrame] = None

_CENTER_FRAME: Optional[ctk.CTkFrame] = None

_ROOT: Optional[ctk.CTk] = None

_TOP_FRAME: Optional[ctk.CTkFrame] = None


# ---------- Helper Functions ---------- #


def ensure_bottom_frame() -> ctk.CTkFrame:
    """
    Ensures that the bottom frame is created.

    Args:
        None

    Returns:
        ctk.CTkFrame: The bottom frame.
    """

    global _BOTTOM_FRAME

    if _BOTTOM_FRAME is not None:
        return _BOTTOM_FRAME

    _BOTTOM_FRAME = ctk.CTkFrame(
        height=25,
        master=ensure_root(),
    )

    _BOTTOM_FRAME.grid(
        column=0,
        padx=5,
        pady=5,
        row=2,
        sticky=NSEW,
    )

    return _BOTTOM_FRAME


def ensure_center_frame() -> ctk.CTkFrame:
    """
    Ensures that the center frame is created.

    Args:
        None

    Returns:
        ctk.CTkFrame: The center frame.
    """

    global _CENTER_FRAME

    if _CENTER_FRAME is not None:
        return _CENTER_FRAME

    _CENTER_FRAME = ctk.CTkFrame(
        master=ensure_root(),
    )

    _CENTER_FRAME.grid(
        column=0,
        padx=5,
        pady=5,
        row=1,
        sticky=NSEW,
    )

    return _CENTER_FRAME


def ensure_root() -> ctk.CTkFrame:
    """
    Ensure that the root window is created.

    Args:
        None

    Returns:
        ctk.CTkFrame: The root window.
    """

    global _ROOT

    if _ROOT is not None:
        return _ROOT

    _ROOT = ctk.CTk()

    _ROOT.geometry(WINDOW_GEOMETRY)
    _ROOT.title(WINDOW_TITLE)

    _ROOT.grid_columnconfigure(
        index=0,
        weight=1,
    )
    _ROOT.grid_rowconfigure(
        index=0,
        weight=0,
    )
    _ROOT.grid_rowconfigure(
        index=1,
        weight=1,
    )
    _ROOT.grid_rowconfigure(
        index=2,
        weight=0,
    )

    return _ROOT


def ensure_top_frame() -> ctk.CTkFrame:
    """
    Ensures that the top frame is created.

    Args:
        None

    Returns:
        ctk.CTkFrame: The top frame.
    """

    global _TOP_FRAME

    if _TOP_FRAME is not None:
        return _TOP_FRAME

    _TOP_FRAME = ctk.CTkFrame(
        height=50,
        master=ensure_root(),
    )

    _TOP_FRAME.grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    return _TOP_FRAME


# ---------- Functions ---------- #


def get_bottom_frame() -> ctk.CTkFrame:
    """
    Returns the bottom frame widget.

    Args:
        None

    Returns:
        ctk.CTkFrame: The bottom frame.
    """

    return ensure_bottom_frame()


def get_center_frame() -> ctk.CTkFrame:
    """
    Returns the center frame widget.

    Args:
        None

    Returns:
        ctk.CTkFrame: The center frame.
    """

    return ensure_center_frame()


def get_root() -> ctk.CTkFrame:
    """
    Returns the root window widget.

    Args:
        None

    Returns:
        ctk.CTkFrame: The root window.
    """

    return ensure_root()


def get_top_frame() -> ctk.CTkFrame:
    """
    Returns the top frame widget.

    Args:
        None

    Returns:
        ctk.CTkFrame: The top frame.
    """

    return ensure_top_frame()
