"""
Author: Louis Goodnews
Date: 2025-12-10
"""

from typing import Final, Literal

from constants.common import APP_NAME, APP_VERSION


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "READONLY",
    "TOPLEVEL_GEOMETRY",
    "WINDOW_GEOMETRY",
    "WINDOW_TITLE",
]


# ---------- Constants ---------- #

READONLY: Final[Literal["readonly"]] = "readonly"

TOAST_GEOMETRY: Final[Literal["400x100"]] = "400x100"

TOPLEVEL_GEOMETRY: Final[Literal["960x540+0+0"]] = "960x540+0+0"

WINDOW_GEOMETRY: Final[Literal["1920x1080+0+0"]] = "1920x1080+0+0"

WINDOW_TITLE: Final[Literal[f"{APP_NAME} ({APP_VERSION})"]] = f"{APP_NAME} ({APP_VERSION})"
