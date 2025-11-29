"""
Author: Louis Goodnews
Date: 2025-11-16
"""

import tkinter

from typing import Any, Final, Literal, TypeAlias, Union

from utils.utils import destroy_widget_children, log_exception, log_info


# ---------- Types ---------- #

QuestionTypes: TypeAlias = Literal[
    "multiple_choice",
    "multiple_select",
    "open_ended",
    "single_choice",
    "single_select",
    "true_false",
]

# ---------- Constants ---------- #

DIFFICULTIES: Final[list[dict[str, Any]]] = []

FORM_VARIABLES: Final[dict[str, dict[str, Union[bool, tkinter.Variable]]]] = {}

NAME: Final[Literal["gui.views.forms.question_create_form"]] = (
    "gui.views.forms.question_create_form"
)

PRIORITIES: Final[list[dict[str, Any]]] = []

STACKS: Final[list[dict[str, Any]]] = []

SUBSCRIPTIONS: Final[list[str]] = []

SUBJECTS: Final[list[dict[str, Any]]] = []

TEACHERS: Final[list[dict[str, Any]]] = []


# ---------- Constants ---------- #

DIFFICULTIES: Final[list[dict[str, Any]]] = []

FORM_VARIABLES: Final[dict[str, dict[str, Union[bool, tkinter.Variable]]]] = {}

NAME: Final[Literal["gui.views.forms.question_create_form"]] = (
    "gui.views.forms.question_create_form"
)

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
        pass
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
        pass
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to create widgets",
            name=NAME,
        )
        raise Exception(f"Failed to create widgets: {e}") from e


def get_question_create_form(master: tkinter.Frame) -> None:
    """
    Get the question create form.

    Args:
        master (tkinter.Frame): The master frame.

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    try:
        log_info(
            message="Getting question create form",
            name=NAME,
        )

        clear_master_frame(master=master)
        configure_master_grid(master=master)
        create_widgets(master=master)

        log_info(
            message="Got question create form successfully",
            name=NAME,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get question create form",
            name=NAME,
        )
        raise Exception(f"Failed to get question create form: {e}") from e


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
                namespace="QUESTION_CREATE_FORM",
                persistent=False,
            )
        )
        SUBSCRIPTIONS.append(
            register_subscription(
                event=CALL_FUNCTION,
                function=on_call_function,
                namespace="QUESTION_CREATE_FORM",
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
