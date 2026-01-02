"""
Author: Louis Goodnews
Date: 2025-12-10
Description: This module defines constants for the logging module.
"""

from typing import Final, Literal

from utils.common import create_rgb_fg_color

# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "CRITICAL_FG",
    "DEBUG_FG",
    "ERROR_FG",
    "INFO_FG",
    "RESET",
    "SUCCESS_FG",
    "TRACE_FG",
    "WARNING_FG",
]


# ---------- Constants ---------- #

RESET: Final[Literal["\033[0m"]] = "\033[0m"

CRITICAL_FG: Final[str] = create_rgb_fg_color(r=255, g=50, b=50)

DEBUG_FG: Final[str] = create_rgb_fg_color(r=150, g=150, b=150)

ERROR_FG: Final[str] = create_rgb_fg_color(r=200, g=50, b=50)

INFO_FG: Final[str] = create_rgb_fg_color(r=50, g=200, b=50)

SUCCESS_FG: Final[str] = create_rgb_fg_color(r=100, g=255, b=100)

TRACE_FG: Final[str] = create_rgb_fg_color(r=150, g=150, b=150)

WARNING_FG: Final[str] = create_rgb_fg_color(r=255, g=175, b=0)
