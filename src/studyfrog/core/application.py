"""
Author: Louis Goodnews
Date: 2025-12-10
"""

from datetime import datetime
from typing import Final, Optional

from constants.events import (
    APPLICATION_STARTED,
    APPLICATION_STARTING,
    APPLICATION_STOPPED,
    APPLICATION_STOPPING,
    GET_DASHBOARD_VIEW,
)
from core.bootstrap import (
    ensure_directories,
    ensure_files,
    ensure_defaults,
    initialize_gui,
    subscribe_to_events,
    unsubscribe_from_events,
)
from gui.gui import get_root
from utils.common import get_now
from utils.dispatcher import dispatch
from utils.logging import log_error, log_info, log_trace


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "run_post_start_tasks",
    "run_post_stop_tasks",
    "run_pre_start_tasks",
    "run_pre_stop_tasks",
    "start_application",
    "stop_application",
]


# ---------- Constants ---------- #

START: Optional[datetime] = None

STOP: Optional[datetime] = None


# ---------- Helper Functions ---------- #


def _get_runtime_duration() -> Optional[int]:
    """
    Returns the application runtime duration.

    Args:
        None

    Returns:
        Optional[int]: The application runtime duration in seconds.

    Raises:
        ValueError: If the start and stop timestamps have not been set. Call '_set_start' and '_set_stop' first.
    """

    try:
        return (_get_stop() - _get_start()).total_seconds()
    except ValueError:
        log_error(
            message="The start and stop timestamps have not been set. Call '_set_start' and '_set_stop' first."
        )
        return None


def _get_start() -> Optional[datetime]:
    """
    Returns the starting timestamp of the application.

    Args:
        None

    Returns:
        Optional[datetime]: The starting timestamp of the application.

    Raises:
        ValueError: If the start timestamp has not been set. Call '_set_start' first.
    """

    if START is None:
        raise ValueError("The start timestamp has not been set. Call '_set_start' first.")

    return START


def _get_stop() -> Optional[datetime]:
    """
    Returns the stopping timestamp of the application.

    Args:
        None

    Returns:
        Optional[datetime]: The stopping timestamp of the application.

    Raises:
        ValueError: If the stop timestamp has not been set. Call '_set_stop' first.
    """

    if STOP is None:
        raise ValueError("The stop timestamp has not been set. Call '_set_stop' first.")

    return STOP


def _set_start(timestamp: datetime) -> None:
    """
    Sets the starting timestamp of the application.

    Args:
        timestamp (datetime): The timestamp to set as the starting timestamp.

    Returns:
        None
    """

    global START

    if START is not None:
        return

    START = timestamp


def _set_stop(timestamp: datetime) -> None:
    """
    Sets the stopping timestamp of the application.

    Args:
        timestamp (datetime): The timestamp to set as the stopping timestamp.

    Returns:
        None
    """

    global STOP

    if STOP is not None:
        return

    STOP = timestamp


# ---------- Functions ---------- #


def run_post_start_tasks() -> None:
    """
    Runs the post start tasks.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an exception is caught while running the post start tasks.
    """

    try:
        initialize_gui()
        dispatch(event=APPLICATION_STARTED)
        dispatch(event=GET_DASHBOARD_VIEW)
    except Exception as e:
        log_error(message=f"Caught an exception while running post start tasks: {e}")
        raise e


def run_post_stop_tasks() -> None:
    """
    Runs the post stop tasks.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an exception is caught while running the post stop tasks.
    """

    try:
        dispatch(event=APPLICATION_STOPPED)
        unsubscribe_from_events()
    except Exception as e:
        log_error(message=f"Caught an exception while running post stop tasks: {e}")
        raise e


def run_pre_start_tasks() -> None:
    """
    Runs the pre start tasks.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an exception is caught while running the pre start tasks.
    """

    try:
        ensure_directories()
        ensure_files()
        ensure_defaults()
        subscribe_to_events()
        dispatch(event=APPLICATION_STARTING)
    except Exception as e:
        log_error(message=f"Caught an exception while running pre start tasks: {e}")
        raise e


def run_pre_stop_tasks() -> None:
    """
    Runs the pre stop tasks.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an exception is caught while running the pre stop tasks.
    """

    try:
        dispatch(event=APPLICATION_STOPPING)
    except Exception as e:
        log_error(message=f"Caught an exception while running pre stop tasks: {e}")
        raise e


def start_application() -> None:
    """
    Starts the application.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an exception is caught while starting the application.
    """

    try:
        _set_start(timestamp=get_now())
        log_info(message="Starting the application...")
        run_pre_start_tasks()
        log_info(message="Application started. Hello!")
        run_post_start_tasks()
        get_root().mainloop()
    except Exception as e:
        log_error(message=f"Caught an exception while starting the application: {e}")
        raise e


def stop_application() -> None:
    """
    Stops the application.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an exception is caught while stopping the application.
    """

    try:
        _set_stop(timestamp=get_now())
        log_info(message="Stopping the application...")
        run_pre_stop_tasks()
        run_post_stop_tasks()
        log_info(message="Application stopped. Goodbye!")
        log_trace(message=f"Runtime duration: {_get_runtime_duration()} seconds.")
    except Exception as e:
        log_error(message=f"Caught an exception while stopping the application: {e}")
        raise e
