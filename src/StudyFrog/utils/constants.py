"""
Author: lodego
Date: 2025-02-06
"""

import copy
import os

from datetime import datetime, timedelta
from os import path
from tkinter import ttk
from typing import *


__all__: Final[List[str]] = ["Constants"]


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
    * CUSTOM_FIELDS: The name of the table for custom fields.
    * DEFAULTS: The name of the table for defaults.
    * DIFFICULTIES: The name of the table for difficulties.
    * FLASHCARDS: The name of the table for flashcards.
    * NOTES: The name of the table for notes.
    * OPTIONS: The name of the table for options.
    * PRIORITIES: The name of the table for priorities.
    * QUESTIONS: The name of the table for questions.
    * SETTINGS: The name of the table for settings.
    * STACKS: The name of the table for stacks.
    * TAGS: The name of the table for tags.
    * USERS: The name of the table for users.

    * DEFAULT_FONT_FAMILY: The default font family.
    * DEFAULT_FONT_SIZE: The default font size.

    * VERY_LARGE_FONT_SIZE: The very large font size.
    * LARGE_FONT_SIZE: The large font size.
    * SMALL_FONT_SIZE: The small font size.

    * BOLD: The font weight bold.
    * ITALIC: The font weight italic.
    * NORMAL: The font weight normal.
    * OVERSTRIKE: The font weight overstrike.
    * UNDERLINE: The font weight underline.

    * AMBER: The color amber.
    * BLACK: The color black.
    * BLUE: The color blue.
    * BROWN: The color brown.
    * CYAN: The color cyan.
    * DEEP_PURPLE: The color deep purple.
    * GREY: The color grey.
    * GREEN: The color green.
    * INDIGO: The color indigo.
    * ORANGE: The color orange.
    * PINK: The color pink.
    * RED: The color red.
    * TEAL: The color teal.
    * WHITE: The color white.
    * YELLOW: The color yellow.

    * DEFAULT_GEOMETRY: The default geometry of the main window.
    * GLOBAL_NAMESPACE: The namespace for global dispatching of events.

    * HIGHEST: The highest priority.
    * HIGH: The high priority.
    * MEDIUM: The medium priority.
    * LOW: The low priority.
    * LOWEST: The lowest priority.

    * HARD: The hard difficulty.
    * MEDIUM: The medium difficulty.
    * EASY: The easy difficulty.

    * TRUE: The true value.
    * FALSE: The false value.

    * ANSWER_NAMESPACE: The namespace for the answer UI.
    * ASSOCIATION_NAMESPACE: The namespace for the association UI.
    * CHANGE_HISTORY_NAMESPACE: The namespace for the change history UI.
    * CHANGE_HISTORY_ITEM_NAMESPACE: The namespace for the change history item UI.
    * CUSTOM_FIELD_NAMESPACE: The namespace for the custom field UI.
    * DEFAULT_NAMESPACE: The namespace for the default UI.
    * DIFFICULTY_NAMESPACE: The namespace for the difficulty UI.
    * FLASHCARD_NAMESPACE: The namespace for the flashcard UI.
    * NOTE_NAMESPACE: The namespace for the note UI.
    * OPTION_NAMESPACE: The namespace for the option UI.
    * PRIORITY_NAMESPACE: The namespace for the priority UI.
    * QUESTION_NAMESPACE: The namespace for the question UI.
    * STACK_NAMESPACE: The namespace for the stack UI.
    * TAG_NAMESPACE: The namespace for the tag UI.
    * USER_NAMESPACE: The namespace for the user UI.

    * CREATE_UI_NAMESPACE: The namespace for the create UI.
    * DASHBOARD_UI_NAMESPACE: The namespace for the dashboard UI.
    * EDIT_UI_NAMESPACE: The namespace for the edit UI.
    * MAIN_UI_NAMESPACE: The namespace for the main UI.
    * REPORT_UI_NAMESPACE: The namespace for the report UI.
    * SEARCH_UI_NAMESPACE: The namespace for the search UI.
    * SETTING_UI_NAMESPACE: The namespace for the setting UI.

    * NOW: The current time.
    * TODAY: The current date.
    * TOMORROW: The current date plus one day.
    * YESTERDAY: The current date minus one day.
    """

    APPLICATION_NAME: Final[str] = "🐸 StudyFrog"
    APPLICATION_VERSION: Final[float] = 0.1

    BASE_ID: Final[int] = 10000

    CWD: Final[str] = os.getcwd()

    DATA_PATH: Final[str] = path.join(
        CWD,
        "data",
    )

    DATABASE_PATH: Final[str] = path.join(
        DATA_PATH,
        "database.db",
    )

    EXPORT_PATH: Final[str] = path.join(
        DATA_PATH,
        "exports",
    )

    IMPORT_PATH: Final[str] = path.join(
        DATA_PATH,
        "imports",
    )

    ANSWERS: Final[str] = "answers"
    ASSOCIATIONS: Final[str] = "associations"
    CHANGE_HISTORIES: Final[str] = "change_histories"
    CHANGE_HISTORY_ITEMS: Final[str] = "change_history_items"
    COMMENTS: Final[str] = "comments"
    CUSTOM_FIELDS: Final[str] = "custom_fields"
    DEFAULTS: Final[str] = "defaults"
    DIFFICULTIES: Final[str] = "difficulties"
    FLASHCARDS: Final[str] = "flashcards"
    LEARNING_SESSIONS: Final[str] = "learning_sessions"
    LEARNING_SESSION_ACTIONS: Final[str] = "learning_session_actions"
    LEARNING_SESSION_ITEMS: Final[str] = "learning_session_items"
    NOTES: Final[str] = "notes"
    OPTIONS: Final[str] = "options"
    PRIORITIES: Final[str] = "priorities"
    QUESTIONS: Final[str] = "questions"
    SETTINGS: Final[str] = "settings"
    STACKS: Final[str] = "stacks"
    STATUSES: Final[str] = "statuses"
    SUBJECTS: Final[str] = "subjects"
    TAGS: Final[str] = "tags"
    TEACHERS: Final[str] = "teachers"
    USERS: Final[str] = "users"

    DEFAULT_FONT_FAMILY: Final[str] = "Helvetica"
    DEFAULT_FONT_SIZE: Final[int] = 16

    VERY_LARGE_FONT_SIZE: Final[int] = 48
    LARGE_FONT_SIZE: Final[int] = 24
    MEDIUM_FONT_SIZE: Final[int] = 16
    SMALL_FONT_SIZE: Final[int] = 12

    BOLD: Final[str] = "bold"
    ITALIC: Final[str] = "italic"
    NORMAL: Final[str] = "normal"
    OVERSTRIKE: Final[str] = "overstrike"
    UNDERLINE: Final[str] = "underline"

    DEFAULT_GEOMETRY: Final[str] = "1920x1080"

    DEFAULT_DATE_FORMAT: Final[str] = "%Y-%m-%d"
    DEFAULT_TIME_FORMAT: Final[str] = "%H:%M:%S"

    DEFAULT_DATE_REGEX: Final[str] = r"^\d{4}-\d{2}-\d{2}$"
    DEFAULT_TIME_REGEX: Final[str] = r"^\d{2}:\d{2}:\d{2}$"

    DEFAULT_DATETIME_FORMAT: Final[str] = (
        f"{DEFAULT_DATE_FORMAT} - {DEFAULT_TIME_FORMAT}"
    )

    AMBER: Final[Dict[str, Any]] = {
        "default": "#FFC107",
        "50": "#FFF8E1",
        "100": "#FFECB3",
        "200": "#FFE082",
        "300": "#FFD54F",
        "400": "#FFCA28",
        "500": "#FFC107",
        "600": "#FFB300",
        "700": "#FFA000",
        "800": "#FF8F00",
        "900": "#FF6F00",
        "A100": "#FFE57F",
        "A200": "#FFD740",
        "A400": "#FFC400",
        "A700": "#FFAB00",
    }

    BLACK: Final[str] = "#000000"

    BLUE: Final[Dict[str, Any]] = {
        "default": "#2196F3",
        "50": "#E3F2FD",
        "100": "#BBDEFB",
        "200": "#90CAF9",
        "300": "#64B5F6",
        "400": "#42A5F5",
        "500": "#2196F3",
        "600": "#1E88E5",
        "700": "#1976D2",
        "800": "#1565C0",
        "900": "#0D47A1",
        "A100": "#82B1FF",
        "A200": "#448AFF",
        "A400": "#2979FF",
        "A700": "#2962FF",
    }

    BLUE_GREY: Final[Dict[str, Any]] = {
        "default": "#607D8B",
        "50": "#ECEFF1",
        "100": "#CFD8DC",
        "200": "#B0BEC5",
        "300": "#90A4AE",
        "400": "#78909C",
        "500": "#607D8B",
        "600": "#546E7A",
        "700": "#455A64",
        "800": "#37474F",
        "900": "#263238",
    }

    BROWN: Final[Dict[str, Any]] = {
        "default": "#795548",
        "50": "#EFEBE9",
        "100": "#D7CCC8",
        "200": "#BCAAA4",
        "300": "#A1887F",
        "400": "#8D6E63",
        "500": "#795548",
        "600": "#6D4C41",
        "700": "#5D4037",
        "800": "#4E342E",
        "900": "#3E2723",
    }

    CYAN: Final[Dict[str, Any]] = {
        "default": "#00BCD4",
        "50": "#E0F7FA",
        "100": "#B2EBF2",
        "200": "#80DEEA",
        "300": "#4DD0E1",
        "400": "#26C6DA",
        "500": "#00BCD4",
        "600": "#00ACC1",
        "700": "#0097A7",
        "800": "#00838F",
        "900": "#006064",
        "A100": "#84FFFF",
        "A200": "#18FFFF",
        "A400": "#00E5FF",
        "A700": "#00B8D4",
    }

    DEPP_ORANGE: Final[Dict[str, Any]] = {
        "default": "#FF5722",
        "50": "#FBE9E7",
        "100": "#FFCCBC",
        "200": "#FFAB91",
        "300": "#FF8A65",
        "400": "#FF7043",
        "500": "#FF5722",
        "600": "#F4511E",
        "700": "#E64A19",
        "800": "#D84315",
        "900": "#BF360C",
        "A100": "#FF9E80",
        "A200": "#FF6E40",
        "A400": "#FF3D00",
        "A700": "#DD2C00",
    }

    DEEP_PURPLE: Final[Dict[str, Any]] = {
        "default": "#673AB7",
        "50": "#EDE7F6",
        "100": "#D1C4E9",
        "200": "#B39DDB",
        "300": "#9575CD",
        "400": "#7E57C2",
        "500": "#673AB7",
        "600": "#5E35B1",
        "700": "#512DA8",
        "800": "#4527A0",
        "900": "#311B92",
        "A100": "#B388FF",
        "A200": "#7C4DFF",
        "A400": "#651FFF",
        "A700": "#6200EA",
    }

    GREEN: Final[Dict[str, Any]] = {
        "default": "#4CAF50",
        "50": "#E8F5E9",
        "100": "#C8E6C9",
        "200": "#A5D6A7",
        "300": "#81C784",
        "400": "#66BB6A",
        "500": "#4CAF50",
        "600": "#43A047",
        "700": "#388E3C",
        "800": "#2E7D32",
        "900": "#1B5E20",
        "A100": "#B9F6CA",
        "A200": "#69F0AE",
        "A400": "#00E676",
        "A700": "#00C853",
    }

    GREY: Final[Dict[str, Any]] = {
        "default": "#9E9E9E",
        "50": "#FAFAFA",
        "100": "#F5F5F5",
        "200": "#EEEEEE",
        "300": "#E0E0E0",
        "400": "#BDBDBD",
        "500": "#9E9E9E",
        "600": "#757575",
        "700": "#616161",
        "800": "#424242",
        "900": "#212121",
    }

    INDIGO: Final[Dict[str, Any]] = {
        "default": "#3F51B5",
        "50": "#E8EAF6",
        "100": "#C5CAE9",
        "200": "#9FA8DA",
        "300": "#7986CB",
        "400": "#5C6BC0",
        "500": "#3F51B5",
        "600": "#3949AB",
        "700": "#303F9F",
        "800": "#283593",
        "900": "#1A237E",
        "A100": "#8C9EFF",
        "A200": "#536DFE",
        "A400": "#3D5AFE",
        "A700": "#304FFE",
    }

    LIGHT_BLUE = {
        "default": "#03A9F4",
        "50": "#E1F5FE",
        "100": "#B3E5FC",
        "200": "#81D4FA",
        "300": "#4FC3F7",
        "400": "#29B6F6",
        "500": "#03A9F4",
        "600": "#039BE5",
        "700": "#0288D1",
        "800": "#0277BD",
        "900": "#01579B",
        "A100": "#80D8FF",
        "A200": "#40C4FF",
        "A400": "#00B0FF",
        "A700": "#0091EA",
    }

    LIGHT_GREEN: Final[Dict[str, Any]] = {
        "default": "#CDDC39",
        "50": "#F1F8E9",
        "100": "#DCEDC8",
        "200": "#C5E1A5",
        "300": "#AED581",
        "400": "#9CCC65",
        "500": "#8BC34A",
        "600": "#7CB342",
        "700": "#689F38",
        "800": "#558B2F",
        "900": "#33691E",
        "A100": "#CCFF90",
        "A200": "#B2FF59",
        "A400": "#76FF03",
        "A700": "#64DD17",
    }

    LIME: Final[Dict[str, Any]] = {
        "default": "#CDDC39",
        "50": "#F9FBE7",
        "100": "#F0F4C3",
        "200": "#E6EE9C",
        "300": "#DCE775",
        "400": "#D4E157",
        "500": "#CDDC39",
        "600": "#C0CA33",
        "700": "#AFB42B",
        "800": "#9E9D24",
        "900": "#827717",
        "A100": "#F4FF81",
        "A200": "#EEFF41",
        "A400": "#C6FF00",
        "A700": "#AEEA00",
    }

    ORANGE: Final[Dict[str, Any]] = {
        "default": "#FF9800",
        "50": "#FFF3E0",
        "100": "#FFE0B2",
        "200": "#FFCC80",
        "300": "#FFB74D",
        "400": "#FFA726",
        "500": "#FF9800",
        "600": "#FB8C00",
        "700": "#F57C00",
        "800": "#EF6C00",
        "900": "#E65100",
        "A100": "#FFD180",
        "A200": "#FFAB40",
        "A400": "#FF9100",
        "A700": "#FF6D00",
    }

    PINK: Final[Dict[str, Any]] = {
        "default": "#E91E63",
        "50": "#FCE4EC",
        "100": "#F8BBD0",
        "200": "#F48FB1",
        "300": "#F06292",
        "400": "#EC407A",
        "500": "#E91E63",
        "600": "#D81B60",
        "700": "#C2185B",
        "800": "#AD1457",
        "900": "#880E4F",
        "A100": "#FF80AB",
        "A200": "#FF4081",
        "A400": "#F50057",
        "A700": "#C51162",
    }

    PURPLE: Final[Dict[str, Any]] = {
        "default": "#9C27B0",
        "50": "#F3E5F5",
        "100": "#E1BEE7",
        "200": "#CE93D8",
        "300": "#BA68C8",
        "400": "#AB47BC",
        "500": "#9C27B0",
        "600": "#8E24AA",
        "700": "#7B1FA2",
        "800": "#6A1B9A",
        "900": "#4A148C",
        "A100": "#EA80FC",
        "A200": "#E040FB",
        "A400": "#D500F9",
        "A700": "#AA00FF",
    }

    RED: Final[Dict[str, Any]] = {
        "default": "#F44336",
        "50": "#FFEBEE",
        "100": "#FFCDD2",
        "200": "#EF9A9A",
        "300": "#E57373",
        "400": "#EF5350",
        "500": "#F44336",
        "600": "#E53935",
        "700": "#D32F2F",
        "800": "#C62828",
        "900": "#B71C1C",
        "A100": "#FF8A80",
        "A200": "#FF5252",
        "A400": "#FF1744",
        "A700": "#D50000",
    }

    TEAL = {
        "default": "#009688",
        "50": "#E0F2F1",
        "100": "#B2DFDB",
        "200": "#80CBC4",
        "300": "#4DB6AC",
        "400": "#26A69A",
        "500": "#009688",
        "600": "#00897B",
        "700": "#00796B",
        "800": "#00695C",
        "900": "#004D40",
        "A100": "#A7FFEB",
        "A200": "#64FFDA",
        "A400": "#1DE9B6",
        "A700": "#00BFA5",
    }

    WHITE: Final[str] = "#ffffff"

    YELLOW: Final[Dict[str, Any]] = {
        "default": "#FFEB3B",
        "50": "#FFFDE7",
        "100": "#FFF9C4",
        "200": "#FFF59D",
        "300": "#FFF176",
        "400": "#FFEE58",
        "500": "#FFEB3B",
        "600": "#FDD835",
        "700": "#FBC02D",
        "800": "#F9A825",
        "900": "#F57F17",
        "A100": "#FFFF8D",
        "A200": "#FFFF00",
        "A400": "#FFEA00",
        "A700": "#FFD600",
    }

    BACKWARD_DIRECTION: Final[str] = "backward"
    FORWARD_DIRECTION: Final[str] = "forward"

    GLOBAL_NAMESPACE: Final[str] = "GLOBAL"

    HIGHEST: Final[str] = "highest"
    HIGH: Final[str] = "high"
    LOW: Final[str] = "low"
    LOWEST: Final[str] = "lowest"

    MEDIUM: Final[str] = "medium"
    HARD: Final[str] = "hard"
    EASY: Final[str] = "easy"

    NEW: Final[str] = "new"
    LEARNING: Final[str] = "learning"
    REVIEW: Final[str] = "review"
    COMPLETED: Final[str] = "completed"

    TRUE: Final[str] = "true"
    FALSE: Final[str] = "false"

    CREATE_UI_NAMESPACE: Final[str] = "CREATE_UI"
    DASHBOARD_UI_NAMESPACE: Final[str] = "DASHBOARD_UI"
    EDIT_UI_NAMESPACE: Final[str] = "EDIT_UI"
    LEARNING_SESSION_NAMESPACE: Final[str] = "LEARNING_SESSION"
    MAIN_UI_NAMESPACE: Final[str] = "MAIN_UI"
    REPORT_UI_NAMESPACE: Final[str] = "REPORT_UI"
    SEARCH_UI_NAMESPACE: Final[str] = "SEARCH_UI"
    SETTING_UI_NAMESPACE: Final[str] = "SETTING_UI"
    STACK_SELECTION_NAMESPACE: Final[str] = "STACK_SELECTION"

    FLASHCARD_IMPORTER_NAMESPACE: Final[str] = "FLASHCARD_IMPORTER"

    # The current date and time
    NOW: Final[datetime] = datetime.now()

    # The current date
    TODAY: Final[datetime] = datetime.today()

    # The next day
    TOMORROW: Final[datetime] = datetime.today() + timedelta(days=1)

    # The previous day
    YESTERDAY: Final[datetime] = datetime.today() - timedelta(days=1)

    # The start of the week
    START_OF_WEEK: Final[datetime] = datetime.today() - timedelta(
        days=datetime.today().weekday()
    )

    # The end of the week
    END_OF_WEEK: Final[datetime] = START_OF_WEEK + timedelta(days=6)

    # The start of the month
    START_OF_MONTH: Final[datetime] = datetime.today().replace(day=1)

    # The end of the month
    END_OF_MONTH: Final[datetime] = START_OF_MONTH + timedelta(days=31)

    # The start of the year
    START_OF_YEAR: Final[datetime] = datetime.today().replace(month=1, day=1)

    # The end of the year
    END_OF_YEAR: Final[datetime] = START_OF_YEAR + timedelta(days=365)

    # The learning modes
    LEARNING_MODES: Final[List[str]] = [
        "Default",
        "Recall",
        "Recall (at random)",
        "Speed-Test",
        "Spaced Repetition",
    ]

    # The question types
    QUESTION_TYPES: Final[List[str]] = [
        "Multiple Select",
        "Open Answer",
        "Single Select",
        "True or False",
    ]

    # Template for JSON imports and exports from the application
    JSON_TEMPLATE: Final[Dict[str, List[Optional[Any]]]] = {
        "answers": [],
        "associations": [],
        "change_histories": [],
        "change_history_items": [],
        "comments": [],
        "custom_fields": [],
        "defaults": [],
        "difficulties": [],
        "flashcards": [],
        "notes": [],
        "options": [],
        "priorities": [],
        "questions": [],
        "settings": [],
        "stacks": [],
        "statuses:": [],
        "users": [],
    }

    # The repetition base interval in days
    BASE_REPETITION_INTERVAL_DAYS: Final[int] = 1

    # The repetition base interval in minutes
    BASE_REPETITION_INTERVAL_MINUTES: Final[int] = 2

    # The repetition base interval in seconds
    BASE_REPETITION_INTERVAL_SECONDS: Final[int] = 120

    @classmethod
    def get_base_id(cls) -> int:
        """
        Returns the base ID.

        The base ID is used to generate unique IDs for objects in the application.

        Returns:
            int: The base ID.
        """
        # Copy the base ID to prevent external modification
        return copy.deepcopy(cls.BASE_ID)

    @classmethod
    def get_base_repetition_interval(
        cls,
        what: Literal[
            "days",
            "minutes",
            "seconds",
        ] = "days",
    ) -> int:
        """
        Returns the base repetition interval in the specified unit.

        The base repetition interval is used to calculate the interval for flashcards.

        Args:
            what (Literal["days", "minutes", "seconds"]): The unit of the base repetition interval. Defaults to "days".

        Returns:
            int: The base repetition interval.
        """

        # Check, if the passed what parameter is "days"
        if what == "days":
            # Return the base repetition interval in days
            return copy.deepcopy(cls.BASE_REPETITION_INTERVAL_DAYS)

        # Check, if the passed what parameter is "minutes"
        if what == "minutes":
            # Return the base repetition interval in minutes
            return copy.deepcopy(cls.BASE_REPETITION_INTERVAL_MINUTES)

        # Return the base repetition interval in seconds
        return copy.deepcopy(cls.BASE_REPETITION_INTERVAL_SECONDS)

    @classmethod
    def get_base_repetition_interval_seconds(cls) -> int:
        """
        Returns the base repetition interval in seconds.

        The base repetition interval is used to calculate the interval for flashcards.

        Returns:
            int: The base repetition interval.
        """
        # Copy the base repetition interval to prevent external modification
        return copy.deepcopy(cls.BASE_REPETITION_INTERVAL_SECONDS)

    @classmethod
    def get_colors(
        cls,
        as_dict: bool = False,
    ) -> Union[Dict[str, str], List[str]]:
        """
        Returns the colors as a dictionary or a list.

        Args:
            as_dict (bool): If True, returns the colors as a dictionary with color names as keys and color codes as values. Defaults to False.

        Returns:
            Union[Dict[str, str], List[str]]: The colors as a dictionary or a list.
        """
        if as_dict:
            # Initialize an empty dictionary
            result: Dict[str, str] = {}

            # Add blue colors
            result.update(cls.BLUE)

            # Add red colors
            result.update(cls.RED)

            # Add green colors
            result.update(cls.GREEN)

            # Add yellow colors
            result.update(cls.YELLOW)

            # Add orange colors
            result.update(cls.ORANGE)

            # Add pink colors
            result.update(cls.PINK)

            # Add purple colors
            result.update(cls.PURPLE)

            # Add teal colors
            result.update(cls.TEAL)

            # Add white colors
            result.update(cls.WHITE)

            # Add black colors
            result.update(cls.BLACK)

            # Return the colors as a dictionary
            return result
        else:
            # Return the colors as a list
            return list(
                cls.BLUE.values()
                + cls.RED.values()
                + cls.GREEN.values()
                + cls.YELLOW.values()
                + cls.ORANGE.values()
                + cls.PINK.values()
                + cls.PURPLE.values()
                + cls.TEAL.values()
                + cls.WHITE.values()
                + cls.BLACK.values()
            )
