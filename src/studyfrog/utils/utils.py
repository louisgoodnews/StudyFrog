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

from common.constants import (
    ANSI_BLUE,
    ANSI_CYAN,
    ANSI_DEFAULT,
    ANSI_GREEN,
    ANSI_MAGENTA,
    ANSI_RED,
    ANSI_YELLOW,
)


# ---------- Constants ---------- #

COLORIZATION: Final[dict[str, str]] = {
    "CRITICAL": ANSI_MAGENTA,
    "DEBUG": ANSI_BLUE,
    "DEFAULT": ANSI_DEFAULT,
    "ERROR": ANSI_RED,
    "INFO": ANSI_GREEN,
    "TRACE": ANSI_CYAN,
    "WARNING": ANSI_YELLOW,
}

LOCK: Final[threading.Lock] = threading.Lock()

NAME: Final[Literal["utils.utils"]] = "utils.utils"

SUBSCRIPTIONS: Final[dict[str, dict[str, list[dict[str, Any]]]]] = {}


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


def generate_model_key(
    name: str,
    index: int,
) -> str:
    """
    Generates a key for a model.

    Args:
        name (str): The name of the model.
        index (int): The index of the model.

    Returns:
        str: The generated key.

    Raises:
        ValueError: If the name is empty.
    """

    if is_string_empty(string=name):
        raise ValueError("Name cannot be empty.")

    return f"{name.upper()}_{index}"


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


def get_length_of_obj(obj: Any) -> Optional[int]:
    """
    Returns the length of an object.

    Args:
        obj (Any): The object to get the length of.

    Returns:
        Optional[int]: The length of the object or None if the object has no length.

    Raises:
        ValueError: If the object has no length.
    """

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


def get_widget_child(
    widget: tkinter.Widget,
    **kwargs,
) -> Optional[tkinter.Widget]:
    """
    Returns the child of a widget.

    Args:
        widget (tkinter.Widget): The widget who's child should be returned.
        **kwargs: Keyword arguments.

    Returns:
        Optional[tkinter.Widget]: The child of the passed widget or None if no child was found.
    """

    for widget in get_widget_children(widget=widget):
        if not all(
            (widget[key] == kwargs[key] for key in kwargs),
        ):
            continue

        return widget

    return None


def get_widget_children(widget: tkinter.Widget) -> list[tkinter.Widget]:
    """
    Returns the children of a widget.

    Args:
        widget (tkinter.Widget): The widget who's children should be returned.

    Returns:
        list[tkinter.Widget]: A list containing the children of the passed widget.
    """

    return widget.winfo_children()


def get_widget_children_count(widget: tkinter.Widget) -> int:
    """
    Returns the number of children of a widget.

    Args:
        widget (tkinter.Widget): The widget who's children count should be returned.

    Returns:
        int: The number of children of the passed widget.
    """

    return len(get_widget_children(widget=widget))


def get_widget_height(widget: tkinter.Widget) -> int:
    """
    Returns the height of a widget.

    Args:
        widget (tkinter.Widget): The widget who's height should be returned.

    Returns:
        int: The height of the passed widget.
    """

    widget.update_idletasks()

    return widget.winfo_height()


def get_widget_required_height(widget: tkinter.Widget) -> int:
    """
    Returns the required height of a widget.

    Args:
        widget (tkinter.Widget): The widget who's required height should be returned.

    Returns:
        int: The required height of the passed widget.
    """

    widget.update_idletasks()

    return widget.winfo_reqheight()


def get_widget_width(widget: tkinter.Widget) -> int:
    """
    Returns the width of a widget.

    Args:
        widget (tkinter.Widget): The widget who's width should be returned.

    Returns:
        int: The width of the passed widget.
    """

    widget.update_idletasks()

    return widget.winfo_width()


def get_widget_required_width(widget: tkinter.Widget) -> int:
    """
    Returns the required width of a widget.

    Args:
        widget (tkinter.Widget): The widget who's required width should be returned.

    Returns:
        int: The required width of the passed widget.
    """

    widget.update_idletasks()

    return widget.winfo_reqwidth()


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


def is_equal(
    value: Any,
    other: Any,
) -> bool:
    """
    Returns True if the value is equal to the other, False otherwise.

    Args:
        value (Any): The value to compare.
        other (Any): The other value to compare.

    Returns:
        bool: True if the value is equal to the other, False otherwise.
    """

    return value == other


def is_greater_than(
    value: Any,
    other: Any,
) -> bool:
    """
    Returns True if the value is greater than the other, False otherwise.

    Args:
        value (Any): The value to compare.
        other (Any): The other value to compare.

    Returns:
        bool: True if the value is greater than the other, False otherwise.
    """

    if not hasattr(
        value,
        "__gt__",
    ) or not hasattr(
        other,
        "__gt__",
    ):
        raise ValueError("Value and other must support the greater than operator.")

    return value > other


def is_greater_than_or_equal(
    value: Any,
    other: Any,
) -> bool:
    """
    Returns True if the value is greater than or equal to the other, False otherwise.

    Args:
        value (Any): The value to compare.
        other (Any): The other value to compare.

    Returns:
        bool: True if the value is greater than or equal to the other, False otherwise.
    """

    if not hasattr(
        value,
        "__ge__",
    ) or not hasattr(
        other,
        "__ge__",
    ):
        raise ValueError("Value and other must support the greater than or equal to operator.")

    return value >= other


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


def is_less_than(
    value: Any,
    other: Any,
) -> bool:
    """
    Returns True if the value is less than the other, False otherwise.

    Args:
        value (Any): The value to compare.
        other (Any): The other value to compare.

    Returns:
        bool: True if the value is less than the other, False otherwise.
    """

    if not hasattr(
        value,
        "__lt__",
    ) or not hasattr(
        other,
        "__lt__",
    ):
        raise ValueError("Value and other must support the less than operator.")

    return value < other


def is_less_than_or_equal(
    value: Any,
    other: Any,
) -> bool:
    """
    Returns True if the value is less than or equal to the other, False otherwise.

    Args:
        value (Any): The value to compare.
        other (Any): The other value to compare.

    Returns:
        bool: True if the value is less than or equal to the other, False otherwise.
    """

    if not hasattr(
        value,
        "__le__",
    ) or not hasattr(
        other,
        "__le__",
    ):
        raise ValueError("Value and other must support the less than or equal to operator.")

    return value <= other


def is_list_empty(list_: list[Any]) -> bool:
    """
    Returns True if the list is empty, False otherwise.

    Args:
        list_ (list[Any]): The list to check.

    Returns:
        bool: True if the list is empty, False otherwise.
    """

    return not list_


def is_not_equal(
    value: Any,
    other: Any,
) -> bool:
    """
    Returns True if the value is not equal to the other, False otherwise.

    Args:
        value (Any): The value to compare.
        other (Any): The other value to compare.

    Returns:
        bool: True if the value is not equal to the other, False otherwise.
    """

    return value != other


def is_string_empty(string: str) -> bool:
    """
    Returns True if the string is empty, False otherwise.

    Args:
        string (str): The string to check.

    Returns:
        bool: True if the string is empty, False otherwise.
    """

    return not string


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
    message: Any,
    name: str,
    level: str = "DEFAULT",
) -> None:
    """
    Logs a message.

    Args:
        level (str): The level at which to log the message. Influences colorized display. Defaults to "DEFAULT"
        message (Any): The message to log.
        name (str): The name under which to log.

    Returns:
        None
    """

    global COLORIZATION

    color: str = COLORIZATION.get(
        level.upper(),
        COLORIZATION.get("DEFAULT"),
    )

    if not isinstance(
        message,
        str,
    ):
        message = str(message)

    print(
        f"{color}{get_now_str()} - [{level.upper()}] - [{name.upper()}]: {message};{COLORIZATION["DEFAULT"]}"
    )


def log_critical(
    message: Any,
    name: str,
) -> None:
    """
    Logs a message at the "CRITICAL" level.

    Args:
        message (Any): The message to log.
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
    message: Any,
    name: str,
) -> None:
    """
    Logs a message at the "DEBUG" level.

    Args:
        message (Any): The message to log.
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
    message: Any,
    name: str,
) -> None:
    """
    Logs a message at the "ERROR" level.

    Args:
        message (Any): The message to log.
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
    message: Any,
    name: str,
) -> None:
    """
    Logs an exception at the "ERROR" level.

    Args:
        exception (Exception): The exception to log.
        message (Any): The message to log.
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
    message: Any,
    name: str,
) -> None:
    """
    Logs a message at the "INFO" level.

    Args:
        message (Any): The message to log.
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
    message: Any,
    name: str,
) -> None:
    """
    Logs a message at the "TRACE" level.

    Args:
        message (Any): The message to log.
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
    message: Any,
    name: str,
) -> None:
    """
    Logs a message at the "WARNING" level.

    Args:
        message (Any): The message to log.
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
    namespace: str = "GLOBAL",
    *args,
    **kwargs,
) -> dict[str, Any]:
    """
    Publishes an event to all subscribers.

    Args:
        event (str): The event to publish.
        namespace (str): The namespace to publish the event to.
        *args: The arguments to pass to the subscribers.
        **kwargs: The keyword arguments to pass to the subscribers.

    Returns:
        dict[str, list[dict[str, Any]]]: A mapping from function name to a list
            of results, each with:
                - "uuid": the subscription UUID
                - "result": the return value of the subscriber
    """

    result: dict[str, Any] = {}

    result["event"] = event
    result["namespace"] = namespace
    result["args"] = args
    result["kwargs"] = kwargs

    if not is_key_in_dict(
        key=event,
        dictionary=SUBSCRIPTIONS,
    ):
        return result

    if not is_key_in_dict(
        key=namespace,
        dictionary=SUBSCRIPTIONS[event],
    ):
        return result

    result["start"] = get_now()
    result["subscribers"] = len(SUBSCRIPTIONS[event][namespace])

    for subscription in list(
        sorted(
            SUBSCRIPTIONS[event][namespace],
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
                    "success": True,
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

            result[function.__name__].append(
                {
                    "uuid": subscription["uuid"],
                    "result": None,
                    "success": False,
                }
            )

    result["end"] = get_now()
    result["duration"] = f"{(result["end"] - result["start"]).total_seconds()} seconds"

    result["start"] = result["start"].isoformat()
    result["end"] = result["end"].isoformat()

    return result


def register_subscription(
    event: str,
    function: Callable[..., Any],
    namespace: str = "GLOBAL",
    persistent: bool = False,
    priority: int = 0,
) -> str:
    """
    Registers a subscription to an event.

    Args:
        event (str): The event to subscribe to.
        function (Callable[..., Any]): The function to call when the event is triggered.
        namespace (str): The namespace to subscribe to.
        persistent (bool): Whether the subscription should be persistent.
        priority (int): The priority of the subscription.

    Returns:
        str: The UUID of the subscription.

    Raises:
        ValueError: If the priority is not between 0 and 100.
    """

    try:
        if not 0 <= priority <= 100:
            raise ValueError("Priority must be between 0 and 100.")

        if not is_key_in_dict(
            key=event,
            dictionary=SUBSCRIPTIONS,
        ):
            SUBSCRIPTIONS[event] = {}

        if not is_key_in_dict(
            key=namespace,
            dictionary=SUBSCRIPTIONS[event],
        ):
            SUBSCRIPTIONS[event][namespace] = []

        uuid: str = get_uuid_str()

        SUBSCRIPTIONS[event][namespace].append(
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

    try:
        return datetime.fromisoformat(datetime_string)
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to convert string to datetime.",
        )
        return None


def string_to_human_case(string: str) -> str:
    """
    Converts a given string to human case.

    Args:
        string (str): The string to convert to human case.

    Returns:
        str: The human case version of the input string.
    """

    if "_" in string:
        string.replace("_", " ")

    if "-" in string:
        string.replace("-", " ")

    return string.title()


def string_to_snake_case(string: str) -> str:
    """
    Converts a given string to snake case.

    Args:
        string (str): The string to convert to snake case.

    Returns:
        str: The snake case version of the input string.
    """

    result: str = ""

    for (
        index,
        char,
    ) in enumerate(iterable=string):
        if char == " ":
            continue

        if char.isupper() and index > 0:
            result += "_"

        result += char.lower()

    return result


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
            namespace,
            subscriptions,
        ) in list(subscriptions.items()):
            for (
                index,
                subscription,
            ) in enumerate(iterable=subscriptions):
                if subscription["uuid"] != uuid:
                    continue

                del subscriptions[index]
                return True

            if not SUBSCRIPTIONS[event][namespace]:
                del SUBSCRIPTIONS[event][namespace]

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
                data=json.dumps(
                    data,
                    indent=4,
                    sort_keys=True,
                ),
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
