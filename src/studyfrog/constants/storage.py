"""
Author: Louis Goodnews
Date: 2026-01-01
"""

from typing import Final, Literal


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "ANSWERS",
    "ASSOCIATIONS",
    "CUSTOMFIELDS",
    "DIFFICULTIES",
    "FLASHCARDS",
    "IMAGES",
    "NOTES",
    "OPTIONS",
    "PRIORITIES",
    "QUESTIONS",
    "REHEARSAL_RUN_ITEMS",
    "REHEARSAL_RUNS",
    "STACKS",
    "SUBJECTS",
    "TAGS",
    "TEACHERS",
    "USERS",
]


# ---------- Constants ---------- #

ANSWERS: Final[Literal["answers"]] = "answers"

ASSOCIATIONS: Final[Literal["associations"]] = "associations"

CUSTOMFIELDS: Final[Literal["customfields"]] = "customfields"

DIFFICULTIES: Final[Literal["difficulties"]] = "difficulties"

FLASHCARDS: Final[Literal["flashcards"]] = "flashcards"

IMAGES: Final[Literal["images"]] = "images"

NOTES: Final[Literal["notes"]] = "notes"

OPTIONS: Final[Literal["options"]] = "options"

PRIORITIES: Final[Literal["priorities"]] = "priorities"

QUESTIONS: Final[Literal["questions"]] = "questions"

REHEARSAL_RUN_ITEMS: Final[Literal["rehearsal_run_items"]] = "rehearsal_run_items"

REHEARSAL_RUNS: Final[Literal["rehearsal_runs"]] = "rehearsal_runs"

STACKS: Final[Literal["stacks"]] = "stacks"

SUBJECTS: Final[Literal["subjects"]] = "subjects"

TAGS: Final[Literal["tags"]] = "tags"

TEACHERS: Final[Literal["teachers"]] = "teachers"

USERS: Final[Literal["users"]] = "users"
