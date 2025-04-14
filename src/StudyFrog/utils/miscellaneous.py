"""
Author: lodego
Date: 2025-02-06
"""

import asyncio
import json
import random
import re
import threading
import uuid

from typing import *

from datetime import datetime, timedelta

from utils.logger import Logger


__all__: Final[List[str]] = ["Miscellaneous"]


class Miscellaneous:
    """
    A class containing miscellaneous utility methods.

    This class provides a set of methods that can be used to perform various
    utility operations, such as converting between different string formats,
    formatting dates and times, and more.

    Attributes:
        logger (Logger): The logger instance associated with the Miscellaneous class.
    """

    logger: Final[Logger] = Logger.get_logger(name="Miscellaneous")

    @classmethod
    def any_to_camel(
        cls,
        string: str,
    ) -> str:
        """
        Converts any string to camelCase.

        Args:
            string (str): The string to be converted.

        Returns:
            str: The camelCase version of the input string.
        """
        return string.lower().replace(" ", "").replace("_", " ")

    @classmethod
    def any_to_snake(
        cls,
        string: str,
    ) -> str:
        """
        Converts any string to snake_case.

        Args:
            string (str): The string to be converted.

        Returns:
            str: The snake_case version of the input string.
        """
        return string.strip().lower().replace(" ", "_")

    @classmethod
    def camel_to_pascal(
        cls,
        string: str,
    ) -> str:
        """
        Converts a camelCase string to PascalCase.

        Args:
            string (str): The camelCase string to be converted.

        Returns:
            str: The PascalCase version of the input string.
        """
        return "".join(x.capitalize() for x in string.split("_"))

    @classmethod
    def camel_to_snake(
        cls,
        string: str,
    ) -> str:
        """
        Converts a camelCase string to snake_case.

        Args:
            string (str): The camelCase string to be converted.

        Returns:
            str: The snake_case version of the input string.
        """
        return "".join(["_" + i.lower() if i.isupper() else i for i in string]).strip(
            "_"
        )

    @classmethod
    def convert_from_db_format(
        cls,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Converts a dictionary's values from a database format back to Python-native types.

        Args:
            data (Dict[str, Any]): The dictionary containing values to be converted.

        Returns:
            Dict[str, Any]: The dictionary with converted values.
        """
        try:
            # Initialize an empty dictionary to store the converted values
            result: Dict[str, Any] = {}

            # Iterate over the keys and values in the dictionary
            for (
                key,
                value,
            ) in data.items():
                # Check, if the current value is a JSON string
                if cls.is_json_string(string=value):
                    # Convert the JSON string into a JSON object
                    result[key] = json.loads(s=value)

                # Check, if the current value is a datetime string
                if cls.is_datetime_string(string=value):
                    # Convert the datetime string into a datetime object
                    result[key] = cls.string_to_datetime(date_string=value)

                # Keep unchanged if no conversion applied
                result[key] = value

            # Return the converted dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'convert_from_db_format' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def convert_to_db_format(
        cls,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Converts a dictionary's values to a database-friendly format.

        Args:
            data (Dict[str, Any]): The dictionary containing values to be converted.

        Returns:
            Dict[str, Any]: The dictionary with converted values.
        """
        try:
            # Initialize an empty dictionary to store the converted values
            result: Dict[str, Any] = {}

            # Iterate over the keys and values in the dictionary
            for (
                key,
                value,
            ) in data.items():
                # Check if the value is a datetime object
                if isinstance(
                    value,
                    datetime,
                ):
                    # Convert the datetime object to a string
                    result[key] = cls.datetime_to_string(datetime=value)
                # Check if the value is a list or dictionary
                elif isinstance(
                    value,
                    (
                        dict,
                        list,
                    ),
                ):
                    # Convert the list or dictionary to a JSON string
                    result[key] = json.dumps(
                        value
                    )  # Convert lists and dictionaries to JSON strings
                else:
                    result[key] = value  # Keep other values unchanged

            # Return the converted dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'convert_to_db_format' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def datetime_to_string(
        cls,
        datetime: datetime,
        format: str = "%Y-%m-%d %H:%M:%S",
    ) -> str:
        """
        Converts a datetime object to a string representation of a date and time.

        Args:
            datetime (datetime): The datetime object to be converted.
            format (str): The format of the string representation of the date and time. Defaults to "%Y-%m-%d %H:%M:%S".

        Returns:
            str: The string representation of the datetime object.
        """
        return datetime.strftime(format=format)

    @classmethod
    def detect_date_format(
        cls,
        date_input: Union[str, datetime],
    ) -> Optional[str]:
        """
        Detects the format of a given date input.

        Args:
            date_input (Union[str, datetime]): A date string or datetime object.

        Returns:
            Optional[str]: The detected date format string (e.g., "%d.%m.%Y") or None if detection fails.
        """

        # Check, if the passed date tnput is a datetime object
        if isinstance(
            date_input,
            datetime,
        ):
            # Use ISO by default for datetime objects
            return "%Y-%m-%d %H:%M:%S"

        # List containing various date formats
        date_formats: List[str] = [
            "%d.%m.%Y",
            "%d.%m.%y",
            "%Y-%m-%d",
            "%y-%m-%d",
            "%m/%d/%Y",
            "%d/%m/%Y",
            "%d %b %Y",
            "%d %B %Y",
            "%b %d, %Y",
            "%B %d, %Y",
        ]

        # Iterate over the list of dateformats
        for format in date_formats:
            try:
                # Attempt to creaate a datetime object from the input string and format
                _ = datetime.strptime(
                    date_input,
                    format,
                )

                # Return the format string
                return format
            except ValueError:
                # if an exception occurs, skip the current loop iteration
                continue

        # Log a warning message
        cls.logger.warning(f"Could not detect date format for input: {date_input}")

        # Return None
        return None

    @classmethod
    def find_match(
        cls,
        string: str,
        group: int = 0,
        pattern: str = r"([A-Za-z]+)",
    ) -> Optional[str]:
        """
        Finds a match for a string against a pattern.

        Args:
            group (int): The group to return. Defaults to 0 (the whole match).
            pattern (str): The pattern to match the string against. Defaults to r"([A-Za-z]+)" (all letters).
            string (str): The string to match.

        Returns:
            Optional[str]: The string that matched the pattern, or None if no match was found.
        """

        # Find a match for the string against the pattern
        match: Optional[re.Match] = re.match(
            pattern=pattern,
            string=string,
        )

        if not match:
            # Log an error message indicating that no match was found
            cls.logger.error(
                message=f"Failed to find match for string '{string}' with pattern '{pattern}'."
            )

            # Return None indicating no match was found
            return None

        # Return the matched group
        return match.group(group)

    @classmethod
    def get_current_datetime(cls) -> datetime:
        """
        Returns the current datetime.

        Returns:
            datetime: The current datetime.
        """
        return datetime.now()

    @classmethod
    def get_date_decrement(
        cls,
        decrement: int,
    ) -> datetime:
        """
        Returns the current datetime decremented by a given amount.

        Args:
            decrement (int): The amount to decrement the datetime by.

        Returns:
            datetime: The decremented datetime.
        """
        return cls.get_current_datetime() - timedelta(days=decrement)

    @classmethod
    def get_date_increment(
        cls,
        increment: int,
    ) -> datetime:
        """
        Returns the current datetime incremented by a given amount.

        Args:
            increment (int): The amount to increment the datetime by.

        Returns:
            datetime: The incremented datetime.
        """
        return datetime.now() + timedelta(days=increment)

    @classmethod
    def get_random_int(
        cls,
        min: int,
        max: int,
    ) -> int:
        """
        Returns a random integer between min and max (inclusive).

        Args:
            min (int): The minimum value of the random integer.
            max (int): The maximum value of the random integer.

        Returns:
            int: A random integer between min and max (inclusive).
        """
        return random.randint(
            a=min,
            b=max,
        )

    @classmethod
    def get_range(cls, min: int, max: int) -> Tuple[int, ...]:
        """
        Returns a range of integers between min and max (inclusive).

        Args:
            min (int): The minimum value of the range.
            max (int): The maximum value of the range.

        Returns:
            range: A range of integers between min and max (inclusive).
        """
        return tuple(range(min, max + 1))

    @classmethod
    def get_uuid(cls) -> str:
        """
        Returns a new UUID.

        Returns:
            str: A new UUID.
        """
        return str(uuid.uuid4())

    @classmethod
    def is_datetime_string(
        cls,
        string: str,
    ) -> bool:
        """
        Checks whether the given string can be interpreted as a datetime.

        This method tries to parse the string using a list of common datetime formats.
        If one of the formats matches, the string is considered a valid datetime.

        Args:
            string (str): The input string to check.

        Returns:
            bool: True if the string can be parsed as a datetime, False otherwise.
        """

        # Check, if the passed string argument is in fact a string object
        if not isinstance(string, str,):
            # Return False
            return False

        # Strip off any leading or trailing whitespaces
        stripped: str = string.strip()

        # A list of common date formats
        common_formats: List[str] = [
            "%Y-%m-%d %H:%M:%S",  # 2025-04-14 08:57:23
            "%Y-%m-%d",           # 2025-04-14
            "%d.%m.%Y",           # 14.04.2025
            "%d.%m.%y",           # 14.04.25
            "%m/%d/%Y",           # 04/14/2025
            "%Y/%m/%d",           # 2025/04/14
            "%d-%b-%Y",           # 14-Apr-2025
        ]

        # Iterate over the common date formats list
        for format in common_formats:
            try:
                # Attempt to create a datetime object from the string with the format
                datetime.strptime(stripped, format,)

                # Return True
                return True
            except ValueError:
                # Skip the current iteration if an exception occurs
                continue

        # Return False
        return False

    @classmethod
    def is_float_number(
        cls,
        string: str,
    ) -> bool:
        """
        Checks if the given string can be converted to a float number.

        Args:
            string (str): The string to be checked.

        Returns:
            bool: True if the string can be converted to a float number, False otherwise.
        """
        try:
            float(string)
            # If the string can be converted to a float number, return True
            return True
        except ValueError:
            # If the string cannot be converted to a float number, return False
            return False

    @classmethod
    def is_int_number(
        cls,
        string: str,
    ) -> bool:
        """
        Checks if the given string can be converted to an int number.

        Args:
            string (str): The string to be checked.

        Returns:
            bool: True if the string can be converted to an int number, False otherwise.
        """
        try:
            int(string)
            # If the string can be converted to an int number, return True
            return True
        except ValueError:
            # If the string cannot be converted to an int number, return False
            return False

    @classmethod
    def is_json_string(
        cls,
        string: str,
    ) -> bool:
        """
        Checks whether the given string is likely to be a JSON string.

        This method checks if the string starts and ends with curly braces `{}` (indicating a JSON object)
        or square brackets `[]` (indicating a JSON array). It does not validate the full JSON structure,
        but is useful as a lightweight pre-check.

        Args:
            string (str): The input string to check.

        Returns:
            bool: True if the string looks like a JSON object or array, False otherwise.
        """
        if not isinstance(string, str):
            return False

        stripped: str = string.strip()

        return (stripped.startswith("{") and stripped.endswith("}")) or (
            stripped.startswith("[") and stripped.endswith("]")
        )

    @classmethod
    def is_numeric(
        cls,
        string: str,
    ) -> bool:
        """
        Checks if the given string can be converted to a numeric value.

        Args:
            string (str): The string to be checked.

        Returns:
            bool: True if the string can be converted to a numeric value, False otherwise.
        """
        return cls.is_float_number(string=string) or cls.is_int_number(string=string)

    @classmethod
    def pluralize(
        cls,
        string: str,
    ) -> str:
        """
        Returns the plural form of a word.

        Args:
            string (str): The word to pluralize.

        Returns:
            str: The plural form of the word.
        """
        if string.endswith("s"):
            return string
        elif string.endswith("y"):
            return string[:-1] + "ies"
        else:
            return string + "s"

    @classmethod
    def run_asynchronously(
        cls,
        func: Callable[..., Any],
        *args,
        **kwargs,
    ) -> Optional[Any]:
        """
        Runs a function asynchronously.

        Args:
            func (Callable[..., Any]): The function to be run asynchronously.
            *args: Additional positional arguments to be passed to the function.
            **kwargs: Additional keyword arguments to be passed to the function.

        Returns:
            Optional[Any]: The return value of the function or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while running the function.
        """
        try:
            # Attempt to run the function asynchronously and return the result
            return asyncio.run(
                main=func,
                *args,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'run_asynchronously' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def run_in_thread(
        cls,
        func: Callable[..., Any],
        *args,
        **kwargs,
    ) -> Optional[Any]:
        """
        Runs a function in a separate thread.

        Args:
            func (Callable[..., Any]): The function to be run in a separate thread.
            *args: Additional positional arguments to be passed to the function.
            **kwargs: Additional keyword arguments to be passed to the function.

        Returns:
            Optional[Any]: The return value of the function or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while running the function.
        """
        try:
            # Run the function in a separate thread and return the result
            return threading.Thread(
                target=func,
                args=args,
                kwargs=kwargs,
            ).start()
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'run_in_thread' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def select_random(
        cls,
        iterable: Iterable[Any],
    ) -> Any:
        """
        Selects a random element from an iterable.

        Args:
            iterable (Iterable[Any]): The iterable to be selected from.

        Returns:
            Any: The selected element.
        """

        # Select a random element from the iterable
        return random.choice(seq=iterable)

    @classmethod
    def shuffle(iterable: Iterable[Any]) -> None:
        """
        Shuffles an iterable.

        Args:
            iterable (Iterable[Any]): The iterable to be shuffled.

        Returns:
            None
        """
        random.shuffle(iterable)

    @classmethod
    def snake_to_camel(
        cls,
        string: str,
    ) -> str:
        """
        Converts a snake_case string to camelCase.

        Args:
            string (str): The snake_case string to be converted.

        Returns:
            str: The camelCase version of the input string.
        """
        return "".join(
            x.capitalize() or "_" + x.lower() for x in string.split("_")
        ).strip("_")

    @classmethod
    def snake_to_pascal(
        cls,
        string: str,
    ) -> str:
        """
        Converts a snake_case string to PascalCase.

        Args:
            string (str): The snake_case string to be converted.

        Returns:
            str: The PascalCase version of the input string.
        """
        return "".join(x.capitalize() for x in string.split("_"))

    @classmethod
    def string_to_datetime(
        cls,
        date_string: str,
        format: str = "%Y-%m-%d %H:%M:%S",
    ) -> Optional[datetime]:
        """
        Converts a string representation of a date and time to a datetime object.

        Args:
            date_string (str): The date and time as a string.
            format (str): The format in which the date_string is provided. Defaults to "%Y-%m-%d %H:%M:%S".

        Returns:
            datetime: A datetime object representing the given date and time.
        """
        try:
            return datetime.strptime(
                date_string,
                format,
            )
        except ValueError:
            return None

    @classmethod
    def validate_date_format(
        cls,
        format_string: str,
    ) -> bool:
        """
        Validates whether the given format string is supported by datetime.strptime.

        Args:
            format_string (str): The date format string to test.

        Returns:
            bool: True if format is valid, False otherwise.
        """
        try:
            # Try parsing a dummy date using the format
            datetime.datetime.strptime(
                cls.datetime_to_string(datetime=cls.get_current_datetime()),
                format_string,
            )

            # Return True
            return True
        except (ValueError, TypeError):
            # Return False, if an exception occures
            return False
