"""
Author: Louis Goodnews
Date: 2025-11-16
"""

from typing import Final

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
    CONFIG_FILE,
    ANSWERS_TABLE_FILE,
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
from utils.utils import ensure_dir, ensure_json


# ---------- Constants ---------- #


# ---------- Functions ---------- #


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
    except Exception as e:
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

    try:
        for path in [
            ANSWERS_TABLE_FILE,
            CONFIG_FILE,
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
    except Exception as e:
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
    except Exception as e:
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

    try:
        get_root().mainloop()
    except Exception as e:
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

    try:
        pass
    except Exception as e:
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

    try:
        initialize_directories()
        initialize_files()
        initialize_gui()
    except Exception as e:
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

    try:
        pass
    except Exception as e:
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

    try:
        run_pre_start_tasks()
        run_post_start_tasks()
    except Exception as e:
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

    try:
        run_pre_stop_tasks()
        run_post_stop_tasks()
    except Exception as e:
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
