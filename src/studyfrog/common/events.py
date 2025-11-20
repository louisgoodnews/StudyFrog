"""
Author: Louis Goodnews
Date: 2025-11-16
"""

from typing import Final, Literal


# ---------- Events ---------- #

ADD_ANSWER: Final[Literal["add_answer"]] = "add_answer"

ADD_ANSWERS: Final[Literal["add_answers"]] = "add_answers"

ADD_ASSOCIATION: Final[Literal["add_association"]] = "add_association"

ADD_ASSOCIATIONS: Final[Literal["add_associations"]] = "add_associations"

ADD_CUSTOMFIELD: Final[Literal["add_customfield"]] = "add_customfield"

ADD_CUSTOMFIELDS: Final[Literal["add_customfields"]] = "add_customfields"

ADD_DIFFICULTY: Final[Literal["add_difficulty"]] = "add_difficulty"

ADD_DIFFICULTIES: Final[Literal["add_difficulties"]] = "add_difficulties"

ADD_FLASHCARD: Final[Literal["add_flashcard"]] = "add_flashcard"

ADD_FLASHCARDS: Final[Literal["add_flashcards"]] = "add_flashcards"

ADD_IMAGE: Final[Literal["add_image"]] = "add_image"

ADD_IMAGES: Final[Literal["add_images"]] = "add_images"

ADD_NOTE: Final[Literal["add_note"]] = "add_note"

ADD_NOTES: Final[Literal["add_notes"]] = "add_notes"

ADD_OPTION: Final[Literal["add_option"]] = "add_option"

ADD_OPTIONS: Final[Literal["add_options"]] = "add_options"

ADD_PRIORITY: Final[Literal["add_priority"]] = "add_priority"

ADD_PRIORITIES: Final[Literal["add_priorities"]] = "add_priorities"

ADD_QUESTION: Final[Literal["add_question"]] = "add_question"

ADD_QUESTIONS: Final[Literal["add_questions"]] = "add_questions"

ADD_REHEARSAL_RUN: Final[Literal["add_rehearsal_run"]] = "add_rehearsal_run"

ADD_REHEARSAL_RUNS: Final[Literal["add_rehearsal_runs"]] = "add_rehearsal_runs"

ADD_REHEARSAL_RUN_ITEM: Final[Literal["add_rehearsal_run_item"]] = "add_rehearsal_run_item"

ADD_REHEARSAL_RUN_ITEMS: Final[Literal["add_rehearsal_run_items"]] = "add_rehearsal_run_items"

ADD_STACK: Final[Literal["add_stack"]] = "add_stack"

ADD_STACKS: Final[Literal["add_stacks"]] = "add_stacks"

ADD_SUBJECT: Final[Literal["add_subject"]] = "add_subject"

ADD_SUBJECTS: Final[Literal["add_subjects"]] = "add_subjects"

ADD_TAG: Final[Literal["add_tag"]] = "add_tag"

ADD_TAGS: Final[Literal["add_tags"]] = "add_tags"

ADD_TEACHER: Final[Literal["add_teacher"]] = "add_teacher"

ADD_TEACHERS: Final[Literal["add_teachers"]] = "add_teachers"

ADD_USER: Final[Literal["add_user"]] = "add_user"

ADD_USERS: Final[Literal["add_users"]] = "add_users"

APPLICATION_STARTED: Final[Literal["application_started"]] = "application_started"

APPLICATION_STARTING: Final[Literal["application_starting"]] = "application_starting"

APPLICATION_STOPPED: Final[Literal["application_stopped"]] = "application_stopped"

APPLICATION_STOPPING: Final[Literal["application_stopping"]] = "application_stopping"

GET_ALL_ANSWERS: Final[Literal["get_all_answers"]] = "get_all_answers"

GET_ALL_ASSOCIATIONS: Final[Literal["get_all_associations"]] = "get_all_associations"

GET_ALL_CUSTOMFIELDS: Final[Literal["get_all_customfields"]] = "get_all_customfields"

GET_ALL_DIFFICULTIES: Final[Literal["get_all_difficulties"]] = "get_all_difficulties"

GET_ALL_FLASHCARDS: Final[Literal["get_all_flashcards"]] = "get_all_flashcards"

GET_ALL_IMAGES: Final[Literal["get_all_images"]] = "get_all_images"

GET_ALL_NOTES: Final[Literal["get_all_notes"]] = "get_all_notes"

GET_ALL_OPTIONS: Final[Literal["get_all_options"]] = "get_all_options"

GET_ALL_PRIORITIES: Final[Literal["get_all_priorities"]] = "get_all_priorities"

GET_ALL_QUESTIONS: Final[Literal["get_all_questions"]] = "get_all_questions"

GET_ALL_REHEARSAL_RUNS: Final[Literal["get_all_rehearsal_runs"]] = "get_all_rehearsal_runs"

GET_ALL_REHEARSAL_RUN_ITEMS: Final[Literal["get_all_rehearsal_run_items"]] = (
    "get_all_rehearsal_run_items"
)

GET_ALL_STACKS: Final[Literal["get_all_stacks"]] = "get_all_stacks"

GET_ALL_SUBJECTS: Final[Literal["get_all_subjects"]] = "get_all_subjects"

GET_ALL_TAGS: Final[Literal["get_all_tags"]] = "get_all_tags"

GET_ALL_TEACHERS: Final[Literal["get_all_teachers"]] = "get_all_teachers"

GET_ALL_USERS: Final[Literal["get_all_users"]] = "get_all_users"

GET_ANSWER: Final[Literal["get_answer"]] = "get_answer"

GET_ANSWERS: Final[Literal["get_answers"]] = "get_answers"

GET_ASSOCIATION: Final[Literal["get_association"]] = "get_association"

GET_ASSOCIATIONS: Final[Literal["get_associations"]] = "get_associations"

GET_CUSTOMFIELD: Final[Literal["get_customfield"]] = "get_customfield"

GET_CUSTOMFIELDS: Final[Literal["get_customfields"]] = "get_customfields"

GET_DIFFICULTY: Final[Literal["get_difficulty"]] = "get_difficulty"

GET_DIFFICULTIES: Final[Literal["get_difficulties"]] = "get_difficulties"

GET_FLASHCARD: Final[Literal["get_flashcard"]] = "get_flashcard"

GET_FLASHCARDS: Final[Literal["get_flashcards"]] = "get_flashcards"

GET_IMAGE: Final[Literal["get_image"]] = "get_image"

GET_IMAGES: Final[Literal["get_images"]] = "get_images"

GET_NOTE: Final[Literal["get_note"]] = "get_note"

GET_NOTES: Final[Literal["get_notes"]] = "get_notes"

GET_OPTION: Final[Literal["get_option"]] = "get_option"

GET_OPTIONS: Final[Literal["get_options"]] = "get_options"

GET_PRIORITY: Final[Literal["get_priority"]] = "get_priority"

GET_PRIORITIES: Final[Literal["get_priorities"]] = "get_priorities"

GET_QUESTION: Final[Literal["get_question"]] = "get_question"

GET_QUESTIONS: Final[Literal["get_questions"]] = "get_questions"

GET_REHEARSAL_RUN: Final[Literal["get_rehearsal_run"]] = "get_rehearsal_run"

GET_REHEARSAL_RUNS: Final[Literal["get_rehearsal_runs"]] = "get_rehearsal_runs"

GET_REHEARSAL_RUN_ITEM: Final[Literal["get_rehearsal_run_item"]] = "get_rehearsal_run_item"

GET_REHEARSAL_RUN_ITEMS: Final[Literal["get_rehearsal_run_items"]] = "get_rehearsal_run_items"

GET_STACK: Final[Literal["get_stack"]] = "get_stack"

GET_STACKS: Final[Literal["get_stacks"]] = "get_stacks"

GET_SUBJECT: Final[Literal["get_subject"]] = "get_subject"

GET_SUBJECTS: Final[Literal["get_subjects"]] = "get_subjects"

GET_TAG: Final[Literal["get_tag"]] = "get_tag"

GET_TAGS: Final[Literal["get_tags"]] = "get_tags"

GET_TEACHER: Final[Literal["get_teacher"]] = "get_teacher"

GET_TEACHERS: Final[Literal["get_teachers"]] = "get_teachers"

GET_USER: Final[Literal["get_user"]] = "get_user"

GET_USERS: Final[Literal["get_users"]] = "get_users"

REMOVE_ANSWER: Final[Literal["remove_answer"]] = "remove_answer"

REMOVE_ANSWERS: Final[Literal["remove_answers"]] = "remove_answers"

REMOVE_ASSOCIATION: Final[Literal["remove_association"]] = "remove_association"

REMOVE_ASSOCIATIONS: Final[Literal["remove_associations"]] = "remove_associations"

REMOVE_CUSTOMFIELD: Final[Literal["remove_customfield"]] = "remove_customfield"

REMOVE_CUSTOMFIELDS: Final[Literal["remove_customfields"]] = "remove_customfields"

REMOVE_DIFFICULTY: Final[Literal["remove_difficulty"]] = "remove_difficulty"

REMOVE_DIFFICULTIES: Final[Literal["remove_difficulties"]] = "remove_difficulties"

REMOVE_FLASHCARD: Final[Literal["remove_flashcard"]] = "remove_flashcard"

REMOVE_FLASHCARDS: Final[Literal["remove_flashcards"]] = "remove_flashcards"

REMOVE_IMAGE: Final[Literal["remove_image"]] = "remove_image"

REMOVE_IMAGES: Final[Literal["remove_images"]] = "remove_images"

REMOVE_NOTE: Final[Literal["remove_note"]] = "remove_note"

REMOVE_NOTES: Final[Literal["remove_notes"]] = "remove_notes"

REMOVE_OPTION: Final[Literal["remove_option"]] = "remove_option"

REMOVE_OPTIONS: Final[Literal["remove_options"]] = "remove_options"

REMOVE_PRIORITY: Final[Literal["remove_priority"]] = "remove_priority"

REMOVE_PRIORITIES: Final[Literal["remove_priorities"]] = "remove_priorities"

REMOVE_QUESTION: Final[Literal["remove_question"]] = "remove_question"

REMOVE_QUESTIONS: Final[Literal["remove_questions"]] = "remove_questions"

REMOVE_REHEARSAL_RUN: Final[Literal["remove_rehearsal_run"]] = "remove_rehearsal_run"

REMOVE_REHEARSAL_RUNS: Final[Literal["remove_rehearsal_runs"]] = "remove_rehearsal_runs"

REMOVE_REHEARSAL_RUN_ITEM: Final[Literal["remove_rehearsal_run_item"]] = "remove_rehearsal_run_item"

REMOVE_REHEARSAL_RUN_ITEMS: Final[Literal["remove_rehearsal_run_items"]] = (
    "remove_rehearsal_run_items"
)

REMOVE_STACK: Final[Literal["remove_stack"]] = "remove_stack"

REMOVE_STACKS: Final[Literal["remove_stacks"]] = "remove_stacks"

REMOVE_SUBJECT: Final[Literal["remove_subject"]] = "remove_subject"

REMOVE_SUBJECTS: Final[Literal["remove_subjects"]] = "remove_subjects"

REMOVE_TAG: Final[Literal["remove_tag"]] = "remove_tag"

REMOVE_TAGS: Final[Literal["remove_tags"]] = "remove_tags"

REMOVE_TEACHER: Final[Literal["remove_teacher"]] = "remove_teacher"

REMOVE_TEACHERS: Final[Literal["remove_teachers"]] = "remove_teachers"

REMOVE_USER: Final[Literal["remove_user"]] = "remove_user"

REMOVE_USERS: Final[Literal["remove_users"]] = "remove_users"

UPDATE_ANSWER: Final[Literal["update_answer"]] = "update_answer"

UPDATE_ANSWERS: Final[Literal["update_answers"]] = "update_answers"

UPDATE_ASSOCIATION: Final[Literal["update_association"]] = "update_association"

UPDATE_ASSOCIATIONS: Final[Literal["update_associations"]] = "update_associations"

UPDATE_CUSTOMFIELD: Final[Literal["update_customfield"]] = "update_customfield"

UPDATE_CUSTOMFIELDS: Final[Literal["update_customfields"]] = "update_customfields"

UPDATE_DIFFICULTY: Final[Literal["update_difficulty"]] = "update_difficulty"

UPDATE_DIFFICULTIES: Final[Literal["update_difficulties"]] = "update_difficulties"

UPDATE_FLASHCARD: Final[Literal["update_flashcard"]] = "update_flashcard"

UPDATE_FLASHCARDS: Final[Literal["update_flashcards"]] = "update_flashcards"

UPDATE_IMAGE: Final[Literal["update_image"]] = "update_image"

UPDATE_IMAGES: Final[Literal["update_images"]] = "update_images"

UPDATE_NOTE: Final[Literal["update_note"]] = "update_note"

UPDATE_NOTES: Final[Literal["update_notes"]] = "update_notes"

UPDATE_OPTION: Final[Literal["update_option"]] = "update_option"

UPDATE_OPTIONS: Final[Literal["update_options"]] = "update_options"

UPDATE_PRIORITY: Final[Literal["update_priority"]] = "update_priority"

UPDATE_PRIORITIES: Final[Literal["update_priorities"]] = "update_priorities"

UPDATE_QUESTION: Final[Literal["update_question"]] = "update_question"

UPDATE_QUESTIONS: Final[Literal["update_questions"]] = "update_questions"

UPDATE_REHEARSAL_RUN: Final[Literal["update_rehearsal_run"]] = "update_rehearsal_run"

UPDATE_REHEARSAL_RUNS: Final[Literal["update_rehearsal_runs"]] = "update_rehearsal_runs"

UPDATE_REHEARSAL_RUN_ITEM: Final[Literal["update_rehearsal_run_item"]] = "update_rehearsal_run_item"

UPDATE_REHEARSAL_RUN_ITEMS: Final[Literal["update_rehearsal_run_items"]] = (
    "update_rehearsal_run_items"
)

UPDATE_STACK: Final[Literal["update_stack"]] = "update_stack"

UPDATE_STACKS: Final[Literal["update_stacks"]] = "update_stacks"

UPDATE_SUBJECT: Final[Literal["update_subject"]] = "update_subject"

UPDATE_SUBJECTS: Final[Literal["update_subjects"]] = "update_subjects"

UPDATE_TAG: Final[Literal["update_tag"]] = "update_tag"

UPDATE_TAGS: Final[Literal["update_tags"]] = "update_tags"

UPDATE_TEACHER: Final[Literal["update_teacher"]] = "update_teacher"

UPDATE_TEACHERS: Final[Literal["update_teachers"]] = "update_teachers"

UPDATE_USER: Final[Literal["update_user"]] = "update_user"

UPDATE_USERS: Final[Literal["update_users"]] = "update_users"


# ---------- Auto-Export ---------- #

# Auto-export all non-private symbols
__all__: Final[list[str]] = [
    name for name in globals() if not name.startswith("_") and name.isidentifier()
]
