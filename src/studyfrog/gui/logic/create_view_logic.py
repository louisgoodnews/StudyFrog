"""
Author: Louis Goodnews
Date: 2025-12-13
Description: The logic of the create view of the application.
"""

import customtkinter as ctk

from typing import Any, Callable, Final, Literal, Optional

from constants.common import GLOBAL
from constants.events import (
    ADD_ANSWER_TO_DB,
    ADD_FLASHCARD_TO_DB,
    ADD_NOTE_TO_DB,
    ADD_STACK_TO_DB,
    ADD_SUBJECT_TO_DB,
    ADD_TEACHER_TO_DB,
    CLEAR_CREATE_FORM,
    DESTROY_ANSWER_CREATE_FORM,
    DESTROY_CREATE_VIEW,
    DESTROY_FLASHCARD_CREATE_FORM,
    DESTROY_NOTE_CREATE_FORM,
    DESTROY_QUESTION_CREATE_FORM,
    DESTROY_STACK_CREATE_FORM,
    FILTER_DIFFICULTIES_FROM_DB,
    FILTER_PRIORITIES_FROM_DB,
    FILTER_STACKS_FROM_DB,
    FILTER_SUBJECTS_FROM_DB,
    FILTER_TEACHERS_FROM_DB,
    GET_ANSWER_FROM_DB,
    GET_ANSWER_MODEL_DICT,
    GET_CREATE_FORM,
    GET_ERROR_TOAST,
    GET_FLASHCARD_FROM_DB,
    GET_FLASHCARD_MODEL_DICT,
    GET_NOTE_FROM_DB,
    GET_NOTE_MODEL_DICT,
    GET_QUESTION_MODEL_DICT,
    GET_STACK_FROM_DB,
    GET_STACK_MODEL_DICT,
    GET_FLASHCARD_CREATE_FORM,
    GET_NOTE_CREATE_FORM,
    GET_QUESTION_CREATE_FORM,
    GET_QUESTION_FROM_DB,
    GET_STACK_CREATE_FORM,
    GET_STACK_FROM_DB,
    GET_SUBJECT_FROM_DB,
    GET_TEACHER_FROM_DB,
    UPDATE_ANSWER_IN_DB,
    UPDATE_FLASHCARD_IN_DB,
    UPDATE_NOTE_IN_DB,
    UPDATE_QUESTION_IN_DB,
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
from utils.common import exists, pluralize_word, search_string, generate_model_key
from utils.dispatcher import bulk_dispatch, dispatch
from utils.logging import log_debug, log_error, log_info, log_warning


# ---------- Exports ---------- #

__all__: Final[list[str]] = []


# ---------- Constants ---------- #


_LAST_CREATED: dict[
    Literal[
        "answer",
        "flashcard",
        "note",
        "question",
        "stack",
        "subject",
        "teacher",
    ],
    tuple[Optional[int], Optional[str]],
] = {}

_LAST_UPDATED: dict[
    Literal[
        "answer",
        "flashcard",
        "note",
        "question",
        "stack",
        "subject",
        "teacher",
    ],
    tuple[Optional[int], Optional[str]],
] = {}


# ---------- Helper Functions ---------- #


def _add_to_database(model_dict: ModelDict) -> Optional[int]:
    """
    Adds the passed model dictionay to the database.

    Args:
        model_dict (ModelDict): The model dictionary to add to the database.

    Returns:
        Optional[int]: The ID of the added model, or None if the model could not be added.
    """

    try:
        type_: str = model_dict["metadata"]["type"].lower()

        result: Optional[int] = (
            dispatch(
                entry=model_dict,
                event=_get_add_event(type_=type_),
                namespace=GLOBAL,
                table_name=_get_table_name(type_=type_),
            )
            .get(
                "add_entry",
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
                "id",
                None,
            )
        )

        if result is not None:
            _update_last_created(
                id_=result,
                type_=model_dict["metadata"]["type"].lower(),
            )

        return result
    except Exception as e:
        log_error(
            message=f"Caught an exception while attempting to add '{model_dict['metadata']['type']}' to the database: {e}"
        )

        return None


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


def _get_add_event(
    type_: Literal[
        "answer",
        "flashcard",
        "note",
        "question",
        "stack",
        "subject",
        "teacher",
    ],
) -> str:
    """
    Returns the add to database event corresponding with the passed type.

    Args:
        type_ (Literal["answer", "flashcard", "note", "question", "stack", "subject", "teacher"]: The type of the entry to add to the database.

    Returns:
        str: The add to database event corresponding with the passed type.
    """

    return {
        "answer": ADD_ANSWER_TO_DB,
        "flashcard": ADD_FLASHCARD_TO_DB,
        "note": ADD_NOTE_TO_DB,
        "stack": ADD_STACK_TO_DB,
        "subject": ADD_SUBJECT_TO_DB,
        "teacher": ADD_TEACHER_TO_DB,
    }[type_]


def _get_from_database(key: str) -> Optional[ModelDict]:
    """
    Retrieves the model dictionary corresponding to the passed key.

    Args:
        key (str): The key of the model dictionary to retrieve.

    Returns:
        Optional[ModelDict]: The model dictionary corresponding to the passed key.
    """

    try:
        (
            type_,
            id_,
        ) = tuple(key.lower().split("_"))

        return (
            dispatch(
                event=_get_get_from_db_event(type_=type_),
                namespace=GLOBAL,
                id_=id_,
                table_name=_get_table_name(type_=type_),
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
    except Exception as e:
        log_error(message=f"Caught an exception while attempting to get '{key}' from database: {e}")

        return None


def _get_get_from_db_event(
    type_: Literal[
        "answer",
        "flashcard",
        "note",
        "question",
        "stack",
        "subject",
        "teacher",
    ],
) -> str:
    """
    Returns the get from database event corresponding with the passed type.

    Args:
        type_ (Literal["answer", "flashcard", "note", "question", "stack", "subject", "teacher"]: The type of the entry to add to the database.

    Returns:
        str: The get from database event corresponding with the passed type.
    """

    return {
        "answer": GET_ANSWER_FROM_DB,
        "flashcard": GET_FLASHCARD_FROM_DB,
        "note": GET_NOTE_FROM_DB,
        "question": GET_QUESTION_FROM_DB,
        "stack": GET_STACK_FROM_DB,
        "subject": GET_SUBJECT_FROM_DB,
        "teacher": GET_TEACHER_FROM_DB,
    }[type_]


def _get_get_model_dict_event(
    type_: Literal[
        "answer",
        "flashcard",
        "note",
        "question",
        "stack",
    ],
) -> str:
    """
    Returns the get model dictionary event corresponding with the passed type.

    Args:
        type_ (Literal["answer", "flashcard", "note", "question", "stack", "subject", "teacher"]: The type of the entry to add to the database.

    Returns:
        str: The get model dictionary event corresponding with the passed type.
    """

    return {
        "answer": GET_ANSWER_MODEL_DICT,
        "flashcard": GET_FLASHCARD_MODEL_DICT,
        "note": GET_NOTE_MODEL_DICT,
        "question": GET_QUESTION_MODEL_DICT,
        "stack": GET_STACK_MODEL_DICT,
    }[type_]


def _get_model_dict(
    data: dict[str, Any],
    type_: Literal[
        "answer",
        "flashcard",
        "note",
        "question",
        "stack",
    ],
) -> Optional[ModelDict]:
    """
    Returns a model dictionary containing the passed data.

    Args:
        data (dict[str, Any]): The data to convert to a model dictionary.

    Returns:
        Optional[ModelDict]: The model dictionary containing the passed data.
    """

    try:
        response: Optional[ModelDict] = (
            dispatch(
                event=_get_get_model_dict_event(type_=type_),
                namespace=GLOBAL,
                **data,
            )
            .get(
                f"get_{type_}_model_dict",
                [{}],
            )[0]
            .get(
                "result",
                None,
            )
        )

        if not exists(value=response):
            log_warning(
                message=f"Failed to get model dictionary for '{type_}' type. Values: {', '.join(data.values())}"
            )
            return None

        return response
    except Exception as e:
        log_error(
            message=f"Caught an exception while attempting to get model dictionary for '{type_}' from database: {e}"
        )

        return None


def _get_table_name(
    type_: Literal[
        "answer",
        "flashcard",
        "note",
        "question",
        "stack",
        "subject",
        "teacher",
    ],
) -> str:
    """
    Returns the table name corresponding to the passed type.

    Args:
        type_ (Literal["answer", "flashcard", "note", "question", "stack", "subject", "teacher"]: The type of the entry to add to the database.

    Returns:
        str: The table name corresponding to the passed type.
    """

    return {
        "answer": ANSWERS,
        "flashcard": FLASHCARDS,
        "note": NOTES,
        "question": QUESTIONS,
        "stack": STACKS,
        "subject": SUBJECTS,
        "teacher": TEACHERS,
    }[type_.lower()]


def _get_update_in_db_event(
    type_: Literal[
        "answer",
        "flashcard",
        "note",
        "question",
        "stack",
        "subject",
        "teacher",
    ],
) -> str:
    """
    Returns the update in database event corresponding with the passed type.

    Args:
        type_ (Literal["answer", "flashcard", "note", "question", "stack", "subject", "teacher"]: The type of the entry to add to the database.

    Returns:
        str: The update in database event corresponding with the passed type.
    """

    return {
        "answer": UPDATE_ANSWER_IN_DB,
        "flashcard": UPDATE_FLASHCARD_IN_DB,
        "note": UPDATE_NOTE_IN_DB,
        "question": UPDATE_QUESTION_IN_DB,
        "stack": UPDATE_STACK_IN_DB,
    }[type_]


def _inherit_metadata_from_stack(dictionary: dict[str, Any]) -> None:
    """
    Inherits the metadata from the stack to the passed form.

    Args:
        dictionary (dict[str, Any]): The form to inherit the metadata from the stack to.

    Returns:
        None

    Raises:
        Exception: If any errors occur
    """

    try:
        has_stack_parent: bool = exists(value=dictionary["stack"])

        if has_stack_parent:
            stack_parent: Optional[dict[str, Any]] = _get_from_database(key=dictionary["stack"])

        if exists(value=dictionary["subject"]):
            dictionary["subject"] = _filter_subject(name=dictionary["subject"])["metadata"]["key"]

        elif not exists(value=dictionary["subject"]) and has_stack_parent:
            dictionary["subject"] = stack_parent["subject"]
        else:
            log_warning(message="Subject metadata could not be inherited. Parent stack not found.")

        if exists(value=dictionary["teacher"]):
            dictionary["teacher"] = _filter_teacher(name=dictionary["teacher"])["metadata"]["key"]

        elif not exists(value=dictionary["teacher"]) and has_stack_parent:
            dictionary["teacher"] = stack_parent["teacher"]
        else:
            log_warning(message="Teacher metadata could not be inherited. Parent stack not found.")
    except Exception as e:
        log_error(
            message=f"Caught an exception while attempting to inherit metadata from stack: {e}"
        )


def _resolve_metadata_keys(dictionary: dict[str, Any]) -> None:
    """
    Resolves various model names or keys within the dictionary to their
    corresponding database metadata keys or objects.

    This method iterates through specific known keys (e.g., 'stack', 'subject',
    'answer') and replaces their display values or temporary keys with the
    actual metadata keys retrieved from the database.

    Args:
        dictionary (dict[str, Any]): The dictionary containing the values
            to be resolved.

    Returns:
        None
    """
    try:
        for key in [
            "answer",
            "flashcard",
            "note",
            "question",
        ]:
            if exists(value=dictionary.get(key)):
                response: Optional[ModelDict] = _get_from_database(key=dictionary[key])

                if not exists(value=response):
                    log_warning(message=f"Failed to resolve metadata key for '{key}'")
                    continue

                dictionary[key] = response["metadata"]["key"]

        if exists(value=dictionary.get("subject")):
            response: Optional[ModelDict] = _filter_subject(name=dictionary["subject"])

            if not exists(value=response):
                log_warning(message="Failed to resolve metadata key for 'subject'")
            else:
                dictionary["subject"] = response.get("metadata", {}).get("key")

        if exists(value=dictionary.get("teacher")):
            response: Optional[ModelDict] = _filter_teacher(name=dictionary["teacher"])

            if not exists(value=response):
                log_warning(message="Failed to resolve metadata key for 'teacher'")
            else:
                dictionary["teacher"] = response.get("metadata", {}).get("key")

        if exists(value=dictionary.get("stack")):
            response: Optional[ModelDict] = _filter_stack(name=dictionary["stack"])

            if not exists(value=response):
                log_warning(message="Failed to resolve metadata key for 'stack'")
            else:
                dictionary["stack"] = response.get("metadata", {}).get("key")

    except Exception as e:
        log_error(message=f"Caught an exception while attempting to resolve metadata keys: {e}")
        raise e


def _update_in_database(model_dict: ModelDict) -> Optional[int]:
    """
    Updates the passed model dictionay to the database.

    Args:
        model_dict (ModelDict): The model dictionary to update to the database.

    Returns:
        Optional[int]: The ID of the added model, or None if the model could not be added.
    """

    try:
        type_: str = model_dict["metadata"]["type"].lower()

        result: Optional[int] = (
            dispatch(
                entry=model_dict,
                event=_get_update_in_db_event(type_=type_),
                namespace=GLOBAL,
                table_name=_get_table_name(type_=type_),
            )
            .get(
                "update_entry",
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
                "id",
                None,
            )
        )

        if result is not None:
            _update_last_updated(
                id_=result,
                type_=model_dict["metadata"]["type"].lower(),
            )

        return result
    except Exception as e:
        log_error(
            message=f"Caught an exception while attempting to update '{model_dict['metadata']['type']}' to the database: {e}"
        )

        return None


def _update_last_created(
    type_: Literal[
        "flashcard",
        "note",
        "question",
        "stack",
    ],
    id_: int,
) -> None:
    """
    Updates the ID of the last created entry of the given type.

    Args:
        type_ (Literal["flashcard", "note", "question", "stack"]: The type of the entry to update.
        id (int): The ID of the last created entry.

    Returns:
        None
    """

    _LAST_CREATED[type_] = (
        id_,
        generate_model_key(
            id_=id_,
            name=type_,
        ),
    )


def _update_last_updated(
    type_: Literal[
        "flashcard",
        "note",
        "question",
        "stack",
    ],
    id_: int,
) -> None:
    """
    Updates the ID of the last updated entry of the given type.

    Args:
        type_ (Literal["flashcard", "note", "question", "stack"]: The type of the entry to update.
        id (int): The ID of the last updated entry.

    Returns:
        None
    """

    _LAST_UPDATED[type_] = (
        id_,
        generate_model_key(
            id_=id_,
            name=type_,
        ),
    )


def _validate_form(form: dict[str, Any]) -> dict[str, Any]:
    """
    Validates the form and returns the validated data.

    Args:
        form (dict[str, Any]): The form to validate.

    Returns:
        dict[str, Any]: The validated data.
    """

    result: dict[str, Any] = {}

    form_type: str = form.pop("type", {}).get("value", "").lower()

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
                title="Note creation failed",
            )

            log_warning(message=f"Missing required field: {key} ({value})")

            return

        result[key] = value

    return result


# ---------- Private Functions ---------- #


def _handle_answer_creation(form: dict[str, Any]) -> None:
    """
    Handles the creation of an answer.

    Args:
        form (dict[str, Any]): The form from which to create an answer from.

    Returns:
        None
    """

    kwargs: dict[str, Any] = _validate_form(form=form)

    _inherit_metadata_from_stack(dictionary=kwargs)


def _handle_flashcard_creation(form: dict[str, Any]) -> None:
    """
    Handles the creation of a flashcard.

    Args:
        form (dict[str, Any]): The form from which to create a flashcard from.

    Returns:
        None
    """

    kwargs: dict[str, Any] = _validate_form(form=form)

    _resolve_metadata_keys(dictionary=kwargs)

    _inherit_metadata_from_stack(dictionary=kwargs)

    flashcard_model: Optional[dict[str, Any]] = _get_model_dict(
        data={
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
        }
    )

    if flashcard_model is None:
        log_warning(message="Failed to get flashcard model. Aborting...")

        return

    id_: Optional[int] = _add_to_database(model_dict=flashcard_model)

    if id_ is None:
        log_warning(message="Failed to add flashcard to database. Aborting...")

        return

    stack: Optional[dict[str, Any]] = _get_from_database(key=kwargs["stack"])

    if stack is None:
        log_warning(message="Failed to get stack. Aborting...")

        return

    stack["items"].append(
        generate_model_key(
            id_=id_,
            name="FLASHCARD",
        ),
    )

    _update_in_database(model_dict=stack)


def _handle_note_creation(form: dict[str, Any]) -> None:
    """
    Handles the creation of a note.

    Args:
        form (dict[str, Any]): The form from which to create a note from.

    Returns:
        None
    """

    kwargs: dict[str, Any] = _validate_form(form=form)

    _resolve_metadata_keys(dictionary=kwargs)

    _inherit_metadata_from_stack(dictionary=kwargs)

    note_model: Optional[dict[str, Any]] = _get_model_dict(
        data={
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
        }
    )

    if note_model is None:
        log_warning(message="Failed to get note model. Aborting...")

        return

    id_: Optional[int] = _add_to_database(model_dict=note_model)

    if id_ is None:
        log_warning(message="Failed to add note to database. Aborting...")

        return

    stack: dict[str, Any] = _filter_stack(metadata={"key": kwargs["stack"]})

    stack["items"].append(
        generate_model_key(
            id_=id_,
            name="NOTE",
        ),
    )

    _update_in_database(model_dict=stack)


def _handle_question_creation(form: dict[str, Any]) -> None:
    """
    Handles the creation of a question.

    Args:
        form (dict[str, Any]): The form from which to create a question from.

    Returns:
        None
    """

    kwargs: dict[str, Any] = _validate_form(form=form)

    _resolve_metadata_keys(dictionary=kwargs)

    _inherit_metadata_from_stack(dictionary=kwargs)

    question_model: Optional[dict[str, Any]] = _get_model_dict(
        data={
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
        }
    )

    if question_model is None:
        log_warning(message="Failed to get question model. Aborting...")

        return

    id_: Optional[int] = _add_to_database(model_dict=question_model)

    if id_ is None:
        log_warning(message="Failed to add question to database. Aborting...")

        return

    stack: dict[str, Any] = _filter_stack(metadata={"key": kwargs["stack"]})

    stack["items"].append(
        generate_model_key(
            id_=id_,
            name="question",
        ),
    )

    _update_in_database(model_dict=stack)


def _handle_stack_creation(form: dict[str, Any]) -> None:
    """
    Handles the creation of a stack.

    Args:
        form (dict[str, Any]): The form from which to create a stack from.

    Returns:
        None
    """

    kwargs: dict[str, Any] = _validate_form(form=form)

    _resolve_metadata_keys(dictionary=kwargs)

    _inherit_metadata_from_stack(dictionary=kwargs)

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

    if exists(value=kwargs["stack"]):
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
    else:
        kwargs.pop("stack")

    stack_model: Optional[ModelDict] = _get_model_dict(
        data=kwargs,
        type_="stack",
    )

    if not exists(value=stack_model):
        log_warning(message="Failed to get stack model. Aborting...")

        return

    id_: Optional[int] = _add_to_database(model_dict=stack_model)

    if not exists(value=id_):
        log_warning(message="Failed to add stack to database. Aborting...")

        return

    parent_stack: Optional[ModelDict] = _get_from_database(
        key=generate_model_key(
            id_=stack_model["parent"],
            name="stack",
        ),
    )

    if not exists(value=parent_stack):
        log_warning(
            message=f"Failed to get parent stack with ID {stack_model['parent']}. Aborting..."
        )

        return

    parent_stack["children"].append(
        generate_model_key(
            id_=id_,
            name="STACK",
        )
    )

    _update_in_database(model_dict=parent_stack)


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

    reponses: Optional[list[dict[str, Any]]] = dispatch(
        event=GET_CREATE_FORM,
        namespace=GLOBAL,
    ).get(
        "_on_get_create_form",
        [{}],
    )

    if not exists(value=reponses):
        log_warning(message="Failed to get create form. Aborting...")

        return

    handlers: dict[
        Literal[
            "answer",
            "flashcard",
            "note",
            "question",
            "stack",
        ],
        Callable[[dict[str, Any]], None],
    ] = {
        "answer": _handle_answer_creation,
        "flashcard": _handle_flashcard_creation,
        "note": _handle_note_creation,
        "question": _handle_question_creation,
        "stack": _handle_stack_creation,
    }

    create_another: bool = False

    form: dict[str, Any] = {
        "core": None,
        "answer": None,
        "flashcard": None,
        "note": None,
        "question": None,
        "stack": None,
    }

    for response in reponses:
        origin: str = response["result"]["origin"].lower()

        if origin == "create_view":
            create_another = response["result"]["form_content"]["create_another"]["value"]
            form["core"] = {
                key: value
                for (
                    key,
                    value,
                ) in response[
                    "result"
                ]["form_content"].items()
                if key != "create_another"
            }
        else:
            form[origin.replace("_create_form", "")] = response["result"]["form_content"]

    for (
        key,
        value,
    ) in form.items():
        if key not in handlers:
            continue

        if not exists(value=value):
            continue

        handlers[key](
            form={
                **form["core"],
                **value,
            }
        )

    if not create_another:
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
        DESTROY_ANSWER_CREATE_FORM,
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
