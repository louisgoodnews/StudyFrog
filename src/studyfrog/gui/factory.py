"""
Author: Louis Goodnews
Date: 2025-11-16
"""

import tkinter

from tkinter import ttk
from tkinter.constants import ALL, BOTH, NS, NSEW, NW, TOP, VERTICAL, YES
from typing import Any, Final, Literal, Optional

from gui.constants import COLOR_CONFIG, TOAST_GEOMETRY
from utils.utils import log_exception

# ---------- Constants ---------- #

COLOR_MODE: Literal["dark", "light"] = "dark"

NAME: Final[Literal["gui.factory"]] = "gui.factory"


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

    try:
        keyword_arguments: dict[str, Any] = dict(COLOR_CONFIG["button"][get_color_mode()])

        keyword_arguments.update(kwargs)

        return tkinter.Button(
            master=master,
            *args,
            **keyword_arguments,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get button",
            name=NAME,
        )
        raise Exception(f"Failed to get button: {e}") from e


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

    try:
        keyword_arguments: dict[str, Any] = dict(COLOR_CONFIG["canvas"][get_color_mode()])

        keyword_arguments.update(kwargs)

        return tkinter.Canvas(
            master=master,
            *args,
            **keyword_arguments,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get canvas",
            name=NAME,
        )
        raise Exception(f"Failed to get canvas: {e}") from e


def get_checkbutton(
    master: tkinter.Widget,
    *args,
    **kwargs,
) -> tkinter.Checkbutton:
    """
    Returns a tkinter.Checkbutton widget.

    Args:
        master (tkinter.Widget): The master of the tkinter.Checkbutton widget to be created.
        *args: Additional arguments passed to the tkinter.Checkbutton constructor.
        **kwargs: Additional keyword arguments passed to the tkinter.Checkbutton constructor.

    Returns:
        tkinter.Checkbutton: The tkinter.Checkbutton widget.
    """

    try:
        keyword_arguments: dict[str, Any] = dict(COLOR_CONFIG["checkbutton"][get_color_mode()])

        keyword_arguments.update(kwargs)

        return tkinter.Checkbutton(
            master=master,
            *args,
            **keyword_arguments,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get checkbutton",
            name=NAME,
        )
        raise Exception(f"Failed to get checkbutton: {e}") from e


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

    return COLOR_MODE


def get_combobox(
    master: tkinter.Widget,
    *args,
    **kwargs,
) -> ttk.Combobox:
    """
    Returns a ttk.Combobox widget.

    Args:
        master (tkinter.Widget): The master of the ttk.Combobox widget to be created.
        *args: Additional arguments passed to the ttk.Combobox constructor.
        **kwargs: Additional keyword arguments passed to the ttk.Combobox constructor.

    Returns:
        ttk.Combobox: The ttk.Combobox widget.
    """

    try:
        keyword_arguments: dict[str, Any] = dict(COLOR_CONFIG["combobox"][get_color_mode()])

        keyword_arguments.update(kwargs)

        return ttk.Combobox(
            master=master,
            *args,
            **keyword_arguments,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get combobox",
            name=NAME,
        )
        raise Exception(f"Failed to get combobox: {e}") from e


def get_entry(
    master: tkinter.Widget,
    *args,
    **kwargs,
) -> tkinter.Entry:
    """
    Returns a tkinter.Entry widget.

    Args:
        master (tkinter.Widget): The master of the tkinter.Entry widget to be created.
        *args: Additional arguments passed to the tkinter.Entry constructor.
        **kwargs: Additional keyword arguments passed to the tkinter.Entry constructor.

    Returns:
        tkinter.Entry: The tkinter.Entry widget.
    """

    try:
        keyword_arguments: dict[str, Any] = dict(COLOR_CONFIG["entry"][get_color_mode()])

        keyword_arguments.update(kwargs)

        return tkinter.Entry(
            master=master,
            *args,
            **keyword_arguments,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get entry",
            name=NAME,
        )
        raise Exception(f"Failed to get entry: {e}") from e


def get_error_toast(
    message: str,
    title: str,
    duration_ms: int = 5300,
    fade_delay_ms: int = 50,
    fade_step: float = 0.05,
    *args,
    **kwargs,
) -> None:
    """
    Displays an error toast.

    Args:
        duration_ms (int): The duration of the toast in milliseconds.
        fade_delay_ms (int): The delay before the toast starts fading in milliseconds.
        fade_step (float): The step size for the fade animation.
        message (str): The message to be displayed in the toast.
        title (str): The title of the toast.
        *args: Additional arguments passed to the tkinter.Toplevel constructor.
        **kwargs: Additional keyword arguments passed to the tkinter.Toplevel constructor.

    Returns:
        None
    """

    try:
        keyword_arguments: dict[str, Any] = {
            "toplevel": COLOR_CONFIG["toplevel"][get_color_mode()],
            "message_label": COLOR_CONFIG["label"][get_color_mode()],
            "title_label": COLOR_CONFIG["label"][get_color_mode()],
        }

        keyword_arguments.update(kwargs)

        get_toast(
            duration_ms=duration_ms,
            fade_delay_ms=fade_delay_ms,
            fade_step=fade_step,
            message=message,
            title=f"ERROR: {title}",
            *args,
            **keyword_arguments,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to display error toast",
            name=NAME,
        )
        raise Exception(f"Failed to display error toast: {e}") from e


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

    try:
        keyword_arguments: dict[str, Any] = dict(COLOR_CONFIG["frame"][get_color_mode()])

        keyword_arguments.update(kwargs)

        return tkinter.Frame(
            master=master,
            *args,
            **keyword_arguments,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get frame",
            name=NAME,
        )
        raise Exception(f"Failed to get frame: {e}") from e


def get_info_toast(
    message: str,
    title: str,
    duration_ms: int = 5300,
    fade_delay_ms: int = 50,
    fade_step: float = 0.05,
    *args,
    **kwargs,
) -> None:
    """
    Displays an info toast.

    Args:
        duration_ms (int): The duration of the toast in milliseconds.
        fade_delay_ms (int): The delay before the toast starts fading in milliseconds.
        fade_step (float): The step size for the fade animation.
        message (str): The message to be displayed in the toast.
        title (str): The title of the toast.
        *args: Additional arguments passed to the tkinter.Toplevel constructor.
        **kwargs: Additional keyword arguments passed to the tkinter.Toplevel constructor.

    Returns:
        None
    """

    try:
        keyword_arguments: dict[str, Any] = {
            "toplevel": COLOR_CONFIG["toplevel"][get_color_mode()],
            "message_label": COLOR_CONFIG["label"][get_color_mode()],
            "title_label": COLOR_CONFIG["label"][get_color_mode()],
        }

        keyword_arguments.update(kwargs)

        get_toast(
            duration_ms=duration_ms,
            fade_delay_ms=fade_delay_ms,
            fade_step=fade_step,
            message=message,
            title=f"INFO: {title}",
            *args,
            **keyword_arguments,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get info toast",
            name=NAME,
        )
        raise Exception(f"Failed to get info toast: {e}") from e


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

    try:
        keyword_arguments: dict[str, Any] = dict(COLOR_CONFIG["label"][get_color_mode()])

        keyword_arguments.update(kwargs)

        return tkinter.Label(
            master=master,
            *args,
            **keyword_arguments,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get label",
            name=NAME,
        )
        raise Exception(f"Failed to get label: {e}") from e


def get_radiobutton(
    master: tkinter.Widget,
    *args,
    **kwargs,
) -> tkinter.Radiobutton:
    """
    Returns a tkinter.Radiobutton widget.

    Args:
        master (tkinter.Widget): The master of the tkinter.Radiobutton widget to be created.
        *args: Additional arguments passed to the tkinter.Radiobutton constructor.
        **kwargs: Additional keyword arguments passed to the tkinter.Radiobutton constructor.

    Returns:
        tkinter.Radiobutton: The tkinter.Radiobutton widget.
    """

    try:
        keyword_arguments: dict[str, Any] = dict(COLOR_CONFIG["radiobutton"][get_color_mode()])

        keyword_arguments.update(kwargs)

        return tkinter.Radiobutton(
            master=master,
            *args,
            **keyword_arguments,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get radiobutton",
            name=NAME,
        )
        raise Exception(f"Failed to get radiobutton: {e}") from e


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

    try:
        keyword_arguments: dict[str, Any] = dict(COLOR_CONFIG["scrollbar"][get_color_mode()])

        keyword_arguments.update(kwargs)

        return tkinter.Scrollbar(
            master=master,
            *args,
            **keyword_arguments,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get scrollbar",
            name=NAME,
        )
        raise Exception(f"Failed to get scrollbar: {e}") from e


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

        try:
            canvas: tkinter.Canvas = result["canvas"]
            canvas.configure(scrollregion=canvas.bbox(ALL))
            canvas.itemconfig(
                result["window_id"],
                width=canvas.winfo_width(),
            )
        except Exception as e:
            log_exception(
                exception=e,
                message="Failed to configure scroll region",
                name=NAME,
            )
            raise Exception(f"Failed to configure scroll region: {e}") from e

    try:
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

        result["window_id"] = result["canvas"].create_window(
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
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        result["canvas"].configure(yscrollcommand=result["scrollbar"].set)

        return result
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get scrolled frame",
            name=NAME,
        )
        raise Exception(f"Failed to get scrolled frame: {e}") from e


def get_scrolled_text(
    master: tkinter.Widget,
    *args,
    **kwargs,
) -> dict[str, tkinter.Widget]:
    """
    Creates a scrolled text widget.

    Args:
        master: The parent widget.
        *args: Additional positional arguments for the text widget.
        **kwargs: Additional keyword arguments for the text widget.

    Returns:
        A dictionary containing the text widget and its scrollbar.
    """

    try:
        result: dict[str, tkinter.Widget] = {}

        result["root"] = get_frame(
            master=master,
            *args,
            **kwargs,
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

        result["text"] = get_text(
            master=result["root"],
            *args,
            **kwargs,
        )

        result["text"].grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        result["scrollbar"] = get_scrollbar(
            command=result["text"].yview,
            master=result["root"],
            orient=VERTICAL,
            *args,
            **kwargs,
        )

        result["scrollbar"].grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=NS,
        )

        result["text"].config(yscrollcommand=result["scrollbar"].set)

        return result
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get scrolled text",
            name=NAME,
        )
        raise Exception(f"Failed to get scrolled text: {e}") from e


def get_success_toast(
    message: str,
    title: str,
    duration_ms: int = 5300,
    fade_delay_ms: int = 50,
    fade_step: float = 0.05,
    *args,
    **kwargs,
) -> None:
    """
    Displays a success toast.

    Args:
        duration_ms (int): The duration of the toast in milliseconds.
        fade_delay_ms (int): The delay before the toast starts fading in milliseconds.
        fade_step (float): The step size for the fade animation.
        message (str): The message to be displayed in the toast.
        title (str): The title of the toast.
        *args: Additional arguments passed to the tkinter.Toplevel constructor.
        **kwargs: Additional keyword arguments passed to the tkinter.Toplevel constructor.

    Returns:
        None
    """

    try:
        keyword_arguments: dict[str, Any] = {
            "toplevel": COLOR_CONFIG["toplevel"][get_color_mode()],
            "message_label": COLOR_CONFIG["label"][get_color_mode()],
            "title_label": COLOR_CONFIG["label"][get_color_mode()],
        }

        keyword_arguments.update(kwargs)

        get_toast(
            duration_ms=duration_ms,
            fade_delay_ms=fade_delay_ms,
            fade_step=fade_step,
            message=message,
            title=f"SUCCESS: {title}",
            *args,
            **keyword_arguments,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get success toast",
            name=NAME,
        )
        raise Exception(f"Failed to get success toast: {e}") from e


def get_text(
    master: tkinter.Widget,
    **kwargs,
) -> tkinter.Text:
    """
    Returns a tkinter.Text widget.

    Args:
        master (tkinter.Widget): The master of the tkinter.Text widget to be created.
        **kwargs: Additional keyword arguments passed to the tkinter.Text constructor.

    Returns:
        tkinter.Text: The tkinter.Text widget.
    """

    try:
        keyword_arguments: dict[str, Any] = dict(COLOR_CONFIG["text"][get_color_mode()])

        keyword_arguments.update(kwargs)

        return tkinter.Text(
            master=master,
            **keyword_arguments,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get text",
            name=NAME,
        )
        raise Exception(f"Failed to get text: {e}") from e


def get_toast(
    message: str,
    title: str,
    duration_ms: int = 3000,
    fade_delay_ms: int = 50,
    fade_step: float = 0.05,
    **kwargs,
) -> None:
    """
    Returns a tkinter.Toplevel widget.

    Args:
        duration_ms (int): The duration of the toast in milliseconds.
        fade_delay_ms (int): The delay between fade steps in milliseconds.
        fade_step (float): The step size for the fade effect.
        message (str): The message of the toast.
        title (str): The title of the toast.
        **kwargs: Additional keyword arguments passed to the tkinter.Toplevel constructor.

    Returns:
        None
    """

    def _fade_out(alpha: float = 1.0) -> None:
        """
        Reduces the window alpha stepwise until it reaches 0,
        then destroys the toplevel.

        Args:
            alpha (float): The alpha value of the window.

        Returns:
            None

        Raises:
            Exception: If the toplevel is already destroyed.
        """
        try:
            if alpha <= 0:
                toplevel.destroy()
                return

            toplevel.attributes("-alpha", alpha)
            toplevel.after(
                fade_delay_ms,
                _fade_out,
                alpha - fade_step,
            )
        except Exception as e:
            log_exception(
                exception=e,
                message="Failed to fade out toast",
                name=NAME,
            )
            raise Exception(f"Failed to fade out toast: {e}") from e

    try:
        toplevel: tkinter.Toplevel = get_toplevel(
            **kwargs.get(
                "toplevel",
                {},
            ),
        )

        toplevel.bind(
            func=lambda event: toplevel.destroy(),
            sequence="<Button-1>",
        )

        toplevel.attributes(
            "-topmost",
            True,
        )
        toplevel.geometry(newGeometry=TOAST_GEOMETRY)
        toplevel.overrideredirect(boolean=True)

        title_label: tkinter.Label = get_label(
            master=toplevel,
            text=title,
            **kwargs.get(
                "title_label",
                {},
            ),
        )

        title_label.pack(
            expand=YES,
            fill=BOTH,
            side=TOP,
        )

        title_label.bind(
            func=lambda event: toplevel.destroy(),
            sequence="<Button-1>",
        )

        message_label: tkinter.Label = get_label(
            master=toplevel,
            text=message,
            **kwargs.get(
                "message_label",
                {},
            ),
        )

        message_label.pack(
            expand=YES,
            fill=BOTH,
            side=TOP,
        )

        message_label.bind(
            func=lambda event: toplevel.destroy(),
            sequence="<Button-1>",
        )

        toplevel.bell()

        toplevel.after(
            duration_ms,
            _fade_out,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get toast",
            name=NAME,
        )
        raise Exception(f"Failed to get toast: {e}") from e


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

    try:
        keyword_arguments: dict[str, Any] = dict(COLOR_CONFIG["window"][get_color_mode()])

        keyword_arguments.update(kwargs)

        return tkinter.Toplevel(
            master=master,
            **keyword_arguments,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get toplevel",
            name=NAME,
        )
        raise Exception(f"Failed to get toplevel: {e}") from e


def get_warning_toast(
    message: str,
    title: str,
    duration_ms: int = 5300,
    fade_delay_ms: int = 50,
    fade_step: float = 0.05,
    *args,
    **kwargs,
) -> None:
    """
    Displays a warning toast.

    Args:
        duration_ms (int): The duration of the toast in milliseconds.
        fade_delay_ms (int): The delay before the toast starts fading in milliseconds.
        fade_step (float): The step size for the fade animation.
        message (str): The message to be displayed in the toast.
        title (str): The title of the toast.
        *args: Additional arguments passed to the tkinter.Toplevel constructor.
        **kwargs: Additional keyword arguments passed to the tkinter.Toplevel constructor.

    Returns:
        None
    """

    try:
        keyword_arguments: dict[str, Any] = {
            "toplevel": COLOR_CONFIG["toplevel"][get_color_mode()],
            "message_label": COLOR_CONFIG["label"][get_color_mode()],
            "title_label": COLOR_CONFIG["label"][get_color_mode()],
        }

        keyword_arguments.update(kwargs)

        get_toast(
            duration_ms=duration_ms,
            fade_delay_ms=fade_delay_ms,
            fade_step=fade_step,
            message=message,
            title=f"WARNING: {title}",
            *args,
            **keyword_arguments,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get warning toast",
            name=NAME,
        )
        raise Exception(f"Failed to get warning toast: {e}") from e


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
