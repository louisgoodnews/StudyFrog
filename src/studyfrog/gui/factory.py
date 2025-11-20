"""
Author: Louis Goodnews
Date: 2025-11-16
"""

import tkinter

from tkinter.constants import ALL, NSEW, NW, VERTICAL
from typing import Final, Literal, Optional

from gui.constants import COLOR_CONFIG
from utils.utils import is_dict_empty

# ---------- Constants ---------- #

COLOR_MODE: Literal["dark", "light"] = "dark"


# ---------- Functions ---------- #


def get_button(
    master: tkinter.Widget,
    *args,
    **kwargs,
) -> tkinter.Button:
    """
    Returns a tkinter.Button widget.

    Args:
        master (tkinter.Widget): The master of the tkinter.Button widget to be created.
        *args: Additional arguments passed to the tkinter.Button constructor.
        **kwargs: Additional keyword arguments passed to the tkinter.Button constructor.

    Returns:
        tkinter.Button: The tkinter.Button widget.
    """

    if is_dict_empty(dictionary=kwargs):
        kwargs.update(COLOR_CONFIG["button"][get_color_mode()])

    return tkinter.Button(
        master=master,
        *args,
        **kwargs,
    )


def get_canvas(
    master: tkinter.Widget,
    *args,
    **kwargs,
) -> tkinter.Canvas:
    """
    Returns a tkinter.Canvas widget.

    Args:
        master (tkinter.Widget): The master of the tkinter.Canvas widget to be created.
        *args: Additional arguments passed to the tkinter.Canvas constructor.
        **kwargs: Additional keyword arguments passed to the tkinter.Canvas constructor.

    Returns:
        tkinter.Canvas: The tkinter.Canvas widget.
    """

    if is_dict_empty(dictionary=kwargs):
        kwargs.update(COLOR_CONFIG["canvas"][get_color_mode()])

    return tkinter.Canvas(
        master=master,
        *args,
        **kwargs,
    )


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

    if is_dict_empty(dictionary=kwargs):
        kwargs.update(COLOR_CONFIG["frame"][get_color_mode()])

    return tkinter.Frame(
        master=master,
        *args,
        **kwargs,
    )


def get_label(
    master: tkinter.Widget,
    *args,
    **kwargs,
) -> tkinter.Label:
    """
    Returns a tkinter.Label widget.

    Args:
        master (tkinter.Widget): The master of the tkinter.Label widget to be created.
        *args: Additional arguments passed to the tkinter.Label constructor.
        **kwargs: Additional keyword arguments passed to the tkinter.Label constructor.

    Returns:
        tkinter.Label: The tkinter.Label widget.
    """

    if is_dict_empty(dictionary=kwargs):
        kwargs.update(COLOR_CONFIG["label"][get_color_mode()])

    return tkinter.Label(
        master=master,
        *args,
        **kwargs,
    )


def get_scrollbar(
    master: tkinter.Widget,
    *args,
    **kwargs,
) -> tkinter.Scrollbar:
    """
    Returns a tkinter.Scrollbar widget.

    Args:
        master (tkinter.Widget): The master of the tkinter.Scrollbar widget to be created.
        *args: Additional arguments passed to the tkinter.Scrollbar constructor.
        **kwargs: Additional keyword arguments passed to the tkinter.Scrollbar constructor.

    Returns:
        tkinter.Scrollbar: The tkinter.Scrollbar widget.
    """

    if is_dict_empty(dictionary=kwargs):
        kwargs.update(COLOR_CONFIG["scrollbar"][get_color_mode()])

    return tkinter.Scrollbar(
        master=master,
        *args,
        **kwargs,
    )


def get_scrolled_frame(
    master: tkinter.Widget,
    **kwargs,
) -> dict[str, tkinter.Widget]:
    """
    Returns a tkinter.Frame widget with a scrollbar.

    Keys:
        - "root": outer frame containing canvas and scrollbar
        - "canvas": the tkinter.Canvas used for scrolling
        - "container": the inner frame where widgets should be placed
        - "scrollbar": the vertical scrollbar widget

    Args:
        master (tkinter.Widget): The master of the tkinter.Frame widget to be created.
        **kwargs: Additional keyword arguments passed to the tkinter.Frame constructor.

    Returns:
        dict[str, tkinter.Widget]: A dictionary containing the root frame and the container frame.
            - "root": The root tkinter.Frame widget.
            - "container": The container tkinter.Frame widget inside the root frame.
            - "canvas": The tkinter.Canvas widget inside the root frame.
            - "scrollbar": The tkinter.Scrollbar widget inside the root frame.
    """

    def _on_configure(event: tkinter.Event) -> None:
        """

        Configures the scroll region of the canvas based on its content.

        This function is called whenever the canvas is resized, and it updates the scroll region
        to match the bounding box of all items in the canvas.

        Args:
            event (tkinter.Event): The configure event that triggered this function.

        Returns:
            None
        """

        canvas: tkinter.Canvas = event.widget
        canvas.configure(scrollregion=canvas.bbox(ALL))

    result: dict[str, tkinter.Widget] = {}

    result["root"] = get_frame(
        master=master,
        **kwargs.get(
            "frame",
            {},
        ),
    )

    result["root"].grid_columnconfigure(
        index=0,
        weight=1,
    )

    result["root"].grid_columnconfigure(
        index=1,
        weight=0,
    )

    result["root"].grid_rowconfigure(
        index=0,
        weight=1,
    )

    result["canvas"] = get_canvas(
        master=result["root"],
        **kwargs.get(
            "canvas",
            {},
        ),
    )

    result["canvas"].grid(
        column=0,
        row=0,
        sticky=NSEW,
    )

    result["container"] = get_frame(
        master=result["canvas"],
        **kwargs.get(
            "container",
            {},
        ),
    )

    result["container"].bind(
        func=_on_configure,
        sequence="<Configure>",
    )

    result["canvas"].create_window(
        (
            0,
            0,
        ),
        anchor=NW,
        window=result["container"],
    )

    result["scrollbar"] = get_scrollbar(
        command=result["canvas"].yview,
        master=result["root"],
        orient=VERTICAL,
        **kwargs.get(
            "scrollbar",
            {},
        ),
    )

    result["scrollbar"].grid(
        column=1,
        row=0,
        sticky=NSEW,
    )

    result["canvas"].configure(yscrollcommand=result["scrollbar"].set)

    return result


def get_toplevel(
    master: Optional[tkinter.Widget] = None,
    **kwargs,
) -> tkinter.Toplevel:
    """
    Returns a tkinter.Toplevel widget.

    Args:
        master (Optional[tkinter.Widget]): The master of the tkinter.Toplevel widget to be created.
        **kwargs: Additional keyword arguments passed to the tkinter.Toplevel constructor.

    Returns:
        tkinter.Toplevel: The tkinter.Toplevel widget.
    """

    if is_dict_empty(dictionary=kwargs):
        kwargs.update(COLOR_CONFIG["window"][get_color_mode()])

    return tkinter.Toplevel(
        master=master,
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
