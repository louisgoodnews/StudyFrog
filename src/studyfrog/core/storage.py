"""
Author: Louis Goodnews
Date: 2025-11-17
"""

import json

from pathlib import Path
from typing import Final

from common.constants import (
    ANSWERS_TABLE_FILE,
    CONFIG_FILE,
    FLASHCARDS_TABLE_FILE,
    NOTES_TABLE_FILE,
    QUESTIONS_TABLE_FILE,
    REHEARSAL_RUNS_TABLE_FILE,
    REHEARSAL_RUN_ITEMS_TABLE_FILE,
    STACKS_TABLE_FILE,
    SUBJECTS_TABLE_FILE,
    TEACHERS_TABLE_FILE,
    USERS_TABLE_FILE,
)
from utils.utils import (
    ensure_dir,
    ensure_json,
    get_dir,
    get_file,
    get_file_content_str,
    write_file_str,
)


# ---------- Constants ---------- #


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
