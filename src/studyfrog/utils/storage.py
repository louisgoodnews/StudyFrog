"""
Author: Louis Goodnews
Date: 2025-12-10
"""

from pathlib import Path
from typing import Any, Final, Optional, Union

from constants.common import PATTERNS
from constants.directories import DATA_DIR
from constants.events import *
from utils.common import (
    exists,
    generate_model_key,
    generate_uuid4_str,
    get_now_str,
    get_today_str,
    pluralize_word,
    search_string,
)
from utils.dispatcher import dispatch
from utils.files import (
    does_file_have_content,
    ensure_file,
    read_file_json,
    write_file_json,
)
from utils.logging import log_error, log_info


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "add_entry",
    "add_entry_if_not_exist",
    "add_entries",
    "add_entries_if_not_exist",
    "count_entries",
    "delete_entry",
    "delete_entries",
    "filter_entries",
    "get_all_entries",
    "get_entries",
    "get_entries_by_keys",
    "get_entry",
    "get_entry_by_keys",
    "update_entry",
    "update_entries",
]


# ---------- Helper Functions ---------- #


def _convert_for_database(model: dict[str, Any]) -> None:
    """
    Converts a model dictionary to a compatible database storage format.

    This function is used internally to update the database storage format of
    entries. It is not intended to be used externally.

    The function checks if the 'metadata' dictionary of the entry contains an
    'id_' key and if so, replaces it with an 'id' key. It also checks if
    the 'metadata' dictionary contains a 'uuid_' key and if so, replaces it
    with a 'uuid' key.

    Args:
        model (dict[str, Any]): The model dictionary to convert.

    Returns:
        None
    """

    for (
        key,
        value,
    ) in model.items():
        if not key.startswith("_"):
            continue

        model[key[1:]] = value

        del model[key]

    if exists(
        value=model.get("metadata", {}).get(
            "id_",
            None,
        )
    ):
        model["metadata"]["id"] = model["metadata"].pop("id_")

    if exists(
        value=model.get(
            "metadata",
            {},
        ).get(
            "uuid_",
            None,
        )
    ):
        model["metadata"]["uuid"] = model["metadata"].pop("uuid_")


def _convert_from_database(model: dict[str, Any]) -> None:
    """
    Converts a model dictionary from the database storage format to a compatible format.

    This function is used internally to convert the database storage format of
    entries to a compatible format. It is not intended to be used externally.

    The function checks if the 'metadata' dictionary of the entry contains an
    'id' key and if so, replaces it with an 'id_' key. It also checks if
    the 'metadata' dictionary contains a 'uuid' key and if so, replaces it
    with a 'uuid_' key.

    Args:
        model (dict[str, Any]): The model dictionary to convert.

    Returns:
        None
    """

    if exists(
        value=model.get("metadata", {}).get(
            "id",
            None,
        )
    ):
        model["metadata"]["id_"] = model["metadata"].pop("id")

    if exists(
        value=model.get("metadata", {}).get(
            "uuid",
            None,
        )
    ):
        model["metadata"]["uuid_"] = model["metadata"].pop("uuid")


def _decrement_table_counters(table_data: dict[str, Any]) -> None:
    """
    Decrements the table's 'next_id' and 'total' counters.

    The 'next_id' counter is typically decremented when an entry is removed,
    allowing the ID pool to potentially be reused or simply maintaining
    an accurate highest assigned ID count. The 'total' counter reflects the
    current number of entries.

    Args:
        table_data (dict[str, Any]): The table data dictionary containing the
                                     'metadata' and 'entries' structures.

    Returns:
        None
    """

    table_data["metadata"]["next_id"] -= 1
    table_data["entries"]["total"] -= 1


def _ensure_table_json_with_content(table_name: str) -> None:
    """
    Ensures that the JSON file for a specific table contains the minimal required structure.

    If the target JSON file is empty or does not exist, this function creates the file
    at `DATA_DIR / table` and initializes it with the standard, empty table structure,
    including metadata (timestamps, UUID, empty entries dictionary).
    If the file already has content, the function returns immediately.

    Args:
        table_name (str): The name of the table/collection (which is used as the filename)
                     to ensure (e.g., "flashcard.json").

    Returns:
        None

    Raises:
        Exception: If an error occurs during file writing or creation.
    """

    try:
        file: Path = DATA_DIR / (
            f"{table_name}.json" if not table_name.endswith(".json") else table_name
        )

        if does_file_have_content(file=file):
            return

        data: dict[str, Any] = {
            "created_at": get_now_str(),
            "created_on": get_today_str(),
            "entries": {
                "entries": {},
                "total": 0,
            },
            "metadata": {
                "fields": {
                    "fields": [],
                    "total": 0,
                },
                "next_id": 0,
                "schema": {},
            },
            "updated_at": get_now_str(),
            "updated_on": get_today_str(),
            "uuid": generate_uuid4_str(),
        }

        _save_table_data(
            table_data=data,
            table_name=table_name,
        )
    except Exception as e:
        log_error(
            message=f"Caught an exception while attempting to ensure '{table_name}' table JSON file with content: {e}"
        )
        dispatch(
            event=DB_OPERATION_FAILURE,
            message=f"Caught an exception while attempting to ensure '{table_name}' table JSON file with content: {e}",
        )
        raise e


def _ensure_table_json(table_name: str) -> None:
    """
    Ensures that a JSON table file exists.

    Args:
        table_name (str): The name of the table.

    Returns:
        None

    Raises:
        Exception: If the table file cannot be created.
    """

    try:
        file: Path = DATA_DIR / (
            f"{table_name}.json" if not table_name.endswith(".json") else table_name
        )

        ensure_file(file=file)

        _ensure_table_json_with_content(table_name=table_name)
    except Exception as e:
        log_error(
            message=f"Caught an exception while attempting to ensure '{table_name}' table JSON file: {e}"
        )
        dispatch(
            event=DB_OPERATION_FAILURE,
            message=f"Caught an exception while attempting to ensure '{table_name}' table JSON file: {e}",
        )
        raise e


def _get_add_event(model_type: str) -> str:
    """
    Retrieves the corresponding 'added' notification event string for a given model type.

    This function maps a lowercase model type identifier (e.g., 'flashcard', 'note')
    to the specific dispatcher notification event (e.g., FLASHCARD_ADDED, NOTE_ADDED)
    that should be broadcast after a successful entry creation operation.

    Args:
        model_type (str): The name of the data model type (e.g., 'flashcard', 'subject').
                          Case sensitivity is handled internally (converted to lowercase).

    Returns:
        str: The constant string identifier of the corresponding broadcast notification event.

    Raises:
        KeyError: If the provided 'model_type' is not defined in the internal mapping,
                  indicating no corresponding 'added' event exists for that model type.
    """

    try:
        return {
            "answer": ANSWER_ADDED,
            "customfield": CUSTOMFIELD_ADDED,
            "difficulty": DIFFICULTY_ADDED,
            "flashcard": FLASHCARD_ADDED,
            "image": IMAGE_ADDED,
            "note": NOTE_ADDED,
            "option": OPTION_ADDED,
            "priority": PRIORITY_ADDED,
            "question": QUESTION_ADDED,
            "rehearsal_run": REHEARSAL_RUN_ADDED,
            "rehearsal_run_item": REHEARSAL_RUN_ITEM_ADDED,
            "stack": STACK_ADDED,
            "subject": SUBJECT_ADDED,
            "tag": TAG_ADDED,
            "teacher": TEACHER_ADDED,
            "user": USER_ADDED,
        }[model_type.lower()]
    except KeyError as e:
        log_error(
            message=f"Caught a KeyError while attempting to get add event for '{model_type}' model: {e}"
        )
        log_error(message=f"No add event defined for '{model_type}' model")
        raise e


def _get_bulk_add_event(model_type: str) -> str:
    """
    Retrieves the corresponding 'bulk added' notification event string for a given model type.

    This function maps a lowercase model type identifier (e.g., 'flashcard', 'note')
    to the specific dispatcher notification event (e.g., FLASHCARDS_ADDED, NOTES_ADDED)
    that should be broadcast after a successful batch entry creation operation.

    Args:
        model_type (str): The name of the data model type (e.g., 'flashcard', 'subject').
                          Case sensitivity is handled internally (converted to lowercase).

    Returns:
        str: The constant string identifier of the corresponding bulk broadcast notification event.

    Raises:
        KeyError: If the provided 'model_type' is not defined in the internal mapping,
                  indicating no corresponding bulk 'added' event exists for that model type.
    """

    try:
        return {
            "answer": ANSWERS_ADDED,
            "customfield": CUSTOMFIELDS_ADDED,
            "difficulty": DIFFICULTIES_ADDED,
            "flashcard": FLASHCARDS_ADDED,
            "image": IMAGES_ADDED,
            "note": NOTES_ADDED,
            "option": OPTIONS_ADDED,
            "priority": PRIORITIES_ADDED,
            "question": QUESTIONS_ADDED,
            "rehearsal_run": REHEARSAL_RUNS_ADDED,
            "rehearsal_run_item": REHEARSAL_RUN_ITEMS_ADDED,
            "stack": STACKS_ADDED,
            "subject": SUBJECTS_ADDED,
            "tag": TAGS_ADDED,
            "teacher": TEACHERS_ADDED,
            "user": USERS_ADDED,
        }[model_type.lower()]
    except KeyError as e:
        log_error(
            message=f"Caught a KeyError while attempting to get add event for '{model_type}' model: {e}"
        )
        log_error(message=f"No add event defined for '{model_type}' model")
        raise e


def _get_bulk_delete_event(model_type: str) -> str:
    """
    Retrieves the corresponding 'bulk deleted' notification event string for a given model type.

    This function maps a lowercase model type identifier (e.g., 'flashcard', 'note')
    to the specific dispatcher notification event (e.g., FLASHCARDS_DELETED, NOTES_DELETED)
    that should be broadcast after a successful batch entry deletion operation.

    Args:
        model_type (str): The name of the data model type (e.g., 'flashcard', 'subject').
                          Case sensitivity is handled internally (converted to lowercase).

    Returns:
        str: The constant string identifier of the corresponding bulk broadcast notification event.

    Raises:
        KeyError: If the provided 'model_type' is not defined in the internal mapping.
    """

    try:
        return {
            "answer": ANSWERS_DELETED,
            "customfield": CUSTOMFIELDS_DELETED,
            "difficulty": DIFFICULTIES_DELETED,
            "flashcard": FLASHCARDS_DELETED,
            "image": IMAGES_DELETED,
            "note": NOTES_DELETED,
            "option": OPTIONS_DELETED,
            "priority": PRIORITIES_DELETED,
            "question": QUESTIONS_DELETED,
            "rehearsal_run": REHEARSAL_RUNS_DELETED,
            "rehearsal_run_item": REHEARSAL_RUN_ITEMS_DELETED,
            "stack": STACKS_DELETED,
            "subject": SUBJECTS_DELETED,
            "tag": TAGS_DELETED,
            "teacher": TEACHERS_DELETED,
            "user": USERS_DELETED,
        }[model_type.lower()]
    except KeyError as e:
        log_error(
            message=f"Caught a KeyError while attempting to get bulk delete event for '{model_type}' model: {e}"
        )
        log_error(message=f"No bulk delete event defined for '{model_type}' model")
        raise e


def _get_bulk_get_event(model_type: str) -> str:
    """
    Retrieves the corresponding 'bulk retrieved' notification event string for a given model type.

    This function maps a lowercase model type identifier (e.g., 'flashcard', 'note')
    to the specific dispatcher notification event (e.g., FLASHCARDS_RETRIEVED, NOTES_RETRIEVED)
    that should be broadcast after a successful batch entry retrieval operation.

    Args:
        model_type (str): The name of the data model type (e.g., 'flashcard', 'subject').
                          Case sensitivity is handled internally (converted to lowercase).

    Returns:
        str: The constant string identifier of the corresponding bulk broadcast notification event.

    Raises:
        KeyError: If the provided 'model_type' is not defined in the internal mapping.
    """

    try:
        return {
            "answer": ANSWERS_RETRIEVED,
            "customfield": CUSTOMFIELDS_RETRIEVED,
            "difficulty": DIFFICULTIES_RETRIEVED,
            "flashcard": FLASHCARDS_RETRIEVED,
            "image": IMAGES_RETRIEVED,
            "note": NOTES_RETRIEVED,
            "option": OPTIONS_RETRIEVED,
            "priority": PRIORITIES_RETRIEVED,
            "question": QUESTIONS_RETRIEVED,
            "rehearsal_run": REHEARSAL_RUNS_RETRIEVED,
            "rehearsal_run_item": REHEARSAL_RUN_ITEMS_RETRIEVED,
            "stack": STACKS_RETRIEVED,
            "subject": SUBJECTS_RETRIEVED,
            "tag": TAGS_RETRIEVED,
            "teacher": TEACHERS_RETRIEVED,
            "user": USERS_RETRIEVED,
        }[model_type.lower()]
    except KeyError as e:
        log_error(
            message=f"Caught a KeyError while attempting to get bulk get event for '{model_type}' model: {e}"
        )
        log_error(message=f"No bulk get event defined for '{model_type}' model")
        raise e


def _get_bulk_update_event(model_type: str) -> str:
    """
    Retrieves the corresponding 'bulk updated' notification event string for a given model type.

    This function maps a lowercase model type identifier (e.g., 'flashcard', 'note')
    to the specific dispatcher notification event (e.g., FLASHCARDS_UPDATED, NOTES_UPDATED)
    that should be broadcast after a successful batch entry update operation.

    Args:
        model_type (str): The name of the data model type (e.g., 'flashcard', 'subject').
                          Case sensitivity is handled internally (converted to lowercase).

    Returns:
        str: The constant string identifier of the corresponding bulk broadcast notification event.

    Raises:
        KeyError: If the provided 'model_type' is not defined in the internal mapping.
    """

    try:
        return {
            "answer": ANSWERS_UPDATED,
            "customfield": CUSTOMFIELDS_UPDATED,
            "difficulty": DIFFICULTIES_UPDATED,
            "flashcard": FLASHCARDS_UPDATED,
            "image": IMAGES_UPDATED,
            "note": NOTES_UPDATED,
            "option": OPTIONS_UPDATED,
            "priority": PRIORITIES_UPDATED,
            "question": QUESTIONS_UPDATED,
            "rehearsal_run": REHEARSAL_RUNS_UPDATED,
            "rehearsal_run_item": REHEARSAL_RUN_ITEMS_UPDATED,
            "stack": STACKS_UPDATED,
            "subject": SUBJECTS_UPDATED,
            "tag": TAGS_UPDATED,
            "teacher": TEACHERS_UPDATED,
            "user": USERS_UPDATED,
        }[model_type.lower()]
    except KeyError as e:
        log_error(
            message=f"Caught a KeyError while attempting to get bulk update event for '{model_type}' model: {e}"
        )
        log_error(message=f"No bulk update event defined for '{model_type}' model")
        raise e


def _get_delete_event(model_type: str) -> str:
    """
    Retrieves the corresponding 'deleted' notification event string for a given model type.

    This function maps a lowercase model type identifier (e.g., 'flashcard', 'note')
    to the specific dispatcher notification event (e.g., FLASHCARD_DELETED, NOTE_DELETED)
    that should be broadcast after a successful single entry deletion operation.

    Args:
        model_type (str): The name of the data model type (e.g., 'flashcard', 'subject').
                          Case sensitivity is handled internally (converted to lowercase).

    Returns:
        str: The constant string identifier of the corresponding broadcast notification event.

    Raises:
        KeyError: If the provided 'model_type' is not defined in the internal mapping.
    """

    try:
        return {
            "answer": ANSWER_DELETED,
            "customfield": CUSTOMFIELD_DELETED,
            "difficulty": DIFFICULTY_DELETED,
            "flashcard": FLASHCARD_DELETED,
            "image": IMAGE_DELETED,
            "note": NOTE_DELETED,
            "option": OPTION_DELETED,
            "priority": PRIORITY_DELETED,
            "question": QUESTION_DELETED,
            "rehearsal_run": REHEARSAL_RUN_DELETED,
            "rehearsal_run_item": REHEARSAL_RUN_ITEM_DELETED,
            "stack": STACK_DELETED,
            "subject": SUBJECT_DELETED,
            "tag": TAG_DELETED,
            "teacher": TEACHER_DELETED,
            "user": USER_DELETED,
        }[model_type.lower()]
    except KeyError as e:
        log_error(
            message=f"Caught a KeyError while attempting to get delete event for '{model_type}' model: {e}"
        )
        log_error(message=f"No delete event defined for '{model_type}' model")
        raise e


def _get_delete_all_event(model_type: str) -> str:
    """
    Retrieves the corresponding 'all deleted' notification event string for a given model type.

    This function maps a lowercase model type identifier (e.g., 'flashcard', 'note')
    to the specific dispatcher notification event (e.g., ALL_FLASHCARDS_DELETED, ALL_NOTES_DELETED)
    that should be broadcast after a successful operation deleting all entries of that type.

    Args:
        model_type (str): The name of the data model type (e.g., 'flashcard', 'subject').
                          Case sensitivity is handled internally (converted to lowercase).

    Returns:
        str: The constant string identifier of the corresponding bulk broadcast notification event.

    Raises:
        KeyError: If the provided 'model_type' is not defined in the internal mapping.
    """

    try:
        return {
            "answer": ALL_ANSWERS_DELETED,
            "customfield": ALL_CUSTOMFIELDS_DELETED,
            "difficulty": ALL_DIFFICULTIES_DELETED,
            "flashcard": ALL_FLASHCARDS_DELETED,
            "image": ALL_IMAGES_DELETED,
            "note": ALL_NOTES_DELETED,
            "option": ALL_OPTIONS_DELETED,
            "priority": ALL_PRIORITIES_DELETED,
            "question": ALL_QUESTIONS_DELETED,
            "rehearsal_run": ALL_REHEARSAL_RUNS_DELETED,
            "rehearsal_run_item": ALL_REHEARSAL_RUN_ITEMS_DELETED,
            "stack": ALL_STACKS_DELETED,
            "subject": ALL_SUBJECTS_DELETED,
            "tag": ALL_TAGS_DELETED,
            "teacher": ALL_TEACHERS_DELETED,
            "user": ALL_USERS_DELETED,
        }[model_type.lower()]
    except KeyError as e:
        log_error(
            message=f"Caught a KeyError while attempting to get delete all event for '{model_type}' model: {e}"
        )
        log_error(message=f"No delete all event defined for '{model_type}' model")
        raise e


def _get_get_all_event(model_type: str) -> str:
    """
    Retrieves the corresponding 'all retrieved' notification event string for a given model type.

    This function maps a lowercase model type identifier (e.g., 'flashcard', 'note')
    to the specific dispatcher notification event (e.g., ALL_FLASHCARDS_RETRIEVED, ALL_NOTES_RETRIEVED)
    that should be broadcast after a successful batch entry retrieval operation.

    Args:
        model_type (str): The name of the data model type (e.g., 'flashcard', 'subject').
                          Case sensitivity is handled internally (converted to lowercase).

    Returns:
        str: The constant string identifier of the corresponding bulk broadcast notification event.

    Raises:
        KeyError: If the provided 'model_type' is not defined in the internal mapping.
    """

    try:
        return {
            "answer": ALL_ANSWERS_RETRIEVED,
            "customfield": ALL_CUSTOMFIELDS_RETRIEVED,
            "difficulty": ALL_DIFFICULTIES_RETRIEVED,
            "flashcard": ALL_FLASHCARDS_RETRIEVED,
            "image": ALL_IMAGES_RETRIEVED,
            "note": ALL_NOTES_RETRIEVED,
            "option": ALL_OPTIONS_RETRIEVED,
            "priority": ALL_PRIORITIES_RETRIEVED,
            "question": ALL_QUESTIONS_RETRIEVED,
            "rehearsal_run": ALL_REHEARSAL_RUNS_RETRIEVED,
            "rehearsal_run_item": ALL_REHEARSAL_RUN_ITEMS_RETRIEVED,
            "stack": ALL_STACKS_RETRIEVED,
            "subject": ALL_SUBJECTS_RETRIEVED,
            "tag": ALL_TAGS_RETRIEVED,
            "teacher": ALL_TEACHERS_RETRIEVED,
            "user": ALL_USERS_RETRIEVED,
        }[model_type.lower()]
    except KeyError as e:
        log_error(
            message=f"Caught a KeyError while attempting to get get all event for '{model_type}' model: {e}"
        )
        log_error(message=f"No get all event defined for '{model_type}' model")
        raise e


def _get_get_event(model_type: str) -> str:
    """
    Retrieves the corresponding 'retrieved' notification event string for a given model type.

    This function maps a lowercase model type identifier (e.g., 'flashcard', 'note')
    to the specific dispatcher notification event (e.g., FLASHCARD_RETRIEVED, NOTE_RETRIEVED)
    that should be broadcast after a successful single entry retrieval operation.

    Args:
        model_type (str): The name of the data model type (e.g., 'flashcard', 'subject').
                          Case sensitivity is handled internally (converted to lowercase).

    Returns:
        str: The constant string identifier of the corresponding broadcast notification event.

    Raises:
        KeyError: If the provided 'model_type' is not defined in the internal mapping.
    """

    try:
        return {
            "answer": ANSWER_RETRIEVED,
            "customfield": CUSTOMFIELD_RETRIEVED,
            "difficulty": DIFFICULTY_RETRIEVED,
            "flashcard": FLASHCARD_RETRIEVED,
            "image": IMAGE_RETRIEVED,
            "note": NOTE_RETRIEVED,
            "option": OPTION_RETRIEVED,
            "priority": PRIORITY_RETRIEVED,
            "question": QUESTION_RETRIEVED,
            "rehearsal_run": REHEARSAL_RUN_RETRIEVED,
            "rehearsal_run_item": REHEARSAL_RUN_ITEM_RETRIEVED,
            "stack": STACK_RETRIEVED,
            "subject": SUBJECT_RETRIEVED,
            "tag": TAG_RETRIEVED,
            "teacher": TEACHER_RETRIEVED,
            "user": USER_RETRIEVED,
        }[model_type.lower()]
    except KeyError as e:
        log_error(
            message=f"Caught a KeyError while attempting to get get event for '{model_type}' model: {e}"
        )
        log_error(message=f"No get event defined for '{model_type}' model")
        raise e


def _get_entry_unique_criteria(entry: dict[str, Any]) -> dict[str, Any]:
    """
    Extract all fields from the entry that are to be used for duplicate detection
    (everything except ‘metadata’).

    Args:
        entry (dict[str, Any]): The entry to be checked.

    Returns:
        dict[str, Any]: The fields that define uniqueness.
    """

    return {
        key: value
        for (
            key,
            value,
        ) in entry.items()
        if key != "metadata"
    }


def _get_update_event(model_type: str) -> str:
    """
    Retrieves the corresponding 'updated' notification event string for a given model type.

    This function maps a lowercase model type identifier (e.g., 'flashcard', 'note')
    to the specific dispatcher notification event (e.g., FLASHCARD_UPDATED, NOTE_UPDATED)
    that should be broadcast after a successful single entry update operation.

    Args:
        model_type (str): The name of the data model type (e.g., 'flashcard', 'subject').
                          Case sensitivity is handled internally (converted to lowercase).

    Returns:
        str: The constant string identifier of the corresponding broadcast notification event.

    Raises:
        KeyError: If the provided 'model_type' is not defined in the internal mapping.
    """

    try:
        return {
            "answer": ANSWER_UPDATED,
            "customfield": CUSTOMFIELD_UPDATED,
            "difficulty": DIFFICULTY_UPDATED,
            "flashcard": FLASHCARD_UPDATED,
            "image": IMAGE_UPDATED,
            "note": NOTE_UPDATED,
            "option": OPTION_UPDATED,
            "priority": PRIORITY_UPDATED,
            "question": QUESTION_UPDATED,
            "rehearsal_run": REHEARSAL_RUN_UPDATED,
            "rehearsal_run_item": REHEARSAL_RUN_ITEM_UPDATED,
            "stack": STACK_UPDATED,
            "subject": SUBJECT_UPDATED,
            "tag": TAG_UPDATED,
            "teacher": TEACHER_UPDATED,
            "user": USER_UPDATED,
        }[model_type.lower()]
    except KeyError as e:
        log_error(
            message=f"Caught a KeyError while attempting to get update event for '{model_type}' model: {e}"
        )
        log_error(message=f"No update event defined for '{model_type}' model")
        raise e


def _increment_table_counters(table_data: dict[str, Any]) -> None:
    """
    Increments the table's 'next_id' and 'total' counters.

    The 'next_id' is incremented to prepare for the subsequent entry addition,
    and 'total' reflects the current count of entries.

    Args:
        table_data (dict[str, Any]): The table data dictionary containing the
                                     'metadata' and 'entries' structures.

    Returns:
        None
    """

    table_data["metadata"]["next_id"] += 1
    table_data["entries"]["total"] += 1


def _insert_table_entry(entry_data: dict[str, Any], table_data: dict[str, Any]) -> None:
    """
    Assigns an ID and key to the entry and inserts it into the table's entries dictionary.

    The ID is derived from the table's current 'next_id' counter.

    Args:
        entry_data (dict[str, Any]): The entry dictionary to be inserted.
                                     The 'id' and 'key' fields are added/overwritten here.
        table_data (dict[str, Any]): The parent table data dictionary where the
                                     entry will be stored under the 'entries' key.

    Returns:
        None
    """

    entry_data["metadata"]["id"] = table_data["metadata"]["next_id"]
    entry_data["metadata"]["key"] = generate_model_key(
        id_=entry_data["metadata"]["id"],
        name=entry_data["metadata"]["type"],
    )

    table_data["entries"]["entries"][str(entry_data["metadata"]["id"])] = entry_data

    _update_metadata_field_list(
        entry=entry_data,
        table_data=table_data,
    )


def _save_table_data(table_data: dict[str, Any], table_name: str) -> None:
    """
    Saves the table data dictionary to the corresponding JSON file.

    This function wraps the file writing operation and includes error handling
    to dispatch a DB_OPERATION_FAILURE event if the file cannot be written.

    Args:
        table_data (dict[str, Any]): The complete table data dictionary to save.
        table_name (str): The name of the table/file (e.g., "flashcard.json").

    Returns:
        None

    Raises:
        Exception: If an error occurs during file writing.
    """

    try:
        file: Path = DATA_DIR / (
            f"{table_name}.json" if not table_name.endswith(".json") else table_name
        )

        write_file_json(
            data=table_data,
            file=file,
        )
    except Exception as e:
        log_error(
            message=f"Caught an exception while attempting to save '{table_name}' table data: {e}"
        )
        dispatch(
            event=DB_OPERATION_FAILURE,
            message=f"Caught an exception while attempting to save '{table_name}' table data: {e}",
        )
        raise e


def _update_metadata_field_list(table_data: dict[str, Any], entry: dict[str, Any]) -> None:
    """
    Updates the list of fields that have ever been stored in this table,
    located in the table's 'metadata' block.

    This is intended for future data validation and ORM preparation. It ensures
    that table_data['metadata']['fields']['fields'] contains a comprehensive,
    sorted list of all keys found in all entries added so far.

    Args:
        table_data (dict[str, Any]): The current table data dictionary.
        entry (dict[str, Any]): The new entry whose fields are to be added.

    Returns:
        None
    """

    if "metadata" not in table_data:
        table_data["metadata"] = {}

    if "fields" not in table_data["metadata"]:
        table_data["metadata"]["fields"] = {"fields": [], "total": 0}

    current_fields_set: set[str] = set(table_data["metadata"]["fields"]["fields"])

    new_fields: set[str] = set([key for key in entry.keys() if key != "metadata"])

    updated_fields_set: set[str] = current_fields_set.union(new_fields)

    updated_fields_list: list[str] = sorted(list(updated_fields_set))

    table_data["metadata"]["fields"]["fields"] = updated_fields_list
    table_data["metadata"]["fields"]["total"] = len(updated_fields_list)


def _update_table_timestamps(table_data: dict[str, Any]) -> None:
    """
    Updates the table's 'updated_at' (datetime) and 'updated_on' (date) timestamps
    to reflect the current time, indicating a modification to the table data.

    Args:
        table_data (dict[str, Any]): The table data dictionary to update.

    Returns:
        None
    """

    table_data["updated_at"] = get_now_str()
    table_data["updated_on"] = get_today_str()


# ---------- Functions ---------- #


def add_entry(
    entry: dict[str, Any],
    table_name: str,
) -> Optional[int]:
    """
    Adds an entry to the table.

    Args:
        entry (dict[str, Any]): The entry to add to the table.
        table_name (str): The name of the table to which to add the entry to.

    Returns:
        Optional[int]: The ID of the added entry.

    Raises:
        Exception: If the entry cannot be added.
    """

    try:
        _ensure_table_json(table_name=table_name)

        file: Path = DATA_DIR / (
            f"{table_name}.json" if not table_name.endswith(".json") else table_name
        )

        table_data: dict[str, Any] = read_file_json(file=file)

        _insert_table_entry(
            entry_data=entry,
            table_data=table_data,
        )
        _increment_table_counters(table_data=table_data)
        _update_table_timestamps(table_data=table_data)

        _save_table_data(
            table_data=table_data,
            table_name=table_name,
        )

        log_info(
            message=f"Successfully added entry '{entry["metadata"]["key"]}' to '{table_name}' table"
        )

        dispatch(
            event=_get_add_event(model_type=entry["metadata"]["type"]),
            **{
                entry["metadata"]["type"].lower(): entry,
            },
        )

        return entry["metadata"]["id"]
    except Exception as e:
        log_error(
            message=f"Caught an exception while attempting to add entry to '{table_name}' table: {e}"
        )
        raise e


def add_entry_if_not_exist(
    entry: dict[str, Any],
    table_name: str,
    force: bool = False,
) -> Optional[dict[str, Any]]:
    """
    Adds a single entry to the table only if no duplicate
    (based on all non-metadata fields) already exists.

    Args:
        entry (dict[str, Any]): The entry to be added.
        force (bool): Whether to force the addition of the entry even if a duplicate is found.
        table_name (str): The name of the table (e.g., ‘flashcards’).

    Returns:
        Optional[dict[str, Any]]: The added entry (with metadata) or None if a duplicate was found.

    Raises:
        Exception: If an exception is caught while adding the entry.
    """

    try:
        if force:
            return add_entry(
                entry=entry,
                table_name=table_name,
            )

        unique_criteria: dict[str, Any] = _get_entry_unique_criteria(entry=entry)

        existing_entries: list[dict[str, Any]] = filter_entries(
            table_name=table_name,
            **unique_criteria,
        )

        if exists(value=existing_entries):
            log_info(
                message=f"Skipping adding entry to '{table_name}' table: Duplicate found based on criteria: {unique_criteria}"
            )
            return None

        return add_entry(
            entry=entry,
            table_name=table_name,
        )
    except Exception as e:
        log_error(
            message=f"Caught an exception while attempting to add entry to '{table_name}' table: {e}"
        )
        raise e


def add_entries(
    entries: list[dict[str, Any]],
    table_name: str,
) -> Optional[list[int]]:
    """
    Adds multiple entries to the table in a single atomic operation.

    This function processes a batch of entries, assigns unique IDs and keys to each,
    updates the table metadata counters, and saves the changes back to the JSON file.

    Args:
        entries (list[dict[str, Any]]): A list of entry dictionaries to add to the table.
        table_name (str): The name of the table to which to add the entries.

    Returns:
        Optional[list[int]]: A list of IDs of the successfully added entries.

    Raises:
        Exception: If an exception is caught while processing or saving the entries.
    """

    try:
        if not exists(value=entries):
            log_info(message=f"Attempted to add 0 entries to '{table_name}' table. Aborting...")
            return []

        _ensure_table_json(table_name=table_name)

        file: Path = DATA_DIR / (
            f"{table_name}.json" if not table_name.endswith(".json") else table_name
        )

        table_data: dict[str, Any] = read_file_json(file=file)

        added_ids: list[int] = []
        model_type: str = ""

        for entry in entries:
            _insert_table_entry(
                entry_data=entry,
                table_data=table_data,
            )

            added_ids.append(entry["metadata"]["id"])

            _increment_table_counters(table_data=table_data)

            if not exists(value=model_type):
                model_type = entry["metadata"]["type"]

        _update_table_timestamps(table_data=table_data)

        _save_table_data(
            table_data=table_data,
            table_name=table_name,
        )

        log_info(
            message=f"Successfully added {len(entries)} entries to '{table_name}' table. IDs: {added_ids}"
        )

        if exists(value=model_type):
            dispatch(
                event=_get_bulk_add_event(model_type=model_type),
                **{
                    pluralize_word(word=model_type).lower(): entries,
                },
            )

        return added_ids
    except Exception as e:
        log_error(
            message=f"Caught an exception while attempting to add {len(entries)} entries to '{table_name}' table: {e}"
        )
        raise e


def add_entries_if_not_exist(
    entries: list[dict[str, Any]],
    table_name: str,
    force: bool = False,
) -> list[dict[str, Any]]:
    """
    Adds a list of entries to the table only if no duplicate
    (based on all non-metadata fields) for the respective entry
    already exists.

    Args:
        entries (list[dict[str, Any]]): The list of entries to be added.
        force (bool): Whether to force the addition of the entries even if a duplicate is found.
        table_name (str): The name of the table (e.g., ‘flashcards’).

    Returns:
        list[dict[str, Any]]: A list of all entries actually added (with metadata).

    Raises:
        Exception: If an exception is caught while processing or saving the entries.
    """

    try:
        if force:
            return add_entries(
                entries=entries,
                table_name=table_name,
            )

        entries_to_add: list[dict[str, Any]] = []

        for entry in entries:
            unique_criteria: dict[str, Any] = _get_entry_unique_criteria(entry=entry)

            existing_entries: list[dict[str, Any]] = filter_entries(
                table_name=table_name,
                **unique_criteria,
            )

            if exists(value=existing_entries):
                log_info(
                    message=f"Skipping adding entry to '{table_name}' table: Duplicate found based on criteria: {unique_criteria}"
                )
                continue

            entries_to_add.append(entry)

        if not exists(value=entries_to_add):
            return []

        return add_entries(
            entries=entries_to_add,
            table_name=table_name,
        )
    except Exception as e:
        log_error(
            message=f"Caught an exception while attempting to add entries to '{table_name}' table: {e}"
        )
        raise e


def count_entries(table_name: str) -> int:
    """
    Returns the total number of entries currently stored in the specified table.

    The function reads the table metadata to retrieve the 'total' counter
    without iterating over all entries.

    Args:
        table_name (str): The name of the table/collection to count entries for.

    Returns:
        int: The total number of entries in the table. Returns 0 if the table is empty.

    Raises:
        Exception: If an exception is caught while accessing or reading the table file.
    """

    try:
        _ensure_table_json(table_name=table_name)

        file: Path = DATA_DIR / (
            f"{table_name}.json" if not table_name.endswith(".json") else table_name
        )

        table_data: dict[str, Any] = read_file_json(file=file)

        count: int = table_data["entries"]["total"]

        log_info(message=f"Successfully retrieved total count ({count}) for '{table_name}' table")

        return count
    except Exception as e:
        log_error(
            message=f"Caught an exception while attempting to count entries in '{table_name}' table: {e}"
        )
        raise e


def delete_all_entries(table_name: str) -> bool:
    """
    Deletes all entries from a specified table by resetting the table file structure.

    This function effectively clears the table by calling _ensure_table_json_with_content,
    which initializes the file with the default empty structure (zero entries, reset metadata).
    A successful operation dispatches the 'ALL_..._DELETED' notification event.

    Args:
        table_name (str): The name of the table/collection to clear of all entries.

    Returns:
        bool: True if the table was successfully cleared, False otherwise.

    Raises:
        Exception: If an exception is caught during the file initialization or event dispatch.
    """

    try:
        _ensure_table_json(table_name=table_name)

        file: Path = DATA_DIR / (
            f"{table_name}.json" if not table_name.endswith(".json") else table_name
        )

        model_type: Optional[str] = None

        if does_file_have_content(file=file):
            try:
                table_data: dict[str, Any] = read_file_json(file=file)

                if not table_data["entries"]["total"] > 0:
                    return

                first_entry = next(iter(table_data["entries"]["entries"].values()), None)

                if not exists(value=first_entry):
                    return

                model_type = first_entry["metadata"]["type"]
            except Exception:
                pass

        _ensure_table_json_with_content(table_name=table_name)

        log_info(message=f"Successfully deleted all entries and reset table '{table_name}'.")

        if exists(value=model_type):
            dispatch(
                event=_get_delete_all_event(model_type=model_type),
                kwargs={},
            )

        return True
    except Exception as e:
        log_error(
            message=f"Caught an exception while attempting to delete all entries from '{table_name}' table: {e}"
        )
        raise e


def delete_entries(
    ids: list[Union[int, str]],
    table_name: str,
) -> bool:
    """
    Deletes multiple entries from a specified table based on a list of unique IDs in a single operation.

    The function reads the entire table file, attempts to remove all specified entries,
    updates the table metadata counters based on the count of successfully deleted entries,
    and saves the changes back to the JSON file. A bulk notification event is dispatched.

    Args:
        ids (list[Union[int, str]]): A list of unique IDs (primary keys) of the entries to delete.
        table_name (str): The name of the table/collection where the entries are stored.

    Returns:
        bool: True if at least one entry was successfully deleted, False otherwise.

    Raises:
        Exception: If an exception is caught while accessing, reading, or writing the table file.
    """

    try:
        if not exists(value=ids):
            log_info(
                message=f"Attempted to delete 0 entries from '{table_name}' table. Aborting..."
            )
            return False

        _ensure_table_json(table_name=table_name)

        entry_id_strs: list[str] = [str(i) for i in ids]

        file: Path = DATA_DIR / (
            f"{table_name}.json" if not table_name.endswith(".json") else table_name
        )

        table_data: dict[str, Any] = read_file_json(file=file)

        deleted_entries: list[dict[str, Any]] = []

        model_type: str = ""

        all_entries: dict[str, Any] = table_data["entries"]["entries"]

        for id_str in entry_id_strs:
            deleted_entry: Optional[dict[str, Any]] = all_entries.pop(id_str, None)

            if not exists(value=deleted_entry):
                continue

            deleted_entries.append(deleted_entry)

            if not exists(value=model_type):
                continue

            model_type = deleted_entry["metadata"]["type"]

        count_deleted: int = len(deleted_entries)

        if count_deleted == 0:
            log_info(
                message=f"Attempted to delete {len(ids)} entries from '{table_name}' table, but none were found."
            )
            return False

        for _ in range(count_deleted):
            _decrement_table_counters(table_data=table_data)
        _update_table_timestamps(table_data=table_data)

        _save_table_data(
            table_data=table_data,
            table_name=table_name,
        )

        log_info(
            message=f"Successfully deleted {count_deleted} entries from '{table_name}' table. IDs deleted: {[e['id'] for e in deleted_entries]}"
        )

        if exists(value=model_type):
            dispatch(
                event=_get_bulk_delete_event(model_type=model_type),
                **{
                    pluralize_word(word=model_type).lower(): deleted_entries,
                },
            )

        return True
    except Exception as e:
        log_error(
            message=f"Caught an exception while attempting to delete entries from '{table_name}' table: {e}"
        )
        raise e


def delete_entry(
    id_: Union[int, str],
    table_name: str,
) -> bool:
    """
    Deletes a single entry from a specified table by its unique ID.

    The function reads the entire table file, attempts to remove the entry
    corresponding to the given ID (stored as a string key), updates the table
    metadata, and saves the changes back to the JSON file if the deletion was successful.
    A successful deletion dispatches a notification event.

    Args:
        id_ (Union[int, str]): The unique ID (primary key) of the entry to delete.
        table_name (str): The name of the table/collection where the entry is stored.

    Returns:
        bool: True if the entry was successfully found and deleted, False otherwise.

    Raises:
        Exception: If an exception is caught while accessing, reading, or writing the table file.
    """

    try:
        _ensure_table_json(table_name=table_name)

        entry_id_str: str = str(id_)

        file: Path = DATA_DIR / (
            f"{table_name}.json" if not table_name.endswith(".json") else table_name
        )

        table_data: dict[str, Any] = read_file_json(file=file)

        deleted_entry: Optional[dict[str, Any]] = table_data["entries"]["entries"].pop(
            entry_id_str, None
        )

        if not exists(value=deleted_entry):
            log_info(
                message=f"Attempted to delete entry with ID '{entry_id_str}' from '{table_name}' table, but it was not found."
            )

            return False

        _decrement_table_counters(table_data=table_data)

        _update_table_timestamps(table_data=table_data)

        write_file_json(
            data=table_data,
            file=file,
        )

        log_info(message=f"Successfully deleted entry '{entry_id_str}' from '{table_name}' table")

        model_type: str = deleted_entry["metadata"]["type"]

        dispatch(
            event=_get_delete_event(model_type=model_type),
            **{
                model_type.lower(): deleted_entry,
            },
        )

        return True
    except Exception as e:
        log_error(
            message=f"Caught an exception while attempting to delete entry '{id_}' from '{table_name}' table: {e}"
        )
        raise e


def filter_entries(
    table_name: str,
    **kwargs: Any,
) -> Optional[list[dict[str, Any]]]:
    """
    Retrieves entries from a table that match specific criteria provided as keyword arguments.

    This function loads all entries from the specified table and filters them
    using a helper function that performs case-insensitive containment matching.
    It dispatches a single-entry or bulk-retrieved event based on the result count.

    Args:
        table_name (str): The name of the table/collection to filter.
        **kwargs: Arbitrary keyword arguments (key/value pairs) used as filtering criteria.
                  An entry must match ALL criteria to be included. Matching is case-insensitive.

    Returns:
        Optional[list[dict[str, Any]]]: A list of dictionary objects containing the matching entries,
                                        or None if the table file cannot be read. Returns an
                                        empty list if no entries match the criteria.

    Raises:
        Exception: If an exception is caught while accessing or reading the table file.
    """

    def _matches_filter(
        criteria: dict[str, Any],
        entry: dict[str, Any],
    ) -> bool:
        """
        Internal helper function to check if a single entry matches all filtering criteria.

        Performs a case-insensitive check for containment (the value in the entry
        must contain the string value provided in the criteria).

        Args:
            criteria (dict[str, Any]): The filtering criteria.
            entry (dict[str, Any]): The entry to check against the criteria.

        Returns:
            bool: True if the entry matches all criteria, False otherwise.
        """

        for (
            outer_key,
            outer_value,
        ) in criteria.items():
            if outer_key in ["table_name"]:
                continue

            if outer_key not in entry:
                return False

            entry_value = entry[outer_key]

            return str(entry_value).lower() == str(outer_value).lower()

    try:
        all_entries: Optional[list[dict[str, Any]]] = get_all_entries(table_name=table_name)

        if not exists(value=all_entries):
            return []

        filtered_entries = list(
            filter(
                lambda entry: _matches_filter(
                    criteria=kwargs,
                    entry=entry,
                ),
                all_entries,
            )
        )

        count: int = len(filtered_entries)

        if count == 0:
            log_info(
                message=f"No entries found in '{table_name}' table matching filter criteria: {kwargs}"
            )

            return []

        model_type: str = filtered_entries[0]["metadata"]["type"]

        log_info(
            message=f"Successfully filtered {count} entries from '{table_name}' table matching criteria: {kwargs}"
        )

        if count == 1:
            entry = filtered_entries[0]

            dispatch(
                event=_get_get_event(model_type=model_type),
                **{
                    pluralize_word(word=model_type).lower(): entry,
                },
            )
        elif count > 1:
            dispatch(
                event=_get_bulk_get_event(model_type=model_type),
                **{
                    pluralize_word(word=model_type).lower(): filtered_entries,
                },
            )

        return filtered_entries
    except Exception as e:
        log_error(
            message=f"Caught an exception while attempting to filter entries from '{table_name}' table with criteria {kwargs}: {e}"
        )
        raise e


def get_all_entries(table_name: str) -> Optional[list[dict[str, Any]]]:
    """
    Retrieves all entries contained within a specified table.

    The function reads the entire table file and returns all entries found in the
    'entries' dictionary structure as a list. A successful retrieval dispatches
    the 'ALL_..._RETRIEVED' notification event.

    Args:
        table_name (str): The name of the table/collection from which to retrieve all entries.

    Returns:
        Optional[list[dict[str, Any]]]: A list of all entry dictionaries from the table,
                                        or None if the table file cannot be read. Returns an
                                        empty list if the table contains no entries.

    Raises:
        Exception: If an exception is caught while accessing or reading the table file.
    """

    try:
        _ensure_table_json(table_name=table_name)

        file: Path = DATA_DIR / (
            f"{table_name}.json" if not table_name.endswith(".json") else table_name
        )

        table_data: dict[str, Any] = read_file_json(file=file)

        all_entries_dict: dict[str, Any] = table_data["entries"]["entries"]

        retrieved_entries: list[dict[str, Any]] = list(all_entries_dict.values())

        count: int = len(retrieved_entries)

        if count <= 0:
            log_info(message=f"Table '{table_name}' contains no entries. Returning empty list.")

            return []

        model_type: str = retrieved_entries[0]["metadata"]["type"]

        log_info(message=f"Successfully retrieved all {count} entries from '{table_name}' table")

        dispatch(
            event=_get_get_all_event(model_type=model_type),
            **{
                f"all_{pluralize_word(word=model_type).lower()}": retrieved_entries,
            },
        )

        return retrieved_entries
    except Exception as e:
        log_error(
            message=f"Caught an exception while attempting to get all entries from '{table_name}' table: {e}"
        )
        raise e


def get_entries(
    ids: list[Union[int, str]],
    table_name: str,
) -> Optional[list[dict[str, Any]]]:
    """
    Retrieves multiple entries from a specified table based on a list of unique IDs.

    The function reads the entire table file, filters for entries whose IDs match
    those in the provided list, and returns the resulting list of entry data.
    If entries are successfully retrieved, a bulk notification event is dispatched.

    Args:
        ids (list[Union[int, str]]): A list of unique IDs (primary keys) of the entries to retrieve.
        table_name (str): The name of the table/collection where the entries are stored.

    Returns:
        Optional[list[dict[str, Any]]]: A list of dictionary objects containing the entry data,
                                        or None if the table file cannot be read. Returns an
                                        empty list if no entries match the provided IDs.

    Raises:
        Exception: If an exception is caught while accessing or reading the table file.
    """

    try:
        if not exists(value=ids):
            log_info(
                message=f"Attempted to get 0 entries from '{table_name}' table. Returning empty list."
            )

            return []

        _ensure_table_json(table_name=table_name)

        entry_id_strs: list[str] = [str(id_) for id_ in ids]

        file: Path = DATA_DIR / (
            f"{table_name}.json" if not table_name.endswith(".json") else table_name
        )

        table_data: dict[str, Any] = read_file_json(file=file)

        retrieved_entries: list[dict[str, Any]] = []

        model_type: str = ""

        all_entries: dict[str, Any] = table_data["entries"]["entries"]

        for id_str in entry_id_strs:
            entry = all_entries.get(id_str)

            if not exists(value=entry):
                continue

            retrieved_entries.append(entry)

            if exists(value=model_type):

                continue

            model_type = entry["metadata"]["type"]

        count: int = len(retrieved_entries)

        if count <= 0:
            log_info(message=f"No entries found for the requested IDs in '{table_name}' table")

            return []

        log_info(
            message=f"Successfully retrieved {count} out of {len(ids)} requested entries from '{table_name}' table"
        )

        if exists(value=model_type):

            dispatch(
                event=_get_bulk_get_event(model_type=model_type),
                **{
                    pluralize_word(word=model_type).lower(): retrieved_entries,
                },
            )

        return retrieved_entries
    except Exception as e:
        log_error(
            message=f"Caught an exception while attempting to get entries from '{table_name}' table: {e}"
        )
        raise e


def get_entries_by_keys(
    keys: list[str],
    table_name: str,
) -> Optional[list[dict[str, Any]]]:
    """
    Retrieves multiple entries from a specified table based on a list of unique keys.

    The function reads the entire table file, filters for entries whose keys match
    those in the provided list, and returns the resulting list of entry data.
    If entries are successfully retrieved, a bulk notification event is dispatched.

    Args:
        keys (list[Union[int, str]]): A list of unique keys (primary keys) of the entries to retrieve.
        table_name (str): The name of the table/collection where the entries are stored.

    Returns:
        Optional[list[dict[str, Any]]]: A list of dictionary objects containing the entry data,
                                        or None if the table file cannot be read. Returns an
                                        empty list if no entries match the provided keys.

    Raises:
        Exception: If an exception is caught while accessing or reading the table file.
    """

    try:
        return get_entries(
            ids=[
                search_string(
                    pattern=PATTERNS["MODEL_KEY"],
                    string=key,
                )
                for key in keys
            ],
            table_name=table_name,
        )
    except Exception as e:
        log_error(
            message=f"Caught an exception while attempting to get entries by keys from '{table_name}' table: {e}"
        )
        raise e


def get_entry(
    id_: Union[int, str],
    table_name: str,
) -> Optional[dict[str, Any]]:
    """
    Retrieves a single entry from a specified table by its unique ID.

    The function reads the entire table file, searches for the entry corresponding
    to the given ID (stored as a string key), and returns the entry data if found.
    A successful retrieval dispatches a notification event.

    Args:
        id_ (Union[int, str]): The unique ID (primary key) of the entry to retrieve.
        table_name (str): The name of the table/collection where the entry is stored.

    Returns:
        Optional[dict[str, Any]]: The dictionary containing the entry data, or None if the entry is not found.

    Raises:
        Exception: If an exception is caught while accessing or reading the table file.
    """

    try:
        _ensure_table_json(table_name=table_name)

        entry_id_str: str = str(id_)

        file: Path = DATA_DIR / (
            f"{table_name}.json" if not table_name.endswith(".json") else table_name
        )

        table_data: dict[str, Any] = read_file_json(file=file)

        entry: Optional[dict[str, Any]] = table_data["entries"]["entries"].get(entry_id_str)

        if not exists(value=entry):
            log_info(message=f"Entry with ID '{entry_id_str}' not found in '{table_name}' table")

            return None

        log_info(message=f"Successfully retrieved entry '{entry_id_str}' from '{table_name}' table")

        model_type: str = entry["metadata"]["type"]

        dispatch(
            event=_get_get_event(model_type=model_type),
            **{
                model_type.lower(): entry,
            },
        )

        return entry
    except Exception as e:
        log_error(
            message=f"Caught an exception while attempting to get entry '{id_}' from '{table_name}' table: {e}"
        )
        raise e


def get_entry_by_key(
    key: str,
    table_name: str,
) -> Optional[dict[str, Any]]:
    """
    Retrieves a single entry from a specified table by its unique key.

    The function reads the entire table file, searches for the entry corresponding
    to the given key (stored as a string key), and returns the entry data if found.
    A successful retrieval dispatches a notification event.

    Args:
        key (str): The unique key of the entry to retrieve.
        table_name (str): The name of the table/collection where the entry is stored.

    Returns:
        Optional[dict[str, Any]]: The dictionary containing the entry data, or None if the entry is not found.

    Raises:
        Exception: If an exception is caught while accessing or reading the table file.
    """

    try:
        return get_entry(
            id_=search_string(
                pattern=PATTERNS["MODEL_ID"],
                string=key,
            ),
            table_name=table_name,
        )
    except Exception as e:
        log_error(
            message=f"Caught an exception while attempting to get entry '{key}' from '{table_name}' table: {e}"
        )
        raise e


def update_entry(
    entry: dict[str, Any],
    table_name: str,
) -> Optional[dict[str, Any]]:
    """
    Updates an existing entry in the specified table.

    The function reads the entire table file, validates that the entry ID exists,
    overwrites the old entry data with the provided updated 'entry' dictionary,
    updates the table metadata timestamp, and saves the changes back to the JSON file.
    A successful update dispatches a notification event.

    Args:
        entry (dict[str, Any]): The complete dictionary of the updated entry data.
                                This dictionary MUST contain the 'id' field.
        table_name (str): The name of the table/collection where the entry is stored.

    Returns:
        Optional[dict[str, Any]]: The updated entry dictionary, or None if the entry ID was not found in the table.

    Raises:
        ValueError: If the 'entry' dictionary is missing the required 'id' key.
        Exception: If an exception is caught while accessing, reading, or writing the table file.
    """

    try:
        if "id" not in entry["metadata"]:
            raise ValueError(
                "The provided entry dictionary must contain an 'id' key for update operations."
            )

        _ensure_table_json(table_name=table_name)

        entry_id_str: str = str(entry["metadata"]["id"])

        file: Path = DATA_DIR / (
            f"{table_name}.json" if not table_name.endswith(".json") else table_name
        )

        table_data: dict[str, Any] = read_file_json(file=file)

        all_entries: dict[str, Any] = table_data["entries"]["entries"]

        if entry_id_str not in all_entries:
            log_info(
                message=f"Attempted to update entry with ID '{entry_id_str}' in '{table_name}' table, but it was not found."
            )
            return None

        all_entries[entry_id_str] = entry

        _update_metadata_field_list(
            entry=entry,
            table_data=table_data,
        )

        _update_table_timestamps(table_data=table_data)

        _save_table_data(
            table_data=table_data,
            table_name=table_name,
        )

        log_info(message=f"Successfully updated entry '{entry_id_str}' in '{table_name}' table")

        model_type: str = entry["metadata"]["type"]

        dispatch(
            event=_get_update_event(model_type=model_type),
            **{
                model_type.lower(): entry,
            },
        )

        return entry
    except Exception as e:
        log_error(
            message=f"Caught an exception while attempting to update entry '{entry.get('id', 'N/A')}' in '{table_name}' table: {e}"
        )
        raise e


def update_entries(
    entries: list[dict[str, Any]],
    table_name: str,
) -> Optional[list[dict[str, Any]]]:
    """
    Updates multiple existing entries in the specified table in a single atomic operation.

    The function reads the entire table file, validates that all entry IDs exist,
    overwrites the old entry data with the provided updated 'entry' dictionaries,
    updates the table metadata timestamp, and saves the changes back to the JSON file.
    A successful batch update dispatches a bulk notification event.

    Args:
        entries (list[dict[str, Any]]): A list of complete dictionaries of the updated entry data.
                                        Each dictionary MUST contain the 'id' field.
        table_name (str): The name of the table/collection where the entries are stored.

    Returns:
        Optional[list[dict[str, Any]]]: A list of the successfully updated entry dictionaries.
                                        Returns an empty list if no valid entries were provided or found.

    Raises:
        ValueError: If any entry dictionary in the list is missing the required 'id' key.
        Exception: If an exception is caught while accessing, reading, or writing the table file.
    """

    try:
        if not entries:
            log_info(message=f"Attempted to update 0 entries in '{table_name}' table. Aborting...")
            return []

        _ensure_table_json(table_name=table_name)

        file: Path = DATA_DIR / (
            f"{table_name}.json" if not table_name.endswith(".json") else table_name
        )

        table_data: dict[str, Any] = read_file_json(file=file)

        all_entries: dict[str, Any] = table_data["entries"]["entries"]

        updated_entries: list[dict[str, Any]] = []

        model_type: str = ""

        for entry in entries:
            if "id" not in entry["metadata"]:
                raise ValueError(
                    "An entry dictionary in the batch update list must contain an 'id' key."
                )

            entry_id_str: str = str(entry["metadata"]["id"])

            if entry_id_str not in all_entries:
                log_info(
                    message=f"Entry with ID '{entry_id_str}' skipped during batch update for '{table_name}' table, as it was not found."
                )
                continue

            all_entries[entry_id_str] = entry

            updated_entries.append(entry)

            _update_metadata_field_list(
                entry=entry,
                table_data=table_data,
            )

            if exists(value=model_type):
                continue

            model_type = entry["metadata"]["type"]

        count_updated: int = len(updated_entries)

        if count_updated == 0:
            log_info(message=f"No existing entries were updated in '{table_name}' table.")

            return []

        _update_table_timestamps(table_data=table_data)

        _save_table_data(
            table_data=table_data,
            table_name=table_name,
        )

        log_info(message=f"Successfully updated {count_updated} entries in '{table_name}' table.")

        if exists(value=model_type):
            dispatch(
                event=_get_bulk_update_event(model_type=model_type),
                **{
                    pluralize_word(word=model_type).lower(): updated_entries,
                },
            )

        return updated_entries
    except Exception as e:
        log_error(
            message=f"Caught an exception while attempting to update batch entries in '{table_name}' table: {e}"
        )
        raise e
