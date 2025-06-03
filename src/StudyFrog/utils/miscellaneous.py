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
    def calculate_continuous_grade(
        cls,
        score: float,
        max_score: float,
        mean_ratio: float = 0.6,
        stddev_ratio: float = 0.15,
        thresholds: List[Tuple[float, float]] = None,
    ) -> float:
        """
        Calculates a smooth, continuous grade via linear interpolation over z-score thresholds.

        Args:
            score (float): Achieved score.
            max_score (float): Maximum achievable score.
            mean_ratio (float): Mean as ratio of max_score (default 60%).
            stddev_ratio (float): Std dev as ratio of max_score (default 15%).
            thresholds (List[Tuple[z_score, grade]]): Sorted descending by z_score.

        Returns:
            float: A continuous grade (e.g. 2.64) interpolated between defined grade levels.
        """

        # Check, if the max_score is valid (i.e. > 0)
        if max_score <= 0:
            # Log an error message indicating an invalid max_score value
            cls.logger.error(
                message=f"Invalid max_score value: {max_score} (must be greater than 0)"
            )

            # Raise a ValueError with a descriptive error message
            raise ValueError("max_score must be greater than 0")

        # Calculate mean
        mu: float = mean_ratio * max_score

        # Calculate standard deviation
        sigma: float = stddev_ratio * max_score

        # Calculate z-score
        z: float = (score - mu) / sigma

        # Check, if thresholds are provided
        if thresholds is None:
            # Default thresholds
            thresholds = [
                (+2.0, 1.0),
                (+1.5, 1.3),
                (+1.0, 1.7),
                (+0.5, 2.0),
                (0.0, 2.3),
                (-0.5, 3.0),
                (-1.0, 3.7),
                (-1.5, 4.0),
                (-2.0, 5.0),
            ]

        # Sort the thresholds in descending order
        thresholds = sorted(thresholds, reverse=True)

        # If z is greater than the highest threshold → best grade
        if z >= thresholds[0][0]:
            # Return the best grade
            return thresholds[0][1]

        # If z is less than the lowest threshold → worst grade
        if z <= thresholds[-1][0]:
            # Return the worst grade
            return thresholds[-1][1]

        # Interpolate between two thresholds
        for i in range(1, len(thresholds)):
            # Get the current threshold and grade
            z1, grade1 = thresholds[i - 1]

            # Get the next threshold and grade
            z2, grade2 = thresholds[i]

            # Check, if z is between the current threshold and the next threshold
            if z1 >= z >= z2:
                # Linear interpolation
                ratio: float = (z - z2) / (z1 - z2)

                # Interpolate the grade
                interpolated: float = grade2 + ratio * (grade1 - grade2)

                # Return the interpolated grade
                return round(interpolated, 3)

        # Fallback (should never happen)
        return 5.0

    @classmethod
    def calculate_duration(
        cls,
        start: datetime,
        as_: Literal["seconds", "minutes", "hours"] = "seconds",
        end: Optional[datetime] = None,
    ) -> Optional[Union[float, int]]:
        """
        Calculates the duration between two datetime objects.

        Args:
            start (datetime): The start datetime.
            end (Optional[datetime]): The end datetime. If None, the current datetime is used.
            as_ (Literal["seconds", "minutes", "hours"]): The unit to return the duration in.

        Returns:
            Optional[Union[float, int]]: The duration between the two datetime objects in the specified unit.
        """

        # Check, if the start datetime is None
        if start is None:
            # Log an error message indicating an invalid start datetime
            cls.logger.error(
                message="Invalid start datetime: None (must be a datetime object)"
            )

            # Return None indicating an invalid start datetime
            return None

        # Check, if the end datetime is None
        if end is None:
            # Use the current datetime
            end = cls.get_current_datetime()

        # Calculate the duration in seconds
        duration: float = (end - start).total_seconds()

        # Return the duration in the specified unit
        if as_ == "seconds":
            return duration
        elif as_ == "minutes":
            return duration // 60
        elif as_ == "hours":
            return duration // 3600

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

        # Initialize an empty string to store the result
        result: str = ""

        # Iterate over each character in the string
        for char in string:
            # Check if the character is uppercase
            if char.isupper():
                # Append an underscore and the lowercase version of the character
                result += "_" + char.lower()
            else:
                # Append the character as is
                result += char

        # Return the result, stripped of leading/trailing underscores
        return result.strip("_")

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
                # Add the value to the result dictionary
                result[key] = value

                # Check, if the current value is not a string
                if not isinstance(
                    value,
                    str,
                ):
                    # Skip to the next iteration
                    continue

                # Check, if the current value is a JSON string
                if cls.is_json_string(string=value):
                    # Convert the JSON string into a JSON object
                    result[key] = json.loads(value)

                    # Skip to the next iteration
                    continue

                # Check, if the current value is a datetime string
                if cls.is_datetime_string(string=value):
                    # Convert the datetime string into a datetime object
                    result[key] = cls.string_to_datetime(date_string=value)

                    # Skip to the next iteration
                    continue

            # Return the converted dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'convert_from_db_format' method from '{cls.__name__}': {e}"
            )

            # Log the traceback
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

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

            # Log the traceback
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def date_format_to_regex_pattern(
        cls,
        date_format: str,
    ) -> Optional[str]:
        """
        Converts a datetime format string into a regex pattern.

        This method transforms a strftime-compatible format (e.g., "%Y-%m-%d")
        into a regex pattern that can be used to validate or match strings
        with the same structure.

        Example:
            "%d.%m.%Y" -> r"\d{1,2}\.\d{1,2}\.\d{4}"

        Args:
            date_format (str): The datetime format string to convert.

        Returns:
            Optional[str]: A regex pattern matching the given format, or None if the input is invalid.
        """

        # Check, if the format is empty or None
        if not date_format:
            # Return early
            return None

        # Mapping of strftime tokens to regex equivalents
        token_map: Dict[str, str] = {
            "%d": r"\d{1,2}",  # Day of the month (1–31)
            "%m": r"\d{1,2}",  # Month (1–12)
            "%y": r"\d{2}",  # Two-digit year
            "%Y": r"\d{4}",  # Four-digit year
            "%H": r"\d{1,2}",  # Hour (0–23)
            "%I": r"\d{1,2}",  # Hour (1–12)
            "%M": r"\d{1,2}",  # Minute (0–59)
            "%S": r"\d{1,2}",  # Second (0–59)
            "%f": r"\d{1,6}",  # Microsecond
            "%p": r"(AM|PM|am|pm)",  # AM/PM in various cases
            "%b": r"[A-Za-z]{3}",  # Abbreviated month name
            "%B": r"[A-Za-z]+",  # Full month name
            "%a": r"[A-Za-z]{3}",  # Abbreviated weekday name
            "%A": r"[A-Za-z]+",  # Full weekday name
            "%j": r"\d{1,3}",  # Day of the year (1–366)
            "%U": r"\d{1,2}",  # Week number (Sunday first)
            "%W": r"\d{1,2}",  # Week number (Monday first)
            "%w": r"\d",  # Weekday as a digit (0–6)
            "%z": r"[\+\-]\d{4}",  # UTC offset (e.g., +0200)
            "%Z": r"[A-Za-z]+",  # Time zone abbreviation
            "%c": r".+",  # Locale-specific datetime representation
            "%x": r".+",  # Locale-specific date
            "%X": r".+",  # Locale-specific time
            "%%": r"%",  # Literal '%'
        }

        # Prepare the final regex string
        regex_pattern: str = ""

        # Iterate through the format string by index
        i: int = 0

        while i < len(date_format):
            # If a token begins with '%', try to match a known format token
            if date_format[i] == "%" and i + 1 < len(date_format):
                token: str = date_format[i : i + 2]

                # If it's a recognized token, add its regex form
                if token in token_map:
                    regex_pattern += token_map[token]
                    i += 2
                    continue

            # If not a format token, escape and add the character literally
            regex_pattern += re.escape(date_format[i])
            i += 1

        # Return the assembled regex pattern
        return regex_pattern

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

        # Log the traceback
        cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

        # Return None
        return None

    @classmethod
    def estimate_reading_time(
        cls,
        content: Union[
            float,
            int,
            str,
        ],
        as_: Literal["minutes", "seconds"] = "minutes",
    ) -> float:
        """
        Estimates the reading time for a given content.

        Args:
            as_ (Literal["minutes", "seconds"]): The unit to return the reading time in. Defaults to "minutes".
            content (Union[float, int, str]): The content to estimate the reading time for.

        Returns:
            float: The estimated reading time in minutes or seconds.
        """

        # Check, if the content is empty
        if content is None or (isinstance(content, str) and not content.strip()):
            # Return early
            return 0.0

        # Check, if the unit is supported
        if as_ not in {
            "minutes",
            "seconds",
        }:
            # Raise a ValueError
            raise ValueError(f"Unsupported unit: {as_}")

        # Initialize the result float to 0.0
        result: float = 0.0

        # Set the base rate of words per minute
        base_rate: int = 200

        # Calculate the word count
        word_count: float = len(content.strip().split()) if isinstance(content, str) else float(content)

        # Calculate the estimated reading time
        result = word_count / base_rate

        # Return the estimated reading time
        return result if as_ == "minutes" else result * 60

    @classmethod
    def find_match(
        cls,
        string: str,
        fullmatch: bool = False,
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

        if fullmatch:
            # Find a match for the string against the pattern
            match: Optional[re.Match] = re.fullmatch(
                pattern=pattern,
                string=string,
            )
        elif not fullmatch:
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
        days: Optional[Union[float, int]] = None,
        hours: Optional[Union[float, int]] = None,
        microseconds: Optional[Union[float, int]] = None,
        milliseconds: Optional[Union[float, int]] = None,
        minutes: Optional[Union[float, int]] = None,
        seconds: Optional[Union[float, int]] = None,
    ) -> datetime:
        """
        Returns the current datetime decremented by a given amount.

        Args:
            days (Optional[Union[float, int]]): The amount of days to decrement the datetime by.
            hours (Optional[Union[float, int]]): The amount of hours to decrement the datetime by.
            microseconds (Optional[Union[float, int]]): The amount of microseconds to decrement the datetime by.
            milliseconds (Optional[Union[float, int]]): The amount of milliseconds to decrement the datetime by.
            minutes (Optional[Union[float, int]]): The amount of minutes to decrement the datetime by.
            seconds (Optional[Union[float, int]]): The amount of seconds to decrement the datetime by.

        Returns:
            datetime: The decremented datetime.
        """
        return cls.get_current_datetime() - timedelta(
            days=days or 0,
            hours=hours or 0,
            microseconds=microseconds or 0,
            milliseconds=milliseconds or 0,
            minutes=minutes or 0,
            seconds=seconds or 0,
        )

    @classmethod
    def get_date_increment(
        cls,
        days: Optional[Union[float, int]] = None,
        hours: Optional[Union[float, int]] = None,
        microseconds: Optional[Union[float, int]] = None,
        milliseconds: Optional[Union[float, int]] = None,
        minutes: Optional[Union[float, int]] = None,
        seconds: Optional[Union[float, int]] = None,
    ) -> datetime:
        """
        Returns the current datetime incremented by a given amount.

        Args:
            days (Optional[Union[float, int]]): The amount of days to increment the datetime by.
            hours (Optional[Union[float, int]]): The amount of hours to increment the datetime by.
            microseconds (Optional[Union[float, int]]): The amount of microseconds to increment the datetime by.
            milliseconds (Optional[Union[float, int]]): The amount of milliseconds to increment the datetime by.
            minutes (Optional[Union[float, int]]): The amount of minutes to increment the datetime by.
            seconds (Optional[Union[float, int]]): The amount of seconds to increment the datetime by.

        Returns:
            datetime: The incremented datetime.
        """
        return datetime.now() + timedelta(
            days=days or 0,
            hours=hours or 0,
            microseconds=microseconds or 0,
            milliseconds=milliseconds or 0,
            minutes=minutes or 0,
            seconds=seconds or 0,
        )

    @classmethod
    def get_random_bool(cls) -> bool:
        """
        Returns a random boolean value.

        Returns:
            bool: A random boolean value.
        """
        return random.choice(seq=[True, False])

    @classmethod
    def get_random_float(cls) -> float:
        """
        Returns a random float value.

        Returns:
            float: A random float value.
        """
        return random.random()

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
    def get_range(cls, min: int, max: int, step: int = 1) -> Tuple[int, ...]:
        """
        Returns a range of integers between min and max (inclusive).

        Args:
            min (int): The minimum value of the range.
            max (int): The maximum value of the range.
            step (int): The step size of the range. Defaults to 1.

        Returns:
            range: A range of integers between min and max (inclusive).
        """
        return tuple(range(min, max + 1, step))

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
        if not isinstance(
            string,
            str,
        ):
            # Return False
            return False

        # Strip off any leading or trailing whitespaces
        stripped: str = string.strip()

        # A list of common date formats
        common_formats: List[str] = [
            "%Y-%m-%d %H:%M:%S",  # 2025-04-14 08:57:23
            "%Y-%m-%d",  # 2025-04-14
            "%d.%m.%Y",  # 14.04.2025
            "%d.%m.%y",  # 14.04.25
            "%m/%d/%Y",  # 04/14/2025
            "%Y/%m/%d",  # 2025/04/14
            "%d-%b-%Y",  # 14-Apr-2025
        ]

        # Iterate over the common date formats list
        for format in common_formats:
            try:
                # Attempt to create a datetime object from the string with the format
                datetime.strptime(
                    stripped,
                    format,
                )

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

        # Strip off any leading or trailing whitespaces
        stripped: str = string.strip()

        # Check if the string starts and ends with curly braces (indicating a JSON object)
        # or square brackets (indicating a JSON array)
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
    def pascal_to_snake(
        cls,
        string: str,
    ) -> str:
        """
        Converts a PascalCase string to snake_case.

        Args:
            string (str): The PascalCase string to be converted.

        Returns:
            str: The snake_case version of the input string.
        """

        # Initialize an empty string to store the result
        result: str = ""

        # Check, if the entire string is lowercase or uppercase
        if string.islower() or string.isupper():
            # Return the lowercase version of the string
            return string.lower() if string.isupper() else string

        # Iterate over each character in the string
        for (
            index,
            char,
        ) in enumerate(iterable=string):
            # Check if the character is uppercase and the first character
            if char.isupper() and index == 0:
                # Append the lowercase version of the character
                result += char.lower()
            # Check if the character is uppercase and not the first character
            elif char.isupper() and index > 0:
                # Append an underscore and the lowercase version of the character
                result += "_" + char.lower()
            else:
                # Append the character as is
                result += char

        # Return the result, stripped of leading/trailing underscores
        return result.strip("_")

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
    def run_async_in_thread(
        cls,
        func: Callable[..., Any],
        *args,
        **kwargs,
    ) -> Optional[Any]:
        """
        Runs a function asynchronously in a separate thread.

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

            def wrapper(
                func: Callable[..., Any],
                *args,
                **kwargs,
            ) -> Optional[Any]:
                """
                A wrapper function to run the given function asynchronously.

                Args:
                    func (Callable[..., Any]): The function to be run asynchronously.
                    *args: Additional positional arguments to be passed to the function.
                    **kwargs: Additional keyword arguments to be passed to the function.

                Returns:
                    Optional[Any]: The return value of the function or None if an exception occurs.
                """
                try:
                    # Run the function and return the result
                    return asyncio.run(
                        main=func(
                            *args,
                            **kwargs,
                        )
                    )
                except Exception as e:
                    # Log an error message indicating an exception has occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'wrapper' method from '{cls.__name__}': {e}"
                    )

                    # Log the traceback
                    cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

                    # Return None indicating an exception has occurred
                    return None

            # Create a thread to run the function asynchronously
            thread: threading.Thread = threading.Thread(
                target=wrapper,
                args=args,
                kwargs=kwargs,
            )

            # Start the thread
            thread.start()

            # Wait for the thread to finish
            thread.join()

            # Return the result of the function
            return thread.result()
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'run_async_in_thread' method from '{cls.__name__}': {e}"
            )

            # Log the traceback
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

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

            # Log the traceback
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

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

            # Log the traceback
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

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
    def shuffle(
        cls,
        iterable: Iterable[Any],
    ) -> None:
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
