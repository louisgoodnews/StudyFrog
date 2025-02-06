"""
Author: lodego
Date: 2025-02-05
"""

import uuid

from datetime import datetime

from typing import *

from utils.field import Field
from utils.logger import Logger
from utils.manager import BaseObjectManager
from utils.object import MutableBaseObject, ImmutableBaseObject


__all__: List[str] = [
    "ImmutableQuestion",
    "MutableQuestion",
    "QuestionConverter",
    "QuestionFactory",
    "QuestionManager",
    "QuestionModel",
]


class ImmutableQuestion(ImmutableBaseObject):
    """
    An immutable class representing a question.

    Attributes:
        Questions (List[int]): The IDs of the Questions.
        created_at (datetime): The timestamp when the question was created.
        id (int): The ID of the question.
        is_correct (bool): Whether the question is correct or not.
        key (str): The key of the question.
        question_text (str): The text of the question.
        question_type (Literal["MULTIPLE_CHOICE", "TRUE_FALSE", "FILL_IN_THE_BLANKS"]): The type of the question.
        updated_at (datetime): The timestamp when the question was last updated.
        uuid (str): The UUID of the question.
    """

    def __init__(
        self,
        question_text: str,
        question_type: Literal["MULTIPLE_CHOICE", "TRUE_FALSE", "FILL_IN_THE_BLANKS"],
        Questions: Optional[List[int]] = None,
        correct_Question: Optional[Unoin[int, bool]] = None,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableQuestion class.

        Args:
            Questions (Optional[List[int]]): The IDs of the Questions.
            created_at (Optional[datetime]): The timestamp when the question was created.
            correct_Question (Optional[Unoin[int, bool]]): The ID of the correct Question or whether the question is correct.
            id (Optional[int]): The ID of the question.
            key (Optional[str]): The key of the question.
            question_text (str): The text of the question.
            question_type (Literal["MULTIPLE_CHOICE", "TRUE_FALSE", "FILL_IN_THE_BLANKS"]): The type of the question.
            updated_at (Optional[datetime]): The timestamp when the question was last updated.
            uuid (Optional[str]): The UUID of the question.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            Questions=Questions,
            correct_Question=correct_Question,
            created_at=created_at,
            id=id,
            key=key,
            question_text=question_text,
            question_type=question_type,
            updated_at=updated_at,
            uuid=uuid,
        )


class MutableQuestion(MutableBaseObject):
    """
    A mutable class representing a question.

    Attributes:
        Questions (Optional[List[int]]): The IDs of the Questions.
        correct_Question (Optional[Unoin[int, bool]]): The ID of the correct Question or whether the question is correct.
        created_at (Optional[datetime]): The timestamp when the question was created.
        id (Optional[int]): The ID of the question.
        key (Optional[str]): The key of the question.
        question_text (str): The text of the question.
        question_type (Literal["MULTIPLE_CHOICE", "TRUE_FALSE", "FILL_IN_THE_BLANKS"]): The type of the question.
        updated_at (Optional[datetime]): The timestamp when the question was last updated.
        uuid (Optional[str]): The UUID of the question.
    """

    def __init__(
        self,
        question_text: str,
        question_type: Literal["MULTIPLE_CHOICE", "TRUE_FALSE", "FILL_IN_THE_BLANKS"],
        Questions: Optional[List[int]] = None,
        correct_Question: Optional[Unoin[int, bool]] = None,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableQuestion class.

        Args:
            question_text (str): The text of the question.
            question_type (Literal["MULTIPLE_CHOICE", "TRUE_FALSE", "FILL_IN_THE_BLANKS"]): The type of the question.
            Questions (Optional[List[int]]): The IDs of the Questions.
            correct_Question (Optional[Unoin[int, bool]]): The ID of the correct Question or whether the question is correct.
            created_at (Optional[datetime]): The timestamp when the question was created.
            id (Optional[int]): The ID of the question.
            key (Optional[str]): The key of the question.
            updated_at (Optional[datetime]): The timestamp when the question was last updated.
            uuid (Optional[str]): The UUID of the question.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            Questions=Questions,
            correct_Question=correct_Question,
            created_at=created_at,
            id=id,
            key=key,
            question_text=question_text,
            question_type=question_type,
            updated_at=updated_at,
            uuid=uuid,
        )


class QuestionConverter:
    logger: Logger = Logger.get_logger(name="QuestionConverter")


class QuestionFactory:
    logger: Logger = Logger.get_logger(name="QuestionFactory")

    @classmethod
    def create_question(
        cls,
        question_text: str,
        question_type: Literal["MULTIPLE_CHOICE", "TRUE_FALSE", "FILL_IN_THE_BLANKS"],
        Questions: Optional[List[int]] = None,
        correct_Question: Optional[Unoin[int, bool]] = None,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> MutableQuestion:
        """
        Creates a new instance of the MutableQuestion class.

        Args:
            question_text (str): The text of the question.
            question_type (Literal["MULTIPLE_CHOICE", "TRUE_FALSE", "FILL_IN_THE_BLANKS"]): The type of the question.
            Questions (Optional[List[int]]): The IDs of the Questions.
            correct_Question (Optional[Unoin[int, bool]]): The ID of the correct Question or whether the question is correct.
            created_at (Optional[datetime]): The timestamp when the question was created.
            id (Optional[int]): The ID of the question.
            key (Optional[str]): The key of the question.
            updated_at (Optional[datetime]): The timestamp when the question was last updated.
            uuid (Optional[str]): The UUID of the question.

        Returns:
            MutableQuestion: A new instance of the MutableQuestion class.
        """
        try:
            # Attempt to create an d return an MutableQuestion object
            return MutableQuestion(
                Questions=Questions,
                correct_Question=correct_Question,
                created_at=created_at,
                id=id,
                key=key,
                question_text=question_text,
                question_type=question_type,
                updated_at=updated_at,
                uuid=uuid,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_question' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class QuestionManager(BaseObjectManager):
    pass


class QuestionModel(BaseModel):
    def __init__(self) -> None:
        super().__init__()
