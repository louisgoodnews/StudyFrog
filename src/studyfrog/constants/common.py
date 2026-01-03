"""
Author: Louis Goodnews
Date: 2025-12-10
"""

import re
import sys

from typing import Final, Literal


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "APP_NAME",
    "APP_VERSION",
    "GLOBAL",
    "PATTERNS",
    "PLATFORM",
    "QUESTION_TYPES",
]


# ---------- Constants ---------- #

APP_NAME: Final[Literal["StudyFrog"]] = "StudyFrog"

APP_VERSION: Final[Literal["0.1.0"]] = "0.1.0"

GLOBAL: Final[Literal["GLOBAL"]] = "GLOBAL"

PATTERNS: Final[dict[str, re.Pattern[str]]] = {
    "MODEL_ID": re.compile(
        flags=re.IGNORECASE,
        pattern=r"[0-9]+$",
    ),
    "MODEL_KEY": re.compile(
        flags=re.IGNORECASE,
        pattern=r"^[A-Z_]+_[0-9]+$",
    ),
    "MODEL_TYPE": re.compile(
        flags=re.IGNORECASE,
        pattern=r"^[A-Z_]+$",
    ),
}

PLATFORM: Final[str] = sys.platform

QUESTION_TYPES: Final[list[str]] = [
    "Multiple or single choice answer",
    "Open answer",
    "True or false",
]
