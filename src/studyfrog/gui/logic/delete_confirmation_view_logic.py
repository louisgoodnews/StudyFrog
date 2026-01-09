"""
Author: Louis Goodnews
Date: 2026-01-05
Description: The logic of the delete confirmation view of the application.
"""

import customtkinter as ctk

from typing import Any, Final, Literal

from constants.common import GLOBAL
from constants.events import (
    DELETE_FLASHCARD_FROM_DB,
    DELETE_STACK_FROM_DB,
    DESTROY_DELETE_CONFIRMATION_VIEW,
    GET_INFO_TOAST,
)
from utils.common import exists, pluralize_word, string_to_snake_case
from utils.dispatcher import dispatch


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "on_cancel_button_click",
    "on_okay_button_click",
]


# ---------- Constants ---------- #


# ---------- Helper Functions ---------- #


# ---------- Private Functions ---------- #


def _has_sub_models(dictionary: dict[str, Any]) -> bool:
    """
    Determines if a passed module dictionary has any sub modules, such as items.

    Args:
        dictionary (dict[str, Any]): The dictionary to check.

    Returns:
        bool: True if the dictionary has sub modules, False otherwise.
    """

    if not exists(
        value=dictionary.get(
            "items",
            None,
        )
    ):
        return False

    return True


# ---------- Public Functions ---------- #


def on_cancel_button_click() -> None:
    """
    Handles the 'cancel' button click.

    Args:
        None

    Returns:
        None
    """

    dispatch(
        event=DESTROY_DELETE_CONFIRMATION_VIEW,
        namespace=GLOBAL,
    )


def on_okay_button_click(obj: dict[str, Any]) -> None:
    """
    Handles the 'okay' button click.

    Args:
        obj (dict[str, Any]): The object of which the deletion to perform.

    Returns:
        None
    """

    type_to_delete_event: dict[
        Literal[
            "flashcard",
            "stack",
        ],
        str,
    ] = {
        "flashcard": DELETE_FLASHCARD_FROM_DB,
        "stack": DELETE_STACK_FROM_DB,
    }

    if _has_sub_models(dictionary=obj):
        pass
    else:
        dispatch(
            event=type_to_delete_event[string_to_snake_case(string=obj["metadata"]["type"])],
            id_=obj["metadata"]["id"],
            namespace=GLOBAL,
            table_name=pluralize_word(word=string_to_snake_case(string=obj["metadata"]["type"])),
        )

    dispatch(
        event=DESTROY_DELETE_CONFIRMATION_VIEW,
        namespace=GLOBAL,
    )

    dispatch(
        event=GET_INFO_TOAST,
        message=f"{obj['metadata']['key']} deleted successfully",
        namespace=GLOBAL,
        title=f"{obj['metadata']['type'].title()} Deleted",
    )
