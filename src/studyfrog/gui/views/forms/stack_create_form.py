"""
Author: Louis Goodnews
Date: 2025-11-16
"""

import tkinter

from tkinter import ttk
from tkinter.constants import NSEW
from typing import Any, Final, Literal, Union

from common.events import (
    ADD_SUBJECT,
    ADD_TEACHER,
    CALL_FUNCTION,
    GET_ALL_DIFFICULTIES,
    GET_ALL_PRIORITIES,
    GET_ALL_STACKS,
    GET_ALL_SUBJECTS,
    GET_ALL_TEACHERS,
    GET_FORM,
    GET_SUBJECT,
    GET_TEACHER,
)
from core.models import get_subject_model, get_teacher_model
from gui.constants import READONLY
from gui.factory import get_combobox, get_entry, get_label, get_scrolled_text
from utils.utils import (
    destroy_widget_children,
    is_item_in_list,
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

NAME: Final[Literal["gui.views.forms.stack_create_form"]] = "gui.views.forms.stack_create_form"

NAMESPACE: Final[Literal["STACK_CREATE_FORM"]] = "STACK_CREATE_FORM"

PRIORITIES: Final[list[dict[str, Any]]] = []

STACKS: Final[list[dict[str, Any]]] = []

SUBJECTS: Final[list[dict[str, Any]]] = []

SUBSCRIPTIONS: Final[list[str]] = []

TEACHERS: Final[list[dict[str, Any]]] = []


# ---------- Functions ---------- #


def append_subject(subject: dict[str, Any]) -> None:
    """
    Append the subject.

    Args:
        subject (dict[str, Any]): The subject.

    Returns:
        None
    """

    SUBJECTS.append(subject)


def append_teacher(teacher: dict[str, Any]) -> None:
    """
    Append the teacher.

    Args:
        teacher (dict[str, Any]): The teacher.

    Returns:
        None
    """

    TEACHERS.append(teacher)


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
            weight=0,
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
        name_label: tkinter.Label = get_label(
            master=master,
            text="Name*: ",
        )

        name_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        name_var: tkinter.StringVar = tkinter.StringVar()

        name_entry: tkinter.Entry = get_entry(
            master=master,
            textvariable=name_var,
        )

        name_entry.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        FORM_VARIABLES["name"] = {
            "value": name_var,
            "is_required": True,
        }

        description_var: tkinter.StringVar = tkinter.StringVar()

        description_label: tkinter.Label = get_label(
            master=master,
            text="Description: ",
        )

        description_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )

        description_text: dict[str, tkinter.Widget] = get_scrolled_text(master=master)

        description_text["root"].grid(
            column=1,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )

        description_text["text"].configure(height=10)

        description_text["text"].bind(
            func=lambda event: description_var.set(
                value=description_text["text"].get(
                    "1.0",
                    "end-1c",
                )
            ),
            sequence="<KeyRelease>",
        )

        FORM_VARIABLES["description"] = {
            "value": description_var,
            "is_required": False,
        }

        difficulty_var: tkinter.StringVar = tkinter.StringVar()

        difficulty_label: tkinter.Label = get_label(
            master=master,
            text="Difficulty*: ",
        )

        difficulty_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=2,
            sticky=NSEW,
        )

        difficulty_combobox: ttk.Combobox = get_combobox(
            master=master,
            state=READONLY,
            textvariable=difficulty_var,
            values=[difficulty["name"] for difficulty in get_difficulties()],
        )

        difficulty_combobox.grid(
            column=1,
            padx=5,
            pady=5,
            row=2,
            sticky=NSEW,
        )

        difficulty_combobox.bind(
            func=lambda event: difficulty_var.set(value=difficulty_combobox.get()),
            sequence="<<ComboboxSelected>>",
        )

        FORM_VARIABLES["difficulty"] = {
            "value": difficulty_var,
            "is_required": True,
        }

        priority_var: tkinter.StringVar = tkinter.StringVar()

        priority_label: tkinter.Label = get_label(
            master=master,
            text="Priority*: ",
        )

        priority_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=3,
            sticky=NSEW,
        )

        priority_combobox: ttk.Combobox = get_combobox(
            master=master,
            state=READONLY,
            textvariable=priority_var,
            values=[priority["name"] for priority in get_priorities()],
        )

        priority_combobox.grid(
            column=1,
            padx=5,
            pady=5,
            row=3,
            sticky=NSEW,
        )

        priority_combobox.bind(
            func=lambda event: priority_var.set(value=priority_combobox.get()),
            sequence="<<ComboboxSelected>>",
        )

        FORM_VARIABLES["priority"] = {
            "value": priority_var,
            "is_required": True,
        }

        subject_var: tkinter.StringVar = tkinter.StringVar()

        subject_label: tkinter.Label = get_label(
            master=master,
            text="Subject: ",
        )

        subject_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=4,
            sticky=NSEW,
        )

        subject_combobox: ttk.Combobox = get_combobox(
            master=master,
            textvariable=subject_var,
            values=[subject["name"] for subject in get_subjects()],
        )

        subject_combobox.grid(
            column=1,
            padx=5,
            pady=5,
            row=4,
            sticky=NSEW,
        )

        subject_combobox.bind(
            func=lambda event: subject_var.set(value=subject_combobox.get()),
            sequence="<<ComboboxSelected>>",
        )

        subject_combobox.bind(
            func=lambda event: on_subject_combobox_return(
                combobox=subject_combobox,
                value=subject_var.get(),
            ),
            sequence="<Return>",
        )

        FORM_VARIABLES["subject"] = {
            "value": subject_var,
            "is_required": False,
        }

        teacher_var: tkinter.StringVar = tkinter.StringVar()

        teacher_label: tkinter.Label = get_label(
            master=master,
            text="Teacher: ",
        )

        teacher_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=5,
            sticky=NSEW,
        )

        teacher_combobox: ttk.Combobox = get_combobox(
            master=master,
            textvariable=teacher_var,
            values=[teacher["name"] for teacher in get_teachers()],
        )

        teacher_combobox.grid(
            column=1,
            padx=5,
            pady=5,
            row=5,
            sticky=NSEW,
        )

        teacher_combobox.bind(
            func=lambda event: teacher_var.set(value=teacher_combobox.get()),
            sequence="<<ComboboxSelected>>",
        )

        teacher_combobox.bind(
            func=lambda event: on_teacher_combobox_return(
                combobox=teacher_combobox,
                value=teacher_var.get(),
            ),
            sequence="<Return>",
        )

        FORM_VARIABLES["teacher"] = {
            "value": teacher_var,
            "is_required": False,
        }

        stack_var: tkinter.StringVar = tkinter.StringVar()

        stack_label: tkinter.Label = get_label(
            master=master,
            text="Stack: ",
        )

        stack_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=6,
            sticky=NSEW,
        )

        stack_combobox: ttk.Combobox = get_combobox(
            master=master,
            state=READONLY,
            textvariable=stack_var,
            values=[stack["name"] for stack in get_stacks()],
        )

        stack_combobox.grid(
            column=1,
            padx=5,
            pady=5,
            row=6,
            sticky=NSEW,
        )

        stack_combobox.bind(
            func=lambda event: stack_var.set(value=stack_combobox.get()),
            sequence="<<ComboboxSelected>>",
        )

        FORM_VARIABLES["stack"] = {
            "value": stack_var,
            "is_required": False,
        }
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

        result.update(
            {
                key: value["value"].get()
                for (
                    key,
                    value,
                ) in FORM_VARIABLES.items()
            }
        )

        result["difficulty"] = next(
            (
                difficulty.get("key")
                for difficulty in get_difficulties()
                if difficulty.get("name") == result.get("difficulty")
            ),
            None,
        )

        result["priority"] = next(
            (
                priority.get("key")
                for priority in get_priorities()
                if priority.get("name") == result.get("priority")
            ),
            None,
        )

        result["stack"] = next(
            (
                stack.get("key")
                for stack in get_stacks()
                if stack.get("name") == result.get("stack")
            ),
            None,
        )

        result["subject"] = next(
            (
                subject.get("key")
                for subject in get_subjects()
                if subject.get("name") == result.get("subject")
            ),
            None,
        )

        result["teacher"] = next(
            (
                teacher.get("key")
                for teacher in get_teachers()
                if teacher.get("name") == result.get("teacher")
            ),
            None,
        )

        return result
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get form",
            name=NAME,
        )
        raise Exception(f"Failed to get form: {e}") from e


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


def get_stack_create_form(master: tkinter.Frame) -> None:
    """
    Get the stack create form.

    Args:
        master (tkinter.Frame): The master frame.

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    try:
        log_info(
            message="Getting stack create form",
            name=NAME,
        )

        set_difficulties(difficulties=load_difficulties())
        set_priorities(priorities=load_priorities())
        set_stacks(stacks=load_stacks())
        set_subjects(subjects=load_subjects())
        set_teachers(teachers=load_teachers())

        clear_master_frame(master=master)
        configure_master_grid(master=master)
        create_widgets(master=master)

        subscribe()

        log_info(
            message="Got stack create form successfully",
            name=NAME,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to get stack create form",
            name=NAME,
        )
        raise Exception(f"Failed to get stack create form: {e}") from e


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


def get_subjects() -> list[dict[str, Any]]:
    """
    Get the subjects.

    Args:
        None

    Returns:
        list[dict[str, Any]]: The subjects.

    Raises:
        Exception: If an error occurs.
    """

    if is_list_empty(list_=SUBJECTS):
        log_warning(
            message="Subjects are empty. Check the logs for additional warnings. StudyFrog will still function though.",
            name=NAME,
        )

    return SUBJECTS


def get_teachers() -> list[dict[str, Any]]:
    """
    Get the teachers.

    Args:
        None

    Returns:
        list[dict[str, Any]]: The teachers.

    Raises:
        Exception: If an error occurs.
    """

    if is_list_empty(list_=TEACHERS):
        log_warning(
            "Teachers are empty. Check the logs for additional warnings. StudyFrog will still function though.",
            name=NAME,
        )

    return TEACHERS


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
        DIFFICULTIES.clear()
        FORM_VARIABLES.clear()
        PRIORITIES.clear()
        STACKS.clear()
        SUBJECTS.clear()
        TEACHERS.clear()
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


def load_subjects() -> list[dict[str, Any]]:
    """
    Load the subjects.

    Args:
        None

    Returns:
        list[dict[str, Any]]: The subjects.

    Raises:
        Exception: If an error occurs.
    """
    try:
        return list(
            publish_event(
                event=GET_ALL_SUBJECTS,
                namespace="GLOBAL",
            )
            .get("get_all_entries")[0]
            .get("result")
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to load subjects",
            name=NAME,
        )
        raise Exception(f"Failed to load subjects: {e}") from e


def load_teachers() -> list[dict[str, Any]]:
    """
    Load the teachers.

    Args:
        None

    Returns:
        list[dict[str, Any]]: The teachers.

    Raises:
        Exception: If an error occurs.
    """
    try:
        return list(
            publish_event(
                event=GET_ALL_TEACHERS,
                namespace="GLOBAL",
            )
            .get("get_all_entries")[0]
            .get("result")
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to load teachers",
            name=NAME,
        )
        raise Exception(f"Failed to load teachers: {e}") from e


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


def on_subject_combobox_return(
    combobox: ttk.Combobox,
    value: str,
) -> None:
    """
    Handle the subject combobox return event.

    Args:
        combobox (ttk.Combobox): The combobox.
        value (str): The value.

    Returns:
        None
    """

    try:
        if is_item_in_list(
            item=value,
            list_=[subject["name"] for subject in get_subjects()],
        ):
            return

        append_subject(
            subject=publish_event(
                event=GET_SUBJECT,
                namespace="GLOBAL",
                entry_id=publish_event(
                    event=ADD_SUBJECT,
                    namespace="GLOBAL",
                    entry=get_subject_model(
                        difficulty=next(
                            filter(
                                lambda difficulty: difficulty["name"] == "medium",
                                DIFFICULTIES,
                            )
                        )["key"],
                        name=value,
                        priority=next(
                            filter(
                                lambda priority: priority["name"] == "medium",
                                PRIORITIES,
                            )
                        )["key"],
                        teacher=None,
                    ),
                )["add_entry"][0]["result"],
            )["get_entry"][0]["result"],
        )

        combobox.set("")

        combobox["values"] = [subject["name"] for subject in get_subjects()]
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to handle subject combobox return event",
            name=NAME,
        )
        raise Exception(f"Failed to handle subject combobox return event: {e}") from e


def on_teacher_combobox_return(
    combobox: ttk.Combobox,
    value: str,
) -> None:
    """
    Handle the teacher combobox return event.

    Args:
        combobox (ttk.Combobox): The combobox.
        value (str): The value.

    Returns:
        None
    """

    try:
        if is_item_in_list(
            item=value,
            list_=[teacher["name"] for teacher in get_teachers()],
        ):
            return

        append_teacher(
            teacher=publish_event(
                event=GET_TEACHER,
                namespace="GLOBAL",
                entry_id=publish_event(
                    event=ADD_TEACHER,
                    namespace="GLOBAL",
                    entry=get_teacher_model(
                        difficulty=next(
                            filter(
                                lambda difficulty: difficulty["name"] == "medium",
                                DIFFICULTIES,
                            )
                        )["key"],
                        name=value,
                        priority=next(
                            filter(
                                lambda priority: priority["name"] == "medium",
                                PRIORITIES,
                            )
                        )["key"],
                        subjects=None,
                    ),
                )["add_entry"][0]["result"],
            )["get_entry"][0]["result"],
        )

        combobox["values"] = [teacher["name"] for teacher in get_teachers()]
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to handle teacher combobox return event",
            name=NAME,
        )
        raise Exception(f"Failed to handle teacher combobox return event: {e}") from e


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


def set_subjects(subjects: list[dict[str, Any]]) -> None:
    """
    Set the subjects.

    Args:
        subjects (list[dict[str, Any]]): The subjects.

    Returns:
        None
    """

    SUBJECTS.extend(subjects)


def set_teachers(teachers: list[dict[str, Any]]) -> None:
    """
    Set the teachers.

    Args:
        teachers (list[dict[str, Any]]): The teachers.

    Returns:
        None
    """

    TEACHERS.extend(teachers)


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
                namespace="STACK_CREATE_FORM",
                persistent=False,
            )
        )
        SUBSCRIPTIONS.append(
            register_subscription(
                event=CALL_FUNCTION,
                function=on_call_function,
                namespace="STACK_CREATE_FORM",
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
