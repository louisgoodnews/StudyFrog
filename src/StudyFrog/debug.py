"""
Author: lodego
Date: 2025-02-05
"""

from datetime import datetime

from scripts.clear_database import clear_database
from scripts.test_ui import test_ui
from scripts.upsert_database import upsert_database

from utils.component_accessor import ComponentAccessor
from utils.miscellaneous import Miscellaneous
from utils.logger import Logger
from utils.utils import DateUtil


def debug() -> None:
    """
    Debugging function.

    This function clears the database tables by iterating the set of model classes
    and dropping and creating the tables.
    """

    # Get the start datetime
    start: datetime = DateUtil.now()

    # Get the logger
    logger: Logger = Logger.get_logger(name="debug")

    # Log a debug message
    logger.debug(message="Debugging...")

    # Log a debug message
    logger.debug(
        message=f"Debugging completed. (runtime {DateUtil.calculate_duration(start=start)} seconds)"
    )


if __name__ == "__main__":
    debug()
