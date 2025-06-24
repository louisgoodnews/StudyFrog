"""
Author: lodego
Date: 2025-05-20
"""

import re
import traceback

from datetime import date, datetime, timedelta
from typing import *

from utils.logger import Logger


__all__: Final[List[str]] = ["DateUtil"]


class DateUtil:
    """
    A utility class for various datetime operations.

    Methods:
        calculate_duration_in_hours(end: datetime, start: datetime) -> Optional[float]: Calculates the duration between two datetime objects in hours.
        calculate_duration_in_minutes(end: datetime, start: datetime) -> Optional[float]: Calculates the duration between two datetime objects in minutes.
        calculate_duration_in_seconds(end: datetime, start: datetime) -> Optional[float]: Calculates the duration between two datetime objects in seconds.
        day_after_tomorrow(timezone: Optional[str] = None) -> date: Returns the date of the day after tomorrow.
        day_before_yesterday(timezone: Optional[str] = None) -> date: Returns the date of the day before yesterday.
        days_left_in_month(timezone: Optional[str] = None) -> int: Returns the number of days left in the month.
        days_left_in_week(timezone: Optional[str] = None) -> int: Returns the number of days left in the week.
        days_left_in_year(timezone: Optional[str] = None) -> int: Returns the number of days left in the year.
        decrement(
            amount: Union[int, float],
            date: Optional[datetime] = None,
            what: Literal[
                "seconds",
                "minutes",
                "hours",
                "days",
                "months",
                "years",
            ] = "days",
        ) -> datetime: Returns the datetime before the passed amount of time.
        end_of_day(day: Optional[date] = None) -> datetime: Returns the end of the day.
        end_of_month(day: Optional[date] = None) -> datetime: Returns the end of the month.
        end_of_week(day: Optional[date] = None) -> datetime: Returns the end of the week.
        end_of_year(day: Optional[date] = None) -> datetime: Returns the end of the year.
        increment(
            amount: Union[int, float],
            date: Optional[datetime] = None,
            what: Literal[
                "seconds",
                "minutes",
                "hours",
                "days",
                "months",
                "years",
            ] = "days",
        ) -> datetime: Returns the datetime after the passed amount of time.
        now(timezone: Optional[str] = None) -> datetime: Returns the current datetime.
        object_to_string(
            datetime_or_date: Union[datetime, date],
            format: Optional[str] = "%Y-%m-%d %H:%M:%S",
        ) -> str: Returns the string representation of the passed datetime or date.
        start_of_day(day: Optional[date] = None) -> datetime: Returns the start of the day.
        start_of_month(day: Optional[date] = None) -> datetime: Returns the start of the month.
        start_of_week(day: Optional[date] = None) -> datetime: Returns the start of the week.
        start_of_year(day: Optional[date] = None) -> datetime: Returns the start of the year.
        string_to_object(
            date_string: str,
            format: Optional[str] = "%Y-%m-%d %H:%M:%S",
            what: Literal["datetime", "date"] = "datetime",
        ) -> Union[datetime, date]: Returns the datetime or date object from the passed string.
        today(timezone: Optional[str] = None) -> date: Returns the current date.
        tomorrow(timezone: Optional[str] = None) -> date: Returns the date of the next day.
        yesterday(timezone: Optional[str] = None) -> date: Returns the date of the previous day.

    Attributes:
        logger (Logger): The logger instance for this class.
    """

    # Initialize the logger instance
    logger: Final[Logger] = Logger.get_logger(name=__name__)

    @classmethod
    def calculate_duration(
        cls,
        start: datetime,
        end: Optional[datetime] = None,
        what: Literal["hours", "minutes", "seconds"] = "seconds",
    ) -> Optional[float]:
        """
        Calculates the duration between two datetime objects.

        Args:
            end (datetime, optional): The end datetime. Defaults to the current datetime.
            start (datetime): The start datetime.
            what (Literal["hours", "minutes", "seconds"]: The unit to return the duration in.

        Returns:
            Optional[float]: The duration between the two datetime objects in the specified unit.

        Raises:
            ValueError: If the end datetime is before the start datetime.
        """
        try:
            if what == "hours":
                return cls.calculate_duration_in_hours(
                    end=end,
                    start=start,
                )
            elif what == "minutes":
                return cls.calculate_duration_in_minutes(
                    end=end,
                    start=start,
                )
            elif what == "seconds":
                return cls.calculate_duration_in_seconds(
                    end=end,
                    start=start,
                )
            else:
                raise ValueError(f"Invalid unit: {what}")
        except Exception as e:
            # Log an error message to indicate that an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'calculate_duration' method from '{cls.__name__}' class: {e}"
            )

            # Log the traceback
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None
            return None

    @classmethod
    def calculate_duration_in_hours(
        cls,
        start: datetime,
        end: Optional[datetime] = None,
    ) -> Optional[float]:
        """
        Calculates the duration between two datetime objects in hours.

        Args:
            end (datetime, optional): The end datetime. Defaults to the current datetime.
            start (datetime): The start datetime.

        Returns:
            Optional[float]: The duration between the two datetime objects in hours.

        Raises:
            ValueError: If the end datetime is before the start datetime.
        """
        try:
            # Check, if the end datetime has been passed
            if not end:
                # Set the end datetime to the current datetime
                end = cls.now()

            # Calculate the duration in hours
            return (end - start).total_seconds() / 3600
        except Exception as e:
            # Log an error message to indicate that an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'calculate_duration_in_hours' method from '{cls.__name__}' class: {e}"
            )

            # Log the traceback
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None
            return None

    @classmethod
    def calculate_duration_in_minutes(
        cls,
        start: datetime,
        end: Optional[datetime] = None,
    ) -> Optional[float]:
        """
        Calculates the duration between two datetime objects in minutes.

        Args:
            end (datetime): The end datetime. Defaults to the current datetime.
            start (datetime): The start datetime.

        Returns:
            Optional[float]: The duration between the two datetime objects in minutes.

        Raises:
            ValueError: If the end datetime is before the start datetime.
        """
        try:
            # Check, if the end datetime has been passed
            if not end:
                # Set the end datetime to the current datetime
                end = cls.now()

            # Calculate the duration in minutes
            return (end - start).total_seconds() / 60
        except Exception as e:
            # Log an error message to indicate that an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'calculate_duration_in_minutes' method from '{cls.__name__}' class: {e}"
            )

            # Log the traceback
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None
            return None

    @classmethod
    def calculate_duration_in_seconds(
        cls,
        start: datetime,
        end: Optional[datetime] = None,
    ) -> Optional[float]:
        """
        Calculates the duration between two datetime objects in seconds.

        Args:
            end (datetime): The end datetime. Defaults to the current datetime.
            start (datetime): The start datetime.

        Returns:
            Optional[float]: The duration between the two datetime objects in seconds.

        Raises:
            ValueError: If the end datetime is before the start datetime.
        """
        try:
            # Check, if the end datetime has been passed
            if not end:
                # Set the end datetime to the current datetime
                end = cls.now()

            # Calculate the duration in seconds
            return (end - start).total_seconds()
        except Exception as e:
            # Log an error message to indicate that an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'calculate_duration_in_seconds' method from '{cls.__name__}' class: {e}"
            )

            # Log the traceback
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None
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
                # Extract the token
                token: str = date_format[i : i + 2]

                # If it's a recognized token, add its regex form
                if token in token_map:
                    # Add the regex form to the pattern
                    regex_pattern += token_map[token]

                    # Increment the index by 2
                    i += 2

                    # Skip the next character
                    continue

            # If not a format token, escape and add the character literally
            regex_pattern += re.escape(date_format[i])

            # Increment the index
            i += 1

        # Return the assembled regex pattern
        return regex_pattern

    @classmethod
    def day_after_tomorrow(
        cls,
        timezone: Optional[str] = None,
        what: Literal["datetime", "date"] = "datetime",
    ) -> Union[datetime, date]:
        """
        Returns the date of the day after tomorrow.

        Args:
            timezone (Optional[str], optional): The timezone to use. Defaults to None.
            what (Literal["datetime", "date"], optional): The type of object to return. Defaults to "datetime".

        Returns:
            Union[datetime, date]: The date of the day after tomorrow.
        """

        # Return the date of the day after tomorrow
        return (
            cls.now(timezone=timezone) + timedelta(days=2)
            if what == "datetime"
            else cls.now(timezone=timezone) + timedelta(days=2)
        )

    @classmethod
    def day_before_yesterday(
        cls,
        timezone: Optional[str] = None,
        what: Literal["datetime", "date"] = "datetime",
    ) -> Union[datetime, date]:
        """
        Returns the date of the day before yesterday.

        Args:
            timezone (Optional[str], optional): The timezone to use. Defaults to None.
            what (Literal["datetime", "date"], optional): The type of object to return. Defaults to "datetime".

        Returns:
            Union[datetime, date]: The date of the day before yesterday.
        """

        # Return the date of the day before yesterday
        return (
            cls.now(timezone=timezone) - timedelta(days=2)
            if what == "datetime"
            else cls.now(timezone=timezone) - timedelta(days=2)
        )

    @classmethod
    def days_left_in_month(
        cls,
        timezone: Optional[str] = None,
    ) -> int:
        """
        Returns the number of days left in the month.

        Args:
            timezone (Optional[str], optional): The timezone to use. Defaults to None.

        Returns:
            int: The number of days left in the month.
        """

        # Return the number of days left in the month
        return (cls.end_of_month(timezone=timezone) - cls.now(timezone=timezone)).days

    @classmethod
    def days_left_in_week(
        cls,
        timezone: Optional[str] = None,
    ) -> int:
        """
        Returns the number of days left in the week.

        Args:
            timezone (Optional[str], optional): The timezone to use. Defaults to None.

        Returns:
            int: The number of days left in the week.
        """

        # Return the number of days left in the week
        return (cls.end_of_week(timezone=timezone) - cls.now(timezone=timezone)).days

    @classmethod
    def days_left_in_year(
        cls,
        timezone: Optional[str] = None,
    ) -> int:
        """
        Returns the number of days left in the year.

        Args:
            timezone (Optional[str], optional): The timezone to use. Defaults to None.

        Returns:
            int: The number of days left in the year.
        """

        # Return the number of days left in the year
        return (cls.end_of_year(timezone=timezone) - cls.now(timezone=timezone)).days

    @classmethod
    def decrement(
        cls,
        amount: Union[int, float],
        date: Optional[datetime] = None,
        what: Literal[
            "seconds",
            "minutes",
            "hours",
            "days",
            "months",
            "years",
        ] = "days",
    ) -> datetime:
        """
        Returns the datetime before the passed amount of time.

        Args:
            amount (Union[int, float]): The amount of time to decrement.
            date (Optional[datetime], optional): The datetime to decrement. Defaults to None.
            what (Literal["seconds", "minutes", "hours" ,"days", "months", "years"], optional): The amount of time to decrement. Defaults to "days".

        Returns:
            datetime: The datetime before the passed amount of time.
        """

        # Check, if a date has been passed
        if not date:
            # Set the date to the current datetime
            date = cls.now()

        # Return the datetime before the passed amount of time
        return date - timedelta(**{what: amount})

    @classmethod
    def end_of_day(
        cls,
        day: Optional[date] = None,
        timezone: Optional[str] = None,
    ) -> datetime:
        """
        Returns the end of the day.

        Args:
            day (Optional[date], optional): The day to get the end of. Defaults to None.
            timezone (Optional[str], optional): The timezone to use. Defaults to None.

        Returns:
            datetime: The end of the day.
        """

        # Check, if a day has been passed
        if not day:
            # Set the day to the current date
            day = cls.now(timezone=timezone)

        # Return the end of the day
        return datetime.combine(day, datetime.max.time())

    @classmethod
    def end_of_month(
        cls,
        day: Optional[date] = None,
        timezone: Optional[str] = None,
        what: Literal["datetime", "date"] = "datetime",
    ) -> Union[datetime, date]:
        """
        Returns the end of the month.

        Args:
            day (Optional[date], optional): The day to get the end of the month for. Defaults to None.
            timezone (Optional[str], optional): The timezone to use. Defaults to None.
            what (Literal["datetime", "date"], optional): The type of object to return. Defaults to "datetime".

        Returns:
            Union[datetime, date]: The end of the month.
        """

        # Check, if a day has been passed
        if not day:
            # Set the day to the current date
            day = cls.now(timezone=timezone)

        # Return the end of the month
        return (
            cls.end_of_day(day.replace(day=day.month))
            if what == "datetime"
            else day.replace(day=day.month)
        )

    @classmethod
    def end_of_week(
        cls,
        day: Optional[date] = None,
        timezone: Optional[str] = None,
        what: Literal["datetime", "date"] = "datetime",
    ) -> Union[datetime, date]:
        """
        Returns the end of the week.

        Args:
            day (Optional[date], optional): The day to get the end of the week for. Defaults to None.
            timezone (Optional[str], optional): The timezone to use. Defaults to None.
            what (Literal["datetime", "date"], optional): The type of object to return. Defaults to "datetime".

        Returns:
            Union[datetime, date]: The end of the week.
        """

        # Check, if a day has been passed
        if not day:
            # Set the day to the current date
            day = cls.now(timezone=timezone)

        # Return the end of the week
        return (
            cls.end_of_day(day + timedelta(days=6 - day.weekday()))
            if what == "datetime"
            else day + timedelta(days=6 - day.weekday())
        )

    @classmethod
    def end_of_year(
        cls,
        day: Optional[date] = None,
        timezone: Optional[str] = None,
        what: Literal["datetime", "date"] = "datetime",
    ) -> Union[datetime, date]:
        """
        Returns the end of the year.

        Args:
            day (Optional[date], optional): The day to get the end of the year for. Defaults to None.
            timezone (Optional[str], optional): The timezone to use. Defaults to None.
            what (Literal["datetime", "date"], optional): The type of object to return. Defaults to "datetime".

        Returns:
            Union[datetime, date]: The end of the year.
        """

        # Check, if a day has been passed
        if not day:
            # Set the day to the current date
            day = cls.now(timezone=timezone)

        # Return the end of the year
        return (
            cls.end_of_day(day.replace(month=12, day=31))
            if what == "datetime"
            else day.replace(month=12, day=31)
        )

    @classmethod
    def increment(
        cls,
        amount: Union[int, float],
        date: Optional[datetime] = None,
        what: Literal[
            "seconds",
            "minutes",
            "hours",
            "days",
            "months",
            "years",
        ] = "days",
    ) -> datetime:
        """
        Returns the datetime after the passed amount of time.

        Args:
            amount (Union[int, float]): The amount of time to increment.
            date (Optional[datetime], optional): The datetime to increment. Defaults to None.
            what (Literal["seconds", "minutes", "hours" ,"days", "months", "years"], optional): The amount of time to increment. Defaults to "days".

        Returns:
            datetime: The datetime after the passed amount of time.
        """

        # Check, if a date has been passed
        if not date:
            # Set the date to the current datetime
            date = cls.now()

        # Return the datetime after the passed amount of time
        return date + timedelta(**{what: amount})

    @classmethod
    def now(
        cls,
        timezone: Optional[str] = None,
    ) -> datetime:
        """
        Returns the current datetime.

        Args:
            timezone (Optional[str], optional): The timezone to use. Defaults to None.

        Returns:
            datetime: The current datetime in the passed timezone if a timezone has been passed. Otherwise, the current datetime.
        """

        # Check, if a timezone has been passed
        if timezone:
            # Return the current datetime in the passed timezone
            return datetime.now(tz=timezone)

        # Return the current datetime
        return datetime.now()

    @classmethod
    def object_to_string(
        cls,
        datetime_or_date: Union[datetime, date],
        format: Optional[str] = "%Y-%m-%d %H:%M:%S",
    ) -> str:
        """
        Returns the string representation of the passed datetime or date.

        Args:
            datetime_or_date (Union[datetime, date]): The datetime or date to convert to a string.
            format (Optional[str], optional): The format to use. Defaults to "%Y-%m-%d %H:%M:%S".

        Returns:
            str: The string representation of the passed datetime or date.
        """

        # Return the string representation of the passed datetime or date
        return datetime_or_date.strftime(format=format)

    @classmethod
    def start_of_day(
        cls,
        day: Optional[date] = None,
        timezone: Optional[str] = None,
    ) -> datetime:
        """
        Returns the start of the day.

        Args:
            day (Optional[date], optional): The day to get the start of. Defaults to None.
            timezone (Optional[str], optional): The timezone to use. Defaults to None.

        Returns:
            datetime: The start of the day.
        """

        # Check, if a day has been passed
        if not day:
            # Set the day to the current date
            day = cls.now(timezone=timezone)

        # Return the start of the day
        return datetime.combine(day, datetime.min.time())

    @classmethod
    def start_of_month(
        cls,
        day: Optional[date] = None,
        timezone: Optional[str] = None,
        what: Literal["datetime", "date"] = "datetime",
    ) -> Union[datetime, date]:
        """
        Returns the start of the month.

        Args:
            day (Optional[date], optional): The day to get the start of the month for. Defaults to None.
            timezone (Optional[str], optional): The timezone to use. Defaults to None.
            what (Literal["datetime", "date"], optional): The type of object to return. Defaults to "datetime".

        Returns:
            Union[datetime, date]: The start of the month.
        """

        # Check, if a day has been passed
        if not day:
            # Set the day to the current date
            day = cls.now(timezone=timezone)

        # Return the start of the month
        return (
            cls.start_of_day(day.replace(day=1))
            if what == "datetime"
            else day.replace(day=1)
        )

    @classmethod
    def start_of_week(
        cls,
        day: Optional[date] = None,
        timezone: Optional[str] = None,
        what: Literal["datetime", "date"] = "datetime",
    ) -> Union[datetime, date]:
        """
        Returns the start of the week.

        Args:
            day (Optional[date], optional): The day to get the start of the week for. Defaults to None.
            timezone (Optional[str], optional): The timezone to use. Defaults to None.
            what (Literal["datetime", "date"], optional): The type of object to return. Defaults to "datetime".

        Returns:
            Union[datetime, date]: The start of the week.
        """

        # Check, if a day has been passed
        if not day:
            # Set the day to the current date
            day = cls.now(timezone=timezone)

        # Return the start of the week
        return (
            cls.start_of_day(day - timedelta(days=day.weekday()))
            if what == "datetime"
            else day - timedelta(days=day.weekday())
        )

    @classmethod
    def start_of_year(
        cls,
        day: Optional[date] = None,
        timezone: Optional[str] = None,
        what: Literal["datetime", "date"] = "datetime",
    ) -> Union[datetime, date]:
        """
        Returns the start of the year.

        Args:
            day (Optional[date], optional): The day to get the start of the year for. Defaults to None.
            timezone (Optional[str], optional): The timezone to use. Defaults to None.
            what (Literal["datetime", "date"], optional): The type of object to return. Defaults to "datetime".

        Returns:
            Union[datetime, date]: The start of the year.
        """

        # Check, if a day has been passed
        if not day:
            # Set the day to the current date
            day = cls.now(timezone=timezone)

        # Return the start of the year
        return (
            cls.start_of_day(day.replace(month=1, day=1))
            if what == "datetime"
            else day.replace(month=1, day=1)
        )

    @classmethod
    def string_to_object(
        cls,
        date_string: str,
        format: Optional[str] = "%Y-%m-%d %H:%M:%S",
        what: Literal["datetime", "date"] = "datetime",
    ) -> Union[datetime, date]:
        """
        Returns the datetime or date object from the passed string.

        Args:
            date_string (str): The string to convert to a datetime or date object.
            format (Optional[str], optional): The format to use. Defaults to "%Y-%m-%d %H:%M:%S".
            what (Literal["datetime", "date"], optional): The type of object to return. Defaults to "datetime".

        Returns:
            Union[datetime, date]: The datetime or date object.
        """

        # Return the datetime or date object from the passed string
        return (
            datetime.strptime(
                date_string,
                format,
            )
            if what == "datetime"
            else date.fromisoformat(date_string)
        )

    @classmethod
    def today(
        cls,
        timezone: Optional[str] = None,
    ) -> date:
        """
        Returns the current date.

        Args:
            timezone (Optional[str], optional): The timezone to use. Defaults to None.

        Returns:
            date: The current date.
        """

        # Return the current date
        return cls.now(timezone=timezone).date()

    @classmethod
    def tomorrow(
        cls,
        timezone: Optional[str] = None,
        what: Literal["datetime", "date"] = "datetime",
    ) -> Union[datetime, date]:
        """
        Returns the date of the next day.

        Args:
            timezone (Optional[str], optional): The timezone to use. Defaults to None.
            what (Literal["datetime", "date"], optional): The type of object to return. Defaults to "datetime".

        Returns:
            Union[datetime, date]: The date of the next day.
        """

        # Return the date of the next day
        return (
            cls.now(timezone=timezone) + timedelta(days=1)
            if what == "datetime"
            else cls.now(timezone=timezone) + timedelta(days=1)
        )

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
                cls.object_to_string(datetime_or_date=cls.now()),
                format_string,
            )

            # Return True
            return True
        except (ValueError, TypeError):
            # Return False, if an exception occures
            return False

    @classmethod
    def yesterday(
        cls,
        timezone: Optional[str] = None,
        what: Literal["datetime", "date"] = "datetime",
    ) -> Union[datetime, date]:
        """
        Returns the date of the previous day.

        Args:
            timezone (Optional[str], optional): The timezone to use. Defaults to None.
            what (Literal["datetime", "date"], optional): The type of object to return. Defaults to "datetime".

        Returns:
            Union[datetime, date]: The date of the previous day.
        """

        # Return the date of the previous day
        return (
            cls.now(timezone=timezone) - timedelta(days=1)
            if what == "datetime"
            else cls.now(timezone=timezone) - timedelta(days=1)
        )
