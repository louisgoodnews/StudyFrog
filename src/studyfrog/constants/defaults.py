"""
Author: Louis Goodnews
Date: 2025-12-12
"""

from typing import Any, Final

from constants.common import APP_NAME
from models.factories import get_difficulty_model_dict, get_priority_model_dict, get_user_model_dict


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

DEFAULT_EASY_DIFFICULTY: Final[dict[str, Any]] = get_difficulty_model_dict(
    display_name="Easy",
    name="easy",
    value=0.25,
)

DEFAULT_HARD_DIFFICULTY: Final[dict[str, Any]] = get_difficulty_model_dict(
    display_name="Hard",
    name="hard",
    value=0.75,
)

DEFAULT_MEDIUM_DIFFICULTY: Final[dict[str, Any]] = get_difficulty_model_dict(
    display_name="Medium",
    name="medium",
    value=0.5,
)

DEFAULT_HIGH_PRIORITY: Final[dict[str, Any]] = get_priority_model_dict(
    display_name="High",
    name="high",
    value=0.75,
)

DEFAULT_HIGHEST_PRIORITY: Final[dict[str, Any]] = get_priority_model_dict(
    display_name="Highest",
    name="highest",
    value=1.0,
)

DEFAULT_LOW_PRIORITY: Final[dict[str, Any]] = get_priority_model_dict(
    display_name="Low",
    name="low",
    value=0.25,
)

DEFAULT_LOWEST_PRIORITY: Final[dict[str, Any]] = get_priority_model_dict(
    display_name="Lowest",
    name="lowest",
    value=0.0,
)

DEFAULT_MEDIUM_PRIORITY: Final[dict[str, Any]] = get_priority_model_dict(
    display_name="Medium",
    name="medium",
    value=0.5,
)

DEFAULT_USER: Final[dict[str, Any]] = get_user_model_dict(name=APP_NAME)
