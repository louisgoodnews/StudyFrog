"""
Author: Louis Goodnews
Date: 2025-12-13
Description: Custom widgets of the application.
"""

import customtkinter as ctk

from tkinter.constants import NSEW
from typing import Any, Callable, Final, Literal, Optional

from constants.gui import TOAST_GEOMETRY
from utils.common import generate_uuid4_str


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "get_error_toast",
    "get_info_toast",
    "get_success_toast",
    "get_warning_toast",
]


# ---------- Constants ---------- #


TOAST_DATA: dict[str, Any] = {}


# ---------- Helper Functions ---------- #


def _decrement_alpha(uuid: str) -> None:
    """
    Decreases the alpha (opacity) of the toast notification window (Fade-Out effect).

    It reads the current alpha and toplevel window from TOAST_DATA.
    The function recursively calls itself via toplevel.after() until the alpha
    reaches 0.0. Once fully transparent, the window is destroyed and the data is cleaned up.

    Args:
        uuid (str): The unique identifier of the toast notification.
    """

    if uuid not in TOAST_DATA:
        return

    data = TOAST_DATA[uuid]
    toplevel: ctk.CTkToplevel = data["toplevel"]
    current_alpha: float = data["alpha"]

    if current_alpha > 0.0:
        new_alpha: float = max(
            0.0,
            current_alpha - 0.05,
        )
        toplevel.attributes(
            "-alpha",
            new_alpha,
        )
        data["alpha"] = new_alpha

        toplevel.after(
            50,
            _decrement_alpha,
            uuid,
        )
    else:
        toplevel.destroy()
        del TOAST_DATA[uuid]


def _determine_position(
    position: Literal[
        "bottom_left",
        "bottom_right",
        "top_left",
        "top_right",
    ],
) -> str:
    """
    Determines the geometry of the toast notification based on the position.

    Args:
        position (Literal["bottom_left", "bottom_right", "top_left", "top_right"]): The position of the toast notification.

    Returns:
        The geometry of the toast notification.
    """

    positions: dict[
        Literal[
            "bottom_left",
            "bottom_right",
            "top_left",
            "top_right",
        ],
        str,
    ] = {
        "bottom_left": "100+0",
        "bottom_right": "100+100",
        "top_left": "0+0",
        "top_right": "0+100",
    }

    return f"{TOAST_GEOMETRY}+{positions.get(position, "0+0")}"


def _increment_alpha(uuid: str) -> None:
    """
    Increases the alpha (opacity) of the toast notification window (Fade-In effect).

    It reads the current alpha and toplevel window from TOAST_DATA.
    The function recursively calls itself via toplevel.after() until the alpha
    reaches 1.0. Once fully opaque, it schedules the start of the fade-out
    effect (_decrement_alpha) after the specified display duration.

    Args:
        uuid (str): The unique identifier of the toast notification.
    """

    if uuid not in TOAST_DATA:
        return

    data = TOAST_DATA[uuid]
    toplevel: ctk.CTkToplevel = data["toplevel"]
    current_alpha: float = data["alpha"]
    duration: int = data["duration"]

    if current_alpha < 0.05:
        current_alpha = 0.05

    if current_alpha < 1.0:
        new_alpha: float = min(
            1.0,
            current_alpha + 0.05,
        )
        toplevel.attributes(
            "-alpha",
            new_alpha,
        )
        data["alpha"] = new_alpha

        toplevel.after(
            50,
            _increment_alpha,
            uuid,
        )
    else:
        toplevel.after(
            duration,
            _decrement_alpha,
            uuid,
        )


# ---------- Private Functions ---------- #


def _get_toast_notification(
    message: str,
    title: str,
    duration: int = 5000,
    on_click: Optional[Callable[[], None]] = None,
    position: Literal[
        "bottom_left",
        "bottom_right",
        "top_left",
        "top_right",
    ] = "top_right",
) -> tuple[ctk.CTkLabel, ctk.CTkLabel, ctk.CTkToplevel]:
    """
    Creates the toast notification widgets.

    Args:
        message (str): The message of the notification.
        title (str): The title of the notification.
        duration (int): The duration of the notification in miliseconds.
        on_click (Optional[Callable[[], None]]): The callback function to be called when the notification is clicked.
        position (Literal["bottom_left", "bottom_right", "top_left", "top_right"]): The position of the notification.

    Returns:
        tuple[ctk.CTkLabel, ctk.CTkLabel, ctk.CTkToplevel]: The toast notification's widgets.
    """

    uuid: str = generate_uuid4_str()

    toplevel: ctk.CTkToplevel = ctk.CTkToplevel()

    toplevel.geometry(geometry_string=_determine_position(position=position))

    toplevel.grid_columnconfigure(
        index=0,
        weight=1,
    )
    toplevel.grid_rowconfigure(
        index=0,
        weight=0,
    )
    toplevel.grid_rowconfigure(
        index=1,
        weight=1,
    )

    title_label: ctk.CTkLabel = ctk.CTkLabel(
        master=toplevel,
        text=title,
    )

    title_label.grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    title_label.bind(
        command=lambda event: (
            (on_click() if on_click is not None else None),
            toplevel.destroy(),
        ),
        sequence="<<ButtonRelease-1>>",
    )

    message_label: ctk.CTkLabel = ctk.CTkLabel(
        master=toplevel,
        text=message,
    )

    message_label.grid(
        column=0,
        padx=5,
        pady=5,
        row=1,
        sticky=NSEW,
    )

    message_label.bind(
        command=lambda event: (
            (on_click() if on_click is not None else None),
            toplevel.destroy(),
        ),
        sequence="<<ButtonRelease-1>>",
    )

    TOAST_DATA[uuid] = {
        "alpha": 0.5,
        "duration": duration,
        "toplevel": toplevel,
    }

    toplevel.attributes(
        "-alpha",
        0.05,
    )

    toplevel.after(
        10,
        _decrement_alpha,
        uuid,
    )

    return (
        message_label,
        title_label,
        toplevel,
    )


# ---------- Public Functions ---------- #


def get_error_toast(
    message: str,
    title: str,
    duration: int = 5000,
    on_click: Optional[Callable[[], None]] = None,
    position: Literal[
        "bottom_left",
        "bottom_right",
        "top_left",
        "top_right",
    ] = "top_right",
) -> None:
    """
    Creates an error toast notification.

    Args:
        message (str): The message of the notification.
        title (str): The title of the notification.
        duration (int): The duration of the notification in miliseconds.
        on_click (Optional[Callable[[], None]]): The callback function to be called when the notification is clicked.
        position (Literal["bottom_left", "bottom_right", "top_left", "top_right"]): The position of the notification.

    Returns:
        None
    """

    (
        message_label,
        title_label,
        toplevel,
    ) = _get_toast_notification(
        message=message,
        title=title,
        duration=duration,
        on_click=on_click,
        position=position,
    )


def get_info_toast(
    message: str,
    title: str,
    duration: int = 5000,
    on_click: Optional[Callable[[], None]] = None,
    position: Literal[
        "bottom_left",
        "bottom_right",
        "top_left",
        "top_right",
    ] = "top_right",
) -> None:
    """
    Creates an info toast notification.

    Args:
        message (str): The message of the notification.
        title (str): The title of the notification.
        duration (int): The duration of the notification in miliseconds.
        on_click (Optional[Callable[[], None]]): The callback function to be called when the notification is clicked.
        position (Literal["bottom_left", "bottom_right", "top_left", "top_right"]): The position of the notification.

    Returns:
        None
    """

    (
        message_label,
        title_label,
        toplevel,
    ) = _get_toast_notification(
        message=message,
        title=title,
        duration=duration,
        on_click=on_click,
        position=position,
    )


def get_success_toast(
    message: str,
    title: str,
    duration: int = 5000,
    on_click: Optional[Callable[[], None]] = None,
    position: Literal[
        "bottom_left",
        "bottom_right",
        "top_left",
        "top_right",
    ] = "top_right",
) -> None:
    """
    Creates a success toast notification.

    Args:
        message (str): The message of the notification.
        title (str): The title of the notification.
        duration (int): The duration of the notification in miliseconds.
        on_click (Optional[Callable[[], None]]): The callback function to be called when the notification is clicked.
        position (Literal["bottom_left", "bottom_right", "top_left", "top_right"]): The position of the notification.

    Returns:
        None
    """

    (
        message_label,
        title_label,
        toplevel,
    ) = _get_toast_notification(
        message=message,
        title=title,
        duration=duration,
        on_click=on_click,
        position=position,
    )


def get_warning_toast(
    message: str,
    title: str,
    duration: int = 5000,
    on_click: Optional[Callable[[], None]] = None,
    position: Literal[
        "bottom_left",
        "bottom_right",
        "top_left",
        "top_right",
    ] = "top_right",
) -> None:
    """
    Creates a warning toast notification.

    Args:
        message (str): The message of the notification.
        title (str): The title of the notification.
        duration (int): The duration of the notification in miliseconds.
        on_click (Optional[Callable[[], None]]): The callback function to be called when the notification is clicked.
        position (Literal["bottom_left", "bottom_right", "top_left", "top_right"]): The position of the notification.

    Returns:
        None
    """

    (
        message_label,
        title_label,
        toplevel,
    ) = _get_toast_notification(
        message=message,
        title=title,
        duration=duration,
        on_click=on_click,
        position=position,
    )
