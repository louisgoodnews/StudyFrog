"""
Author: Louis Goodnews
Date: 2025-11-16
"""

from typing import Any, Final

from core.models import get_difficulty, get_priority, get_user


# ---------- Constants ---------- #

EASY_DIFFICULTY: Final[dict[str, Any]] = get_difficulty(
    name="easy",
    value=1,
)

MEDIUM_DIFFICULTY: Final[dict[str, Any]] = get_difficulty(
    name="medium",
    value=2,
)

HARD_DIFFICULTY: Final[dict[str, Any]] = get_difficulty(
    name="hard",
    value=3,
)

LOWEST_PRIORITY: Final[dict[str, Any]] = get_priority(
    name="lowest",
    value=1,
)

LOW_PRIORITY: Final[dict[str, Any]] = get_priority(
    name="low",
    value=2,
)

MEDIUM_PRIORITY: Final[dict[str, Any]] = get_priority(
    name="medium",
    value=3,
)

HIGH_PRIORITY: Final[dict[str, Any]] = get_priority(
    name="high",
    value=4,
)

HIGHEST_PRIORITY: Final[dict[str, Any]] = get_priority(
    name="highest",
    value=5,
)

STUDY_FROG_USER: Final[dict[str, Any]] = get_user(
    name="StudyFrog",
)


# ---------- Auto-Export ---------- #

# Auto-export all non-private symbols
__all__: Final[list[str]] = [
    name for name in globals() if not name.startswith("_") and name.isidentifier()
]
