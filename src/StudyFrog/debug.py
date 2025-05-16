"""
Author: lodego
Date: 2025-02-05
"""

import tkinter

from tkinter.constants import *
from typing import *

from scripts.clear_database import clear_database
from scripts.upsert_database import upsert_database

from utils.base_view_form import BaseViewForm
from utils.component_accessor import ComponentAccessor
from utils.logger import Logger


def debug() -> None:
    """
    Debugging function.

    This function clears the database tables by iterating the set of model classes
    and dropping and creating the tables.
    """

    # Get the logger
    logger: Logger = Logger.get_logger(name="debug")

    # Log a debug message
    logger.debug(message="Debugging...")

    logger.debug(
        message=f"Operation (clear database) result: {"success!" if clear_database() else "failure!"}"
    )

    # Log a debug message
    logger.debug(message="Debugging completed.")


if __name__ == "__main__":
    debug()
