"""
Author: Louis Goodnews
Date: 2025-12-10
Description: The events module holds all the events used in the application defined as Final[str] objects.
"""

from typing import Callable, Final, Optional


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "ADD_ANSWERS_TO_DB",
    "ADD_ANSWER_TO_DB",
    "ADD_ASSOCIATION_TO_DB",
    "ADD_ASSOCIATIONS_TO_DB",
    "ADD_CUSTOMFIELDS_TO_DB",
    "ADD_CUSTOMFIELD_TO_DB",
    "ADD_DIFFICULTIES_TO_DB",
    "ADD_DIFFICULTY_TO_DB",
    "ADD_FLASHCARDS_TO_DB",
    "ADD_FLASHCARD_TO_DB",
    "ADD_IMAGES_TO_DB",
    "ADD_IMAGE_TO_DB",
    "ADD_NOTES_TO_DB",
    "ADD_NOTE_TO_DB",
    "ADD_OPTIONS_TO_DB",
    "ADD_OPTION_TO_DB",
    "ADD_PRIORITIES_TO_DB",
    "ADD_PRIORITY_TO_DB",
    "ADD_QUESTIONS_TO_DB",
    "ADD_QUESTION_TO_DB",
    "ADD_REHEARSAL_RUNS_TO_DB",
    "ADD_REHEARSAL_RUN_ITEMS_TO_DB",
    "ADD_REHEARSAL_RUN_ITEM_TO_DB",
    "ADD_REHEARSAL_RUN_TO_DB",
    "ADD_STACKS_TO_DB",
    "ADD_STACK_TO_DB",
    "ADD_SUBJECTS_TO_DB",
    "ADD_SUBJECT_TO_DB",
    "ADD_TAGS_TO_DB",
    "ADD_TAG_TO_DB",
    "ADD_TEACHERS_TO_DB",
    "ADD_TEACHER_TO_DB",
    "ADD_USERS_TO_DB",
    "ADD_USER_TO_DB",
    "ALL_ANSWERS_DELETED",
    "ALL_ANSWERS_RETRIEVED",
    "ALL_ASSOCIATIONS_DELETED",
    "ALL_ASSOCIATIONS_RETRIEVED",
    "ALL_CUSTOMFIELDS_DELETED",
    "ALL_CUSTOMFIELDS_RETRIEVED",
    "ALL_DIFFICULTIES_DELETED",
    "ALL_DIFFICULTIES_RETRIEVED",
    "ALL_FLASHCARDS_DELETED",
    "ALL_FLASHCARDS_RETRIEVED",
    "ALL_IMAGES_DELETED",
    "ALL_IMAGES_RETRIEVED",
    "ALL_NOTES_DELETED",
    "ALL_NOTES_RETRIEVED",
    "ALL_OPTIONS_DELETED",
    "ALL_OPTIONS_RETRIEVED",
    "ALL_PRIORITIES_DELETED",
    "ALL_PRIORITIES_RETRIEVED",
    "ALL_QUESTIONS_DELETED",
    "ALL_QUESTIONS_RETRIEVED",
    "ALL_REHEARSAL_RUNS_DELETED",
    "ALL_REHEARSAL_RUNS_RETRIEVED",
    "ALL_REHEARSAL_RUN_ITEMS_DELETED",
    "ALL_REHEARSAL_RUN_ITEMS_RETRIEVED",
    "ALL_STACKS_DELETED",
    "ALL_STACKS_RETRIEVED",
    "ALL_SUBJECTS_DELETED",
    "ALL_SUBJECTS_RETRIEVED",
    "ALL_TAGS_DELETED",
    "ALL_TAGS_RETRIEVED",
    "ALL_TEACHERS_DELETED",
    "ALL_TEACHERS_RETRIEVED",
    "ALL_USERS_DELETED",
    "ALL_USERS_RETRIEVED",
    "ANSWERS_ADDED",
    "ANSWERS_DELETED",
    "ANSWERS_RETRIEVED",
    "ANSWERS_UPDATED",
    "ANSWER_ADDED",
    "ANSWER_DELETED",
    "ANSWER_RETRIEVED",
    "ANSWER_UPDATED",
    "APPLICATION_STARTED",
    "APPLICATION_STARTING",
    "APPLICATION_STOPPED",
    "APPLICATION_STOPPING",
    "ASSOCIATION_ADDED",
    "ASSOCIATIONS_ADDED",
    "CLEAR_CREATE_FORM",
    "CLEAR_REHEARSAL_RUN_SETUP_FORM",
    "CLICKED_CANCEL_BUTTON",
    "CLICKED_EASY_BUTTON",
    "CLICKED_EDIT_BUTTON",
    "CLICKED_MEDIUM_BUTTON",
    "CLICKED_HARD_BUTTON",
    "CLICKED_NEXT_BUTTON",
    "CLICKED_PREVIOUS_BUTTON",
    "COUNT_WIDGET_CHILDREN",
    "CUSTOMFIELDS_ADDED",
    "CUSTOMFIELDS_DELETED",
    "CUSTOMFIELDS_RETRIEVED",
    "CUSTOMFIELDS_UPDATED",
    "CUSTOMFIELD_ADDED",
    "CUSTOMFIELD_DELETED",
    "CUSTOMFIELD_RETRIEVED",
    "CUSTOMFIELD_UPDATED",
    "DB_OPERATION_FAILURE",
    "DB_OPERATION_SUCCESS",
    "DELETE_ALL_ANSWERS_FROM_DB",
    "DELETE_ALL_ASSOCIATIONS_FROM_DB",
    "DELETE_ALL_CUSTOMFIELDS_FROM_DB",
    "DELETE_ALL_DIFFICULTIES_FROM_DB",
    "DELETE_ALL_FLASHCARDS_FROM_DB",
    "DELETE_ALL_IMAGES_FROM_DB",
    "DELETE_ALL_NOTES_FROM_DB",
    "DELETE_ALL_OPTIONS_FROM_DB",
    "DELETE_ALL_PRIORITIES_FROM_DB",
    "DELETE_ALL_QUESTIONS_FROM_DB",
    "DELETE_ALL_REHEARSAL_RUNS_FROM_DB",
    "DELETE_ALL_REHEARSAL_RUN_ITEMS_FROM_DB",
    "DELETE_ALL_STACKS_FROM_DB",
    "DELETE_ALL_SUBJECTS_FROM_DB",
    "DELETE_ALL_TAGS_FROM_DB",
    "DELETE_ALL_TEACHERS_FROM_DB",
    "DELETE_ALL_USERS_FROM_DB",
    "DELETE_ANSWERS_FROM_DB",
    "DELETE_ANSWER_FROM_DB",
    "DELETE_ASSOCIATIONS_FROM_DB",
    "DELETE_ASSOCIATION_FROM_DB",
    "DELETE_CUSTOMFIELDS_FROM_DB",
    "DELETE_CUSTOMFIELD_FROM_DB",
    "DELETE_DIFFICULTIES_FROM_DB",
    "DELETE_DIFFICULTY_FROM_DB",
    "DELETE_FLASHCARDS_FROM_DB",
    "DELETE_FLASHCARD_FROM_DB",
    "DELETE_IMAGES_FROM_DB",
    "DELETE_IMAGE_FROM_DB",
    "DELETE_NOTES_FROM_DB",
    "DELETE_NOTE_FROM_DB",
    "DELETE_OPTIONS_FROM_DB",
    "DELETE_OPTION_FROM_DB",
    "DELETE_PRIORITIES_FROM_DB",
    "DELETE_PRIORITY_FROM_DB",
    "DELETE_QUESTIONS_FROM_DB",
    "DELETE_QUESTION_FROM_DB",
    "DELETE_REHEARSAL_RUNS_FROM_DB",
    "DELETE_REHEARSAL_RUN_FROM_DB",
    "DELETE_REHEARSAL_RUN_ITEMS_FROM_DB",
    "DELETE_REHEARSAL_RUN_ITEM_FROM_DB",
    "DELETE_STACKS_FROM_DB",
    "DELETE_STACK_FROM_DB",
    "DELETE_SUBJECTS_FROM_DB",
    "DELETE_SUBJECT_FROM_DB",
    "DELETE_TAGS_FROM_DB",
    "DELETE_TAG_FROM_DB",
    "DELETE_TEACHERS_FROM_DB",
    "DELETE_TEACHER_FROM_DB",
    "DELETE_USERS_FROM_DB",
    "DELETE_USER_FROM_DB",
    "DESTROY_ANSWER_CHOICE_CREATE_FORM",
    "DESTROY_ANSWER_CREATE_FORM",
    "DESTROY_ANSWER_EDIT_FORM",
    "DESTROY_ANSWER_OPEN_ENDED_CREATE_FORM",
    "DESTROY_ANSWER_TRUE_FALSE_CREATE_FORM",
    "DESTROY_ANSWER_VIEW_FORM",
    "DESTROY_CREATE_VIEW",
    "DESTROY_DASHBOARD_VIEW",
    "DESTROY_DELETE_CONFIRMATION_VIEW",
    "DESTROY_EDIT_VIEW",
    "DESTROY_FLASHCARD_CREATE_FORM",
    "DESTROY_FLASHCARD_EDIT_FORM",
    "DESTROY_FLASHCARD_REHEARSAL_VIEW",
    "DESTROY_FLASHCARD_VIEW_FORM",
    "DESTROY_NOTE_CREATE_FORM",
    "DESTROY_NOTE_EDIT_FORM",
    "DESTROY_NOTE_REHEARSAL_VIEW",
    "DESTROY_NOTE_VIEW_FORM",
    "DESTROY_QUESTION_CREATE_FORM",
    "DESTROY_QUESTION_EDIT_FORM",
    "DESTROY_QUESTION_REHEARSAL_VIEW",
    "DESTROY_QUESTION_VIEW_FORM",
    "DESTROY_REHEARSAL_RUN_RESULT_VIEW",
    "DESTROY_REHEARSAL_RUN_SETUP_VIEW",
    "DESTROY_REHEARSAL_RUN_VIEW",
    "DESTROY_SEARCH_VIEW",
    "DESTROY_SETTINGS_VIEW",
    "DESTROY_STACK_CREATE_FORM",
    "DESTROY_STACK_EDIT_FORM",
    "DESTROY_STACK_VIEW_FORM",
    "DESTROY_SUBJECT_EDIT_FORM",
    "DESTROY_SUBJECT_VIEW_FORM",
    "DESTROY_TEACHER_EDIT_FORM",
    "DESTROY_TEACHER_VIEW_FORM",
    "DESTROY_VIEW_VIEW",
    "DESTROY_WIDGET_CHILDREN",
    "DIFFICULTIES_ADDED",
    "DIFFICULTIES_DELETED",
    "DIFFICULTIES_RETRIEVED",
    "DIFFICULTIES_UPDATED",
    "DIFFICULTY_ADDED",
    "DIFFICULTY_DELETED",
    "DIFFICULTY_RETRIEVED",
    "DIFFICULTY_UPDATED",
    "FILTER_ANSWERS_FROM_DB",
    "FILTER_ASSOCIATIONS_FROM_DB",
    "FILTER_CUSTOMFIELDS_FROM_DB",
    "FILTER_DIFFICULTIES_FROM_DB",
    "FILTER_FLASHCARDS_FROM_DB",
    "FILTER_IMAGES_FROM_DB",
    "FILTER_NOTES_FROM_DB",
    "FILTER_OPTIONS_FROM_DB",
    "FILTER_QUESTIONS_FROM_DB",
    "FILTER_REHEARSAL_RUNS_FROM_DB",
    "FILTER_REHEARSAL_RUN_ITEMS_FROM_DB",
    "FILTER_STACKS_FROM_DB",
    "FILTER_SUBJECTS_FROM_DB",
    "FILTER_TAGS_FROM_DB",
    "FILTER_TEACHERS_FROM_DB",
    "FILTER_USERS_FROM_DB",
    "FLASHCARDS_ADDED",
    "FLASHCARDS_DELETED",
    "FLASHCARD_FLIPPED",
    "FLASHCARDS_RETRIEVED",
    "FLASHCARDS_UPDATED",
    "FLASHCARD_ADDED",
    "FLASHCARD_DELETED",
    "FLASHCARD_RETRIEVED",
    "FLASHCARD_UPDATED",
    "GET_ALL_ANSWERS_FROM_DB",
    "GET_ALL_ASSOCIATIONS_FROM_DB",
    "GET_ALL_CUSTOMFIELDS_FROM_DB",
    "GET_ALL_DIFFICULTIES_FROM_DB",
    "GET_ALL_FLASHCARDS_FROM_DB",
    "GET_ALL_IMAGES_FROM_DB",
    "GET_ALL_NOTES_FROM_DB",
    "GET_ALL_OPTIONS_FROM_DB",
    "GET_ALL_PRIORITIES_FROM_DB",
    "GET_ALL_QUESTIONS_FROM_DB",
    "GET_ALL_REHEARSAL_RUNS_FROM_DB",
    "GET_ALL_REHEARSAL_RUN_ITEMS_FROM_DB",
    "GET_ALL_STACKS_FROM_DB",
    "GET_ALL_SUBJECTS_FROM_DB",
    "GET_ALL_TAGS_FROM_DB",
    "GET_ALL_TEACHERS_FROM_DB",
    "GET_ALL_USERS_FROM_DB",
    "GET_ANSWER_CHOICE_CREATE_FORM",
    "GET_ANSWER_CREATE_FORM",
    "GET_ANSWERS_FROM_DB",
    "GET_ANSWER_EDIT_FORM",
    "GET_ANSWER_FROM_DB",
    "GET_ANSWER_MODEL_DICT",
    "GET_ANSWER_OPEN_ENDED_CREATE_FORM",
    "GET_ANSWER_TRUE_FALSE_CREATE_FORM",
    "GET_ANSWER_VIEW_FORM",
    "GET_ASSOCIATION_FROM_DB",
    "GET_ASSOCIATION_MODEL_DICT",
    "GET_ASSOCIATIONS_FROM_DB",
    "GET_CREATE_FORM",
    "GET_CREATE_VIEW",
    "GET_CUSTOMFIELDS_FROM_DB",
    "GET_CUSTOMFIELD_FROM_DB",
    "GET_DASHBOARD_VIEW",
    "GET_DELETE_CONFIRMATION_VIEW",
    "GET_DIFFICULTIES_FROM_DB",
    "GET_DIFFICULTY_FROM_DB",
    "GET_EDIT_FORM",
    "GET_EDIT_VIEW",
    "GET_ERROR_TOAST",
    "GET_FLASHCARDS_FROM_DB",
    "GET_FLASHCARD_CREATE_FORM",
    "GET_FLASHCARD_EDIT_FORM",
    "GET_FLASHCARD_FROM_DB",
    "GET_FLASHCARD_MODEL_DICT",
    "GET_FLASHCARD_REHEARSAL_VIEW",
    "GET_FLASHCARD_VIEW_FORM",
    "GET_IMAGES_FROM_DB",
    "GET_IMAGE_FROM_DB",
    "GET_INFO_TOAST",
    "GET_NOTES_FROM_DB",
    "GET_NOTE_CREATE_FORM",
    "GET_NOTE_EDIT_FORM",
    "GET_NOTE_FROM_DB",
    "GET_NOTE_MODEL_DICT",
    "GET_NOTE_REHEARSAL_VIEW",
    "GET_NOTE_VIEW_FORM",
    "GET_OPTIONS_FROM_DB",
    "GET_OPTION_FROM_DB",
    "GET_PRIORITIES_FROM_DB",
    "GET_PRIORITY_FROM_DB",
    "GET_QUESTIONS_FROM_DB",
    "GET_QUESTION_CREATE_FORM",
    "GET_QUESTION_EDIT_FORM",
    "GET_QUESTION_FROM_DB",
    "GET_QUESTION_MODEL_DICT",
    "GET_QUESTION_REHEARSAL_VIEW",
    "GET_QUESTION_VIEW_FORM",
    "GET_REHEARSAL_RUN_MODEL_DICT",
    "GET_REHEARSAL_RUNS_FROM_DB",
    "GET_REHEARSAL_RUN_FROM_DB",
    "GET_REHEARSAL_RUN_ITEMS_FROM_DB",
    "GET_REHEARSAL_RUN_ITEM_FROM_DB",
    "GET_REHEARSAL_RUN_ITEM_MODEL_DICT",
    "GET_REHEARSAL_RUN_RESULT_VIEW",
    "GET_REHEARSAL_RUN_SETUP_FORM",
    "GET_REHEARSAL_RUN_SETUP_VIEW",
    "GET_REHEARSAL_RUN_VIEW",
    "GET_SEARCH_VIEW",
    "GET_SETTINGS_VIEW",
    "GET_STACK_CREATE_FORM",
    "GET_STACK_EDIT_FORM",
    "GET_STACK_FROM_DB",
    "GET_STACK_MODEL_DICT",
    "GET_STACK_VIEW_FORM",
    "GET_STACKS_FROM_DB",
    "GET_SUBJECTS_FROM_DB",
    "GET_SUBJECT_EDIT_FORM",
    "GET_SUBJECT_FROM_DB",
    "GET_SUBJECT_VIEW_FORM",
    "GET_SUCCESS_TOAST",
    "GET_TAGS_FROM_DB",
    "GET_TAG_FROM_DB",
    "GET_TEACHERS_FROM_DB",
    "GET_TEACHER_EDIT_FORM",
    "GET_TEACHER_FROM_DB",
    "GET_TEACHER_VIEW_FORM",
    "GET_USER_FROM_DB",
    "GET_USERS_FROM_DB",
    "GET_VIEW_VIEW",
    "GET_WARNING_TOAST",
    "GET_WIDGET_CHILDREN",
    "IMAGES_ADDED",
    "IMAGES_DELETED",
    "IMAGES_RETRIEVED",
    "IMAGES_UPDATED",
    "IMAGE_ADDED",
    "IMAGE_DELETED",
    "IMAGE_RETRIEVED",
    "IMAGE_UPDATED",
    "LOAD_REHEARSAL_VIEW_FORM",
    "NOTES_ADDED",
    "NOTES_DELETED",
    "NOTES_RETRIEVED",
    "NOTES_UPDATED",
    "NOTE_ADDED",
    "NOTE_DELETED",
    "NOTE_RETRIEVED",
    "NOTE_UPDATED",
    "OPTIONS_ADDED",
    "OPTIONS_DELETED",
    "OPTIONS_RETRIEVED",
    "OPTIONS_UPDATED",
    "OPTION_ADDED",
    "OPTION_DELETED",
    "OPTION_RETRIEVED",
    "OPTION_UPDATED",
    "PRIORITIES_ADDED",
    "PRIORITIES_DELETED",
    "PRIORITIES_RETRIEVED",
    "PRIORITIES_UPDATED",
    "PRIORITY_ADDED",
    "PRIORITY_DELETED",
    "PRIORITY_RETRIEVED",
    "PRIORITY_UPDATED",
    "QUESTIONS_ADDED",
    "QUESTIONS_DELETED",
    "QUESTIONS_RETRIEVED",
    "QUESTIONS_UPDATED",
    "QUESTION_ADDED",
    "QUESTION_DELETED",
    "QUESTION_RETRIEVED",
    "QUESTION_UPDATED",
    "REHEARSAL_RUNS_ADDED",
    "REHEARSAL_RUNS_DELETED",
    "REHEARSAL_RUNS_RETRIEVED",
    "REHEARSAL_RUNS_UPDATED",
    "REHEARSAL_RUN_ADDED",
    "REHEARSAL_RUN_DELETED",
    "REHEARSAL_RUN_INDEX_DECREMENTED",
    "REHEARSAL_RUN_INDEX_INCREMENTED",
    "REHEARSAL_RUN_INDEX_MAX_REACHED",
    "REHEARSAL_RUN_INDEX_MIN_REACHED",
    "REHEARSAL_RUN_ITEMS_ADDED",
    "REHEARSAL_RUN_ITEMS_DELETED",
    "REHEARSAL_RUN_ITEMS_RETRIEVED",
    "REHEARSAL_RUN_ITEMS_UPDATED",
    "REHEARSAL_RUN_ITEM_ADDED",
    "REHEARSAL_RUN_ITEM_DELETED",
    "REHEARSAL_RUN_ITEM_RETRIEVED",
    "REHEARSAL_RUN_ITEM_UPDATED",
    "REHEARSAL_RUN_RETRIEVED",
    "REHEARSAL_RUN_UPDATED",
    "RESET_CREATE_FORM",
    "SET_CREATE_FORM",
    "SET_EDIT_FORM",
    "SET_VIEW_FORM",
    "STACKS_ADDED",
    "STACKS_DELETED",
    "STACKS_RETRIEVED",
    "STACKS_UPDATED",
    "STACK_ADDED",
    "STACK_DELETED",
    "STACK_RETRIEVED",
    "STACK_UPDATED",
    "SUBJECTS_ADDED",
    "SUBJECTS_DELETED",
    "SUBJECTS_RETRIEVED",
    "SUBJECTS_UPDATED",
    "SUBJECT_ADDED",
    "SUBJECT_DELETED",
    "SUBJECT_RETRIEVED",
    "SUBJECT_UPDATED",
    "TAGS_ADDED",
    "TAGS_DELETED",
    "TAGS_RETRIEVED",
    "TAGS_UPDATED",
    "TAG_ADDED",
    "TAG_DELETED",
    "TAG_RETRIEVED",
    "TAG_UPDATED",
    "TEACHERS_ADDED",
    "TEACHERS_DELETED",
    "TEACHERS_RETRIEVED",
    "TEACHERS_UPDATED",
    "TEACHER_ADDED",
    "TEACHER_DELETED",
    "TEACHER_RETRIEVED",
    "TEACHER_UPDATED",
    "UPDATE_ANSWERS_IN_DB",
    "UPDATE_ANSWER_IN_DB",
    "UPDATE_ASSOCIATIONS_IN_DB",
    "UPDATE_ASSOCIATION_IN_DB",
    "UPDATE_CUSTOMFIELDS_IN_DB",
    "UPDATE_CUSTOMFIELD_IN_DB",
    "UPDATE_DIFFICULTIES_IN_DB",
    "UPDATE_DIFFICULTY_IN_DB",
    "UPDATE_FLASHCARDS_IN_DB",
    "UPDATE_FLASHCARD_IN_DB",
    "UPDATE_IMAGES_IN_DB",
    "UPDATE_IMAGE_IN_DB",
    "UPDATE_NOTES_IN_DB",
    "UPDATE_NOTE_IN_DB",
    "UPDATE_OPTIONS_IN_DB",
    "UPDATE_OPTION_IN_DB",
    "UPDATE_PRIORITIES_IN_DB",
    "UPDATE_PRIORITY_IN_DB",
    "UPDATE_QUESTIONS_IN_DB",
    "UPDATE_QUESTION_IN_DB",
    "UPDATE_REHEARSAL_RUNS_IN_DB",
    "UPDATE_REHEARSAL_RUN_IN_DB",
    "UPDATE_REHEARSAL_RUN_ITEMS_IN_DB",
    "UPDATE_REHEARSAL_RUN_ITEM_IN_DB",
    "UPDATE_STACKS_IN_DB",
    "UPDATE_STACK_IN_DB",
    "UPDATE_SUBJECTS_IN_DB",
    "UPDATE_SUBJECT_IN_DB",
    "UPDATE_TAGS_IN_DB",
    "UPDATE_TAG_IN_DB",
    "UPDATE_TEACHERS_IN_DB",
    "UPDATE_TEACHER_IN_DB",
    "UPDATE_USERS_IN_DB",
    "UPDATE_USER_IN_DB",
    "USERS_ADDED",
    "USERS_DELETED",
    "USERS_RETRIEVED",
    "USERS_UPDATED",
    "USER_ADDED",
    "USER_DELETED",
    "USER_RETRIEVED",
    "USER_UPDATED",
    "get_all_events",
    "get_answer_events",
    "get_customfield_events",
    "get_difficulty_events",
    "get_event_by_name",
    "get_events_by_names",
    "get_events_by_prefix",
    "get_events_by_prefixes",
    "get_flashcard_events",
    "get_image_events",
    "get_note_events",
    "get_option_events",
    "get_priority_events",
    "get_rehearsal_run_events",
    "get_rehearsal_run_item_events",
    "get_stack_events",
    "get_subject_events",
    "get_tag_events",
    "get_teacher_events",
    "get_user_events",
    "get_utility_events",
]


# ---------- Constants ---------- #

ADD_ANSWER_TO_DB: Final[str] = "broadcast:request:add_answer_to_db"
ADD_ANSWERS_TO_DB: Final[str] = "broadcast:request:add_answers_to_db"
FILTER_ANSWERS_FROM_DB: Final[str] = "broadcast:request:filter_answers_from_db"
GET_ANSWER_FROM_DB: Final[str] = "broadcast:request:get_answer_from_db"
GET_ANSWER_MODEL_DICT: Final[str] = "broadcast:request:get_answer_model_dict"
GET_ANSWERS_FROM_DB: Final[str] = "broadcast:request:get_answers_from_db"
GET_ALL_ANSWERS_FROM_DB: Final[str] = "broadcast:request:get_all_answers_from_db"
DELETE_ANSWER_FROM_DB: Final[str] = "broadcast:request:delete_answer_from_db"
DELETE_ANSWERS_FROM_DB: Final[str] = "broadcast:request:delete_answers_from_db"
DELETE_ALL_ANSWERS_FROM_DB: Final[str] = "broadcast:request:delete_all_answers_from_db"
UPDATE_ANSWER_IN_DB: Final[str] = "broadcast:request:update_answer_in_db"
UPDATE_ANSWERS_IN_DB: Final[str] = "broadcast:request:update_answers_in_db"
ANSWER_ADDED: Final[str] = "broadcast:notification:answer_added"
ANSWERS_ADDED: Final[str] = "broadcast:notification:answers_added"
ANSWER_DELETED: Final[str] = "broadcast:notification:answer_deleted"
ANSWERS_DELETED: Final[str] = "broadcast:notification:answers_deleted"
ALL_ANSWERS_DELETED: Final[str] = "broadcast:notification:all_answers_deleted"
ANSWER_RETRIEVED: Final[str] = "broadcast:notification:answer_retrieved"
ANSWERS_RETRIEVED: Final[str] = "broadcast:notification:answers_retrieved"
ALL_ANSWERS_RETRIEVED: Final[str] = "broadcast:notification:all_answers_retrieved"
ANSWER_UPDATED: Final[str] = "broadcast:notification:answer_updated"
ANSWERS_UPDATED: Final[str] = "broadcast:notification:answers_updated"

ADD_ASSOCIATION_TO_DB: Final[str] = "broadcast:request:add_association_to_db"
ADD_ASSOCIATIONS_TO_DB: Final[str] = "broadcast:request:add_associations_to_db"
FILTER_ASSOCIATIONS_FROM_DB: Final[str] = "broadcast:request:filter_associations_from_db"
GET_ASSOCIATION_FROM_DB: Final[str] = "broadcast:request:get_association_from_db"
GET_ASSOCIATION_MODEL_DICT: Final[str] = "broadcast:request:get_association_model_dict"
GET_ASSOCIATIONS_FROM_DB: Final[str] = "broadcast:request:get_associations_from_db"
GET_ALL_ASSOCIATIONS_FROM_DB: Final[str] = "broadcast:request:get_all_associations_from_db"
DELETE_ASSOCIATION_FROM_DB: Final[str] = "broadcast:request:delete_association_from_db"
DELETE_ASSOCIATIONS_FROM_DB: Final[str] = "broadcast:request:delete_associations_from_db"
DELETE_ALL_ASSOCIATIONS_FROM_DB: Final[str] = "broadcast:request:delete_all_associations_from_db"
UPDATE_ASSOCIATION_IN_DB: Final[str] = "broadcast:request:update_association_in_db"
UPDATE_ASSOCIATIONS_IN_DB: Final[str] = "broadcast:request:update_associations_in_db"
ASSOCIATION_ADDED: Final[str] = "broadcast:notification:association_added"
ASSOCIATIONS_ADDED: Final[str] = "broadcast:notification:associations_added"
ASSOCIATION_DELETED: Final[str] = "broadcast:notification:association_deleted"
ASSOCIATIONS_DELETED: Final[str] = "broadcast:notification:associations_deleted"
ALL_ASSOCIATIONS_DELETED: Final[str] = "broadcast:notification:all_associations_deleted"
ASSOCIATION_RETRIEVED: Final[str] = "broadcast:notification:association_retrieved"
ASSOCIATIONS_RETRIEVED: Final[str] = "broadcast:notification:associations_retrieved"
ALL_ASSOCIATIONS_RETRIEVED: Final[str] = "broadcast:notification:all_associations_retrieved"
ASSOCIATION_UPDATED: Final[str] = "broadcast:notification:association_updated"
ASSOCIATIONS_UPDATED: Final[str] = "broadcast:notification:associations_updated"

ADD_CUSTOMFIELD_TO_DB: Final[str] = "broadcast:request:add_customfield_to_db"
ADD_CUSTOMFIELDS_TO_DB: Final[str] = "broadcast:request:add_customfields_to_db"
FILTER_CUSTOMFIELDS_FROM_DB: Final[str] = "broadcast:request:filter_customfields_from_db"
GET_CUSTOMFIELD_FROM_DB: Final[str] = "broadcast:request:get_customfield_from_db"
GET_CUSTOMFIELDS_FROM_DB: Final[str] = "broadcast:request:get_customfields_from_db"
GET_ALL_CUSTOMFIELDS_FROM_DB: Final[str] = "broadcast:request:get_all_customfields_from_db"
DELETE_CUSTOMFIELD_FROM_DB: Final[str] = "broadcast:request:delete_customfield_from_db"
DELETE_CUSTOMFIELDS_FROM_DB: Final[str] = "broadcast:request:delete_customfields_from_db"
DELETE_ALL_CUSTOMFIELDS_FROM_DB: Final[str] = "broadcast:request:delete_all_customfields_from_db"
UPDATE_CUSTOMFIELD_IN_DB: Final[str] = "broadcast:request:update_customfield_in_db"
UPDATE_CUSTOMFIELDS_IN_DB: Final[str] = "broadcast:request:update_customfields_in_db"
CUSTOMFIELD_ADDED: Final[str] = "broadcast:notification:customfield_added"
CUSTOMFIELDS_ADDED: Final[str] = "broadcast:notification:customfields_added"
CUSTOMFIELD_DELETED: Final[str] = "broadcast:notification:customfield_deleted"
CUSTOMFIELDS_DELETED: Final[str] = "broadcast:notification:customfields_deleted"
ALL_CUSTOMFIELDS_DELETED: Final[str] = "broadcast:notification:all_customfields_deleted"
CUSTOMFIELD_RETRIEVED: Final[str] = "broadcast:notification:customfield_retrieved"
CUSTOMFIELDS_RETRIEVED: Final[str] = "broadcast:notification:customfields_retrieved"
ALL_CUSTOMFIELDS_RETRIEVED: Final[str] = "broadcast:notification:all_customfields_retrieved"
CUSTOMFIELD_UPDATED: Final[str] = "broadcast:notification:customfield_updated"
CUSTOMFIELDS_UPDATED: Final[str] = "broadcast:notification:customfields_updated"

ADD_DIFFICULTY_TO_DB: Final[str] = "broadcast:request:add_difficulty_to_db"
ADD_DIFFICULTIES_TO_DB: Final[str] = "broadcast:request:add_difficulties_to_db"
FILTER_DIFFICULTIES_FROM_DB: Final[str] = "broadcast:request:filter_difficulties_from_db"
GET_DIFFICULTY_FROM_DB: Final[str] = "broadcast:request:get_difficulty_from_db"
GET_DIFFICULTIES_FROM_DB: Final[str] = "broadcast:request:get_difficulties_from_db"
GET_ALL_DIFFICULTIES_FROM_DB: Final[str] = "broadcast:request:get_all_difficulties_from_db"
DELETE_DIFFICULTY_FROM_DB: Final[str] = "broadcast:request:delete_difficulty_from_db"
DELETE_DIFFICULTIES_FROM_DB: Final[str] = "broadcast:request:delete_difficulties_from_db"
DELETE_ALL_DIFFICULTIES_FROM_DB: Final[str] = "broadcast:request:delete_all_difficulties_from_db"
UPDATE_DIFFICULTY_IN_DB: Final[str] = "broadcast:request:update_difficulty_in_db"
UPDATE_DIFFICULTIES_IN_DB: Final[str] = "broadcast:request:update_difficulties_in_db"
DIFFICULTY_ADDED: Final[str] = "broadcast:notification:difficulty_added"
DIFFICULTIES_ADDED: Final[str] = "broadcast:notification:difficulties_added"
DIFFICULTY_DELETED: Final[str] = "broadcast:notification:difficulty_deleted"
DIFFICULTIES_DELETED: Final[str] = "broadcast:notification:difficulties_deleted"
ALL_DIFFICULTIES_DELETED: Final[str] = "broadcast:notification:all_difficulties_deleted"
DIFFICULTY_RETRIEVED: Final[str] = "broadcast:notification:difficulty_retrieved"
DIFFICULTIES_RETRIEVED: Final[str] = "broadcast:notification:difficulties_retrieved"
ALL_DIFFICULTIES_RETRIEVED: Final[str] = "broadcast:notification:all_difficulties_retrieved"
DIFFICULTY_UPDATED: Final[str] = "broadcast:notification:difficulty_updated"
DIFFICULTIES_UPDATED: Final[str] = "broadcast:notification:difficulties_updated"

ADD_FLASHCARD_TO_DB: Final[str] = "broadcast:request:add_flashcard_to_db"
ADD_FLASHCARDS_TO_DB: Final[str] = "broadcast:request:add_flashcards_to_db"
FILTER_FLASHCARDS_FROM_DB: Final[str] = "broadcast:request:filter_flashcards_from_db"
GET_FLASHCARD_FROM_DB: Final[str] = "broadcast:request:get_flashcard_from_db"
GET_FLASHCARD_MODEL_DICT: Final[str] = "broadcast:request:get_flashcard_model_dict"
GET_FLASHCARDS_FROM_DB: Final[str] = "broadcast:request:get_flashcards_from_db"
GET_ALL_FLASHCARDS_FROM_DB: Final[str] = "broadcast:request:get_all_flashcards_from_db"
DELETE_FLASHCARD_FROM_DB: Final[str] = "broadcast:request:delete_flashcard_from_db"
DELETE_FLASHCARDS_FROM_DB: Final[str] = "broadcast:request:delete_flashcards_from_db"
DELETE_ALL_FLASHCARDS_FROM_DB: Final[str] = "broadcast:request:delete_all_flashcards_from_db"
UPDATE_FLASHCARD_IN_DB: Final[str] = "broadcast:request:update_flashcard_in_db"
UPDATE_FLASHCARDS_IN_DB: Final[str] = "broadcast:request:update_flashcards_in_db"
FLASHCARD_ADDED: Final[str] = "broadcast:notification:flashcard_added"
FLASHCARDS_ADDED: Final[str] = "broadcast:notification:flashcards_added"
FLASHCARD_DELETED: Final[str] = "broadcast:notification:flashcard_deleted"
FLASHCARDS_DELETED: Final[str] = "broadcast:notification:flashcards_deleted"
ALL_FLASHCARDS_DELETED: Final[str] = "broadcast:notification:all_flashcards_deleted"
FLASHCARD_RETRIEVED: Final[str] = "broadcast:notification:flashcard_retrieved"
FLASHCARDS_RETRIEVED: Final[str] = "broadcast:notification:flashcards_retrieved"
ALL_FLASHCARDS_RETRIEVED: Final[str] = "broadcast:notification:all_flashcards_retrieved"
FLASHCARD_UPDATED: Final[str] = "broadcast:notification:flashcard_updated"
FLASHCARDS_UPDATED: Final[str] = "broadcast:notification:flashcards_updated"

ADD_IMAGE_TO_DB: Final[str] = "broadcast:request:add_image_to_db"
ADD_IMAGES_TO_DB: Final[str] = "broadcast:request:add_images_to_db"
FILTER_IMAGES_FROM_DB: Final[str] = "broadcast:request:filter_images_from_db"
GET_IMAGE_FROM_DB: Final[str] = "broadcast:request:get_image_from_db"
GET_IMAGES_FROM_DB: Final[str] = "broadcast:request:get_images_from_db"
GET_ALL_IMAGES_FROM_DB: Final[str] = "broadcast:request:get_all_images_from_db"
DELETE_IMAGE_FROM_DB: Final[str] = "broadcast:request:delete_image_from_db"
DELETE_IMAGES_FROM_DB: Final[str] = "broadcast:request:delete_images_from_db"
DELETE_ALL_IMAGES_FROM_DB: Final[str] = "broadcast:request:delete_all_images_from_db"
UPDATE_IMAGE_IN_DB: Final[str] = "broadcast:request:update_image_in_db"
UPDATE_IMAGES_IN_DB: Final[str] = "broadcast:request:update_images_in_db"
IMAGE_ADDED: Final[str] = "broadcast:notification:image_added"
IMAGES_ADDED: Final[str] = "broadcast:notification:images_added"
IMAGE_DELETED: Final[str] = "broadcast:notification:image_deleted"
IMAGES_DELETED: Final[str] = "broadcast:notification:images_deleted"
ALL_IMAGES_DELETED: Final[str] = "broadcast:notification:all_images_deleted"
IMAGE_RETRIEVED: Final[str] = "broadcast:notification:image_retrieved"
IMAGES_RETRIEVED: Final[str] = "broadcast:notification:images_retrieved"
ALL_IMAGES_RETRIEVED: Final[str] = "broadcast:notification:all_images_retrieved"
IMAGE_UPDATED: Final[str] = "broadcast:notification:image_updated"
IMAGES_UPDATED: Final[str] = "broadcast:notification:images_updated"

ADD_NOTE_TO_DB: Final[str] = "broadcast:request:add_note_to_db"
ADD_NOTES_TO_DB: Final[str] = "broadcast:request:add_notes_to_db"
FILTER_NOTES_FROM_DB: Final[str] = "broadcast:request:filter_notes_from_db"
GET_NOTE_FROM_DB: Final[str] = "broadcast:request:get_note_from_db"
GET_NOTE_MODEL_DICT: Final[str] = "broadcast:request:get_note_model_dict"
GET_NOTES_FROM_DB: Final[str] = "broadcast:request:get_notes_from_db"
GET_ALL_NOTES_FROM_DB: Final[str] = "broadcast:request:get_all_notes_from_db"
DELETE_NOTE_FROM_DB: Final[str] = "broadcast:request:delete_note_from_db"
DELETE_NOTES_FROM_DB: Final[str] = "broadcast:request:delete_notes_from_db"
DELETE_ALL_NOTES_FROM_DB: Final[str] = "broadcast:request:delete_all_notes_from_db"
UPDATE_NOTE_IN_DB: Final[str] = "broadcast:request:update_note_in_db"
UPDATE_NOTES_IN_DB: Final[str] = "broadcast:request:update_notes_in_db"
NOTE_ADDED: Final[str] = "broadcast:notification:note_added"
NOTES_ADDED: Final[str] = "broadcast:notification:notes_added"
NOTE_DELETED: Final[str] = "broadcast:notification:note_deleted"
NOTES_DELETED: Final[str] = "broadcast:notification:notes_deleted"
ALL_NOTES_DELETED: Final[str] = "broadcast:notification:all_notes_deleted"
NOTE_RETRIEVED: Final[str] = "broadcast:notification:note_retrieved"
NOTES_RETRIEVED: Final[str] = "broadcast:notification:notes_retrieved"
ALL_NOTES_RETRIEVED: Final[str] = "broadcast:notification:all_notes_retrieved"
NOTE_UPDATED: Final[str] = "broadcast:notification:note_updated"
NOTES_UPDATED: Final[str] = "broadcast:notification:notes_updated"

ADD_OPTION_TO_DB: Final[str] = "broadcast:request:add_option_to_db"
ADD_OPTIONS_TO_DB: Final[str] = "broadcast:request:add_options_to_db"
FILTER_OPTIONS_FROM_DB: Final[str] = "broadcast:request:filter_options_from_db"
GET_OPTION_FROM_DB: Final[str] = "broadcast:request:get_option_from_db"
GET_OPTIONS_FROM_DB: Final[str] = "broadcast:request:get_options_from_db"
GET_ALL_OPTIONS_FROM_DB: Final[str] = "broadcast:request:get_all_options_from_db"
DELETE_OPTION_FROM_DB: Final[str] = "broadcast:request:delete_option_from_db"
DELETE_OPTIONS_FROM_DB: Final[str] = "broadcast:request:delete_options_from_db"
DELETE_ALL_OPTIONS_FROM_DB: Final[str] = "broadcast:request:delete_all_options_from_db"
UPDATE_OPTION_IN_DB: Final[str] = "broadcast:request:update_option_in_db"
UPDATE_OPTIONS_IN_DB: Final[str] = "broadcast:request:update_options_in_db"
OPTION_ADDED: Final[str] = "broadcast:notification:option_added"
OPTIONS_ADDED: Final[str] = "broadcast:notification:options_added"
OPTION_DELETED: Final[str] = "broadcast:notification:option_deleted"
OPTIONS_DELETED: Final[str] = "broadcast:notification:options_deleted"
ALL_OPTIONS_DELETED: Final[str] = "broadcast:notification:all_options_deleted"
OPTION_RETRIEVED: Final[str] = "broadcast:notification:option_retrieved"
OPTIONS_RETRIEVED: Final[str] = "broadcast:notification:options_retrieved"
ALL_OPTIONS_RETRIEVED: Final[str] = "broadcast:notification:all_options_retrieved"
OPTION_UPDATED: Final[str] = "broadcast:notification:option_updated"
OPTIONS_UPDATED: Final[str] = "broadcast:notification:options_updated"

ADD_PRIORITY_TO_DB: Final[str] = "broadcast:request:add_priority_to_db"
ADD_PRIORITIES_TO_DB: Final[str] = "broadcast:request:add_priorities_to_db"
FILTER_PRIORITIES_FROM_DB: Final[str] = "broadcast:request:filter_priorities_from_db"
GET_PRIORITY_FROM_DB: Final[str] = "broadcast:request:get_priority_from_db"
GET_PRIORITIES_FROM_DB: Final[str] = "broadcast:request:get_priorities_from_db"
GET_ALL_PRIORITIES_FROM_DB: Final[str] = "broadcast:request:get_all_priorities_from_db"
DELETE_PRIORITY_FROM_DB: Final[str] = "broadcast:request:delete_priority_from_db"
DELETE_PRIORITIES_FROM_DB: Final[str] = "broadcast:request:delete_priorities_from_db"
DELETE_ALL_PRIORITIES_FROM_DB: Final[str] = "broadcast:request:delete_all_priorities_from_db"
UPDATE_PRIORITY_IN_DB: Final[str] = "broadcast:request:update_priority_in_db"
UPDATE_PRIORITIES_IN_DB: Final[str] = "broadcast:request:update_priorities_in_db"
PRIORITY_ADDED: Final[str] = "broadcast:notification:priority_added"
PRIORITIES_ADDED: Final[str] = "broadcast:notification:priorities_added"
PRIORITY_DELETED: Final[str] = "broadcast:notification:priority_deleted"
PRIORITIES_DELETED: Final[str] = "broadcast:notification:priorities_deleted"
ALL_PRIORITIES_DELETED: Final[str] = "broadcast:notification:all_priorities_deleted"
PRIORITY_RETRIEVED: Final[str] = "broadcast:notification:priority_retrieved"
PRIORITIES_RETRIEVED: Final[str] = "broadcast:notification:priorities_retrieved"
ALL_PRIORITIES_RETRIEVED: Final[str] = "broadcast:notification:all_priorities_retrieved"
PRIORITY_UPDATED: Final[str] = "broadcast:notification:priority_updated"
PRIORITIES_UPDATED: Final[str] = "broadcast:notification:priorities_updated"

ADD_QUESTION_TO_DB: Final[str] = "broadcast:request:add_question_to_db"
ADD_QUESTIONS_TO_DB: Final[str] = "broadcast:request:add_questions_to_db"
FILTER_QUESTIONS_FROM_DB: Final[str] = "broadcast:request:filter_questions_from_db"
GET_QUESTION_FROM_DB: Final[str] = "broadcast:request:get_question_from_db"
GET_QUESTION_MODEL_DICT: Final[str] = "broadcast:request:get_question_model_dict"
GET_QUESTIONS_FROM_DB: Final[str] = "broadcast:request:get_questions_from_db"
GET_ALL_QUESTIONS_FROM_DB: Final[str] = "broadcast:request:get_all_questions_from_db"
DELETE_QUESTION_FROM_DB: Final[str] = "broadcast:request:delete_question_from_db"
DELETE_QUESTIONS_FROM_DB: Final[str] = "broadcast:request:delete_questions_from_db"
DELETE_ALL_QUESTIONS_FROM_DB: Final[str] = "broadcast:request:delete_all_questions_from_db"
UPDATE_QUESTION_IN_DB: Final[str] = "broadcast:request:update_question_in_db"
UPDATE_QUESTIONS_IN_DB: Final[str] = "broadcast:request:update_questions_in_db"
QUESTION_ADDED: Final[str] = "broadcast:notification:question_added"
QUESTIONS_ADDED: Final[str] = "broadcast:notification:questions_added"
QUESTION_DELETED: Final[str] = "broadcast:notification:question_deleted"
QUESTIONS_DELETED: Final[str] = "broadcast:notification:questions_deleted"
ALL_QUESTIONS_DELETED: Final[str] = "broadcast:notification:all_questions_deleted"
QUESTION_RETRIEVED: Final[str] = "broadcast:notification:question_retrieved"
QUESTIONS_RETRIEVED: Final[str] = "broadcast:notification:questions_retrieved"
ALL_QUESTIONS_RETRIEVED: Final[str] = "broadcast:notification:all_questions_retrieved"
QUESTION_UPDATED: Final[str] = "broadcast:notification:question_updated"
QUESTIONS_UPDATED: Final[str] = "broadcast:notification:questions_updated"

ADD_REHEARSAL_RUN_TO_DB: Final[str] = "broadcast:request:add_rehearsal_run_to_db"
ADD_REHEARSAL_RUNS_TO_DB: Final[str] = "broadcast:request:add_rehearsal_runs_to_db"
FILTER_REHEARSAL_RUNS_FROM_DB: Final[str] = "broadcast:request:filter_rehearsal_runs_from_db"
GET_REHEARSAL_RUN_FROM_DB: Final[str] = "broadcast:request:get_rehearsal_run_from_db"
GET_REHEARSAL_RUNS_FROM_DB: Final[str] = "broadcast:request:get_rehearsal_runs_from_db"
GET_ALL_REHEARSAL_RUNS_FROM_DB: Final[str] = "broadcast:request:get_all_rehearsal_runs_from_db"
DELETE_REHEARSAL_RUN_FROM_DB: Final[str] = "broadcast:request:delete_rehearsal_run_from_db"
DELETE_REHEARSAL_RUNS_FROM_DB: Final[str] = "broadcast:request:delete_rehearsal_runs_from_db"
DELETE_ALL_REHEARSAL_RUNS_FROM_DB: Final[str] = (
    "broadcast:request:delete_all_rehearsal_runs_from_db"
)
UPDATE_REHEARSAL_RUN_IN_DB: Final[str] = "broadcast:request:update_rehearsal_run_in_db"
UPDATE_REHEARSAL_RUNS_IN_DB: Final[str] = "broadcast:request:update_rehearsal_runs_in_db"
REHEARSAL_RUN_ADDED: Final[str] = "broadcast:notification:rehearsal_run_added"
REHEARSAL_RUNS_ADDED: Final[str] = "broadcast:notification:rehearsal_runs_added"
REHEARSAL_RUN_DELETED: Final[str] = "broadcast:notification:rehearsal_run_deleted"
REHEARSAL_RUNS_DELETED: Final[str] = "broadcast:notification:rehearsal_runs_deleted"
ALL_REHEARSAL_RUNS_DELETED: Final[str] = "broadcast:notification:all_rehearsal_runs_deleted"
REHEARSAL_RUN_RETRIEVED: Final[str] = "broadcast:notification:rehearsal_run_retrieved"
REHEARSAL_RUNS_RETRIEVED: Final[str] = "broadcast:notification:rehearsal_runs_retrieved"
ALL_REHEARSAL_RUNS_RETRIEVED: Final[str] = "broadcast:notification:all_rehearsal_runs_retrieved"
REHEARSAL_RUN_UPDATED: Final[str] = "broadcast:notification:rehearsal_run_updated"
REHEARSAL_RUNS_UPDATED: Final[str] = "broadcast:notification:rehearsal_runs_updated"

ADD_REHEARSAL_RUN_ITEM_TO_DB: Final[str] = "broadcast:request:add_rehearsal_run_item_to_db"
ADD_REHEARSAL_RUN_ITEMS_TO_DB: Final[str] = "broadcast:request:add_rehearsal_run_items_to_db"
FILTER_REHEARSAL_RUN_ITEMS_FROM_DB: Final[str] = (
    "broadcast:request:filter_rehearsal_run_items_from_db"
)
GET_REHEARSAL_RUN_ITEM_FROM_DB: Final[str] = "broadcast:request:get_rehearsal_run_item_from_db"
GET_REHEARSAL_RUN_ITEMS_FROM_DB: Final[str] = "broadcast:request:get_rehearsal_run_items_from_db"
GET_ALL_REHEARSAL_RUN_ITEMS_FROM_DB: Final[str] = (
    "broadcast:request:get_all_rehearsal_run_items_from_db"
)
DELETE_REHEARSAL_RUN_ITEM_FROM_DB: Final[str] = (
    "broadcast:request:delete_rehearsal_run_item_from_db"
)
DELETE_REHEARSAL_RUN_ITEMS_FROM_DB: Final[str] = (
    "broadcast:request:delete_rehearsal_run_items_from_db"
)
GET_REHEARSAL_RUN_ITEM_MODEL_DICT: Final[str] = (
    "broadcast:request:get_rehearsal_run_item_model_dict"
)
DELETE_ALL_REHEARSAL_RUN_ITEMS_FROM_DB: Final[str] = (
    "broadcast:request:delete_all_rehearsal_run_items_from_db"
)
GET_REHEARSAL_RUN_MODEL_DICT: Final[str] = "broadcast:request:get_rehearsal_run_model_dict"
UPDATE_REHEARSAL_RUN_ITEM_IN_DB: Final[str] = "broadcast:request:update_rehearsal_run_item_in_db"
UPDATE_REHEARSAL_RUN_ITEMS_IN_DB: Final[str] = "broadcast:request:update_rehearsal_run_items_in_db"
REHEARSAL_RUN_ITEM_ADDED: Final[str] = "broadcast:notification:rehearsal_run_item_added"
REHEARSAL_RUN_ITEMS_ADDED: Final[str] = "broadcast:notification:rehearsal_run_items_added"
REHEARSAL_RUN_ITEM_DELETED: Final[str] = "broadcast:notification:rehearsal_run_item_deleted"
REHEARSAL_RUN_ITEMS_DELETED: Final[str] = "broadcast:notification:rehearsal_run_items_deleted"
ALL_REHEARSAL_RUN_ITEMS_DELETED: Final[str] = (
    "broadcast:notification:all_rehearsal_run_items_deleted"
)
REHEARSAL_RUN_ITEM_RETRIEVED: Final[str] = "broadcast:notification:rehearsal_run_item_retrieved"
REHEARSAL_RUN_ITEMS_RETRIEVED: Final[str] = "broadcast:notification:rehearsal_run_items_retrieved"
ALL_REHEARSAL_RUN_ITEMS_RETRIEVED: Final[str] = (
    "broadcast:notification:all_rehearsal_run_items_retrieved"
)
REHEARSAL_RUN_ITEM_UPDATED: Final[str] = "broadcast:notification:rehearsal_run_item_updated"
REHEARSAL_RUN_ITEMS_UPDATED: Final[str] = "broadcast:notification:rehearsal_run_items_updated"

ADD_STACK_TO_DB: Final[str] = "broadcast:request:add_stack_to_db"
ADD_STACKS_TO_DB: Final[str] = "broadcast:request:add_stacks_to_db"
FILTER_STACKS_FROM_DB: Final[str] = "broadcast:request:filter_stacks_from_db"
GET_STACK_FROM_DB: Final[str] = "broadcast:request:get_stack_from_db"
GET_STACK_MODEL_DICT: Final[str] = "broadcast:request:get_stack_model_dict"
GET_STACKS_FROM_DB: Final[str] = "broadcast:request:get_stacks_from_db"
GET_ALL_STACKS_FROM_DB: Final[str] = "broadcast:request:get_all_stacks_from_db"
DELETE_STACK_FROM_DB: Final[str] = "broadcast:request:delete_stack_from_db"
DELETE_STACKS_FROM_DB: Final[str] = "broadcast:request:delete_stacks_from_db"
DELETE_ALL_STACKS_FROM_DB: Final[str] = "broadcast:request:delete_all_stacks_from_db"
UPDATE_STACK_IN_DB: Final[str] = "broadcast:request:update_stack_in_db"
UPDATE_STACKS_IN_DB: Final[str] = "broadcast:request:update_stacks_in_db"
STACK_ADDED: Final[str] = "broadcast:notification:stack_added"
STACKS_ADDED: Final[str] = "broadcast:notification:stacks_added"
STACK_DELETED: Final[str] = "broadcast:notification:stack_deleted"
STACKS_DELETED: Final[str] = "broadcast:notification:stacks_deleted"
ALL_STACKS_DELETED: Final[str] = "broadcast:notification:all_stacks_deleted"
STACK_RETRIEVED: Final[str] = "broadcast:notification:stack_retrieved"
STACKS_RETRIEVED: Final[str] = "broadcast:notification:stacks_retrieved"
ALL_STACKS_RETRIEVED: Final[str] = "broadcast:notification:all_stacks_retrieved"
STACK_UPDATED: Final[str] = "broadcast:notification:stack_updated"
STACKS_UPDATED: Final[str] = "broadcast:notification:stacks_updated"

ADD_SUBJECT_TO_DB: Final[str] = "broadcast:request:add_subject_to_db"
ADD_SUBJECTS_TO_DB: Final[str] = "broadcast:request:add_subjects_to_db"
FILTER_SUBJECTS_FROM_DB: Final[str] = "broadcast:request:filter_subjects_from_db"
GET_SUBJECT_FROM_DB: Final[str] = "broadcast:request:get_subject_from_db"
GET_SUBJECTS_FROM_DB: Final[str] = "broadcast:request:get_subjects_from_db"
GET_ALL_SUBJECTS_FROM_DB: Final[str] = "broadcast:request:get_all_subjects_from_db"
DELETE_SUBJECT_FROM_DB: Final[str] = "broadcast:request:delete_subject_from_db"
DELETE_SUBJECTS_FROM_DB: Final[str] = "broadcast:request:delete_subjects_from_db"
DELETE_ALL_SUBJECTS_FROM_DB: Final[str] = "broadcast:request:delete_all_subjects_from_db"
UPDATE_SUBJECT_IN_DB: Final[str] = "broadcast:request:update_subject_in_db"
UPDATE_SUBJECTS_IN_DB: Final[str] = "broadcast:request:update_subjects_in_db"
SUBJECT_ADDED: Final[str] = "broadcast:notification:subject_added"
SUBJECTS_ADDED: Final[str] = "broadcast:notification:subjects_added"
SUBJECT_DELETED: Final[str] = "broadcast:notification:subject_deleted"
SUBJECTS_DELETED: Final[str] = "broadcast:notification:subjects_deleted"
ALL_SUBJECTS_DELETED: Final[str] = "broadcast:notification:all_subjects_deleted"
SUBJECT_RETRIEVED: Final[str] = "broadcast:notification:subject_retrieved"
SUBJECTS_RETRIEVED: Final[str] = "broadcast:notification:subjects_retrieved"
ALL_SUBJECTS_RETRIEVED: Final[str] = "broadcast:notification:all_subjects_retrieved"
SUBJECT_UPDATED: Final[str] = "broadcast:notification:subject_updated"
SUBJECTS_UPDATED: Final[str] = "broadcast:notification:subjects_updated"

ADD_TAG_TO_DB: Final[str] = "broadcast:request:add_tag_to_db"
ADD_TAGS_TO_DB: Final[str] = "broadcast:request:add_tags_to_db"
FILTER_TAGS_FROM_DB: Final[str] = "broadcast:request:filter_tags_from_db"
GET_TAG_FROM_DB: Final[str] = "broadcast:request:get_tag_from_db"
GET_TAGS_FROM_DB: Final[str] = "broadcast:request:get_tags_from_db"
GET_ALL_TAGS_FROM_DB: Final[str] = "broadcast:request:get_all_tags_from_db"
DELETE_TAG_FROM_DB: Final[str] = "broadcast:request:delete_tag_from_db"
DELETE_TAGS_FROM_DB: Final[str] = "broadcast:request:delete_tags_from_db"
DELETE_ALL_TAGS_FROM_DB: Final[str] = "broadcast:request:delete_all_tags_from_db"
UPDATE_TAG_IN_DB: Final[str] = "broadcast:request:update_tag_in_db"
UPDATE_TAGS_IN_DB: Final[str] = "broadcast:request:update_tags_in_db"
TAG_ADDED: Final[str] = "broadcast:notification:tag_added"
TAGS_ADDED: Final[str] = "broadcast:notification:tags_added"
TAG_DELETED: Final[str] = "broadcast:notification:tag_deleted"
TAGS_DELETED: Final[str] = "broadcast:notification:tags_deleted"
ALL_TAGS_DELETED: Final[str] = "broadcast:notification:all_tags_deleted"
TAG_RETRIEVED: Final[str] = "broadcast:notification:tag_retrieved"
TAGS_RETRIEVED: Final[str] = "broadcast:notification:tags_retrieved"
ALL_TAGS_RETRIEVED: Final[str] = "broadcast:notification:all_tags_retrieved"
TAG_UPDATED: Final[str] = "broadcast:notification:tag_updated"
TAGS_UPDATED: Final[str] = "broadcast:notification:tags_updated"

ADD_TEACHER_TO_DB: Final[str] = "broadcast:request:add_teacher_to_db"
ADD_TEACHERS_TO_DB: Final[str] = "broadcast:request:add_teachers_to_db"
FILTER_TEACHERS_FROM_DB: Final[str] = "broadcast:request:filter_teachers_from_db"
GET_TEACHER_FROM_DB: Final[str] = "broadcast:request:get_teacher_from_db"
GET_TEACHERS_FROM_DB: Final[str] = "broadcast:request:get_teachers_from_db"
GET_ALL_TEACHERS_FROM_DB: Final[str] = "broadcast:request:get_all_teachers_from_db"
DELETE_TEACHER_FROM_DB: Final[str] = "broadcast:request:delete_teacher_from_db"
DELETE_TEACHERS_FROM_DB: Final[str] = "broadcast:request:delete_teachers_from_db"
DELETE_ALL_TEACHERS_FROM_DB: Final[str] = "broadcast:request:delete_all_teachers_from_db"
UPDATE_TEACHER_IN_DB: Final[str] = "broadcast:request:update_teacher_in_db"
UPDATE_TEACHERS_IN_DB: Final[str] = "broadcast:request:update_teachers_in_db"
TEACHER_ADDED: Final[str] = "broadcast:notification:teacher_added"
TEACHERS_ADDED: Final[str] = "broadcast:notification:teachers_added"
TEACHER_DELETED: Final[str] = "broadcast:notification:teacher_deleted"
TEACHERS_DELETED: Final[str] = "broadcast:notification:teachers_deleted"
ALL_TEACHERS_DELETED: Final[str] = "broadcast:notification:all_teachers_deleted"
TEACHER_RETRIEVED: Final[str] = "broadcast:notification:teacher_retrieved"
TEACHERS_RETRIEVED: Final[str] = "broadcast:notification:teachers_retrieved"
ALL_TEACHERS_RETRIEVED: Final[str] = "broadcast:notification:all_teachers_retrieved"
TEACHER_UPDATED: Final[str] = "broadcast:notification:teacher_updated"
TEACHERS_UPDATED: Final[str] = "broadcast:notification:teachers_updated"

ADD_USER_TO_DB: Final[str] = "broadcast:request:add_user_to_db"
ADD_USERS_TO_DB: Final[str] = "broadcast:request:add_users_to_db"
FILTER_USERS_FROM_DB: Final[str] = "broadcast:request:filter_users_from_db"
GET_USER_FROM_DB: Final[str] = "broadcast:request:get_user_from_db"
GET_USERS_FROM_DB: Final[str] = "broadcast:request:get_users_from_db"
GET_ALL_USERS_FROM_DB: Final[str] = "broadcast:request:get_all_users_from_db"
DELETE_USER_FROM_DB: Final[str] = "broadcast:request:delete_user_from_db"
DELETE_USERS_FROM_DB: Final[str] = "broadcast:request:delete_users_from_db"
DELETE_ALL_USERS_FROM_DB: Final[str] = "broadcast:request:delete_all_users_from_db"
UPDATE_USER_IN_DB: Final[str] = "broadcast:request:update_user_in_db"
UPDATE_USERS_IN_DB: Final[str] = "broadcast:request:update_users_in_db"
USER_ADDED: Final[str] = "broadcast:notification:user_added"
USERS_ADDED: Final[str] = "broadcast:notification:users_added"
USER_DELETED: Final[str] = "broadcast:notification:user_deleted"
USERS_DELETED: Final[str] = "broadcast:notification:users_deleted"
ALL_USERS_DELETED: Final[str] = "broadcast:notification:all_users_deleted"
USER_RETRIEVED: Final[str] = "broadcast:notification:user_retrieved"
USERS_RETRIEVED: Final[str] = "broadcast:notification:users_retrieved"
ALL_USERS_RETRIEVED: Final[str] = "broadcast:notification:all_users_retrieved"
USER_UPDATED: Final[str] = "broadcast:notification:user_updated"
USERS_UPDATED: Final[str] = "broadcast:notification:users_updated"

# UI
DESTROY_ANSWER_EDIT_FORM: Final[str] = "broadcast:request:destroy_answer_edit_form"
GET_ANSWER_EDIT_FORM: Final[str] = "broadcast:request:get_answer_edit_form"
DESTROY_ANSWER_VIEW_FORM: Final[str] = "broadcast:request:destroy_answer_view_form"
GET_ANSWER_VIEW_FORM: Final[str] = "broadcast:request:get_answer_view_form"

GET_ANSWER_CHOICE_CREATE_FORM: Final[str] = "broadcast:request:get_answer_choice_create_form"
DESTROY_ANSWER_CHOICE_CREATE_FORM: Final[str] = (
    "broadcast:request:destroy_answer_choice_create_form"
)
GET_ANSWER_CREATE_FORM: Final[str] = "broadcast:request:get_answer_create_form"
DESTROY_ANSWER_CREATE_FORM: Final[str] = "broadcast:request:destroy_answer_create_form"
GET_ANSWER_OPEN_ENDED_CREATE_FORM: Final[str] = (
    "broadcast:request:get_answer_open_ended_create_form"
)
DESTROY_ANSWER_OPEN_ENDED_CREATE_FORM: Final[str] = (
    "broadcast:request:destroy_answer_open_ended_create_form"
)
GET_ANSWER_TRUE_FALSE_CREATE_FORM: Final[str] = (
    "broadcast:request:get_answer_true_false_create_form"
)
DESTROY_ANSWER_TRUE_FALSE_CREATE_FORM: Final[str] = (
    "broadcast:request:destroy_answer_true_false_create_form"
)

CLEAR_CREATE_FORM: Final[str] = "broadcast:request:clear_create_form"
GET_CREATE_FORM: Final[str] = "broadcast:request:get_create_form"
RESET_CREATE_FORM: Final[str] = "broadcast:request:reset_create_form"
SET_CREATE_FORM: Final[str] = "broadcast:request:set_create_form"
GET_EDIT_FORM: Final[str] = "broadcast:request:get_edit_form"
SET_EDIT_FORM: Final[str] = "broadcast:request:set_edit_form"
GET_VIEW_FORM: Final[str] = "broadcast:request:get_view_form"
SET_VIEW_FORM: Final[str] = "broadcast:request:set_view_form"

DESTROY_CREATE_VIEW: Final[str] = "broadcast:request:destroy_create_view"
GET_CREATE_VIEW: Final[str] = "broadcast:request:get_create_view"

DESTROY_DASHBOARD_VIEW: Final[str] = "broadcast:request:destroy_dashboard_view"
GET_DASHBOARD_VIEW: Final[str] = "broadcast:request:get_dashboard_view"

DESTROY_DELETE_CONFIRMATION_VIEW: Final[str] = "broadcast:request:destroy_delete_confirmation_view"
GET_DELETE_CONFIRMATION_VIEW: Final[str] = "broadcast:request:get_delete_confirmation_view"

DESTROY_EDIT_VIEW: Final[str] = "broadcast:request:destroy_edit_view"
GET_EDIT_VIEW: Final[str] = "broadcast:request:get_edit_view"

DESTROY_FLASHCARD_CREATE_FORM: Final[str] = "broadcast:request:destroy_flashcard_create_form"
GET_FLASHCARD_CREATE_FORM: Final[str] = "broadcast:request:get_flashcard_create_form"
DESTROY_FLASHCARD_EDIT_FORM: Final[str] = "broadcast:request:destroy_flashcard_edit_form"
GET_FLASHCARD_EDIT_FORM: Final[str] = "broadcast:request:get_flashcard_edit_form"
DESTROY_FLASHCARD_REHEARSAL_VIEW: Final[str] = "broadcast:request:destroy_flashcard_rehearsal_view"
GET_FLASHCARD_REHEARSAL_VIEW: Final[str] = "broadcast:request:get_flashcard_rehearsal_view"
DESTROY_FLASHCARD_VIEW_FORM: Final[str] = "broadcast:request:destroy_flashcard_view_form"
GET_FLASHCARD_VIEW_FORM: Final[str] = "broadcast:request:get_flashcard_view_form"

FLASHCARD_FLIPPED: Final[str] = "broadcast:notify:flashcard_flipped"

DESTROY_NOTE_CREATE_FORM: Final[str] = "broadcast:request:destroy_note_create_form"
GET_NOTE_CREATE_FORM: Final[str] = "broadcast:request:get_note_create_form"
DESTROY_NOTE_EDIT_FORM: Final[str] = "broadcast:request:destroy_note_edit_form"
GET_NOTE_EDIT_FORM: Final[str] = "broadcast:request:get_note_edit_form"
DESTROY_NOTE_REHEARSAL_VIEW: Final[str] = "broadcast:request:destroy_note_rehearsal_view"
GET_NOTE_REHEARSAL_VIEW: Final[str] = "broadcast:request:get_note_rehearsal_view"
DESTROY_NOTE_VIEW_FORM: Final[str] = "broadcast:request:destroy_note_view_form"
GET_NOTE_VIEW_FORM: Final[str] = "broadcast:request:get_note_view_form"

DESTROY_QUESTION_CREATE_FORM: Final[str] = "broadcast:request:destroy_question_create_form"
GET_QUESTION_CREATE_FORM: Final[str] = "broadcast:request:get_question_create_form"
DESTROY_QUESTION_EDIT_FORM: Final[str] = "broadcast:request:destroy_question_edit_form"
GET_QUESTION_EDIT_FORM: Final[str] = "broadcast:request:get_question_edit_form"
DESTROY_QUESTION_REHEARSAL_VIEW: Final[str] = "broadcast:request:destroy_question_rehearsal_view"
GET_QUESTION_REHEARSAL_VIEW: Final[str] = "broadcast:request:get_question_rehearsal_view"
DESTROY_QUESTION_VIEW_FORM: Final[str] = "broadcast:request:destroy_question_view_form"
GET_QUESTION_VIEW_FORM: Final[str] = "broadcast:request:get_question_view_form"

DESTROY_REHEARSAL_RUN_RESULT_VIEW: Final[str] = (
    "broadcast:request:destroy_rehearsal_run_result_view"
)
GET_REHEARSAL_RUN_RESULT_VIEW: Final[str] = "broadcast:request:get_rehearsal_run_result_view"
DESTROY_REHEARSAL_RUN_SETUP_VIEW: Final[str] = "broadcast:request:destroy_rehearsal_run_setup_view"
CLEAR_REHEARSAL_RUN_SETUP_FORM: Final[str] = "broadcast:request:clear_rehearsal_run_setup_form"
GET_REHEARSAL_RUN_SETUP_FORM: Final[str] = "broadcast:request:get_rehearsal_run_setup_form"
GET_REHEARSAL_RUN_SETUP_VIEW: Final[str] = "broadcast:request:get_rehearsal_run_setup_view"
DESTROY_REHEARSAL_RUN_VIEW: Final[str] = "broadcast:request:destroy_rehearsal_run_view"
GET_REHEARSAL_RUN_VIEW: Final[str] = "broadcast:request:get_rehearsal_run_view"
LOAD_REHEARSAL_VIEW_FORM: Final[str] = "broadcast:request:load_rehearsal_view_form"

DESTROY_SEARCH_VIEW: Final[str] = "broadcast:request:destroy_search_view"
GET_SEARCH_VIEW: Final[str] = "broadcast:request:get_search_view"

DESTROY_SETTINGS_VIEW: Final[str] = "broadcast:request:destroy_settings_view"
GET_SETTINGS_VIEW: Final[str] = "broadcast:request:get_settings_view"

DESTROY_STACK_CREATE_FORM: Final[str] = "broadcast:request:destroy_stack_create_form"
GET_STACK_CREATE_FORM: Final[str] = "broadcast:request:get_stack_create_form"
DESTROY_STACK_EDIT_FORM: Final[str] = "broadcast:request:destroy_stack_edit_form"
GET_STACK_EDIT_FORM: Final[str] = "broadcast:request:get_stack_edit_form"
DESTROY_STACK_VIEW_FORM: Final[str] = "broadcast:request:destroy_stack_view_form"
GET_STACK_VIEW_FORM: Final[str] = "broadcast:request:get_stack_view_form"

DESTROY_TEACHER_EDIT_FORM: Final[str] = "broadcast:request:destroy_teacher_edit_form"
GET_TEACHER_EDIT_FORM: Final[str] = "broadcast:request:get_teacher_edit_form"
DESTROY_TEACHER_VIEW_FORM: Final[str] = "broadcast:request:destroy_teacher_view_form"
GET_TEACHER_VIEW_FORM: Final[str] = "broadcast:request:get_teacher_view_form"

DESTROY_SUBJECT_EDIT_FORM: Final[str] = "broadcast:request:destroy_subject_edit_form"
GET_SUBJECT_EDIT_FORM: Final[str] = "broadcast:request:get_subject_edit_form"
DESTROY_SUBJECT_VIEW_FORM: Final[str] = "broadcast:request:destroy_subject_view_form"
GET_SUBJECT_VIEW_FORM: Final[str] = "broadcast:request:get_subject_view_form"

DESTROY_VIEW_VIEW: Final[str] = "broadcast:request:destroy_view_view"
GET_VIEW_VIEW: Final[str] = "broadcast:request:get_view_view"

COUNT_WIDGET_CHILDREN: Final[str] = "broadcast:request:count_widget_children"
DESTROY_WIDGET_CHILDREN: Final[str] = "broadcast:request:destroy_widget_children"
GET_WIDGET_CHILDREN: Final[str] = "broadcast:request:get_widget_children"

GET_ERROR_TOAST: Final[str] = "broadcast:request:get_error_toast"
GET_INFO_TOAST: Final[str] = "broadcast:request:get_info_toast"
GET_SUCCESS_TOAST: Final[str] = "broadcast:request:get_success_toast"
GET_WARNING_TOAST: Final[str] = "broadcast:request:get_warning_toast"

CLICKED_NEXT_BUTTON: Final[str] = "broadcast:notification:clicked_next_button"
CLICKED_PREVIOUS_BUTTON: Final[str] = "broadcast:notification:clicked_previous_button"
CLICKED_EASY_BUTTON: Final[str] = "broadcast:notification:clicked_easy_button"
CLICKED_MEDIUM_BUTTON: Final[str] = "broadcast:notification:clicked_medium_button"
CLICKED_HARD_BUTTON: Final[str] = "broadcast:notification:clicked_hard_button"
CLICKED_CANCEL_BUTTON: Final[str] = "broadcast:notification:clicked_cancel_button"
CLICKED_EDIT_BUTTON: Final[str] = "broadcast:notification:clicked_edit_button"

REHEARSAL_RUN_INDEX_DECREMENTED: Final[str] = (
    "broadcast:notification:rehearsal_run_index_decremented"
)
REHEARSAL_RUN_INDEX_INCREMENTED: Final[str] = (
    "broadcast:notification:rehearsal_run_index_incremented"
)
REHEARSAL_RUN_INDEX_MAX_REACHED: Final[str] = (
    "broadcast:notification:rehearsal_run_index_max_reached"
)
REHEARSAL_RUN_INDEX_MIN_REACHED: Final[str] = (
    "broadcast:notification:rehearsal_run_index_min_reached"
)

# UTILITIES
APPLICATION_STARTED: Final[str] = "broadcast:notification:application_started"
APPLICATION_STARTING: Final[str] = "broadcast:notification:application_starting"
APPLICATION_STOPPED: Final[str] = "broadcast:notification:application_stopped"
APPLICATION_STOPPING: Final[str] = "broadcast:notification:application_stopping"
DB_OPERATION_FAILURE: Final[str] = "broadcast:notification:db_operation_failure"
DB_OPERATION_SUCCESS: Final[str] = "broadcast:notification:db_operation_success"


# ---------- Helper Functions ---------- #


def _filter_events_by_prefix(prefix: str) -> list[str]:
    """
    Returns a list of events filtered by a specified prefix.

    Args:
        prefix (str): The prefix to filter events by.

    Returns:
        list[str]: The list of events filtered by the specified prefix.
    """

    return list(
        filter(
            lambda event: event.startswith(prefix.upper()),
            [
                key
                for (
                    key,
                    value,
                ) in globals().items()
                if key.isupper()
                and isinstance(
                    value,
                    str,
                )
            ],
        )
    )


def _filter_events_by_prefixes(prefixes: list[str]) -> list[str]:
    """
    Returns a list of events filtered by a specified list of prefixes.

    Args:
        prefixes (list[str]): The list of prefixes to filter events by.

    Returns:
        list[str]: The list of events filtered by the specified prefix.
    """

    result: list[str] = []

    for prefix in prefixes:
        result.extend(_filter_events_by_prefix(prefix=prefix))

    return result


# ---------- Functions ---------- #


def get_all_events() -> list[str]:
    """
    Returns a list of all events.

    Args:
        None

    Returns:
        list[str]: The list of all events.
    """

    return [
        value
        for (
            key,
            value,
        ) in globals().items()
        if key.isupper()
        and isinstance(
            value,
            str,
        )
    ]


get_answer_events: Callable[[], list[str]] = lambda: _filter_events_by_prefixes(
    prefixes=[
        "ADD_ANSWER",
        "DELETE_ANSWER",
        "FILTER_ANSWERS",
        "GET_ANSWER",
        "GET_ALL_ANSWERS",
        "UPDATE_ANSWER",
    ]
)

get_association_events: Callable[[], list[str]] = lambda: _filter_events_by_prefixes(
    prefixes=[
        "ADD_ASSOCIATION",
        "DELETE_ASSOCIATION",
        "FILTER_ASSOCIATIONS",
        "GET_ASSOCIATION",
        "GET_ALL_ASSOCIATIONS",
        "UPDATE_ASSOCIATION",
    ]
)

get_customfield_events: Callable[[], list[str]] = lambda: _filter_events_by_prefixes(
    prefixes=[
        "ADD_CUSTOMFIELD",
        "DELETE_CUSTOMFIELD",
        "FILTER_CUSTOMFIELDS",
        "GET_CUSTOMFIELD",
        "GET_ALL_CUSTOMFIELDS",
        "UPDATE_CUSTOMFIELD",
    ]
)

get_difficulty_events: Callable[[], list[str]] = lambda: _filter_events_by_prefixes(
    prefixes=[
        "ADD_DIFFICULTY",
        "DELETE_DIFFICULTY",
        "FILTER_DIFFICULTIES",
        "GET_DIFFICULTY",
        "GET_ALL_DIFFICULTIES",
        "UPDATE_DIFFICULTY",
        "UPDATE_DIFFICULTIES",
    ]
)


def get_event_by_name(name: str) -> Optional[str]:
    """
    Retrieves a single event constant string from the module's global scope by its name.

    The function converts the input `name` to uppercase and searches the module's
    global dictionary (`globals()`) for a corresponding uppercase variable that
    is a string.

    Args:
        name (str): The name (case-insensitive) of the event constant to be retrieved.

    Returns:
        Optional[str]: The event constant string (e.g., “FLASHCARD_ADDED”) if found, otherwise None.
    """

    event_name: str = name.upper()

    if event_name in globals() and isinstance(globals()[event_name], str):
        return globals()[event_name]

    return None


def get_events_by_names(names: list[str]) -> list[str]:
    """
    Retrieves a list of event constant strings corresponding to a list of event names.

    This function iterates over the provided list of names, calling `get_event_by_name`
    for each. Only event strings that are successfully found are included in the
        resulting list. Not found events are silently dropped.

    Args:
        names (list[str]): A list of event names (case-insensitive) to be retrieved.

    Returns:
        list[str]: A list of the event constant strings found.
    """

    return [event for name in names if (event := get_event_by_name(name=name)) is not None]


def get_events_by_prefix(prefix: str) -> Optional[list[str]]:
    """
    Returns a list of events by prefix, if they exist.

    Args:
        prefix (str): The prefix to retrieve the events by.

    Returns:
        Optional[str]: The list of events if they exist, otherwise None.
    """

    return _filter_events_by_prefix(prefix=prefix.upper())


def get_events_by_prefixes(prefixes: list[str]) -> Optional[list[str]]:
    """
    Returns a list of events by prefixes, if they exist.

    Args:
        prefixes (list[str]): The prefixes to retrieve the events by.

    Returns:
        Optional[str]: The list of events if they exist, otherwise None.
    """

    return _filter_events_by_prefixes(prefixes=[prefix.upper() for prefix in prefixes])


get_flashcard_events: Callable[[], list[str]] = lambda: _filter_events_by_prefixes(
    prefixes=[
        "ADD_FLASHCARD",
        "DELETE_FLASHCARD",
        "FILTER_FLASHCARDS",
        "GET_FLASHCARD",
        "GET_ALL_FLASHCARDS",
        "UPDATE_FLASHCARD",
    ]
)

get_image_events: Callable[[], list[str]] = lambda: _filter_events_by_prefixes(
    prefixes=[
        "ADD_IMAGE",
        "DELETE_IMAGE",
        "FILTER_IMAGES",
        "GET_IMAGE",
        "GET_ALL_IMAGE",
        "UPDATE_IMAGE",
    ]
)

get_note_events: Callable[[], list[str]] = lambda: _filter_events_by_prefixes(
    prefixes=[
        "ADD_NOTE",
        "DELETE_NOTE",
        "FILTER_NOTES",
        "GET_NOTE",
        "GET_ALL_NOTE",
        "UPDATE_NOTE",
    ]
)

get_option_events: Callable[[], list[str]] = lambda: _filter_events_by_prefixes(
    prefixes=[
        "ADD_OPTION",
        "DELETE_OPTION",
        "GET_OPTION",
        "GET_ALL_OPTION",
        "UPDATE_OPTION",
    ]
)

get_priority_events: Callable[[], list[str]] = lambda: _filter_events_by_prefixes(
    prefixes=[
        "ADD_PRIORITY",
        "DELETE_PRIORITY",
        "FILTER_PRIORITIES",
        "GET_PRIORITY",
        "GET_ALL_PRIORITIES",
        "UPDATE_PRIORITY",
        "UPDATE_PRIORITY",
    ]
)

get_question_events: Callable[[], list[str]] = lambda: _filter_events_by_prefixes(
    prefixes=[
        "ADD_QUESTION",
        "DELETE_QUESTION",
        "FILTER_QUESTIONS",
        "GET_QUESTION",
        "GET_ALL_QUESTIONS",
        "UPDATE_QUESTION",
    ]
)

get_rehearsal_run_events: Callable[[], list[str]] = lambda: _filter_events_by_prefixes(
    prefixes=[
        "ADD_REHEARSAL_RUN",
        "DELETE_REHEARSAL_RUN",
        "FILTER_REHEARSAL_RUNS",
        "GET_REHEARSAL_RUN",
        "GET_ALL_REHEARSAL_RUNS",
        "UPDATE_REHEARSAL_RUN",
    ]
)

get_rehearsal_run_item_events: Callable[[], list[str]] = lambda: _filter_events_by_prefixes(
    prefixes=[
        "ADD_REHEARSAL_RUN_ITEM",
        "DELETE_REHEARSAL_RUN_ITEM",
        "FILTER_REHEARSAL_RUN_ITEMS",
        "GET_REHEARSAL_RUN_ITEM",
        "GET_ALL_REHEARSAL_RUN_ITEMS",
        "UPDATE_REHEARSAL_RUN_ITEM",
    ]
)

get_stack_events: Callable[[], list[str]] = lambda: _filter_events_by_prefixes(
    prefixes=[
        "ADD_STACK",
        "DELETE_STACK",
        "FILTER_STACKS",
        "GET_STACK",
        "GET_ALL_STACKS",
        "UPDATE_STACK",
    ]
)

get_subject_events: Callable[[], list[str]] = lambda: _filter_events_by_prefixes(
    prefixes=[
        "ADD_SUBJECT",
        "DELETE_SUBJECT",
        "FILTER_SUBJECTS",
        "GET_SUBJECT",
        "GET_ALL_SUBJECTS",
        "UPDATE_SUBJECT",
    ]
)

get_tag_events: Callable[[], list[str]] = lambda: _filter_events_by_prefixes(
    prefixes=[
        "ADD_TAG",
        "DELETE_TAG",
        "FILTER_TAGS",
        "GET_TAG",
        "GET_ALL_TAG",
        "UPDATE_TAG",
    ]
)

get_teacher_events: Callable[[], list[str]] = lambda: _filter_events_by_prefixes(
    prefixes=[
        "ADD_TEACHER",
        "DELETE_TEACHER",
        "FILTER_TEACHERS",
        "GET_TEACHER",
        "GET_ALL_TEACHER",
        "UPDATE_TEACHER",
    ]
)

get_user_events: Callable[[], list[str]] = lambda: _filter_events_by_prefixes(
    prefixes=[
        "ADD_USER",
        "DELETE_USER",
        "FILTER_USERS",
        "GET_USER",
        "GET_ALL_USER",
        "UPDATE_USER",
    ]
)


def get_utility_events() -> list[str]:
    """
    Returns a list containing the 'DB_OPERATION_FAILURE' and 'DB_OPERATION_SUCCESS' utility events.

    Args:
        None

    Returns:
        list[str]: The list containing the 'DB_OPERATION_FAILURE' and 'DB_OPERATION_SUCCESS' utility events.
    """
    return [
        DB_OPERATION_FAILURE,
        DB_OPERATION_SUCCESS,
    ]
