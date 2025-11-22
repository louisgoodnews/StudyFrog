"""
Author: Louis Goodnews
Date: 2025-11-16
"""

from typing import Final


# ---------- Exceptions ---------- #


class GenericStudyFrogException(Exception):
    """
    Generic exception for StudyFrog.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes the exception.

        Args:
            message (str): The message to display.
        """
        self.message = message
        super().__init__(message)


class StudyFrogTableExtractionException(GenericStudyFrogException):
    """
    Exception raised when a table extraction fails.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes the exception.

        Args:
            message (str): The message to display.
        """
        self.message = message
        super().__init__(message)


class StudyFrogTableInsertionException(GenericStudyFrogException):
    """
    Exception raised when a table insertion fails.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes the exception.

        Args:
            message (str): The message to display.
        """
        self.message = message
        super().__init__(message)


class StudyFrogTableLookupException(GenericStudyFrogException):
    """
    Exception raised when a table lookup fails.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes the exception.

        Args:
            message (str): The message to display.
        """
        self.message = message
        super().__init__(message)


class StudyFrogTableRetrievalException(GenericStudyFrogException):
    """
    Exception raised when a table retrieval fails.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes the exception.

        Args:
            message (str): The message to display.
        """
        self.message = message
        super().__init__(message)


class StudyFrogTableUpdateException(GenericStudyFrogException):
    """
    Exception raised when a table update fails.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes the exception.

        Args:
            message (str): The message to display.
        """
        self.message = message
        super().__init__(message)


# ---------- Auto-Export ---------- #

# Auto-export all non-private symbols
__all__: Final[list[str]] = [
    key
    for (
        key,
        value,
    ) in globals().items()
    if not key.startswith("_")
    and isinstance(
        value,
        Exception,
    )
]
