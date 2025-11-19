"""
Author: Louis Goodnews
Date: 2025-11-17
"""

from pathlib import Path
from typing import Any, Final, Literal, Union

from common.constants import (
    ANSWERS_TABLE_FILE,
    CONFIG_FILE,
    CUSTOMFIELDS_TABLE_FILE,
    DIFFICULTIES_TABLE_FILE,
    FLASHCARDS_TABLE_FILE,
    IMAGES_TABLE_FILE,
    NOTES_TABLE_FILE,
    PRIORITIES_TABLE_FILE,
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
    get_now_str,
    get_today_str,
    get_uuid_str,
    is_dict_empty,
    is_key_in_dict,
    log_exception,
    write_file_json,
)


# ---------- Constants ---------- #

NAME: Final[Literal["core.storage"]] = "core.storage"

TABLES: dict[str, Path] = {
    "answers": ANSWERS_TABLE_FILE,
    "configs": CONFIG_FILE,
    "customfields": CUSTOMFIELDS_TABLE_FILE,
    "difficulties": DIFFICULTIES_TABLE_FILE,
    "flashcards": FLASHCARDS_TABLE_FILE,
    "images": IMAGES_TABLE_FILE,
    "notes": NOTES_TABLE_FILE,
    "priorities": PRIORITIES_TABLE_FILE,
    "questions": QUESTIONS_TABLE_FILE,
    "rehearsal_runs": REHEARSAL_RUNS_TABLE_FILE,
    "rehearsal_run_items": REHEARSAL_RUN_ITEMS_TABLE_FILE,
    "stacks": STACKS_TABLE_FILE,
    "subjects": SUBJECTS_TABLE_FILE,
    "teachers": TEACHERS_TABLE_FILE,
    "users": USERS_TABLE_FILE,
}


# ---------- Functions ---------- #


def add_table_entry(
    entry: dict[str, Any],
    table_name: Literal[
        "answers",
        "configs",
        "customfields",
        "difficulties",
        "flashcards",
        "images",
        "notes",
        "priorities",
        "questions",
        "rehearsal_runs",
        "rehearsal_run_items",
        "stacks",
        "subjects",
        "teachers",
        "users",
    ],
) -> int:
    """
    Adds an entry to the table.

    Args:
        entry (dict[str, Any]): The entry to add.
        table_name (Literal[...]): The name of the table. Can be one of:
            - "answers"
            - "configs"
            - "customfields"
            - "difficulties"
            - "flashcards"
            - "images"
            - "notes"
            - "priorities"
            - "questions"
            - "rehearsal_runs"
            - "rehearsal_run_items"
            - "stacks"
            - "subjects"
            - "teachers"
            - "users"

    Returns:
        int: The ID of the added entry.

    Raises:
        Exception: If there is an error adding the entry.
    """

    global NAME

    try:
        table: dict[str, Any] = get_table_content(table_name=table_name)

        new_id: int = int(
            table.get("entries", {}).get(
                "total",
                0,
            )
        )

        entry["created_at"] = get_now_str()
        entry["created_on"] = get_today_str()
        entry["id"] = new_id
        entry["key"] = f"{entry['type'].upper()}_{new_id}"
        entry["updated_at"] = get_now_str()
        entry["updated_on"] = get_today_str()

        table["entries"]["values"][str(new_id)] = entry

        table["schema"]["fields"]["values"] = sorted(
            list(set(table["schema"]["fields"]["values"] + list(entry.keys())))
        )

        table["schema"]["fields"]["total"] = len(table["schema"]["fields"]["values"])

        table["entries"]["total"] = new_id + 1

        write_table_content(
            table_name=table_name,
            table=table,
        )

        return new_id
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to add entry to table with name '{table_name}'.",
        )
        raise e


def add_table_entry_if_not_exists(
    entry: dict[str, Any],
    table_name: Literal[
        "answers",
        "configs",
        "customfields",
        "difficulties",
        "flashcards",
        "images",
        "notes",
        "priorities",
        "questions",
        "rehearsal_runs",
        "rehearsal_run_items",
        "stacks",
        "subjects",
        "teachers",
        "users",
    ],
) -> int:
    """
    Adds an entry to the table if it doesn't exist.

    Args:
        entry (dict[str, Any]): The entry to add.
        table_name (Literal[...]): The name of the table. Can be one of:
            - "answers"
            - "configs"
            - "customfields"
            - "difficulties"
            - "flashcards"
            - "images"
            - "notes"
            - "priorities"
            - "questions"
            - "rehearsal_runs"
            - "rehearsal_run_items"
            - "stacks"
            - "subjects"
            - "teachers"
            - "users"

    Returns:
        int: The ID of the added entry.

    Raises:
        Exception: If there is an error adding the entry.
    """

    global NAME

    try:
        filtered_entries: list[dict[str, Any]] = filter_table_entries(
            table_name=table_name,
            **{
                key: value
                for (
                    key,
                    value,
                ) in entry.items()
                if not key
                in {
                    "created_at",
                    "created_on",
                    "id",
                    "key",
                    "updated_at",
                    "updated_on",
                    "uuid",
                }
            },
        )

        if not filtered_entries:
            return add_table_entry(
                entry=entry,
                table_name=table_name,
            )

        return filtered_entries[0]["id"]
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to add entry to table with name '{table_name}'.",
        )
        raise e


def add_table_entries(
    entries: list[dict[str, Any]],
    table_name: Literal[
        "answers",
        "configs",
        "customfields",
        "difficulties",
        "flashcards",
        "images",
        "notes",
        "priorities",
        "questions",
        "rehearsal_runs",
        "rehearsal_run_items",
        "stacks",
        "subjects",
        "teachers",
        "users",
    ],
) -> list[int]:
    """
    Adds multiple entries to the table.

    Args:
        entries (list[dict[str, Any]]): The entries to add.
        table_name (Literal[...]): The name of the table. Can be one of:
            - "answers"
            - "configs"
            - "customfields"
            - "difficulties"
            - "flashcards"
            - "images"
            - "notes"
            - "priorities"
            - "questions"
            - "rehearsal_runs"
            - "rehearsal_run_items"
            - "stacks"
            - "subjects"
            - "teachers"
            - "users"

    Returns:
        list[int]: The IDs of the added entries.

    Raises:
        Exception: If there is an error adding the entries.
    """

    global NAME

    try:
        return [
            add_table_entry(
                entry=entry,
                table_name=table_name,
            )
            for entry in entries
        ]
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to add entries to table with name '{table_name}'.",
        )
        raise e


def count_entries_in_table(
    table_name: Literal[
        "answers",
        "configs",
        "customfields",
        "difficulties",
        "flashcards",
        "images",
        "notes",
        "priorities",
        "questions",
        "rehearsal_runs",
        "rehearsal_run_items",
        "stacks",
        "subjects",
        "teachers",
        "users",
    ],
) -> int:
    """
    Counts the number of entries in the table.

    Args:
        table_name (Literal[...]): The name of the table. Can be one of:
            - "answers"
            - "configs"
            - "customfields"
            - "difficulties"
            - "flashcards"
            - "images"
            - "notes"
            - "priorities"
            - "questions"
            - "rehearsal_runs"
            - "rehearsal_run_items"
            - "stacks"
            - "subjects"
            - "teachers"
            - "users"

    Returns:
        int: The number of entries in the table.

    Raises:
        Exception: If there is an error counting the entries.
    """

    global NAME

    try:
        return (
            get_table_content(table_name=table_name)
            .get(
                "entries",
                {},
            )
            .get(
                "total",
                0,
            )
        )
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to count entries in table with name '{table_name}'.",
        )
        return 0


def create_table_if_not_exists(
    table_name: Literal[
        "answers",
        "configs",
        "customfields",
        "difficulties",
        "flashcards",
        "images",
        "notes",
        "priorities",
        "questions",
        "rehearsal_runs",
        "rehearsal_run_items",
        "stacks",
        "subjects",
        "teachers",
        "users",
    ],
) -> bool:
    """
    Creates a table if it doesn't exist.

    Args:
        table_name (Literal[...]): The name of the table. Can be one of:
            - "answers"
            - "configs"
            - "customfields"
            - "difficulties"
            - "flashcards"
            - "images"
            - "notes"
            - "priorities"
            - "questions"
            - "rehearsal_runs"
            - "rehearsal_run_items"
            - "stacks"
            - "subjects"
            - "teachers"
            - "users"

    Returns:
        bool: True if the table was created, False otherwise.
    """

    global NAME, TABLES

    try:
        if not ensure_json(path=TABLES[table_name]):
            return False

        if not is_dict_empty(get_table_content(table_name=table_name)):
            return False

        write_table_content(
            table_name=table_name,
            table={
                "created_at": get_now_str(),
                "created_on": get_today_str(),
                "entries": {"total": 0, "values": {}},
                "metadata": {},
                "name": TABLES[table_name].stem,
                "schema": {"fields": {"total": 0, "values": []}},
                "updated_at": get_now_str(),
                "updated_on": get_today_str(),
                "uuid": get_uuid_str(),
            },
        )

        return True
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to create table with name '{table_name}'.",
        )
        return False


def empty_table(
    table_name: Literal[
        "answers",
        "configs",
        "customfields",
        "difficulties",
        "flashcards",
        "images",
        "notes",
        "priorities",
        "questions",
        "rehearsal_runs",
        "rehearsal_run_items",
        "stacks",
        "subjects",
        "teachers",
        "users",
    ],
) -> bool:
    """
    Empties the table.

    Args:
        table_name (Literal[...]): The name of the table. Can be one of:
            - "answers"
            - "configs"
            - "customfields"
            - "difficulties"
            - "flashcards"
            - "images"
            - "notes"
            - "priorities"
            - "questions"
            - "rehearsal_runs"
            - "rehearsal_run_items"
            - "stacks"
            - "subjects"
            - "teachers"
            - "users"

    Returns:
        bool: True if the table was emptied, False otherwise.
    """

    global NAME

    try:
        table: dict[str, Any] = get_table_content(table_name=table_name)

        table["entries"]["values"] = {}
        table["entries"]["total"] = 0

        return write_table_content(
            table_name=table_name,
            table=table,
        )
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to empty table with name '{table_name}'.",
        )
        return False


def filter_table_entries(
    table_name: Literal[
        "answers",
        "configs",
        "customfields",
        "difficulties",
        "flashcards",
        "images",
        "notes",
        "priorities",
        "questions",
        "rehearsal_runs",
        "rehearsal_run_items",
        "stacks",
        "subjects",
        "teachers",
        "users",
    ],
    **kwargs,
) -> list[dict[str, Any]]:
    """
    Filters the entries in the table.

    Args:
        table_name (Literal[...]): The name of the table. Can be one of:
            - "answers"
            - "configs"
            - "customfields"
            - "difficulties"
            - "flashcards"
            - "images"
            - "notes"
            - "priorities"
            - "questions"
            - "rehearsal_runs"
            - "rehearsal_run_items"
            - "stacks"
            - "subjects"
            - "teachers"
            - "users"
        **kwargs (dict[str, Any]): The keyword arguments to filter by.

    Returns:
        list[dict[str, Any]]: The filtered entries.
    """

    global NAME

    try:
        return list(
            filter(
                lambda entry: all(
                    entry.get(key) == value
                    for (
                        key,
                        value,
                    ) in kwargs.items()
                ),
                get_all_table_entries(table_name=table_name),
            )
        )
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to filter entries in table with name '{table_name}'.",
        )
        return []


def get_all_table_entries(
    table_name: Literal[
        "answers",
        "configs",
        "customfields",
        "difficulties",
        "flashcards",
        "images",
        "notes",
        "priorities",
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
    Gets all entries from the table.

    Args:
        table_name (Literal[...]): The name of the table. Can be one of:
            - "answers"
            - "configs"
            - "customfields"
            - "difficulties"
            - "flashcards"
            - "images"
            - "notes"
            - "priorities"
            - "questions"
            - "rehearsal_runs"
            - "rehearsal_run_items"
            - "stacks"
            - "subjects"
            - "teachers"
            - "users"

    Returns:
        dict[str, Any]: The table.
    """

    global NAME

    try:
        return (
            get_table_content(table_name=table_name)
            .get(
                "entries",
                {},
            )
            .get(
                "values",
                {},
            )
            .values()
        )
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to get all entries from table with name '{table_name}'.",
        )
        return []


def get_table_entry(
    id: Union[int, str],
    table_name: Literal[
        "answers",
        "configs",
        "customfields",
        "difficulties",
        "flashcards",
        "images",
        "notes",
        "priorities",
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
        id (Union[int, str]): The ID of the entry to retrieve.
        table_name (Literal[...]): The name of the table. Can be one of:
            - "answers"
            - "configs"
            - "customfields"
            - "difficulties"
            - "flashcards"
            - "images"
            - "notes"
            - "priorities"
            - "questions"
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

    global NAME

    try:
        if isinstance(
            id,
            int,
        ):
            id = str(id)

        return (
            get_table_content(table_name=table_name)
            .get(
                "entries",
                {},
            )
            .get(
                "values",
                {},
            )
            .get(
                id,
                {},
            )
        )
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to get entry with ID '{id}' from table with name '{table_name}'.",
        )
        return {}


def get_table_entries(
    ids: list[Union[int, str]],
    table_name: Literal[
        "answers",
        "configs",
        "customfields",
        "difficulties",
        "flashcards",
        "images",
        "notes",
        "priorities",
        "questions",
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
        ids (list[Union[int, str]]): The IDs of the entries to retrieve.
        table_name (Literal[...]): The name of the table. Can be one of:
            - "answers"
            - "configs"
            - "customfields"
            - "difficulties"
            - "flashcards"
            - "images"
            - "notes"
            - "priorities"
            - "questions"
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

    global NAME

    try:
        return [
            get_table_entry(
                id=id,
                table_name=table_name,
            )
            for id in ids
        ]
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to get entries with IDs '{ids}' from table with name '{table_name}'.",
        )
        return []


def get_table_content(
    table_name: Literal[
        "answers",
        "configs",
        "customfields",
        "difficulties",
        "flashcards",
        "images",
        "notes",
        "priorities",
        "questions",
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
        table_name (Literal[...]): The name of the table. Can be one of:
            - "answers"
            - "configs"
            - "customfields"
            - "difficulties"
            - "flashcards"
            - "images"
            - "notes"
            - "priorities"
            - "questions"
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

    global NAME

    try:
        ensure_json(path=get_table_file_path(table_name=table_name))
        return get_file_content_json(path=get_table_file_path(table_name=table_name))
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to get content of table with name '{table_name}'.",
        )
        return {}


def get_table_file_path(
    table_name: Literal[
        "answers",
        "configs",
        "customfields",
        "difficulties",
        "flashcards",
        "images",
        "notes",
        "priorities",
        "questions",
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
        table_name (Literal[...]): The name of the table. Can be one of:
            - "answers"
            - "configs"
            - "customfields"
            - "difficulties"
            - "flashcards"
            - "images"
            - "notes"
            - "priorities"
            - "questions"
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

    global NAME, TABLES

    try:
        return TABLES[table_name]
    except KeyError as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to get file path for table with name '{table_name}'.",
        )
        raise e
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to get file path for table with name '{table_name}'.",
        )
        raise e


def is_table_empty(
    table_name: Literal[
        "answers",
        "configs",
        "customfields",
        "difficulties",
        "flashcards",
        "images",
        "notes",
        "priorities",
        "questions",
        "rehearsal_run_items",
        "stacks",
        "subjects",
        "teachers",
        "users",
    ],
) -> bool:
    """
    Returns True if the table is empty, False otherwise.

    Args:
        table_name (Literal[...]): The name of the table. Can be one of:
            - "answers"
            - "configs"
            - "customfields"
            - "difficulties"
            - "flashcards"
            - "images"
            - "notes"
            - "priorities"
            - "questions"
            - "rehearsal_run_items"
            - "stacks"
            - "subjects"
            - "teachers"
            - "users"

    Returns:
        bool: True if the table is empty, False otherwise.
    """

    global NAME

    try:
        return is_dict_empty(dictionary=get_table_content(table_name=table_name))
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to check if table with name '{table_name}' is empty.",
        )
        return False


def remove_table_entry(
    id: Union[int, str],
    table_name: Literal[
        "answers",
        "configs",
        "customfields",
        "difficulties",
        "flashcards",
        "images",
        "notes",
        "priorities",
        "questions",
        "rehearsal_run_items",
        "stacks",
        "subjects",
        "teachers",
        "users",
    ],
) -> bool:
    """
    Removes an entry from the table.

    Args:
        id (Union[int, str]): The ID of the entry to remove.
        table_name (Literal[...]): The name of the table. Can be one of:
            - "answers"
            - "configs"
            - "customfields"
            - "difficulties"
            - "flashcards"
            - "images"
            - "notes"
            - "priorities"
            - "questions"
            - "rehearsal_run_items"
            - "stacks"
            - "subjects"
            - "teachers"
            - "users"

    Returns:
        bool: True if the entry was removed, False otherwise.

    Raises:
        Exception: If there is an error removing the entry.
    """

    global NAME

    try:
        table: dict[str, Any] = get_table_content(table_name=table_name)

        table["entries"]["values"].pop(str(id), None)

        table["entries"]["total"] -= 1

        return write_table_content(
            table_name=table_name,
            table=table,
        )
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to remove entry with ID '{id}' from table with name '{table_name}'.",
        )
        return False


def remove_table_entries(
    ids: list[Union[int, str]],
    table_name: Literal[
        "answers",
        "configs",
        "customfields",
        "difficulties",
        "flashcards",
        "images",
        "notes",
        "priorities",
        "questions",
        "rehearsal_run_items",
        "stacks",
        "subjects",
        "teachers",
        "users",
    ],
) -> list[bool]:
    """
    Removes multiple entries from the table.

    Args:
        ids (list[Union[int, str]]): The IDs of the entries to remove.
        table_name (Literal[...]): The name of the table. Can be one of:
            - "answers"
            - "configs"
            - "customfields"
            - "difficulties"
            - "flashcards"
            - "images"
            - "notes"
            - "priorities"
            - "questions"
            - "rehearsal_runs"
            - "rehearsal_run_items"
            - "stacks"
            - "subjects"
            - "teachers"
            - "users"

    Returns:
        list[bool]: A list of booleans indicating whether each entry was removed.

    Raises:
        Exception: If there is an error removing the entries.
    """

    global NAME

    try:
        return [
            remove_table_entry(
                id=id,
                table_name=table_name,
            )
            for id in ids
        ]
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to remove entries with IDs '{ids}' from table with name '{table_name}'.",
        )
        return []


def update_table_entry(
    entry: dict[str, Any],
    id: Union[int, str],
    table_name: Literal[
        "answers",
        "configs",
        "customfields",
        "difficulties",
        "flashcards",
        "images",
        "notes",
        "priorities",
        "questions",
        "rehearsal_runs",
        "rehearsal_run_items",
        "stacks",
        "subjects",
        "teachers",
        "users",
    ],
) -> bool:
    """
    Updates an entry in the table.

    Args:
        entry (dict[str, Any]): The entry to update.
        id (Union[int, str]): The ID of the entry to update.
        table_name (Literal[...]): The name of the table. Can be one of:
            - "answers"
            - "configs"
            - "customfields"
            - "difficulties"
            - "flashcards"
            - "images"
            - "notes"
            - "priorities"
            - "questions"
            - "rehearsal_runs"
            - "rehearsal_run_items"
            - "stacks"
            - "subjects"
            - "teachers"
            - "users"

    Returns:
        bool: True if the entry was updated, False otherwise.

    Raises:
        Exception: If there is an error updating the entry.
    """

    global NAME

    try:
        table: dict[str, Any] = get_table_content(table_name=table_name)

        if not is_key_in_dict(
            key=str(id),
            dictionary=table["entries"]["values"],
        ):
            return False

        entry["updated_at"] = get_now_str()
        entry["updated_on"] = get_today_str()

        table["entries"]["values"][str(id)] = entry

        table["schema"]["fields"]["values"] = sorted(
            list(set(table["schema"]["fields"]["values"] + list(entry.keys())))
        )

        table["schema"]["fields"]["total"] = len(table["schema"]["fields"]["values"])

        return write_table_content(
            table_name=table_name,
            table=table,
        )
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to update entry with ID '{id}' in table with name '{table_name}'.",
        )
        return False


def update_table_entries(
    entries: list[dict[str, Any]],
    ids: list[Union[int, str]],
    table_name: Literal[
        "answers",
        "configs",
        "customfields",
        "difficulties",
        "flashcards",
        "images",
        "notes",
        "priorities",
        "questions",
        "rehearsal_run_items",
        "stacks",
        "subjects",
        "teachers",
        "users",
    ],
) -> list[bool]:
    """
    Updates multiple entries in the table.

    Args:
        entries (list[dict[str, Any]]): The entries to update.
        ids (list[Union[int, str]]): The IDs of the entries to update.
        table_name (Literal[...]): The name of the table. Can be one of:
            - "answers"
            - "configs"
            - "customfields"
            - "difficulties"
            - "flashcards"
            - "images"
            - "notes"
            - "priorities"
            - "questions"
            - "rehearsal_runs"
            - "rehearsal_run_items"
            - "stacks"
            - "subjects"
            - "teachers"
            - "users"

    Returns:
        list[bool]: A list of booleans indicating whether each entry was updated.

    Raises:
        ValueError: If the number of entries and IDs do not match.
        Exception: If there is an error updating the entries.
    """

    global NAME

    try:
        return [
            update_table_entry(
                entry=entry,
                id=id,
                table_name=table_name,
            )
            for entry, id in zip(
                entries,
                ids,
                strict=True,
            )
        ]
    except ValueError as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to update entries with IDs '{ids}' in table with name '{table_name}'.",
        )
        raise e
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to update entries with IDs '{ids}' in table with name '{table_name}'.",
        )
        raise e


def write_table_content(
    table_name: Literal[
        "answers",
        "configs",
        "customfields",
        "difficulties",
        "flashcards",
        "images",
        "notes",
        "priorities",
        "questions",
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
        table_name (Literal[...]): The name of the table. Can be one of:
            - "answers"
            - "configs"
            - "customfields"
            - "difficulties"
            - "flashcards"
            - "images"
            - "notes"
            - "priorities"
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

    global NAME

    try:
        ensure_json(path=get_table_file_path(table_name=table_name))
        return write_file_json(
            data=table,
            path=get_table_file_path(table_name=table_name),
        )
    except Exception as e:
        log_exception(
            exception=e,
            name=NAME,
            message=f"Failed to write table content to file with name '{table_name}'.",
        )
        return False


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
