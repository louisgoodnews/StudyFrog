"""
Author: Louis Goodnews
Date: 2025-12-10
"""

import json
from pathlib import Path
import random
import re
import uuid

from datetime import date, datetime
from typing import Any, Final, Optional, Union


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "create_rgb_bg_color",
    "create_rgb_fg_color",
    "exists",
    "date_from_string",
    "datetime_from_string",
    "find_string",
    "generate_model_key",
    "generate_uuid4",
    "generate_uuid4_str",
    "get_now",
    "get_now_str",
    "get_today",
    "get_today_str",
    "is_empty",
    "is_none",
    "is_none_or_empty",
    "is_not_none",
    "is_not_none_or_empty",
    "match_string",
    "model_key_to_model_type",
    "path_from_string",
    "pluralize_word",
    "search_string",
    "shuffle_list",
    "simple_dict_to_string",
    "simple_string_to_dict",
    "singularize_word",
    "string_to_snake_case",
    "uuid_from_string",
]


# ---------- Functions ---------- #


def create_rgb_bg_color(r: int, g: int, b: int) -> str:
    """
    Returns the ANSI escape code for a background color with the specified RGB values.

    Args:
        r (int): The Red value.
        g (int): The Green value.
        b (int): The Blue value.

    Returns:
        str: The ANSI escape code for the specified RGB values.
    """

    return f"\033[48;2;{r};{g};{b}m"


def create_rgb_fg_color(r: int, g: int, b: int) -> str:
    """
    Returns the ANSI escape code for a foreground color with the specified RGB values.

    Args:
        r (int): The Red value.
        g (int): The Green value.
        b (int): The Blue value.

    Returns:
        str: The ANSI escape code for the specified RGB values.
    """

    return f"\033[38;2;{r};{g};{b}m"


def date_from_string(string: str) -> Optional[date]:
    """
    Attempts to convert a given string into a date object and returns it if conversion was successfull.

    Args:
        string (str): The string to attempt conversion on.

    Returns:
        Optional[date]: The converted date object if conversion was successfull, otherwise None.
    """

    try:
        return date.fromisoformat(string)
    except Exception:
        return None


def datetime_from_string(string: str) -> Optional[datetime]:
    """
    Attempts to convert a given string into a datetime object and returns it if conversion was successfull.

    Args:
        string (str): The string to attempt conversion on.

    Returns:
        Optional[datetime]: The converted datetime object if conversion was successfull, otherwise None.
    """

    try:
        return datetime.fromisoformat(string)
    except Exception:
        return None


def exists(value: Any) -> bool:
    """
    Returns True if the given value exists, False otherwise.

    A value exists if it is not None and is not an empty string.
    If the value is 0 or False, it is considered to exist.

    Args:
        value (Any): The value to check.

    Returns:
        bool: True if the value exists, False otherwise.
    """

    if value == 0 or value is False:
        return True

    return bool(value)


def find_string(
    string: str,
    pattern: str,
    flags: Optional[int] = None,
) -> Optional[list[str]]:
    """
    Filters a given string against a matching pattern.

    Args:
        string (str): The string to filter.
        pattern (str): The pattern to filter the string against.
        flags (int, optional): The flags to use when matching the pattern. Defaults to None.

    Returns:
        Optional[list[str]]: The filtered string.
    """

    match: Optional[list[str]] = re.findall(
        flags=flags,
        pattern=pattern,
        string=string,
    )

    if not exists(value=match):
        return None

    return match


def generate_model_key(
    id_: int,
    name: str,
) -> str:
    """
    Returns a model key based on a specified name and ID.

    Args:
        id_ (int): The ID to generate the model key with.
        name (str): The name to generate the model key with.

    Returns:
        str: The generated model key in the format "NAME_ID".
    """

    return f"{name.upper()}_{id_}"


def generate_uuid4() -> uuid.UUID:
    """
    Generates a UUID4.

    Args:
        None

    Returns:
        uuid.UUID: The generated UUID4.
    """

    return uuid.uuid4()


def generate_uuid4_str() -> str:
    """
    Generates a UUID4.

    Args:
        None

    Returns:
        str: The generated UUID4 as a string.
    """

    return str(generate_uuid4())


def get_now() -> datetime:
    """
    Returns the current date and time as datetime object.

    Args:
        None

    Returns:
        datetime: The current date and time.
    """

    return datetime.now()


def get_now_str() -> str:
    """
    Returns the current date and time as an ISO format string.

    Args:
        None

    Returns:
        str: The current date and time as an ISO format string.
    """

    return get_now().isoformat()


def get_today() -> date:
    """
    Returns the current date as a date object.

    Args:
        None

    Returns:
        date: The current date.
    """

    return get_now().date()


def get_today_str() -> str:
    """
    Returns the current date as an ISO format string.

    Args:
        None

    Returns:
        str: The current date as an ISO format string.
    """

    return get_today().isoformat()


def is_empty(obj: Any) -> bool:
    """
    Returns true if the passed object is empty, False otherwise.

    Args:
        obj (Any): The object to check.

    Returns:
        bool: True if the object is empty, False otherwise.
    """

    if hasattr(
        obj,
        "__len__",
    ):
        return len(obj) == 0

    return False


def is_none(obj: Any) -> bool:
    """
    Returns true if the passed object is None, False otherwise.

    Args:
        obj (Any): The object to check.

    Returns:
        bool: True if the object is None, False otherwise.
    """

    return obj is None


def is_none_or_empty(obj: Any) -> None:
    """
    Returns true if the passed object is None or empty, False otherwise.

    Args:
        obj (Any): The object to check.

    Returns:
        bool: True if the object is None or empty, False otherwise.
    """

    if isinstance(
        obj,
        str,
    ):
        return is_none(obj=obj) or obj == ""
    elif isinstance(
        obj,
        (
            dict,
            list,
            set,
            tuple,
        ),
    ):
        return is_none(obj=obj) or len(obj) == 0
    return is_none(obj=obj)


def is_not_none(obj: Any) -> bool:
    """
    Returns true if the passed object is not None, False otherwise.

    Args:
        obj (Any): The object to check.

    Returns:
        bool: True if the object is not None, False otherwise.
    """

    return obj is not None


def is_not_none_or_empty(obj: Any) -> None:
    """
    Returns true if the passed object is not None or empty, False otherwise.

    Args:
        obj (Any): The object to check.

    Returns:
        bool: True if the object is not None or empty, False otherwise.
    """

    if isinstance(
        obj,
        str,
    ):
        return is_not_none(obj=obj) and obj != ""
    elif isinstance(
        obj,
        (
            dict,
            list,
            set,
            tuple,
        ),
    ):
        return is_not_none(obj=obj) and len(obj) > 0

    return is_not_none(obj=obj)


def match_string(
    string: str,
    pattern: str,
    flags: Optional[int] = None,
) -> Optional[str]:
    """
    Filters a given string against a matching pattern.

    Args:
        string (str): The string to filter.
        pattern (str): The pattern to filter the string against.
        flags (int, optional): The flags to use when matching the pattern. Defaults to None.

    Returns:
        Optional[str]: The filtered string.
    """

    match: Optional[re.Match[str]] = re.match(
        flags=flags,
        pattern=pattern,
        string=string,
    )

    if not exists(value=match):
        return None

    return match.group()


def model_key_to_model_type(
    model_key: str,
    as_lower_case: bool = True,
) -> str:
    """
    Retrieves the model type from a model key.

    Args:
        model_key (str): The model key to retrieve the model type from.
        as_lower_case (bool, optional): Whether to retrieve the model type
            as a lower case string. Defaults to True.

    Returns:
        str: The model type.
    """

    return (
        model_key.rsplit("_", 1)[0].lower()
        if as_lower_case
        else model_key.rsplit("_", 1)[0].upper()
    )


def path_from_string(string: str) -> Optional[Path]:
    """
    Attempts to convert a given string into a resolved Path object.

    Args:
        string (str): The string to attempt conversion on.

    Returns:
        Optional[Path]: The resolved Path object if conversion was successful, otherwise None.

    Raises:
        Exception: If an exception is caught while attempting to convert the string into a Path.
    """

    try:
        path: Path = Path(string)

        return path.resolve()
    except Exception:
        return None


def pluralize_word(word: str) -> str:
    """
    Pluralizes an English word based on simplified rules.

    Args:
        word (str): The word to pluralize.

    Returns:
        str: The word in plural form.
    """

    if word.endswith(("s", "ss", "sh", "ch", "x", "z")):
        return word + "es"

    if word.endswith("y") and word[-2] not in ("a", "e", "i", "o", "u"):
        return word[:-1] + "ies"

    return word + "s"


def search_string(
    string: str,
    pattern: str,
    flags: Optional[int] = None,
) -> Optional[str]:
    """
    Filters a given string against a matching pattern.

    Args:
        string (str): The string to filter.
        pattern (str): The pattern to filter the string against.
        flags (int, optional): The flags to use when matching the pattern. Defaults to None.

    Returns:
        Optional[str]: The filtered string.
    """

    match: Optional[re.Match[str]] = re.search(
        flags=flags,
        pattern=pattern,
        string=string,
    )

    if not exists(value=match):
        return None

    return match.group()


def shuffle_list(list_: list[Any]) -> None:
    """
    Shuffles a given list.

    Args:
        list_ (list[Any]): The list to shuffle.

    Returns:
        None
    """

    random.shuffle(list_)


def simple_dict_to_string(dict_or_list: Union[dict[str, Any], list[Any]]) -> str:
    """
    Converts a given dictionary or list into a string.

    Args:
        dict_or_list (Union[dict[str, Any], list[Any]]): The dictionary or list to convert.

    Returns:
        str: The converted string.
    """

    return json.dumps(dict_or_list)


def simple_string_to_dict(string: str) -> Optional[Union[dict[str, Any], list[Any]]]:
    """
    Attempts to convert a string into a dicionary or list and returns if upon success.

    Args:
        string (str): The string to attempt the conversion on.

    Returns:
        Optional[Union[dict[str, Any], list[Any]]]: The converted dictionary or list.
    """

    try:
        return json.loads(string)
    except ValueError:
        return None


def singularize_word(word: str) -> str:
    """
    Singularizes an English word based on simplified rules (reversing pluralize_word).

    Args:
        word (str): The word to singularize.

    Returns:
        str: The word in singular form.
    """

    if word.endswith("ies") and len(word) > 3:
        return word[:-3] + "y"

    if word.endswith("es") and len(word) > 2:
        return word[:-2]

    if word.endswith("s") and len(word) > 1:
        if word.endswith(("es", "ies")):
            return word

        return word[:-1]

    return word


def string_to_snake_case(string: str) -> str:
    """
    Returns a snake case representation of the passed string.

    Args:
        string (str): The string to convert to snake case.

    Returns:
        str: The snake case representation of the passed string.
    """

    return string.replace(" ", "_").lower()


def uuid_from_string(string: str) -> Optional[uuid.UUID]:
    """
    Attempts to convert a given string into a UUID object.

    Args:
        string (str): The string to convert into a UUID object.

    Returns:
        Optional[uuid.UUID]: The UUID object if the conversion was successful, None otherwise.
    """

    try:
        return uuid.UUID(
            hex=string,
            version=4,
        )
    except (ValueError, AttributeError, TypeError):
        return None
