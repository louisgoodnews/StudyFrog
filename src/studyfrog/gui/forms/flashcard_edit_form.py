"""
Author: Louis Goodnews
Date: 2026-01-10
Description: The flashcard edit form of the application.
"""

import customtkinter as ctk

from typing import Any, Final, Optional

from constants.common import GLOBAL
from constants.events import DESTROY_FLASHCARD_EDIT_FORM
from utils.common import exists
from utils.dispatcher import subscribe, unsubscribe
from utils.logging import log_error


# ---------- Exports ---------- #


__all__: Final[list[str]] = ["get_flashcard_edit_form"]


# ---------- Constants ---------- #

_FORM_FRAME: Optional[ctk.CTkFrame] = None

_CUSTOMFIELDS_FRAME: Optional[ctk.CTkFrame] = None

_MASTER: Optional[ctk.CTkTabview] = None

_SuBSCRIPTION_IDS: Final[list[str]] = []


# ---------- Helper Functions ---------- #


def _append_subscription_id(uuid_: str) -> None:
    """
    Appends a subscription ID to the list of subscription IDs.
    
    Args:
        uuid_ (str): The subscription ID to append.
        
    Returns:
        None
    """

    _get_subscription_ids().append(uuid_)


def _clear_subscription_ids() -> None:
    """
    Clears the list of subscription IDs.

    Args:
        None
    
    Returns:
        None
    """

    _get_subscription_ids().clear()


def _get_customfields_frame() -> ctk.CTkFrame:
    """
    Retrieves the customfields frame for the flashcard edit form.

    Raises:
        ValueError: If the customfields frame has not been initialized yet.
            The method '_set_customfields_frame' must be executed first.

    Returns:
        ctk.CTkFrame: The customfields frame for the flashcard edit form.

    Raises:
        ValueError: If the customfields frame has not been initialized yet.
    """

    if not exists(value=_CUSTOMFIELDS_FRAME):
        raise ValueError("'customfields_frame' widget has not been initialized yet. Call the '_set_customfields_frame' function first.")

    return _CUSTOMFIELDS_FRAME


def _get_form_frame() -> ctk.CTkFrame:
    """
    Retrieves the form frame for the flashcard edit form.

    Raises:
        ValueError: If the form frame has not been initialized yet.
            The method '_set_form_frame' must be executed first.

    Returns:
        ctk.CTkFrame: The form frame for the flashcard edit form.

    Raises:
        ValueError: If the form frame has not been initialized yet.
    """

    if not exists(value=_FORM_FRAME):
        raise ValueError("'form_frame' widget has not been initialized yet. Call the '_set_form_frame' function first.")

    return _FORM_FRAME


def _get_master() -> ctk.CTkTabview:
    """
    Retrieves the master widget for the flashcard edit form.

    Raises:
        ValueError: If the master widget has not been initialized yet.
            The method '_set_master' must be executed first.

    Returns:
        ctk.CTkTabview: The master widget for the flashcard edit form.

    Raises:
        ValueError: If the master widget has not been initialized yet.
    """

    if not exists(value=_MASTER):
        raise ValueError("'master' widget has not been initialized yet. Call the '_set_master' function first.")

    return _MASTER


def _get_subscription_ids() -> list[str]:
    """
    Retrieves the list of subscription IDs.
    
    Returns:
        list[str]: The list of subscription IDs.
    """

    return _SuBSCRIPTION_IDS


def _set_customfields_frame(frame: ctk.CTkFrame) -> None:
    """
    Sets the customfields frame for the flashcard edit form.

    Args:
        frame (ctk.CTkFrame): The customfields frame for the flashcard edit form.

    Returns:
        None
    """

    global _CUSTOMFIELDS_FRAME

    if exists(value=_CUSTOMFIELDS_FRAME):
        return

    _CUSTOMFIELDS_FRAME = frame


def _set_form_frame(frame: ctk.CTkFrame) -> None:
    """
    Sets the form frame for the flashcard edit form.

    Args:
        frame (ctk.CTkFrame): The form frame for the flashcard edit form.

    Returns:
        None
    """

    global _FORM_FRAME

    if exists(value=_FORM_FRAME):
        return

    _FORM_FRAME = frame


def _set_master(tabview: ctk.CTkTabview) -> None:
    """
    Sets the master widget for the flashcard edit form.

    Args:
        tabview (ctk.CTkTabview): The master widget for the flashcard edit form.

    Returns:
        None
    """

    global _MASTER

    if exists(value=_MASTER):
        return

    _MASTER = tabview


# ---------- Private Functions ---------- #


def _create_widgets() -> None:
    """
    Creates the widgets of the flashcard edit form.

    Args:
        None

    Returns:
        None
    """

    pass


def _on_destroy() -> None:
    """
    Handles the 'DESTROY_FLASHCARD_EDIT_FORM' event.

    Clears the list of subscription IDs, and sets the form frame,
    customfields frame, and master widget for the flashcard edit form
    to None.

    Args:
        None

    Returns:
        None
    """

    global _FORM_FRAME, _CUSTOMFIELDS_FRAME, _MASTER

    _clear_subscription_ids()

    _FORM_FRAME = None
    _CUSTOMFIELDS_FRAME = None
    _MASTER = None


def _subscribe_to_events() -> None:
    """
    Subscribes to events for the flashcard edit form.

    Iterates through a list of subscriptions and calls
    `subscribe(event=subscription["event"], function=subscription["function"], namespace=subscription["namespace"], persistent=subscription["persistent"], priority=subscription["priority"])`
    for each subscription in the list, and adds the returned UUID
    to the list of subscription IDs.

    Args:
        None

    Returns:
        None
    """

    subscrptions: list[dict[str, Any]] = [
        {
            "event": DESTROY_FLASHCARD_EDIT_FORM,
            "function": _on_destroy,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        }
    ]

    for subscription in subscrptions:
        _append_subscription_id(
            uuid=subscribe(
                event=subscription["event"],
                function=subscription["function"],
                namespace=subscription["namespace"],
                persistent=subscription["persistent"],
                priority=subscription["priority"],
            )
        )


def _unsubscribe_from_events() -> None:
    """
    Unsubscribes from all currently active event subscriptions.

    Iterates through the subscription IDs returned by `_get_subscription_ids()`
    and calls `unsubscribe(uuid=uuid)` for each ID.

    Args:
        None

    Returns:
        None
    """

    for uuid in _get_subscription_ids():
        unsubscribe(uuid=uuid)

    _clear_subscription_ids()


# ---------- Public Functions ---------- #


def get_flashcard_edit_form(tabview: ctk.CTkTabview) -> ctk.CTkToplevel:
    """
    Gets the flashcard edit form.

    Args:
        tabview (ctk.CTkTabview): The tabview to add the form to.

    Returns:
        ctk.CTkToplevel: The toplevel window of the flashcard edit form.

    Raises:
        Exception: If an exception is caught while attempting to get the flashcard edit form.
    """

    try:
        _set_master(tabview=tabview)
        _create_widgets()
    except Exception as e:
        log_error(message=f"Caught an exception while attemping to run 'get_flashcard_edit_form': {e}")

        raise e
