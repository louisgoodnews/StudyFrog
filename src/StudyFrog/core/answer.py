"""
Author: lodego
Date: 2025-02-05
"""

import asyncio

import uuid

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
        custom_field_values (List[Dict[str, Any]]): A list of custom field values.
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
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
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
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
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
            custom_field_values=custom_field_values,
            id=id,
            is_correct=is_correct,
            key=key,
            updated_at=updated_at,
            uuid=uuid,
        )

    def to_mutable(self) -> "MutableAnswer":
        """
        Returns a new instance of the MutableAnswer class with the same attributes as this instance.

        Returns:
            MutableAnswer: A new instance of the MutableAnswer class with the same attributes as this instance.
        """

        # Create a new instance of the MutableAnswer class with the same attributes as this instance
        return MutableAnswer(**self.to_dict(exclude=["_logger"]))


class MutableAnswer(MutableBaseObject):
    """
    A mutable class representing an answer.

    Attributes:
        answer_text (str): The text of the answer.
        created_at (datetime): The timestamp when the answer was created.
        custom_field_values (List[Dict[str, Any]]): A list of custom field values.
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
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
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
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
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
            custom_field_values=custom_field_values,
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
        return ImmutableAnswer(**self.to_dict(exclude=["_logger"]))


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
            return ImmutableAnswer(
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
            return AnswerModel(**object.to_dict(exclude=["_logger"]))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'object_to_model' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class AnswerFactory:
    """
    A factory class for creating ImmutableAnswer instances.

    Attributes:
        logger (Logger): The logger instance associated with the AnswerFactory class.
    """

    logger: Logger = Logger.get_logger(name="AnswerFactory")

    @classmethod
    def create_answer(
        cls,
        answer_text: str,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
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
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
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
                custom_field_values=custom_field_values,
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
    """
    A manager class for managing answers in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for answers.

    Attributes:
        cache: (List[Any]): The cache for storing answers.
        logger (Logger): The logger instance associated with the object.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the AnswerManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def count(self) -> int:
        """
        Returns the number of answers in the database.

        Returns:
            int: The number of answers in the database.
        """
        try:
            # Count the number of answers in the database
            result: Any = asyncio.run(
                AnswerModel.execute(
                    database=Constants.DATABASE_PATH,
                    sql=f"SELECT COUNT(*) FROM {Constants.ANSWERS};",
                )
            )

            # Return the number of answers in the database
            return result[0][0] if result else 0
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_answer(
        self,
        answer: Union[ImmutableAnswer, MutableAnswer],
    ) -> Optional[ImmutableAnswer]:
        """
        Creates a new answer in the database.

        Args:
            answer (Union[ImmutableAnswer, MutableAnswer]): The answer to be created.

        Returns:
            Optional[ImmutableAnswer]: The newly created immutable answer if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the answer.
        """
        try:
            # Check if the answer object is immutable
            if isinstance(
                answer,
                ImmutableAnswer,
            ):
                # If it is, convert it to a mutable answer
                answer = MutableAnswer(**answer.to_dict(exclude=["_logger"]))

            # Set the created_at timestamp of the answer
            answer.created_at = Miscellaneous.get_current_datetime()

            # Set the custom_field_values of the answer
            answer.custom_field_values = [] or answer.custom_field_values

            # Set the key of the answer
            answer.key = f"ANSWER_{self.count_answers() + 1}"

            # Set the updated_at timestamp of the answer
            answer.updated_at = Miscellaneous.get_current_datetime()

            # Set the uuid of the answer
            answer.uuid = Miscellaneous.get_uuid()

            # Convert the answer object to a AnswerModel object
            model: AnswerModel = AnswerConverter.object_to_model(object=answer)

            # Create a new answer in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            if id:
                # Set the ID of the answer
                answer.id = id

                # Convert the answer to an immutable answer
                answer = ImmutableAnswer(**answer.to_dict(exclude=["_logger"]))

                # Add the answer to the cache
                self.add_to_cache(
                    key=answer.key,
                    value=answer,
                )

                # Return the newly created immutable answer
                return answer

            # Log a warning message indicating an error has occurred
            self.logger.warning(
                message=f"It seems that an error has occured while attempting to create a answer ({answer}) in the database."
            )

            # Return None indicating an error has occurred
            return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_answer' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete_answer(
        self,
        answer: Union[ImmutableAnswer, MutableAnswer],
    ) -> bool:
        """
        Deletes a answer from the database.

        Args:
            answer (Union[ImmutableAnswer, MutableAnswer]): The answer to be deleted.

        Returns:
            bool: True if the answer was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the answer to an immutable answer and delete the answer from the database
            result: bool = asyncio.run(
                AnswerConverter.object_to_model(
                    object=ImmutableAnswer(**answer.to_dict(exclude=["_logger"]))
                ).delete()
            )

            # Return True if the answer was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all_answers(self) -> Optional[List[ImmutableAnswer]]:
        """
        Returns a list of all answers in the database.

        Returns:
            Optional[List[ImmutableAnswer]]: A list of all answers in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if cache and table size are equal
            if self.cache and len(self._cache) == self.count():
                # Return the list of immutable answers from the cache
                return self.get_cache_values()

            # Get all answers from the database
            models: List[AnswerModel] = asyncio.run(
                AnswerModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of AnswerModel objects to a list of ImmutableAnswer objects
            answers: List[ImmutableAnswer] = [
                ImmutableAnswer(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable answers
            for answer in answers:
                if not self.is_key_in_cache(key=answer.key):
                    # Add the immutable answer to the cache
                    self.add_to_cache(
                        key=answer.key,
                        value=answer,
                    )
                else:
                    # Update the immutable answer in the cache
                    self.update_in_cache(
                        key=answer.key,
                        value=answer,
                    )

            # Return the list of immutable answers
            return answers
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_answer_by(
        self,
        field: str,
        value: Any,
    ) -> Optional[ImmutableAnswer]:
        """
        Retrieves a answer by the given field and value.

        Args:
            field (str): The field to search by.
            value (Any): The value to search for.

        Returns:
            Optional[ImmutableAnswer]: The answer with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the answer is already in the cache
            if self.is_key_in_cache(key=field):
                # Return the answer from the cache
                return self.get_value_from_cache(key=field)

            # Get the answer with the given field and value from the database
            model: Optional[AnswerModel] = asyncio.run(
                AnswerModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Return the answer if it exists
            if model is not None:
                # Convert the AnswerModel object to an ImmutableAnswer object
                return ImmutableAnswer(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the answer does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_answer_by_id(
        self,
        id: int,
    ) -> Optional[ImmutableAnswer]:
        """
        Returns a answer with the given ID.

        Args:
            id (int): The ID of the answer.

        Returns:
            Optional[ImmutableAnswer]: The answer with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the answer is already in the cache
            if self.is_key_in_cache(key=f"ANSWER_{id}"):
                # Return the answer from the cache
                return self.get_value_from_cache(key=f"ANSWER_{id}")

            # Get the answer with the given ID from the database
            model: Optional[AnswerModel] = asyncio.run(
                AnswerModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the answer if it exists
            if model is not None:
                # Convert the AnswerModel object to an ImmutableAnswer object
                return ImmutableAnswer(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the answer does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_answer_by_uuid(
        self,
        uuid: str,
    ) -> Optional[ImmutableAnswer]:
        """
        Returns a answer with the given UUID.

        Args:
            uuid (str): The UUID of the answer.

        Returns:
            Optional[ImmutableAnswer]: The answer with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the answer is already in the cache
            if self.is_key_in_cache(key=uuid):
                # Return the answer from the cache
                return self.get_value_from_cache(key=uuid)

            # Get the answer with the given UUID from the database
            model: Optional[AnswerModel] = asyncio.run(
                AnswerModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the answer if it exists
            if model is not None:
                # Convert the AnswerModel object to an ImmutableAnswer object
                return ImmutableAnswer(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the answer does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_answer(
        self,
        answer: Union[ImmutableAnswer, MutableAnswer],
    ) -> Optional[ImmutableAnswer]:
        """
        Updates a answer with the given ID.

        Args:
            answer (Union[ImmutableAnswer, MutableAnswer]): The answer to update.

        Returns:
            Optional[ImmutableAnswer]: The updated answer if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the answer to an immutable answer and update the answer in the database
            model: Optional[AnswerModel] = asyncio.run(
                AnswerConverter.object_to_model(
                    object=ImmutableAnswer(**answer.to_dict(exclude=["_logger"]))
                ).update(
                    **answer.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    )
                )
            )

            # Return the updated answer if it exists
            if model is not None:
                # Convert the AnswerModel object to an ImmutableAnswer object
                answer = ImmutableAnswer(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the answer to the cache
                self.update_in_cache(
                    key=answer.key,
                    value=answer,
                )

                # Return the updated answer
                return answer
            else:
                # Return None indicating that the answer does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class AnswerModel(ImmutableBaseModel):
    """
    Represents the structure of an answer model.

    Attributes:
        answer_text (Optional[str]): The text of the answer.
        created_at (Optional[datetime]): The timestamp when the answer was created.
        id (Optional[int]): The ID of the answer.
        is_correct (Optional[bool]): Whether the answer is correct or not.
        key (Optional[str]): The key of the answer.
        table (str): The table name of the answer model.
        updated_at (Optional[datetime]): The timestamp when the answer was last updated.
        uuid (Optional[str]): The UUID of the answer.
    """

    table: str = Constants.ANSWERS

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

    answer_text: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="answer_text",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=True,
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
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
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
        answer_text: Optional[str] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
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
            custom_field_values (Optional[List[Dict[str, Any]]]): The values of the custom fields.
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
            table=Constants.ANSWERS,
            updated_at=updated_at,
            uuid=uuid,
        )
