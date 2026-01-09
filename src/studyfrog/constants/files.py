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

ANSWERS_DB_JSON: Final[Path] = DATA_DIR / "answers.json"

ASSOCIATIONS_DB_JSON: Final[Path] = DATA_DIR / "associations.json"

CONFIG_DB_JSON: Final[Path] = CONFIG_DIR / "config.json"

CUSTOMFIELDS_DB_JSON: Final[Path] = DATA_DIR / "customfields.json"

DIFFICULTIES_DB_JSON: Final[Path] = DATA_DIR / "difficulties.json"

FLASHCARDS_DB_JSON: Final[Path] = DATA_DIR / "flashcards.json"

IMAGES_DB_JSON: Final[Path] = DATA_DIR / "images.json"

NOTES_DB_JSON: Final[Path] = DATA_DIR / "notes.json"

OPTIONS_DB_JSON: Final[Path] = DATA_DIR / "options.json"

PRIORITIES_DB_JSON: Final[Path] = DATA_DIR / "priorities.json"

QUESTIONS_DB_JSON: Final[Path] = DATA_DIR / "questions.json"

REHEARSAL_RUN_DB_JSON: Final[Path] = DATA_DIR / "rehearsal_runs.json"

REHEARSAL_RUN_ITEM_DB_JSON: Final[Path] = DATA_DIR / "rehearsal_run_items.json"

STACKS_DB_JSON: Final[Path] = DATA_DIR / "stacks.json"

SUBJECTS_DB_JSON: Final[Path] = DATA_DIR / "subjects.json"

TAGS_DB_JSON: Final[Path] = DATA_DIR / "tags.json"

TEACHERS_DB_JSON: Final[Path] = DATA_DIR / "teachers.json"

USERS_DB_JSON: Final[Path] = DATA_DIR / "users.json"
