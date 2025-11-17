"""
Author: Louis Goodnews
Date: 2025-11-16
"""

import tkinter

from typing import Final, Literal

from gui.constants import COLOR_CONFIG


# ---------- Constants ---------- #

COLOR_MODE: Final[Literal["dark", "light"]] = "dark"


# ---------- Functions ---------- #


def get_color_mode() -> Literal[
    "dark",
    "light",
]:
    """
    Returns the color mode.

    Args:
        None

    Returns:
        Literal["dark", "light"]: The color mode.
    """

    global COLOR_MODE

    return COLOR_MODE


def get_frame(
    master: tkinter.Widget,
    *args,
    **kwargs,
) -> tkinter.Frame:
    """
    Returns a tkinter.Frame widget.

    Args:
        master (tkinter.Widget): The master of the tkinter.Frame widget to be created.
        *args: Additional arguments passed to the tkinter.Frame constructor.
        **kwargs: Additional keyword arguments passed to the tkinter.Frame constructor.

    Returns:
        tkinter.Frame: The tkinter.Frame widget.
    """

    if not kwargs:
        kwargs.update(COLOR_CONFIG["frame"][get_color_mode()])

    return tkinter.Frame(
        master=master,
        *args,
        **kwargs,
    )


def set_color_mode(
    color_mode: Literal[
        "dark",
        "light",
    ] = "dark",
) -> None:
    """
    Sets the color mode.

    Args:
        color_mode (Literal["dark", "light"]): The color mode.

    Returns:
        None
    """

    global COLOR_MODE

    COLOR_MODE = color_mode


# ---------- Auto-Export ---------- #

# Auto-export all non-private symbols
__all__: Final[list[str]] = [
    key
    for (
        key,
        value,
    ) in globals().items()
    if not key.startswith("_") and callable(value)
]
