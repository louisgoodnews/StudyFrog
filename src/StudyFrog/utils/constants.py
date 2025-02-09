"""
Author: lodego
Date: 2025-02-06
"""

import os

from os import path

from datetime import datetime, timedelta


class Constants:
    """
    Contains various constants used throughout the program.

    The constants that are available are:

    * APPLICATION_NAME: The name of the application.
    * APPLICATION_VERSION: The version of the application.
    * BASE_ID: The base ID of objects in the application.
    * CWD: The current working directory.
    * DATA_PATH: The path to the data directory.
    * DATABASE_PATH: The path to the database file.
    * EXPORT_PATH: The path to the export directory.
    * IMPORT_PATH: The path to the import directory.
    * ANSWERS: The name of the table for answers.
    * ASSOCIATIONS: The name of the table for associations.
    * CHANGE_HISTORY: The name of the table for change history.
    * CHANGE_HISTORY_ITEMS: The name of the table for change history items.
    * DEFAULTS: The name of the table for defaults.
    * DIFFICULTIES: The name of the table for difficulties.
    * FLASHCARDS: The name of the table for flashcards.
    * NOTES: The name of the table for notes.
    * PRIORITIES: The name of the table for priorities.
    * QUESTIONS: The name of the table for questions.
    * SETTINGS: The name of the table for settings.
    * STACKS: The name of the table for stacks.
    * TAGS: The name of the table for tags.
    * USERS: The name of the table for users.
    * DEFAULT_FONT_FAMILIY: The default font family.
    * DEFAULT_FONT_SIZE: The default font size.
    * INDIGO: The color indigo.
    * GREY: The color grey.
    * BLACK: The color black.
    * WHITE: The color white.
    * DEFAULT_GEOMETRY: The default geometry of the main window.
    * GLOBAL_NAMESPACE: The namespace for global dispatching of events.
    * MAIN_UI_NAMESPACE: The namespace for the main UI.
    * NOW: The current time.
    * TODAY: The current date.
    * TOMORROW: The current date plus one day.
    * YESTERDAY: The current date minus one day.
    """

    APPLICATION_NAME: str = "StudyFrog"
    APPLICATION_VERSION: float = 0.1

    BASE_ID: int = 10000

    CWD: str = os.getcwd()

    DATA_PATH: str = path.join(
        CWD,
        "data",
    )

    DATABASE_PATH: str = path.join(
        DATA_PATH,
        "database.db",
    )

    EXPORT_PATH: str = path.join(
        DATA_PATH,
        "exports",
    )

    IMPORT_PATH: str = path.join(
        DATA_PATH,
        "imports",
    )

    ANSWERS: str = "answers"
    ASSOCIATIONS: str = "associations"
    CHANGE_HISTORIES: str = "change_histories"
    CHANGE_HISTORY_ITEMS: str = "change_history_items"
    DEFAULTS: str = "defaults"
    DIFFICULTIES: str = "difficulties"
    FLASHCARDS: str = "flashcards"
    NOTES: str = "notes"
    PRIORITIES: str = "priorities"
    QUESTIONS: str = "questions"
    SETTINGS: str = "settings"
    STACKS: str = "stacks"
    TAGS: str = "tags"
    USERS: str = "users"

    DEFAULT_FONT_FAMILIY: str = "Helvetica"
    DEFAULT_FONT_SIZE: int = 16

    DEFAULT_GEOMETRY: str = "1920x1080"

    BLACK: str = "#000000"
    GREY: str = "#9e9e9e"
    INDIGO: str = "#3f51b5"
    WHITE: str = "#ffffff"

    GLOBAL_NAMESPACE: str = "GLOBAL"

    MAIN_UI_NAMESPACE: str = "MAIN_UI"

    NOW: datetime = datetime.now()

    TODAY: datetime = datetime.today()
    TOMORROW: datetime = datetime.today() + timedelta(days=1)
    YESTERDAY: datetime = datetime.today() - timedelta(days=1)
