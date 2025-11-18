"""
Author: Louis Goodnews
Date: 2025-11-16
"""

from typing import Final, Literal


# ---------- Constants ---------- #

NAME: Final[Literal["gui.views.flashcard_rehearsal_view"]] = "gui.views.flashcard_rehearsal_view"


# ---------- Functions ---------- #


# ---------- Auto-Export ---------- #

# Auto-export all non-private symbols
__all__: Final[list[str]] = [
    key
    for (
        key,
        value,
    ) in globals().items()
    if not key.startswith("_") and callable(value)
]
