"""
Author: lodego
Date: 2025-02-06
"""

from typing import *

from datetime import datetime

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
    def get_current_datetime(cls) -> datetime:
        """
        Returns the current datetime.

        Returns:
            datetime: The current datetime.
        """
        return datetime.now()

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
            date_string=date_string,
            format=format,
        )
