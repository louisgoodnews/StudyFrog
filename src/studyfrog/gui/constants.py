"""
Author: Louis Goodnews
Date: 2025-11-16
"""

from tkinter import ttk
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

SMALL_FONT_SIZE: Final[int] = 10

LARGE_FONT_SIZE: Final[int] = 16

BOLD_FONT_WEIGHT: Final[Literal["bold"]] = "bold"

DEFAULT_FONT_WEIGHT: Final[Literal["normal"]] = "normal"

DEFAULT_FONT: Final[tuple[str, int, Literal["normal"]]] = (
    DEFAULT_FONT_FAMILY,
    DEFAULT_FONT_SIZE,
    DEFAULT_FONT_WEIGHT,
)

SMALL_FONT: Final[tuple[str, int, Literal["normal"]]] = (
    DEFAULT_FONT_FAMILY,
    SMALL_FONT_SIZE,
    DEFAULT_FONT_WEIGHT,
)

LARGE_FONT: Final[tuple[str, int, Literal["normal"]]] = (
    DEFAULT_FONT_FAMILY,
    LARGE_FONT_SIZE,
    DEFAULT_FONT_WEIGHT,
)

LARGE_BOLD_FONT: Final[tuple[str, int, Literal["bold"]]] = (
    DEFAULT_FONT_FAMILY,
    LARGE_FONT_SIZE,
    BOLD_FONT_WEIGHT,
)

WHITE: Final[Literal["#FFFFFF"]] = "#FFFFFF"


COLOR_CONFIG: dict[str, dict[str, dict[str, str]]] = {
    "button": {
        "dark": {
            "activebackground": DARK_ACCENT,
            "activeforeground": WHITE,
            "background": DARK_PRIMARY,
            "bg": DARK_PRIMARY,
            "fg": WHITE,
            "font": DEFAULT_FONT,
            "foreground": WHITE,
        },
        "light": {
            "background": WHITE,
            "bg": WHITE,
            "fg": BLACK,
            "font": DEFAULT_FONT,
            "foreground": BLACK,
        },
    },
    "canvas": {
        "dark": {"background": DARK_SECONDARY},
        "light": {"background": WHITE},
    },
    "checkbutton": {
        "dark": {
            "background": DARK_PRIMARY,
            "bg": DARK_PRIMARY,
            "fg": WHITE,
            "font": DEFAULT_FONT,
            "foreground": WHITE,
        },
        "light": {
            "font": DEFAULT_FONT,
            "fg": BLACK,
        },
    },
    "combobox": {
        "dark": {"font": DEFAULT_FONT},
        "light": {"font": DEFAULT_FONT},
    },
    "entry": {
        "dark": {
            "background": DARK_SECONDARY,
            "bg": DARK_SECONDARY,
            "fg": WHITE,
            "font": DEFAULT_FONT,
            "foreground": WHITE,
        },
        "light": {
            "background": WHITE,
            "bg": WHITE,
            "fg": BLACK,
            "font": DEFAULT_FONT,
            "foreground": BLACK,
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
    "label": {
        "dark": {
            "background": DARK_SECONDARY,
            "bg": DARK_SECONDARY,
            "font": DEFAULT_FONT,
            "foreground": WHITE,
            "fg": WHITE,
        },
        "light": {
            "font": DEFAULT_FONT,
            "fg": BLACK,
        },
    },
    "menu": {
        "dark": {
            "activebackground": DARK_ACCENT,
            "activeforeground": WHITE,
            "background": DARK_SECONDARY,
            "bg": DARK_SECONDARY,
            "fg": WHITE,
            "font": DEFAULT_FONT,
            "foreground": WHITE,
        },
        "light": {
            "background": WHITE,
            "bg": WHITE,
            "foreground": BLACK,
            "fg": BLACK,
        },
    },
    "scrollbar": {
        "dark": {"background": DARK_SECONDARY},
        "light": {"background": WHITE},
    },
    "text": {
        "dark": {
            "background": DARK_SECONDARY,
            "bg": DARK_SECONDARY,
            "fg": WHITE,
            "font": DEFAULT_FONT,
            "foreground": WHITE,
        },
        "light": {
            "background": WHITE,
            "bg": WHITE,
            "fg": BLACK,
            "font": DEFAULT_FONT,
            "foreground": BLACK,
        },
    },
    "toplevel": {
        "dark": {
            "background": DARK_SECONDARY,
            "bg": DARK_SECONDARY,
        },
        "light": {
            "background": WHITE,
            "bg": WHITE,
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

READONLY: Final[Literal["readonly"]] = "readonly"

TOAST_GEOMETRY: Final[Literal["400x200+100+100"]] = "400x200+100+100"

TOPLEVEL_GEOMETRY: Final[Literal["960x540+0+0"]] = "960x540+0+0"

TOPLEVEL_LARGE_GEOMETRY: Final[Literal["1920x1080+0+0"]] = "1920x1080+0+0"

TOPLEVEL_SMALL_GEOMETRY: Final[Literal["480x270+0+0"]] = "480x270+0+0"

WINDOW_GEOMETRY: Final[Literal["1920x1080+0+0"]] = "1920x1080+0+0"

WINDOW_TITLE: Final[Literal[f"{PROJECT_NAME} ({PROJECT_VERSION})"]] = (
    f"{PROJECT_NAME} ({PROJECT_VERSION})"
)


# ---------- Auto-Export ---------- #

# Auto-export all non-private symbols
__all__: Final[list[str]] = [
    name for name in globals() if not name.startswith("_") and name.isidentifier()
]
