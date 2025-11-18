"""
Author: Louis Goodnews
Date: 2025-11-16
"""

from typing import Final, Literal

from common.constants import (
    ASSETS_DIR,
    BACKUP_DIR,
    CONFIG_DIR,
    DATA_DIR,
    EXPORTS_DIR,
    IMPORTS_DIR,
    LOG_DIR,
    RESOURCES_DIR,
    TEMP_DIR,
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
from core.storage import create_table_if_not_exists
from gui.gui import (
    get_bottom_frame,
    get_center_frame,
    get_edit_menu,
    get_file_menu,
    get_menu,
    get_root,
    get_top_frame,
    get_view_menu,
)
from gui.views.views import get_view
from utils.utils import ensure_dir, ensure_json, log_exception, log_info


# ---------- Constants ---------- #

NAME: Final[Literal["core.core"]] = "core.core"


# ---------- Functions ---------- #


def ensure_defaults() -> None:
    """
    Ensures default values are present in the database.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    global NAME

    log_info(
        message="Ensuring defaults...",
        name=NAME,
    )

    try:
        log_info(
            message="Defaults ensured.",
            name=NAME,
        )
    except Exception as e:
        log_exception(
            name=NAME,
            message="Failed to ensure defaults.",
            exception=e,
        )
        raise e


def initialize_directories() -> None:
    """
    Initializes directories.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    global NAME

    log_info(
        message="Initializing directories...",
        name=NAME,
    )

    try:
        for path in (
            ASSETS_DIR,
            BACKUP_DIR,
            CONFIG_DIR,
            DATA_DIR,
            EXPORTS_DIR,
            IMPORTS_DIR,
            LOG_DIR,
            RESOURCES_DIR,
            TEMP_DIR,
        ):
            ensure_dir(path=path)

        log_info(
            message="Directories initialized.",
            name=NAME,
        )
    except Exception as e:
        log_exception(
            name=NAME,
            message="Failed to initialize directories.",
            exception=e,
        )
        raise e


def initialize_files() -> None:
    """
    Initializes files.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    global NAME

    log_info(
        message="Initializing files...",
        name=NAME,
    )

    try:
        for path in [
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
        ]:
            ensure_json(path=path)

        log_info(
            message="Files initialized.",
            name=NAME,
        )
    except Exception as e:
        log_exception(
            name=NAME,
            message="Failed to initialize files.",
            exception=e,
        )
        raise e


def initialize_gui() -> None:
    """
    Initializes the GUI.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    global NAME

    log_info(
        message="Initializing GUI...",
        name=NAME,
    )

    try:
        get_root()
        get_menu()
        get_edit_menu()
        get_file_menu()
        get_view_menu()
        get_top_frame()
        get_center_frame()
        get_bottom_frame()
        get_view(name="dashboard")

        log_info(
            message="GUI initialized.",
            name=NAME,
        )
    except Exception as e:
        log_exception(
            name=NAME,
            message="Failed to initialize GUI.",
            exception=e,
        )
        raise e


def initialize_tables() -> None:
    """
    Initializes tables.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    global NAME

    log_info(
        message="Initializing tables...",
        name=NAME,
    )

    try:
        for path in [
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
        ]:
            create_table_if_not_exists(name=path.stem)

        log_info(
            message="Tables initialized.",
            name=NAME,
        )
    except Exception as e:
        log_exception(
            name=NAME,
            message="Failed to initialize tables.",
            exception=e,
        )
        raise e


def run_post_start_tasks() -> None:
    """
    Runs tasks that need to be run after the application starts.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    global NAME

    log_info(
        message="Running post-start tasks...",
        name=NAME,
    )

    try:
        log_info(
            message="Post-start tasks completed.",
            name=NAME,
        )
        get_root().mainloop()
    except Exception as e:
        log_exception(
            name=NAME,
            message="Failed to run post-start tasks.",
            exception=e,
        )
        raise e


def run_post_stop_tasks() -> None:
    """
    Runs tasks that need to be run after the application stops.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    global NAME

    log_info(
        message="Running post-stop tasks...",
        name=NAME,
    )

    try:
        log_info(
            message="Post-stop tasks completed.",
            name=NAME,
        )
    except Exception as e:
        log_exception(
            name=NAME,
            message="Failed to run post-stop tasks.",
            exception=e,
        )
        raise e


def run_pre_start_tasks() -> None:
    """
    Runs tasks that need to be run before the application starts.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    global NAME

    log_info(
        message="Running pre-start tasks...",
        name=NAME,
    )

    try:
        ensure_defaults()
        initialize_directories()
        initialize_files()
        initialize_gui()
        initialize_tables()

        log_info(
            message="Pre-start tasks completed.",
            name=NAME,
        )
    except Exception as e:
        log_exception(
            name=NAME,
            message="Failed to run pre-start tasks.",
            exception=e,
        )
        raise e


def run_pre_stop_tasks() -> None:
    """
    Runs tasks that need to be run before the application stops.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    global NAME

    log_info(
        message="Running pre-stop tasks...",
        name=NAME,
    )

    try:
        log_info(
            message="Pre-stop tasks completed.",
            name=NAME,
        )
    except Exception as e:
        log_exception(
            name=NAME,
            message="Failed to run pre-stop tasks.",
            exception=e,
        )
        raise e


def start() -> None:
    """
    Starts the application.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    global NAME

    log_info(
        message="Starting application...",
        name=NAME,
    )

    try:
        run_pre_start_tasks()
        run_post_start_tasks()

        log_info(
            message="Application started.",
            name=NAME,
        )
    except Exception as e:
        log_exception(
            name=NAME,
            message="Failed to start application.",
            exception=e,
        )
        raise e


def stop() -> None:
    """
    Stops the application.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    global NAME

    log_info(
        message="Stopping application...",
        name=NAME,
    )

    try:
        run_pre_stop_tasks()
        run_post_stop_tasks()

        log_info(
            message="Application stopped.",
            name=NAME,
        )
    except Exception as e:
        log_exception(
            name=NAME,
            message="Failed to stop application.",
            exception=e,
        )
        raise e


# ---------- Auto-Export ---------- #

# Auto-Export all non-private symbols
__all__: Final[list[str]] = [
    key
    for (
        key,
        value,
    ) in globals().items()
    if not key.startswith("_") and callable(value)
]
