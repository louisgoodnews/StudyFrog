"""
Author: Louis Goodnews
Date: 2025-11-16
"""

from pathlib import Path
from typing import Final, Literal


# ---------- Constants ---------- #

PROJECT_NAME: Final[Literal["StudyFrog"]] = "StudyFrog"

PROJECT_VERSION: Final[Literal["0.1.0"]] = "0.1.0"


# ---------- Path-Constants ---------- #

CWD: Final[Path] = Path.cwd()

LOCAL_DIR: Final[Path] = CWD / ".local"

ASSETS_DIR: Final[Path] = LOCAL_DIR / "assets"

BACKUP_DIR: Final[Path] = LOCAL_DIR / "backup"

CACHE_DIR: Final[Path] = LOCAL_DIR / "cache"

CONFIG_DIR: Final[Path] = LOCAL_DIR / "config"

DATA_DIR: Final[Path] = LOCAL_DIR / "data"

EXPORTS_DIR: Final[Path] = LOCAL_DIR / "exports"

IMPORTS_DIR: Final[Path] = LOCAL_DIR / "imports"

LOG_DIR: Final[Path] = LOCAL_DIR / "log"

RESOURCES_DIR: Final[Path] = LOCAL_DIR / "resources"

TEMP_DIR: Final[Path] = LOCAL_DIR / "temp"

ANSWERS_TABLE_FILE: Final[Path] = DATA_DIR / "answers.json"

CONFIG_FILE: Final[Path] = CONFIG_DIR / "config.json"

DIFFICULTIES_TABLE_FILE: Final[Path] = DATA_DIR / "difficulties.json"

FLASHCARDS_TABLE_FILE: Final[Path] = DATA_DIR / "flashcards.json"

IMAGES_TABLE_FILE: Final[Path] = DATA_DIR / "images.json"

NOTES_TABLE_FILE: Final[Path] = DATA_DIR / "notes.json"

PRIORITIES_TABLE_FILE: Final[Path] = DATA_DIR / "priorities.json"

QUESTIONS_TABLE_FILE: Final[Path] = DATA_DIR / "questions.json"

REHEARSAL_RUNS_TABLE_FILE: Final[Path] = DATA_DIR / "rehearsal_runs.json"

REHEARSAL_RUN_ITEMS_TABLE_FILE: Final[Path] = DATA_DIR / "rehearsal_run_items.json"

STACKS_TABLE_FILE: Final[Path] = DATA_DIR / "stacks.json"

SUBJECTS_TABLE_FILE: Final[Path] = DATA_DIR / "subjects.json"

TEACHERS_TABLE_FILE: Final[Path] = DATA_DIR / "teachers.json"

USERS_TABLE_FILE: Final[Path] = DATA_DIR / "users.json"


# ---------- Auto-Export ---------- #

# Auto-export all non-private symbols
__all__: Final[list[str]] = [name for name in globals() if not name.startswith("_")]
