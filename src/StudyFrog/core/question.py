"""
Author: lodego
Date: 2025-02-05
"""

import asyncio

from datetime import datetime

from typing import *

from utils.constants import Constants
from utils.field import Field
from utils.logger import Logger
from utils.manager import BaseObjectManager
from utils.miscellaneous import Miscellaneous
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
        answers (Optional[List[str]]): The answers to the question.
        correct_answers (Optional[List[str]]): The correct answers to the question.
        created_at (datetime): The timestamp when the question was created.
        custom_field_values (Optional[List[Dict[str, Any]]]): The values of the custom fields.
        icon (Optional[str]): The icon of the question.
        id (int): The ID of the question.
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
        answers: Optional[List[str]] = None,
        correct_answers: Optional[List[str]] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        icon: Optional[str] = "❓",
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableQuestion class.

        Args:
            question_text (str): The text of the question.
            question_type (Literal["MULTIPLE_CHOICE", "TRUE_FALSE", "FILL_IN_THE_BLANKS"]): The type of the question.
            answers (Optional[List[str]]): The answers to the question.
            correct_answers (Optional[List[str]]): The correct answers to the question.
            created_at (Optional[datetime]): The timestamp when the question was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): The values of the custom fields.
            icon (Optional[str]): The icon of the question. Defaults to "❓".
            id (Optional[int]): The ID of the question.
            key (Optional[str]): The key of the question.
            updated_at (Optional[datetime]): The timestamp when the question was last updated.
            uuid (Optional[str]): The UUID of the question.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            answers=answers,
            correct_answers=correct_answers,
            created_at=created_at,
            custom_field_values=custom_field_values,
            icon=icon,
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
        return MutableQuestion(**self.to_dict(exclude=["_logger"]))


class MutableQuestion(MutableBaseObject):
    """
    A mutable class representing a question.

    Attributes:
        answers (Optional[List[str]]): The answers to the question.
        correct_answers (Optional[List[str]]): The correct answers to the question.
        created_at (Optional[datetime]): The timestamp when the question was created.
        custom_field_values (Optional[List[Dict[str, Any]]]): The values of the custom fields.
        icon (Optional[str]): The icon of the question.
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
        answers: Optional[List[str]] = None,
        correct_answers: Optional[List[str]] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        icon: Optional[str] = "❓",
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
            answers (Optional[List[str]]): The answers to the question.
            correct_answers (Optional[List[str]]): The correct answers to the question.
            created_at (Optional[datetime]): The timestamp when the question was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): The values of the custom fields.
            icon (Optional[str]): The icon of the question. Defaults to "❓".
            id (Optional[int]): The ID of the question.
            key (Optional[str]): The key of the question.
            updated_at (Optional[datetime]): The timestamp when the question was last updated.
            uuid (Optional[str]): The UUID of the question.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            answers=answers,
            correct_answers=correct_answers,
            created_at=created_at,
            custom_field_values=custom_field_values,
            icon=icon,
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
        return ImmutableQuestion(**self.to_dict(exclude=["_logger"]))


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
            return ImmutableQuestion(
                **model.to_dict(
                    exclude=[
                        "_logger",
                        "table",
                    ]
                )
            )
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
            return QuestionModel(**object.to_dict(exclude=["_logger"]))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'object_to_model' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class QuestionFactory:
    """
    A factory class for creating question objects.

    Attributes:
        logger (Logger): The logger instance associated with the QuestionFactory class.
    """

    logger: Logger = Logger.get_logger(name="QuestionFactory")

    @classmethod
    def create_question(
        cls,
        question_text: str,
        question_type: Literal["MULTIPLE_CHOICE", "TRUE_FALSE", "FILL_IN_THE_BLANKS"],
        answers: Optional[List[str]] = None,
        correct_answers: Optional[List[str]] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        icon: Optional[str] = "❓",
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
            answers (Optional[List[str]]): The answers to the question.
            correct_answers (Optional[List[str]]): The correct answers to the question.
            created_at (Optional[datetime]): The timestamp when the question was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): The values of the custom fields.
            icon (Optional[str]): The icon of the question. Defaults to "❓".
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
                answers=answers,
                correct_answers=correct_answers,
                created_at=created_at,
                custom_field_values=custom_field_values,
                icon=icon,
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
    """
    A manager class for managing questions in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for questions.

    Attributes:
        cache: (List[Any]): The cache for storing questions.
        logger (Logger): The logger instance associated with the object.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the QuestionManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def count_questions(self) -> int:
        """
        Returns the number of questions in the database.

        Returns:
            int: The number of questions in the database.
        """
        try:
            # Count the number of questions in the database
            result: Any = asyncio.run(
                QuestionModel.execute(
                    database=Constants.DATABASE_PATH,
                    sql=f"SELECT COUNT(*) FROM {Constants.QUESTIONS};",
                )
            )

            # Return the number of questions in the database
            return result[0][0] if result else 0
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_question(
        self,
        question: Union[ImmutableQuestion, MutableQuestion],
    ) -> Optional[ImmutableQuestion]:
        """
        Creates a new question in the database.

        Args:
            question (Union[ImmutableQuestion, MutableQuestion]): The question to be created.

        Returns:
            Optional[ImmutableQuestion]: The newly created immutable question if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the question.
        """
        try:
            # Check if the question object is immutable
            if isinstance(
                question,
                ImmutableQuestion,
            ):
                # If it is, convert it to a mutable question
                question = MutableQuestion(**question.to_dict(exclude=["_logger"]))

            # Set the created_at timestamp of the question
            question.created_at = Miscellaneous.get_current_datetime()

            # Set the custom_field_values of the question
            question.custom_field_values = [] or question.custom_field_values

            # Set the key of the question
            question.key = f"QUESTION_{self.count_questions() + 1}"

            # Set the updated_at timestamp of the question
            question.updated_at = Miscellaneous.get_current_datetime()

            # Set the uuid of the question
            question.uuid = Miscellaneous.get_uuid()

            # Convert the question object to a QuestionModel object
            model: QuestionModel = QuestionConverter.object_to_model(object=question)

            # Create a new question in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            if id:
                # Set the ID of the question
                question.id = id

                # Convert the question to an immutable question
                question = ImmutableQuestion(**question.to_dict(exclude=["_logger"]))

                # Add the question to the cache
                self.add_to_cache(
                    key=question.key,
                    value=question,
                )

                # Return the newly created immutable question
                return question

            # Log a warning message indicating an error has occurred
            self.logger.warning(
                message=f"It seems that an error has occured while attempting to create a question ({question}) in the database."
            )

            # Return None indicating an error has occurred
            return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_question' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete_question(
        self,
        question: Union[ImmutableQuestion, MutableQuestion],
    ) -> bool:
        """
        Deletes a question from the database.

        Args:
            question (Union[ImmutableQuestion, MutableQuestion]): The question to be deleted.

        Returns:
            bool: True if the question was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the question to an immutable question and delete the question from the database
            result: bool = asyncio.run(
                QuestionConverter.object_to_model(
                    object=ImmutableQuestion(**question.to_dict(exclude=["_logger"]))
                ).delete()
            )

            # Return True if the question was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all_questions(self) -> Optional[List[ImmutableQuestion]]:
        """
        Returns a list of all questions in the database.

        Returns:
            Optional[List[ImmutableQuestion]]: A list of all questions in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if cache and table size are equal
            if self.cache and len(self._cache) == self.count_questions():
                # Return the list of immutable questions from the cache
                return self.get_cache_values()

            # Get all questions from the database
            models: List[QuestionModel] = asyncio.run(
                QuestionModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of QuestionModel objects to a list of ImmutableQuestion objects
            questions: List[ImmutableQuestion] = [
                ImmutableQuestion(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable questions
            for question in questions:
                if not self.is_key_in_cache(key=question.key):
                    # Add the immutable question to the cache
                    self.add_to_cache(
                        key=question.key,
                        value=question,
                    )
                else:
                    # Update the immutable question in the cache
                    self.update_in_cache(
                        key=question.key,
                        value=question,
                    )

            # Return the list of immutable questions
            return questions
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_question_by(
        self,
        field: str,
        value: Any,
    ) -> Optional[ImmutableQuestion]:
        """
        Retrieves a question by the given field and value.

        Args:
            field (str): The field to search by.
            value (Any): The value to search for.

        Returns:
            Optional[ImmutableQuestion]: The question with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the question is already in the cache
            if self.is_key_in_cache(key=field):
                # Return the question from the cache
                return self.get_value_from_cache(key=field)

            # Get the question with the given field and value from the database
            model: Optional[QuestionModel] = asyncio.run(
                QuestionModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Return the question if it exists
            if model is not None:
                # Convert the QuestionModel object to an ImmutableQuestion object
                return ImmutableQuestion(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the question does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_question_by_id(
        self,
        id: int,
    ) -> Optional[ImmutableQuestion]:
        """
        Returns a question with the given ID.

        Args:
            id (int): The ID of the question.

        Returns:
            Optional[ImmutableQuestion]: The question with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the question is already in the cache
            if self.is_key_in_cache(key=f"QUESTION_{id}"):
                # Return the question from the cache
                return self.get_value_from_cache(key=f"QUESTION_{id}")

            # Get the question with the given ID from the database
            model: Optional[QuestionModel] = asyncio.run(
                QuestionModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the question if it exists
            if model is not None:
                # Convert the QuestionModel object to an ImmutableQuestion object
                return ImmutableQuestion(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the question does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_question_by_uuid(
        self,
        uuid: str,
    ) -> Optional[ImmutableQuestion]:
        """
        Returns a question with the given UUID.

        Args:
            uuid (str): The UUID of the question.

        Returns:
            Optional[ImmutableQuestion]: The question with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the question is already in the cache
            if self.is_key_in_cache(key=uuid):
                # Return the question from the cache
                return self.get_value_from_cache(key=uuid)

            # Get the question with the given UUID from the database
            model: Optional[QuestionModel] = asyncio.run(
                QuestionModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the question if it exists
            if model is not None:
                # Convert the QuestionModel object to an ImmutableQuestion object
                return ImmutableQuestion(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the question does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def search_questions(
        self,
        **kwargs,
    ) -> Optional[Union[List[ImmutableQuestion]]]:
        """
        Searches for questions in the database.

        Args:
            **kwargs: Any additional keyword arguments to be passed to the search method of the QuestionModel class.

        Returns:
            Optional[Union[List[ImmutableQuestion]]]: The found questions if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Search for questions in the database
            models: Optional[List[QuestionModel]] = asyncio.run(
                QuestionModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found questions if any
            if models is not None and len(models) > 0:
                return [
                    ImmutableQuestion(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                    for model in models
                ]
            else:
                # Return None indicating that no questions were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_question(
        self,
        question: Union[ImmutableQuestion, MutableQuestion],
    ) -> Optional[ImmutableQuestion]:
        """
        Updates a question with the given ID.

        Args:
            question (Union[ImmutableQuestion, MutableQuestion]): The question to update.

        Returns:
            Optional[ImmutableQuestion]: The updated question if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the question to an immutable question and update the question in the database
            model: Optional[QuestionModel] = asyncio.run(
                QuestionConverter.object_to_model(
                    object=ImmutableQuestion(**question.to_dict(exclude=["_logger"]))
                ).update(
                    database=Constants.DATABASE_PATH,
                    **question.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Return the updated question if it exists
            if model is not None:
                # Convert the QuestionModel object to an ImmutableQuestion object
                question = ImmutableQuestion(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the question to the cache
                self.update_in_cache(
                    key=question.key,
                    value=question,
                )

                # Return the updated question
                return question
            else:
                # Return None indicating that the question does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class QuestionModel(ImmutableBaseModel):
    """
    Represents the structure of a question model.

    Attributes:
        id (Field): The ID field of the question.
        answers (Field): The answers of the question.
        correct_answers (Field): The correct answers of the question.
        created_at (Field): The timestamp when the question was created.
        icon (Field): The icon of the question. Defaults to "❓".
        key (Field): The key of the question.
        question_text (Field): The text of the question.
        question_type (Field): The type of the question.
        table (str): The table name of the question model.
        updated_at (Field): The timestamp when the question was last updated.
        uuid (Field): The UUID of the question.
    """

    table: str = Constants.QUESTIONS

    id: Field = Field(
        autoincrement=True,
        default=None,
        description="",
        foreign_key=None,
        index=True,
        name="id",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=True,
        size=None,
        type="INTEGER",
        unique=False,
    )

    answers: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="answers",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
        unique=False,
    )

    correct_answers: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="correct_answers",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
        unique=False,
    )

    created_at: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="created_at",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="DATETIME",
        unique=False,
    )

    custom_field_values: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="custom_field_values",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
        unique=False,
    )

    icon: Field = Field(
        autoincrement=False,
        default="❓",
        description="",
        foreign_key=None,
        index=False,
        name="icon",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=False,
    )

    key: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="key",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=True,
    )

    question_text: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="question_text",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="TEXT",
        unique=False,
    )

    question_type: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="question_type",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=False,
    )

    updated_at: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="updated_at",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="DATETIME",
        unique=False,
    )

    uuid: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="uuid",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=True,
    )

    def __init__(
        self,
        answers: Optional[List[str]] = None,
        correct_answers: Optional[List[str]] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[Dict[str, Any]] = None,
        icon: Optional[str] = "❓",
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
        Initializes a new instance of the MutableQuestion class.

        Args:
            answers (Optional[List[str]]): The answers to the question.
            correct_answers (Optional[List[str]]): The correct answers to the question.
            created_at (Optional[datetime]): The timestamp when the question was created.
            custom_field_values (Optional[Dict[str, Any]]): The values of the custom fields.
            icon (Optional[str]): The icon of the question. Defaults to "❓".
            id (Optional[int]): The ID of the question.
            key (Optional[str]): The key of the question.
            question_text (Optional[str]): The text of the question.
            question_type (Optional[Literal["MULTIPLE_CHOICE", "TRUE_FALSE", "FILL_IN_THE_BLANKS"]]): The type of the question.
            updated_at (Optional[datetime]): The timestamp when the question was last updated.
            uuid (Optional[str]): The UUID of the question.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            answers=answers,
            correct_answers=correct_answers,
            created_at=created_at,
            custom_field_values=custom_field_values,
            icon="❓",
            id=id,
            key=key,
            question_text=question_text,
            question_type=question_type,
            table=Constants.QUESTIONS,
            updated_at=updated_at,
            uuid=uuid,
        )
