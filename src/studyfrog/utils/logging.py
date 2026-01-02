"""
Author: Louis Goodnews
Date: 2025-12-08
Description: This module holds the logg functions for the application.
"""

import sys

from typing import Any, Final, Literal, Optional, TypeAlias

from constants.common import APP_NAME
from constants.logging import (
    CRITICAL_FG,
    DEBUG_FG,
    ERROR_FG,
    INFO_FG,
    RESET,
    SUCCESS_FG,
    TRACE_FG,
    WARNING_FG,
)
from utils.common import get_now_str


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "log",
    "log_critical",
    "log_debug",
    "log_error",
    "log_info",
    "log_success",
    "log_trace",
    "log_warning",
]


# ---------- Types ---------- #

LogLevel: TypeAlias = Literal[
    "CRITICAL",
    "DEBUG",
    "ERROR",
    "INFO",
    "SUCCESS",
    "TRACE",
    "WARNING",
]

# ---------- Functions ---------- #


def log(
    message: Any,
    level: LogLevel = "TRACE",
    name: Optional[str] = None,
) -> None:
    """
    Prints a log message to the console.

    Args:
        level (LogLevel, optional): The level of the log. Defaults to "TRACE".
        message (Any): The message to log.
        name (str, optional): The name of the log. Defaults to the application name.

    Returns:
        None
    """

    if not level.isupper():
        level = level.upper()

    level_to_color: dict[LogLevel, str] = {
        "CRITICAL": CRITICAL_FG,
        "DEBUG": DEBUG_FG,
        "ERROR": ERROR_FG,
        "INFO": INFO_FG,
        "SUCCESS": SUCCESS_FG,
        "TRACE": TRACE_FG,
        "WARNING": WARNING_FG,
    }

    log_string: str = (
        f"{level_to_color.get(level, RESET)}{get_now_str()} - [{level}]{f' - [{name.upper()}] ' if name else f' - [{APP_NAME}] '}- {str(message)};{RESET}\n"
    )

    if level not in [
        "CRITICAL",
        "ERROR",
        "WARNING",
    ]:
        sys.stdout.write(log_string)

        return

    sys.stderr.write(log_string)


def log_critical(
    message: Any,
    name: Optional[str] = None,
) -> None:
    """
    Prints a log message with CRITICAL level.

    Args:
        message (Any): The message to log.
        name (str, optional): The name of the log. Defaults to None.

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
    name: Optional[str] = None,
) -> None:
    """
    Prints a log message with DEBUG level.

    Args:
        message (Any): The message to log.
        name (str, optional): The name of the log. Defaults to None.

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
    name: Optional[str] = None,
) -> None:
    """
    Prints a log message with ERROR level.

    Args:
        message (Any): The message to log.
        name (str, optional): The name of the log. Defaults to None.

    Returns:
        None
    """

    log(
        level="ERROR",
        message=message,
        name=name,
    )


def log_info(
    message: Any,
    name: Optional[str] = None,
) -> None:
    """
    Prints a log message with INFO level.

    Args:
        message (Any): The message to log.
        name (str, optional): The name of the log. Defaults to None.

    Returns:
        None
    """

    log(
        level="INFO",
        message=message,
        name=name,
    )


def log_success(
    message: Any,
    name: Optional[str] = None,
) -> None:
    """
    Prints a log message with SUCCESS level.

    Args:
        message (Any): The message to log.
        name (str, optional): The name of the log. Defaults to None.

    Returns:
        None
    """

    log(
        level="SUCCESS",
        message=message,
        name=name,
    )


def log_trace(
    message: Any,
    name: Optional[str] = None,
) -> None:
    """
    Prints a log message with TRACE level.

    Args:
        message (Any): The message to log.
        name (str, optional): The name of the log. Defaults to None.

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
    name: Optional[str] = None,
) -> None:
    """
    Prints a log message with WARNING level.

    Args:
        message (Any): The message to log.
        name (str, optional): The name of the log. Defaults to None.

    Returns:
        None
    """

    log(
        level="WARNING",
        message=message,
        name=name,
    )
