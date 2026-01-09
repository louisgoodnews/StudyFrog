"""
Author: Louis Goodnews
Date: 2025-12-31
Description: The rehearsal run result view of the application.
"""

import customtkinter as ctk

from typing import Any, Final, Optional

from constants.common import GLOBAL
from constants.events import DESTROY_REHEARSAL_RUN_RESULT_VIEW
from gui.gui import get_bottom_frame, get_center_frame, get_top_frame
from models.factories import ModelDict
from utils.dispatcher import subscribe, unsubscribe
from utils.gui import clear_frames, reset_frame_grids
from utils.logging import log_debug, log_error, log_info, log_warning


# ---------- Exports ---------- #

__all__: Final[list[str]] = []


# ---------- Constants ---------- #

REHEARSAL_RUN: Optional[ModelDict] = None

SUBSCRIPTION_IDS: Final[list[str]] = []

# ---------- Helper Functions ---------- #


# ---------- Private Functions ---------- #


def _configure_bottom_frame_grid() -> None:
    """
    Configures the grid of the 'bottom frame' of the rehearsal run result view.

    Args:
        None

    Returns:
        None
    """

    pass


def _configure_center_frame_grid() -> None:
    """
    Configures the grid of the 'center frame' of the rehearsal run result view.

    Args:
        None

    Returns:
        None
    """

    pass


def _configure_top_frame_grid() -> None:
    """
    Configures the grid of the 'top frame' of the rehearsal run result view.

    Args:
        None

    Returns:
        None
    """

    pass


def _configure_grid() -> None:
    """
    Configures the grid of the rehearsal run result view.

    Args:
        None

    Returns:
        None
    """

    _configure_bottom_frame_grid()
    _configure_center_frame_grid()
    _configure_top_frame_grid()


def _create_bottom_frame_widgets() -> None:
    """
    Creates the 'bottom frame' widgets of the rehearsal run result view.

    Args:
        None

    Returns:
        None
    """

    pass


def _create_center_frame_widgets() -> None:
    """
    Creates the 'center frame' widgets of the rehearsal run result view.

    Args:
        None

    Returns:
        None
    """

    pass


def _create_top_frame_widgets() -> None:
    """
    Creates the 'top frame' widgets of the rehearsal run result view.

    Args:
        None

    Returns:
        None
    """

    pass


def _create_widgets() -> None:
    """
    Creates the widgets of the rehearsal run result view.

    Args:
        None

    Returns:
        None
    """

    _create_bottom_frame_widgets()
    _create_center_frame_widgets()
    _create_top_frame_widgets()


def _get_rehearsal_run() -> ModelDict:
    """
    Returns the rehearsal run of the rehearsal run result view.

    Args:
        None

    Returns:
        ModelDict: The rehearsal run of the rehearsal run result view.

    Raises:
        ValueError: If the rehearsal run is not set.
    """

    if REHEARSAL_RUN is None:
        raise ValueError("Rehearsal is not set. Run '_set_rehearsal_run' method first.")

    return REHEARSAL_RUN


def _on_destroy() -> None:
    """
    Handles the 'DESTROY_REHEARSAL_RUN_VIEW' event.

    Args:
        None

    Returns:
        None
    """

    _unsubscribe_from_events()

    SUBSCRIPTION_IDS.clear()


def _set_rehearsal_run(model_dict: ModelDict) -> None:
    """
    Sets the rehearsal run for the rehearsal run result view.

    Args:
        model_dict (ModelDict): The rehearsal run to be set.

    Returns:
        None
    """

    global REHEARSAL_RUN

    REHEARSAL_RUN = model_dict


def _subscribe_to_events() -> None:
    """
    Subscribes to events in the rehearsal run result view.

    Args:
        None

    Returns:
        None
    """

    subscriptions: list[dict[str, Any]] = [
        {
            "event": DESTROY_REHEARSAL_RUN_RESULT_VIEW,
            "function": _on_destroy,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        }
    ]

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

    log_info(message="Subscribed to events in the rehearsal run result view.")


def _unsubscribe_from_events() -> None:
    """
    Unsubscribes from events in the rehearsal run result view.

    Args:
        None

    Returns:
        None
    """

    for uuid in SUBSCRIPTION_IDS:
        unsubscribe(uuid=uuid)

    log_info(message="Unsubscribed from all events in the rehearsal run result view.")


# ---------- Public Functions ---------- #


def get_rehearsal_run_result_view(rehearsal_run: ModelDict) -> None:
    """
    Gets the rehearsal run result view of the application.

    Args:
        rehearsal_run (ModelDict): The rehearsal run to be displayed.

    Returns:
        None
    """

    try:
        _set_rehearsal_run(model_dict=rehearsal_run)

        clear_frames()
        reset_frame_grids()

        _configure_grid()
        _create_widgets()
        _subscribe_to_events()
    except Exception as e:
        log_error(
            message=f"Failed to get rehearsal run result view: {e}",
        )
