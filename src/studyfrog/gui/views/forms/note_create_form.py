"""
Author: Louis Goodnews
Date: 2025-11-16
"""

import tkinter

from tkinter.constants import NSEW
from typing import Any, Final, Literal, Union

from common.events import (
    GET_FORM,
    CALL_FUNCTION,
    GET_ALL_DIFFICULTIES,
    GET_ALL_PRIORITIES,
    GET_ALL_STACKS,
)
from gui.factory import get_entry, get_label, get_scrolled_text
from utils.utils import (
    destroy_widget_children,
    is_list_empty,
    log_exception,
    log_info,
    log_warning,
    publish_event,
    register_subscription,
    unsubscribe_subscription,
)


# ---------- Constants ---------- #

DIFFICULTIES: Final[list[dict[str, Any]]] = []

FORM_VARIABLES: Final[dict[str, dict[str, Union[bool, tkinter.Variable]]]] = {}

NAME: Final[Literal["gui.views.forms.note_create_form"]] = "gui.views.forms.note_create_form"

PRIORITIES: Final[list[dict[str, Any]]] = []

STACKS: Final[list[dict[str, Any]]] = []

SUBSCRIPTIONS: Final[list[str]] = []


# ---------- Functions ---------- #


def clear_master_frame(master: tkinter.Frame) -> None:
    """
    Clear the master frame.

    Args:
        master (tkinter.Frame): The master frame.

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    try:
        destroy_widget_children(master)
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to clear master frame",
            name=NAME,
        )
        raise Exception(f"Failed to clear master frame: {e}") from e


def configure_master_grid(master: tkinter.Frame) -> None:
    """
    Configure the master grid.

    Args:
        master (tkinter.Frame): The master frame.

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    try:
        master.grid_columnconfigure(
            index=0,
            weight=0,
        )
        master.grid_columnconfigure(
            index=1,
            weight=1,
        )
        master.grid_rowconfigure(
            index=0,
            weight=0,
        )
        master.grid_rowconfigure(
            index=1,
            weight=1,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to configure master grid",
            name=NAME,
        )
        raise Exception(f"Failed to configure master grid: {e}") from e


def create_widgets(master: tkinter.Frame) -> None:
    """
    Create the widgets.

    Args:
        master (tkinter.Frame): The master frame.

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    try:
        title_label: tkinter.Label = get_label(
            master=master,
            text="Title*:",
        )

        title_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        title_var: tkinter.StringVar = tkinter.StringVar()

        FORM_VARIABLES["title"] = {
            "is_required": True,
            "variable": title_var,
        }

        title_entry: tkinter.Entry = get_entry(
            master=master,
            textvariable=title_var,
        )

        title_entry.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        text_label: tkinter.Label = get_label(
            master=master,
            text="Text*:",
        )

        text_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )

        text_var: tkinter.StringVar = tkinter.StringVar()

        FORM_VARIABLES["text"] = {
            "is_required": True,
            "variable": text_var,
        }

        text_entry: dict[str, tkinter.Widget] = get_scrolled_text(master=master)

        text_entry["root"].grid(
            column=1,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )

        text_entry["text"].configure(height=10)

        text_entry["text"].bind(
            add="+",
            func=lambda event: text_var.set(
                value=text_entry["text"]
                .get(
                    index1="1.0",
                    index2="end-1c",
                )
                .strip()
            ),
            sequence="<KeyRelease>",
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to create widgets",
            name=NAME,
        )
        raise Exception(f"Failed to create widgets: {e}") from e


def get_difficulties() -> list[str]:
    """
    Get the difficulties.

    Args:
        None

    Returns:
        list[str]: The difficulties.

    Raises:
        Exception: If an error occurs.
    """

    if is_list_empty(list_=DIFFICULTIES):
        raise Exception(
            "Difficulties are empty. Check the logs for errors as this should not be happening."
        )

    return DIFFICULTIES


def get_form() -> dict[str, Any]:
    """
    Get the form.

    Args:
        None

    Returns:
        dict[str, Any]: The form.

    Raises:
        Exception: If an error occurs.
    """

    try:
        result: dict[str, Any] = {}

        for (
            key,
            value,
        ) in FORM_VARIABLES.items():
            variable_value: str = value["variable"].get()

            if value["is_required"] and not variable_value:
                raise ValueError(f"Required field '{key}' is empty")

            result[key] = variable_value

        result["difficulty"] = next(
            (
                difficulty.get("key")
                for difficulty in get_difficulties()
                if difficulty.get("name") == result.get("difficulty")
            ),
        )

        result["priority"] = next(
            (
                priority.get("key")
                for priority in get_priorities()
                if priority.get("name") == result.get("priority")
            ),
        )

        result["stack"] = next(
            (
                stack.get("key")
                for stack in get_stacks()
                if stack.get("name") == result.get("stack")
            ),
        )

        return result
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get form",
            name=NAME,
        )
        raise Exception(f"Failed to get form: {e}") from e


def get_note_create_form(master: tkinter.Frame) -> None:
    """
    Get the note create form.

    Args:
        master (tkinter.Frame): The master frame.

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    try:
        log_info(
            message="Getting note create form",
            name=NAME,
        )

        clear_master_frame(master=master)
        configure_master_grid(master=master)
        create_widgets(master=master)

        subscribe()

        log_info(
            message="Got note create form successfully",
            name=NAME,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get note create form",
            name=NAME,
        )
        raise Exception(f"Failed to get note create form: {e}") from e


def get_priorities() -> list[dict[str, Any]]:
    """
    Get the priorities.

    Args:
        None

    Returns:
        list[dict[str, Any]]: The priorities.

    Raises:
        Exception: If an error occurs.
    """

    if is_list_empty(list_=PRIORITIES):
        raise Exception(
            "Priorities are empty. Check the logs for errors as this should not be happening."
        )

    return PRIORITIES


def get_stacks() -> list[dict[str, Any]]:
    """
    Get the stacks.

    Args:
        None

    Returns:
        list[dict[str, Any]]: The stacks.

    Raises:
        Exception: If an error occurs.
    """

    if is_list_empty(list_=STACKS):
        log_warning(
            message="Stacks are empty. Check the logs for additional warnings. StudyFrog will still function though.",
            name=NAME,
        )

    return STACKS


def handle_destruction() -> None:
    """
    Handles the destruction of the form.

    This function is called when the form is destroyed.
    It unsubscribes from the events and clears the variables.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    try:
        FORM_VARIABLES.clear()
        unsubscribe()
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to handle destruction",
            name=NAME,
        )
        raise Exception(f"Failed to handle destruction: {e}") from e


def load_difficulties() -> list[dict[str, Any]]:
    """
    Load the difficulties.

    Args:
        None

    Returns:
        list[dict[str, Any]]: The difficulties.

    Raises:
        Exception: If an error occurs.
    """

    try:
        return list(
            publish_event(
                event=GET_ALL_DIFFICULTIES,
                namespace="GLOBAL",
            )
            .get("get_all_entries")[0]
            .get("result")
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to load difficulties",
            name=NAME,
        )
        raise Exception(f"Failed to load difficulties: {e}") from e


def load_priorities() -> list[dict[str, Any]]:
    """
    Load the priorities.

    Args:
        None

    Returns:
        list[dict[str, Any]]: The priorities.

    Raises:
        Exception: If an error occurs.
    """

    try:
        return list(
            publish_event(
                event=GET_ALL_PRIORITIES,
                namespace="GLOBAL",
            )
            .get("get_all_entries")[0]
            .get("result")
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to load priorities",
            name=NAME,
        )
        raise Exception(f"Failed to load priorities: {e}") from e


def load_stacks() -> list[dict[str, Any]]:
    """
    Load the stacks.

    Args:
        None

    Returns:
        list[dict[str, Any]]: The stacks.

    Raises:
        Exception: If an error occurs.
    """

    try:
        return list(
            publish_event(
                event=GET_ALL_STACKS,
                namespace="GLOBAL",
            )
            .get("get_all_entries")[0]
            .get("result")
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to load stacks",
            name=NAME,
        )
        raise Exception(f"Failed to load stacks: {e}") from e


def on_call_function(
    function: str,
    *args,
    **kwargs,
) -> Any:
    """
    Handle the call function event.

    Calls a function by name with the provided arguments.

    Args:
        function (str): The function name to call.

    Returns:
        Any: The result.

    Raises:
        Exception: If an error occurs.
    """

    try:
        value: Any = globals().get(function)

        if not callable(value):
            raise Exception(f"Attribute '{function}' is not callable")

        return value(
            *args,
            **kwargs,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to handle call function event",
            name=NAME,
        )
        raise Exception(f"Failed to handle call function event: {e}") from e


def on_call_functions(
    functions: list[str],
    *args,
    **kwargs,
) -> list[Any]:
    """
    Handle the call functions event.

    Calls multiple functions sequentially.

    Args:
        functions (list[str]): The list of function names to call.
        *args: Positional arguments to pass to each function.
        **kwargs: Keyword arguments to pass to each function.

    Returns:
        list[Any]: The list of results from each function call.

    Raises:
        Exception: If an error occurs during function execution.
    """

    try:
        results: list[Any] = []

        for function in functions:
            result: Any = on_call_function(
                function=function,
                *args,
                **kwargs,
            )

            results.append(result)
        return results
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to call functions",
            name=NAME,
        )
        raise Exception(f"Failed to call functions: {e}") from e


def on_get_form() -> dict[str, Any]:
    """
    Handle the get form event.

    Args:
        None

    Returns:
        dict[str, Any]: The form.

    Raises:
        Exception: If an error occurs.
    """

    try:
        return get_form()
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to handle get form event",
            name=NAME,
        )
        raise Exception(f"Failed to handle get form event: {e}") from e


def on_get_form() -> dict[str, Any]:
    """
    Handle the get form event.

    Args:
        None

    Returns:
        dict[str, Any]: The form.

    Raises:
        Exception: If an error occurs.
    """

    try:
        return get_form()
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to handle get form event",
            name=NAME,
        )
        raise Exception(f"Failed to handle get form event: {e}") from e


def set_difficulties(difficulties: list[dict[str, Any]]) -> None:
    """
    Set the difficulties.

    Args:
        difficulties (list[dict[str, Any]]): The difficulties.

    Returns:
        None
    """

    DIFFICULTIES.extend(difficulties)


def set_priorities(priorities: list[dict[str, Any]]) -> None:
    """
    Set the priorities.

    Args:
        priorities (list[dict[str, Any]]): The priorities.

    Returns:
        None
    """

    PRIORITIES.extend(priorities)


def set_stacks(stacks: list[dict[str, Any]]) -> None:
    """
    Set the stacks.

    Args:
        stacks (list[dict[str, Any]]): The stacks.

    Returns:
        None
    """

    STACKS.extend(stacks)


def subscribe() -> None:
    """
    Subscribe to various events.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    try:
        SUBSCRIPTIONS.append(
            register_subscription(
                event=GET_FORM,
                function=on_get_form,
                namespace="NOTE_CREATE_FORM",
                persistent=True,
            )
        )

        SUBSCRIPTIONS.append(
            register_subscription(
                event=CALL_FUNCTION,
                function=on_call_function,
                namespace="NOTE_CREATE_FORM",
                persistent=True,
            )
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to subscribe",
            name=NAME,
        )
        raise Exception(f"Failed to subscribe: {e}") from e


def unsubscribe() -> None:
    """
    Unsubscribe from various events.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    try:
        for subscription in SUBSCRIPTIONS:
            unsubscribe_subscription(uuid=subscription)
        SUBSCRIPTIONS.clear()
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to unsubscribe",
            name=NAME,
        )
        raise Exception(f"Failed to unsubscribe: {e}") from e


# ---------- Auto-Export ---------- #

# Auto-export all non-private symbols
__all__: Final[list[str]] = [
    key
    for (
        key,
        value,
    ) in globals().items()
    if not key.startswith("_") and callable(value)
]
