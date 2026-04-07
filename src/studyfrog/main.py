"""
Author: Louis Goodnews
Date: 2025-12-10
"""

from __future__ import annotations

from typing import Final

from studyfrog.core.application import start_application, stop_application
from studyfrog.utils.logging import log_error, log_exception


__NAME__: Final[str] = "src.main.main"


def main() -> int:
    """
    Primary entry point for the application.

    This function initializes and starts the entire application process. It is
    typically responsible for the following core tasks:
    1. System Initialization: Ensuring critical components (e.g., directory structure,
       logging, event dispatcher) are set up.
    2. Data Loading: Loading initial configuration and persistent data stores.
    3. Interface Setup: Constructing and displaying the main user interface (GUI).
    4. Main Loop Execution: Starting the application's main processing loop (e.g., Tkinter mainloop).

    The program terminates when the main loop exits.

    Args:
        None

    Returns:
        int: The exit code of the application. (0 for success, 1 for failure)
    """

    try:
        start_application()
        stop_application()
        return 0
    except Exception as e:
        log_error(
            message=f"Caught an exception while running the application: {e}",
            name=f"{__NAME__}.main",
        )
        log_exception(message="", name=f"{__NAME__}.main")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
