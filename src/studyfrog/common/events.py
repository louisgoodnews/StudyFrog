"""
Author: Louis Goodnews
Date: 2025-11-16
Description: Defines all events used in the application as ApplicationEvent constants.
"""

from typing import Final, Literal, TypeAlias


# ---------- Types ---------- #

ApplicationEvent: TypeAlias = Literal[
    "add_answer",
    "add_answers",
    "add_association",
    "add_associations",
    "add_customfield",
    "add_customfields",
    "add_difficulty",
    "add_difficulties",
    "add_flashcard",
    "add_flashcards",
    "add_image",
    "add_images",
    "add_note",
    "add_notes",
    "add_option",
    "add_options",
    "add_priority",
    "add_priorities",
    "add_question",
    "add_questions",
    "add_rehearsal_run",
    "add_rehearsal_runs",
    "add_rehearsal_run_item",
    "add_rehearsal_run_items",
    "add_stack",
    "add_stacks",
    "add_subject",
    "add_subjects",
    "add_tag",
    "add_tags",
    "add_teacher",
    "add_teachers",
    "add_user",
    "add_users",
    "added_answer",
    "added_answers",
    "added_customfield",
    "added_customfields",
    "added_difficulty",
    "added_difficulties",
    "added_flashcard",
    "added_flashcards",
    "added_image",
    "added_images",
    "added_note",
    "added_notes",
    "added_option",
    "added_options",
    "added_priority",
    "added_priorities",
    "added_question",
    "added_questions",
    "added_rehearsal_run",
    "added_rehearsal_runs",
    "added_rehearsal_run_item",
    "added_rehearsal_run_items",
    "added_stack",
    "added_stacks",
    "added_subject",
    "added_subjects",
    "added_tag",
    "added_tags",
    "added_teacher",
    "added_teachers",
    "added_user",
    "added_users",
    "application_started",
    "application_starting",
    "application_stopped",
    "application_stopping",
    "call_function",
    "call_functions",
    "cancel_button_clicked",
    "confirm_button_clicked",
    "create_button_clicked",
    "destroy_widget",
    "destroy_widget_children",
    "get_all_answers",
    "get_all_associations",
    "get_all_customfields",
    "get_all_difficulties",
    "get_all_flashcards",
    "get_all_images",
    "get_all_notes",
    "get_all_options",
    "get_all_priorities",
    "get_all_questions",
    "get_all_rehearsal_runs",
    "get_all_rehearsal_run_items",
    "get_all_stacks",
    "get_all_subjects",
    "get_all_tags",
    "get_all_teachers",
    "get_all_users",
    "get_answer",
    "get_answers",
    "get_association",
    "get_associations",
    "get_attribute",
    "get_attributes",
    "get_customfield",
    "get_customfields",
    "get_difficulty",
    "get_difficulties",
    "get_flashcard",
    "get_flashcards",
    "get_form",
    "get_image",
    "get_images",
    "get_note",
    "get_notes",
    "get_option",
    "get_options",
    "get_priority",
    "get_priorities",
    "get_question",
    "get_questions",
    "get_rehearsal_run",
    "get_rehearsal_runs",
    "get_rehearsal_run_item",
    "get_rehearsal_run_items",
    "get_stack",
    "get_stacks",
    "get_subject",
    "get_subjects",
    "get_tag",
    "get_tags",
    "get_teacher",
    "get_teachers",
    "get_user",
    "get_users",
    "ok_button_clicked",
    "remove_answer",
    "remove_answers",
    "remove_association",
    "remove_associations",
    "remove_customfield",
    "remove_customfields",
    "remove_difficulty",
    "remove_difficulties",
    "remove_flashcard",
    "remove_flashcards",
    "remove_image",
    "remove_images",
    "remove_note",
    "remove_notes",
    "remove_option",
    "remove_options",
    "remove_priority",
    "remove_priorities",
    "remove_question",
    "remove_questions",
    "remove_rehearsal_run",
    "remove_rehearsal_runs",
    "remove_rehearsal_run_item",
    "remove_rehearsal_run_items",
    "remove_stack",
    "remove_stacks",
    "remove_subject",
    "remove_subjects",
    "remove_tag",
    "remove_tags",
    "remove_teacher",
    "remove_teachers",
    "remove_user",
    "remove_users",
    "update_answer",
    "update_answers",
    "update_association",
    "update_associations",
    "update_customfield",
    "update_customfields",
    "update_difficulty",
    "update_difficulties",
    "update_flashcard",
    "update_flashcards",
    "update_image",
    "update_images",
    "update_note",
    "update_notes",
    "update_option",
    "update_options",
    "update_priority",
    "update_priorities",
    "update_question",
    "update_questions",
    "update_rehearsal_run",
    "update_rehearsal_runs",
    "update_rehearsal_run_item",
    "update_rehearsal_run_items",
    "update_stack",
    "update_stacks",
    "update_subject",
    "update_subjects",
    "update_tag",
    "update_tags",
    "update_teacher",
    "update_teachers",
    "update_user",
    "update_users",
]

# ---------- Events ---------- #

ADD_ANSWER: Final[ApplicationEvent] = "add_answer"

ADD_ANSWERS: Final[ApplicationEvent] = "add_answers"

ADD_ASSOCIATION: Final[ApplicationEvent] = "add_association"

ADD_ASSOCIATIONS: Final[ApplicationEvent] = "add_associations"

ADD_CUSTOMFIELD: Final[ApplicationEvent] = "add_customfield"

ADD_CUSTOMFIELDS: Final[ApplicationEvent] = "add_customfields"

ADD_DIFFICULTY: Final[ApplicationEvent] = "add_difficulty"

ADD_DIFFICULTIES: Final[ApplicationEvent] = "add_difficulties"

ADD_FLASHCARD: Final[ApplicationEvent] = "add_flashcard"

ADD_FLASHCARDS: Final[ApplicationEvent] = "add_flashcards"

ADD_IMAGE: Final[ApplicationEvent] = "add_image"

ADD_IMAGES: Final[ApplicationEvent] = "add_images"

ADD_NOTE: Final[ApplicationEvent] = "add_note"

ADD_NOTES: Final[ApplicationEvent] = "add_notes"

ADD_OPTION: Final[ApplicationEvent] = "add_option"

ADD_OPTIONS: Final[ApplicationEvent] = "add_options"

ADD_PRIORITY: Final[ApplicationEvent] = "add_priority"

ADD_PRIORITIES: Final[ApplicationEvent] = "add_priorities"

ADD_QUESTION: Final[ApplicationEvent] = "add_question"

ADD_QUESTIONS: Final[ApplicationEvent] = "add_questions"

ADD_REHEARSAL_RUN: Final[ApplicationEvent] = "add_rehearsal_run"

ADD_REHEARSAL_RUNS: Final[ApplicationEvent] = "add_rehearsal_runs"

ADD_REHEARSAL_RUN_ITEM: Final[ApplicationEvent] = "add_rehearsal_run_item"

ADD_REHEARSAL_RUN_ITEMS: Final[ApplicationEvent] = "add_rehearsal_run_items"

ADD_STACK: Final[ApplicationEvent] = "add_stack"

ADD_STACKS: Final[ApplicationEvent] = "add_stacks"

ADD_SUBJECT: Final[ApplicationEvent] = "add_subject"

ADD_SUBJECTS: Final[ApplicationEvent] = "add_subjects"

ADD_TAG: Final[ApplicationEvent] = "add_tag"

ADD_TAGS: Final[ApplicationEvent] = "add_tags"

ADD_TEACHER: Final[ApplicationEvent] = "add_teacher"

ADD_TEACHERS: Final[ApplicationEvent] = "add_teachers"

ADD_USER: Final[ApplicationEvent] = "add_user"

ADD_USERS: Final[ApplicationEvent] = "add_users"

ADDED_ANSWER: Final[ApplicationEvent] = "added_answer"

ADDED_ANSWERS: Final[ApplicationEvent] = "added_answers"

ADDED_CUSTOMFIELD: Final[ApplicationEvent] = "added_customfield"

ADDED_CUSTOMFIELDS: Final[ApplicationEvent] = "added_customfields"

ADDED_DIFFICULTY: Final[ApplicationEvent] = "added_difficulty"

ADDED_DIFFICULTIES: Final[ApplicationEvent] = "added_difficulties"

ADDED_FLASHCARD: Final[ApplicationEvent] = "added_flashcard"

ADDED_FLASHCARDS: Final[ApplicationEvent] = "added_flashcards"

ADDED_IMAGE: Final[ApplicationEvent] = "added_image"

ADDED_IMAGES: Final[ApplicationEvent] = "added_images"

ADDED_NOTE: Final[ApplicationEvent] = "added_note"

ADDED_NOTES: Final[ApplicationEvent] = "added_notes"

ADDED_OPTION: Final[ApplicationEvent] = "added_option"

ADDED_OPTIONS: Final[ApplicationEvent] = "added_options"

ADDED_PRIORITY: Final[ApplicationEvent] = "added_priority"

ADDED_PRIORITIES: Final[ApplicationEvent] = "added_priorities"

ADDED_QUESTION: Final[ApplicationEvent] = "added_question"

ADDED_QUESTIONS: Final[ApplicationEvent] = "added_questions"

ADDED_REHEARSAL_RUN: Final[ApplicationEvent] = "added_rehearsal_run"

ADDED_REHEARSAL_RUNS: Final[ApplicationEvent] = "added_rehearsal_runs"

ADDED_REHEARSAL_RUN_ITEM: Final[ApplicationEvent] = "added_rehearsal_run_item"

ADDED_REHEARSAL_RUN_ITEMS: Final[ApplicationEvent] = "added_rehearsal_run_items"

ADDED_STACK: Final[ApplicationEvent] = "added_stack"

ADDED_STACKS: Final[ApplicationEvent] = "added_stacks"

ADDED_SUBJECT: Final[ApplicationEvent] = "added_subject"

ADDED_SUBJECTS: Final[ApplicationEvent] = "added_subjects"

ADDED_TAG: Final[ApplicationEvent] = "added_tag"

ADDED_TAGS: Final[ApplicationEvent] = "added_tags"

ADDED_TEACHER: Final[ApplicationEvent] = "added_teacher"

ADDED_TEACHERS: Final[ApplicationEvent] = "added_teachers"

ADDED_USER: Final[ApplicationEvent] = "added_user"

ADDED_USERS: Final[ApplicationEvent] = "added_users"

APPLICATION_STARTED: Final[ApplicationEvent] = "application_started"

APPLICATION_STARTING: Final[ApplicationEvent] = "application_starting"

APPLICATION_STOPPED: Final[ApplicationEvent] = "application_stopped"

APPLICATION_STOPPING: Final[ApplicationEvent] = "application_stopping"

CALL_FUNCTION: Final[ApplicationEvent] = "call_function"

CALL_FUNCTIONS: Final[ApplicationEvent] = "call_functions"

CANCEL_BUTTON_CLICKED: Final[ApplicationEvent] = "cancel_button_clicked"

CONFIRM_BUTTON_CLICKED: Final[ApplicationEvent] = "confirm_button_clicked"

CREATE_BUTTON_CLICKED: Final[ApplicationEvent] = "create_button_clicked"

DESTROY_WIDGET: Final[ApplicationEvent] = "destroy_widget"

DESTROY_WIDGET_CHILDREN: Final[ApplicationEvent] = "destroy_widget_children"

GET_ALL_ANSWERS: Final[ApplicationEvent] = "get_all_answers"

GET_ALL_ASSOCIATIONS: Final[ApplicationEvent] = "get_all_associations"

GET_ALL_CUSTOMFIELDS: Final[ApplicationEvent] = "get_all_customfields"

GET_ALL_DIFFICULTIES: Final[ApplicationEvent] = "get_all_difficulties"

GET_ALL_FLASHCARDS: Final[ApplicationEvent] = "get_all_flashcards"

GET_ALL_IMAGES: Final[ApplicationEvent] = "get_all_images"

GET_ALL_NOTES: Final[ApplicationEvent] = "get_all_notes"

GET_ALL_OPTIONS: Final[ApplicationEvent] = "get_all_options"

GET_ALL_PRIORITIES: Final[ApplicationEvent] = "get_all_priorities"

GET_ALL_QUESTIONS: Final[ApplicationEvent] = "get_all_questions"

GET_ALL_REHEARSAL_RUNS: Final[ApplicationEvent] = "get_all_rehearsal_runs"

GET_ALL_REHEARSAL_RUN_ITEMS: Final[ApplicationEvent] = "get_all_rehearsal_run_items"

GET_ALL_STACKS: Final[ApplicationEvent] = "get_all_stacks"

GET_ALL_SUBJECTS: Final[ApplicationEvent] = "get_all_subjects"

GET_ALL_TAGS: Final[ApplicationEvent] = "get_all_tags"

GET_ALL_TEACHERS: Final[ApplicationEvent] = "get_all_teachers"

GET_ALL_USERS: Final[ApplicationEvent] = "get_all_users"

GET_ANSWER: Final[ApplicationEvent] = "get_answer"

GET_ANSWERS: Final[ApplicationEvent] = "get_answers"

GET_ASSOCIATION: Final[ApplicationEvent] = "get_association"

GET_ASSOCIATIONS: Final[ApplicationEvent] = "get_associations"

GET_ATTRIBUTE: Final[ApplicationEvent] = "get_attribute"

GET_ATTRIBUTES: Final[ApplicationEvent] = "get_attributes"

GET_CUSTOMFIELD: Final[ApplicationEvent] = "get_customfield"

GET_CUSTOMFIELDS: Final[ApplicationEvent] = "get_customfields"

GET_DIFFICULTY: Final[ApplicationEvent] = "get_difficulty"

GET_DIFFICULTIES: Final[ApplicationEvent] = "get_difficulties"

GET_FLASHCARD: Final[ApplicationEvent] = "get_flashcard"

GET_FLASHCARDS: Final[ApplicationEvent] = "get_flashcards"

GET_FORM: Final[ApplicationEvent] = "get_form"

GET_IMAGE: Final[ApplicationEvent] = "get_image"

GET_IMAGES: Final[ApplicationEvent] = "get_images"

GET_NOTE: Final[ApplicationEvent] = "get_note"

GET_NOTES: Final[ApplicationEvent] = "get_notes"

GET_OPTION: Final[ApplicationEvent] = "get_option"

GET_OPTIONS: Final[ApplicationEvent] = "get_options"

GET_PRIORITY: Final[ApplicationEvent] = "get_priority"

GET_PRIORITIES: Final[ApplicationEvent] = "get_priorities"

GET_QUESTION: Final[ApplicationEvent] = "get_question"

GET_QUESTIONS: Final[ApplicationEvent] = "get_questions"

GET_REHEARSAL_RUN: Final[ApplicationEvent] = "get_rehearsal_run"

GET_REHEARSAL_RUNS: Final[ApplicationEvent] = "get_rehearsal_runs"

GET_REHEARSAL_RUN_ITEM: Final[ApplicationEvent] = "get_rehearsal_run_item"

GET_REHEARSAL_RUN_ITEMS: Final[ApplicationEvent] = "get_rehearsal_run_items"

GET_STACK: Final[ApplicationEvent] = "get_stack"

GET_STACKS: Final[ApplicationEvent] = "get_stacks"

GET_SUBJECT: Final[ApplicationEvent] = "get_subject"

GET_SUBJECTS: Final[ApplicationEvent] = "get_subjects"

GET_TAG: Final[ApplicationEvent] = "get_tag"

GET_TAGS: Final[ApplicationEvent] = "get_tags"

GET_TEACHER: Final[ApplicationEvent] = "get_teacher"

GET_TEACHERS: Final[ApplicationEvent] = "get_teachers"

GET_USER: Final[ApplicationEvent] = "get_user"

GET_USERS: Final[ApplicationEvent] = "get_users"

OK_BUTTON_CLICKED: Final[ApplicationEvent] = "ok_button_clicked"

REMOVE_ANSWER: Final[ApplicationEvent] = "remove_answer"

REMOVE_ANSWERS: Final[ApplicationEvent] = "remove_answers"

REMOVE_ASSOCIATION: Final[ApplicationEvent] = "remove_association"

REMOVE_ASSOCIATIONS: Final[ApplicationEvent] = "remove_associations"

REMOVE_CUSTOMFIELD: Final[ApplicationEvent] = "remove_customfield"

REMOVE_CUSTOMFIELDS: Final[ApplicationEvent] = "remove_customfields"

REMOVE_DIFFICULTY: Final[ApplicationEvent] = "remove_difficulty"

REMOVE_DIFFICULTIES: Final[ApplicationEvent] = "remove_difficulties"

REMOVE_FLASHCARD: Final[ApplicationEvent] = "remove_flashcard"

REMOVE_FLASHCARDS: Final[ApplicationEvent] = "remove_flashcards"

REMOVE_IMAGE: Final[ApplicationEvent] = "remove_image"

REMOVE_IMAGES: Final[ApplicationEvent] = "remove_images"

REMOVE_NOTE: Final[ApplicationEvent] = "remove_note"

REMOVE_NOTES: Final[ApplicationEvent] = "remove_notes"

REMOVE_OPTION: Final[ApplicationEvent] = "remove_option"

REMOVE_OPTIONS: Final[ApplicationEvent] = "remove_options"

REMOVE_PRIORITY: Final[ApplicationEvent] = "remove_priority"

REMOVE_PRIORITIES: Final[ApplicationEvent] = "remove_priorities"

REMOVE_QUESTION: Final[ApplicationEvent] = "remove_question"

REMOVE_QUESTIONS: Final[ApplicationEvent] = "remove_questions"

REMOVE_REHEARSAL_RUN: Final[ApplicationEvent] = "remove_rehearsal_run"

REMOVE_REHEARSAL_RUNS: Final[ApplicationEvent] = "remove_rehearsal_runs"

REMOVE_REHEARSAL_RUN_ITEM: Final[ApplicationEvent] = "remove_rehearsal_run_item"

REMOVE_REHEARSAL_RUN_ITEMS: Final[ApplicationEvent] = "remove_rehearsal_run_items"

REMOVE_STACK: Final[ApplicationEvent] = "remove_stack"

REMOVE_STACKS: Final[ApplicationEvent] = "remove_stacks"

REMOVE_SUBJECT: Final[ApplicationEvent] = "remove_subject"

REMOVE_SUBJECTS: Final[ApplicationEvent] = "remove_subjects"

REMOVE_TAG: Final[ApplicationEvent] = "remove_tag"

REMOVE_TAGS: Final[ApplicationEvent] = "remove_tags"

REMOVE_TEACHER: Final[ApplicationEvent] = "remove_teacher"

REMOVE_TEACHERS: Final[ApplicationEvent] = "remove_teachers"

REMOVE_USER: Final[ApplicationEvent] = "remove_user"

REMOVE_USERS: Final[ApplicationEvent] = "remove_users"

UPDATE_ANSWER: Final[ApplicationEvent] = "update_answer"

UPDATE_ANSWERS: Final[ApplicationEvent] = "update_answers"

UPDATE_ASSOCIATION: Final[ApplicationEvent] = "update_association"

UPDATE_ASSOCIATIONS: Final[ApplicationEvent] = "update_associations"

UPDATE_CUSTOMFIELD: Final[ApplicationEvent] = "update_customfield"

UPDATE_CUSTOMFIELDS: Final[ApplicationEvent] = "update_customfields"

UPDATE_DIFFICULTY: Final[ApplicationEvent] = "update_difficulty"

UPDATE_DIFFICULTIES: Final[ApplicationEvent] = "update_difficulties"

UPDATE_FLASHCARD: Final[ApplicationEvent] = "update_flashcard"

UPDATE_FLASHCARDS: Final[ApplicationEvent] = "update_flashcards"

UPDATE_IMAGE: Final[ApplicationEvent] = "update_image"

UPDATE_IMAGES: Final[ApplicationEvent] = "update_images"

UPDATE_NOTE: Final[ApplicationEvent] = "update_note"

UPDATE_NOTES: Final[ApplicationEvent] = "update_notes"

UPDATE_OPTION: Final[ApplicationEvent] = "update_option"

UPDATE_OPTIONS: Final[ApplicationEvent] = "update_options"

UPDATE_PRIORITY: Final[ApplicationEvent] = "update_priority"

UPDATE_PRIORITIES: Final[ApplicationEvent] = "update_priorities"

UPDATE_QUESTION: Final[ApplicationEvent] = "update_question"

UPDATE_QUESTIONS: Final[ApplicationEvent] = "update_questions"

UPDATE_REHEARSAL_RUN: Final[ApplicationEvent] = "update_rehearsal_run"

UPDATE_REHEARSAL_RUNS: Final[ApplicationEvent] = "update_rehearsal_runs"

UPDATE_REHEARSAL_RUN_ITEM: Final[ApplicationEvent] = "update_rehearsal_run_item"

UPDATE_REHEARSAL_RUN_ITEMS: Final[ApplicationEvent] = "update_rehearsal_run_items"

UPDATE_STACK: Final[ApplicationEvent] = "update_stack"

UPDATE_STACKS: Final[ApplicationEvent] = "update_stacks"

UPDATE_SUBJECT: Final[ApplicationEvent] = "update_subject"

UPDATE_SUBJECTS: Final[ApplicationEvent] = "update_subjects"

UPDATE_TAG: Final[ApplicationEvent] = "update_tag"

UPDATE_TAGS: Final[ApplicationEvent] = "update_tags"

UPDATE_TEACHER: Final[ApplicationEvent] = "update_teacher"

UPDATE_TEACHERS: Final[ApplicationEvent] = "update_teachers"

UPDATE_USER: Final[ApplicationEvent] = "update_user"

UPDATE_USERS: Final[ApplicationEvent] = "update_users"


# ---------- Functions ---------- #


def get_answer_events() -> tuple[ApplicationEvent, ...]:
    """
    Returns a tuple of all answer events.

    Returns:
        tuple[ApplicationEvent, ...]: A tuple of all answer events.
    """

    return (
        ADD_ANSWER,
        ADD_ANSWERS,
        REMOVE_ANSWER,
        REMOVE_ANSWERS,
        UPDATE_ANSWER,
        UPDATE_ANSWERS,
    )


def get_customfield_events() -> tuple[ApplicationEvent, ...]:
    """
    Returns a tuple of all customfield events.

    Returns:
        tuple[ApplicationEvent, ...]: A tuple of all customfield events.
    """

    return (
        ADD_CUSTOMFIELD,
        ADD_CUSTOMFIELDS,
        REMOVE_CUSTOMFIELD,
        REMOVE_CUSTOMFIELDS,
        UPDATE_CUSTOMFIELD,
        UPDATE_CUSTOMFIELDS,
    )


def get_difficulty_events() -> tuple[ApplicationEvent, ...]:
    """
    Returns a tuple of all difficulty events.

    Returns:
        tuple[ApplicationEvent, ...]: A tuple of all difficulty events.
    """

    return (
        ADD_DIFFICULTY,
        ADD_DIFFICULTIES,
        REMOVE_DIFFICULTY,
        REMOVE_DIFFICULTIES,
        UPDATE_DIFFICULTY,
        UPDATE_DIFFICULTIES,
    )


def get_event_by_name(name: str) -> ApplicationEvent:
    """
    Returns the event with the given name.

    Args:
        name (str): The name of the event.

    Returns:
        ApplicationEvent: The event with the given name.
    """

    return ApplicationEvent(name)


def get_events() -> tuple[ApplicationEvent, ...]:
    """
    Returns a tuple of all events.

    Returns:
        tuple[ApplicationEvent, ...]: A tuple of all events.
    """

    return ApplicationEvent.__args__


def get_events_dict() -> dict[str, ApplicationEvent]:
    """
    Returns a dictionary of all events.

    Returns:
        dict[str, ApplicationEvent]: A dictionary of all events.
    """

    return {event.lower(): event.upper() for event in ApplicationEvent.__args__}


def get_events_list() -> list[ApplicationEvent]:
    """
    Returns a list of all events.

    Returns:
        list[ApplicationEvent]: A list of all events.
    """

    return list(ApplicationEvent.__args__)


def get_flashcard_events() -> tuple[ApplicationEvent, ...]:
    """
    Returns a tuple of all flashcard events.

    Returns:
        tuple[ApplicationEvent, ...]: A tuple of all flashcard events.
    """

    return (
        ADD_FLASHCARD,
        ADD_FLASHCARDS,
        REMOVE_FLASHCARD,
        REMOVE_FLASHCARDS,
        UPDATE_FLASHCARD,
        UPDATE_FLASHCARDS,
    )


def get_image_events() -> tuple[ApplicationEvent, ...]:
    """
    Returns a tuple of all image events.

    Returns:
        tuple[ApplicationEvent, ...]: A tuple of all image events.
    """

    return (
        ADD_IMAGE,
        ADD_IMAGES,
        REMOVE_IMAGE,
        REMOVE_IMAGES,
        UPDATE_IMAGE,
        UPDATE_IMAGES,
    )


def get_note_events() -> tuple[..., ApplicationEvent]:
    """
    Returns a tuple of all note events.

    Returns:
        tuple[..., ApplicationEvent]: A tuple of all note events.
    """

    return (
        ADD_NOTE,
        ADD_NOTES,
        REMOVE_NOTE,
        REMOVE_NOTES,
        UPDATE_NOTE,
        UPDATE_NOTES,
    )


def get_option_events() -> tuple[..., ApplicationEvent]:
    """
    Returns a tuple of all option events.

    Returns:
        tuple[..., ApplicationEvent]: A tuple of all option events.
    """

    return (
        ADD_OPTION,
        ADD_OPTIONS,
        REMOVE_OPTION,
        REMOVE_OPTIONS,
        UPDATE_OPTION,
        UPDATE_OPTIONS,
    )


def get_priority_events() -> tuple[..., ApplicationEvent]:
    """
    Returns a tuple of all priority events.

    Returns:
        tuple[..., ApplicationEvent]: A tuple of all priority events.
    """

    return (
        ADD_PRIORITY,
        ADD_PRIORITIES,
        REMOVE_PRIORITY,
        REMOVE_PRIORITIES,
        UPDATE_PRIORITY,
        UPDATE_PRIORITIES,
    )


def get_question_events() -> tuple[..., ApplicationEvent]:
    """
    Returns a tuple of all question events.

    Returns:
        tuple[..., ApplicationEvent]: A tuple of all question events.
    """

    return (
        ADD_QUESTION,
        ADD_QUESTIONS,
        REMOVE_QUESTION,
        REMOVE_QUESTIONS,
        UPDATE_QUESTION,
        UPDATE_QUESTIONS,
    )


def get_rehearsal_run_events() -> tuple[..., ApplicationEvent]:
    """
    Returns a tuple of all rehearsal run events.

    Returns:
        tuple[..., ApplicationEvent]: A tuple of all rehearsal run events.
    """

    return (
        ADD_REHEARSAL_RUN,
        ADD_REHEARSAL_RUNS,
        REMOVE_REHEARSAL_RUN,
        REMOVE_REHEARSAL_RUNS,
        UPDATE_REHEARSAL_RUN,
        UPDATE_REHEARSAL_RUNS,
    )


def get_rehearsal_run_item_events() -> tuple[..., ApplicationEvent]:
    """
    Returns a tuple of all rehearsal run item events.

    Returns:
        tuple[..., ApplicationEvent]: A tuple of all rehearsal run item events.
    """

    return (
        ADD_REHEARSAL_RUN_ITEM,
        ADD_REHEARSAL_RUN_ITEMS,
        REMOVE_REHEARSAL_RUN_ITEM,
        REMOVE_REHEARSAL_RUN_ITEMS,
        UPDATE_REHEARSAL_RUN_ITEM,
        UPDATE_REHEARSAL_RUN_ITEMS,
    )


def get_stack_events() -> tuple[..., ApplicationEvent]:
    """
    Returns a tuple of all stack events.

    Returns:
        tuple[..., ApplicationEvent]: A tuple of all stack events.
    """

    return (
        ADD_STACK,
        ADD_STACKS,
        REMOVE_STACK,
        REMOVE_STACKS,
        UPDATE_STACK,
        UPDATE_STACKS,
    )


def get_subject_events() -> tuple[..., ApplicationEvent]:
    """
    Returns a tuple of all subject events.

    Returns:
        tuple[..., ApplicationEvent]: A tuple of all subject events.
    """

    return (
        ADD_SUBJECT,
        ADD_SUBJECTS,
        REMOVE_SUBJECT,
        REMOVE_SUBJECTS,
        UPDATE_SUBJECT,
        UPDATE_SUBJECTS,
    )


def get_tag_events() -> tuple[..., ApplicationEvent]:
    """
    Returns a tuple of all tag events.

    Returns:
        tuple[..., ApplicationEvent]: A tuple of all tag events.
    """

    return (
        ADD_TAG,
        ADD_TAGS,
        REMOVE_TAG,
        REMOVE_TAGS,
        UPDATE_TAG,
        UPDATE_TAGS,
    )


def get_teacher_events() -> tuple[..., ApplicationEvent]:
    """
    Returns a tuple of all teacher events.

    Returns:
        tuple[..., ApplicationEvent]: A tuple of all teacher events.
    """

    return (
        ADD_TEACHER,
        ADD_TEACHERS,
        REMOVE_TEACHER,
        REMOVE_TEACHERS,
        UPDATE_TEACHER,
        UPDATE_TEACHERS,
    )


def get_user_events() -> tuple[..., ApplicationEvent]:
    """
    Returns a tuple of all user events.

    Returns:
        tuple[..., ApplicationEvent]: A tuple of all user events.
    """

    return (
        ADD_USER,
        ADD_USERS,
        REMOVE_USER,
        REMOVE_USERS,
        UPDATE_USER,
        UPDATE_USERS,
    )


# ---------- Auto-Export ---------- #

# Auto-export all non-private symbols
__all__: Final[list[str]] = [
    "ADD_ANSWER",
    "ADD_ANSWERS",
    "ADD_ASSOCIATION",
    "ADD_ASSOCIATIONS",
    "ADD_CUSTOMFIELD",
    "ADD_CUSTOMFIELDS",
    "ADD_DIFFICULTY",
    "ADD_DIFFICULTIES",
    "ADD_FLASHCARD",
    "ADD_FLASHCARDS",
    "ADD_IMAGE",
    "ADD_IMAGES",
    "ADD_NOTE",
    "ADD_NOTES",
    "ADD_OPTION",
    "ADD_OPTIONS",
    "ADD_PRIORITY",
    "ADD_PRIORITIES",
    "ADD_QUESTION",
    "ADD_QUESTIONS",
    "ADD_REHEARSAL_RUN",
    "ADD_REHEARSAL_RUNS",
    "ADD_REHEARSAL_RUN_ITEM",
    "ADD_REHEARSAL_RUN_ITEMS",
    "ADD_STACK",
    "ADD_STACKS",
    "ADD_SUBJECT",
    "ADD_SUBJECTS",
    "ADD_TAG",
    "ADD_TAGS",
    "ADD_TEACHER",
    "ADD_TEACHERS",
    "ADD_USER",
    "ADD_USERS",
    "ADDED_ANSWER",
    "ADDED_ANSWERS",
    "ADDED_CUSTOMFIELD",
    "ADDED_CUSTOMFIELDS",
    "ADDED_DIFFICULTY",
    "ADDED_DIFFICULTIES",
    "ADDED_FLASHCARD",
    "ADDED_FLASHCARDS",
    "ADDED_IMAGE",
    "ADDED_IMAGES",
    "ADDED_NOTE",
    "ADDED_NOTES",
    "ADDED_OPTION",
    "ADDED_OPTIONS",
    "ADDED_PRIORITY",
    "ADDED_PRIORITIES",
    "ADDED_QUESTION",
    "ADDED_QUESTIONS",
    "ADDED_REHEARSAL_RUN",
    "ADDED_REHEARSAL_RUNS",
    "ADDED_REHEARSAL_RUN_ITEM",
    "ADDED_REHEARSAL_RUN_ITEMS",
    "ADDED_STACK",
    "ADDED_STACKS",
    "ADDED_SUBJECT",
    "ADDED_SUBJECTS",
    "ADDED_TAG",
    "ADDED_TAGS",
    "ADDED_TEACHER",
    "ADDED_TEACHERS",
    "ADDED_USER",
    "ADDED_USERS",
    "APPLICATION_STARTED",
    "APPLICATION_STARTING",
    "APPLICATION_STOPPED",
    "APPLICATION_STOPPING",
    "CALL_FUNCTION",
    "CALL_FUNCTIONS",
    "CANCEL_BUTTON_CLICKED",
    "CONFIRM_BUTTON_CLICKED",
    "CREATE_BUTTON_CLICKED",
    "DESTROY_WIDGET",
    "DESTROY_WIDGET_CHILDREN",
    "GET_ALL_ANSWERS",
    "GET_ALL_ASSOCIATIONS",
    "GET_ALL_CUSTOMFIELDS",
    "GET_ALL_DIFFICULTIES",
    "GET_ALL_FLASHCARDS",
    "GET_ALL_IMAGES",
    "GET_ALL_NOTES",
    "GET_ALL_OPTIONS",
    "GET_ALL_PRIORITIES",
    "GET_ALL_QUESTIONS",
    "GET_ALL_REHEARSAL_RUNS",
    "GET_ALL_REHEARSAL_RUN_ITEMS",
    "GET_ALL_STACKS",
    "GET_ALL_SUBJECTS",
    "GET_ALL_TAGS",
    "GET_ALL_TEACHERS",
    "GET_ALL_USERS",
    "GET_ANSWER",
    "GET_ANSWERS",
    "GET_ASSOCIATION",
    "GET_ASSOCIATIONS",
    "GET_ATTRIBUTE",
    "GET_ATTRIBUTES",
    "GET_CUSTOMFIELD",
    "GET_CUSTOMFIELDS",
    "GET_DIFFICULTY",
    "GET_DIFFICULTIES",
    "GET_FLASHCARD",
    "GET_FLASHCARDS",
    "GET_FORM",
    "GET_IMAGE",
    "GET_IMAGES",
    "GET_NOTE",
    "GET_NOTES",
    "GET_OPTION",
    "GET_OPTIONS",
    "GET_PRIORITY",
    "GET_PRIORITIES",
    "GET_QUESTION",
    "GET_QUESTIONS",
    "GET_REHEARSAL_RUN",
    "GET_REHEARSAL_RUNS",
    "GET_REHEARSAL_RUN_ITEM",
    "GET_REHEARSAL_RUN_ITEMS",
    "GET_STACK",
    "GET_STACKS",
    "GET_SUBJECT",
    "GET_SUBJECTS",
    "GET_TAG",
    "GET_TAGS",
    "GET_TEACHER",
    "GET_TEACHERS",
    "GET_USER",
    "GET_USERS",
    "OK_BUTTON_CLICKED",
    "REMOVE_ANSWER",
    "REMOVE_ANSWERS",
    "REMOVE_ASSOCIATION",
    "REMOVE_ASSOCIATIONS",
    "REMOVE_CUSTOMFIELD",
    "REMOVE_CUSTOMFIELDS",
    "REMOVE_DIFFICULTY",
    "REMOVE_DIFFICULTIES",
    "REMOVE_FLASHCARD",
    "REMOVE_FLASHCARDS",
    "REMOVE_IMAGE",
    "REMOVE_IMAGES",
    "REMOVE_NOTE",
    "REMOVE_NOTES",
    "REMOVE_OPTION",
    "REMOVE_OPTIONS",
    "REMOVE_PRIORITY",
    "REMOVE_PRIORITIES",
    "REMOVE_QUESTION",
    "REMOVE_QUESTIONS",
    "REMOVE_REHEARSAL_RUN",
    "REMOVE_REHEARSAL_RUNS",
    "REMOVE_REHEARSAL_RUN_ITEM",
    "REMOVE_REHEARSAL_RUN_ITEMS",
    "REMOVE_STACK",
    "REMOVE_STACKS",
    "REMOVE_SUBJECT",
    "REMOVE_SUBJECTS",
    "REMOVE_TAG",
    "REMOVE_TAGS",
    "REMOVE_TEACHER",
    "REMOVE_TEACHERS",
    "REMOVE_USER",
    "REMOVE_USERS",
    "UPDATE_ANSWER",
    "UPDATE_ANSWERS",
    "UPDATE_ASSOCIATION",
    "UPDATE_ASSOCIATIONS",
    "UPDATE_CUSTOMFIELD",
    "UPDATE_CUSTOMFIELDS",
    "UPDATE_DIFFICULTY",
    "UPDATE_DIFFICULTIES",
    "UPDATE_FLASHCARD",
    "UPDATE_FLASHCARDS",
    "UPDATE_IMAGE",
    "UPDATE_IMAGES",
    "UPDATE_NOTE",
    "UPDATE_NOTES",
    "UPDATE_OPTION",
    "UPDATE_OPTIONS",
    "UPDATE_PRIORITY",
    "UPDATE_PRIORITIES",
    "UPDATE_QUESTION",
    "UPDATE_QUESTIONS",
    "UPDATE_REHEARSAL_RUN",
    "UPDATE_REHEARSAL_RUNS",
    "UPDATE_REHEARSAL_RUN_ITEM",
    "UPDATE_REHEARSAL_RUN_ITEMS",
    "UPDATE_STACK",
    "UPDATE_STACKS",
    "UPDATE_SUBJECT",
    "UPDATE_SUBJECTS",
    "UPDATE_TAG",
    "UPDATE_TAGS",
    "UPDATE_TEACHER",
    "UPDATE_TEACHERS",
    "UPDATE_USER",
    "UPDATE_USERS",
    "get_answer_events",
    "get_customfield_events",
    "get_difficulty_events",
    "get_event_by_name",
    "get_events",
    "get_events_dict",
    "get_events_list",
    "get_flashcard_events",
    "get_image_events",
    "get_note_events",
    "get_option_events",
    "get_priority_events",
    "get_question_events",
    "get_rehearsal_run_events",
    "get_rehearsal_run_item_events",
    "get_stack_events",
    "get_subject_events",
    "get_tag_events",
    "get_teacher_events",
    "get_user_events",
]
