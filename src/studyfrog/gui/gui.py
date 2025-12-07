"""
Author: Louis Goodnews
Date: 2025-11-16
"""

import tkinter

from tkinter.constants import NSEW
from typing import Final, Optional

from gui.constants import COLOR_CONFIG, DARK_PRIMARY, WINDOW_GEOMETRY, WINDOW_TITLE
from gui.factory import get_color_mode, get_frame


# ---------- Constants ---------- #

BOTTOM_FRAME: Optional[tkinter.Frame] = None

CENTER_FRAME: Optional[tkinter.Frame] = None

MENU: Optional[tkinter.Menu] = None

EDIT_MENU: Optional[tkinter.Menu] = None

FILE_MENU: Optional[tkinter.Menu] = None

VIEW_MENU: Optional[tkinter.Menu] = None

ROOT: Optional[tkinter.Tk] = None

TOP_FRAME: Optional[tkinter.Frame] = None


# ---------- Functions ---------- #


def _none_root() -> None:
    """
    Sets the global ROOT variable to None.

    Args:
        None

    Returns:
        None
    """

    global ROOT

    if not ROOT:
        return

    ROOT.destroy()

    ROOT = None


def get_bottom_frame() -> tkinter.Frame:
    """
    Returns the 'bottom frame' tkinter.Frame widget.

    Args:
        None

    Returns:
        tkinter.Frame: The 'bottom frame' tkinter.Frame widget.def get_bottom_frame() -> tkinter.Frame:
    """

    global BOTTOM_FRAME

    if BOTTOM_FRAME is not None:
        return BOTTOM_FRAME

    BOTTOM_FRAME = get_frame(
        height=25,
        master=get_root(),
        **COLOR_CONFIG["frame"][get_color_mode()],
    )

    BOTTOM_FRAME.grid(
        column=0,
        padx=5,
        pady=5,
        row=2,
        sticky=NSEW,
    )

    return BOTTOM_FRAME


def get_bottom_frame_height() -> int:
    """
    Returns the height of the bottom frame.

    Args:
        None

    Returns:
        int: The height of the bottom frame.
    """

    get_bottom_frame().update_idletasks()

    return get_bottom_frame().winfo_height()


def get_bottom_frame_width() -> int:
    """
    Returns the width of the bottom frame.

    Args:
        None

    Returns:
        int: The width of the bottom frame.
    """

    get_bottom_frame().update_idletasks()

    return get_bottom_frame().winfo_width()


def get_center_frame() -> tkinter.Frame:
    """
    Returns the 'center frame' tkinter.Frame widget.

    Args:
        None

    Returns:
        tkinter.Frame: The 'center frame' tkinter.Frame widget.
    """

    global CENTER_FRAME

    if CENTER_FRAME is not None:
        return CENTER_FRAME

    CENTER_FRAME = get_frame(
        master=get_root(),
        **COLOR_CONFIG["frame"][get_color_mode()],
    )

    CENTER_FRAME.grid(
        column=0,
        padx=5,
        pady=5,
        row=1,
        sticky=NSEW,
    )

    return CENTER_FRAME


def get_center_frame_height() -> int:
    """
    Returns the height of the center frame.

    Args:
        None

    Returns:
        int: The height of the center frame.
    """

    get_center_frame().update_idletasks()

    return get_center_frame().winfo_height()


def get_center_frame_width() -> int:
    """
    Returns the width of the center frame.

    Args:
        None

    Returns:
        int: The width of the center frame.
    """

    get_center_frame().update_idletasks()

    return get_center_frame().winfo_width()


def get_edit_menu() -> tkinter.Menu:
    """
    Returns the 'edit menu' tkinter.Menu widget.

    Args:
        None

    Returns:
        tkinter.Menu: The 'edit menu' tkinter.Menu widget.
    """

    global EDIT_MENU

    if EDIT_MENU is not None:
        return EDIT_MENU

    EDIT_MENU = tkinter.Menu(
        master=get_menu(),
        **COLOR_CONFIG["menu"][get_color_mode()],
    )

    get_menu().add_cascade(
        background=COLOR_CONFIG["menu"][get_color_mode()]["background"],
        foreground=COLOR_CONFIG["menu"][get_color_mode()]["foreground"],
        label="Edit",
        menu=EDIT_MENU,
    )

    return EDIT_MENU


def get_file_menu() -> tkinter.Menu:
    """
    Returns the 'file menu' tkinter.Menu widget.

    Args:
        None

    Returns:
        tkinter.Menu: The 'file menu' tkinter.Menu widget.
    """

    global FILE_MENU

    if FILE_MENU is not None:
        return FILE_MENU

    FILE_MENU = tkinter.Menu(
        master=get_menu(),
        **COLOR_CONFIG["menu"][get_color_mode()],
    )

    get_menu().add_cascade(
        background=COLOR_CONFIG["menu"][get_color_mode()]["background"],
        foreground=COLOR_CONFIG["menu"][get_color_mode()]["foreground"],
        label="File",
        menu=FILE_MENU,
    )

    return FILE_MENU


def get_menu() -> tkinter.Menu:
    """
    Returns the tkinter.Menu widget.

    Args:
        None

    Returns:
        tkinter.Menu: The tkinter.Menu widget.
    """

    global MENU

    if MENU is not None:
        return MENU

    MENU = tkinter.Menu(
        master=get_root(),
        **COLOR_CONFIG["menu"][get_color_mode()],
    )

    get_root().configure(menu=MENU)

    return MENU


def get_root() -> tkinter.Tk:
    """
    Returns the root window tkinter.Tk widget.

    Args:
        None

    Returns:
        tkinter.Tk: The root window tkinter.Tk widget.
    """

    global ROOT

    if ROOT is not None:
        return ROOT

    ROOT = tkinter.Tk()

    ROOT.configure(**COLOR_CONFIG["window"][get_color_mode()])

    ROOT.geometry(newGeometry=WINDOW_GEOMETRY)

    ROOT.title(string=WINDOW_TITLE)

    ROOT.grid_columnconfigure(
        index=0,
        weight=1,
    )

    ROOT.grid_rowconfigure(
        index=0,
        weight=0,
    )

    ROOT.grid_rowconfigure(
        index=1,
        weight=1,
    )

    ROOT.grid_rowconfigure(
        index=2,
        weight=0,
    )

    ROOT.protocol(
        name="WM_DELETE_WINDOW",
        func=_none_root,
    )

    return ROOT


def get_root_height() -> int:
    """
    Returns the height of the root window.

    Args:
        None

    Returns:
        int: The height of the root window.
    """

    get_root().update_idletasks()

    return get_root().winfo_height()


def get_root_width() -> int:
    """
    Returns the width of the root window.

    Args:
        None

    Returns:
        int: The width of the root window.
    """

    get_root().update_idletasks()

    return get_root().winfo_width()


def get_top_frame() -> tkinter.Frame:
    """
    Returns the 'top frame' tkinter.Frame widget.

    Args:
        None

    Returns:
        tkinter.Frame: The 'top frame' tkinter.Frame widget.
    """

    global TOP_FRAME

    if TOP_FRAME is not None:
        return TOP_FRAME

    TOP_FRAME = get_frame(
        height=50,
        master=get_root(),
        **COLOR_CONFIG["frame"][get_color_mode()],
    )

    TOP_FRAME.configure(
        background=DARK_PRIMARY,
        bg=DARK_PRIMARY,
    )

    TOP_FRAME.grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    return TOP_FRAME


def get_top_frame_height() -> int:
    """
    Returns the height of the top frame.

    Args:
        None

    Returns:
        int: The height of the top frame.
    """

    get_top_frame().update_idletasks()

    return get_top_frame().winfo_height()


def get_top_frame_width() -> int:
    """
    Returns the width of the top frame.

    Args:
        None

    Returns:
        int: The width of the top frame.
    """

    get_top_frame().update_idletasks()

    return get_top_frame().winfo_width()


def get_view_menu() -> tkinter.Menu:
    """
    Returns the 'view menu' tkinter.Menu widget.

    Args:
        None

    Returns:
        tkinter.Menu: The 'view menu' tkinter.Menu widget.
    """

    global VIEW_MENU

    if VIEW_MENU is not None:
        return VIEW_MENU

    VIEW_MENU = tkinter.Menu(
        master=get_menu(),
        **COLOR_CONFIG["menu"][get_color_mode()],
    )

    get_menu().add_cascade(
        background=COLOR_CONFIG["menu"][get_color_mode()]["background"],
        foreground=COLOR_CONFIG["menu"][get_color_mode()]["foreground"],
        label="View",
        menu=VIEW_MENU,
    )

    return VIEW_MENU


def is_root_active() -> bool:
    """
    Returns whether the root window is active.

    Args:
        None

    Returns:
        bool: True if the root window is active, False otherwise.
    """

    return ROOT is not None


def make_root_none_if_possible() -> None:
    """
    Sets the global ROOT variable to None if the root window is active.

    Args:
        None

    Returns:
        None
    """

    global ROOT

    if ROOT.winfo_exists():
        return

    ROOT = None


# ---------- Auto-Export ---------- #

# Auto-export all non-private symbols
__all__: Final[list[str]] = [
    key
    for (
        key,
        value,
    ) in globals().items()
    if not key.startswith("_") and not callable(value)
]
