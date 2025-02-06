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
    * CWD: The current working directory.
    * DATA_PATH: The path to the data directory.
    * DATABASE_PATH: The path to the database file.
    * EXPORT_PATH: The path to the export directory.
    * IMPORT_PATH: The path to the import directory.
    * DEFAULT_FONT_FAMILIY: The default font family.
    * DEFAULT_FONT_SIZE: The default font size.
    * GLOBAL_NAMESPACE: The namespace for global dispatching of events.
    * NOW: The current time.
    * TODAY: The current date.
    * TOMORROW: The current date plus one day.
    * YESTERDAY: The current date minus one day.
    """

    APPLICATION_NAME: str = "StudyFrog"
    APPLICATION_VERSION: float = 0.1

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

    DEFAULT_FONT_FAMILIY: str = "Helvetica"
    DEFAULT_FONT_SIZE: int = 16

    GLOBAL_NAMESPACE: str = "GLOBAL"

    NOW: datetime = datetime.now()

    TODAY: datetime = datetime.today()
    TOMORROW: datetime = datetime.today() + timedelta(days=1)
    YESTERDAY: datetime = datetime.today() - timedelta(days=1)
