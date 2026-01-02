"""
Author: Louis Goodnews
Date: 2025-12-10
"""

import tkinter as tk

from typing import Final

from gui.gui import get_bottom_frame, get_center_frame, get_top_frame


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "clear_center_frame",
    "clear_bottom_frame",
    "clear_frames",
    "clear_top_frame",
    "count_widget_children",
    "destroy_widget_children",
    "get_widget_children",
    "reset_bottom_frame_grid",
    "reset_center_frame_grid",
    "reset_frame_grids",
    "reset_top_frame_grid",
]


# ---------- Functions ---------- #


def clear_bottom_frame() -> None:
    """
    Destroys all child widgets contained within the application's bottom frame.

    Args:
        None

    Returns:
        None
    """

    destroy_widget_children(widget=get_bottom_frame())


def clear_center_frame() -> None:
    """
    Destroys all child widgets contained within the application's center frame.

    Args:
        None

    Returns:
        None
    """

    destroy_widget_children(widget=get_center_frame())


def clear_frames() -> None:
    """
    Destroys all child widgets contained within the application's 'bottom', 'center' and 'top' frames.

    Args:
        None

    Returns:
        None
    """

    clear_bottom_frame()
    clear_center_frame()
    clear_top_frame()


def clear_top_frame() -> None:
    """
    Destroys all child widgets contained within the application's top frame.

    Args:
        None

    Returns:
        None
    """

    destroy_widget_children(widget=get_top_frame())


def count_widget_children(widget: tk.Widget) -> int:
    """
    Counts the number of children of a tkinter widget.

    Args:
        widget (tk.Widget): The tkinter widget to count children from.

    Returns:
        int: The number of children of the tkinter widget.
    """

    return len(get_widget_children(widget=widget))


def destroy_widget_children(widget: tk.Widget) -> None:
    """
    Destroys all children of a tkinter widget.

    Args:
        widget (tk.Widget): The tkinter widget to destroy children from.

    Returns:
        None
    """

    for child in get_widget_children(widget=widget):
        child.destroy()


def get_widget_children(widget: tk.Widget) -> list[tk.Widget]:
    """
    Returns a list of all children of a tkinter widget.

    Args:
        widget (tk.Widget): The tkinter widget to get children from.

    Returns:
        list[tk.Widget]: A list of all children of the tkinter widget.
    """

    return widget.winfo_children()


def reset_bottom_frame_grid() -> None:
    """
    Resets the grid configuration of the 'bottom' frame of the application.

    Args:
        None

    Returns:
        None
    """

    (
        columns,
        rows,
    ) = get_bottom_frame().grid_size()

    for column in range(columns):
        get_bottom_frame().grid_columnconfigure(
            index=column,
            weight=0,
        )

    for row in range(rows):
        get_bottom_frame().grid_rowconfigure(
            index=row,
            weight=0,
        )


def reset_center_frame_grid() -> None:
    """
    Resets the grid configuration of the 'center' frame of the application.

    Args:
        None

    Returns:
        None
    """

    (
        columns,
        rows,
    ) = get_center_frame().grid_size()

    for column in range(columns):
        get_center_frame().grid_columnconfigure(
            index=column,
            weight=0,
        )

    for row in range(rows):
        get_center_frame().grid_rowconfigure(
            index=row,
            weight=0,
        )


def reset_frame_grids() -> None:
    """
    Resets the grid configurations of the 'bottom', 'center' and 'top' frames of the application.

    Args:
        None

    Returns:
        None
    """

    reset_bottom_frame_grid()
    reset_center_frame_grid()
    reset_top_frame_grid()


def reset_top_frame_grid() -> None:
    """
    Resets the grid configuration of the 'top' frame of the application.

    Args:
        None

    Returns:
        None
    """

    (
        columns,
        rows,
    ) = get_top_frame().grid_size()

    for column in range(columns):
        get_top_frame().grid_columnconfigure(
            index=column,
            weight=0,
        )

    for row in range(rows):
        get_top_frame().grid_rowconfigure(
            index=row,
            weight=0,
        )
