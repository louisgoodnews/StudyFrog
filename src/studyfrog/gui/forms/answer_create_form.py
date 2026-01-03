"""
Author: Louis Goodnews
Date: 2025-12-13
Description: The answer create form of the application.
"""

import customtkinter as ctk

from tkinter.constants import BOTTOM, CENTER, FALSE, NONE, NSEW, TOP, W, X, YES
from typing import Any, Final, Optional, Union

from constants.common import GLOBAL
from constants.events import DESTROY_ANSWER_CREATE_FORM, GET_CREATE_FORM
from utils.dispatcher import subscribe, unsubscribe
from utils.gui import destroy_widget_children, reset_widget_grid
from utils.logging import log_error, log_info


# ---------- Exports ---------- #


__all__: Final[list[str]] = [
    "get_answer_choice_create_form",
    "get_answer_open_ended_create_form",
    "get_answer_true_false_create_form",
]


# ---------- Constants ---------- #

_ANSWERS: Final[dict[int, Any]] = {}

_CONTAINER: Optional[ctk.CTkScrollableFrame] = None

_FORM: Final[dict[str, Any]] = {}

_MASTER: Optional[ctk.CTkFrame] = None

_SUBSCRIPTION_IDS: Final[list[str]] = []


# ---------- Helper Functions ---------- #


def _append_answer(answer: dict[str, Any]) -> int:
    """
    Appends a passed answer dictionary to the list of answers.

    Args:
        answer (dict[str, Any]): The answer dictionary to add to the list of answers.

    Returns:
        int: The index at which the answer was added.
    """

    index: int = max(
        _ANSWERS.keys(),
        default=0,
    )

    _ANSWERS[index] = answer

    return index


def _get_answers() -> dict[int, Any]:
    """
    Returns the list of answers 'serializing' the UI.

    Args:
        None

    Returns:
        dict[int, Any]: The dictionary of answers 'serializing' the UI.
    """

    return _ANSWERS


def _get_container() -> ctk.CTkScrollableFrame:
    """
    Returns the ctk.CTkScrollableFrame container widget.

    Args:
        None

    Returns:
        ctk.CTkScrollableFrame: The container frame widget.
    """

    if _CONTAINER is None:
        raise ValueError(
            "Container is None. Please provide a container frame (call '_set_container' function first)."
        )

    return _CONTAINER


def _get_form() -> dict[str, Any]:
    """
    Returns the underlying dictionary 'serializing' the UI form.

    Args:
        None

    Returns:
        dict[str, Any]: The underlying dictionary 'serializing' the UI form.
    """

    return _FORM


def _get_form_content() -> dict[str, Any]:
    """
    Returns the form content as a serialized dictionary.

    Args:
        None

    Returns:
        dict[str, Any]: The form content as a serialized dictionary.
    """

    result: dict[str, Any] = {
        "form_content": None,
        "origin": "answer_create_form",
    }

    if _get_answers():
        result["form_content"] = [
            {
                key: {
                    "is_correct": value["is_correct"].get(),
                    "is_required": value["is_required"],
                    "value": value["variable"].get(),
                }
            }
            for (
                key,
                value,
            ) in _get_answers().items()
        ]
    elif _get_form():
        result["form_content"] = [
            {
                key: {
                    "is_correct": value["is_correct"].get(),
                    "is_required": value["is_required"],
                    "value": value["variable"].get(),
                }
            }
            for (
                key,
                value,
            ) in _get_form().items()
        ]

    return result


def _get_master() -> ctk.CTkFrame:
    """
    Returns the ctk.CTkFrame master widget.

    Args:
        None

    Returns:
        ctk.CTkFrame: The master frame widget.
    """

    if _MASTER is None:
        raise ValueError(
            "Master is None. Please provide a master frame (call '_set_master' function first)."
        )

    return _MASTER


def _remove_answer(index: int) -> bool:
    """
    Removes the answer located at the given index.

    Args:
        index (int): The index at which to remove the answer.

    Returns:
        bool: Returns True if the answer was removed successfully, False otherwise.
    """

    if index not in _ANSWERS:
        return False

    del _ANSWERS[index]

    return True


def _set_container(container: ctk.CTkScrollableFrame) -> None:
    """
    Sets the ctk.CTkScrollableFrame container widget.

    Args:
        container (ctk.CTkScrollableFrame): The container frame to add the form to.

    Returns:
        None
    """

    global _CONTAINER

    _CONTAINER = container

    log_info(message="ctk.CTkScrollableFrame container widget set successfully.")


def _set_master(master: ctk.CTkFrame) -> None:
    """
    Sets the ctk.CTkFrame master widget.

    Args:
        master (ctk.CTkFrame): The master frame to add the form to.

    Returns:
        None
    """

    global _MASTER

    _MASTER = master

    log_info(message="ctk.CTkFrame master widget set successfully.")


def _update_form(
    key: Union[list[str], str],
    value: Any,
) -> None:
    """
    Updates the underlying dictionary 'serializing' the UI form with the passed key and value pairs.

    Args:
        key (Union[list[str], str]): The key(s) to update with the passed value.
        value (Any): The value to update the passed key(s) with.

    Returns:
        None
    """

    if isinstance(
        key,
        list,
    ):
        for _key in key:
            _get_form()[_key] = value

        return

    _get_form()[key] = value


# ---------- Private Functions ---------- #


def _clear_master() -> None:
    """
    Clears the ctk.CTkFrame master widget.

    Args:
        None

    Returns:
        None
    """

    destroy_widget_children(widget=_get_master())


def _configure_choice_grid() -> None:
    """
    Configures the ctk.CTkFrame master widget's grid.

    Args:
        None

    Returns:
        None
    """

    _get_master().grid_columnconfigure(
        index=0,
        weight=1,
    )
    _get_master().grid_rowconfigure(
        index=0,
        weight=1,
    )


def _configure_open_ended_grid() -> None:
    """
    Configures the ctk.CTkFrame master widget's grid.

    Args:
        None

    Returns:
        None
    """

    _get_master().grid_columnconfigure(
        index=0,
        weight=0,
    )
    _get_master().grid_columnconfigure(
        index=1,
        weight=1,
    )
    _get_master().grid_rowconfigure(
        index=0,
        weight=1,
    )


def _configure_true_false_grid() -> None:
    """
    Configures the ctk.CTkFrame master widget's grid.

    Args:
        None

    Returns:
        None
    """

    _get_master().grid_columnconfigure(
        index=0,
        weight=0,
    )
    _get_master().grid_columnconfigure(
        index=1,
        weight=1,
    )
    _get_master().grid_rowconfigure(
        index=0,
        weight=1,
    )


def _create_choice_widgets() -> None:
    """
    Creates the widgets of the answer choice create form.

    Args:
        None

    Returns:
        None
    """

    scrollable_frame: ctk.CTkScrollableFrame = ctk.CTkScrollableFrame(master=_get_master())

    scrollable_frame.grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    _set_container(container=scrollable_frame)

    ctk.CTkButton(
        command=_on_add_answer_button_click,
        master=_get_container(),
        text="Add answer",
    ).pack(
        anchor=CENTER,
        expand=FALSE,
        fill=NONE,
        padx=5,
        pady=5,
        side=BOTTOM,
    )


def _create_open_ended_widgets() -> None:
    """
    Creates the widgets of the answer open ended create form.

    Args:
        None

    Returns:
        None
    """

    ctk.CTkLabel(
        anchor=W,
        font=(
            "Helvetica",
            12,
            "bold",
        ),
        master=_get_master(),
        text="Provide the correct answer*: ",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    _update_form(
        key="answer",
        value={
            "is_correct": ctk.BooleanVar(value=False),
            "is_required": True,
            "variable": ctk.StringVar(value=""),
        },
    )

    text_box: ctk.CTkTextbox = ctk.CTkTextbox(master=_get_master())

    text_box.grid(
        column=1,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    text_box.bind(
        command=lambda event: _get_form()["answer"]["variable"].set(
            value=text_box.get(
                index1="1.0",
                index2="end-1c",
            )
        ),
        sequence="<KeyRelease>",
    )


def _create_true_false_widgets() -> None:
    """
    Creates the widgets of the answer true false create form.

    Args:
        None

    Returns:
        None
    """

    ctk.CTkLabel(
        anchor=W,
        font=(
            "Helvetica",
            12,
            "bold",
        ),
        master=_get_master(),
        text="Set the correct answer*: ",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    _update_form(
        key="correct_answer",
        value={
            "is_correct": ctk.BooleanVar(value=True),
            "is_required": True,
            "variable": ctk.StringVar(value="True"),
        },
    )

    ctk.CTkSegmentedButton(
        master=_get_master(),
        values=[
            "True",
            "False",
        ],
        variable=_get_form()["correct_answer"]["variable"],
    ).grid(
        column=1,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )


def _on_add_answer_button_click() -> None:
    """
    Handles the click event of the 'add answer' button.

    Args:
        None

    Returns:
        None
    """

    def _on_remove_button_click() -> None:
        """
        Handles the click event of the 'remove' button.

        Args:
            None

        Returns:
            None
        """

        frame.destroy()

        _remove_answer(index=index)

    answer: dict[str, Any] = {
        "is_correct": ctk.BooleanVar(value=False),
        "is_required": True,
        "variable": ctk.StringVar(value=""),
    }

    index: int = _append_answer(answer=answer)

    frame: ctk.CTkFrame = ctk.CTkFrame(master=_get_container())

    frame.grid_columnconfigure(
        index=0,
        weight=0,
    )
    frame.grid_columnconfigure(
        index=1,
        weight=1,
    )
    frame.grid_columnconfigure(
        index=2,
        weight=0,
    )
    frame.grid_columnconfigure(
        index=3,
        weight=0,
    )
    frame.grid_columnconfigure(
        index=4,
        weight=0,
    )
    frame.grid_rowconfigure(
        index=0,
        weight=1,
    )

    frame.pack(
        expand=YES,
        fill=X,
        padx=5,
        pady=5,
        side=TOP,
    )

    ctk.CTkLabel(
        anchor=W,
        font=(
            "Helvetica",
            12,
            "bold",
        ),
        master=frame,
        text="Answer text': ",
    ).grid(
        column=0,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    ctk.CTkEntry(
        font=(
            "Helvetica",
            12,
        ),
        master=frame,
        placeholder_text="Enter your answer text here",
        textvariable=answer["variable"],
    ).grid(
        column=1,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    ctk.CTkCheckBox(
        font=(
            "Helvetica",
            12,
            "bold",
        ),
        master=frame,
        text="Is answer correct?* ",
        variable=answer["is_correct"],
    ).grid(
        column=2,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    ctk.CTkButton(
        command=lambda: (
            answer["variable"].set(value=""),
            answer["is_correct"].set(value=False),
        ),
        master=frame,
        text="Clear",
    ).grid(
        column=3,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )

    ctk.CTkButton(
        command=_on_remove_button_click,
        master=frame,
        text="Remove",
    ).grid(
        column=4,
        padx=5,
        pady=5,
        row=0,
        sticky=NSEW,
    )


def _on_destroy() -> None:
    """
    Handles the 'DESTROY_ANSWER_CREATE_FORM' event.

    Args:
        None

    Returns:
        None
    """

    global _MASTER

    _unsubscribe_from_events()

    _MASTER = None

    _ANSWERS.clear()

    _FORM.clear()


def _on_get_create_form() -> dict[str, Any]:
    """
    Handles the 'GET_CREATE_FORM' event.

    Args:
        None

    Returns:
        dict[str, Any]: The form.
    """

    return _get_form_content()


def _subscribe_to_events() -> None:
    """
    Subscribes to events for the answer create form.

    Agrs:
        None

    Returns:
        None
    """

    subscriptions: list[dict[str, Any]] = [
        {
            "event": DESTROY_ANSWER_CREATE_FORM,
            "function": _on_destroy,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
        {
            "event": GET_CREATE_FORM,
            "function": _on_get_create_form,
            "namespace": GLOBAL,
            "persistent": True,
            "priority": 100,
        },
    ]

    for subscription in subscriptions:
        _SUBSCRIPTION_IDS.append(
            subscribe(
                event=subscription["event"],
                function=subscription["function"],
                namespace=subscription["namespace"],
                persistent=subscription["persistent"],
                priority=subscription["priority"],
            )
        )


def _unsubscribe_from_events() -> None:
    """
    Unsubscribes from events for the answer create form.

    Agrs:
        None

    Returns:
        None
    """

    for uuid in _SUBSCRIPTION_IDS:
        unsubscribe(uuid=uuid)

    log_info(message="Unsubscribed from all events for the answer create form.")

    _SUBSCRIPTION_IDS.clear()


# ---------- Public Functions ---------- #


def get_answer_choice_create_form(frame: ctk.CTkFrame) -> None:
    """
    Gets the answer choice create form.

    Args:
        frame (ctk.CTkFrame): The frame to add the form to.

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    try:
        _set_master(master=frame)
        _clear_master()

        reset_widget_grid(widget=_get_master())

        _configure_choice_grid()
        _create_choice_widgets()
        _subscribe_to_events()
    except Exception as e:
        log_error(message=f"Failed to get answer choice create form: {e}")
        raise e


def get_answer_open_ended_create_form(frame: ctk.CTkFrame) -> None:
    """
    Gets the answer open ended create form.

    Args:
        frame (ctk.CTkFrame): The frame to add the form to.

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    try:
        _set_master(master=frame)
        _clear_master()

        reset_widget_grid(widget=_get_master())

        _configure_open_ended_grid()
        _create_open_ended_widgets()
        _subscribe_to_events()
    except Exception as e:
        log_error(message=f"Failed to get answer open ended create form: {e}")
        raise e


def get_answer_true_false_create_form(frame: ctk.CTkFrame) -> None:
    """
    Gets the answer true false create form.

    Args:
        frame (ctk.CTkFrame): The frame to add the form to.

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    try:
        _set_master(master=frame)
        _clear_master()

        reset_widget_grid(widget=_get_master())

        _configure_true_false_grid()
        _create_true_false_widgets()
        _subscribe_to_events()
    except Exception as e:
        log_error(message=f"Failed to get answer true false create form: {e}")
        raise e
