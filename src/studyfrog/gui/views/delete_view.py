"""
Author: Louis Goodnews
Date: 2025-11-16
"""

import tkinter

from tkinter.constants import NSEW
from typing import Final, Literal, Optional

from gui.constants import TOPLEVEL_GEOMETRY
from gui.factory import get_frame
from utils.utils import destroy_widget_children


# ---------- Constants ---------- #

BOTTOM_FRAME: Optional[tkinter.Frame] = None

CENTER_FRAME: Optional[tkinter.Frame] = None

MASTER: Optional[tkinter.Toplevel] = None

NAME: Final[Literal["gui.views.views.delete_view"]] = "gui.views.views.delete_view"

TOP_FRAME: Optional[tkinter.Frame] = None


# ---------- Functions ---------- #


def clear_bottom_frame() -> None:
    """
    Clears the bottom frame.

    Args:
        None

    Returns:
        None
    """

    try:
        destroy_widget_children(get_bottom_frame())
    except Exception as e:
        raise e


def clear_center_frame() -> None:
    """
    Clears the center frame.

    Args:
        None

    Returns:
        None
    """

    try:
        destroy_widget_children(get_center_frame())
    except Exception as e:
        raise e


def clear_top_frame() -> None:
    """
    Clears the top frame.

    Args:
        None

    Returns:
        None
    """

    try:
        destroy_widget_children(get_top_frame())
    except Exception as e:
        raise e


def clear_widgets() -> None:
    """
    Clears all widgets.

    Args:
        None

    Returns:
        None
    """

    try:
        clear_bottom_frame()
        clear_center_frame()
        clear_top_frame()
    except Exception as e:
        raise e


def configure_bottom_frame_grid() -> None:
    """
    Configures the bottom frame grid.

    Args:
        None

    Returns:
        None
    """

    try:
        pass
    except Exception as e:
        raise e


def configure_center_frame_grid() -> None:
    """
    Configures the center frame grid.

    Args:
        None

    Returns:
        None
    """

    try:
        pass
    except Exception as e:
        raise e


def configure_grid() -> None:
    """
    Configures the grid.

    Args:
        None

    Returns:
        None
    """

    try:
        configure_bottom_frame_grid()
        configure_center_frame_grid()
        configure_top_frame_grid()
    except Exception as e:
        raise e


def configure_top_frame_grid() -> None:
    """
    Configures the top frame grid.

    Args:
        None

    Returns:
        None
    """

    try:
        pass
    except Exception as e:
        raise e


def create_bottom_frame_widgets(master: tkinter.Frame) -> None:
    """
    Creates the bottom frame widgets.

    Args:
        master (tkinter.Frame): The master frame.

    Returns:
        None
    """

    try:
        pass
    except Exception as e:
        raise e


def create_center_frame_widgets(master: tkinter.Frame) -> None:
    """
    Creates the center frame widgets.

    Args:
        master (tkinter.Frame): The master frame.

    Returns:
        None
    """

    try:
        pass
    except Exception as e:
        raise e


def create_top_frame_widgets(master: tkinter.Frame) -> None:
    """
    Creates the top frame widgets.

    Args:
        master (tkinter.Frame): The master frame.

    Returns:
        None
    """

    try:
        pass
    except Exception as e:
        raise e


def create_widgets() -> None:
    """
    Creates all widgets.

    Args:
        None

    Returns:
        None
    """

    try:
        create_bottom_frame_widgets(master=get_bottom_frame())
        create_center_frame_widgets(master=get_center_frame())
        create_top_frame_widgets(master=get_top_frame())
    except Exception as e:
        raise e


def get_bottom_frame() -> tkinter.Frame:
    """
    Returns the bottom frame.

    Args:
        None

    Returns:
        tkinter.Frame: The bottom frame.
    """

    global BOTTOM_FRAME

    if BOTTOM_FRAME is not None:
        return BOTTOM_FRAME

    BOTTOM_FRAME = get_frame(master=get_master())

    BOTTOM_FRAME.grid(
        column=0,
        padx=5,
        pady=5,
        row=2,
        sticky=NSEW,
    )

    return BOTTOM_FRAME


def get_center_frame() -> tkinter.Frame:
    """
    Returns the center frame.

    Args:
        None

    Returns:
        tkinter.Frame: The center frame.
    """

    global CENTER_FRAME

    if CENTER_FRAME is not None:
        return CENTER_FRAME

    CENTER_FRAME = get_frame(master=get_master())

    CENTER_FRAME.grid(
        column=0,
        padx=5,
        pady=5,
        row=1,
        sticky=NSEW,
    )

    return CENTER_FRAME


def get_delete_view(master: tkinter.Toplevel) -> None:
    """
    Returns the delete view.

    Args:
        master (tkinter.Toplevel): The master window.

    Returns:
        None
    """

    try:
        set_master(master=master)
        clear_widgets()
        create_widgets()
        configure_grid()
    except Exception as e:
        raise e


def get_master() -> tkinter.Toplevel:
    """
    Returns the master of the delete view.

    Args:
        None

    Returns:
        tkinter.Toplevel: The master window.

    Raises:
        ValueError: If the master is not set. Call 'set_master' first.
    """

    global MASTER

    if MASTER is None:
        raise ValueError("Master not set. Call 'set_master' first.")

    return MASTER


def get_top_frame() -> tkinter.Frame:
    """
    Returns the top frame.

    Args:
        None

    Returns:
        tkinter.Frame: The top frame.
    """

    global TOP_FRAME

    if TOP_FRAME is not None:
        return TOP_FRAME

    TOP_FRAME = get_frame(master=get_master())

    TOP_FRAME.grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    return TOP_FRAME


def set_master(master: tkinter.Toplevel) -> None:
    """
    Sets the master of the delete view.

    Args:
        master (tkinter.Toplevel): The master window.

    Returns:
        None
    """

    global MASTER

    MASTER = master

    master.geometry(newGeometry=TOPLEVEL_GEOMETRY)

    MASTER.grid_columnconfigure(
        index=0,
        weight=1,
    )

    MASTER.grid_rowconfigure(
        index=0,
        weight=0,
    )

    MASTER.grid_rowconfigure(
        index=1,
        weight=1,
    )

    MASTER.grid_rowconfigure(
        index=2,
        weight=0,
    )


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
