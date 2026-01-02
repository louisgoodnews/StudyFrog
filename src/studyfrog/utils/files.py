"""
Author: Louis Goodnews
Date: 2025-12-10
"""

import json

from pathlib import Path
from typing import Any, Final, Optional

from utils.directories import create_directory


# ---------- Exports ---------- #

__all__: Final[list[str]] = [
    "create_file",
    "does_file_exist",
    "does_file_have_content",
    "ensure_file",
    "read_file_json",
    "read_file_text",
    "remove_file",
    "write_file_json",
    "write_file_text",
]


# ---------- Functions ---------- #


def create_file(file: Path) -> bool:
    """
    Creates a file if it does not exist.

    Args:
        file (Path): The file to create.

    Returns:
        bool: True if the file was created, False otherwise.
    """

    if file.exists():
        return True

    try:
        create_directory(directory=file.parent)

        file.touch(exist_ok=True)

        return True
    except Exception:
        return False


def does_file_exist(file: Path) -> bool:
    """
    Returns True if a file exists, False otherwise.

    Args:
        file (Path): The file to check.

    Returns:
        bool: True if the file exists, False otherwise.
    """

    return file.exists()


def does_file_have_content(file: Path) -> bool:
    """
    Returns True if a file has content, False otherwise.

    Args:
        file (Path): The file to check.

    Returns:
        bool: True if the file has content, False otherwise.
    """

    if not does_file_exist(file=file):
        return False

    return file.stat().st_size > 0


def ensure_file(file: Path) -> bool:
    """
    Ensures the existance of a file.

    Args:
        file (Path): The file to ensure.

    Returns:
        bool: True if the file exists, False otherwise.
    """

    return create_file(file=file) or does_file_exist(file=file)


def read_file_json(
    file: Path,
    encoding: str = "utf-8",
) -> Optional[dict[str, Any]]:
    """
    Reads the JSON content of a given file.

    Args:
        file (Path): The file to read.
        encoding (str, optional): The encoding of the file. Defaults to "utf-8".

    Returns:
        Optional[str]: The text content of the file, or None if the file does not exist.
    """

    text: Optional[str] = read_file_text(
        encoding=encoding,
        file=file,
    )

    if not text:
        return None

    return json.loads(text)


def read_file_text(
    file: Path,
    encoding: str = "utf-8",
) -> Optional[str]:
    """
    Reads the text content of a given file.

    Args:
        file (Path): The file to read.
        encoding (str, optional): The encoding of the file. Defaults to "utf-8".

    Returns:
        Optional[str]: The text content of the file, or None if the file does not exist.
    """

    if not does_file_exist(file=file):
        return None

    return file.read_text(encoding=encoding)


def remove_file(file: Path) -> bool:
    """
    Removes a file.

    Args:
        file (Path): The file to remove.

    Returns:
        bool: True if the file was removed, False otherwise.
    """

    if not does_file_exist(file=file):
        return True

    file.unlink()

    return True


def write_file_json(
    data: dict[str, Any],
    file: Path,
    encoding: str = "utf-8",
) -> bool:
    """
    Writes JSON content to a given file.

    Args:
        data (dict[str, Any]): The data to write.
        encoding (str, optional): The encoding of the file. Defaults to "utf-8".
        file (Path): The file to write to.

    Returns:
        bool: True if the file was written, False otherwise.
    """

    ensure_file(file=file)

    file.write_text(
        data=json.dumps(
            data,
            indent=4,
            sort_keys=True,
        ),
        encoding=encoding,
    )

    return True


def write_file_text(
    data: str,
    file: Path,
    encoding: str = "utf-8",
) -> bool:
    """
    Writes text content to a given file.

    Args:
        data (str): The data to write.
        encoding (str, optional): The encoding of the file. Defaults to "utf-8".
        file (Path): The file to write to.

    Returns:
        bool: True if the file was written, False otherwise.
    """

    ensure_file(file=file)

    file.write_text(
        data=data,
        encoding=encoding,
    )

    return True
