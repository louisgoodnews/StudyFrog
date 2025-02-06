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

    def to_mutable(self) -> "MutableAnswer":
        """
        Returns a new instance of the MutableAnswer class with the same attributes as this instance.

        Returns:
            MutableAnswer: A new instance of the MutableAnswer class with the same attributes as this instance.
        """

        # Create a new instance of the MutableAnswer class with the same attributes as this instance
        return MutableAnswer(**self.to_dict(exclude=["logger"]))


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

    def to_immutable(self) -> "ImmutableAnswer":
        """
        Returns a new instance of the ImmutableAnswer class with the same attributes as this instance.

        Returns:
            ImmutableAnswer: A new instance of the ImmutableAnswer class with the same attributes as this instance.
        """

        # Create a new instance of the ImmutableAnswer class with the same attributes as this instance
        return ImmutableAnswer(**self.to_dict(exclude=["logger"]))


class AnswerConverter:
    """
    A converter class for transforming between AnswerModel and ImmutableAnswer instances.

    This class provides methods to convert a AnswerModel instance to an ImmutableAnswer instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the AnswerConverter class.
    """

    logger: Logger = Logger.get_logger(name="AnswerConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "AnswerModel",
    ) -> Optional[ImmutableAnswer]:
        """
        Converts a given AnswerModel instance to an ImmutableAnswer instance.

        Args:
            model (AnswerModel): The AnswerModel instance to be converted.

        Returns:
            ImmutableAnswer: The converted ImmutableAnswer instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the AnswerModel instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableAnswer class from the dictionary representation of the AnswerModel instance
            return ImmutableAnswer(**model.to_dict(exclude=["logger"])["fields"])
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
        object: ImmutableAnswer,
    ) -> Optional["AnswerModel"]:
        """
        Converts a given ImmutableAnswer instance to a AnswerModel instance.

        Args:
            object (ImmutableAnswer): The ImmutableAnswer instance to be converted.

        Returns:
            AnswerModel: The converted AnswerModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ImmutableAnswer instance.
        """
        try:
            # Attempt to create and return a new instance of the AnswerModel class from the dictionary representation of the ImmutableAnswer instance
            return AnswerModel(**object.to_dict(exclude=["logger"]))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'object_to_model' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


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


class AnswerModel(ImmutableBaseModel):
    def __init__(
        self,
        answer_text: Optional[str] = None,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        is_correct: Optional[bool] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the AnswerModel class.

        Args:
            answer_text (Optional[str]): The text of the answer.
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
            table="answers",
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
            answer_text=(
                answer_text
                or Field(
                    autoincrement=False,
                    default=None,
                    description="",
                    foreign_key=None,
                    index=False,
                    name="answer_text",
                    nullable=True,
                    on_delete="NO ACTION",
                    on_update="NO ACTION",
                    primary_key=False,
                    size=255,
                    type="VARCHAR",
                    unique=False,
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
