"""
Author: Louis Goodnews
Date: 2025-11-16
"""

import json
import sys
import threading
import tkinter
import traceback
import uuid

from datetime import date, datetime
from pathlib import Path
from typing import Any, Callable, Final, Literal, Optional


# ---------- Constants ---------- #

COLORIZATION: Final[dict[str, str]] = {
    "BOLD": "\033[1m",
    "CRITICAL": "\033[35m",
    "DEBUG": "\033[36m",
    "DEFAULT": "\033[0m",
    "ERROR": "\033[31m",
    "INFO": "\033[32m",
    "ITALIC": "\033[3m",
    "TRACE": "\033[34m",
    "UNDERLINED": "\033[4m",
    "WARNING": "\033[33m",
}

LOCK: Final[threading.Lock] = threading.Lock()

NAME: Final[Literal["utils.utils"]] = "utils.utils"

SUBSCRIPTIONS: Final[dict[str, list[dict[str, Any]]]] = {}


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

    global NAME

    try:
        path.mkdir(exist_ok=True)
        return True
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to ensure directory.",
        )
        return False


def ensure_file(path: Path) -> bool:
    """
    Ensures that a file exists at the specified path.

    Args:
        path (Path): The path to the file.

    Returns:
        bool: True if the file exists, False otherwise.
    """

    global NAME

    try:
        ensure_dir(path.parent)
        path.touch(exist_ok=True)
        return True
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to ensure file.",
        )
        return False


def ensure_json(path: Path) -> bool:
    """
    Ensures that a JSON file exists at the specified path.

    Args:
        path (Path): The path to the JSON file.

    Returns:
        bool: True if the JSON file exists, False otherwise.
    """

    global NAME

    try:
        ensure_dir(path.parent)
        if not path.exists():
            path.write_text(
                data="{}",
                encoding="utf-8",
            )
        return True
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to ensure JSON file.",
        )
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

    global NAME

    try:
        path.mkdir(
            exist_ok=True,
            parent=True,
        )
        return True
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to get directory.",
        )
        return False


def get_file(path: Path) -> bool:
    """
    Ensures that a file exists at the specified path.

    Args:
        path (Path): The path to the file.

    Returns:
        bool: True if the file exists, False otherwise.
    """

    global NAME

    try:
        path.touch()
        return True
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to get file.",
        )
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
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to get file content as bytes.",
        )
        return None


def get_file_content_json(path: Path) -> Optional[dict[str, Any]]:
    """
    Returns the content of a file as a JSON object.

    Args:
        path (Path): A Path object pointing to the location from which the file contents are to be read.

    Returns:
        Optional[dict[str, Any]]: The content of the file as a JSON object or None if reading the file fails.
    """

    global LOCK

    try:
        with LOCK:
            return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to get file content as JSON.",
        )
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
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to get file content as string.",
        )
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


def get_length_of_obj(obj: Any) -> int:
    """
    Returns the length of an object.

    Args:
        obj (Any): The object to get the length of.

    Returns:
        int: The length of the object.

    Raises:
        ValueError: If the object has no length.
    """

    global NAME

    try:
        if not hasattr(
            obj,
            "__len__",
        ):
            raise ValueError("Object has no length.")

        return len(obj)
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to get length of object.",
        )
        return None


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


def get_size_of_obj(obj: Any) -> int:
    """
    Returns the size of an object in bytes.

    Args:
        obj (Any): The object to get the size of.

    Returns:
        int: The size of the object in bytes.
    """

    return sys.getsizeof(obj)


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


def invert_dict(dictionary: dict[str, Any]) -> dict[Any, str]:
    """
    Returns the inverse of a dictionary.

    Args:
        dictionary (dict[str, Any]): The dictionary to invert.

    Returns:
        dict[Any, str]: The inverse of the passed dictionary.

    Raises:
        Exception: If inversion of the dictionary fails.
    """

    global NAME

    try:
        return {
            value: key
            for (
                key,
                value,
            ) in dictionary.items()
        }
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to invert dictionary.",
        )
        return None


def is_dict_empty(dictionary: dict[str, Any]) -> bool:
    """
    Returns True if the dictionary is empty, False otherwise.

    Args:
        dictionary (dict[str, Any]): The dictionary to check.

    Returns:
        bool: True if the dictionary is empty, False otherwise.
    """

    return not dictionary


def is_item_in_list(
    item: Any,
    list_: list[Any],
) -> bool:
    """
    Returns True if the item is in the list, False otherwise.

    Args:
        item (Any): The item to check.
        list_ (list[Any]): The list to check.

    Returns:
        bool: True if the item is in the list, False otherwise.
    """

    return item in list_


def is_item_in_tuple(
    item: Any,
    tuple_: tuple[Any, ...],
) -> bool:
    """
    Returns True if the item is in the tuple, False otherwise.

    Args:
        item (Any): The item to check.
        tuple_ (tuple[Any, ...]): The tuple to check.

    Returns:
        bool: True if the item is in the tuple, False otherwise.
    """

    return item in tuple_


def is_key_in_dict(
    key: str,
    dictionary: dict[str, Any],
) -> bool:
    """
    Returns True if the key is in the dictionary, False otherwise.

    Args:
        key (str): The key to check.
        dictionary (dict[str, Any]): The dictionary to check.

    Returns:
        bool: True if the key is in the dictionary, False otherwise.
    """

    return key in dictionary


def is_list_empty(list_: list[Any]) -> bool:
    """
    Returns True if the list is empty, False otherwise.

    Args:
        list_ (list[Any]): The list to check.

    Returns:
        bool: True if the list is empty, False otherwise.
    """

    return not list_


def is_tuple_empty(tuple_: tuple[Any, ...]) -> bool:
    """
    Returns True if the tuple is empty, False otherwise.

    Args:
        tuple_ (tuple[Any, ...]): The tuple to check.

    Returns:
        bool: True if the tuple is empty, False otherwise.
    """

    return not tuple_


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
        f"{color}{get_now_str()} - [{level.upper()}] - [{name.upper()}]: {message}{COLORIZATION["DEFAULT"]};"
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
    message: str,
    name: str,
) -> None:
    """
    Logs an exception at the "ERROR" level.

    Args:
        exception (Exception): The exception to log.
        message (str): The message to log.
        name (str): The name under which to log.

    Returns:
        None
    """

    log(
        level="ERROR",
        message=f"{message}\n{exception}\n{traceback.format_exc()}",
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


def log_trace(
    message: str,
    name: str,
) -> None:
    """
    Logs a message at the "TRACE" level.

    Args:
        message (str): The message to log.
        name (str): The name under which to log.

    Returns:
        None
    """

    log(
        level="TRACE",
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


def pluralize_str(string: str) -> str:
    """
    Pluralizes a string.

    Args:
        string (str): The string to pluralize.

    Returns:
        str: The pluralized string.
    """

    if string.endswith("y"):
        return string[:-1] + "ies"

    if string.endswith("s"):
        return string + "es"

    return string + "s"


def publish_event(
    event: str,
    *args,
    **kwargs,
) -> dict[str, Any]:
    """
    Publishes an event to all subscribers.

    Args:
        event (str): The event to publish.
        *args: The arguments to pass to the subscribers.
        **kwargs: The keyword arguments to pass to the subscribers.

    Returns:
        dict[str, list[dict[str, Any]]]: A mapping from function name to a list
            of results, each with:
                - "uuid": the subscription UUID
                - "result": the return value of the subscriber
    """

    result: dict[str, Any] = {}

    if not is_key_in_dict(
        key=event,
        dictionary=SUBSCRIPTIONS,
    ):
        return result

    for subscription in list(
        sorted(
            SUBSCRIPTIONS[event],
            key=lambda x: x["priority"],
            reverse=True,
        ),
    ):
        function: Callable[..., Any] = subscription["function"]

        if not is_key_in_dict(
            key=function.__name__,
            dictionary=result,
        ):
            result[function.__name__] = []

        try:
            result[function.__name__].append(
                {
                    "uuid": subscription["uuid"],
                    "result": function(
                        *args,
                        **kwargs,
                    ),
                }
            )

            if not subscription["persistent"]:
                unsubscribe_subscription(uuid=subscription["uuid"])

        except Exception as e:
            log_exception(
                exception=e,
                name=NAME,
                message=f"Failed to publish event: {event}",
            )

    return result


def register_subscription(
    event: str,
    function: Callable[..., Any],
    persistent: bool = False,
    priority: int = 0,
) -> str:
    """
    Registers a subscription to an event.

    Args:
        event (str): The event to subscribe to.
        function (Callable[..., Any]): The function to call when the event is triggered.
        persistent (bool): Whether the subscription should be persistent.
        priority (int): The priority of the subscription.

    Returns:
        str: The UUID of the subscription.

    Raises:
        ValueError: If the priority is not between 0 and 100.
    """

    try:
        if not 0 < priority < 100:
            raise ValueError("Priority must be between 0 and 100.")

        if not is_key_in_dict(
            key=event,
            dictionary=SUBSCRIPTIONS,
        ):
            SUBSCRIPTIONS[event] = []

        uuid: str = get_uuid_str()

        SUBSCRIPTIONS[event].append(
            {
                "function": function,
                "persistent": persistent,
                "priority": priority,
                "uuid": uuid,
            }
        )

        return uuid
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to register subscription: {event}",
        )
        raise Exception(f"Failed to register subscription: {e}") from e


def str_to_date(date_string: str) -> Optional[date]:
    """
    Converts a string to a date object.

    Args:
        date_string (str): The string to convert.

    Returns:
        Optional[date]: The date object or None if the conversion failed.
    """

    global NAME

    try:
        return date.fromisoformat(date_string)
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to convert string to date.",
        )
        return None


def str_to_datetime(datetime_string: str) -> Optional[datetime]:
    """
    Converts a string to a datetime object.

    Args:
        datetime_string (str): The string to convert.

    Returns:
        Optional[datetime]: The datetime object or None if the conversion failed.
    """

    global NAME

    try:
        return datetime.fromisoformat(datetime_string)
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to convert string to datetime.",
        )
        return None


def unsubscribe_subscription(uuid: str) -> bool:
    """
    Unsubscribes from an event.

    Args:
        uuid (str): The UUID of the subscription to unsubscribe from.

    Returns:
        bool: True if the subscription was unsubscribed successfully, False otherwise.
    """

    for (
        event,
        subscriptions,
    ) in list(SUBSCRIPTIONS.items()):
        for (
            index,
            subscription,
        ) in enumerate(iterable=subscriptions):
            if subscription["uuid"] != uuid:
                continue

            del subscriptions[index]
            return True

        if not SUBSCRIPTIONS[event]:
            del SUBSCRIPTIONS[event]

    return False


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

    global LOCK, NAME

    try:
        with LOCK:
            path.write_bytes(data=data)
        return True
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to write bytes to file.",
        )
        return False


def write_file_json(
    data: dict[str, Any],
    path: Path,
) -> bool:
    """
    Writes a JSON object to a specified file.

    Args:
        data (dict[str, Any]): The data to write to the file.
        path (Path): The path to the file.

    Returns:
        bool: True if the file was written successfully, False otherwise.
    """

    global LOCK

    try:
        with LOCK:
            path.write_text(
                data=json.dumps(data),
                encoding="utf-8",
            )
        return True
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to write JSON to file.",
        )
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
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to write string to file.",
        )
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
