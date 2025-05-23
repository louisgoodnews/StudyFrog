"""
Author: lodego
Date: 2025-04-19
"""

from typing import *


__all__: Final[List[str]] = [
    "AnswerNotCreated",
    "AnswerNotDeleted",
    "AnswerNotFound",
    "AnswerNotUpdated",
    "AssociationNotCreated",
    "AssociationNotDeleted",
    "AssociationNotFound",
    "AssociationNotUpdated",
    "ChangeHistoryNotCreated",
    "ChangeHistoryNotDeleted",
    "ChangeHistoryNotFound",
    "ChangeHistoryNotUpdated",
    "ChangeHistoryItemNotCreated",
    "ChangeHistoryItemNotDeleted",
    "ChangeHistoryItemNotFound",
    "ChangeHistoryItemNotUpdated",
    "CommentNotCreated",
    "CommentNotDeleted",
    "CommentNotFound",
    "CommentNotUpdated",
    "CustomFieldNotCreated",
    "CustomFieldNotDeleted",
    "CustomFieldNotFound",
    "CustomFieldNotUpdated",
    "UnknownError",
]


class NotCreated(Exception):
    """
    Exception raised when an object is not created in the StudyFrog application.
    """

    def __init__(
        self,
        code: str,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the NotCreated class.

        Args:
            code (str): The code associated with the exception.
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code,
            message,
        )

    def __str__(self) -> str:
        """
        Returns a string representation of the exception.

        Args:
            None

        Returns:
            str: A string representation of the exception.
        """

        return f"{self.__class__.__name__}: {self.args[1]} (Code: {self.args[0]})"


class NotDeleted(Exception):
    """
    Exception raised when an object is not deleted in the StudyFrog application.
    """

    def __init__(
        self,
        code: str,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the NotDeleted class.

        Args:
            code (str): The code associated with the exception.
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code,
            message,
        )

    def __str__(self) -> str:
        """
        Returns a string representation of the exception.

        Args:
            None

        Returns:
            str: A string representation of the exception.
        """

        return f"{self.__class__.__name__}: {self.args[1]} (Code: {self.args[0]})"


class NotFound(Exception):
    """
    Exception raised when an object is not found in the StudyFrog application.
    """

    def __init__(
        self,
        code: str,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the NotFound class.

        Args:
            code (str): The code associated with the exception.
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code,
            message,
        )

    def __str__(self) -> str:
        """
        Returns a string representation of the exception.

        Args:
            None

        Returns:
            str: A string representation of the exception.
        """

        return f"{self.__class__.__name__}: {self.args[1]} (Code: {self.args[0]})"


class NotUpdated(Exception):
    """
    Exception raised when an object is not updated in the StudyFrog application.
    """

    def __init__(
        self,
        code: str,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the NotUpdated class.

        Args:
            code (str): The code associated with the exception.
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code,
            message,
        )

    def __str__(self) -> str:
        """
        Returns a string representation of the exception.

        Args:
            None

        Returns:
            str: A string representation of the exception.
        """

        return f"{self.__class__.__name__}: {self.args[1]} (Code: {self.args[0]})"


class UnknownError(Exception):
    """
    Exception raised when an unknown error occurs in the StudyFrog application.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the UnknownError class.

        Args:
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(message)

    def __str__(self) -> str:
        """
        Returns a string representation of the exception.

        Args:
            None

        Returns:
            str: A string representation of the exception.
        """

        return f"{self.__class__.__name__}: {self.args[0]} (Code: unknown)"


class AnswerNotCreated(NotCreated):
    """
    Exception raised when an answer is not created in the StudyFrog application.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the AnswerNotCreated class.

        Args:
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code="1000000",
            message=message,
        )


class AnswerNotDeleted(NotDeleted):
    """
    Exception raised when an answer is not deleted in the StudyFrog application.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the AnswerNotDeleted class.

        Args:
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code="1000001",
            message=message,
        )


class AnswerNotFound(NotFound):
    """
    Exception raised when an answer is not found in the StudyFrog application.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the AnswerNotFound class.

        Args:
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code="1000002",
            message=message,
        )


class AnswerNotUpdated(NotUpdated):
    """
    Exception raised when an answer is not updated in the StudyFrog application.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the AnswerNotUpdated class.

        Args:
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code="1000003",
            message=message,
        )


class AssociationNotCreated(NotCreated):
    """
    Exception raised when an association is not created in the StudyFrog application.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the AssociationNotCreated class.

        Args:
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code="1000004",
            message=message,
        )


class AssociationNotDeleted(NotDeleted):
    """
    Exception raised when an association is not deleted in the StudyFrog application.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the AssociationNotDeleted class.

        Args:
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code="1000005",
            message=message,
        )


class AssociationNotFound(NotFound):
    """
    Exception raised when an association is not found in the StudyFrog application.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the AssociationNotFound class.

        Args:
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code="1000006",
            message=message,
        )


class AssociationNotUpdated(NotUpdated):
    """
    Exception raised when an association is not updated in the StudyFrog application.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the AssociationNotUpdated class.

        Args:
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code="1000007",
            message=message,
        )


class ChangeHistoryNotCreated(NotCreated):
    """
    Exception raised when a change history is not created in the StudyFrog application.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the ChangeHistoryNotCreated class.

        Args:
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code="1000008",
            message=message,
        )


class ChangeHistoryNotDeleted(NotDeleted):
    """
    Exception raised when a change history is not deleted in the StudyFrog application.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the ChangeHistoryNotDeleted class.

        Args:
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code="1000009",
            message=message,
        )


class ChangeHistoryNotFound(NotFound):
    """
    Exception raised when a change history is not found in the StudyFrog application.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the ChangeHistoryNotFound class.

        Args:
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code="1000010",
            message=message,
        )


class ChangeHistoryNotUpdated(NotUpdated):
    """
    Exception raised when a change history is not updated in the StudyFrog application.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the ChangeHistoryNotUpdated class.

        Args:
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code="1000011",
            message=message,
        )


class ChangeHistoryItemNotCreated(NotCreated):
    """
    Exception raised when a change history item is not created in the StudyFrog application.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the ChangeHistoryItemNotCreated class.

        Args:
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code="1000012",
            message=message,
        )


class ChangeHistoryItemNotDeleted(NotDeleted):
    """
    Exception raised when a change history item is not deleted in the StudyFrog application.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the ChangeHistoryItemNotDeleted class.

        Args:
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code="1000013",
            message=message,
        )


class ChangeHistoryItemNotFound(NotFound):
    """
    Exception raised when a change history item is not found in the StudyFrog application.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the ChangeHistoryItemNotFound class.

        Args:
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code="1000014",
            message=message,
        )


class ChangeHistoryItemNotUpdated(NotUpdated):
    """
    Exception raised when a change history item is not updated in the StudyFrog application.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the ChangeHistoryItemNotUpdated class.

        Args:
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code="1000015",
            message=message,
        )


class CommentNotCreated(NotCreated):
    """
    Exception raised when a comment is not created in the StudyFrog application.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the CommentNotCreated class.

        Args:
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code="1000016",
            message=message,
        )


class CommentNotDeleted(NotDeleted):
    """
    Exception raised when a comment is not deleted in the StudyFrog application.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the CommentNotDeleted class.

        Args:
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code="1000017",
            message=message,
        )


class CommentNotFound(NotFound):
    """
    Exception raised when a comment is not found in the StudyFrog application.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the CommentNotFound class.

        Args:
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code="1000018",
            message=message,
        )


class CommentNotUpdated(NotUpdated):
    """
    Exception raised when a comment is not updated in the StudyFrog application.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the CommentNotUpdated class.

        Args:
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code="1000019",
            message=message,
        )


class CustomFieldNotCreated(NotCreated):
    """
    Exception raised when a custom field is not created in the StudyFrog application.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the CustomFieldNotCreated class.

        Args:
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code="1000020",
            message=message,
        )


class CustomFieldNotDeleted(NotDeleted):
    """
    Exception raised when a custom field is not deleted in the StudyFrog application.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the CustomFieldNotDeleted class.

        Args:
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code="1000021",
            message=message,
        )


class CustomFieldNotFound(NotFound):
    """
    Exception raised when a custom field is not found in the StudyFrog application.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the CustomFieldNotFound class.

        Args:
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code="1000022",
            message=message,
        )


class CustomFieldNotUpdated(NotUpdated):
    """
    Exception raised when a custom field is not updated in the StudyFrog application.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        """
        Initializes a new instance of the CustomFieldNotUpdated class.

        Args:
            message (str): The message associated with the exception.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            code="1000023",
            message=message,
        )
