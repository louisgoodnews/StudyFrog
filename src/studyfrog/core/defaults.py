"""
Author: Louis Goodnews
Date: 2025-11-16
"""

from typing import Any, Final

from core.models import get_difficulty_model, get_priority_model, get_user_model


# ---------- Constants ---------- #

EASY_DIFFICULTY: Final[dict[str, Any]] = get_difficulty_model(
    name="Easy",
    value=1,
)

MEDIUM_DIFFICULTY: Final[dict[str, Any]] = get_difficulty_model(
    name="Medium",
    value=2,
)

HARD_DIFFICULTY: Final[dict[str, Any]] = get_difficulty_model(
    name="Hard",
    value=3,
)

LOWEST_PRIORITY: Final[dict[str, Any]] = get_priority_model(
    name="Lowest",
    value=1,
)

LOW_PRIORITY: Final[dict[str, Any]] = get_priority_model(
    name="Low",
    value=2,
)

MEDIUM_PRIORITY: Final[dict[str, Any]] = get_priority_model(
    name="Medium",
    value=3,
)

HIGH_PRIORITY: Final[dict[str, Any]] = get_priority_model(
    name="High",
    value=4,
)

HIGHEST_PRIORITY: Final[dict[str, Any]] = get_priority_model(
    name="Highest",
    value=5,
)

STUDY_FROG_USER: Final[dict[str, Any]] = get_user_model(
    name="StudyFrog",
)


# ---------- Auto-Export ---------- #

# Auto-export all non-private symbols
__all__: Final[list[str]] = [
    "EASY_DIFFICULTY",
    "HARD_DIFFICULTY",
    "HIGH_PRIORITY",
    "HIGHEST_PRIORITY",
    "LOW_PRIORITY",
    "LOWEST_PRIORITY",
    "MEDIUM_DIFFICULTY",
    "MEDIUM_PRIORITY",
    "STUDY_FROG_USER",
]
