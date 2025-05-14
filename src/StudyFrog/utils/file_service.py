"""
Author: lodego
Date: 2025-04-19
"""

import aiofiles
import os
import traceback

from pathlib import Path
from typing import *

from utils.logger import Logger

__all__: Final[List[str]] = ["FileService"]


class FileService:
    """
    Provides asynchronous file system operations for reading, writing, appending, creating, and deleting files.

    This service abstracts common file I/O operations using async capabilities via `aiofiles`,
    while offering built-in logging and error handling mechanisms.

    All methods are class methods, allowing stateless and utility-like usage. This class is
    intended to be used for backend operations where safe, asynchronous file interactions are needed,
    such as saving logs, configuration files, exports, or cached data.

    Attributes:
        logger (Logger): An instance of the Logger class used for logging purposes.
    """

    logger: Final[Logger] = Logger.get_logger(name="FileService")

    @classmethod
    async def append(
        cls,
        content: Union[bytes, str],
        path: str,
        encoding: str = "utf-8",
    ) -> str:
        """
        Appends content to an existing file asynchronously.

        This method checks if the given file exists and then appends the provided content
        to it using asynchronous I/O. It supports both string and byte content.

        Args:
            content (Union[bytes, str]): The content to append to the file.
            path (str): The full path to the file.
            encoding (str, optional): The encoding to use for writing string content. Defaults to 'utf-8'.

        Returns:
            Optional[str]: The path of the file if successful, or None if the file doesn't exist.

        Raises:
            Exception: If an error occurs during appending.
        """
        try:
            # Check, if the file exists
            if not os.path.exists(path=path):
                # Log a warning message
                cls.logger.warning(message=f"{path} does not exist. Aborting...")

                # Return early
                return

            # Append content to the file
            await cls.write(
                content=content,
                path=path,
                mode="a",
                encoding=encoding,
            )

            # Return the path to the caller
            return path
        except Exception as e:
            # Log an error message
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'append' method from '{cls.__name__}' class: {e}"
            )

            # Log the traceback
            cls.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    @classmethod
    async def create(
        cls,
        path: str,
        content: Optional[Union[bytes, str]] = None,
        encoding: str = "utf-8",
        name: Optional[str] = None,
    ) -> Optional[str]:
        """
        Creates a new file asynchronously at the given path.

        If a filename is included in the `path`, then `name` must not be provided.
        If the `name` is provided, it is joined with the `path` to form the full path.
        If content is provided, it is written to the file immediately.

        Args:
            content (Optional[Union[bytes, str]]): The content to write to the file (optional).
            encoding (str, optional): The encoding to use for writing string content. Defaults to 'utf-8'.
            name (Optional[str]): The name of the file to be created (optional).
            path (str): The full path to the file or the directory path if `name` is given.

        Returns:
            Optional[str]: The full path to the created file or None if an error occurred.
        """
        try:
            # Convert to a pathlib.Path object
            base_path: Path = Path(path)

            # Check if path includes filename and name is also given (invalid)
            if base_path.suffix and name:
                raise ValueError(
                    "If 'path' includes a filename, 'name' must not be provided."
                )

            # Construct full file path
            if not base_path.suffix:
                if not name:
                    raise ValueError(
                        "If 'path' is a directory, 'name' must be provided."
                    )
                file_path: Path = base_path / name
            else:
                file_path: Path = base_path

            # Create parent directories if they don't exist
            file_path.parent.mkdir(
                exist_ok=True,
                parents=True,
            )

            # Create the file (touch ensures it's created)
            file_path.touch(exist_ok=False)

            # Check if content exists
            if content is not None:
                # Write initial content if provided
                await cls.write(
                    encoding=encoding,
                    content=content,
                    path=str(file_path),
                )

            # Return the full file path
            return str(file_path)
        except Exception as e:
            # Log an error message
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create' method from '{cls.__name__}' class: {e}"
            )

            # Log the traceback
            cls.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    @classmethod
    async def delete(
        cls,
        path: str,
    ) -> bool:
        """
        Asynchronously deletes a file at the given path.

        This method checks if the specified file exists, and if so, deletes it.
        It logs appropriate warnings or errors and returns True only if the deletion
        was successful.

        Args:
            path (str): The full path to the file to be deleted.

        Returns:
            bool: True if the file was successfully deleted, False otherwise.

        Raises:
            Exception: If an error occurs during file deletion.
        """
        try:
            # Check, if the file exists
            if not os.path.exists(path=path):
                # Log a warning message
                cls.logger.warning(message=f"{path} does not exist. Aborting...")

                # Return False early
                return False

            # Delete the file
            os.remove(path=path)

            # Log success
            cls.logger.info(message=f"Successfully deleted: '{path}'")

            # Return success
            return True
        except Exception as e:
            # Log an error message
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{cls.__name__}' class: {e}"
            )

            # Log the traceback
            cls.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    @classmethod
    async def read(
        cls,
        path: str,
        as_lines: bool = False,
        encoding: str = "utf-8",
    ) -> Optional[Union[str, List[str]]]:
        """
        Asynchronously reads the contents of a file at the given path.

        This method opens and reads the file either as a full string or as a list of lines,
        depending on the `as_lines` flag. It supports custom encoding and includes
        error logging and exception handling.

        Args:
            path (str): The full path to the file to read.
            as_lines (bool, optional): If True, returns a list of lines. If False, returns the full content as string. Defaults to False.
            encoding (str, optional): The encoding used to read the file. Defaults to 'utf-8'.

        Returns:
            Optional[Union[str, List[str]]]: The file content as string or list of lines if successful, None otherwise.

        Raises:
            Exception: If an error occurs during file reading.
        """
        try:
            # Check, if the file exists
            if not os.path.exists(path=path):
                # Log a warning message
                cls.logger.warning(message=f"{path} does not exist. Aborting...")

                # Return False early
                return False

            # Initialize the result (optional) str or list as None
            result: Optional[Union[str, List[str]]] = None

            # Use aiofiles to open the file asynchronously
            async with aiofiles.open(
                encoding=encoding,
                mode="r",
                path=path,
            ) as file:
                # Read the contents based on the as_lines flag
                result = await file.readlines() if as_lines else await file.read()

            # Log success
            cls.logger.info(message=f"Successfully read file: {path}")

            # Return the content
            return result
        except Exception as e:
            # Log an error message
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'read' method from '{cls.__name__}' class: {e}"
            )

            # Log the traceback
            cls.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    @classmethod
    async def write(
        cls,
        content: Union[bytes, str],
        path: str,
        mode: Literal["a", "w"] = "w",
        encoding: str = "utf-8",
    ) -> None:
        """
        Asynchronously writes content to a file.

        This method writes the provided content to the given file path using async I/O.
        It can be used to either overwrite or append to the file depending on the mode.

        Args:
            path (str): The full path to the file.
            content (Union[bytes, str]): The content to write to the file.
            mode (str, optional): File mode ('w' for overwrite, 'a' for append). Defaults to 'w'.
            encoding (str, optional): The encoding to use when writing the file. Defaults to 'utf-8'.

        Returns:
            None

        Raises:
            Exception: If an error occurs during file writing.
        """
        try:
            # Check, if the file exists
            if not os.path.exists(path=path):
                # Log a warning message
                cls.logger.warning(message=f"{path} does not exist. Aborting...")

                # Return early
                return

            # Open the file asynchronously using aiofiles
            async with aiofiles.open(
                file=path,
                mode=mode,
                encoding=encoding,
            ) as file:
                # Write the content to the file
                await file.write(content)
        except Exception as e:
            # Log an error message
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'write' method from '{cls.__name__}' class: {e}"
            )

            # Log the traceback
            cls.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e
