"""
Author: Louis Goodnews
Date: 2025-12-10
"""

from core.application import start_application, stop_application
from utils.logging import log_error


def main() -> None:
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
        None
    """

    try:
        start_application()
        stop_application()
        exit(0)
    except Exception as e:
        log_error(message=f"Caught an exception while running the application: {e}")
        exit(1)


if __name__ == "__main__":
    main()
