"""
Author: Louis Goodnews
Date: 2025-12-10
"""

from core.common import get_default_difficulties, get_default_priorities, get_default_user
from utils.logging import log_debug
from utils.storage import get_all_entries


def debug() -> None:
    """
    Entry point for running debugging, testing, or temporary development code.

    This function is typically executed only when the module is run directly
    (i.e., when `if __name__ == "__main__":` is true). It should contain logic
    for unit testing, integration testing, application setup validation,
    or quick ad-hoc testing during development.

    Args:
        None

    Returns:
        None
    """

    log_debug("Debugging...")
    log_debug(message=get_all_entries(table_name="difficulties"))


if __name__ == "__main__":
    debug()
