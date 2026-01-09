"""
Author: Louis Goodnews
Date: 2025-12-10
"""

from pathlib import Path
from typing import Any, Callable, Final

from constants.common import GLOBAL
from constants.defaults import (
    DEFAULT_EASY_DIFFICULTY,
    DEFAULT_HARD_DIFFICULTY,
    DEFAULT_HIGH_PRIORITY,
    DEFAULT_HIGHEST_PRIORITY,
    DEFAULT_LOW_PRIORITY,
    DEFAULT_LOWEST_PRIORITY,
    DEFAULT_MEDIUM_DIFFICULTY,
    DEFAULT_MEDIUM_PRIORITY,
    DEFAULT_USER,
)
from constants.directories import (
    ASSETS_DIR,
    CONFIG_DIR,
    DATA_DIR,
    EXPORTS_DIR,
    IMAGES_DIR,
    IMPORTS_DIR,
    LOGS_DIR,
    RESOURCES_DIR,
    TEMP_DIR,
)
from constants.events import *
from constants.files import (
    ANSWERS_DB_JSON,
    ASSOCIATIONS_DB_JSON,
    CONFIG_DB_JSON,
    CUSTOMFIELDS_DB_JSON,
    DIFFICULTIES_DB_JSON,
    FLASHCARDS_DB_JSON,
    IMAGES_DB_JSON,
    NOTES_DB_JSON,
    OPTIONS_DB_JSON,
    PRIORITIES_DB_JSON,
    QUESTIONS_DB_JSON,
    REHEARSAL_RUN_DB_JSON,
    REHEARSAL_RUN_ITEM_DB_JSON,
    STACKS_DB_JSON,
    SUBJECTS_DB_JSON,
    TAGS_DB_JSON,
    TEACHERS_DB_JSON,
    USERS_DB_JSON,
)
from gui.forms.answer_create_form import (
    get_answer_choice_create_form,
    get_answer_open_ended_create_form,
    get_answer_true_false_create_form,
)
from gui.forms.flashcard_create_form import get_flashcard_create_form
from gui.forms.note_create_form import get_note_create_form
from gui.forms.question_create_form import get_question_create_form
from gui.forms.stack_create_form import get_stack_create_form
from gui.gui import get_bottom_frame, get_center_frame, get_root, get_top_frame
from gui.views.create_view import get_create_view
from gui.views.dashboard_view import get_dashboard_view
from gui.views.edit_view import get_edit_view
from gui.views.delete_confirmation_view import get_delete_confirmation_view
from gui.views.flashcard_rehearsal_view import get_flashcard_rehearsal_view
from gui.views.note_rehearsal_view import get_note_rehearsal_view
from gui.views.question_rehearsal_view import get_question_rehearsal_view
from gui.views.rehearsal_run_view import get_rehearsal_run_view
from gui.views.rehearsal_run_result_view import get_rehearsal_run_result_view
from gui.views.rehearsal_run_setup_view import get_rehearsal_run_setup_view
from gui.widgets import get_error_toast, get_info_toast, get_success_toast, get_warning_toast
from models.factories import (
    get_answer_model_dict,
    get_flashcard_model_dict,
    get_note_model_dict,
    get_question_model_dict,
    get_rehearsal_run_model_dict,
    get_rehearsal_run_item_model_dict,
    get_stack_model_dict,
)
from utils.common import pluralize_word
from utils.directories import ensure_directory
from utils.dispatcher import subscribe, unsubscribe
from utils.files import ensure_file
from utils.logging import log_error, log_info
from utils.storage import (
    add_entries_if_not_exist,
    add_entry_if_not_exist,
    delete_all_entries,
    delete_entries,
    delete_entry,
    filter_entries,
    get_all_entries,
    get_entries,
    get_entry,
    update_entry,
    update_entries,
)


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "initialize_gui",
    "subscribe_to_events",
    "unsubscribe_from_events",
]


# ---------- Constants ---------- #

APPLICATION_DIRECTORIES: Final[tuple[Path]] = (
    ASSETS_DIR,
    CONFIG_DIR,
    DATA_DIR,
    EXPORTS_DIR,
    IMAGES_DIR,
    IMPORTS_DIR,
    LOGS_DIR,
    RESOURCES_DIR,
    TEMP_DIR,
)

DEFAULT_DIFFICULTY_MODEL_DICTS: Final[tuple[dict[str, Any]]] = (
    DEFAULT_EASY_DIFFICULTY,
    DEFAULT_HARD_DIFFICULTY,
    DEFAULT_MEDIUM_DIFFICULTY,
)

DEFAULT_PRIORITY_MODEL_DICTS: Final[tuple[dict[str, Any]]] = (
    DEFAULT_HIGH_PRIORITY,
    DEFAULT_HIGHEST_PRIORITY,
    DEFAULT_LOW_PRIORITY,
    DEFAULT_LOWEST_PRIORITY,
    DEFAULT_MEDIUM_PRIORITY,
)

DEFAULT_USER_MODEL_DICT: Final[dict[str, Any]] = DEFAULT_USER

DEFAULT_MODEL_DICTS: Final[tuple[dict[str, Any]]] = (
    *DEFAULT_DIFFICULTY_MODEL_DICTS,
    *DEFAULT_PRIORITY_MODEL_DICTS,
    DEFAULT_USER_MODEL_DICT,
)

STORAGE_FILES: Final[tuple[Path]] = (
    ANSWERS_DB_JSON,
    ASSOCIATIONS_DB_JSON,
    CONFIG_DB_JSON,
    CUSTOMFIELDS_DB_JSON,
    DIFFICULTIES_DB_JSON,
    FLASHCARDS_DB_JSON,
    IMAGES_DB_JSON,
    NOTES_DB_JSON,
    OPTIONS_DB_JSON,
    PRIORITIES_DB_JSON,
    QUESTIONS_DB_JSON,
    REHEARSAL_RUN_DB_JSON,
    REHEARSAL_RUN_ITEM_DB_JSON,
    STACKS_DB_JSON,
    SUBJECTS_DB_JSON,
    TAGS_DB_JSON,
    TEACHERS_DB_JSON,
    USERS_DB_JSON,
)

STORAGE_FUNCTIONS: Final[tuple[Callable[[..., Any], Any]]] = [
    add_entry_if_not_exist,
    add_entries_if_not_exist,
    delete_all_entries,
    delete_entry,
    delete_entries,
    filter_entries,
    get_all_entries,
    get_entry,
    get_entries,
    update_entry,
    update_entries,
]

SUBSCRIPTION_IDS: Final[list[str]] = []


# ---------- Helper Functions ---------- #


def _get_get_create_form_subscriptions() -> list[dict[str, Any]]:
    """
    Generates a list of subscription dictionaries for 'GET_..._CREATE_FORM' events.

    These events are used to retrieve the specific GUI forms (e.g., AnswerCreateForm)
    for model creation, and are registered as global, persistent event handlers.

    Returns:
        list[dict[str, Any]]: A list of subscription dictionaries, each defining
                              the event, the function to be called, namespace,
                              persistence, and priority.
    """

    subscriptions: list[dict[str, Any]] = [
        {
            "event": GET_ANSWER_CHOICE_CREATE_FORM,
            "function": get_answer_choice_create_form,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": GET_ANSWER_OPEN_ENDED_CREATE_FORM,
            "function": get_answer_open_ended_create_form,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": GET_ANSWER_TRUE_FALSE_CREATE_FORM,
            "function": get_answer_true_false_create_form,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": GET_FLASHCARD_CREATE_FORM,
            "function": get_flashcard_create_form,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": GET_NOTE_CREATE_FORM,
            "function": get_note_create_form,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": GET_QUESTION_CREATE_FORM,
            "function": get_question_create_form,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": GET_STACK_CREATE_FORM,
            "function": get_stack_create_form,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
    ]

    return subscriptions


def _get_get_view_form_subscriptions() -> list[dict[str, Any]]:
    """
    Generates a list of subscription dictionaries for view-related event functions.

    These events typically retrieve view components (e.g., get_create_view, get_dashboard_view)
    and are registered as global, persistent handlers.

    Args:
        None

    Returns:
        list[dict[str, Any]]: A list of subscription dictionaries, each containing
                              the 'event', 'function', 'namespace', 'persistent', and 'priority'.
    """

    subscriptions: list[dict[str, Any]] = []

    subscriptions.extend(
        [
            {
                "event": GET_CREATE_VIEW,
                "function": get_create_view,
                "namespace": GLOBAL,
                "persistent": True,
                "priority": 100,
            },
            {
                "event": GET_DASHBOARD_VIEW,
                "function": get_dashboard_view,
                "namespace": GLOBAL,
                "persistent": True,
                "priority": 100,
            },
            {
                "event": GET_EDIT_VIEW,
                "function": get_edit_view,
                "namespace": GLOBAL,
                "persistent": True,
                "priority": 100,
            },
            {
                "event": GET_DELETE_CONFIRMATION_VIEW,
                "function": get_delete_confirmation_view,
                "namespace": GLOBAL,
                "persistent": True,
                "priority": 100,
            },
            {
                "event": GET_FLASHCARD_REHEARSAL_VIEW,
                "function": get_flashcard_rehearsal_view,
                "namespace": GLOBAL,
                "persistent": True,
                "priority": 100,
            },
            {
                "event": GET_NOTE_REHEARSAL_VIEW,
                "function": get_note_rehearsal_view,
                "namespace": GLOBAL,
                "persistent": True,
                "priority": 100,
            },
            {
                "event": GET_QUESTION_REHEARSAL_VIEW,
                "function": get_question_rehearsal_view,
                "namespace": GLOBAL,
                "persistent": True,
                "priority": 100,
            },
            {
                "event": GET_REHEARSAL_RUN_VIEW,
                "function": get_rehearsal_run_view,
                "namespace": GLOBAL,
                "persistent": True,
                "priority": 100,
            },
            {
                "event": GET_REHEARSAL_RUN_RESULT_VIEW,
                "function": get_rehearsal_run_result_view,
                "namespace": GLOBAL,
                "persistent": True,
                "priority": 100,
            },
            {
                "event": GET_REHEARSAL_RUN_SETUP_VIEW,
                "function": get_rehearsal_run_setup_view,
                "namespace": GLOBAL,
                "persistent": True,
                "priority": 100,
            },
        ]
    )

    return subscriptions


def _get_model_event_subscriptions() -> list[dict[str, Any]]:
    """
    Generates a list of subscription dictionaries for model-related event functions.

    These events typically retrieve model dictionaries (e.g., get_answer_model_dict)
    and are registered as global, persistent handlers.

    Returns:
        list[dict[str, Any]]: A list of subscription dictionaries, each containing
                              the 'event', 'function', 'namespace', 'persistent', and 'priority'.
    """

    subscriptions: list[dict[str, Any]] = [
        {
            "event": GET_ANSWER_MODEL_DICT,
            "function": get_answer_model_dict,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": GET_FLASHCARD_MODEL_DICT,
            "function": get_flashcard_model_dict,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": GET_NOTE_MODEL_DICT,
            "function": get_note_model_dict,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": GET_QUESTION_MODEL_DICT,
            "function": get_question_model_dict,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": GET_REHEARSAL_RUN_MODEL_DICT,
            "function": get_rehearsal_run_model_dict,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": GET_REHEARSAL_RUN_ITEM_MODEL_DICT,
            "function": get_rehearsal_run_item_model_dict,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": GET_STACK_MODEL_DICT,
            "function": get_stack_model_dict,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
    ]

    return subscriptions


def _get_storage_event_subscriptions() -> list[dict[str, Any]]:
    """
    Dynamically generates a list of subscription dictionaries for all
    model-specific command events.

    Each subscription assigns a command event (e.g., ADD_FLASHCARD) to the
    corresponding storage function (e.g., add_entry_if_not_exist). These storage functions
    are called directly as handlers when the event is triggered.

    The function ensures that the 11 command event types (Add, Delete, Get, Filter, Update)
    are correctly assigned to the 11 storage functions for each model type.

    Args:
        None

    Returns:
        list[dict[str, Any]]: A list of subscription dictionaries.
    """

    subscriptions: list[dict[str, Any]] = []

    for model_type in (
        "answer",
        "customfield",
        "difficulty",
        "flashcard",
        "image",
        "note",
        "option",
        "priority",
        "question",
        "rehearsal_run",
        "rehearsal_run_item",
        "stack",
        "subject",
        "tag",
        "teacher",
    ):
        singular: str = model_type
        plural: str = pluralize_word(word=singular)

        events: list[str] = [
            event
            for event in sorted(
                set(
                    get_events_by_names(
                        names=get_events_by_prefixes(
                            prefixes=[
                                f"ADD_{singular.upper()}",
                                f"ADD_{plural.upper()}",
                                f"DELETE_ALL_{plural.upper()}",
                                f"DELETE_{singular.upper()}",
                                f"DELETE_{plural.upper()}",
                                f"FILTER_{plural.upper()}",
                                f"GET_{singular.upper()}",
                                f"GET_{plural.upper()}",
                                f"GET_ALL_{plural.upper()}",
                                f"UPDATE_{singular.upper()}",
                                f"UPDATE_{plural.upper()}",
                            ]
                        )
                    )
                )
            )
            if not "form" in event and not "model" in event and not "view" in event
        ]

        if model_type == "rehearsal_run":
            events = [event for event in events if not "rehearsal_run_item" in event]

        elif model_type == "rehearsal_runitem":
            events = [event for event in events if "rehearsal_run_item" in event]

        if len(events) != len(STORAGE_FUNCTIONS):
            log_info(
                message=f"Skipping subscriptions for '{singular}' due to mismatch between {len(events)} events and {len(STORAGE_FUNCTIONS)} functions."
            )
            continue

        for (
            event,
            function,
        ) in zip(
            events,
            STORAGE_FUNCTIONS,
            strict=True,
        ):
            subscriptions.append(
                {
                    "event": event,
                    "function": function,
                    "namespace": GLOBAL,
                    "persistent": True,
                    "priority": 100,
                }
            )

    return subscriptions


def _get_toast_event_subscriptions() -> list[dict[str, Any]]:
    """
    Generates a list of subscription dictionaries for toast notification events.

    These events trigger the display of different types of toast messages
    (e.g., error, info, success, warning) via their respective getter functions.

    Returns:
        list[dict[str, Any]]: A list of subscription dictionaries for toast events.
    """

    subscriptions: list[dict[str, Any]] = [
        {
            "event": GET_ERROR_TOAST,
            "function": get_error_toast,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": GET_INFO_TOAST,
            "function": get_info_toast,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": GET_SUCCESS_TOAST,
            "function": get_success_toast,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": GET_WARNING_TOAST,
            "function": get_warning_toast,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
    ]

    return subscriptions


# ---------- Functions ---------- #


def ensure_directories() -> None:
    """
    Ensures that all necessary application directories exist.

    It iterates through the defined APPLICATION_DIRECTORIES list and calls
    the utility function to create each directory if it does not already exist.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an exception occurs while ensuring application directories.
    """

    try:
        for directory in APPLICATION_DIRECTORIES:
            ensure_directory(directory=directory)

        log_info(
            message=f"Successfully ensured {len(APPLICATION_DIRECTORIES)} application directories."
        )
    except Exception as e:
        log_error(message=f"Caught an exception while ensuring application directories: {e}")
        raise e


def ensure_defaults() -> None:
    """
    Ensures that all necessary application default settings and initial data are present.

    Currently unimplemented placeholder for future default configuration logic.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an exception occurs while ensuring default difficulty models.
    """

    try:
        for default_model_dict in DEFAULT_MODEL_DICTS:
            add_entry_if_not_exist(
                entry=default_model_dict,
                table_name=pluralize_word(word=default_model_dict["metadata"]["type"].lower()),
            )
    except Exception as e:
        log_error(message=f"Caught an exception while ensuring default difficulty models: {e}")
        raise e


def ensure_files() -> None:
    """
    Ensures that all necessary application data files (JSON databases) exist.

    It iterates through the defined STORAGE_FILES list and calls the utility
    function to create each file if it does not already exist.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an exception occurs while ensuring storage files.
    """

    try:
        for file in STORAGE_FILES:
            ensure_file(file=file)

        log_info(message=f"Successfully ensured {len(STORAGE_FILES)} storage files.")
    except Exception as e:
        log_error(message=f"Caught an exception while ensuring storage files: {e}")
        raise e


def initialize_gui() -> None:
    """
    Initializes the GUI.

    Sets up the main application window and its primary frames
    (root, top, center, and bottom frame) in preparation for application startup.

    Args:
        None

    Returns:
        None
    """

    get_root()
    get_bottom_frame()
    get_center_frame()
    get_top_frame()


def subscribe_to_events() -> None:
    """
    Subscribes to all storage command events.

    This function calls the helper to dynamically generate all subscriptions
    for the database layer (e.g., ADD_FLASHCARD events triggering the add_entry_if_not_exist
    function) and registers them with the event dispatcher.

    Args:
        None

    Returns:
        None
    """

    subscriptions: list[dict[str, Any]] = []

    subscriptions.extend(_get_get_create_form_subscriptions())
    subscriptions.extend(_get_get_view_form_subscriptions())
    subscriptions.extend(_get_model_event_subscriptions())
    subscriptions.extend(_get_storage_event_subscriptions())
    subscriptions.extend(_get_toast_event_subscriptions())

    for subscription in subscriptions:
        SUBSCRIPTION_IDS.append(
            subscribe(
                event=subscription["event"],
                function=subscription["function"],
                namespace=subscription["namespace"],
                persistent=subscription["persistent"],
                priority=subscription["priority"],
            )
        )

    log_info(message=f"Subscribed to {len(subscriptions)} events.")


def unsubscribe_from_events() -> None:
    """
    Unsubscribes from all currently active event subscriptions.

    Clears the event listeners registered by `subscribe_to_events()` using the
    stored subscription UUIDs, ensuring a clean shutdown or event reset.

    Args:
        None

    Returns:
        None
    """

    for uuid in SUBSCRIPTION_IDS:
        unsubscribe(uuid=uuid)

    log_info(message=f"Unsubscribed from {len(SUBSCRIPTION_IDS)} events.")

    SUBSCRIPTION_IDS.clear()
