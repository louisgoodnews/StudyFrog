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
    "ImmutableAnswer",
    "MutableAnswer",
    "AnswerConverter",
    "AnswerFactory",
    "AnswerManager",
    "AnswerModel",
]


class ImmutableAnswer(ImmutableBaseObject):
    """
    An immutable class representing an answer.

    An answer is a piece of text that is associated with a question and is either correct or not.

    Attributes:
        answer_text (str): The text of the answer.
        created_at (datetime): The timestamp when the answer was created.
        id (int): The ID of the answer.
        is_correct (bool): Whether the answer is correct or not.
        key (str): The key of the answer.
        updated_at (datetime): The timestamp when the answer was last updated.
        uuid (str): The UUID of the answer.
    """

    def __init__(
        self,
        answer_text: str,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        is_correct: Optional[bool] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableAnswer class.

        Args:
            answer_text (str): The text of the answer.
            created_at (Optional[datetime]): The timestamp when the answer was created.
            id (Optional[int]): The ID of the answer.
            is_correct (Optional[bool]): Whether the answer is correct or not.
            key (Optional[str]): The key of the answer.
            updated_at (Optional[datetime]): The timestamp when the answer was last updated.
            uuid (Optional[str]): The UUID of the answer.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            answer_text=answer_text,
            created_at=created_at,
            id=id,
            is_correct=is_correct,
            key=key,
            updated_at=updated_at,
            uuid=uuid or str(uuid.uuid4()),
        )


class MutableAnswer(MutableBaseObject):
    """
    A mutable class representing an answer.

    Attributes:
        answer_text (str): The text of the answer.
        created_at (datetime): The timestamp when the answer was created.
        id (int): The ID of the answer.
        is_correct (bool): Whether the answer is correct or not.
        key (str): The key of the answer.
        updated_at (datetime): The timestamp when the answer was last updated.
        uuid (str): The UUID of the answer.
    """

    def __init__(
        self,
        answer_text: str,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        is_correct: Optional[bool] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableAnswer class.

        Args:
            answer_text (str): The text of the answer.
            created_at (Optional[datetime]): The timestamp when the answer was created.
            id (Optional[int]): The ID of the answer.
            is_correct (Optional[bool]): Whether the answer is correct or not.
            key (Optional[str]): The key of the answer.
            updated_at (Optional[datetime]): The timestamp when the answer was last updated.
            uuid (Optional[str]): The UUID of the answer.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            answer_text=answer_text,
            created_at=created_at,
            id=id,
            is_correct=is_correct,
            key=key,
            updated_at=updated_at,
            uuid=uuid,
        )


class AnswerConverter:
    logger: Logger = Logger.get_logger(name="AnswerConverter")


class AnswerFactory:
    logger: Logger = Logger.get_logger(name="AnswerFactory")

    @classmethod
    def create_answer(
        cls,
        answer_text: str,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        is_correct: Optional[bool] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutableAnswer]:
        """
        Creates and returns a new instance of ImmutableAnswer class.

        Args:
            answer_text (str): The text of the answer.
            created_at (Optional[datetime]): The timestamp when the answer was created.
            id (Optional[int]): The ID of the answer.
            is_correct (Optional[bool]): Whether the answer is correct or not.
            key (Optional[str]): The key of the answer.
            updated_at (Optional[datetime]): The timestamp when the answer was last updated.
            uuid (Optional[str]): The UUID of the answer.

        Returns:
            Optional[ImmutableAnswer]: The created answer object if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the answer.
        """
        try:
            # Attempt to create an d return an ImmutableAnswer object
            return ImmutableAnswer(
                answer_text=answer_text,
                created_at=created_at,
                id=id,
                is_correct=is_correct,
                key=key,
                updated_at=updated_at,
                uuid=uuid,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_answer' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class AnswerManager(BaseObjectManager):
    pass


class AnswerModel(BaseModel):
    def __init__(self) -> None:
        super().__init__()
