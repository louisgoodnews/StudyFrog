"""
Author: Louis Goodnews
Date: 2025-12-12
Description: The logic of the rehearsal run view of the application.
"""

from typing import Any, Final, Literal, Optional

from constants.common import GLOBAL, PATTERNS
from constants.events import (
    CLICKED_EASY_BUTTON,
    CLICKED_EDIT_BUTTON,
    CLICKED_HARD_BUTTON,
    CLICKED_MEDIUM_BUTTON,
    CLICKED_NEXT_BUTTON,
    CLICKED_PREVIOUS_BUTTON,
    FILTER_DIFFICULTIES_FROM_DB,
    GET_DASHBOARD_VIEW,
    GET_FLASHCARD_FROM_DB,
    GET_NOTE_FROM_DB,
    GET_QUESTION_FROM_DB,
    GET_REHEARSAL_RUN_RESULT_VIEW,
    GET_STACK_FROM_DB,
    LOAD_REHEARSAL_VIEW_FORM,
    REHEARSAL_RUN_INDEX_DECREMENTED,
    REHEARSAL_RUN_INDEX_INCREMENTED,
    REHEARSAL_RUN_INDEX_MAX_REACHED,
    REHEARSAL_RUN_INDEX_MIN_REACHED,
    UPDATE_FLASHCARD_IN_DB,
    UPDATE_NOTE_IN_DB,
    UPDATE_QUESTION_IN_DB,
    UPDATE_REHEARSAL_RUN_IN_DB,
)
from models.models import ModelDict
from utils.common import (
    exists,
    get_now,
    model_key_to_model_type,
    pluralize_word,
    search_string,
    shuffle_list,
)
from utils.dispatcher import dispatch
from utils.logging import log_debug, log_info, log_warning


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "end_rehearsal_run",
    "on_cancel_button_click",
    "on_easy_button_click",
    "on_edit_button_click",
    "on_hard_button_click",
    "on_medium_button_click",
    "on_next_button_click",
    "on_previous_button_click",
    "start_rehearsal_run",
]


# ---------- Constants ---------- #

CURRENT_INDEX: int = 0

STACK_ITEM_KEYS: Final[list[str]] = []


# ---------- Private Functions ---------- #


def _add_to_stack_items(key: str) -> None:
    """
    Adds a passed key to the stack items keys list.

    Args:
        key (str): The key to add to the stack items keys list.

    Returns:
        None
    """

    if key in STACK_ITEM_KEYS:
        log_warning(message=f"Key {key} already contained in stack item keys list. Aborting...")
        return

    STACK_ITEM_KEYS.append(key)

    log_info(message=f"Added key {key} to stack item keys list.")


def _filter_stack_items_by_difficulty(difficulty_key: str) -> None:
    """
    Filters the stack items keys list by the passed difficulty.

    Args:
        difficulty_key (str): The key of the difficulty to filter the items by.

    Returns:
        None
    """

    model_type_to_event: dict[
        Literal[
            "flashcard",
            "note",
            "question",
        ],
        str,
    ] = {
        "flashcard": GET_FLASHCARD_FROM_DB,
        "note": GET_NOTE_FROM_DB,
        "question": GET_QUESTION_FROM_DB,
    }

    for item_key in STACK_ITEM_KEYS:
        model_type: Literal[
            "flashcard",
            "note",
            "question",
        ] = model_key_to_model_type(model_key=item_key)

        response: Optional[ModelDict] = (
            dispatch(
                event=model_type_to_event[model_type],
                id_=search_string(
                    pattern=PATTERNS["MODEL_ID"],
                    string=item_key,
                ),
                namespace=GLOBAL,
                table_name=pluralize_word(word=model_type),
            )
            .get(
                "get_entry",
                [{}],
            )[0]
            .get(
                "result",
                {},
            )
        )

        if not exists(value=response):
            log_warning(
                message=f"Failed to retrieve {model_type} with ID {search_string(pattern=PATTERNS['MODEL_ID'], string=item_key)}"
            )
            continue

        if response["difficulty"] != difficulty_key:
            _remove_from_stack_item_keys(key=item_key)


def _filter_stack_items_by_priority(priority_key: str) -> None:
    """
    Filters the stack items keys list by the passed priority.

    Args:
        priority_key (str): The key of the priority to filter the items by.

    Returns:
        None
    """

    model_type_to_event: dict[
        Literal[
            "flashcard",
            "note",
            "question",
        ],
        str,
    ] = {
        "flashcard": GET_FLASHCARD_FROM_DB,
        "note": GET_NOTE_FROM_DB,
        "question": GET_QUESTION_FROM_DB,
    }

    for item_key in STACK_ITEM_KEYS:
        model_type: Literal[
            "flashcard",
            "note",
            "question",
        ] = model_key_to_model_type(model_key=item_key)

        response: Optional[ModelDict] = (
            dispatch(
                event=model_type_to_event[model_type],
                id_=search_string(
                    pattern=PATTERNS["MODEL_ID"],
                    string=item_key,
                ),
                namespace=GLOBAL,
                table_name=pluralize_word(word=model_type),
            )
            .get(
                "get_entry",
                [{}],
            )[0]
            .get(
                "result",
                {},
            )
        )

        if not exists(value=response):
            log_warning(
                message=f"Failed to retrieve {model_type} with ID {search_string(pattern=PATTERNS['MODEL_ID'], string=item_key)}"
            )
            continue

        if response["priority"] != priority_key:
            _remove_from_stack_item_keys(key=item_key)


def _get_stack_items(key: str) -> list[str]:
    """
    Retrieves the keys of the stack items from the database.

    Args:
        key (str): The key of the stack to retrieve the items from.

    Returns:
        list[str]: The keys of the stack items.
    """

    response: Optional[dict[str, Any]] = (
        dispatch(
            event=GET_STACK_FROM_DB,
            id_=search_string(
                pattern=PATTERNS["MODEL_ID"],
                string=key,
            ),
            namespace=GLOBAL,
            table_name="stacks",
        )
        .get(
            "get_entry",
            [{}],
        )[0]
        .get(
            "result",
            {},
        )
    )

    if not exists(value=response):
        log_warning(
            message=f"Failed to retrieve stack with ID {search_string(pattern=PATTERNS['MODEL_ID'], string=key)}"
        )

        return []

    return response.get("items", [])


def _load_stack_item_from_db(stack_item_key: str) -> ModelDict:
    """
    Loads the stack item corresponding to the passed stack item key from the database.

    Args:
        stack_item_key (str): The key to load the stack item from.

    Returns:
        ModelDict: The stack item.
    """

    model_type: Optional[str] = model_key_to_model_type(model_key=stack_item_key)

    if not exists(value=model_type):
        log_warning(message=f"Failed to retrieve model type from stack item key {stack_item_key}")

        return {}

    model_type = model_type.lower()

    model_type_to_get_event: dict[
        Literal[
            "flashcard",
            "note",
            "question",
        ],
        str,
    ] = {
        "flashcard": GET_FLASHCARD_FROM_DB,
        "note": GET_NOTE_FROM_DB,
        "question": GET_QUESTION_FROM_DB,
    }

    model_id: Optional[str] = search_string(
        pattern=PATTERNS["MODEL_ID"],
        string=stack_item_key,
    )

    if not exists(value=model_id):
        log_warning(message=f"Failed to retrieve model ID from stack item key {stack_item_key}")

        return {}

    model_id = model_id.lower()

    return (
        dispatch(
            event=model_type_to_get_event[model_type],
            id_=model_id,
            namespace=GLOBAL,
            table_name=pluralize_word(word=model_type),
        )
        .get(
            "get_entry",
            [{}],
        )[0]
        .get(
            "result",
            {},
        )
    )


def _remove_from_stack_item_keys(key: str) -> None:
    """
    Removes a passed key from the stack item keys list.

    Args:
        key (str): The key to remove from the stack item keys list.

    Returns:
        None
    """

    if key not in STACK_ITEM_KEYS:
        log_warning(message=f"Key {key} not found in stack item keys list. Aborting...")
        return

    STACK_ITEM_KEYS.remove(key)

    log_info(message=f"Removed key {key} from stack item keys list.")


# ---------- Public Functions ---------- #


def end_rehearsal_run(rehearsal_run: ModelDict) -> None:
    """
    Handles the end of the rehearsal run.

    Args:
        rehearsal_run (ModelDict): The rehearsal run to end.

    Returns:
        None
    """

    rehearsal_run["end"] = get_now()

    rehearsal_run["duration"] = {
        "minutes": (rehearsal_run["end"] - rehearsal_run["start"]).total_seconds() // 60,
        "seconds": (rehearsal_run["end"] - rehearsal_run["start"]).total_seconds(),
    }

    rehearsal_run["end"] = rehearsal_run["end"].isoformat()

    rehearsal_run["start"] = rehearsal_run["start"].isoformat()

    dispatch(
        entry=rehearsal_run,
        event=UPDATE_REHEARSAL_RUN_IN_DB,
        namespace=GLOBAL,
        table_name="rehearsal_runs",
    )

    log_debug(message=f"Ending rehearsal run: {rehearsal_run}")

    dispatch(
        event=GET_REHEARSAL_RUN_RESULT_VIEW,
        namespace=GLOBAL,
        rehearsal_run=rehearsal_run,
    )


def on_cancel_button_click() -> None:
    """
    Handles the 'cancel' button click.

    Args:
        None

    Returns:
        None
    """

    dispatch(
        event=GET_DASHBOARD_VIEW,
        namespace=GLOBAL,
    )


def on_easy_button_click() -> None:
    """
    Handles the 'easy' button click.

    Args:
        None

    Returns:
        None
    """

    difficulty: ModelDict = (
        dispatch(
            event=FILTER_DIFFICULTIES_FROM_DB,
            name="easy",
            namespace=GLOBAL,
            table_name="difficulties",
        )
        .get(
            "filter_entries",
            [{}],
        )[0]
        .get(
            "result",
            [{}],
        )[0]
    )

    model_type_to_get_event: dict[
        Literal[
            "flashcard",
            "note",
            "question",
        ],
        str,
    ] = {
        "flashcard": GET_FLASHCARD_FROM_DB,
        "note": GET_NOTE_FROM_DB,
        "question": GET_QUESTION_FROM_DB,
    }

    model_id: Optional[str] = search_string(
        pattern=PATTERNS["MODEL_ID"],
        string=STACK_ITEM_KEYS[CURRENT_INDEX],
    )

    if not exists(value=model_id):
        log_warning(
            message=f"Failed to retrieve model ID from stack item key {STACK_ITEM_KEYS[CURRENT_INDEX]}"
        )

        return

    model_id = model_id.lower()

    model_type: Optional[str] = model_key_to_model_type(model_key=STACK_ITEM_KEYS[CURRENT_INDEX])

    if not exists(value=model_type):
        log_warning(
            message=f"Failed to retrieve model type from stack item key {STACK_ITEM_KEYS[CURRENT_INDEX]}"
        )

        return

    model_type = model_type.lower()

    model_dict: ModelDict = (
        dispatch(
            event=model_type_to_get_event[model_type],
            id_=model_id,
            namespace=GLOBAL,
            table_name=pluralize_word(word=model_type),
        )
        .get(
            "get_entry",
            [{}],
        )[0]
        .get(
            "result",
            {},
        )
    )

    model_type_to_update_event: dict[
        Literal[
            "flashcard",
            "note",
            "question",
        ],
        str,
    ] = {
        "flashcard": UPDATE_FLASHCARD_IN_DB,
        "note": UPDATE_NOTE_IN_DB,
        "question": UPDATE_QUESTION_IN_DB,
    }

    model_dict["difficulty"] = difficulty["metadata"]["key"]

    dispatch(
        entry=model_dict,
        event=model_type_to_update_event[model_type],
        namespace=GLOBAL,
        table_name=pluralize_word(word=model_type),
    )

    dispatch(
        event=CLICKED_EASY_BUTTON,
        namespace=GLOBAL,
    )


def on_edit_button_click() -> None:
    """
    Handles the 'edit' button click.

    Args:
        None

    Returns:
        None
    """

    dispatch(
        event=CLICKED_EDIT_BUTTON,
        namespace=GLOBAL,
    )


def on_hard_button_click() -> None:
    """
    Handles the 'hard' button click.

    Args:
        None

    Returns:
        None
    """

    difficulty: ModelDict = (
        dispatch(
            event=FILTER_DIFFICULTIES_FROM_DB,
            name="hard",
            namespace=GLOBAL,
            table_name="difficulties",
        )
        .get(
            "filter_entries",
            [{}],
        )[0]
        .get(
            "result",
            [{}],
        )[0]
    )

    model_type_to_get_event: dict[
        Literal[
            "flashcard",
            "note",
            "question",
        ],
        str,
    ] = {
        "flashcard": GET_FLASHCARD_FROM_DB,
        "note": GET_NOTE_FROM_DB,
        "question": GET_QUESTION_FROM_DB,
    }

    model_id: Optional[str] = search_string(
        pattern=PATTERNS["MODEL_ID"],
        string=STACK_ITEM_KEYS[CURRENT_INDEX],
    )

    if not exists(value=model_id):
        log_warning(
            message=f"Failed to retrieve model ID from stack item key {STACK_ITEM_KEYS[CURRENT_INDEX]}"
        )

        return

    model_id = model_id.lower()

    model_type: Optional[str] = model_key_to_model_type(model_key=STACK_ITEM_KEYS[CURRENT_INDEX])

    if not exists(value=model_type):
        log_warning(
            message=f"Failed to retrieve model type from stack item key {STACK_ITEM_KEYS[CURRENT_INDEX]}"
        )

        return

    model_type = model_type.lower()

    model_dict: ModelDict = (
        dispatch(
            event=model_type_to_get_event[model_type],
            id_=model_id,
            namespace=GLOBAL,
            table_name=pluralize_word(word=model_type),
        )
        .get(
            "get_entry",
            [{}],
        )[0]
        .get(
            "result",
            {},
        )
    )

    model_type_to_update_event: dict[
        Literal[
            "flashcard",
            "note",
            "question",
        ],
        str,
    ] = {
        "flashcard": UPDATE_FLASHCARD_IN_DB,
        "note": UPDATE_NOTE_IN_DB,
        "question": UPDATE_QUESTION_IN_DB,
    }

    model_dict["difficulty"] = difficulty["metadata"]["key"]

    dispatch(
        entry=model_dict,
        event=model_type_to_update_event[model_type],
        namespace=GLOBAL,
        table_name=pluralize_word(word=model_type),
    )

    dispatch(
        event=CLICKED_HARD_BUTTON,
        namespace=GLOBAL,
    )


def on_medium_button_click() -> None:
    """
    Handles the 'medium' button click.

    Args:
        None

    Returns:
        None
    """

    difficulty: ModelDict = (
        dispatch(
            event=FILTER_DIFFICULTIES_FROM_DB,
            name="medium",
            namespace=GLOBAL,
            table_name="difficulties",
        )
        .get(
            "filter_entries",
            [{}],
        )[0]
        .get(
            "result",
            [{}],
        )[0]
    )

    model_type_to_get_event: dict[
        Literal[
            "flashcard",
            "note",
            "question",
        ],
        str,
    ] = {
        "flashcard": GET_FLASHCARD_FROM_DB,
        "note": GET_NOTE_FROM_DB,
        "question": GET_QUESTION_FROM_DB,
    }

    model_id: Optional[str] = search_string(
        pattern=PATTERNS["MODEL_ID"],
        string=STACK_ITEM_KEYS[CURRENT_INDEX],
    )

    if not exists(value=model_id):
        log_warning(
            message=f"Failed to retrieve model ID from stack item key {STACK_ITEM_KEYS[CURRENT_INDEX]}"
        )

        return

    model_id = model_id.lower()

    model_type: Optional[str] = model_key_to_model_type(model_key=STACK_ITEM_KEYS[CURRENT_INDEX])

    if not exists(value=model_type):
        log_warning(
            message=f"Failed to retrieve model type from stack item key {STACK_ITEM_KEYS[CURRENT_INDEX]}"
        )

        return

    model_type = model_type.lower()

    model_dict: ModelDict = (
        dispatch(
            event=model_type_to_get_event[model_type],
            id_=model_id,
            namespace=GLOBAL,
            table_name=pluralize_word(word=model_type),
        )
        .get(
            "get_entry",
            [{}],
        )[0]
        .get(
            "result",
            {},
        )
    )

    model_type_to_update_event: dict[
        Literal[
            "flashcard",
            "note",
            "question",
        ],
        str,
    ] = {
        "flashcard": UPDATE_FLASHCARD_IN_DB,
        "note": UPDATE_NOTE_IN_DB,
        "question": UPDATE_QUESTION_IN_DB,
    }

    model_dict["difficulty"] = difficulty["metadata"]["key"]

    dispatch(
        entry=model_dict,
        event=model_type_to_update_event[model_type],
        namespace=GLOBAL,
        table_name=pluralize_word(word=model_type),
    )

    dispatch(
        event=CLICKED_MEDIUM_BUTTON,
        namespace=GLOBAL,
    )


def on_next_button_click() -> None:
    """
    Handles the 'next' button click.

    Args:
        None

    Returns:
        None
    """

    global CURRENT_INDEX

    if CURRENT_INDEX == len(STACK_ITEM_KEYS) - 1:
        log_warning(
            message=f"Current index {CURRENT_INDEX} is equal to the last index {len(STACK_ITEM_KEYS) - 1}. Aborting..."
        )

        dispatch(
            event=REHEARSAL_RUN_INDEX_MAX_REACHED,
            namespace=GLOBAL,
        )

        return

    CURRENT_INDEX += 1

    model_type_to_event: dict[
        Literal[
            "flashcard",
            "note",
            "question",
        ],
        str,
    ] = {
        "flashcard": GET_FLASHCARD_FROM_DB,
        "note": GET_NOTE_FROM_DB,
        "question": GET_QUESTION_FROM_DB,
    }

    model_id: Optional[str] = search_string(
        pattern=PATTERNS["MODEL_ID"],
        string=STACK_ITEM_KEYS[CURRENT_INDEX],
    )

    if not exists(value=model_id):
        log_warning(
            message=f"Failed to retrieve model ID from stack item key {STACK_ITEM_KEYS[CURRENT_INDEX]}"
        )

        return

    model_id = model_id.lower()

    model_type: Optional[str] = model_key_to_model_type(model_key=STACK_ITEM_KEYS[CURRENT_INDEX])

    if not exists(value=model_type):
        log_warning(
            message=f"Failed to retrieve model type from stack item key {STACK_ITEM_KEYS[CURRENT_INDEX]}"
        )

        return

    model_type = model_type.lower()

    model_dict: ModelDict = (
        dispatch(
            event=model_type_to_event[model_type],
            id_=model_id,
            namespace=GLOBAL,
            table_name=pluralize_word(word=model_type),
        )
        .get(
            "get_entry",
            [{}],
        )[0]
        .get(
            "result",
            {},
        )
    )

    dispatch(
        event=CLICKED_NEXT_BUTTON,
        namespace=GLOBAL,
        **{
            model_type.lower(): model_dict,
        },
    )

    dispatch(
        event=REHEARSAL_RUN_INDEX_INCREMENTED,
        namespace=GLOBAL,
    )

    dispatch(
        _load_stack_item_from_db(stack_item_key=STACK_ITEM_KEYS[CURRENT_INDEX]),
        event=LOAD_REHEARSAL_VIEW_FORM,
        namespace=GLOBAL,
    )


def on_previous_button_click() -> None:
    """
    Handles the 'previous' button click.

    Args:
        None

    Returns:
        None
    """

    global CURRENT_INDEX

    if CURRENT_INDEX == -1:
        log_warning(message=f"Current index {CURRENT_INDEX} is equal to -1. Aborting...")

        CURRENT_INDEX = 0

        dispatch(
            event=REHEARSAL_RUN_INDEX_MIN_REACHED,
            namespace=GLOBAL,
        )

        return

    CURRENT_INDEX -= 1

    model_type_to_event: dict[
        Literal[
            "flashcard",
            "note",
            "question",
        ],
        str,
    ] = {
        "flashcard": GET_FLASHCARD_FROM_DB,
        "note": GET_NOTE_FROM_DB,
        "question": GET_QUESTION_FROM_DB,
    }

    model_id: Optional[str] = search_string(
        pattern=PATTERNS["MODEL_ID"],
        string=STACK_ITEM_KEYS[CURRENT_INDEX],
    )

    if not exists(value=model_id):
        log_warning(
            message=f"Failed to retrieve model ID from stack item key {STACK_ITEM_KEYS[CURRENT_INDEX]}"
        )

        return

    model_id = model_id.lower()

    model_type: Optional[str] = model_key_to_model_type(model_key=STACK_ITEM_KEYS[CURRENT_INDEX])

    if not exists(value=model_type):
        log_warning(
            message=f"Failed to retrieve model type from stack item key {STACK_ITEM_KEYS[CURRENT_INDEX]}"
        )

        return

    model_type = model_type.lower()

    model_dict: ModelDict = (
        dispatch(
            event=model_type_to_event[model_type],
            id_=model_id,
            namespace=GLOBAL,
            table_name=pluralize_word(word=model_type),
        )
        .get(
            "get_entry",
            [{}],
        )[0]
        .get(
            "result",
            {},
        )
    )

    dispatch(
        event=CLICKED_PREVIOUS_BUTTON,
        namespace=GLOBAL,
        **{
            model_type: model_dict,
        },
    )

    dispatch(
        event=REHEARSAL_RUN_INDEX_DECREMENTED,
        namespace=GLOBAL,
    )

    dispatch(
        _load_stack_item_from_db(stack_item_key=STACK_ITEM_KEYS[CURRENT_INDEX]),
        event=LOAD_REHEARSAL_VIEW_FORM,
        namespace=GLOBAL,
    )


def start_rehearsal_run(rehearsal_run: ModelDict) -> None:
    """
    Handles the start of the rehearsal run.

    Args:
        rehearsal_run (ModelDict): The rehearsal run to start.

    Returns:
        None
    """

    rehearsal_run["start"] = get_now()

    for stack in rehearsal_run["stacks"]:
        for key in _get_stack_items(key=stack):
            _add_to_stack_items(key=key)

    if exists(value=rehearsal_run["configuration"]["filter_by_difficulty_enabled"]):
        _filter_stack_items_by_difficulty(
            difficulty_key=rehearsal_run["configuration"]["difficulty"]
        )

    if exists(value=rehearsal_run["configuration"]["filter_by_priority_enabled"]):
        _filter_stack_items_by_priority(priority_key=rehearsal_run["configuration"]["priority"])

    if exists(value=rehearsal_run["configuration"]["item_order_randomization_enabled"]):
        shuffle_list(list_=STACK_ITEM_KEYS)

    dispatch(
        _load_stack_item_from_db(stack_item_key=STACK_ITEM_KEYS[CURRENT_INDEX]),
        event=LOAD_REHEARSAL_VIEW_FORM,
        namespace=GLOBAL,
    )
