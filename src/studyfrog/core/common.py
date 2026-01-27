"""
Author: Louis Goodnews
Date: 2025-12-12
Description: This module holds common functions for the application.
"""

from typing import Final

from constants.defaults import (
    DEFAULT_EASY_DIFFICULTY,
    DEFAULT_HARD_DIFFICULTY,
    DEFAULT_MEDIUM_DIFFICULTY,
    DEFAULT_HIGH_PRIORITY,
    DEFAULT_HIGHEST_PRIORITY,
    DEFAULT_LOW_PRIORITY,
    DEFAULT_LOWEST_PRIORITY,
    DEFAULT_MEDIUM_PRIORITY,
    DEFAULT_USER,
)
from models.models import Model


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "get_default_difficulties",
    "get_default_priorities",
    "get_default_user",
]


# ---------- Public Functions ---------- #


def get_default_difficulties() -> list[Model]:
    """
    Returns the default difficulties for the application.

    Returns:
        list[Model]: The default difficulties for the application.
    """
    return [
        DEFAULT_EASY_DIFFICULTY,
        DEFAULT_MEDIUM_DIFFICULTY,
        DEFAULT_HARD_DIFFICULTY,
    ]


def get_default_priorities() -> list[Model]:
    """
    Returns the default priorities for the application.

    Returns:
        list[Model]: The default priorities for the application.
    """
    return [
        DEFAULT_LOWEST_PRIORITY,
        DEFAULT_LOW_PRIORITY,
        DEFAULT_MEDIUM_PRIORITY,
        DEFAULT_HIGH_PRIORITY,
        DEFAULT_HIGHEST_PRIORITY,
    ]


def get_default_user() -> Model:
    """
    Returns the default user for the application.

    Returns:
        Model: The default user for the application.
    """
    return DEFAULT_USER
