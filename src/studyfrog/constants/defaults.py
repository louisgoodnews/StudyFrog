"""
Author: Louis Goodnews
Date: 2025-12-12
Description: This module holds default values for the application.
"""

from __future__ import annotations

from typing import Final

from studyfrog.constants.common import APP_NAME
from studyfrog.models.factory import Model, get_difficulty_model, get_priority_model, get_user_model


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "DEFAULT_EASY_DIFFICULTY",
    "DEFAULT_HARD_DIFFICULTY",
    "DEFAULT_MEDIUM_DIFFICULTY",
    "DEFAULT_HIGH_PRIORITY",
    "DEFAULT_HIGHEST_PRIORITY",
    "DEFAULT_LOW_PRIORITY",
    "DEFAULT_LOWEST_PRIORITY",
    "DEFAULT_MEDIUM_PRIORITY",
    "DEFAULT_USER",
]


# ---------- Constants ---------- #

DEFAULT_EASY_DIFFICULTY: Final[Model] = get_difficulty_model(
    display_name="Easy",
    name="easy",
    value=0.25,
)

DEFAULT_HARD_DIFFICULTY: Final[Model] = get_difficulty_model(
    display_name="Hard",
    name="hard",
    value=0.75,
)

DEFAULT_MEDIUM_DIFFICULTY: Final[Model] = get_difficulty_model(
    display_name="Medium",
    name="medium",
    value=0.5,
)

DEFAULT_HIGH_PRIORITY: Final[Model] = get_priority_model(
    display_name="High",
    name="high",
    value=0.75,
)

DEFAULT_HIGHEST_PRIORITY: Final[Model] = get_priority_model(
    display_name="Highest",
    name="highest",
    value=1.0,
)

DEFAULT_LOW_PRIORITY: Final[Model] = get_priority_model(
    display_name="Low",
    name="low",
    value=0.25,
)

DEFAULT_LOWEST_PRIORITY: Final[Model] = get_priority_model(
    display_name="Lowest",
    name="lowest",
    value=0.0,
)

DEFAULT_MEDIUM_PRIORITY: Final[Model] = get_priority_model(
    display_name="Medium",
    name="medium",
    value=0.5,
)

DEFAULT_USER: Final[Model] = get_user_model(name=APP_NAME)
