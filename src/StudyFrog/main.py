"""
Author: lodego
Date: 2025-02-05
"""

from core.application import Application


def main() -> None:
    """
    The entry point of the StudyFrog application.

    Initializes the singleton Application class instance and starts it.

    Args:
        None

    Returns:
        None
    """

    # Initialize the application
    application: Application = Application()

    # Start the application
    application.start_application()

    # Stop the application
    application.stop_application()


if __name__ == "__main__":
    main()
