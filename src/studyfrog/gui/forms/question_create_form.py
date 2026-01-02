"""
Author: Louis Goodnews
Date: 2025-12-13
Description: The question create form of the application.
"""

import customtkinter as ctk

from tkinter.constants import NSEW
from typing import Any, Final

from utils.logging import log_error, log_info


# ---------- Exports ---------- #


__all__: Final[list[str]] = ["get_question_create_form"]


# ---------- Constants ---------- #


FORM: Final[dict[str, Any]] = {}

SUBSCRIPTION_IDS: Final[list[str]] = []


# ---------- Helper Functions ---------- #


# ---------- Private Functions ---------- #


# ---------- Public Functions ---------- #


def get_question_create_form(scrollable_frame: ctk.CTkScrollableFrame) -> None:
    """
    Gets the question create form.

    Args:
        scrollable_frame (ctk.CTkScrollableFrame): The scrollable frame to add the form to.

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    try:
        pass
    except Exception as e:
        log_error(message=f"Failed to get question create form: {e}")
        raise e
