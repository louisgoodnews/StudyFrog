"""
Author: Louis Goodnews
Date: 2025-12-13
Description: The answer create form of the application.
"""

import customtkinter as ctk

from tkinter.constants import NSEW
from typing import Any, Final

from utils.logging import log_error, log_info


# ---------- Exports ---------- #


__all__: Final[list[str]] = [
    "get_answer_create_form",
    "get_answer_choice_create_form",
    "get_answer_open_ended_create_form",
    "get_answer_true_false_create_form",
]


# ---------- Constants ---------- #


FORM: Final[dict[str, Any]] = {}

SUBSCRIPTION_IDS: Final[list[str]] = []


# ---------- Helper Functions ---------- #


# ---------- Private Functions ---------- #


# ---------- Public Functions ---------- #


def get_answer_create_form(scrollable_frame: ctk.CTkScrollableFrame) -> None:
    """
    Gets the answer create form.

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
        log_error(message=f"Failed to get answer create form: {e}")
        raise e


def get_answer_choice_create_form(scrollable_frame: ctk.CTkScrollableFrame) -> None:
    """
    Gets the answer choice create form.

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
        log_error(message=f"Failed to get answer choice create form: {e}")
        raise e


def get_answer_open_ended_create_form(scrollable_frame: ctk.CTkScrollableFrame) -> None:
    """
    Gets the answer open ended create form.

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
        log_error(message=f"Failed to get answer open ended create form: {e}")
        raise e


def get_answer_true_false_create_form(scrollable_frame: ctk.CTkScrollableFrame) -> None:
    """
    Gets the answer true false create form.

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
        log_error(message=f"Failed to get answer true false create form: {e}")
        raise e
