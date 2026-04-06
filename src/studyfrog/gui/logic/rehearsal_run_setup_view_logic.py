"""
Author: Louis Goodnews
Date: 2025-12-19
Description: The logic of the rehearsal run setup view of the application.
"""

from __future__ import annotations

from typing import Any, Final, Optional

from studyfrog.constants.common import GLOBAL
from studyfrog.constants.events import (
    ADD_REHEARSAL_RUN_TO_DB,
    DESTROY_REHEARSAL_RUN_SETUP_VIEW,
    FILTER_DIFFICULTIES_FROM_DB,
    FILTER_PRIORITIES_FROM_DB,
    FILTER_STACKS_FROM_DB,
    GET_DASHBOARD_VIEW,
    GET_REHEARSAL_RUN_FROM_DB,
    GET_REHEARSAL_RUN_MODEL,
    GET_REHEARSAL_RUN_SETUP_FORM,
    GET_REHEARSAL_RUN_VIEW,
)
from studyfrog.models.models import Model
from studyfrog.utils.common import exists
from studyfrog.utils.dispatcher import dispatch
from studyfrog.utils.logging import log_debug, log_error


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "on_cancel_button_click",
    "on_start_button_click",
]


# ---------- Constants ---------- #


# ---------- Helper Functions ---------- #


def _filter_difficulty(**kwargs) -> Model:
    """
    Returns a difficulty matching the given criteria from the database.

    Args:
        **kwargs: The criteria to filter the difficulty by.

    Returns:
        Model: The difficulty matching the given criteria.
    """

    difficulties: Optional[list[Model]] = (
        dispatch(
            event=FILTER_DIFFICULTIES_FROM_DB,
            namespace=GLOBAL,
            table_name="difficulties",
            **kwargs,
        )
        .get(
            "filter_entries",
            [{}],
        )[0]
        .get(
            "result",
            [{}],
        )
    )

    if not difficulties:
        return {}

    return difficulties[0]


def _filter_priority(**kwargs) -> Model:
    """
    Returns a priority matching the given criteria from the database.

    Args:
        **kwargs: The criteria to filter the priority by.

    Returns:
        Model: The priority matching the given criteria.
    """

    priorities: Optional[list[Model]] = (
        dispatch(
            event=FILTER_PRIORITIES_FROM_DB,
            namespace=GLOBAL,
            table_name="priorities",
            **kwargs,
        )
        .get(
            "filter_entries",
            [{}],
        )[0]
        .get(
            "result",
            [{}],
        )
    )

    if not priorities:
        return {}

    return priorities[0]


def _filter_stack(**kwargs) -> Model:
    """
    Returns a stack matching the given criteria from the database.

    Args:
        **kwargs: The criteria to filter the stack by.

    Returns:
        Model: The stack matching the given criteria.
    """

    stacks: Optional[list[Model]] = (
        dispatch(
            event=FILTER_STACKS_FROM_DB,
            namespace=GLOBAL,
            table_name="stacks",
            **kwargs,
        )
        .get(
            "filter_entries",
            [{}],
        )[0]
        .get(
            "result",
            [{}],
        )
    )

    if not stacks:
        return {}

    return stacks[0]


def _handle_difficulty_data(data: str) -> str:
    """
    Handles the difficulty form data.

    Args:
        data (str): The difficulty data to handle.

    Returns:
        str: The processed difficulty data.
    """

    try:
        dificulty_data: list[Model] = _filter_difficulty(display_name=data)

        if not dificulty_data:
            return ""

        return dificulty_data[0].key
    except Exception as e:
        log_error(message=f"Failed to handle difficulty data: {e}")
        raise e


def _handle_priority_data(data: str) -> str:
    """
    Handles the priority form data.

    Args:
        data (str): The priority data to handle.

    Returns:
        str: The processed priority data.
    """

    try:
        priority_data: list[Model] = _filter_priority(display_name=data)

        if not priority_data:
            return ""

        return priority_data[0].key
    except Exception as e:
        log_error(message=f"Failed to handle priority data: {e}")
        raise e


def _handle_stacks_data(data: str) -> list[str]:
    """
    Handles the stack form data.

    Args:
        data (str): The stack data to handle.

    Returns:
        list[str]: The processed stack data (i.e. the keys of the stacks).
    """

    try:
        result: list[str] = []

        if ", " in data:
            data = data.split(", ")
        else:
            data = [data]

        for name in data:
            stack: Optional[Model] = _filter_stack(name=name)

            if not exists(value=stack):
                raise ValueError(f"Stack '{name}' not found.")

            key: Optional[str] = stack.key

            if not exists(value=key):
                raise ValueError(f"Failed to get key from metadata in stack '{name}'.")

            result.append(key)

            if stack.children:
                result.extend(stack.children)

        return result
    except Exception as e:
        log_error(message=f"Failed to handle stack data: {e}")
        raise e


def _verify_form_data(data: Model) -> None:
    """
    Verifies the form data for completeness.

    Args:
        data (Model): The form data.

    Returns:
        None

    Raises:
        Exception: If the form data is invalid.
    """

    try:
        for (
            key,
            value,
        ) in data.items():
            is_required: bool = value["is_required"]

            if is_required and not exists(value=value.get("value")):
                raise ValueError(
                    f"Form data is invalid. Missing value for '{key}' (got '{value.get('value', None)}' instead)."
                )
    except Exception as e:
        log_error(message=f"Failed to verify form data: {e}")
        raise e


# ---------- Private Functions ---------- #


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
        event=GET_DASHBOARD_VIEW,
        namespace=GLOBAL,
    )


def on_start_button_click() -> None:
    """
    Handles the 'start' button click.

    Args:
        None

    Returns:
        None
    """

    response: Optional[dict[str, Any]] = (
        dispatch(
            event=GET_REHEARSAL_RUN_SETUP_FORM,
            namespace=GLOBAL,
        )
        .get(
            "_on_get_rehearsal_run_setup_form",
            [{}],
        )[0]
        .get(
            "result",
            None,
        )
    )

    if not exists(value=response):
        log_error(message="Failed to get rehearsal run setup form")
        return

    _verify_form_data(data=response)

    response["difficulty"]["value"] = _handle_difficulty_data(data=response["difficulty"]["value"])
    response["priority"]["value"] = _handle_priority_data(data=response["priority"]["value"])
    response["stacks"]["value"] = _handle_stacks_data(data=response["stacks"]["value"])

    rehearsal_run_model: Model = (
        dispatch(
            event=GET_REHEARSAL_RUN_MODEL,
            filter_by_difficulty_enabled=bool(response["difficulty"]["value"]),
            filter_by_difficulty=response["difficulty"]["value"],
            filter_by_priority_enabled=bool(response["priority"]["value"]),
            filter_by_priority=response["priority"]["value"],
            item_order_randomization_enabled=bool(
                response["item_order_randomization_enabled"]["value"]
            ),
            namespace=GLOBAL,
            stacks=response["stacks"]["value"],
        )
        .get(
            "get_rehearsal_run_model",
            [{}],
        )[0]
        .get(
            "result",
            {},
        )
    )

    id: Optional[int] = (
        dispatch(
            model=rehearsal_run_model,
            event=ADD_REHEARSAL_RUN_TO_DB,
            force=True,
            namespace=GLOBAL,
            table_name="rehearsal_runs",
        )
        .get(
            "add_entry_if_not_exist",
            [{}],
        )[0]
        .get(
            "result",
            None,
        )
    )

    if not exists(value=id):
        log_error(message="Failed to add rehearsal run to database")
        return

    dispatch(
        event=DESTROY_REHEARSAL_RUN_SETUP_VIEW,
        namespace=GLOBAL,
    )

    dispatch(
        event=GET_REHEARSAL_RUN_VIEW,
        model=dispatch(
            event=GET_REHEARSAL_RUN_FROM_DB,
            id_=id,
            namespace=GLOBAL,
            table_name="rehearsal_runs",
        )
        .get(
            "get_entry",
            [{}],
        )[0]
        .get(
            "result",
            {},
        ),
        namespace=GLOBAL,
    )
