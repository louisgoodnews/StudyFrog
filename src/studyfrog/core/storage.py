"""
Author: Louis Goodnews
Date: 2025-11-17
"""

from pathlib import Path
from typing import Any, Final, Literal

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
    ensure_json,
    get_file_content_json,
    write_file_json,
)


# ---------- Constants ---------- #

TABLES: dict[str, Path] = {
    "answers": ANSWERS_TABLE_FILE,
    "config": CONFIG_FILE,
    "flashcards": FLASHCARDS_TABLE_FILE,
    "notes": NOTES_TABLE_FILE,
    "questions": QUESTIONS_TABLE_FILE,
    "rehearsal_runs": REHEARSAL_RUNS_TABLE_FILE,
    "rehearsal_run_items": REHEARSAL_RUN_ITEMS_TABLE_FILE,
    "stacks": STACKS_TABLE_FILE,
    "subjects": SUBJECTS_TABLE_FILE,
    "teachers": TEACHERS_TABLE_FILE,
    "users": USERS_TABLE_FILE,
}


# ---------- Functions ---------- #


def get_table_entry(
    id: int,
    name: Literal[
        "answers",
        "config",
        "flashcards",
        "notes",
        "questions",
        "rehearsal_runs",
        "rehearsal_run_items",
        "stacks",
        "subjects",
        "teachers",
        "users",
    ],
) -> dict[str, Any]:
    """
    Gets an entry from the table.

    Args:
        id (int): The ID of the entry to retrieve.
        name (Literal[...]): The name of the table. Can be one of:
            - "answers"
            - "config"
            - "flashcards"
            - "notes"
            - "questions"
            - "rehearsal_runs"
            - "rehearsal_run_items"
            - "stacks"
            - "subjects"
            - "teachers"
            - "users"

    Returns:
        dict[str, Any]: The entry from the table.

    Raises:
        Exception: If there is an error retrieving the entry.
    """

    try:
        return (
            get_table_content(name=name)
            .get(
                "entries",
                {str(id): {}},
            )
            .get(
                str(id),
                {},
            )
        )
    except Exception as e:
        raise e


def get_table_entries(
    ids: list[int],
    name: Literal[
        "answers",
        "config",
        "flashcards",
        "notes",
        "questions",
        "rehearsal_runs",
        "rehearsal_run_items",
        "stacks",
        "subjects",
        "teachers",
        "users",
    ],
) -> list[dict[str, Any]]:
    """
    Gets multiple entries from the table.

    Args:
        ids (list[int]): The IDs of the entries to retrieve.
        name (Literal[...]): The name of the table. Can be one of:
            - "answers"
            - "config"
            - "flashcards"
            - "notes"
            - "questions"
            - "rehearsal_runs"
            - "rehearsal_run_items"
            - "stacks"
            - "subjects"
            - "teachers"
            - "users"

    Returns:
        list[dict[str, Any]]: The entries from the table.

    Raises:
        Exception: If there is an error retrieving the entries.
    """

    try:
        return [
            get_table_entry(
                id=id,
                name=name,
            )
            for id in ids
        ]
    except Exception as e:
        raise e


def get_table_content(
    name: Literal[
        "answers",
        "config",
        "flashcards",
        "notes",
        "questions",
        "rehearsal_runs",
        "rehearsal_run_items",
        "stacks",
        "subjects",
        "teachers",
        "users",
    ],
) -> dict[str, Any]:
    """
    Returns the content of the table.

    Args:
        name (Literal[...]): The name of the table. Can be one of:
            - "answers"
            - "config"
            - "flashcards"
            - "notes"
            - "questions"
            - "rehearsal_runs"
            - "rehearsal_run_items"
            - "stacks"
            - "subjects"
            - "teachers"
            - "users"

    Returns:
        dict[str, Any]: The content of the table.

    Raises:
        Exception: If there is an error retrieving the table content.
    """

    try:
        ensure_json(path=get_table_file_path(name=name))
        return get_file_content_json(path=get_table_file_path(name=name))
    except Exception as e:
        raise e


def get_table_file_path(
    name: Literal[
        "answers",
        "config",
        "flashcards",
        "notes",
        "questions",
        "rehearsal_runs",
        "rehearsal_run_items",
        "stacks",
        "subjects",
        "teachers",
        "users",
    ],
) -> Path:
    """
    Returns the path to the table file.

    Args:
        name (Literal[...]): The name of the table. Can be one of:
            - "answers"
            - "config"
            - "flashcards"
            - "notes"
            - "questions"
            - "rehearsal_runs"
            - "rehearsal_run_items"
            - "stacks"
            - "subjects"
            - "teachers"
            - "users"

    Returns:
        Path: The path to the table file.

    Raises:
        Exception: If there is an error retrieving the table file path.
    """

    global TABLES

    try:
        return TABLES[name]
    except KeyError as e:
        raise e
    except Exception as e:
        raise e


def write_table_content(
    name: Literal[
        "answers",
        "config",
        "flashcards",
        "notes",
        "questions",
        "rehearsal_runs",
        "rehearsal_run_items",
        "stacks",
        "subjects",
        "teachers",
        "users",
    ],
    table: dict[str, Any],
) -> bool:
    """
    Writes the content of the table to a file.

    Args:
        name (Literal[...]): The name of the table. Can be one of:
            - "answers"
            - "config"
            - "flashcards"
            - "notes"
            - "questions"
            - "rehearsal_runs"
            - "rehearsal_run_items"
            - "stacks"
            - "subjects"
            - "teachers"
            - "users"
        table (dict[str, Any]): The content of the table.

    Returns:
        bool: True if the file was written successfully, False otherwise.

    Raises:
        Exception: If there is an error writing the table content.
    """

    try:
        ensure_json(path=get_table_file_path(name=name))
        return write_file_json(
            data=table,
            path=get_table_file_path(name=name),
        )
    except Exception as e:
        raise e


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
