"""
Author: Louis Goodnews
Date: 2025-12-10
"""

import shutil

from pathlib import Path
from typing import Final


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "create_directory",
    "does_directory_exist",
    "ensure_directory",
    "is_directory_empty",
    "remove_directory",
]


# ---------- Functions ---------- #


def create_directory(directory: Path) -> bool:
    """
    Creates a directory if it does not exist.

    Args:
        directory (Path): The directory to create.

    Returns:
        bool: True if the directory was created, False otherwise.
    """

    if directory.exists():
        return True

    try:
        directory.mkdir(
            exist_ok=True,
            parents=True,
        )

        return True
    except Exception:
        return False


def does_directory_exist(directory: Path) -> bool:
    """
    Returns True if a directory exists, False otherwise.

    Args:
        directory (Path): The directory to check.

    Returns:
        bool: True if the directory exists, False otherwise.
    """

    return directory.exists()


def ensure_directory(directory: Path) -> bool:
    """
    Ensures the existance of a directory.

    Args:
        directory (Path): The directory to ensure.

    Returns:
        bool: True if the directory exists, False otherwise.
    """

    return create_directory(directory=directory) or does_directory_exist(directory=directory)


def is_directory(directory: Path) -> bool:
    """
    Returns True if the directory is a directory, False otherwise.

    Args:
        directory (Path): The directory to check.

    Returns:
        bool: True if the directory is a directory, False otherwise.
    """

    if not does_directory_exist(directory=directory):
        return False

    return directory.is_dir()


def is_directory_empty(directory: Path) -> bool:
    """
    Returns True if the directory is empty, False otherwise.

    Args:
        directory (Path): The directory to check.

    Returns:
        bool: True if the directory is empty, False otherwise.
    """

    if not does_directory_exist(directory=directory):
        return True

    return not bool(
        next(
            directory.iterdir(),
            False,
        )
    )


def remove_directory(directory: Path) -> bool:
    """
    Removes a directory.

    Args:
        directory (Path): The directory to remove.

    Returns:
        bool: True if the directory was removed, False otherwise.
    """

    if not does_directory_exist(directory=directory):
        return True

    shutil.rmtree(path=directory)

    if not does_directory_exist(directory=directory):
        return True

    return False
