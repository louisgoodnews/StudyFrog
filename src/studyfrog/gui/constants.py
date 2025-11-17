"""
Author: Louis Goodnews
Date: 2025-11-16
"""

from typing import Final, Literal

from common.constants import PROJECT_NAME, PROJECT_VERSION


# ---------- Constants ---------- #

BLACK: Final[Literal["#FFFFFF"]] = "#FFFFFF"

DARK_ACCENT: Final[Literal["#03A9F4"]] = "#03A9F4"

DARK_DIVIDER: Final[Literal["#BDBDBD"]] = "#BDBDBD"

DARK_LIGHT_PRIMARY: Final[Literal["#D1C4E9"]] = "#D1C4E9"

DARK_PRIMARY: Final[Literal["#512DA8"]] = "#512DA8"

DARK_PRIMARY_TEXT: Final[Literal["#212121"]] = "#212121"

DARK_SECONDARY: Final[Literal["#673AB7"]] = "#673AB7"

DARK_SECONDARY_TEXT: Final[Literal["#757575"]] = "#757575"

DEFAULT_FONT_FAMILY: Final[Literal["Helvetica"]] = "Helvetica"

DEFAULT_FONT_SIZE: Final[int] = 12

DEFAULT_FONT_WEIGHT: Final[Literal["normal", "bold"]] = "normal"

DEFAULT_FONT: Final[tuple[str, int, Literal["normal", "bold"]]] = (
    DEFAULT_FONT_FAMILY,
    DEFAULT_FONT_SIZE,
    DEFAULT_FONT_WEIGHT,
)

WHITE: Final[Literal["#FFFFFF"]] = "#FFFFFF"

COLOR_CONFIG: dict[str, dict[str, dict[str, str]]] = {
    "button": {
        "dark": {
            "activebackground": DARK_ACCENT,
            "activeforeground": WHITE,
            "background": DARK_PRIMARY,
            "bg": DARK_PRIMARY,
            "foreground": WHITE,
            "fg": WHITE,
        },
        "light": {
            "background": WHITE,
            "bg": WHITE,
        },
    },
    "frame": {
        "dark": {
            "background": DARK_SECONDARY,
            "bg": DARK_SECONDARY,
        },
        "light": {
            "background": WHITE,
            "bg": WHITE,
        },
    },
    "menu": {
        "dark": {
            "activebackground": DARK_ACCENT,
            "activeforeground": WHITE,
            "background": DARK_SECONDARY,
            "bg": DARK_SECONDARY,
            "foreground": WHITE,
            "fg": WHITE,
        },
        "light": {
            "background": WHITE,
            "bg": WHITE,
            "foreground": BLACK,
            "fg": BLACK,
        },
    },
    "window": {
        "dark": {
            "background": DARK_SECONDARY,
            "bg": DARK_SECONDARY,
        },
        "light": {
            "background": WHITE,
            "bg": WHITE,
        },
    },
}

WINDOW_GEOMETRY: Final[Literal["1920x1080+0+0"]] = "1920x1080+0+0"

WINDOW_TITLE: Final[Literal[f"{PROJECT_NAME} ({PROJECT_VERSION})"]] = (
    f"{PROJECT_NAME} ({PROJECT_VERSION})"
)


# ---------- Auto-Export ---------- #

# Auto-export all non-private symbols
__all__: Final[list[str]] = [
    name for name in globals() if not name.startswith("_") and name.isidentifier()
]
