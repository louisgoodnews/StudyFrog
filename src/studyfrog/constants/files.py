"""
Author: Louis Goodnews
Date: 2025-12-10
"""

from pathlib import Path
from typing import Final

from constants.directories import CONFIG_DIR, DATA_DIR


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "ANSWERS_DB_JSON",
    "ASSOCIATIONS_DB_JSON",
    "CONFIG_DB_JSON",
    "CUSTOMFIELDS_DB_JSON",
    "DIFFICULTIES_DB_JSON",
    "FLASHCARDS_DB_JSON",
    "IMAGES_DB_JSON",
    "NOTES_DB_JSON",
    "OPTIONS_DB_JSON",
    "PRIORITIES_DB_JSON",
    "QUESTIONS_DB_JSON",
    "REHEARSAL_RUN_DB_JSON",
    "REHEARSAL_RUN_ITEM_DB_JSON",
    "STACKS_DB_JSON",
    "SUBJECTS_DB_JSON",
    "TAGS_DB_JSON",
    "TEACHERS_DB_JSON",
    "USERS_DB_JSON",
]


# ---------- Constants ---------- #

ANSWERS_DB_JSON: Final[Path] = DATA_DIR / "answers"

ASSOCIATIONS_DB_JSON: Final[Path] = DATA_DIR / "associations"

CONFIG_DB_JSON: Final[Path] = CONFIG_DIR / "config"

CUSTOMFIELDS_DB_JSON: Final[Path] = DATA_DIR / "customfields"

DIFFICULTIES_DB_JSON: Final[Path] = DATA_DIR / "difficulties"

FLASHCARDS_DB_JSON: Final[Path] = DATA_DIR / "flashcards"

IMAGES_DB_JSON: Final[Path] = DATA_DIR / "images"

NOTES_DB_JSON: Final[Path] = DATA_DIR / "notes"

OPTIONS_DB_JSON: Final[Path] = DATA_DIR / "options"

PRIORITIES_DB_JSON: Final[Path] = DATA_DIR / "priorities"

QUESTIONS_DB_JSON: Final[Path] = DATA_DIR / "questions"

REHEARSAL_RUN_DB_JSON: Final[Path] = DATA_DIR / "rehearsal_runs"

REHEARSAL_RUN_ITEM_DB_JSON: Final[Path] = DATA_DIR / "rehearsal_run_item"

STACKS_DB_JSON: Final[Path] = DATA_DIR / "stacks"

SUBJECTS_DB_JSON: Final[Path] = DATA_DIR / "subjects"

TAGS_DB_JSON: Final[Path] = DATA_DIR / "tags"

TEACHERS_DB_JSON: Final[Path] = DATA_DIR / "teachers"

USERS_DB_JSON: Final[Path] = DATA_DIR / "users"
