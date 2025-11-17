"""
Author: Louis Goodnews
Date: 2025-11-16
"""

import sys
import threading
import tkinter
import traceback
import uuid

from datetime import date, datetime
from pathlib import Path
from typing import Final, Literal, Optional


# ---------- Constants ---------- #

COLORIZATION: Final[dict[str, str]] = {
    "BOLD": "\033[1m",
    "CRITICAL": "\033[35m",
    "DEBUG": "\033[36m",
    "DEFAULT": "\033[0m",
    "ERROR": "\033[31m",
    "INFO": "\033[32m",
    "ITALIC": "\033[3m",
    "UNDERLINED": "\033[4m",
    "WARNING": "\033[33m",
}

LOCK: Final[threading.Lock] = threading.Lock()


# ---------- Functions ---------- #


def destroy_widget_children(widget: tkinter.Widget) -> None:
    """
    Destroys all children of the specified widget.

    Args:
        widget (tkinter.Widget): The widget who's children should be destroyed

    Returns:
        None
    """

    for child in widget.winfo_children():
        child.destroy()


def ensure_dir(path: Path) -> bool:
    """
    Ensures that a directory exists at the specified path.

    Args:
        path (Path): The path to the directory.

    Returns:
        bool: True if the directory exists, False otherwise.
    """

    try:
        path.mkdir(exist_ok=True)
        return True
    except Exception:
        return False


def ensure_file(path: Path) -> bool:
    """
    Ensures that a file exists at the specified path.

    Args:
        path (Path): The path to the file.

    Returns:
        bool: True if the file exists, False otherwise.
    """

    try:
        ensure_dir(path.parent)
        path.touch(exist_ok=True)
        return True
    except Exception:
        return False


def ensure_json(path: Path) -> bool:
    """
    Ensures that a JSON file exists at the specified path.

    Args:
        path (Path): The path to the JSON file.

    Returns:
        bool: True if the JSON file exists, False otherwise.
    """

    try:
        ensure_dir(path.parent)
        if not path.exists():
            path.write_text(
                data="{}",
                encoding="utf-8",
            )
        return True
    except Exception:
        return False


def get_cwd() -> Path:
    """
    Returns the current working directory.

    Args:
        None

    Returns:
        Path: A Path object pointing to the current working directory.
    """

    return Path.cwd()


def get_dir(path: Path) -> bool:
    """
    Ensures that a directory exists at the specified path.

    Args:
        path (Path): The path to the directory.

    Returns:
        bool: True if the directory exists, False otherwise.
    """

    try:
        path.mkdir(
            exist_ok=True,
            parent=True,
        )
        return True
    except Exception:
        return False


def get_file(path: Path) -> bool:
    """
    Ensures that a file exists at the specified path.

    Args:
        path (Path): The path to the file.

    Returns:
        bool: True if the file exists, False otherwise.
    """

    try:
        path.touch()
        return True
    except Exception:
        return False


def get_file_content_bytes(path: Path) -> Optional[bytes]:
    """
    Returns the content of a file as bytes.

    Args:
        path (Path): A Path object pointing to the location from which the file contents are to be read.

    Returns:
        Optional[bytes]: The content of the file or None if reading the file fails.
    """

    global LOCK

    try:
        with LOCK:
            return path.read_bytes()
    except Exception:
        return None


def get_file_content_str(path: Path) -> Optional[str]:
    """
    Returns the content of a file as a string.

    Args:
        path (Path): A Path object pointing to the location from which the file contents are to be read.

    Returns:
        Optional[str]: The content of the file or None if reading the file fails.
    """

    global LOCK

    try:
        with LOCK:
            return path.read_text(encoding="utf-8")
    except Exception:
        return None


def get_home() -> Path:
    """
    Returns the current date and time.

    Args:
        None

    Returns:
        A Path object pointing the user's home directory.
    """

    return Path.home()


def get_now() -> datetime:
    """
    Returns the current date and time.

    Args:
        None

    Returns:
        datetime: The current date and time.
    """

    return datetime.now()


def get_now_str() -> str:
    """
    Returns the current date and time as a string.

    Args:
        None

    Returns:
        str: The current date and time as a string.
    """

    return get_now().isoformat()


def get_platform() -> Literal["darwin", "linux", "windows"]:
    """
    Returns the current platform.

    Args:
        None

    Returns:
        Literal["darwin", "linux", "windows"]: A literal string being either 'darwin' (MacOS), 'linux' or 'windows'.
    """

    return sys.platform.lower()


def get_today() -> date:
    """
    Returns the current date.

    Args:
        None

    Returns:
        date: The current date.
    """

    return date.today()


def get_today_str() -> str:
    """
    Returns the current date as a string.

    Args:
        None

    Returns:
        str: The current date as a string.
    """

    return get_today().isoformat()


def get_uuid() -> uuid.UUID:
    """
    Returns a random UUID.

    Args:
        None

    Returns:
        uuid.UUID: A random UUID.
    """

    return uuid.uuid4()


def get_uuid_str() -> str:
    """
    Returns a random UUID as a string.

    Args:
        None

    Returns:
        str: A random UUID as a string.
    """

    return str(get_uuid())


def get_widget_children(widget: tkinter.Widget) -> list[tkinter.Widget]:
    """
    Returns the children of a widget.

    Args:
        widget (tkinter.Widget): The widget who's children should be returned.

    Returns:
        list[tkinter.Widget]: A list containing the children of the passed widget.
    """

    return widget.winfo_children()


def log(
    message: str,
    name: str,
    level: str = "DEFAULT",
) -> None:
    """
    Logs a message.

    Args:
        level (str): The level at which to log the message. Influences colorized display. Defaults to "DEFAULT"
        message (str): The message to log.
        name (str): The name under which to log.

    Returns:
        None
    """

    global COLORIZATION

    color: str = COLORIZATION.get(
        level.upper(),
        COLORIZATION.get("DEFAULT"),
    )

    print(
        f"{color}{get_now_str()} - [{level.upper()}] - [{name.upper()}]:{message}{COLORIZATION["DEFAULT"]};"
    )


def log_critical(
    message: str,
    name: str,
) -> None:
    """
    Logs a message at the "CRITICAL" level.

    Args:
        message (str): The message to log.
        name (str): The name under which to log.

    Returns:
        None
    """

    log(
        level="CRITICAL",
        message=message,
        name=name,
    )


def log_debug(
    message: str,
    name: str,
) -> None:
    """
    Logs a message at the "DEBUG" level.

    Args:
        message (str): The message to log.
        name (str): The name under which to log.

    Returns:
        None
    """

    log(
        level="DEBUG",
        message=message,
        name=name,
    )


def log_error(
    message: str,
    name: str,
) -> None:
    """
    Logs a message at the "ERROR" level.

    Args:
        message (str): The message to log.
        name (str): The name under which to log.

    Returns:
        None
    """

    log(
        level="ERROR",
        message=message,
        name=name,
    )


def log_exception(
    exception: Exception,
    name: str,
) -> None:
    """
    Logs an exception at the "ERROR" level.

    Args:
        exception (Exception): The exception to log.
        name (str): The name under which to log.

    Returns:
        None
    """

    log(
        level="ERROR",
        message=f"{exception}\n{traceback.format_exc()}",
        name=name,
    )


def log_info(
    message: str,
    name: str,
) -> None:
    """
    Logs a message at the "INFO" level.

    Args:
        message (str): The message to log.
        name (str): The name under which to log.

    Returns:
        None
    """

    log(
        level="INFO",
        message=message,
        name=name,
    )


def log_warning(
    message: str,
    name: str,
) -> None:
    """
    Logs a message at the "WARNING" level.

    Args:
        message (str): The message to log.
        name (str): The name under which to log.

    Returns:
        None
    """

    log(
        level="WARNING",
        message=message,
        name=name,
    )


def write_file_bytes(
    data: bytes,
    path: Path,
) -> bool:
    """
    Writes bytes to a specified file.

    Args:
        data (bytes): The data to write to the file.
        path (Path): The path to the file.

    Returns:
        bool: True if the file was written successfully, False otherwise.
    """

    global LOCK

    try:
        with LOCK:
            path.write_bytes(data=data)
        return True
    except Exception:
        return False


def write_file_str(
    data: str,
    path: Path,
    encoding: str = "utf-8",
) -> bool:
    """
    Writes a string to a specified file.

    Args:
        data (str): The data to write to the file.
        path (Path): The path to the file.
        encoding (str, optional): The encoding to use when writing the file. Defaults to "utf-8".

    Returns:
        bool: True if the file was written successfully, False otherwise.
    """

    global LOCK

    try:
        with LOCK:
            path.write_text(
                data=data,
                encoding=encoding,
            )
        return True
    except Exception:
        return False


# ---------- Auto-Export ---------- #

# Auto-Export all non-private symbols
__all__: Final[list[str]] = [
    key
    for (
        key,
        value,
    ) in globals().items()
    if not key.startswith("_") and callable(value)
]
