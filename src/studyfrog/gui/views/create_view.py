"""
Author: Louis Goodnews
Date: 2025-11-16
"""

import tkinter

from tkinter import ttk
from tkinter.constants import E, NSEW, W
from typing import Any, Final, Literal, Optional, TypeAlias

from common.events import CALL_FUNCTION, CALL_FUNCTIONS
from gui.constants import DEFAULT_FONT, LARGE_BOLD_FONT, READONLY, TOPLEVEL_GEOMETRY
from gui.factory import (
    get_button,
    get_combobox,
    get_frame,
    get_label,
    get_scrolled_frame,
)
from gui.views.logic.create_view_logic import (
    get_form_getter,
    on_cancel_button_click,
    on_combobox_change,
    on_create_button_click,
)
from utils.utils import (
    destroy_widget_children,
    log_exception,
    log_info,
    register_subscription,
    unsubscribe_subscription,
)


# ---------- Types ---------- #

WhatType: TypeAlias = Literal[
    "flashcard",
    "note",
    "question",
    "stack",
    "subject",
    "teacher",
]


# ---------- Constants ---------- #

BOTTOM_FRAME: Optional[tkinter.Frame] = None

CENTER_FRAME: Optional[tkinter.Frame] = None

CONTAINER_FRAME: Optional[tkinter.Frame] = None

MASTER: Optional[tkinter.Toplevel] = None

NAME: Final[Literal["gui.views.views.create_view"]] = "gui.views.views.create_view"

NAMESPACE: Final[Literal["CREATE_VIEW"]] = "CREATE_VIEW"

SUBSCRIPTIONS: list[str] = []

TITLE_LABEL: Optional[tkinter.Label] = None

TOP_FRAME: Optional[tkinter.Frame] = None

WHAT: Optional[WhatType] = None


# ---------- Functions ---------- #


def clear_bottom_frame() -> None:
    """
    Clears the bottom frame.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If the bottom frame is not set. Call 'set_bottom_frame' first.
    """

    try:
        destroy_widget_children(get_bottom_frame())
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to clear bottom frame",
            name=NAME,
        )
        raise Exception(f"Failed to clear bottom frame: {e}") from e


def clear_center_frame() -> None:
    """
    Clears the center frame.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If the center frame is not set. Call 'set_center_frame' first.
    """

    try:
        destroy_widget_children(get_center_frame())
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to clear center frame",
            name=NAME,
        )
        raise Exception(f"Failed to clear center frame: {e}") from e


def clear_top_frame() -> None:
    """
    Clears the top frame.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If the top frame is not set. Call 'set_top_frame' first.
    """

    try:
        destroy_widget_children(get_top_frame())
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to clear top frame",
            name=NAME,
        )
        raise Exception(f"Failed to clear top frame: {e}") from e


def clear_widgets() -> None:
    """
    Clears all widgets.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If the bottom frame is not set. Call 'set_bottom_frame' first.
        Exception: If the center frame is not set. Call 'set_center_frame' first.
        Exception: If the top frame is not set. Call 'set_top_frame' first.
    """

    try:
        clear_bottom_frame()
        clear_center_frame()
        clear_top_frame()
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to clear widgets",
            name=NAME,
        )
        raise Exception(f"Failed to clear widgets: {e}") from e


def configure_bottom_frame_grid() -> None:
    """
    Configures the bottom frame grid.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If the bottom frame is not set. Call 'set_bottom_frame' first.
    """

    try:
        get_bottom_frame().grid_columnconfigure(
            index=0,
            weight=1,
        )
        get_bottom_frame().grid_columnconfigure(
            index=1,
            weight=0,
        )
        get_bottom_frame().grid_columnconfigure(
            index=2,
            weight=0,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to configure bottom frame grid",
            name=NAME,
        )
        raise Exception(f"Failed to configure bottom frame grid: {e}") from e


def configure_center_frame_grid() -> None:
    """
    Configures the center frame grid.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If the center frame is not set. Call 'set_center_frame' first.
    """

    try:
        get_center_frame().grid_columnconfigure(
            index=0,
            weight=0,
        )
        get_center_frame().grid_columnconfigure(
            index=1,
            weight=1,
        )
        get_container_frame().grid_rowconfigure(
            index=0,
            weight=0,
        )
        get_container_frame().grid_rowconfigure(
            index=1,
            weight=1,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to configure center frame grid",
            name=NAME,
        )
        raise Exception(f"Failed to configure center frame grid: {e}") from e


def configure_grid() -> None:
    """
    Configures the grid.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If the bottom frame is not set. Call 'set_bottom_frame' first.
        Exception: If the center frame is not set. Call 'set_center_frame' first.
        Exception: If the top frame is not set. Call 'set_top_frame' first.
    """

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
        raise Exception(f"Failed to configure grid: {e}") from e


def configure_top_frame_grid() -> None:
    """
    Configures the top frame grid.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If the top frame is not set. Call 'set_top_frame' first.
    """

    try:
        pass
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to configure top frame grid",
            name=NAME,
        )
        raise Exception(f"Failed to configure top frame grid: {e}") from e


def create_bottom_frame_widgets(master: tkinter.Frame) -> None:
    """
    Creates the bottom frame widgets.

    Args:
        master (tkinter.Frame): The master frame.

    Returns:
        None

    Raises:
        Exception: If the bottom frame is not set. Call 'set_bottom_frame' first.
    """

    try:
        get_button(
            command=on_create_button_click,
            master=master,
            text="Create",
        ).grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
        )
        get_button(
            command=on_cancel_button_click,
            master=master,
            text="Cancel",
        ).grid(
            column=2,
            padx=5,
            pady=5,
            row=0,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to create bottom frame widgets",
            name=NAME,
        )
        raise Exception(f"Failed to create bottom frame widgets: {e}") from e


def create_center_frame_widgets(master: tkinter.Frame) -> None:
    """
    Creates the center frame widgets.

    Args:
        master (tkinter.Frame): The master frame.

    Returns:
        None

    Raises:
        Exception: If the center frame is not set. Call 'set_center_frame' first.
    """

    try:
        what_label: tkinter.Label = get_label(
            anchor=W,
            font=LARGE_BOLD_FONT,
            master=master,
            text="What*?",
        )

        what_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
        )

        frame: tkinter.Frame = get_frame(master=master)

        frame.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        frame.grid_columnconfigure(
            index=0,
            weight=0,
        )

        frame.grid_columnconfigure(
            index=1,
            weight=1,
        )

        frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        what_values: list[str] = [
            "Flashcard",
            "Note",
            "Stack",
            "Subject",
            "Tag",
            "Teacher",
            "User",
        ]

        what_combobox: ttk.Combobox = get_combobox(
            master=frame,
            state=READONLY,
            values=what_values,
        )

        what_combobox.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=E,
        )

        what_combobox.current(what_values.index(get_what().title()))

        what_combobox.bind(
            add="+",
            func=lambda event: set_what(what=what_combobox.get()),
            sequence="<<ComboboxSelected>>",
        )

        what_combobox.bind(
            add="+",
            func=lambda event: on_combobox_change(
                master=get_container_frame(),
                value=what_combobox.get(),
            ),
            sequence="<<ComboboxSelected>>",
        )

        scrolled_frame: dict[str, tkinter.Widget] = get_scrolled_frame(master=master)

        scrolled_frame["root"].grid(
            column=0,
            columnspan=2,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )

        scrolled_frame["container"].grid_columnconfigure(
            index=0,
            weight=1,
        )

        set_container_frame(frame=scrolled_frame["container"])
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to create center frame widgets",
            name=NAME,
        )
        raise Exception(f"Failed to create center frame widgets: {e}") from e


def create_top_frame_widgets(master: tkinter.Frame) -> None:
    """
    Creates the top frame widgets.

    Args:
        master (tkinter.Frame): The master frame.

    Returns:
        None

    Raises:
        Exception: If the top frame is not set. Call 'set_top_frame' first.
    """

    try:
        title_label: tkinter.Label = get_label(
            anchor=W,
            font=LARGE_BOLD_FONT,
            master=master,
            text=f"Create {get_what()}",
        )

        title_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        set_title_label(title_label=title_label)

        description_label: tkinter.Label = get_label(
            anchor=W,
            font=DEFAULT_FONT,
            master=master,
            text="Required fields are marked with an asterisk. *",
        )

        description_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to create top frame widgets",
            name=NAME,
        )
        raise Exception(f"Failed to create top frame widgets: {e}") from e


def create_widgets() -> None:
    """
    Creates all widgets.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If the bottom frame is not set. Call 'set_bottom_frame' first.
        Exception: If the center frame is not set. Call 'set_center_frame' first.
        Exception: If the top frame is not set. Call 'set_top_frame' first.
    """

    try:
        create_bottom_frame_widgets(master=get_bottom_frame())
        create_center_frame_widgets(master=get_center_frame())
        create_top_frame_widgets(master=get_top_frame())
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to create widgets",
            name=NAME,
        )
        raise Exception(f"Failed to create widgets: {e}") from e


def destroy() -> None:
    """
    Destroys the create view.

    Args:
        None

    Returns:
        None
    """

    global BOTTOM_FRAME, CENTER_FRAME, CONTAINER_FRAME, MASTER, TITLE_LABEL, TOP_FRAME

    if MASTER is None:
        return

    MASTER.destroy()

    MASTER = None

    BOTTOM_FRAME = None
    CENTER_FRAME = None
    CONTAINER_FRAME = None
    TITLE_LABEL = None
    TOP_FRAME = None

    make_master_none_if_possible()

    unsubscribe()


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

    BOTTOM_FRAME = get_frame(
        height=50,
        master=get_master(),
    )

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


def get_container_frame() -> tkinter.Frame:
    """
    Returns the container frame.

    Args:
        None

    Returns:
        tkinter.Frame: The container frame.

    Raises:
        ValueError: If the container frame is not set. Call 'set_container_frame' first.
    """

    global CONTAINER_FRAME

    if CONTAINER_FRAME is None:
        raise ValueError("Container frame not set. Call 'set_container_frame' first.")

    return CONTAINER_FRAME


def get_create_view(
    master: tkinter.Toplevel,
    what: WhatType = "flashcard",
) -> None:
    """
    Returns the create view.

    Args:
        master (tkinter.Toplevel): The master window.
        what (WhatType): The type of entity to create. Default is "flashcard".
            Must be one of "flashcard", "note", "question", "stack", "subject", "teacher".

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    try:
        log_info(
            message="Getting create view",
            name=NAME,
        )

        set_master(master=master)
        set_what(what=what)

        clear_widgets()
        create_widgets()
        configure_grid()

        get_form_getter(what=what)(master=get_container_frame())

        subscribe()

        log_info(
            message="Got create view successfully",
            name=NAME,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get create view",
            name=NAME,
        )
        raise Exception(f"Failed to get create view: {e}") from e


def get_master() -> tkinter.Toplevel:
    """
    Returns the master of the create view.

    Args:
        None

    Returns:
        tkinter.Toplevel: The master window.

    Raises:
        ValueError: If the master is not set. Call 'set_master' first.
    """

    if MASTER is None:
        raise ValueError("Master not set. Call 'set_master' first.")

    return MASTER


def get_title_label() -> tkinter.Label:
    """
    Returns the title label.

    Args:
        None

    Returns:
        tkinter.Label: The title label.

    Raises:
        ValueError: If the title label is not set. Call 'set_title_label' first.
    """

    if TITLE_LABEL is None:
        raise ValueError("Title label not set. Call 'set_title_label' first.")

    return TITLE_LABEL


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

    TOP_FRAME = get_frame(
        height=50,
        master=get_master(),
    )

    TOP_FRAME.grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    return TOP_FRAME


def get_what() -> WhatType:
    """
    Returns the what.

    Args:
        None

    Returns:
        WhatType: The what.

    Raises:
        ValueError: If the what is not set. Call 'set_what' first.
    """

    global WHAT

    if WHAT is None:
        raise ValueError("What not set. Call 'set_what' first.")

    return WHAT


def make_master_none_if_possible() -> None:
    """
    Makes the master none if possible.

    Args:
        None

    Returns:
        None
    """

    global MASTER

    if MASTER is None:
        return

    MASTER = None


def on_call_function(
    function: str,
    *args,
    **kwargs,
) -> Any:
    """
    Handle the call function event.

    Args:
        function (str): The function.

    Returns:
        Any: The result.

    Raises:
        Exception: If an error occurs.
    """

    try:
        value: Any = globals().get(function)

        if not callable(value):
            raise Exception(f"Attribute '{function}' is not callable")

        return value(
            *args,
            **kwargs,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to handle call function event",
            name=NAME,
        )
        raise Exception(f"Failed to handle call function event: {e}") from e


def on_call_functions(
    functions: list[str],
    *args,
    **kwargs,
) -> list[Any]:
    """
    Handle the call functions event.

    Args:
        functions (list[str]): The functions.

    Returns:
        list[Any]: The results.

    Raises:
        Exception: If an error occurs.
    """

    try:
        result: list[Any] = []

        for function in functions:
            result.append(
                on_call_function(
                    function=function,
                    *args,
                    **kwargs,
                )
            )

        return result
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to handle call functions event",
            name=NAME,
        )
        raise Exception(f"Failed to handle call functions event: {e}") from e


def set_container_frame(frame: tkinter.Frame) -> None:
    """
    Sets the container frame.

    Args:
        frame (tkinter.Frame): The container frame.

    Returns:
        None
    """

    global CONTAINER_FRAME

    CONTAINER_FRAME = frame


def set_master(master: tkinter.Toplevel) -> None:
    """
    Sets the master of the create view.

    Args:
        master (tkinter.Toplevel): The master window.

    Returns:
        None
    """

    global MASTER

    MASTER = master

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

    MASTER.geometry(newGeometry=TOPLEVEL_GEOMETRY)


def set_title_label(title_label: tkinter.Label) -> None:
    """
    Sets the title label.

    Args:
        title_label (tkinter.Label): The title label.

    Returns:
        None
    """

    global TITLE_LABEL

    TITLE_LABEL = title_label


def set_what(what: WhatType) -> None:
    """
    Sets the what.

    Args:
        what (WhatType): The what.

    Returns:
        None
    """

    global WHAT

    WHAT = what


def subscribe() -> None:
    """
    Subscribe to various events.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    try:
        SUBSCRIPTIONS.append(
            register_subscription(
                event=CALL_FUNCTION,
                function=on_call_function,
                namespace=NAMESPACE,
                persistent=True,
            )
        )
        SUBSCRIPTIONS.append(
            register_subscription(
                event=CALL_FUNCTIONS,
                function=on_call_functions,
                namespace=NAMESPACE,
                persistent=True,
            )
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to subscribe",
            name=NAME,
        )
        raise Exception(f"Failed to subscribe: {e}") from e


def unsubscribe() -> None:
    """
    Unsubscribe from various events.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    try:
        for subscription in SUBSCRIPTIONS:
            unsubscribe_subscription(uuid=subscription)
        SUBSCRIPTIONS.clear()
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to unsubscribe",
            name=NAME,
        )
        raise Exception(f"Failed to unsubscribe: {e}") from e


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
