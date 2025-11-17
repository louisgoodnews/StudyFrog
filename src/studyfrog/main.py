"""
Author: Louis Goodnews
Date: 2025-11-16
"""

from core.core import start, stop


def main() -> None:
    """
    Entrypoint of the StudyFrog project.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If any errors occur during application execution.
    """

    try:
        start()
        stop()
        exit(0)
    except Exception:
        exit(1)


if __name__ == "__main__":
    main()
