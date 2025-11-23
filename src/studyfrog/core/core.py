"""
Author: Louis Goodnews
Date: 2025-11-16
"""

from typing import Any, Callable, Final, Literal

from common.constants import (
    ASSETS_DIR,
    BACKUP_DIR,
    CONFIG_DIR,
    DATA_DIR,
    EXPORTS_DIR,
    IMPORTS_DIR,
    LOCAL_DIR,
    LOG_DIR,
    RESOURCES_DIR,
    TEMP_DIR,
    ANSWERS_TABLE_FILE,
    ASSOCIATIONS_TABLE_FILE,
    CONFIGS_FILE,
    CUSTOMFIELDS_TABLE_FILE,
    DIFFICULTIES_TABLE_FILE,
    FLASHCARDS_TABLE_FILE,
    IMAGES_TABLE_FILE,
    NOTES_TABLE_FILE,
    OPTIONS_TABLE_FILE,
    PRIORITIES_TABLE_FILE,
    QUESTIONS_TABLE_FILE,
    REHEARSAL_RUNS_TABLE_FILE,
    REHEARSAL_RUN_ITEMS_TABLE_FILE,
    STACKS_TABLE_FILE,
    SUBJECTS_TABLE_FILE,
    TAGS_TABLE_FILE,
    TEACHERS_TABLE_FILE,
    USERS_TABLE_FILE,
)
from common.events import (
    ADD_ANSWER,
    ADD_ANSWERS,
    ADD_ASSOCIATION,
    ADD_ASSOCIATIONS,
    ADD_CUSTOMFIELD,
    ADD_CUSTOMFIELDS,
    ADD_DIFFICULTY,
    ADD_DIFFICULTIES,
    ADD_FLASHCARD,
    ADD_FLASHCARDS,
    ADD_IMAGE,
    ADD_IMAGES,
    ADD_NOTE,
    ADD_NOTES,
    ADD_OPTION,
    ADD_OPTIONS,
    ADD_PRIORITY,
    ADD_PRIORITIES,
    ADD_QUESTION,
    ADD_QUESTIONS,
    ADD_REHEARSAL_RUN,
    ADD_REHEARSAL_RUNS,
    ADD_REHEARSAL_RUN_ITEM,
    ADD_REHEARSAL_RUN_ITEMS,
    ADD_STACK,
    ADD_STACKS,
    ADD_SUBJECT,
    ADD_SUBJECTS,
    ADD_TAG,
    ADD_TAGS,
    ADD_TEACHER,
    ADD_TEACHERS,
    ADD_USER,
    ADD_USERS,
    APPLICATION_STARTED,
    APPLICATION_STARTING,
    APPLICATION_STOPPED,
    APPLICATION_STOPPING,
    GET_ALL_ANSWERS,
    GET_ALL_ASSOCIATIONS,
    GET_ALL_CUSTOMFIELDS,
    GET_ALL_DIFFICULTIES,
    GET_ALL_FLASHCARDS,
    GET_ALL_IMAGES,
    GET_ALL_NOTES,
    GET_ALL_OPTIONS,
    GET_ALL_PRIORITIES,
    GET_ALL_QUESTIONS,
    GET_ALL_REHEARSAL_RUNS,
    GET_ALL_REHEARSAL_RUN_ITEMS,
    GET_ALL_STACKS,
    GET_ALL_SUBJECTS,
    GET_ALL_TAGS,
    GET_ALL_TEACHERS,
    GET_ALL_USERS,
    GET_ANSWER,
    GET_ANSWERS,
    GET_ASSOCIATION,
    GET_ASSOCIATIONS,
    GET_CUSTOMFIELD,
    GET_CUSTOMFIELDS,
    GET_DIFFICULTY,
    GET_DIFFICULTIES,
    GET_FLASHCARD,
    GET_FLASHCARDS,
    GET_IMAGE,
    GET_IMAGES,
    GET_NOTE,
    GET_NOTES,
    GET_OPTION,
    GET_OPTIONS,
    GET_PRIORITY,
    GET_PRIORITIES,
    GET_QUESTION,
    GET_QUESTIONS,
    GET_REHEARSAL_RUN,
    GET_REHEARSAL_RUNS,
    GET_REHEARSAL_RUN_ITEM,
    GET_REHEARSAL_RUN_ITEMS,
    GET_STACK,
    GET_STACKS,
    GET_SUBJECT,
    GET_SUBJECTS,
    GET_TAG,
    GET_TAGS,
    GET_TEACHER,
    GET_TEACHERS,
    GET_USER,
    GET_USERS,
    REMOVE_ANSWER,
    REMOVE_ANSWERS,
    REMOVE_ASSOCIATION,
    REMOVE_ASSOCIATIONS,
    REMOVE_CUSTOMFIELD,
    REMOVE_CUSTOMFIELDS,
    REMOVE_DIFFICULTY,
    REMOVE_DIFFICULTIES,
    REMOVE_FLASHCARD,
    REMOVE_FLASHCARDS,
    REMOVE_IMAGE,
    REMOVE_IMAGES,
    REMOVE_NOTE,
    REMOVE_NOTES,
    REMOVE_OPTION,
    REMOVE_OPTIONS,
    REMOVE_PRIORITY,
    REMOVE_PRIORITIES,
    REMOVE_QUESTION,
    REMOVE_QUESTIONS,
    REMOVE_REHEARSAL_RUN,
    REMOVE_REHEARSAL_RUNS,
    REMOVE_REHEARSAL_RUN_ITEM,
    REMOVE_REHEARSAL_RUN_ITEMS,
    REMOVE_STACK,
    REMOVE_STACKS,
    REMOVE_SUBJECT,
    REMOVE_SUBJECTS,
    REMOVE_TAG,
    REMOVE_TAGS,
    REMOVE_TEACHER,
    REMOVE_TEACHERS,
    REMOVE_USER,
    REMOVE_USERS,
    UPDATE_ANSWER,
    UPDATE_ANSWERS,
    UPDATE_ASSOCIATION,
    UPDATE_ASSOCIATIONS,
    UPDATE_CUSTOMFIELD,
    UPDATE_CUSTOMFIELDS,
    UPDATE_DIFFICULTY,
    UPDATE_DIFFICULTIES,
    UPDATE_FLASHCARD,
    UPDATE_FLASHCARDS,
    UPDATE_IMAGE,
    UPDATE_IMAGES,
    UPDATE_NOTE,
    UPDATE_NOTES,
    UPDATE_OPTION,
    UPDATE_OPTIONS,
    UPDATE_PRIORITY,
    UPDATE_PRIORITIES,
    UPDATE_QUESTION,
    UPDATE_QUESTIONS,
    UPDATE_REHEARSAL_RUN,
    UPDATE_REHEARSAL_RUNS,
    UPDATE_REHEARSAL_RUN_ITEM,
    UPDATE_REHEARSAL_RUN_ITEMS,
    UPDATE_STACK,
    UPDATE_STACKS,
    UPDATE_SUBJECT,
    UPDATE_SUBJECTS,
    UPDATE_TAG,
    UPDATE_TAGS,
    UPDATE_TEACHER,
    UPDATE_TEACHERS,
    UPDATE_USER,
    UPDATE_USERS,
)
from core.defaults import (
    EASY_DIFFICULTY,
    HARD_DIFFICULTY,
    HIGH_PRIORITY,
    HIGHEST_PRIORITY,
    LOW_PRIORITY,
    LOWEST_PRIORITY,
    MEDIUM_DIFFICULTY,
    MEDIUM_PRIORITY,
    STUDY_FROG_USER,
)
from core.objects import (
    add_answer,
    add_answers,
    add_association,
    add_associations,
    add_customfield,
    add_customfields,
    add_difficulty,
    add_difficulties,
    add_flashcard,
    add_flashcards,
    add_image,
    add_images,
    add_note,
    add_notes,
    add_option,
    add_options,
    add_priority,
    add_priorities,
    add_question,
    add_questions,
    add_rehearsal_run,
    add_rehearsal_runs,
    add_rehearsal_run_item,
    add_rehearsal_run_items,
    add_stack,
    add_stacks,
    add_subject,
    add_subjects,
    add_tag,
    add_tags,
    add_teacher,
    add_teachers,
    add_user,
    add_users,
    get_all_answers,
    get_all_associations,
    get_all_customfields,
    get_all_difficulties,
    get_all_flashcards,
    get_all_images,
    get_all_notes,
    get_all_options,
    get_all_priorities,
    get_all_questions,
    get_all_rehearsal_runs,
    get_all_rehearsal_run_items,
    get_all_stacks,
    get_all_subjects,
    get_all_tags,
    get_all_teachers,
    get_all_users,
    get_answer,
    get_answers,
    get_association,
    get_associations,
    get_customfield,
    get_customfields,
    get_difficulty,
    get_difficulties,
    get_flashcard,
    get_flashcards,
    get_image,
    get_images,
    get_note,
    get_notes,
    get_option,
    get_options,
    get_priority,
    get_priorities,
    get_question,
    get_questions,
    get_rehearsal_run,
    get_rehearsal_runs,
    get_rehearsal_run_item,
    get_rehearsal_run_items,
    get_stack,
    get_stacks,
    get_subject,
    get_subjects,
    get_tag,
    get_tags,
    get_teacher,
    get_teachers,
    get_user,
    get_users,
    remove_answer,
    remove_answers,
    remove_association,
    remove_associations,
    remove_customfield,
    remove_customfields,
    remove_difficulty,
    remove_difficulties,
    remove_flashcard,
    remove_flashcards,
    remove_image,
    remove_images,
    remove_note,
    remove_notes,
    remove_option,
    remove_options,
    remove_priority,
    remove_priorities,
    remove_question,
    remove_questions,
    remove_rehearsal_run,
    remove_rehearsal_runs,
    remove_rehearsal_run_item,
    remove_rehearsal_run_items,
    remove_stack,
    remove_stacks,
    remove_subject,
    remove_subjects,
    remove_tag,
    remove_tags,
    remove_teacher,
    remove_teachers,
    remove_user,
    remove_users,
    update_answer,
    update_answers,
    update_association,
    update_associations,
    update_customfield,
    update_customfields,
    update_difficulty,
    update_difficulties,
    update_flashcard,
    update_flashcards,
    update_image,
    update_images,
    update_note,
    update_notes,
    update_option,
    update_options,
    update_priority,
    update_priorities,
    update_question,
    update_questions,
    update_rehearsal_run,
    update_rehearsal_runs,
    update_rehearsal_run_item,
    update_rehearsal_run_items,
    update_stack,
    update_stacks,
    update_subject,
    update_subjects,
    update_tag,
    update_tags,
    update_teacher,
    update_teachers,
    update_user,
    update_users,
)
from core.storage import add_table_entry_if_not_exists, create_table_if_not_exists
from gui.gui import (
    get_bottom_frame,
    get_center_frame,
    get_edit_menu,
    get_file_menu,
    get_menu,
    get_root,
    get_top_frame,
    get_view_menu,
    is_root_active,
    make_root_none_if_possible,
)
from gui.views.views import get_view
from utils.utils import (
    ensure_dir,
    ensure_json,
    log_exception,
    log_info,
    pluralize_str,
    publish_event,
    register_subscription,
    unsubscribe_subscription,
)


# ---------- Constants ---------- #

NAME: Final[Literal["core.core"]] = "core.core"

SUBSCRIPTIONS: Final[list[str]] = []


# ---------- Functions ---------- #


def ensure_defaults() -> None:
    """
    Ensures default values are present in the database.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    log_info(
        message="Ensuring defaults...",
        name=NAME,
    )

    try:
        for dictionary in (
            EASY_DIFFICULTY,
            HARD_DIFFICULTY,
            HIGH_PRIORITY,
            HIGHEST_PRIORITY,
            LOW_PRIORITY,
            LOWEST_PRIORITY,
            MEDIUM_DIFFICULTY,
            MEDIUM_PRIORITY,
            STUDY_FROG_USER,
        ):
            add_table_entry_if_not_exists(
                entry=dictionary,
                table_name=pluralize_str(string=dictionary["type"].lower()),
            )

        log_info(
            message="Defaults ensured.",
            name=NAME,
        )
    except Exception as e:
        log_exception(
            name=NAME,
            message="Failed to ensure defaults.",
            exception=e,
        )
        raise Exception(f"Failed to ensure defaults: {e}") from e


def initialize_directories() -> None:
    """
    Initializes directories.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    log_info(
        message="Initializing directories...",
        name=NAME,
    )

    try:
        for path in (
            LOCAL_DIR,
            ASSETS_DIR,
            BACKUP_DIR,
            CONFIG_DIR,
            DATA_DIR,
            EXPORTS_DIR,
            IMPORTS_DIR,
            LOG_DIR,
            RESOURCES_DIR,
            TEMP_DIR,
        ):
            ensure_dir(path=path)

        log_info(
            message="Directories initialized.",
            name=NAME,
        )
    except Exception as e:
        log_exception(
            name=NAME,
            message="Failed to initialize directories.",
            exception=e,
        )
        raise Exception(f"Failed to initialize directories: {e}") from e


def initialize_files() -> None:
    """
    Initializes files.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    log_info(
        message="Initializing files...",
        name=NAME,
    )

    try:
        for path in [
            ANSWERS_TABLE_FILE,
            ASSOCIATIONS_TABLE_FILE,
            CONFIGS_FILE,
            CUSTOMFIELDS_TABLE_FILE,
            DIFFICULTIES_TABLE_FILE,
            FLASHCARDS_TABLE_FILE,
            IMAGES_TABLE_FILE,
            NOTES_TABLE_FILE,
            OPTIONS_TABLE_FILE,
            PRIORITIES_TABLE_FILE,
            QUESTIONS_TABLE_FILE,
            REHEARSAL_RUNS_TABLE_FILE,
            REHEARSAL_RUN_ITEMS_TABLE_FILE,
            STACKS_TABLE_FILE,
            SUBJECTS_TABLE_FILE,
            TAGS_TABLE_FILE,
            TEACHERS_TABLE_FILE,
            USERS_TABLE_FILE,
        ]:
            ensure_json(path=path)

        log_info(
            message="Files initialized.",
            name=NAME,
        )
    except Exception as e:
        log_exception(
            name=NAME,
            message="Failed to initialize files.",
            exception=e,
        )
        raise Exception(f"Failed to initialize files: {e}") from e


def initialize_gui() -> None:
    """
    Initializes the GUI.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    log_info(
        message="Initializing GUI...",
        name=NAME,
    )

    try:
        get_root()
        get_menu()
        get_edit_menu()
        get_file_menu()
        get_view_menu()
        get_top_frame()
        get_center_frame()
        get_bottom_frame()
        get_view(name="dashboard")

        log_info(
            message="GUI initialized.",
            name=NAME,
        )
    except Exception as e:
        log_exception(
            name=NAME,
            message="Failed to initialize GUI.",
            exception=e,
        )
        raise Exception(f"Failed to initialize GUI: {e}") from e


def initialize_subscriptions() -> None:
    """
    Initializes subscriptions.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    log_info(
        message="Initializing subscriptions...",
        name=NAME,
    )

    try:
        events: tuple[str] = (
            ADD_ANSWER,
            ADD_ANSWERS,
            ADD_ASSOCIATION,
            ADD_ASSOCIATIONS,
            ADD_CUSTOMFIELD,
            ADD_CUSTOMFIELDS,
            ADD_DIFFICULTY,
            ADD_DIFFICULTIES,
            ADD_FLASHCARD,
            ADD_FLASHCARDS,
            ADD_IMAGE,
            ADD_IMAGES,
            ADD_NOTE,
            ADD_NOTES,
            ADD_OPTION,
            ADD_OPTIONS,
            ADD_PRIORITY,
            ADD_PRIORITIES,
            ADD_QUESTION,
            ADD_QUESTIONS,
            ADD_REHEARSAL_RUN,
            ADD_REHEARSAL_RUNS,
            ADD_REHEARSAL_RUN_ITEM,
            ADD_REHEARSAL_RUN_ITEMS,
            ADD_STACK,
            ADD_STACKS,
            ADD_SUBJECT,
            ADD_SUBJECTS,
            ADD_TAG,
            ADD_TAGS,
            ADD_TEACHER,
            ADD_TEACHERS,
            ADD_USER,
            ADD_USERS,
            GET_ALL_ANSWERS,
            GET_ALL_ASSOCIATIONS,
            GET_ALL_CUSTOMFIELDS,
            GET_ALL_DIFFICULTIES,
            GET_ALL_FLASHCARDS,
            GET_ALL_IMAGES,
            GET_ALL_NOTES,
            GET_ALL_OPTIONS,
            GET_ALL_PRIORITIES,
            GET_ALL_QUESTIONS,
            GET_ALL_REHEARSAL_RUNS,
            GET_ALL_REHEARSAL_RUN_ITEMS,
            GET_ALL_STACKS,
            GET_ALL_SUBJECTS,
            GET_ALL_TAGS,
            GET_ALL_TEACHERS,
            GET_ALL_USERS,
            GET_ANSWER,
            GET_ANSWERS,
            GET_ASSOCIATION,
            GET_ASSOCIATIONS,
            GET_CUSTOMFIELD,
            GET_CUSTOMFIELDS,
            GET_DIFFICULTY,
            GET_DIFFICULTIES,
            GET_FLASHCARD,
            GET_FLASHCARDS,
            GET_IMAGE,
            GET_IMAGES,
            GET_NOTE,
            GET_NOTES,
            GET_OPTION,
            GET_OPTIONS,
            GET_PRIORITY,
            GET_PRIORITIES,
            GET_QUESTION,
            GET_QUESTIONS,
            GET_REHEARSAL_RUN,
            GET_REHEARSAL_RUNS,
            GET_REHEARSAL_RUN_ITEM,
            GET_REHEARSAL_RUN_ITEMS,
            GET_STACK,
            GET_STACKS,
            GET_SUBJECT,
            GET_SUBJECTS,
            GET_TAG,
            GET_TAGS,
            GET_TEACHER,
            GET_TEACHERS,
            GET_USER,
            GET_USERS,
            REMOVE_ANSWER,
            REMOVE_ANSWERS,
            REMOVE_ASSOCIATION,
            REMOVE_ASSOCIATIONS,
            REMOVE_CUSTOMFIELD,
            REMOVE_CUSTOMFIELDS,
            REMOVE_DIFFICULTY,
            REMOVE_DIFFICULTIES,
            REMOVE_FLASHCARD,
            REMOVE_FLASHCARDS,
            REMOVE_IMAGE,
            REMOVE_IMAGES,
            REMOVE_NOTE,
            REMOVE_NOTES,
            REMOVE_OPTION,
            REMOVE_OPTIONS,
            REMOVE_PRIORITY,
            REMOVE_PRIORITIES,
            REMOVE_QUESTION,
            REMOVE_QUESTIONS,
            REMOVE_REHEARSAL_RUN,
            REMOVE_REHEARSAL_RUNS,
            REMOVE_REHEARSAL_RUN_ITEM,
            REMOVE_REHEARSAL_RUN_ITEMS,
            REMOVE_STACK,
            REMOVE_STACKS,
            REMOVE_SUBJECT,
            REMOVE_SUBJECTS,
            REMOVE_TAG,
            REMOVE_TAGS,
            REMOVE_TEACHER,
            REMOVE_TEACHERS,
            REMOVE_USER,
            REMOVE_USERS,
            UPDATE_ANSWER,
            UPDATE_ANSWERS,
            UPDATE_ASSOCIATION,
            UPDATE_ASSOCIATIONS,
            UPDATE_CUSTOMFIELD,
            UPDATE_CUSTOMFIELDS,
            UPDATE_DIFFICULTY,
            UPDATE_DIFFICULTIES,
            UPDATE_FLASHCARD,
            UPDATE_FLASHCARDS,
            UPDATE_IMAGE,
            UPDATE_IMAGES,
            UPDATE_NOTE,
            UPDATE_NOTES,
            UPDATE_OPTION,
            UPDATE_OPTIONS,
            UPDATE_PRIORITY,
            UPDATE_PRIORITIES,
            UPDATE_QUESTION,
            UPDATE_QUESTIONS,
            UPDATE_REHEARSAL_RUN,
            UPDATE_REHEARSAL_RUNS,
            UPDATE_REHEARSAL_RUN_ITEM,
            UPDATE_REHEARSAL_RUN_ITEMS,
            UPDATE_STACK,
            UPDATE_STACKS,
            UPDATE_SUBJECT,
            UPDATE_SUBJECTS,
            UPDATE_TAG,
            UPDATE_TAGS,
            UPDATE_TEACHER,
            UPDATE_TEACHERS,
            UPDATE_USER,
            UPDATE_USERS,
        )

        functions: tuple[Callable[[], Any]] = (
            add_answer,
            add_answers,
            add_association,
            add_associations,
            add_customfield,
            add_customfields,
            add_difficulty,
            add_difficulties,
            add_flashcard,
            add_flashcards,
            add_image,
            add_images,
            add_note,
            add_notes,
            add_option,
            add_options,
            add_priority,
            add_priorities,
            add_question,
            add_questions,
            add_rehearsal_run,
            add_rehearsal_runs,
            add_rehearsal_run_item,
            add_rehearsal_run_items,
            add_stack,
            add_stacks,
            add_subject,
            add_subjects,
            add_tag,
            add_tags,
            add_teacher,
            add_teachers,
            add_user,
            add_users,
            get_all_answers,
            get_all_associations,
            get_all_customfields,
            get_all_difficulties,
            get_all_flashcards,
            get_all_images,
            get_all_notes,
            get_all_options,
            get_all_priorities,
            get_all_questions,
            get_all_rehearsal_runs,
            get_all_rehearsal_run_items,
            get_all_stacks,
            get_all_subjects,
            get_all_tags,
            get_all_teachers,
            get_all_users,
            get_answer,
            get_answers,
            get_association,
            get_associations,
            get_customfield,
            get_customfields,
            get_difficulty,
            get_difficulties,
            get_flashcard,
            get_flashcards,
            get_image,
            get_images,
            get_note,
            get_notes,
            get_option,
            get_options,
            get_priority,
            get_priorities,
            get_question,
            get_questions,
            get_rehearsal_run,
            get_rehearsal_runs,
            get_rehearsal_run_item,
            get_rehearsal_run_items,
            get_stack,
            get_stacks,
            get_subject,
            get_subjects,
            get_tag,
            get_tags,
            get_teacher,
            get_teachers,
            get_user,
            get_users,
            remove_answer,
            remove_answers,
            remove_association,
            remove_associations,
            remove_customfield,
            remove_customfields,
            remove_difficulty,
            remove_difficulties,
            remove_flashcard,
            remove_flashcards,
            remove_image,
            remove_images,
            remove_note,
            remove_notes,
            remove_option,
            remove_options,
            remove_priority,
            remove_priorities,
            remove_question,
            remove_questions,
            remove_rehearsal_run,
            remove_rehearsal_runs,
            remove_rehearsal_run_item,
            remove_rehearsal_run_items,
            remove_stack,
            remove_stacks,
            remove_subject,
            remove_subjects,
            remove_tag,
            remove_tags,
            remove_teacher,
            remove_teachers,
            remove_user,
            remove_users,
            update_answer,
            update_answers,
            update_association,
            update_associations,
            update_customfield,
            update_customfields,
            update_difficulty,
            update_difficulties,
            update_flashcard,
            update_flashcards,
            update_image,
            update_images,
            update_note,
            update_notes,
            update_option,
            update_options,
            update_priority,
            update_priorities,
            update_question,
            update_questions,
            update_rehearsal_run,
            update_rehearsal_runs,
            update_rehearsal_run_item,
            update_rehearsal_run_items,
            update_stack,
            update_stacks,
            update_subject,
            update_subjects,
            update_tag,
            update_tags,
            update_teacher,
            update_teachers,
            update_user,
            update_users,
        )

        for (
            event,
            function,
        ) in zip(
            events,
            functions,
            strict=True,
        ):
            SUBSCRIPTIONS.append(
                register_subscription(
                    event=event,
                    function=function,
                    persistent=True,
                    priority=100,
                )
            )

            log_info(
                message=f"Registered '{event.upper()}' event for subscription with function '{function.__name__}'.",
                name=NAME,
            )

        log_info(
            message="Subscriptions initialized.",
            name=NAME,
        )
    except Exception as e:
        log_exception(
            name=NAME,
            message="Failed to initialize subscriptions.",
            exception=e,
        )
        raise Exception(f"Failed to initialize subscriptions: {e}") from e


def initialize_tables() -> None:
    """
    Initializes tables.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    log_info(
        message="Initializing tables...",
        name=NAME,
    )

    try:
        for path in [
            ANSWERS_TABLE_FILE,
            ASSOCIATIONS_TABLE_FILE,
            CONFIGS_FILE,
            CUSTOMFIELDS_TABLE_FILE,
            DIFFICULTIES_TABLE_FILE,
            FLASHCARDS_TABLE_FILE,
            IMAGES_TABLE_FILE,
            NOTES_TABLE_FILE,
            OPTIONS_TABLE_FILE,
            PRIORITIES_TABLE_FILE,
            QUESTIONS_TABLE_FILE,
            REHEARSAL_RUNS_TABLE_FILE,
            REHEARSAL_RUN_ITEMS_TABLE_FILE,
            STACKS_TABLE_FILE,
            SUBJECTS_TABLE_FILE,
            TAGS_TABLE_FILE,
            TEACHERS_TABLE_FILE,
            USERS_TABLE_FILE,
        ]:
            create_table_if_not_exists(table_name=path.stem)

        log_info(
            message="Tables initialized.",
            name=NAME,
        )
    except Exception as e:
        log_exception(
            name=NAME,
            message="Failed to initialize tables.",
            exception=e,
        )
        raise Exception(f"Failed to initialize tables: {e}") from e


def run_post_start_tasks() -> None:
    """
    Runs tasks that need to be run after the application starts.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    log_info(
        message="Running post-start tasks...",
        name=NAME,
    )

    try:
        ensure_defaults()
        log_info(
            message="Post-start tasks completed.",
            name=NAME,
        )
        publish_event(event=APPLICATION_STARTED)
        get_root().mainloop()
    except Exception as e:
        log_exception(
            name=NAME,
            message="Failed to run post-start tasks.",
            exception=e,
        )
        raise Exception(f"Failed to run post-start tasks: {e}") from e


def run_post_stop_tasks() -> None:
    """
    Runs tasks that need to be run after the application stops.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    log_info(
        message="Running post-stop tasks...",
        name=NAME,
    )

    try:
        log_info(
            message="Post-stop tasks completed.",
            name=NAME,
        )
        publish_event(event=APPLICATION_STOPPED)
        unsubscribe_subscriptions()

        if is_root_active():
            get_root().destroy()

            make_root_none_if_possible()
    except Exception as e:
        log_exception(
            name=NAME,
            message="Failed to run post-stop tasks.",
            exception=e,
        )
        raise Exception(f"Failed to run post-stop tasks: {e}") from e


def run_pre_start_tasks() -> None:
    """
    Runs tasks that need to be run before the application starts.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    log_info(
        message="Running pre-start tasks...",
        name=NAME,
    )

    try:
        initialize_directories()
        initialize_files()
        initialize_gui()
        initialize_tables()
        initialize_subscriptions()

        log_info(
            message="Pre-start tasks completed.",
            name=NAME,
        )
        publish_event(event=APPLICATION_STARTING)
    except Exception as e:
        log_exception(
            name=NAME,
            message="Failed to run pre-start tasks.",
            exception=e,
        )
        raise Exception(f"Failed to run pre-start tasks: {e}") from e


def run_pre_stop_tasks() -> None:
    """
    Runs tasks that need to be run before the application stops.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    log_info(
        message="Running pre-stop tasks...",
        name=NAME,
    )

    try:
        log_info(
            message="Pre-stop tasks completed.",
            name=NAME,
        )
        publish_event(event=APPLICATION_STOPPING)
    except Exception as e:
        log_exception(
            name=NAME,
            message="Failed to run pre-stop tasks.",
            exception=e,
        )
        raise Exception(f"Failed to run pre-stop tasks: {e}") from e


def start() -> None:
    """
    Starts the application.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    log_info(
        message="Starting application...",
        name=NAME,
    )

    try:
        run_pre_start_tasks()
        run_post_start_tasks()

        log_info(
            message="Application started.",
            name=NAME,
        )
    except Exception as e:
        log_exception(
            name=NAME,
            message="Failed to start application.",
            exception=e,
        )
        raise Exception(f"Failed to start application: {e}") from e


def stop() -> None:
    """
    Stops the application.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    log_info(
        message="Stopping application...",
        name=NAME,
    )

    try:
        run_pre_stop_tasks()
        run_post_stop_tasks()

        log_info(
            message="Application stopped.",
            name=NAME,
        )
    except Exception as e:
        log_exception(
            name=NAME,
            message="Failed to stop application.",
            exception=e,
        )
        raise Exception(f"Failed to stop application: {e}") from e


def unsubscribe_subscriptions() -> None:
    """
    Unsubscribes from all subscriptions.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If an error occurs.
    """

    log_info(
        message="Unsubscribing subscriptions...",
        name=NAME,
    )

    try:
        for uuid in SUBSCRIPTIONS:
            unsubscribe_subscription(uuid=uuid)

        log_info(
            message="Subscriptions unsubscribed.",
            name=NAME,
        )
    except Exception as e:
        log_exception(
            name=NAME,
            message="Failed to unsubscribe from subscriptions.",
            exception=e,
        )
        raise Exception(f"Failed to unsubscribe from subscriptions: {e}") from e


# ---------- Auto-Export ---------- #

# Auto-Export all non-private symbols
__all__: Final[list[str]] = [
    key
    for (
        key,
        value,
    ) in globals().items()
    if not key.startswith("_") and callable(value)
]
