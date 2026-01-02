"""
Author: Louis Goodnews
Date: 2025-12-13
Description: The logic of the create view of the application.
"""

import customtkinter as ctk

from typing import Any, Final, Optional

from constants.common import GLOBAL, PATTERNS
from constants.events import (
    ADD_FLASHCARD_TO_DB,
    ADD_NOTE_TO_DB,
    ADD_STACK_TO_DB,
    ADD_SUBJECT_TO_DB,
    ADD_TEACHER_TO_DB,
    CLEAR_CREATE_FORM,
    FILTER_DIFFICULTIES_FROM_DB,
    FILTER_PRIORITIES_FROM_DB,
    FILTER_SUBJECTS_FROM_DB,
    FILTER_TEACHERS_FROM_DB,
    GET_CREATE_FORM,
    GET_ERROR_TOAST,
    GET_FLASHCARD_MODEL_DICT,
    GET_NOTE_MODEL_DICT,
    GET_STACK_FROM_DB,
    GET_STACK_MODEL_DICT,
    DESTROY_CREATE_VIEW,
    DESTROY_FLASHCARD_CREATE_FORM,
    DESTROY_NOTE_CREATE_FORM,
    DESTROY_QUESTION_CREATE_FORM,
    DESTROY_STACK_CREATE_FORM,
    FILTER_STACKS_FROM_DB,
    GET_FLASHCARD_CREATE_FORM,
    GET_NOTE_CREATE_FORM,
    GET_QUESTION_CREATE_FORM,
    GET_STACK_CREATE_FORM,
    GET_SUBJECT_FROM_DB,
    GET_TEACHER_FROM_DB,
    UPDATE_STACK_IN_DB,
)
from constants.storage import (
    ANSWERS,
    DIFFICULTIES,
    FLASHCARDS,
    NOTES,
    PRIORITIES,
    QUESTIONS,
    STACKS,
    SUBJECTS,
    TEACHERS,
)
from models.models import ModelDict
from utils.common import search_string, generate_model_key
from utils.dispatcher import bulk_dispatch, dispatch
from utils.logging import log_debug, log_warning


# ---------- Exports ---------- #

__all__: Final[list[str]] = []


# ---------- Constants ---------- #


# ---------- Helper Functions ---------- #


def _filter_difficulty(**kwargs) -> dict[str, Any]:
    """
    Returns a difficulty matching the given criteria from the database.

    Args:
        **kwargs: The criteria to filter the difficulty by.

    Returns:
        dict[str, Any]: The difficulty matching the given criteria.
    """

    difficulties: Optional[list[dict[str, Any]]] = (
        dispatch(
            event=FILTER_DIFFICULTIES_FROM_DB,
            namespace=GLOBAL,
            table_name=DIFFICULTIES,
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


def _filter_priority(**kwargs) -> dict[str, Any]:
    """
    Returns a priority matching the given criteria from the database.

    Args:
        **kwargs: The criteria to filter the priority by.

    Returns:
        dict[str, Any]: The priority matching the given criteria.
    """

    priorities: Optional[list[dict[str, Any]]] = (
        dispatch(
            event=FILTER_PRIORITIES_FROM_DB,
            namespace=GLOBAL,
            table_name=PRIORITIES,
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


def _filter_stack(**kwargs) -> dict[str, Any]:
    """
    Returns a stack matching the given criteria from the database.

    Args:
        **kwargs: The criteria to filter the stack by.

    Returns:
        dict[str, Any]: The stack matching the given criteria.
    """

    stacks: Optional[list[dict[str, Any]]] = (
        dispatch(
            event=FILTER_STACKS_FROM_DB,
            namespace=GLOBAL,
            table_name=STACKS,
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


def _filter_subject(**kwargs) -> dict[str, Any]:
    """
    Returns a subject matching the given criteria from the database.

    Args:
        **kwargs: The criteria to filter the subject by.

    Returns:
        dict[str, Any]: The subject matching the given criteria.
    """

    subjects: Optional[list[dict[str, Any]]] = (
        dispatch(
            event=FILTER_SUBJECTS_FROM_DB,
            namespace=GLOBAL,
            table_name=SUBJECTS,
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

    if not subjects:
        return {}

    return subjects[0]


def _filter_teacher(**kwargs) -> dict[str, Any]:
    """
    Returns a teacher matching the given criteria from the database.

    Args:
        **kwargs: The criteria to filter the teacher by.

    Returns:
        dict[str, Any]: The teacher matching the given criteria.
    """

    teachers: Optional[list[dict[str, Any]]] = (
        dispatch(
            event=FILTER_TEACHERS_FROM_DB,
            namespace=GLOBAL,
            table_name=TEACHERS,
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

    if not teachers:
        return {}

    return teachers[0]


# ---------- Private Functions ---------- #


def _handle_answer_creation(form: dict[str, Any]) -> None:
    """
    Handles the creation of an answer.

    Args:
        form (dict[str, Any]): The form from which to create an answer from.

    Returns:
        None
    """

    kwargs: dict[str, Any] = {}

    for (
        key,
        value_dict,
    ) in form.items():
        is_required: bool = value_dict.get(
            "is_required",
            False,
        )
        value: Optional[Any] = value_dict.get(
            "value",
            None,
        )

        if is_required and value is None:
            dispatch(
                event=GET_ERROR_TOAST,
                message="Please fill in all required fields.",
                namespace=GLOBAL,
                title="Answer creation failed",
            )

            return

        kwargs[key] = value

    if kwargs.get(
        "subject",
        None,
    ) not in (
        None,
        "",
    ):
        kwargs["subject"] = (
            dispatch(
                event=GET_SUBJECT_FROM_DB,
                id=(
                    dispatch(
                        event=ADD_SUBJECT_TO_DB,
                        name=kwargs["subject"],
                        namespace=GLOBAL,
                        table_name=SUBJECTS,
                    )
                    .get(
                        "add_entry",
                        [{}],
                    )[0]
                    .get(
                        "result",
                        None,
                    )
                ),
                namespace=GLOBAL,
                table_name=SUBJECTS,
            )
            .get(
                "get_entry",
                [{}],
            )[0]
            .get(
                "result",
                {},
            )
            .get(
                "metadata",
                {},
            )
            .get(
                "key",
                None,
            )
        )

    if kwargs.get(
        "subject",
        None,
    ) in (
        None,
        "",
    ):
        kwargs["subject"] = (
            _filter_subject(
                key=_filter_stack(name=kwargs["stack"]).get(
                    "subject",
                    None,
                )
            )
            .get(
                "metadata",
                {},
            )
            .get(
                "key",
                None,
            )
        )

    if kwargs.get(
        "teacher",
        None,
    ) not in (
        None,
        "",
    ):
        kwargs["teacher"] = (
            dispatch(
                event=GET_TEACHER_FROM_DB,
                id=(
                    dispatch(
                        event=ADD_TEACHER_TO_DB,
                        name=kwargs["teacher"],
                        namespace=GLOBAL,
                        table_name=TEACHERS,
                    )
                    .get(
                        "add_entry",
                        [{}],
                    )[0]
                    .get(
                        "result",
                        None,
                    )
                ),
                namespace=GLOBAL,
                table_name=TEACHERS,
            )
            .get(
                "get_entry",
                [{}],
            )[0]
            .get(
                "result",
                {},
            )
            .get(
                "metadata",
                {},
            )
            .get(
                "key",
                None,
            )
        )

    if kwargs.get(
        "teacher",
        None,
    ) in (
        None,
        "",
    ):
        kwargs["teacher"] = (
            _filter_teacher(
                key=_filter_stack(name=kwargs["stack"]).get(
                    "teacher",
                    None,
                )
            )
            .get(
                "metadata",
                {},
            )
            .get(
                "key",
                None,
            )
        )


def _handle_flashcard_creation(form: dict[str, Any]) -> None:
    """
    Handles the creation of a flashcard.

    Args:
        form (dict[str, Any]): The form from which to create a flashcard from.

    Returns:
        None
    """

    kwargs: dict[str, Any] = {}

    for (
        key,
        value_dict,
    ) in form.items():
        if key in (
            "create_another",
            "description",
            "name",
            "type",
        ):
            continue

        is_required: bool = value_dict.get(
            "is_required",
            False,
        )
        value: Optional[Any] = value_dict.get(
            "value",
            None,
        )

        if is_required and value is None:
            dispatch(
                event=GET_ERROR_TOAST,
                message="Please fill in all required fields.",
                namespace=GLOBAL,
                title="Flashcard creation failed",
            )

            return

        kwargs[key] = value

    kwargs["difficulty"] = (
        _filter_difficulty(display_name=kwargs["difficulty"])
        .get(
            "metadata",
            {},
        )
        .get(
            "key",
            None,
        )
    )
    kwargs["priority"] = (
        _filter_priority(display_name=kwargs["priority"])
        .get(
            "metadata",
            {},
        )
        .get(
            "key",
            None,
        )
    )

    if (
        kwargs.get(
            "stack",
            None,
        )
        is not None
    ):
        kwargs["stack"] = (
            _filter_stack(name=kwargs["stack"])
            .get(
                "metadata",
                {},
            )
            .get(
                "key",
                None,
            )
        )

    if kwargs.get(
        "subject",
        None,
    ) not in (
        None,
        "",
    ):
        kwargs["subject"] = (
            dispatch(
                event=GET_SUBJECT_FROM_DB,
                id=(
                    dispatch(
                        event=ADD_SUBJECT_TO_DB,
                        name=kwargs["subject"],
                        namespace=GLOBAL,
                        table_name=SUBJECTS,
                    )
                    .get(
                        "add_entry",
                        [{}],
                    )[0]
                    .get(
                        "result",
                        None,
                    )
                ),
                namespace=GLOBAL,
                table_name=SUBJECTS,
            )
            .get(
                "get_entry",
                [{}],
            )[0]
            .get(
                "result",
                {},
            )
            .get(
                "metadata",
                {},
            )
            .get(
                "key",
                None,
            )
        )

    elif kwargs.get(
        "subject",
        None,
    ) in (
        None,
        "",
    ):
        kwargs["subject"] = (
            _filter_subject(
                key=_filter_stack(name=kwargs["stack"]).get(
                    "subject",
                    None,
                )
            )
            .get(
                "metadata",
                {},
            )
            .get(
                "key",
                None,
            )
        )

    if kwargs.get(
        "teacher",
        None,
    ) not in (
        None,
        "",
    ):
        kwargs["teacher"] = (
            dispatch(
                event=GET_TEACHER_FROM_DB,
                id=(
                    dispatch(
                        event=ADD_TEACHER_TO_DB,
                        name=kwargs["teacher"],
                        namespace=GLOBAL,
                        table_name=TEACHERS,
                    )
                    .get(
                        "add_entry",
                        [{}],
                    )[0]
                    .get(
                        "result",
                        None,
                    )
                ),
                namespace=GLOBAL,
                table_name=TEACHERS,
            )
            .get(
                "get_entry",
                [{}],
            )[0]
            .get(
                "result",
                {},
            )
            .get(
                "metadata",
                {},
            )
            .get(
                "key",
                None,
            )
        )

    elif kwargs.get(
        "teacher",
        None,
    ) in (
        None,
        "",
    ):
        kwargs["teacher"] = (
            _filter_teacher(
                key=_filter_stack(name=kwargs["stack"]).get(
                    "teacher",
                    None,
                )
            )
            .get(
                "metadata",
                {},
            )
            .get(
                "key",
                None,
            )
        )

    flashcard_model: Optional[dict[str, Any]] = (
        dispatch(
            event=GET_FLASHCARD_MODEL_DICT,
            namespace=GLOBAL,
            **{
                key: value
                for (
                    key,
                    value,
                ) in kwargs.items()
                if key
                not in (
                    "create_another",
                    "stack",
                    "type",
                )
            },
        )
        .get(
            "get_flashcard_model_dict",
            [{}],
        )[0]
        .get(
            "result",
            None,
        )
    )

    if flashcard_model is None:
        log_warning(message="Failed to get flashcard model. Aborting...")

        return

    id: Optional[int] = (
        dispatch(
            entry=flashcard_model,
            event=ADD_FLASHCARD_TO_DB,
            namespace=GLOBAL,
            table_name=FLASHCARDS,
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

    if id is None:
        log_warning(message="Failed to add flashcard to database. Aborting...")

        return

    stack: Optional[dict[str, Any]] = (
        dispatch(
            event=GET_STACK_FROM_DB,
            id=search_string(
                pattern=PATTERNS["MODEL_ID"],
                string=kwargs["stack"],
            ),
            namespace=GLOBAL,
            table_name=STACKS,
        )
        .get(
            "get_entry",
            [{}],
        )[0]
        .get(
            "result",
            {},
        )
    )

    if stack is None:
        log_warning(message="Failed to get stack. Aborting...")

        return

    stack["items"].append(
        generate_model_key(
            id=id,
            name="FLASHCARD",
        ),
    )

    dispatch(
        entry=stack,
        event=UPDATE_STACK_IN_DB,
        namespace=GLOBAL,
        table_name=STACKS,
    )


def _handle_note_creation(form: dict[str, Any]) -> None:
    """
    Handles the creation of a note.

    Args:
        form (dict[str, Any]): The form from which to create a note from.

    Returns:
        None
    """

    kwargs: dict[str, Any] = {}

    for (
        key,
        value_dict,
    ) in form.items():
        if key in (
            "create_another",
            "description",
            "name",
            "type",
        ):
            continue

        is_required: bool = value_dict.get(
            "is_required",
            False,
        )
        value: Optional[Any] = value_dict.get(
            "value",
            None,
        )

        if is_required and value is None:
            dispatch(
                event=GET_ERROR_TOAST,
                message="Please fill in all required fields.",
                namespace=GLOBAL,
                title="Note creation failed",
            )

            return

        kwargs[key] = value

    kwargs["difficulty"] = (
        _filter_difficulty(display_name=kwargs["difficulty"])
        .get(
            "metadata",
            {},
        )
        .get(
            "key",
            None,
        )
    )
    kwargs["priority"] = (
        _filter_priority(display_name=kwargs["priority"])
        .get(
            "metadata",
            {},
        )
        .get(
            "key",
            None,
        )
    )

    if (
        kwargs.get(
            "stack",
            None,
        )
        is not None
    ):
        kwargs["stack"] = (
            _filter_stack(name=kwargs["stack"])
            .get(
                "metadata",
                {},
            )
            .get(
                "key",
                None,
            )
        )

    if kwargs.get(
        "subject",
        None,
    ) not in (
        None,
        "",
    ):
        kwargs["subject"] = (
            dispatch(
                event=GET_SUBJECT_FROM_DB,
                id=(
                    dispatch(
                        event=ADD_SUBJECT_TO_DB,
                        name=kwargs["subject"],
                        namespace=GLOBAL,
                        table_name=SUBJECTS,
                    )
                    .get(
                        "add_entry",
                        [{}],
                    )[0]
                    .get(
                        "result",
                        None,
                    )
                ),
                namespace=GLOBAL,
                table_name=SUBJECTS,
            )
            .get(
                "get_entry",
                [{}],
            )[0]
            .get(
                "result",
                {},
            )
            .get(
                "metadata",
                {},
            )
            .get(
                "key",
                None,
            )
        )

    if kwargs.get(
        "subject",
        None,
    ) in (
        None,
        "",
    ):
        kwargs["subject"] = (
            _filter_subject(
                key=_filter_stack(name=kwargs["stack"]).get(
                    "subject",
                    None,
                )
            )
            .get(
                "metadata",
                {},
            )
            .get(
                "key",
                None,
            )
        )

    if kwargs.get(
        "teacher",
        None,
    ) not in (
        None,
        "",
    ):
        kwargs["teacher"] = (
            dispatch(
                event=GET_TEACHER_FROM_DB,
                id=(
                    dispatch(
                        event=ADD_TEACHER_TO_DB,
                        name=kwargs["teacher"],
                        namespace=GLOBAL,
                        table_name=TEACHERS,
                    )
                    .get(
                        "add_entry",
                        [{}],
                    )[0]
                    .get(
                        "result",
                        None,
                    )
                ),
                namespace=GLOBAL,
                table_name=TEACHERS,
            )
            .get(
                "get_entry",
                [{}],
            )[0]
            .get(
                "result",
                {},
            )
            .get(
                "metadata",
                {},
            )
            .get(
                "key",
                None,
            )
        )

    if kwargs.get(
        "teacher",
        None,
    ) in (
        None,
        "",
    ):
        kwargs["teacher"] = (
            _filter_teacher(
                key=_filter_stack(name=kwargs["stack"]).get(
                    "teacher",
                    None,
                )
            )
            .get(
                "metadata",
                {},
            )
            .get(
                "key",
                None,
            )
        )

    note_model: Optional[dict[str, Any]] = (
        dispatch(
            event=GET_NOTE_MODEL_DICT,
            namespace=GLOBAL,
            **{
                key: value
                for (
                    key,
                    value,
                ) in kwargs.items()
                if key
                not in (
                    "create_another",
                    "stack",
                    "type",
                )
            },
        )
        .get(
            "get_note_model_dict",
            [{}],
        )[0]
        .get(
            "result",
            None,
        )
    )

    if note_model is None:
        log_warning(message="Failed to get note model. Aborting...")

        return

    id: Optional[int] = (
        dispatch(
            entry=note_model,
            event=ADD_NOTE_TO_DB,
            namespace=GLOBAL,
            table_name=NOTES,
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

    if id is None:
        log_warning(message="Failed to add note to database. Aborting...")

        return

    stack: dict[str, Any] = _filter_stack(metadata={"key": kwargs["stack"]})

    stack["items"].append(
        generate_model_key(
            id=id,
            name="NOTE",
        ),
    )

    dispatch(
        entry=stack,
        event=UPDATE_STACK_IN_DB,
        namespace=GLOBAL,
        table_name=STACKS,
    )


def _handle_question_creation(form: dict[str, Any]) -> None:
    """
    Handles the creation of a question.

    Args:
        form (dict[str, Any]): The form from which to create a question from.

    Returns:
        None
    """

    kwargs: dict[str, Any] = {}

    for (
        key,
        value_dict,
    ) in form.items():
        is_required: bool = value_dict.get(
            "is_required",
            False,
        )
        value: Optional[Any] = value_dict.get(
            "value",
            None,
        )

        if is_required and value is None:
            dispatch(
                event=GET_ERROR_TOAST,
                message="Please fill in all required fields.",
                namespace=GLOBAL,
                title="Question creation failed",
            )

            return

        kwargs[key] = value

    if kwargs.get(
        "subject",
        None,
    ) not in (
        None,
        "",
    ):
        kwargs["subject"] = (
            dispatch(
                event=GET_SUBJECT_FROM_DB,
                id=(
                    dispatch(
                        event=ADD_SUBJECT_TO_DB,
                        name=kwargs["subject"],
                        namespace=GLOBAL,
                        table_name=SUBJECTS,
                    )
                    .get(
                        "add_entry",
                        [{}],
                    )[0]
                    .get(
                        "result",
                        None,
                    )
                ),
                namespace=GLOBAL,
                table_name=SUBJECTS,
            )
            .get(
                "get_entry",
                [{}],
            )[0]
            .get(
                "result",
                {},
            )
            .get(
                "metadata",
                {},
            )
            .get(
                "key",
                None,
            )
        )

    if kwargs.get(
        "subject",
        None,
    ) in (
        None,
        "",
    ):
        kwargs["subject"] = (
            _filter_subject(
                key=_filter_stack(name=kwargs["stack"]).get(
                    "subject",
                    None,
                )
            )
            .get(
                "metadata",
                {},
            )
            .get(
                "key",
                None,
            )
        )

    if kwargs.get(
        "teacher",
        None,
    ) not in (
        None,
        "",
    ):
        kwargs["teacher"] = (
            dispatch(
                event=GET_TEACHER_FROM_DB,
                id=(
                    dispatch(
                        event=ADD_TEACHER_TO_DB,
                        name=kwargs["teacher"],
                        namespace=GLOBAL,
                        table_name=TEACHERS,
                    )
                    .get(
                        "add_entry",
                        [{}],
                    )[0]
                    .get(
                        "result",
                        None,
                    )
                ),
                namespace=GLOBAL,
                table_name=TEACHERS,
            )
            .get(
                "get_entry",
                [{}],
            )[0]
            .get(
                "result",
                {},
            )
            .get(
                "metadata",
                {},
            )
            .get(
                "key",
                None,
            )
        )

    if kwargs.get(
        "teacher",
        None,
    ) in (
        None,
        "",
    ):
        kwargs["teacher"] = (
            _filter_teacher(
                key=_filter_stack(name=kwargs["stack"]).get(
                    "teacher",
                    None,
                )
            )
            .get(
                "metadata",
                {},
            )
            .get(
                "key",
                None,
            )
        )


def _handle_stack_creation(form: dict[str, Any]) -> None:
    """
    Handles the creation of a stack.

    Args:
        form (dict[str, Any]): The form from which to create a stack from.

    Returns:
        None
    """

    kwargs: dict[str, Any] = {}

    if form["stack"]["value"] not in (
        None,
        "",
    ):
        form["stack"]["is_required"] = False

    for (
        key,
        value_dict,
    ) in form.items():
        if key in (
            "create_another",
            "type",
        ):
            continue

        is_required: bool = value_dict.get(
            "is_required",
            False,
        )
        value: Optional[Any] = value_dict.get(
            "value",
            None,
        )

        if is_required and value is None:
            dispatch(
                event=GET_ERROR_TOAST,
                message="Please fill in all required fields.",
                namespace=GLOBAL,
                title="Stack creation failed",
            )

            return

        kwargs[key] = value

    kwargs["difficulty"] = (
        _filter_difficulty(display_name=kwargs["difficulty"])
        .get(
            "metadata",
            {},
        )
        .get(
            "key",
            None,
        )
    )
    kwargs["priority"] = (
        _filter_priority(display_name=kwargs["priority"])
        .get(
            "metadata",
            {},
        )
        .get(
            "key",
            None,
        )
    )

    if kwargs.get(
        "stack",
        None,
    ) not in (
        None,
        "",
    ):
        kwargs["parent"] = (
            _filter_stack(name=kwargs.pop("stack"))
            .get(
                "metadata",
                {},
            )
            .get(
                "key",
                None,
            )
        )

    if kwargs.get(
        "subject",
        None,
    ) not in (
        None,
        "",
    ):
        kwargs["subject"] = (
            dispatch(
                event=GET_SUBJECT_FROM_DB,
                id=(
                    dispatch(
                        event=ADD_SUBJECT_TO_DB,
                        name=kwargs["subject"],
                        namespace=GLOBAL,
                        table_name=SUBJECTS,
                    )
                    .get(
                        "add_entry",
                        [{}],
                    )[0]
                    .get(
                        "result",
                        None,
                    )
                ),
                namespace=GLOBAL,
                table_name=SUBJECTS,
            )
            .get(
                "get_entry",
                [{}],
            )[0]
            .get(
                "result",
                {},
            )
            .get(
                "metadata",
                {},
            )
            .get(
                "key",
                None,
            )
        )

    if kwargs.get(
        "subject",
        None,
    ) in (
        None,
        "",
    ):
        kwargs["subject"] = (
            _filter_subject(
                key=_filter_stack(name=kwargs["stack"]).get(
                    "subject",
                    None,
                )
            )
            .get(
                "metadata",
                {},
            )
            .get(
                "key",
                None,
            )
        )

    if kwargs.get(
        "teacher",
        None,
    ) not in (
        None,
        "",
    ):
        kwargs["teacher"] = (
            dispatch(
                event=GET_TEACHER_FROM_DB,
                id=(
                    dispatch(
                        event=ADD_TEACHER_TO_DB,
                        name=kwargs["teacher"],
                        namespace=GLOBAL,
                        table_name=TEACHERS,
                    )
                    .get(
                        "add_entry",
                        [{}],
                    )[0]
                    .get(
                        "result",
                        None,
                    )
                ),
                namespace=GLOBAL,
                table_name=TEACHERS,
            )
            .get(
                "get_entry",
                [{}],
            )[0]
            .get(
                "result",
                {},
            )
            .get(
                "metadata",
                {},
            )
            .get(
                "key",
                None,
            )
        )

    if kwargs.get(
        "teacher",
        None,
    ) in (
        None,
        "",
    ):
        kwargs["teacher"] = (
            _filter_teacher(
                key=_filter_stack(name=kwargs["stack"]).get(
                    "teacher",
                    None,
                )
            )
            .get(
                "metadata",
                {},
            )
            .get(
                "key",
                None,
            )
        )

    stack_model: Optional[dict[str, Any]] = (
        dispatch(
            event=GET_STACK_MODEL_DICT,
            namespace=GLOBAL,
            **kwargs,
        )
        .get(
            "get_stack_model_dict",
            [{}],
        )[0]
        .get(
            "result",
            None,
        )
    )

    if stack_model is None:
        log_warning(message="Failed to get stack model. Aborting...")

        return

    id: Optional[int] = (
        dispatch(
            entry=stack_model,
            event=ADD_STACK_TO_DB,
            namespace=GLOBAL,
            table_name=STACKS,
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

    if id is None:
        log_warning(message="Failed to add stack to database. Aborting...")

        return

    parent_stack: Optional[ModelDict] = (
        dispatch(
            event=GET_STACK_FROM_DB,
            id=stack_model["parent"],
            namespace=GLOBAL,
            table_name=STACKS,
        )
        .get(
            "get_entry",
            [{}],
        )[0]
        .get(
            "result",
            None,
        )
    )

    if parent_stack is None:
        log_warning(
            message=f"Failed to get parent stack with ID {stack_model['parent']}. Aborting..."
        )

        return

    parent_stack["children"].append(
        generate_model_key(
            id=id,
            name="STACK",
        )
    )

    dispatch(
        entry=parent_stack,
        event=UPDATE_STACK_IN_DB,
        namespace=GLOBAL,
        table_name=STACKS,
    )


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
        event=DESTROY_CREATE_VIEW,
        namespace=GLOBAL,
    )


def on_create_button_click() -> None:
    """
    Handles the 'create' button click.

    Args:
        None

    Returns:
        None
    """

    reponse: Optional[list[dict[str, Any]]] = dispatch(
        event=GET_CREATE_FORM,
        namespace=GLOBAL,
    ).get(
        "_on_get_create_form",
        [{}],
    )

    if not reponse:
        log_warning(message="Failed to get create form. Aborting...")

        return

    form: dict[str, Any] = {}

    for result in reponse:
        form.update(result.get("result", {}))

    {
        "answer": _handle_answer_creation,
        "flashcard": _handle_flashcard_creation,
        "note": _handle_note_creation,
        "question": _handle_question_creation,
        "stack": _handle_stack_creation,
    }[form["type"]["value"].lower()](form=form)

    if not form.get(
        "create_another",
        {},
    ).get(
        "value",
        False,
    ):
        dispatch(
            event=DESTROY_CREATE_VIEW,
            namespace=GLOBAL,
        )

        return

    dispatch(
        event=CLEAR_CREATE_FORM,
        namespace=GLOBAL,
    )


def on_type_combobox_select(
    scrollable_frame: ctk.CTkScrollableFrame,
    value: str,
) -> None:
    """
    Handles the type combobox's <<ComboboxSelected>> event.

    Args:
        scrollable_frame (ctk.CTkScrollableFrame): The scrollable frame to add the form to.
        value (str): The value of the combobox.

    Returns:
        None
    """

    if not value:
        log_warning(message="Received empty value. Aborting...")

        return

    events: list[str] = [
        DESTROY_FLASHCARD_CREATE_FORM,
        DESTROY_NOTE_CREATE_FORM,
        DESTROY_QUESTION_CREATE_FORM,
        DESTROY_STACK_CREATE_FORM,
    ]

    bulk_dispatch(
        events=events,
        namespaces=[GLOBAL for _ in events],
    )

    dispatch(
        event={
            "flashcard": GET_FLASHCARD_CREATE_FORM,
            "note": GET_NOTE_CREATE_FORM,
            "question": GET_QUESTION_CREATE_FORM,
            "stack": GET_STACK_CREATE_FORM,
        }[value.lower()],
        namespace=GLOBAL,
        scrollable_frame=scrollable_frame,
    )
