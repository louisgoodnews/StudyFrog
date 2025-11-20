"""
Author: Louis Goodnews
Date: 2025-11-16
"""

from typing import Any, Callable, Final, Literal, Union

from core.storage import (
    add_table_entries,
    add_table_entry,
    get_all_table_entries,
    get_table_entries,
    get_table_entry,
    remove_table_entries,
    remove_table_entry,
    update_table_entries,
    update_table_entry,
)
from utils.utils import log_exception


# ---------- Constants ---------- #

ANSWERS: Final[Literal["answers"]] = "answers"

ASSOCIATIONS: Final[Literal["associations"]] = "associations"

CUSTOMFIELDS: Final[Literal["customfields"]] = "customfields"

DIFFICULTIES: Final[Literal["difficulties"]] = "difficulties"

FLASHCARDS: Final[Literal["flashcards"]] = "flashcards"

IMAGES: Final[Literal["images"]] = "images"

NAME: Final[Literal["core.objects"]] = "core.objects"

NOTES: Final[Literal["notes"]] = "notes"

OPTIONS: Final[Literal["options"]] = "options"

PRIORITIES: Final[Literal["priorities"]] = "priorities"

QUESTIONS: Final[Literal["questions"]] = "questions"

REHEARSAL_RUNS: Final[Literal["rehearsal_runs"]] = "rehearsal_runs"

REHEARSAL_RUN_ITEMS: Final[Literal["rehearsal_run_items"]] = "rehearsal_run_items"

STACKS: Final[Literal["stacks"]] = "stacks"

SUBJECTS: Final[Literal["subjects"]] = "subjects"

TAGS: Final[Literal["tags"]] = "tags"

TEACHERS: Final[Literal["teachers"]] = "teachers"

USERS: Final[Literal["users"]] = "users"


# ---------- Functions ---------- #


def _make_add_entries(table_name: str) -> Callable[[list[dict[str, Any]]], list[int]]:
    """
    Make a function to add entries to the table.

    Args:
        table_name (str): Name of the table.

    Returns:
        Callable[[list[dict[str, Any]]], list[int]]: Function to add entries to the table.
    """

    def add_entries(entries: list[dict[str, Any]]) -> list[int]:
        """
        Add entries to the table.

        Args:
            entries (list[dict[str, Any]]): List of entries to add to the table.

        Returns:
            list[int]: List of IDs of the added entries.

        Raises:
            Exception: If the entries were not added.
        """
        try:
            return add_table_entries(
                entries=entries,
                table_name=table_name,
            )
        except Exception as e:
            log_exception(
                exception=e,
                message=f"Failed to add entries to table {table_name}",
                name=NAME,
            )
            raise Exception(f"Failed to add entries to table {table_name}: {e}") from e

    return add_entries


def _make_add_entry(table_name: str) -> Callable[[dict[str, Any]], int]:
    """
    Make a function to add an entry to the table.

    Args:
        table_name (str): Name of the table.

    Returns:
        Callable[[dict[str, Any]], int]: Function to add an entry to the table.
    """

    def add_entry(entry: dict[str, Any]) -> int:
        """
        Add an entry to the table.

        Args:
            entry (dict[str, Any]): Entry to add to the table.

        Returns:
            int: ID of the added entry.

        Raises:
            Exception: If the entry was not added.
        """
        try:
            return add_table_entry(
                entry=entry,
                table_name=table_name,
            )
        except Exception as e:
            log_exception(
                exception=e,
                message=f"Failed to add entry to table {table_name}",
                name=NAME,
            )
            raise Exception(f"Failed to add entry to table {table_name}: {e}") from e

    return add_entry


def _make_get_all_entries(table_name: str) -> Callable[[None], list[dict[str, Any]]]:
    """
    Make a function to get all entries from the table.

    Args:
        table_name (str): Name of the table.

    Returns:
        Callable[[None], list[dict[str, Any]]]: Function to get all entries from the table.
    """

    def get_all_entries() -> list[dict[str, Any]]:
        """
        Get all entries from the table.

        Returns:
            list[dict[str, Any]]: List of all entries in the table.

        Raises:
            Exception: If the entries were not retrieved.
        """
        try:
            return get_all_table_entries(table_name)
        except Exception as e:
            log_exception(
                exception=e,
                message=f"Failed to get all entries from table {table_name}",
                name=NAME,
            )
            raise Exception(f"Failed to get all entries from table {table_name}: {e}") from e

    return get_all_entries


def _make_get_entry(table_name: str) -> Callable[[int], dict[str, Any]]:
    """
    Make a function to get an entry from the table.

    Args:
        table_name (str): Name of the table.

    Returns:
        Callable[[int], dict[str, Any]]: Function to get an entry from the table.
    """

    def get_entry(entry_id: int) -> dict[str, Any]:
        """
        Get an entry from the table.

        Args:
            entry_id (int): ID of the entry.

        Returns:
            dict[str, Any]: Entry from the table.

        Raises:
            Exception: If the entry was not retrieved.
        """
        try:
            return get_table_entry(
                entry_id=entry_id,
                table_name=table_name,
            )
        except Exception as e:
            log_exception(
                exception=e,
                message=f"Failed to get entry {entry_id} from table {table_name}",
                name=NAME,
            )
            raise Exception(f"Failed to get entry {entry_id} from table {table_name}: {e}") from e

    return get_entry


def _make_get_entries(table_name: str) -> Callable[[list[int]], list[dict[str, Any]]]:
    """
    Make a function to get entries from the table.

    Args:
        table_name (str): Name of the table.

    Returns:
        Callable[[list[int]], list[dict[str, Any]]]: Function to get entries from the table.
    """

    def get_entries(entry_ids: list[int]) -> list[dict[str, Any]]:
        """
        Get entries from the table.

        Args:
            entry_ids (list[int]): IDs of the entries.

        Returns:
            list[dict[str, Any]]: List of entries from the table.

        Raises:
            Exception: If the entries were not retrieved.
        """
        try:
            return get_table_entries(
                entry_ids=entry_ids,
                table_name=table_name,
            )
        except Exception as e:
            log_exception(
                exception=e,
                message=f"Failed to get entries {entry_ids} from table {table_name}",
                name=NAME,
            )
            raise Exception(
                f"Failed to get entries {entry_ids} from table {table_name}: {e}"
            ) from e

    return get_entries


def _make_remove_entries(table_name: str) -> Callable[[list[int]], list[bool]]:
    """
    Make a function to remove entries from the table.

    Args:
        table_name (str): Name of the table.

    Returns:
        Callable[[list[int]], list[bool]]: Function to remove entries from the table.
    """

    def remove_entries(entry_ids: list[int]) -> list[bool]:
        """
        Remove entries from the table.

        Args:
            entry_ids (list[int]): IDs of the entries.

        Returns:
            list[bool]: List of booleans indicating whether the entries were removed.

        Raises:
            Exception: If the entries were not removed.
        """
        try:
            return remove_table_entries(
                entry_ids=entry_ids,
                table_name=table_name,
            )
        except Exception as e:
            log_exception(
                exception=e,
                message=f"Failed to remove entries {entry_ids} from table {table_name}",
                name=NAME,
            )
            raise Exception(
                f"Failed to remove entries {entry_ids} from table {table_name}: {e}"
            ) from e

    return remove_entries


def _make_remove_entry(table_name: str) -> Callable[[int], bool]:
    """
    Make a function to remove an entry from the table.

    Args:
        table_name (str): Name of the table.

    Returns:
        Callable[[int], bool]: Function to remove an entry from the table.
    """

    def remove_entry(entry_id: int) -> bool:
        """
        Remove an entry from the table.

        Args:
            entry_id (int): ID of the entry.

        Returns:
            bool: True if the entry was removed, False otherwise.

        Raises:
            Exception: If the entry was not removed.
        """
        try:
            return remove_table_entry(
                entry_id=entry_id,
                table_name=table_name,
            )
        except Exception as e:
            log_exception(
                exception=e,
                message=f"Failed to remove entry {entry_id} from table {table_name}",
                name=NAME,
            )
            raise Exception(
                f"Failed to remove entry {entry_id} from table {table_name}: {e}"
            ) from e

    return remove_entry


def _make_update_entries(table_name: str) -> Callable[[list[int], dict[str, Any]], list[bool]]:
    """
    Make a function to update entries in the table.

    Args:
        table_name (str): Name of the table.

    Returns:
        Callable[[list[int], dict[str, Any]], list[bool]]: Function to update entries in the table.
    """

    def update_entries(
        entry_ids: list[int],
        entry: dict[str, Any],
    ) -> list[bool]:
        """
        Update entries in the table.

        Args:
            entry_ids (list[int]): IDs of the entries.
            entry (dict[str, Any]): Entry to update in the table.

        Returns:
            list[bool]: List of booleans indicating whether the entries were updated.

        Raises:
            Exception: If the entries were not updated.
        """
        try:
            return update_table_entries(
                entry_ids=entry_ids,
                entry=entry,
                table_name=table_name,
            )
        except Exception as e:
            log_exception(
                exception=e,
                message=f"Failed to update entries {entry_ids} in table {table_name}",
                name=NAME,
            )
            raise Exception(
                f"Failed to update entries {entry_ids} in table {table_name}: {e}"
            ) from e

    return update_entries


def _make_update_entry(table_name: str) -> Callable[[int, dict[str, Any]], bool]:
    """
    Make a function to update an entry in the table.

    Args:
        table_name (str): Name of the table.

    Returns:
        Callable[[int, dict[str, Any]], bool]: Function to update an entry in the table.
    """

    def update_entry(
        entry_id: int,
        entry: dict[str, Any],
    ) -> bool:
        """
        Update an entry in the table.

        Args:
            entry_id (int): ID of the entry.
            entry (dict[str, Any]): Entry to update in the table.

        Raises:
            Exception: If the entry was not updated.
        """
        try:
            return update_table_entry(
                entry_id=entry_id,
                entry=entry,
                table_name=table_name,
            )
        except Exception as e:
            log_exception(
                exception=e,
                message=f"Failed to update entry {entry_id} in table {table_name}",
                name=NAME,
            )
            raise Exception(f"Failed to update entry {entry_id} in table {table_name}: {e}") from e

    return update_entry


# ---------- Add One ---------- #

add_answer: Callable[[dict[str, Any]], int] = _make_add_entry(table_name=ANSWERS)
add_customfield: Callable[[dict[str, Any]], int] = _make_add_entry(table_name=CUSTOMFIELDS)
add_difficulty: Callable[[dict[str, Any]], int] = _make_add_entry(table_name=DIFFICULTIES)
add_flashcard: Callable[[dict[str, Any]], int] = _make_add_entry(table_name=FLASHCARDS)
add_image: Callable[[dict[str, Any]], int] = _make_add_entry(table_name=IMAGES)
add_note: Callable[[dict[str, Any]], int] = _make_add_entry(table_name=NOTES)
add_option: Callable[[dict[str, Any]], int] = _make_add_entry(table_name=OPTIONS)
add_priority: Callable[[dict[str, Any]], int] = _make_add_entry(table_name=PRIORITIES)
add_question: Callable[[dict[str, Any]], int] = _make_add_entry(table_name=QUESTIONS)
add_rehearsal_run: Callable[[dict[str, Any]], int] = _make_add_entry(table_name=REHEARSAL_RUNS)
add_rehearsal_run_item: Callable[[dict[str, Any]], int] = _make_add_entry(
    table_name=REHEARSAL_RUN_ITEMS
)
add_stack: Callable[[dict[str, Any]], int] = _make_add_entry(table_name=STACKS)
add_subject: Callable[[dict[str, Any]], int] = _make_add_entry(table_name=SUBJECTS)
add_tag: Callable[[dict[str, Any]], int] = _make_add_entry(table_name=TAGS)
add_teacher: Callable[[dict[str, Any]], int] = _make_add_entry(table_name=TEACHERS)
add_user: Callable[[dict[str, Any]], int] = _make_add_entry(table_name=USERS)


# ---------- Add Multiple ---------- #

add_answers: Callable[[list[dict[str, Any]]], list[int]] = _make_add_entries(table_name=ANSWERS)
add_customfields: Callable[[list[dict[str, Any]]], list[int]] = _make_add_entries(
    table_name=CUSTOMFIELDS
)
add_difficulties: Callable[[list[dict[str, Any]]], list[int]] = _make_add_entries(
    table_name=DIFFICULTIES
)
add_flashcards: Callable[[list[dict[str, Any]]], list[int]] = _make_add_entries(
    table_name=FLASHCARDS
)
add_images: Callable[[list[dict[str, Any]]], list[int]] = _make_add_entries(table_name=IMAGES)
add_notes: Callable[[list[dict[str, Any]]], list[int]] = _make_add_entries(table_name=NOTES)
add_options: Callable[[list[dict[str, Any]]], list[int]] = _make_add_entries(table_name=OPTIONS)
add_priorities: Callable[[list[dict[str, Any]]], list[int]] = _make_add_entries(
    table_name=PRIORITIES
)
add_questions: Callable[[list[dict[str, Any]]], list[int]] = _make_add_entries(table_name=QUESTIONS)
add_rehearsal_runs: Callable[[list[dict[str, Any]]], list[int]] = _make_add_entries(
    table_name=REHEARSAL_RUNS
)
add_rehearsal_run_items: Callable[[list[dict[str, Any]]], list[int]] = _make_add_entries(
    table_name=REHEARSAL_RUN_ITEMS
)
add_stacks: Callable[[list[dict[str, Any]]], list[int]] = _make_add_entries(table_name=STACKS)
add_subjects: Callable[[list[dict[str, Any]]], list[int]] = _make_add_entries(table_name=SUBJECTS)
add_tags: Callable[[list[dict[str, Any]]], list[int]] = _make_add_entries(table_name=TAGS)
add_teachers: Callable[[list[dict[str, Any]]], list[int]] = _make_add_entries(table_name=TEACHERS)
add_users: Callable[[list[dict[str, Any]]], list[int]] = _make_add_entries(table_name=USERS)


# ---------- Get All ---------- #

get_all_ansers: Callable[[None], list[dict[str, Any]]] = _make_get_all_entries(table_name=ANSWERS)
get_all_customfields: Callable[[None], list[dict[str, Any]]] = _make_get_all_entries(
    table_name=CUSTOMFIELDS
)
get_all_difficulties: Callable[[None], list[dict[str, Any]]] = _make_get_all_entries(
    table_name=DIFFICULTIES
)
get_all_flashcards: Callable[[None], list[dict[str, Any]]] = _make_get_all_entries(
    table_name=FLASHCARDS
)
get_all_images: Callable[[None], list[dict[str, Any]]] = _make_get_all_entries(table_name=IMAGES)
get_all_notes: Callable[[None], list[dict[str, Any]]] = _make_get_all_entries(table_name=NOTES)
get_all_options: Callable[[None], list[dict[str, Any]]] = _make_get_all_entries(table_name=OPTIONS)
get_all_priorities: Callable[[None], list[dict[str, Any]]] = _make_get_all_entries(
    table_name=PRIORITIES
)
get_all_questions: Callable[[None], list[dict[str, Any]]] = _make_get_all_entries(
    table_name=QUESTIONS
)
get_all_rehearsal_runs: Callable[[None], list[dict[str, Any]]] = _make_get_all_entries(
    table_name=REHEARSAL_RUNS
)
get_all_rehearsal_run_items: Callable[[None], list[dict[str, Any]]] = _make_get_all_entries(
    table_name=REHEARSAL_RUN_ITEMS
)
get_all_stacks: Callable[[None], list[dict[str, Any]]] = _make_get_all_entries(table_name=STACKS)
get_all_subjects: Callable[[None], list[dict[str, Any]]] = _make_get_all_entries(
    table_name=SUBJECTS
)
get_all_tags: Callable[[None], list[dict[str, Any]]] = _make_get_all_entries(table_name=TAGS)
get_all_teachers: Callable[[None], list[dict[str, Any]]] = _make_get_all_entries(
    table_name=TEACHERS
)
get_all_users: Callable[[None], list[dict[str, Any]]] = _make_get_all_entries(table_name=USERS)


# ---------- Get One ---------- #

get_answer: Callable[[Union[int, str]], dict[str, Any]] = _make_get_entry(table_name=ANSWERS)
get_customfield: Callable[[Union[int, str]], dict[str, Any]] = _make_get_entry(
    table_name=CUSTOMFIELDS
)
get_difficulty: Callable[[Union[int, str]], dict[str, Any]] = _make_get_entry(
    table_name=DIFFICULTIES
)
get_flashcard: Callable[[Union[int, str]], dict[str, Any]] = _make_get_entry(table_name=FLASHCARDS)
get_image: Callable[[Union[int, str]], dict[str, Any]] = _make_get_entry(table_name=IMAGES)
get_note: Callable[[Union[int, str]], dict[str, Any]] = _make_get_entry(table_name=NOTES)
get_option: Callable[[Union[int, str]], dict[str, Any]] = _make_get_entry(table_name=OPTIONS)
get_priority: Callable[[Union[int, str]], dict[str, Any]] = _make_get_entry(table_name=PRIORITIES)
get_question: Callable[[Union[int, str]], dict[str, Any]] = _make_get_entry(table_name=QUESTIONS)
get_rehearsal_run: Callable[[Union[int, str]], dict[str, Any]] = _make_get_entry(
    table_name=REHEARSAL_RUNS
)
get_rehearsal_run_item: Callable[[Union[int, str]], dict[str, Any]] = _make_get_entry(
    table_name=REHEARSAL_RUN_ITEMS
)
get_stack: Callable[[Union[int, str]], dict[str, Any]] = _make_get_entry(table_name=STACKS)
get_subject: Callable[[Union[int, str]], dict[str, Any]] = _make_get_entry(table_name=SUBJECTS)
get_tag: Callable[[Union[int, str]], dict[str, Any]] = _make_get_entry(table_name=TAGS)
get_teacher: Callable[[Union[int, str]], dict[str, Any]] = _make_get_entry(table_name=TEACHERS)
get_user: Callable[[Union[int, str]], dict[str, Any]] = _make_get_entry(table_name=USERS)


# ---------- Get Multiple ---------- #

get_answers: Callable[[list[Union[int, str]]], list[dict[str, Any]]] = _make_get_entries(
    table_name=ANSWERS
)
get_customfields: Callable[[list[Union[int, str]]], list[dict[str, Any]]] = _make_get_entries(
    table_name=CUSTOMFIELDS
)
get_difficulties: Callable[[list[Union[int, str]]], list[dict[str, Any]]] = _make_get_entries(
    table_name=DIFFICULTIES
)
get_flashcards: Callable[[list[Union[int, str]]], list[dict[str, Any]]] = _make_get_entries(
    table_name=FLASHCARDS
)
get_images: Callable[[list[Union[int, str]]], list[dict[str, Any]]] = _make_get_entries(
    table_name=IMAGES
)
get_notes: Callable[[list[Union[int, str]]], list[dict[str, Any]]] = _make_get_entries(
    table_name=NOTES
)
get_options: Callable[[list[Union[int, str]]], list[dict[str, Any]]] = _make_get_entries(
    table_name=OPTIONS
)
get_priorities: Callable[[list[Union[int, str]]], list[dict[str, Any]]] = _make_get_entries(
    table_name=PRIORITIES
)
get_questions: Callable[[list[Union[int, str]]], list[dict[str, Any]]] = _make_get_entries(
    table_name=QUESTIONS
)
get_rehearsal_runs: Callable[[list[Union[int, str]]], list[dict[str, Any]]] = _make_get_entries(
    table_name=REHEARSAL_RUNS
)
get_rehearsal_run_items: Callable[[list[Union[int, str]]], list[dict[str, Any]]] = (
    _make_get_entries(table_name=REHEARSAL_RUN_ITEMS)
)
get_stacks: Callable[[list[Union[int, str]]], list[dict[str, Any]]] = _make_get_entries(
    table_name=STACKS
)
get_subjects: Callable[[list[Union[int, str]]], list[dict[str, Any]]] = _make_get_entries(
    table_name=SUBJECTS
)
get_tags: Callable[[list[Union[int, str]]], list[dict[str, Any]]] = _make_get_entries(
    table_name=TAGS
)
get_teachers: Callable[[list[Union[int, str]]], list[dict[str, Any]]] = _make_get_entries(
    table_name=TEACHERS
)
get_users: Callable[[list[Union[int, str]]], list[dict[str, Any]]] = _make_get_entries(
    table_name=USERS
)


# ---------- Remove One ---------- #

remove_answer: Callable[[Union[int, str]], None] = _make_remove_entry(table_name=ANSWERS)
remove_customfield: Callable[[Union[int, str]], None] = _make_remove_entry(table_name=CUSTOMFIELDS)
remove_difficulty: Callable[[Union[int, str]], None] = _make_remove_entry(table_name=DIFFICULTIES)
remove_flashcard: Callable[[Union[int, str]], None] = _make_remove_entry(table_name=FLASHCARDS)
remove_image: Callable[[Union[int, str]], None] = _make_remove_entry(table_name=IMAGES)
remove_note: Callable[[Union[int, str]], None] = _make_remove_entry(table_name=NOTES)
remove_option: Callable[[Union[int, str]], None] = _make_remove_entry(table_name=OPTIONS)
remove_priority: Callable[[Union[int, str]], None] = _make_remove_entry(table_name=PRIORITIES)
remove_question: Callable[[Union[int, str]], None] = _make_remove_entry(table_name=QUESTIONS)
remove_rehearsal_run: Callable[[Union[int, str]], None] = _make_remove_entry(
    table_name=REHEARSAL_RUNS
)
remove_rehearsal_run_item: Callable[[Union[int, str]], None] = _make_remove_entry(
    table_name=REHEARSAL_RUN_ITEMS
)
remove_stack: Callable[[Union[int, str]], None] = _make_remove_entry(table_name=STACKS)
remove_subject: Callable[[Union[int, str]], None] = _make_remove_entry(table_name=SUBJECTS)
remove_tag: Callable[[Union[int, str]], None] = _make_remove_entry(table_name=TAGS)
remove_teacher: Callable[[Union[int, str]], None] = _make_remove_entry(table_name=TEACHERS)
remove_user: Callable[[Union[int, str]], None] = _make_remove_entry(table_name=USERS)


# ---------- Remove Multiple ---------- #

remove_answers: Callable[[list[Union[int, str]]], None] = _make_remove_entries(table_name=ANSWERS)
remove_customfields: Callable[[list[Union[int, str]]], None] = _make_remove_entries(
    table_name=CUSTOMFIELDS
)
remove_difficulties: Callable[[list[Union[int, str]]], None] = _make_remove_entries(
    table_name=DIFFICULTIES
)
remove_flashcards: Callable[[list[Union[int, str]]], None] = _make_remove_entries(
    table_name=FLASHCARDS
)
remove_images: Callable[[list[Union[int, str]]], None] = _make_remove_entries(table_name=IMAGES)
remove_notes: Callable[[list[Union[int, str]]], None] = _make_remove_entries(table_name=NOTES)
remove_options: Callable[[list[Union[int, str]]], None] = _make_remove_entries(table_name=OPTIONS)
remove_priorities: Callable[[list[Union[int, str]]], None] = _make_remove_entries(
    table_name=PRIORITIES
)
remove_questions: Callable[[list[Union[int, str]]], None] = _make_remove_entries(
    table_name=QUESTIONS
)
remove_rehearsal_runs: Callable[[list[Union[int, str]]], None] = _make_remove_entries(
    table_name=REHEARSAL_RUNS
)
remove_rehearsal_run_items: Callable[[list[Union[int, str]]], None] = _make_remove_entries(
    table_name=REHEARSAL_RUN_ITEMS
)
remove_stacks: Callable[[list[Union[int, str]]], None] = _make_remove_entries(table_name=STACKS)
remove_subjects: Callable[[list[Union[int, str]]], None] = _make_remove_entries(table_name=SUBJECTS)
remove_tags: Callable[[list[Union[int, str]]], None] = _make_remove_entries(table_name=TAGS)
remove_teachers: Callable[[list[Union[int, str]]], None] = _make_remove_entries(table_name=TEACHERS)
remove_users: Callable[[list[Union[int, str]]], None] = _make_remove_entries(table_name=USERS)

# ---------- Update One ---------- #

update_answer: Callable[[Union[int, str], dict[str, Any]], None] = _make_update_entry(
    table_name=ANSWERS
)
update_customfield: Callable[[Union[int, str], dict[str, Any]], None] = _make_update_entry(
    table_name=CUSTOMFIELDS
)
update_difficulty: Callable[[Union[int, str], dict[str, Any]], None] = _make_update_entry(
    table_name=DIFFICULTIES
)
update_flashcard: Callable[[Union[int, str], dict[str, Any]], None] = _make_update_entry(
    table_name=FLASHCARDS
)
update_image: Callable[[Union[int, str], dict[str, Any]], None] = _make_update_entry(
    table_name=IMAGES
)
update_note: Callable[[Union[int, str], dict[str, Any]], None] = _make_update_entry(
    table_name=NOTES
)
update_option: Callable[[Union[int, str], dict[str, Any]], None] = _make_update_entry(
    table_name=OPTIONS
)
update_priority: Callable[[Union[int, str], dict[str, Any]], None] = _make_update_entry(
    table_name=PRIORITIES
)
update_question: Callable[[Union[int, str], dict[str, Any]], None] = _make_update_entry(
    table_name=QUESTIONS
)
update_rehearsal_run: Callable[[Union[int, str], dict[str, Any]], None] = _make_update_entry(
    table_name=REHEARSAL_RUNS
)
update_rehearsal_run_item: Callable[[Union[int, str], dict[str, Any]], None] = _make_update_entry(
    table_name=REHEARSAL_RUN_ITEMS
)
update_stack: Callable[[Union[int, str], dict[str, Any]], None] = _make_update_entry(
    table_name=STACKS
)
update_subject: Callable[[Union[int, str], dict[str, Any]], None] = _make_update_entry(
    table_name=SUBJECTS
)
update_tag: Callable[[Union[int, str], dict[str, Any]], None] = _make_update_entry(table_name=TAGS)
update_teacher: Callable[[Union[int, str], dict[str, Any]], None] = _make_update_entry(
    table_name=TEACHERS
)
update_user: Callable[[Union[int, str], dict[str, Any]], None] = _make_update_entry(
    table_name=USERS
)


# ---------- Update Multiple ---------- #

update_answers: Callable[[list[Union[int, str]], dict[str, Any]], None] = _make_update_entries(
    table_name=ANSWERS
)
update_customfields: Callable[[list[Union[int, str]], dict[str, Any]], None] = _make_update_entries(
    table_name=CUSTOMFIELDS
)
update_difficulties: Callable[[list[Union[int, str]], dict[str, Any]], None] = _make_update_entries(
    table_name=DIFFICULTIES
)
update_flashcards: Callable[[list[Union[int, str]], dict[str, Any]], None] = _make_update_entries(
    table_name=FLASHCARDS
)
update_images: Callable[[list[Union[int, str]], dict[str, Any]], None] = _make_update_entries(
    table_name=IMAGES
)
update_notes: Callable[[list[Union[int, str]], dict[str, Any]], None] = _make_update_entries(
    table_name=NOTES
)
update_options: Callable[[list[Union[int, str]], dict[str, Any]], None] = _make_update_entries(
    table_name=OPTIONS
)
update_priorities: Callable[[list[Union[int, str]], dict[str, Any]], None] = _make_update_entries(
    table_name=PRIORITIES
)
update_questions: Callable[[list[Union[int, str]], dict[str, Any]], None] = _make_update_entries(
    table_name=QUESTIONS
)
update_rehearsal_runs: Callable[[list[Union[int, str]], dict[str, Any]], None] = (
    _make_update_entries(table_name=REHEARSAL_RUNS)
)
update_rehearsal_run_items: Callable[[list[Union[int, str]], dict[str, Any]], None] = (
    _make_update_entries(table_name=REHEARSAL_RUN_ITEMS)
)
update_stacks: Callable[[list[Union[int, str]], dict[str, Any]], None] = _make_update_entries(
    table_name=STACKS
)
update_subjects: Callable[[list[Union[int, str]], dict[str, Any]], None] = _make_update_entries(
    table_name=SUBJECTS
)
update_tags: Callable[[list[Union[int, str]], dict[str, Any]], None] = _make_update_entries(
    table_name=TAGS
)
update_teachers: Callable[[list[Union[int, str]], dict[str, Any]], None] = _make_update_entries(
    table_name=TEACHERS
)
update_users: Callable[[list[Union[int, str]], dict[str, Any]], None] = _make_update_entries(
    table_name=USERS
)


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
