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


__all__: List[str] = ["Miscellaneous"]


class Miscellaneous:
    """
    A class containing miscellaneous utility methods.

    This class provides a set of methods that can be used to perform various
    utility operations, such as converting between different string formats,
    formatting dates and times, and more.

    Attributes:
        logger (Logger): The logger instance associated with the Miscellaneous class.
    """

    logger: Logger = Logger.get_logger(name="Miscellaneous")

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
        return string.lower().replace(" ", "_")

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
                # Check if the value is a string (since DB stores JSON/datetime as strings)
                if isinstance(
                    value,
                    str,
                ):
                    # Try parsing as JSON
                    try:
                        parsed_value = json.loads(value)
                        if isinstance(
                            parsed_value,
                            (
                                dict,
                                list,
                            ),
                        ):  # Only accept valid JSON
                            result[key] = parsed_value
                            continue
                    except json.JSONDecodeError:
                        pass  # Not a valid JSON, continue

                    # Try parsing as datetime
                    try:
                        result[key] = cls.string_to_datetime(value)
                        continue
                    except ValueError:
                        pass  # Not a valid datetime, keep original value

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
        return re.match(
            pattern=pattern,
            string=string,
        ).group(group)

    @classmethod
    def get_current_datetime(cls) -> datetime:
        """
        Returns the current datetime.

        Returns:
            datetime: The current datetime.
        """
        return datetime.now()

    @classmethod
    def get_uuid(cls) -> str:
        """
        Returns a new UUID.

        Returns:
            str: A new UUID.
        """
        return str(uuid.uuid4())

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
    ) -> datetime:
        """
        Converts a string representation of a date and time to a datetime object.

        Args:
            date_string (str): The date and time as a string.
            format (str): The format in which the date_string is provided. Defaults to "%Y-%m-%d %H:%M:%S".

        Returns:
            datetime: A datetime object representing the given date and time.
        """
        return datetime.strptime(
            date_string,
            format,
        )
