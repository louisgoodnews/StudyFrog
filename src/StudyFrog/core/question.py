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
from utils.model import ImmutableBaseModel
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

    def to_mutable(self) -> "MutableQuestion":
        """
        Converts the immutable question to a mutable question.

        Returns:
            MutableQuestion: The mutable version of the immutable question.
        """

        # Create a new MutableQuestion instance from the dictionary representation of the ImmutableQuestion instance
        return MutableQuestion(**self.to_dict(exclude=["logger"]))


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

    def to_immutable(self) -> ImmutableQuestion:
        """
        Converts the mutable question to an immutable question.

        Returns:
            ImmutableQuestion: The immutable version of the mutable question.
        """

        # Create a new ImmutableQuestion instance from the dictionary representation of the MutableQuestion instance
        return ImmutableQuestion(**self.to_dict(exclude=["logger"]))


class QuestionConverter:
    """
    A converter class for transforming between QuestionModel and ImmutableQuestion instances.

    This class provides methods to convert a QuestionModel instance to an ImmutableQuestion instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the QuestionConverter class.
    """

    logger: Logger = Logger.get_logger(name="QuestionConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "QuestionModel",
    ) -> Optional[ImmutableQuestion]:
        """
        Converts a given QuestionModel instance to an ImmutableQuestion instance.

        Args:
            model (QuestionModel): The QuestionModel instance to be converted.

        Returns:
            ImmutableQuestion: The converted ImmutableQuestion instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the QuestionModel instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableQuestion class from the dictionary representation of the QuestionModel instance
            return ImmutableQuestion(**model.to_dict(exclude=["logger"])["fields"])
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'model_to_object' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def object_to_model(
        cls,
        object: ImmutableQuestion,
    ) -> Optional["QuestionModel"]:
        """
        Converts a given ImmutableQuestion instance to a QuestionModel instance.

        Args:
            object (ImmutableQuestion): The ImmutableQuestion instance to be converted.

        Returns:
            QuestionModel: The converted QuestionModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ImmutableQuestion instance.
        """
        try:
            # Attempt to create and return a new instance of the QuestionModel class from the dictionary representation of the ImmutableQuestion instance
            return QuestionModel(**object.to_dict(exclude=["logger"]))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'object_to_model' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


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

    """
    Represents the structure of a question model.

    Attributes:
        created_at (datetime): The timestamp when the question was created.
        id (int): The ID of the question.
        key (str): The key of the question.
        question_text (str): The text of the question.
        question_type (Literal["MULTIPLE_CHOICE", "TRUE_FALSE", "FILL_IN_THE_BLANKS"]): The type of the question.
        updated_at (datetime): The timestamp when the question was updated.
        uuid (str): The UUID of the question.

    """

    def __init__(
        self,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        question_text: Optional[str] = None,
        question_type: Optional[
            Literal["MULTIPLE_CHOICE", "TRUE_FALSE", "FILL_IN_THE_BLANKS"]
        ] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the QuestionModel class.

        Args:
            created_at (Optional[datetime]): The timestamp when the question was created.
            id (Optional[int]): The ID of the question.
            key (Optional[str]): The key of the question.
            question_text (Optional[str]): The text of the question.
            question_type (Optional[Literal["MULTIPLE_CHOICE", "TRUE_FALSE", "FILL_IN_THE_BLANKS"]]): The type of the question.
            updated_at (Optional[datetime]): The timestamp when the question was updated.
            uuid (Optional[str]): The UUID of the question.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            table="question",
            id=(
                id
                or Field(
                    autoincrement=True,
                    default=None,
                    description="",
                    foreign_key=None,
                    index=True,
                    name="id",
                    nullable=True,
                    on_delete="CASCADE",
                    on_update="CASCADE",
                    primary_key=True,
                    size=None,
                    type="INTEGER",
                    unique=True,
                )
            ),
            created_at=(
                created_at
                or Field(
                    autoincrement=False,
                    default=None,
                    description="",
                    foreign_key=None,
                    index=False,
                    name="created_at",
                    nullable=True,
                    on_delete="NO ACTION",
                    on_update="NO ACTION",
                    primary_key=False,
                    size=None,
                    type="DATETIME",
                    unique=False,
                )
            ),
            key=(
                key
                or Field(
                    autoincrement=False,
                    default=None,
                    description="",
                    foreign_key=None,
                    index=False,
                    name="key",
                    nullable=True,
                    on_delete="NO ACTION",
                    on_update="NO ACTION",
                    primary_key=False,
                    size=255,
                    type="VARCHAR",
                    unique=False,
                )
            ),
            question_text=(
                answer_text
                or Field(
                    autoincrement=False,
                    default=None,
                    description="",
                    foreign_key=None,
                    index=False,
                    name="question_text",
                    nullable=True,
                    on_delete="NO ACTION",
                    on_update="NO ACTION",
                    primary_key=False,
                    size=255,
                    type="VARCHAR",
                    unique=False,
                )
            ),
            question_type=(
                answer_text
                or Field(
                    autoincrement=False,
                    default=None,
                    description="",
                    foreign_key=None,
                    index=False,
                    name="question_type",
                    nullable=True,
                    on_delete="NO ACTION",
                    on_update="NO ACTION",
                    primary_key=False,
                    size=255,
                    type="VARCHAR",
                    unique=False,
                )
            ),
            updated_at=(
                updated_at
                or Field(
                    autoincrement=False,
                    default=None,
                    description="",
                    foreign_key=None,
                    index=False,
                    name="updated_at",
                    nullable=True,
                    on_delete="NO ACTION",
                    on_update="NO ACTION",
                    primary_key=False,
                    size=None,
                    type="DATETIME",
                    unique=False,
                )
            ),
            uuid=(
                uuid
                or Field(
                    autoincrement=False,
                    default=None,
                    description="",
                    foreign_key=None,
                    index=False,
                    name="uuid",
                    nullable=True,
                    on_delete="NO ACTION",
                    on_update="NO ACTION",
                    primary_key=False,
                    size=255,
                    type="VARCHAR",
                    unique=False,
                )
            ),
        )
