"""
Author: Louis Goodnews
Date: 2025-11-16
"""

import tkinter

from tkinter.constants import NSEW
from typing import Final, Literal, Optional

from gui.factory import get_button, get_scrolled_frame
from gui.gui import get_bottom_frame, get_center_frame, get_top_frame
from gui.views.logic.dashboard_view_logic import (
    on_create_button_click,
    on_delete_button_click,
    on_edit_button_click,
    on_view_button_click,
)
from utils.utils import destroy_widget_children, log_exception, log_info


# ---------- Constants ---------- #

CONTAINER: Optional[tkinter.Frame] = None

NAME: Final[Literal["gui.views.views.dashboard_view"]] = "gui.views.views.dashboard_view"


# ---------- Functions ---------- #


def clear_bottom_frame() -> None:
    """
    Clears the bottom frame.

    Args:
        None

    Returns:
        None
    """

    global NAME

    try:
        destroy_widget_children(get_bottom_frame())
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to clear bottom frame",
            name=NAME,
        )
        raise e


def clear_center_frame() -> None:
    """
    Clears the center frame.

    Args:
        None

    Returns:
        None
    """

    global NAME

    try:
        destroy_widget_children(get_center_frame())
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to clear center frame",
            name=NAME,
        )
        raise e


def clear_top_frame() -> None:
    """
    Clears the top frame.

    Args:
        None

    Returns:
        None
    """

    global NAME

    try:
        destroy_widget_children(get_top_frame())
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to clear top frame",
            name=NAME,
        )
        raise e


def clear_widgets() -> None:
    """
    Clears all widgets.

    Args:
        None

    Returns:
        None
    """

    global NAME

    try:
        clear_bottom_frame()
        clear_center_frame()
        clear_top_frame()
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to clear all widgets",
            name=NAME,
        )
        raise e


def configure_bottom_frame_grid() -> None:
    """
    Configures the bottom frame grid.

    Args:
        None

    Returns:
        None
    """

    global NAME

    try:
        get_bottom_frame().grid_columnconfigure(
            index=0,
            weight=1,
        )
        get_bottom_frame().grid_rowconfigure(
            index=0,
            weight=1,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to configure bottom frame grid",
            name=NAME,
        )
        raise e


def configure_center_frame_grid() -> None:
    """
    Configures the center frame grid.

    Args:
        None

    Returns:
        None
    """

    global NAME

    try:
        get_center_frame().grid_columnconfigure(
            index=0,
            weight=1,
        )
        get_center_frame().grid_rowconfigure(
            index=0,
            weight=1,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to configure center frame grid",
            name=NAME,
        )
        raise e


def configure_grid() -> None:
    """
    Configures the grid.

    Args:
        None

    Returns:
        None
    """

    global NAME

    try:
        configure_bottom_frame_grid()
        configure_center_frame_grid()
        configure_top_frame_grid()
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to configure grid",
            name=NAME,
        )
        raise e


def configure_top_frame_grid() -> None:
    """
    Configures the top frame grid.

    Args:
        None

    Returns:
        None
    """

    global NAME

    try:
        get_top_frame().grid_columnconfigure(
            index=0,
            weight=1,
        )
        get_top_frame().grid_rowconfigure(
            index=0,
            weight=1,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to configure top frame grid",
            name=NAME,
        )
        raise e


def create_bottom_frame_widgets(master: tkinter.Frame) -> None:
    """
    Creates the bottom frame widgets.

    Args:
        master (tkinter.Frame): The master frame.

    Returns:
        None
    """

    global NAME

    try:
        pass
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to create bottom frame widgets",
            name=NAME,
        )
        raise e


def create_center_frame_widgets(master: tkinter.Frame) -> None:
    """
    Creates the center frame widgets.

    Args:
        master (tkinter.Frame): The master frame.

    Returns:
        None
    """

    global NAME

    try:
        scrolled_frame: dict[str, tkinter.Widget] = get_scrolled_frame(master=master)

        scrolled_frame["root"].grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        set_container(frame=scrolled_frame["container"])
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to create center frame widgets",
            name=NAME,
        )
        raise e


def create_top_frame_widgets(master: tkinter.Frame) -> None:
    """
    Creates the top frame widgets.

    Args:
        master (tkinter.Frame): The master frame.

    Returns:
        None
    """

    global NAME

    try:
        get_button(
            command=on_create_button_click,
            master=master,
            text="Create",
        ).grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to create top frame widgets",
            name=NAME,
        )
        raise e


def create_widgets() -> None:
    """
    Creates all widgets.

    Args:
        None

    Returns:
        None
    """

    global NAME

    try:
        create_bottom_frame_widgets(master=get_bottom_frame())
        create_center_frame_widgets(master=get_center_frame())
        create_top_frame_widgets(master=get_top_frame())
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to create all widgets",
            name=NAME,
        )
        raise e


def get_container() -> tkinter.Frame:
    """
    Returns the container frame for the dashboard view.

    Args:
        None

    Returns:
        tkinter.Frame: The container frame.

    Raises:
        ValueError: If the container has not been set.
    """

    global CONTAINER

    if CONTAINER is None:
        raise ValueError("Container not set. Call 'set_container' first.")

    return CONTAINER


def get_dashboard_view() -> None:
    """
    Returns the dashboard view.

    Args:
        None

    Returns:
        None
    """

    global NAME

    try:
        log_info(
            message="Getting dashboard view",
            name=NAME,
        )

        clear_widgets()
        create_widgets()
        configure_grid()

        log_info(
            message="Got dashboard view successfully",
            name=NAME,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get dashboard view",
            name=NAME,
        )
        raise e


def set_container(frame: tkinter.Frame) -> None:
    """
    Sets the container frame for the dashboard view.

    Args:
        frame (tkinter.Frame): The frame to set as the container.

    Returns:
        None
    """

    global CONTAINER

    CONTAINER = frame


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
