"""
Author: Louis Goodnews
Date: 2025-11-16
"""

import tkinter

from tkinter import ttk
from tkinter.constants import NSEW
from typing import Any, Callable, Final, Literal, Optional, TypeAlias, Union

from common.events import (
    CALL_FUNCTION,
    GET_ALL_DIFFICULTIES,
    GET_ALL_PRIORITIES,
    GET_ALL_STACKS,
    GET_ALL_SUBJECTS,
    GET_ALL_TEACHERS,
    GET_FORM,
)
from gui.constants import READONLY
from gui.factory import (
    get_button,
    get_checkbutton,
    get_combobox,
    get_entry,
    get_frame,
    get_label,
    get_radiobutton,
    get_scrolled_text,
)
from utils.utils import (
    destroy_widget_children,
    get_widget_children_count,
    is_list_empty,
    log_exception,
    log_info,
    log_warning,
    publish_event,
    register_subscription,
    string_to_human_case,
    string_to_snake_case,
    unsubscribe_subscription,
)


# ---------- Types ---------- #

QuestionType: TypeAlias = Literal[
    "multiple_choice",
    "multiple_select",
    "open_ended",
    "single_choice",
    "single_select",
    "true_false",
]

# ---------- Constants ---------- #

ANSWERS: Final[list[dict[str, Any]]] = []

CONTAINER: Optional[tkinter.Frame] = None

DIFFICULTIES: Final[list[dict[str, Any]]] = []

FORM_VARIABLES: Final[dict[str, dict[str, Union[bool, tkinter.Variable]]]] = {}

NAME: Final[Literal["gui.views.forms.question_create_form"]] = (
    "gui.views.forms.question_create_form"
)

PRIORITIES: Final[list[dict[str, Any]]] = []

QUESTION_TYPE: Optional[QuestionType] = None

STACKS: Final[list[dict[str, Any]]] = []

SUBJECTS: Final[list[dict[str, Any]]] = []

SUBSCRIPTIONS: Final[list[str]] = []

TEACHERS: Final[list[dict[str, Any]]] = []


# ---------- Functions ---------- #


def append_stack(stack: dict[str, Any]) -> None:
    """
    Append the stack.

    Args:
        stack (dict[str, Any]): The stack.

    Returns:
        None
    """

    STACKS.append(stack)


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


def clear_container_frame() -> None:
    """
    Clear the container frame.

    Returns:
        None
    """
    try:
        destroy_widget_children(widget=get_container_frame())
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to clear container frame",
            name=NAME,
        )
        raise Exception(f"Failed to clear container frame: {e}") from e


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
        master.grid_rowconfigure(
            index=2,
            weight=0,
        )
        master.grid_rowconfigure(
            index=3,
            weight=0,
        )
        master.grid_rowconfigure(
            index=4,
            weight=0,
        )
        master.grid_rowconfigure(
            index=5,
            weight=1,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to configure master grid",
            name=NAME,
        )
        raise Exception(f"Failed to configure master grid: {e}") from e


def create_multiple_choice_answer_item() -> None:
    """
    Create the multiple choice answer item.

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    try:
        frame: tkinter.Frame = get_frame(master=get_container_frame())

        frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        frame.grid_columnconfigure(
            index=0,
            weight=0,
        )

        frame.grid_rowconfigure(
            index=0,
            weight=0,
        )

        frame.grid(
            column=0,
            padx=5,
            pady=5,
            row=get_widget_children_count(widget=get_container_frame()),
            sticky=NSEW,
        )

        answer_var: tkinter.StringVar = tkinter.StringVar()

        entry: tkinter.Entry = get_entry(
            master=frame,
            textvariable=answer_var,
        )

        entry.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        is_correct_var: tkinter.BooleanVar = tkinter.BooleanVar()

        checkbutton: tkinter.Checkbutton = get_checkbutton(
            master=frame,
            text="Correct",
            variable=is_correct_var,
        )

        checkbutton.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        ANSWERS.append(
            {
                "is_correct": is_correct_var,
                "variable": answer_var,
            }
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to create multiple choice answer item",
            name=NAME,
        )
        raise Exception(f"Failed to create multiple choice answer item: {e}") from e


def create_multiple_choice_answer_widgets(master: tkinter.Frame) -> None:
    """
    Create the multiple choice answer widgets.

    Args:
        master (tkinter.Frame): The master frame.

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    try:
        get_button(
            command=create_multiple_choice_answer_item,
            master=master,
            text="Add Answer",
        ).grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to create multiple choice answer widgets",
            name=NAME,
        )
        raise Exception(f"Failed to create multiple choice answer widgets: {e}") from e


def create_true_false_answer_widgets(master: tkinter.Frame) -> None:
    """
    Create the true false answer widgets.

    Args:
        master (tkinter.Frame): The master frame.

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    try:
        answer_var: tkinter.BooleanVar = tkinter.BooleanVar()

        get_radiobutton(
            master=master,
            variable=answer_var,
        ).grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        get_radiobutton(
            master=master,
            variable=answer_var,
        ).grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        ANSWERS.append(
            {
                "is_correct": answer_var,
                "variable": answer_var,
            }
        )
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to create true false answer widgets",
            name=NAME,
        )
        raise Exception(f"Failed to create true false answer widgets: {e}") from e


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
        stack_label: tkinter.Label = get_label(
            master=master,
            text="Stack*:",
        )

        stack_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        stack_var: tkinter.StringVar = tkinter.StringVar()

        stack_combobox: ttk.Combobox = get_combobox(
            master=master,
            state=READONLY,
            textvariable=stack_var,
            values=[f"{stack["name"]} ({stack["key"]})" for stack in get_stacks()],
        )

        stack_combobox.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        stack_combobox.bind(
            func=lambda event: stack_var.set(value=stack_combobox.get()),
            sequence="<<ComboboxSelected>>",
        )

        FORM_VARIABLES["stack"] = {
            "variable": stack_var,
            "is_required": True,
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
            row=1,
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
            row=1,
            sticky=NSEW,
        )

        difficulty_combobox.bind(
            func=lambda event: difficulty_var.set(value=difficulty_combobox.get()),
            sequence="<<ComboboxSelected>>",
        )

        FORM_VARIABLES["difficulty"] = {
            "variable": difficulty_var,
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
            row=2,
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
            row=2,
            sticky=NSEW,
        )

        priority_combobox.bind(
            func=lambda event: priority_var.set(value=priority_combobox.get()),
            sequence="<<ComboboxSelected>>",
        )

        FORM_VARIABLES["priority"] = {
            "variable": priority_var,
            "is_required": True,
        }

        question_text_label = get_label(
            master=master,
            text="Question Text*:",
        )

        question_text_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=3,
            sticky=NSEW,
        )

        question_text_var: tkinter.StringVar = tkinter.StringVar()

        FORM_VARIABLES["text"] = {
            "variable": question_text_var,
            "is_required": True,
        }

        question_text_entry: dict[str, tkinter.Widget] = get_scrolled_text(master=master)

        question_text_entry["root"].grid(
            column=1,
            padx=5,
            pady=5,
            row=3,
            sticky=NSEW,
        )

        question_text_entry["text"].configure(height=10)

        question_text_entry["text"].bind(
            add="+",
            func=lambda event: question_text_var.set(
                value=question_text_entry["text"]
                .get(
                    index1="1.0",
                    index2="end-1c",
                )
                .strip()
            ),
            sequence="<KeyRelease>",
        )

        question_type_label: tkinter.Label = get_label(
            master=master,
            text="Question Type*:",
        )

        question_type_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=4,
            sticky=NSEW,
        )

        question_type_var: tkinter.StringVar = tkinter.StringVar()

        question_type_values: list[str] = [
            "Multiple Choice",
            "Multiple Select",
            "Open Ended",
            "Single Choice",
            "Single Select",
            "True False",
        ]

        question_type_combobox: ttk.Combobox = get_combobox(
            master=master,
            state=READONLY,
            textvariable=question_type_var,
            values=question_type_values,
        )

        question_type_combobox.grid(
            column=1,
            padx=5,
            pady=5,
            row=4,
            sticky=NSEW,
        )

        question_type_combobox.current(
            question_type_values.index(string_to_human_case(string=get_question_type()))
        )

        question_type_combobox.bind(
            func=lambda event: question_type_var.set(value=question_type_combobox.get()),
            sequence="<<ComboboxSelected>>",
        )

        question_type_combobox.bind(
            func=lambda event: on_question_type_change(question_type=question_type_var.get()),
            sequence="<<ComboboxSelected>>",
        )

        FORM_VARIABLES["question_type"] = {
            "variable": question_type_var,
            "is_required": True,
        }

        frame: tkinter.Frame = get_frame(master=master)

        frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        frame.grid(
            column=0,
            columnspan=2,
            padx=5,
            pady=5,
            row=5,
            sticky=NSEW,
        )

        set_container_frame(frame=frame)

        create_multiple_choice_answer_widgets(master=get_container_frame())
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to create widgets",
            name=NAME,
        )
        raise Exception(f"Failed to create widgets: {e}") from e


def get_container_frame() -> tkinter.Frame:
    """
    Get the container.

    Args:
        None

    Returns:
        tkinter.Frame: The container.

    Raises:
        Exception: If an error occurs.
    """

    if not CONTAINER:
        raise Exception(
            "Container is not initialized. Check the logs for errors as this should not be happening."
        )

    return CONTAINER


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

        result["answers"] = [
            {
                "is_correct": answer["is_correct"].get(),
                "text": answer["variable"].get(),
            }
            for answer in ANSWERS
        ]

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

        result["question_type"] = get_question_type()

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


def get_question_create_form(
    master: tkinter.Frame,
    question_type: QuestionType = "multiple_choice",
) -> None:
    """
    Get the question create form.

    Args:
        master (tkinter.Frame): The master frame.
        question_type (QuestionType): The question type. Defaults to "multiple_choice".

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

        set_question_type(question_type=question_type)

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


def get_question_type() -> QuestionType:
    """
    Get the question type.

    Args:
        None

    Returns:
        QuestionType: The question type.

    Raises:
        Exception: If an error occurs.
    """

    if QUESTION_TYPE is None:
        raise Exception(
            "Question type is None. Check the logs for errors as this should not be happening."
        )

    return QUESTION_TYPE


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

    Returns:
        dict[str, Any]: The form.
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


def on_question_type_change(question_type: QuestionType) -> None:
    """
    Handle the question type change event.

    Args:
        question_type (QuestionType): The question type.

    Returns:
        None
    """

    try:
        ANSWERS.clear()

        clear_container_frame()

        question_type = string_to_snake_case(string=question_type)

        set_question_type(question_type=question_type)

        question_type_to_widget_creator: dict[QuestionType, Callable[[tkinter.Frame], None]] = {
            "multiple_choice": create_multiple_choice_answer_widgets,
            "true_false": create_true_false_answer_widgets,
        }

        widget_creator: Optional[Callable[[tkinter.Frame], None]] = (
            question_type_to_widget_creator.get(
                question_type,
                None,
            )
        )

        if not widget_creator:
            log_warning(
                message=f"Failed to get widget creator for unsupported question type: {question_type}.",
                name=NAME,
            )

            return

        widget_creator(master=get_container_frame())
    except Exception as e:
        log_exception(
            exception=e,
            message="Failed to handle question type change",
            name=NAME,
        )
        raise Exception(f"Failed to handle question type change: {e}") from e


def set_container_frame(frame: tkinter.Frame) -> None:
    """
    Set the container.

    Args:
        frame (tkinter.Frame): The frame.

    Returns:
        None
    """

    global CONTAINER

    CONTAINER = frame


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


def set_question_type(question_type: QuestionType) -> None:
    """
    Set the question type.

    Args:
        question_type (QuestionType): The question type.

    Returns:
        None
    """

    global QUESTION_TYPE

    QUESTION_TYPE = question_type


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
                namespace="QUESTION_CREATE_FORM",
                persistent=True,
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
