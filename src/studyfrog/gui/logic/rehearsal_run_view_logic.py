"""
Author: Louis Goodnews
Date: 2025-12-12
Description: The logic of the rehearsal run view of the application.
"""

from __future__ import annotations

from typing import Final, Literal, Optional

from studyfrog.constants.common import PATTERNS
from studyfrog.constants.events import (
    ADD_REHEARSAL_RUN_ITEM_TO_DB,
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
    GET_REHEARSAL_RUN_ITEM_FROM_DB,
    GET_REHEARSAL_RUN_ITEM_MODEL,
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
from studyfrog.constants.namespaces import GLOBAL_NAMESPACE
from studyfrog.models.models import Model
from studyfrog.utils.common import (
    exists,
    get_now,
    get_today,
    model_key_to_model_type,
    pluralize_word,
    search_string,
    shuffle_list,
)
from studyfrog.utils.dispatcher import dispatch
from studyfrog.utils.logging import log_debug, log_error, log_info, log_warning


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "end_rehearsal_run",
    "on_cancel_button_click",
    "on_easy_button_click",
    "on_edit_button_click",
    "on_end_button_click",
    "on_hard_button_click",
    "on_medium_button_click",
    "on_next_button_click",
    "on_previous_button_click",
    "start_rehearsal_run",
]


# ---------- Constants ---------- #

__NAME__: Final[str] = "src.gui.logic.rehearsal_run_view_logic"

CURRENT_INDEX: int = 0

REHEARSAL_RUN: Optional[Model] = None

REHEARSAL_RUN_ITEM: Optional[Model] = None

STACK_ITEM_KEYS: Final[list[str]] = []


# ---------- Helper Functions ---------- #


def _check_run_ending_conditions() -> bool:
    """
    Checks if the run has reached the end.

    Args:
        None

    Returns:
        bool: True if the run has reached the end, False otherwise.
    """

    return _get_current_index() >= _get_stack_items_length() or _get_current_index() <= -1


def _decrement_current_index() -> None:
    """
    Decrements the current index.

    Args:
        None

    Returns:
        None
    """

    global CURRENT_INDEX

    CURRENT_INDEX -= 1


def _get_current_index() -> int:
    """
    Returns the current index.

    Args:
        None

    Returns:
        int: The current index
    """

    return CURRENT_INDEX


def _get_rehearsal_run() -> Model:
    """
    Returns the rehearsal run.

    Args:
        None

    Returns:
        Model: The rehearsal run.

    Raises:
        ValueError: If the rehearsal run is not set.
    """

    if not exists(value=REHEARSAL_RUN):
        raise ValueError("Rehearsal run is not set. Call '_set_rehearsal_run' function first.")

    return REHEARSAL_RUN


def _get_rehearsal_run_item() -> Model:
    """
    Returns the rehearsal run item.

    Args:
        None

    Returns:
        Model: The rehearsal run item.

    Raises:
        ValueError: If the rehearsal run item is not set.
    """

    if not exists(value=REHEARSAL_RUN_ITEM):
        raise ValueError(
            "Rehearsal run item is not set. Call '_set_rehearsal_run_item' function first."
        )

    return REHEARSAL_RUN_ITEM


def _get_stack_item_key_at_current_index() -> str:
    """
    Returns the stack item key at the current index.

    Args:
        None

    Returns:
        str: The stack item key at the current index.
    """

    return STACK_ITEM_KEYS[_get_current_index()]


def _get_stack_items_length() -> int:
    """
    Returns the length of the stack items.

    Args:
        None

    Returns:
        int: The length of the stack items.
    """

    return len(STACK_ITEM_KEYS)


def _increment_current_index() -> None:
    """
    Increments the current index.

    Args:
        None

    Returns:
        None
    """

    global CURRENT_INDEX

    CURRENT_INDEX += 1


def _set_current_index(integer: int) -> None:
    """
    Sets the current index.

    Args:
        integer (int): The index to set.

    Returns:
        None
    """

    global CURRENT_INDEX

    CURRENT_INDEX = integer


def _set_rehearsal_run(model: Model) -> None:
    """
    Sets the rehearsal run.

    Args:
        model (Model): The rehearsal run model to set.

    Returns:
        None
    """

    global REHEARSAL_RUN

    REHEARSAL_RUN = model


def _set_rehearsal_run_item(model: Model) -> None:
    """
    Sets the rehearsal run item.

    Args:
        model (Model): The rehearsal run item to set.

    Returns:
        None
    """

    global REHEARSAL_RUN_ITEM

    REHEARSAL_RUN_ITEM = model


def _update_rehearsal_run() -> None:
    """
    Updates the rehearsal run.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If any errors occur.
    """

    model: Optional[Model] = (
        dispatch(
            event=UPDATE_REHEARSAL_RUN_IN_DB,
            model=_get_rehearsal_run(),
            namespace=GLOBAL_NAMESPACE,
            table_name="rehearsal_runs",
        )
        .get(
            "update_entry",
            [{}],
        )[0]
        .get(
            "result",
            {},
        )
    )

    if not model:
        log_error(message="Failed to update rehearsal run")
        return

    _set_rehearsal_run(model=model)


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

        response: Optional[Model] = (
            dispatch(
                event=model_type_to_event[model_type],
                id_=search_string(
                    pattern=PATTERNS["MODEL_ID"],
                    string=item_key,
                ),
                namespace=GLOBAL_NAMESPACE,
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

        if response.difficulty != difficulty_key:
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

        response: Optional[Model] = (
            dispatch(
                event=model_type_to_event[model_type],
                id_=search_string(
                    pattern=PATTERNS["MODEL_ID"],
                    string=item_key,
                ),
                namespace=GLOBAL_NAMESPACE,
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

        if response.priority != priority_key:
            _remove_from_stack_item_keys(key=item_key)


def _get_stack_items(key: str) -> list[str]:
    """
    Retrieves the keys of the stack items from the database.

    Args:
        key (str): The key of the stack to retrieve the items from.

    Returns:
        list[str]: The keys of the stack items.
    """

    response: Optional[Model] = (
        dispatch(
            event=GET_STACK_FROM_DB,
            id_=search_string(
                pattern=PATTERNS["MODEL_ID"],
                string=key,
            ),
            namespace=GLOBAL_NAMESPACE,
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

    return response.items["items"]


def _load_stack_item_from_db(stack_item_key: str) -> Model:
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
            namespace=GLOBAL_NAMESPACE,
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


def end_rehearsal_run() -> None:
    """
    Handles the end of the rehearsal run.

    Args:
        None

    Returns:
        None
    """

    log_info(message=f"Ending rehearsal run: {_get_rehearsal_run().key}")

    _get_rehearsal_run().finished_at = get_now()
    _get_rehearsal_run().finished_on = _get_rehearsal_run().finished_at.date()

    _get_rehearsal_run().duration = {
        "minutes": (
            _get_rehearsal_run().finished_at - _get_rehearsal_run().started_at
        ).total_seconds()
        // 60,
        "seconds": (
            _get_rehearsal_run().finished_at - _get_rehearsal_run().started_at
        ).total_seconds(),
    }

    _get_rehearsal_run().finished_at = _get_rehearsal_run().finished_at.isoformat()
    _get_rehearsal_run().finished_on = _get_rehearsal_run().finished_on.isoformat()
    _get_rehearsal_run().started_at = _get_rehearsal_run().started_at.isoformat()
    _get_rehearsal_run().started_on = _get_rehearsal_run().started_on.isoformat()

    log_info(message=f"Updating rehearsal run: {_get_rehearsal_run().key}")

    _update_rehearsal_run()

    log_info(
        message=f"Loading rehearsal run result view for rehearsal run {_get_rehearsal_run().key}..."
    )

    dispatch(
        event=GET_REHEARSAL_RUN_RESULT_VIEW,
        namespace=GLOBAL_NAMESPACE,
        rehearsal_run=_get_rehearsal_run(),
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
        namespace=GLOBAL_NAMESPACE,
    )


def on_easy_button_click() -> None:
    """
    Handles the 'easy' button click.

    Args:
        None

    Returns:
        None
    """

    difficulty: Model = (
        dispatch(
            event=FILTER_DIFFICULTIES_FROM_DB,
            name="easy",
            namespace=GLOBAL_NAMESPACE,
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

    model: Model = (
        dispatch(
            event=model_type_to_get_event[model_type],
            id_=model_id,
            namespace=GLOBAL_NAMESPACE,
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

    model.difficulty = difficulty.key

    dispatch(
        model=model,
        event=model_type_to_update_event[model_type],
        namespace=GLOBAL_NAMESPACE,
        table_name=pluralize_word(word=model_type),
    )

    dispatch(
        event=CLICKED_EASY_BUTTON,
        namespace=GLOBAL_NAMESPACE,
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
        namespace=GLOBAL_NAMESPACE,
    )


def on_end_button_click() -> None:
    """
    Handles the 'end' button click.

    This function dispatches the 'REHEARSAL_RUN_INDEX_MAX_REACHED' event,
    thus prompting the rehearsal run to end.

    Args:
        None

    Returns:
        None
    """

    dispatch(
        event=REHEARSAL_RUN_INDEX_MAX_REACHED,
        namespace=GLOBAL_NAMESPACE,
    )


def on_hard_button_click() -> None:
    """
    Handles the 'hard' button click.

    Args:
        None

    Returns:
        None
    """

    difficulty: Model = (
        dispatch(
            event=FILTER_DIFFICULTIES_FROM_DB,
            name="hard",
            namespace=GLOBAL_NAMESPACE,
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

    model: Model = (
        dispatch(
            event=model_type_to_get_event[model_type],
            id_=model_id,
            namespace=GLOBAL_NAMESPACE,
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

    model.difficulty = difficulty.key

    dispatch(
        model=model,
        event=model_type_to_update_event[model_type],
        namespace=GLOBAL_NAMESPACE,
        table_name=pluralize_word(word=model_type),
    )

    dispatch(
        event=CLICKED_HARD_BUTTON,
        namespace=GLOBAL_NAMESPACE,
    )


def on_medium_button_click() -> None:
    """
    Handles the 'medium' button click.

    Args:
        None

    Returns:
        None
    """

    difficulty: Model = (
        dispatch(
            event=FILTER_DIFFICULTIES_FROM_DB,
            name="medium",
            namespace=GLOBAL_NAMESPACE,
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
        string=_get_stack_item_key_at_current_index(),
    )

    if not exists(value=model_id):
        log_warning(
            message=f"Failed to retrieve model ID from stack item key {_get_stack_item_key_at_current_index()}"
        )

        return

    model_id = model_id.lower()

    model_type: Optional[str] = model_key_to_model_type(
        model_key=_get_stack_item_key_at_current_index()
    )

    if not exists(value=model_type):
        log_warning(
            message=f"Failed to retrieve model type from stack item key {_get_stack_item_key_at_current_index()}"
        )

        return

    model_type = model_type.lower()

    model: Model = (
        dispatch(
            event=model_type_to_get_event[model_type],
            id_=model_id,
            namespace=GLOBAL_NAMESPACE,
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

    model.difficulty = difficulty.key

    dispatch(
        model=model,
        event=model_type_to_update_event[model_type],
        namespace=GLOBAL_NAMESPACE,
        table_name=pluralize_word(word=model_type),
    )

    dispatch(
        event=CLICKED_MEDIUM_BUTTON,
        namespace=GLOBAL_NAMESPACE,
    )


def on_next_button_click() -> None:
    """
    Handles the 'next' button click.

    Args:
        None

    Returns:
        None
    """

    if _check_run_ending_conditions():
        log_warning(
            message=f"Current index {_get_current_index()} is equal to the last index {len(STACK_ITEM_KEYS) - 1}. Aborting..."
        )

        dispatch(
            event=REHEARSAL_RUN_INDEX_MAX_REACHED,
            namespace=GLOBAL_NAMESPACE,
        )

        return

    _increment_current_index()

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
        string=_get_stack_item_key_at_current_index(),
    )

    if not exists(value=model_id):
        log_warning(
            message=f"Failed to retrieve model ID from stack item key {_get_stack_item_key_at_current_index()}"
        )

        return

    model_id = model_id.lower()

    model_type: Optional[str] = model_key_to_model_type(
        model_key=_get_stack_item_key_at_current_index()
    )

    if not exists(value=model_type):
        log_warning(
            message=f"Failed to retrieve model type from stack item key {_get_stack_item_key_at_current_index()}"
        )

        return

    model_type = model_type.lower()

    model: Model = (
        dispatch(
            event=model_type_to_event[model_type],
            id_=model_id,
            namespace=GLOBAL_NAMESPACE,
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

    if not exists(value=model):
        log_warning(
            message=f"Failed to load stack item from database for key {_get_stack_item_key_at_current_index()}. Aborting..."
        )

        dispatch(
            event=REHEARSAL_RUN_INDEX_MAX_REACHED,
            namespace=GLOBAL_NAMESPACE,
        )

        return

    rehearsal_run_item: Optional[Model] = (
        dispatch(
            event=GET_REHEARSAL_RUN_ITEM_MODEL,
            item=_get_stack_item_key_at_current_index(),
            namespace=GLOBAL_NAMESPACE,
        )
        .get(
            "get_rehearsal_run_item_model",
            {},
        )[0]
        .get(
            "result",
            {},
        )
    )

    id_: Optional[int] = (
        dispatch(
            event=ADD_REHEARSAL_RUN_ITEM_TO_DB,
            model=rehearsal_run_item,
            namespace=GLOBAL_NAMESPACE,
            table_name="rehearsal_run_items",
        )
        .get(
            "add_entry_if_not_exists",
            {},
        )
        .get(
            "result",
            None,
        )
    )

    if not exists(value=id_):
        log_warning(
            message="Failed to add rehearsal run item to database",
            name=f"{__NAME__}.on_next_button_click",
        )
        return

    rehearsal_run_item = (
        dispatch(
            event=GET_REHEARSAL_RUN_ITEM_FROM_DB,
            id_=id_,
            namespace=GLOBAL_NAMESPACE,
            table_name="rehearsal_run_items",
        )
        .get(
            "get_rehearsal_run_item_from_db",
            [{}],
        )[0]
        .get(
            "result",
            {},
        )
    )

    if not exists(value=rehearsal_run_item):
        log_warning(
            message=f"Failed to get rehearsal run item with ID {id_} from database",
            name=f"{__NAME__}.on_next_button_click",
        )
        return

    _set_rehearsal_run_item(model=rehearsal_run_item)

    _get_rehearsal_run().items["items"][_get_stack_item_key_at_current_index()].append(
        rehearsal_run_item.id
    )
    _get_rehearsal_run().items["total"][_get_stack_item_key_at_current_index()] = len(
        _get_rehearsal_run().items["items"]
    )

    log_debug(
        message=f"Rehearsal run item {rehearsal_run_item.id} added to stack item {_get_stack_item_key_at_current_index()}",
        name=f"{__NAME__}.on_next_button_click",
    )

    _update_rehearsal_run()

    dispatch(
        event=CLICKED_NEXT_BUTTON,
        namespace=GLOBAL_NAMESPACE,
        **{
            model_type.lower(): model,
        },
    )

    dispatch(
        event=REHEARSAL_RUN_INDEX_INCREMENTED,
        namespace=GLOBAL_NAMESPACE,
    )

    dispatch(
        model=model,
        event=LOAD_REHEARSAL_VIEW_FORM,
        namespace=GLOBAL_NAMESPACE,
    )


def on_previous_button_click() -> None:
    """
    Handles the 'previous' button click.

    Args:
        None

    Returns:
        None
    """

    if _check_run_ending_conditions():
        log_warning(message=f"Current index {_get_current_index()} is equal to -1. Aborting...")

        _set_current_index(integer=0)

        dispatch(
            event=REHEARSAL_RUN_INDEX_MIN_REACHED,
            namespace=GLOBAL_NAMESPACE,
        )

        return

    _decrement_current_index()

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
        string=_get_stack_item_key_at_current_index(),
    )

    if not exists(value=model_id):
        log_warning(
            message=f"Failed to retrieve model ID from stack item key {_get_stack_item_key_at_current_index()}"
        )

        return

    model_id = model_id.lower()

    model_type: Optional[str] = model_key_to_model_type(
        model_key=_get_stack_item_key_at_current_index()
    )

    if not exists(value=model_type):
        log_warning(
            message=f"Failed to retrieve model type from stack item key {_get_stack_item_key_at_current_index()}"
        )

        return

    model_type = model_type.lower()

    model: Model = (
        dispatch(
            event=model_type_to_event[model_type],
            id_=model_id,
            namespace=GLOBAL_NAMESPACE,
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
        namespace=GLOBAL_NAMESPACE,
        **{
            model_type: model,
        },
    )

    dispatch(
        event=REHEARSAL_RUN_INDEX_DECREMENTED,
        namespace=GLOBAL_NAMESPACE,
    )

    dispatch(
        _load_stack_item_from_db(stack_item_key=_get_stack_item_key_at_current_index()),
        event=LOAD_REHEARSAL_VIEW_FORM,
        namespace=GLOBAL_NAMESPACE,
    )


def start_rehearsal_run(model: Model) -> None:
    """
    Handles the start of the rehearsal run.

    Args:
        model (Model): The model to start.

    Returns:
        None
    """

    model.started_at = get_now()
    model.started_on = get_today()

    for stack in model.stacks:
        stack_items: list[str] = _get_stack_items(key=stack)

        if not stack_items:
            continue

        for key in stack_items:
            _add_to_stack_items(key=key)

    if model.configuration.get(
        "filter_by_difficulty_enabled",
        False,
    ):
        _filter_stack_items_by_difficulty(
            difficulty_key=model.configuration.get("filter_by_difficulty")
        )

    if model.configuration.get(
        "filter_by_priority_enabled",
        False,
    ):
        _filter_stack_items_by_priority(priority_key=model.configuration.get("filter_by_priority"))

    if model.configuration.get(
        "item_order_randomization_enabled",
        False,
    ):
        shuffle_list(list_=STACK_ITEM_KEYS)

    _set_current_index(integer=0)

    _set_rehearsal_run(model=model)

    _get_rehearsal_run().items = {
        "items": {},
        "total": 0,
    }

    _update_rehearsal_run()

    dispatch(
        _load_stack_item_from_db(stack_item_key=_get_stack_item_key_at_current_index()),
        event=LOAD_REHEARSAL_VIEW_FORM,
        namespace=GLOBAL_NAMESPACE,
    )
