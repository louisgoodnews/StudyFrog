"""
Author: lodego
Date: 2025-02-05
"""

import asyncio
import traceback

from datetime import datetime
from typing import *

from utils.builder import BaseObjectBuilder
from utils.constants import Constants
from utils.field import Field
from utils.logger import Logger
from utils.manager import BaseObjectManager
from utils.miscellaneous import Miscellaneous
from utils.model import ImmutableBaseModel
from utils.object import MutableBaseObject, ImmutableBaseObject


__all__: Final[List[str]] = [
    "ImmutableAnswer",
    "MutableAnswer",
    "AnswerConverter",
    "AnswerFactory",
    "AnswerBuilder",
    "AnswerManager",
    "AnswerModel",
    "Answers",
]


class ImmutableAnswer(ImmutableBaseObject):
    """
    An immutable class representing an answer.

    An answer is a piece of text that is associated with a question and is either correct or not.

    Attributes:
        answer_text (str): The text of the answer.
        answer_text_word_count (int): The word count of the answer text.
        created_at (datetime): The timestamp when the answer was created.
        custom_field_values (List[Dict[str, Any]]): A list of custom field values.
        icon (str): The icon of the answer.
        id (int): The ID of the answer.
        key (str): The key of the answer.
        metadata (Optional[Dict[str, Any]]): A dictionary of metadata.
        tags (List[str]): The keys of the tags associated with the answer.
        total_word_count (int): The total word count of the answer.
        updated_at (datetime): The timestamp when the answer was last updated.
        uuid (str): The UUID of the answer.
    """

    def __init__(
        self,
        answer_text: str,
        answer_text_word_count: Optional[int] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        icon: Optional[str] = "💬",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        tags: Optional[List[str]] = None,
        total_word_count: Optional[int] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableAnswer class.

        Args:
            answer_text (str): The text of the answer.
            answer_text_word_count (Optional[int]): The word count of the answer text.
            created_at (Optional[datetime]): The timestamp when the answer was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
            icon (Optional[str]): The icon of the answer. Defaults to "💬".
            id (Optional[int]): The ID of the answer.
            key (Optional[str]): The key of the answer.
            metadata (Optional[Dict[str, Any]]): A dictionary of metadata.
            tags (List[str]): The keys of the tags associated with the answer.
            total_word_count (Optional[int]): The total word count of the answer.
            updated_at (Optional[datetime]): The timestamp when the answer was last updated.
            uuid (Optional[str]): The UUID of the answer.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            answer_text=answer_text,
            answer_text_word_count=answer_text_word_count,
            created_at=created_at,
            custom_field_values=custom_field_values,
            hide_attributes=True,
            icon=icon,
            id=id,
            key=key,
            metadata=metadata,
            tags=tags,
            total_word_count=total_word_count,
            updated_at=updated_at,
            uuid=uuid,
        )

    @property
    def answer_text(self) -> str:
        """
        Gets the text of the answer.

        Returns:
            str: The text of the answer.
        """

        return self._answer_text

    @property
    def answer_text_word_count(self) -> int:
        """
        Gets the word count of the answer text.

        Returns:
            int: The word count of the answer text.
        """

        return self._answer_text_word_count

    @property
    def created_at(self) -> datetime:
        """
        Gets the timestamp when the answer was created.

        Returns:
            datetime: The timestamp when the answer was created.
        """

        return self._created_at

    @property
    def custom_field_values(self) -> List[Dict[str, Any]]:
        """
        Gets the custom field values of the answer.

        Returns:
            List[Dict[str, Any]]: The custom field values of the answer.
        """

        return self._custom_field_values

    @property
    def icon(self) -> str:
        """
        Gets the icon of the answer.

        Returns:
            str: The icon of the answer.
        """

        return self._icon

    @property
    def id(self) -> int:
        """
        Gets the ID of the answer.

        Returns:
            int: The ID of the answer.
        """

        return self._id

    @property
    def key(self) -> str:
        """
        Gets the key of the answer.

        Returns:
            str: The key of the answer.
        """

        return self._key

    @property
    def metadata(self) -> Dict[str, Any]:
        """
        Gets the metadata of the answer.

        Returns:
            Dict[str, Any]: The metadata of the answer.
        """

        return self._metadata

    @property
    def tags(self) -> List[str]:
        """
        Gets the tags of the answer.

        Returns:
            List[str]: The tags associated with the answer.
        """

        return self._tags

    @property
    def total_word_count(self) -> int:
        """
        Gets the total word count of the answer.

        Returns:
            int: The total word count of the answer.
        """

        return self._total_word_count

    @property
    def updated_at(self) -> datetime:
        """
        Gets the timestamp when the answer was last updated.

        Returns:
            datetime: The timestamp when the answer was last updated.
        """

        return self._updated_at

    @property
    def uuid(self) -> str:
        """
        Gets the UUID of the answer.

        Returns:
            str: The UUID of the answer.
        """

        return self._uuid

    def to_mutable(self) -> "MutableAnswer":
        """
        Returns a new instance of the MutableAnswer class with the same attributes as this instance.

        Returns:
            MutableAnswer: A new instance of the MutableAnswer class with the same attributes as this instance.
        """
        try:
            # Create a new instance of the MutableAnswer class with the same attributes as this instance
            return MutableAnswer(
                **self.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_mutable' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class MutableAnswer(MutableBaseObject):
    """
    A mutable class representing an answer.

    Attributes:
        answer_text (str): The text of the answer.
        answer_text_word_count (int): The word count of the answer text.
        created_at (datetime): The timestamp when the answer was created.
        custom_field_values (List[Dict[str, Any]]): A list of custom field values.
        icon (str): The icon of the answer.
        id (int): The ID of the answer.
        key (str): The key of the answer.
        metadata (Optional[Dict[str, Any]]): A dictionary of metadata.
        tags (List[str]): The keys of the tags associated with the answer.
        total_word_count (int): The total word count of the answer.
        updated_at (datetime): The timestamp when the answer was last updated.
        uuid (str): The UUID of the answer.
    """

    def __init__(
        self,
        answer_text: str,
        answer_text_word_count: Optional[int] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        icon: Optional[str] = "💬",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        tags: Optional[List[str]] = None,
        total_word_count: Optional[int] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableAnswer class.

        Args:
            answer_text (str): The text of the answer.
            answer_text_word_count (Optional[int]): The word count of the answer text.
            created_at (Optional[datetime]): The timestamp when the answer was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
            icon (Optional[str]): The icon of the answer. Defaults to "💬".
            id (Optional[int]): The ID of the answer.
            key (Optional[str]): The key of the answer.
            metadata (Optional[Dict[str, Any]]): A dictionary of metadata.
            tags (List[str]): The keys of the tags associated with the answer.
            total_word_count (Optional[int]): The total word count of the answer.
            updated_at (Optional[datetime]): The timestamp when the answer was last updated.
            uuid (Optional[str]): The UUID of the answer.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            answer_text=answer_text,
            answer_text_word_count=answer_text_word_count,
            created_at=created_at,
            custom_field_values=custom_field_values,
            hide_attributes=True,
            icon=icon,
            id=id,
            key=key,
            metadata=metadata,
            tags=tags,
            total_word_count=total_word_count,
            updated_at=updated_at,
            uuid=uuid,
        )

    @property
    def answer_text(self) -> str:
        """
        Gets the text of the answer.

        Returns:
            str: The text of the answer.
        """

        return self._answer_text

    @answer_text.setter
    def answer_text(
        self,
        value: str,
    ) -> None:
        """
        Sets the text of the answer.

        Args:
            value (str): The new text of the answer.

        Returns:
            None
        """

        self._answer_text = value

    @property
    def answer_text_word_count(self) -> int:
        """
        Gets the word count of the answer text.

        Returns:
            int: The word count of the answer text.
        """

        return self._answer_text_word_count

    @answer_text_word_count.setter
    def answer_text_word_count(
        self,
        value: int,
    ) -> None:
        """
        Sets the word count of the answer text.

        Args:
            value (int): The new word count of the answer text.

        Returns:
            None
        """

        self._answer_text_word_count = value

    @property
    def created_at(self) -> datetime:
        """
        Gets the timestamp when the answer was created.

        Returns:
            datetime: The timestamp when the answer was created.
        """

        return self._created_at

    @created_at.setter
    def created_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the timestamp when the answer was created.

        Args:
            value (datetime): The new timestamp when the answer was created.

        Returns:
            None
        """

        self._created_at = value

    @property
    def custom_field_values(self) -> List[Dict[str, Any]]:
        """
        Gets the custom field values of the answer.

        Returns:
            List[Dict[str, Any]]: The custom field values of the answer.
        """

        return self._custom_field_values

    @custom_field_values.setter
    def custom_field_values(
        self,
        value: Union[
            Dict[str, Any],
            List[Dict[str, Any]],
        ],
    ) -> None:
        """
        Sets the custom field values of the answer.

        Args:
            value (Union[Dict[str, Any], List[Dict[str, Any]]]): The new custom field values of the answer.

        Returns:
            None
        """

        # Check, if the 'custom_field_values' attribute exists
        if not self._custom_field_values:
            # Initialize the 'custom_field_values' attribute as an empty list
            self._custom_field_values = []

        # Check, if the passed value is a dictionary
        if isinstance(
            value,
            dict,
        ):
            # Append the passed value to the 'custom_field_values' list attribute
            self._custom_field_values.append(value)
        # Check, if the passed value is a list
        elif isinstance(
            value,
            list,
        ):
            # Update the 'custom_field_values' attribute list with the passed value list
            self._custom_field_values = value

    @property
    def icon(self) -> str:
        """
        Gets the icon of the answer.

        Returns:
            str: The icon of the answer.
        """

        return self._icon

    @property
    def id(self) -> int:
        """
        Gets the ID of the answer.

        Returns:
            int: The ID of the answer.
        """

        return self._id

    @property
    def key(self) -> str:
        """
        Gets the key of the answer.

        Returns:
            str: The key of the answer.
        """

        return self._key

    @property
    def metadata(self) -> Dict[str, Any]:
        """
        Gets the metadata of the answer.

        Returns:
            Dict[str, Any]: The metadata of the answer.
        """

        return self._metadata

    @metadata.setter
    def metadata(
        self,
        **kwargs,
    ) -> None:
        """
        Sets the metadata of the answer.

        Args:
            **kwargs: The keyword arguments representing the metadata key-value pairs.

        Returns:
            None
        """

        # Check, if the 'metadata' attribute exists
        if not self._metadata:
            # Initialize the 'metadata' attribute as an empty dictionary
            self._metadata = {}

        # Update the 'metadata' attribute with the passed keyword arguments
        self._metadata.update(**kwargs)

    @property
    def tags(self) -> List[str]:
        """
        Gets the tags of the answer.

        Returns:
            List[str]: The tags associated with the answer.
        """

        return self._tags

    @tags.setter
    def tags(
        self,
        value: Union[
            List[str],
            str,
        ],
    ) -> None:
        """
        Sets the tags of the answer.

        Args:
            value (Union[List[str], str]): The tags of the answer.

        Returns:
            None
        """

        # Check, if the 'tags' attribute exists
        if not self._tags:
            # Initialize the 'tags' attribute as an empty list
            self._tags = []

        # Check, if the passed value is a list
        if isinstance(
            value,
            list,
        ):
            # Update the 'tags' attribute list with the passed value list
            self._tags = value
        # Check, if the passed value is a string
        if isinstance(
            value,
            str,
        ):
            # Append the passed value to the 'tags' list attribute
            self._tags.append(value)

    @property
    def total_word_count(self) -> int:
        """
        Gets the total word count of the answer.

        Returns:
            int: The total word count of the answer.
        """

        return self._total_word_count

    @total_word_count.setter
    def total_word_count(
        self,
        value: int,
    ) -> None:
        """
        Sets the total word count of the answer.

        Args:
            value (int): The new total word count of the answer.

        Returns:
            None
        """

        self._total_word_count = value

    @property
    def updated_at(self) -> datetime:
        """
        Gets the timestamp when the answer was last updated.

        Returns:
            datetime: The timestamp when the answer was last updated.
        """

        return self._updated_at

    @updated_at.setter
    def updated_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the timestamp when the answer was last updated.

        Args:
            value (datetime): The new timestamp when the answer was last updated.

        Returns:
            None
        """

        self._updated_at = value

    @property
    def uuid(self) -> str:
        """
        Gets the UUID of the answer.

        Returns:
            str: The UUID of the answer.
        """

        return self._uuid

    def to_immutable(self) -> "ImmutableAnswer":
        """
        Returns a new instance of the ImmutableAnswer class with the same attributes as this instance.

        Returns:
            ImmutableAnswer: A new instance of the ImmutableAnswer class with the same attributes as this instance.
        """
        try:
            # Create a new instance of the ImmutableAnswer class with the same attributes as this instance
            return ImmutableAnswer(
                **self.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_immutable' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class AnswerConverter:
    """
    A converter class for transforming between AnswerModel and ImmutableAnswer instances.

    This class provides methods to convert a AnswerModel instance to an ImmutableAnswer instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the AnswerConverter class.
    """

    logger: Final[Logger] = Logger.get_logger(name="AnswerConverter")

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
            return AnswerModel(
                **object.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
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

    logger: Final[Logger] = Logger.get_logger(name="AnswerFactory")

    @classmethod
    def create_answer(
        cls,
        answer_text: str,
        answer_text_word_count: Optional[int] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        icon: Optional[str] = "💬",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        tags: Optional[List[str]] = None,
        total_word_count: Optional[int] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutableAnswer]:
        """
        Creates and returns a new instance of ImmutableAnswer class.

        Args:
            answer_text (str): The text of the answer.
            answer_text_word_count (Optional[int]): The word count of the answer text.
            created_at (Optional[datetime]): The timestamp when the answer was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
            icon (Optional[str]): The icon of the answer. Defaults to "💬".
            id (Optional[int]): The ID of the answer.
            key (Optional[str]): The key of the answer.
            metadata (Optional[Dict[str, Any]]): A dictionary of metadata.
            tags (List[str]): The keys of the tags associated with the answer.
            total_word_count (Optional[int]): The total word count of the answer.
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
                answer_text_word_count=answer_text_word_count,
                created_at=created_at,
                custom_field_values=custom_field_values,
                icon=icon,
                id=id,
                key=key,
                metadata=metadata,
                tags=tags,
                total_word_count=total_word_count,
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


class AnswerBuilder(BaseObjectBuilder):
    """ """

    def __init__(self) -> None:
        """ """

        # Call the parent class constructor
        super().__init__()

    @override
    def build(self) -> Optional[ImmutableAnswer]:
        """
        Builds and returns an instance of ImmutableAnswer class using the configuration dictionary.

        This method attempts to create an instance of the ImmutableAnswer class using the configuration dictionary passed to the constructor.
        If an exception occurs while creating the instance, this method will log an error message and return None.

        Returns:
            Optional[ImmutableAnswer]: The created ImmutableAnswer instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to run 'build' method from '{self.__name__}'.
        """
        try:
            # Attempt to create and return an ImmutableAnswer instance
            return AnswerFactory.create_answer(**self.configuration)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'build' method from '{self.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def answer_text(
        self,
        value: str,
    ) -> Self:
        """
        Sets the answer text for the builder.

        Args:
            value (str): The answer text to set.

        Returns:
            Self: The builder instance with the answer text set.
        """

        # Set the answer text
        self.configuration["answer_text"] = value

        # Set the answer text wordcount
        self.answer_text_word_count(value=len(value.split(" ")))

        # Set the total wordcount
        self.total_word_count(value=len(value.split(" ")))

        # Return the builder instance
        return self

    def answer_text_word_count(
        self,
        value: int,
    ) -> Self:
        """
        Sets the answer text wordcount for the builder.

        Args:
            value (int): The answer text wordcount to set.

        Returns:
            Self: The builder instance with the answer text wordcount set.
        """

        # Set the answer text wordcount
        self.configuration["answer_text_word_count"] = value

        # Return the builder instance
        return self

    def custom_field_values(
        self,
        value: Union[Dict[str, Any], List[Dict[str, Any]]],
    ) -> Self:
        """
        Sets the custom field values for the builder.

        Args:
            value (Union[Dict[str, Any], List[Dict[str, Any]]]): The custom field values to set.

        Returns:
            Self: The builder instance with the custom field values set.
        """

        # Check, if the 'custom_field_values' key exists in the 'configuration' dictionary
        if "custom_field_values" not in self.configuration:
            # Initialize the 'custom_field_values' key with an empty list
            self.configuration["custom_field_values"] = []

        # Check, if the passed value is a dictionary
        if isinstance(
            value,
            dict,
        ):
            # Convert the dictionary to a list of dictionaries
            value = [value]
        # Check, if the passed value is a list
        elif isinstance(
            value,
            list,
        ):
            # Set the custom field values
            self.configuration["custom_field_values"] = value

        # Return the builder instance
        return self

    def metadata(
        self,
        value: Dict[str, Any],
    ) -> Self:
        """
        Sets the metadata of the answer.

        Args:
            value (Dict[str, Any]): The metadata of the answer.

        Returns:
            Self: The builder instance.
        """

        # Check, if the 'metadata' key exists in the 'configuration' dictionary
        if "metadata" not in self.configuration:
            self.configuration["metadata"] = {}

        # Update the 'metadata' dictionary with the new values
        self.configuration["metadata"].update(value)

        # Return the builder instance
        return self

    def tags(
        self,
        value: Union[List[str], str],
    ) -> Self:
        """
        Sets the tags of the answer.

        Args:
            value (Union[List[str], str]): The tags of the answer.

        Returns:
            Self: The builder instance.
        """

        # Check, if the 'tags' key exists in the 'configuration' dictionary
        if "tags" not in self.configuration:
            self.configuration["tags"] = []

        # Check, if the passed value is a list
        if isinstance(
            value,
            list,
        ):
            # Set the tags
            self.configuration["tags"] = value
        # Check, if the passed value is a string
        elif isinstance(
            value,
            str,
        ):
            # Add the tag to the list
            self.configuration["tags"].append(value)

        # Return the builder instance
        return self

    def total_word_count(
        self,
        value: int,
    ) -> Self:
        """
        Sets the total wordcount of the answer.

        Args:
            value (int): The total wordcount of the answer.

        Returns:
            Self: The builder instance.
        """

        # Set the total wordcount
        self.configuration["total_word_count"] = value

        # Return the builder instance
        return self


class AnswerManager(BaseObjectManager):
    """
    A manager class for managing answers in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for answers.

    Attributes:
        cache: (List[Any]): The cache for storing answers.
        logger (Logger): The logger instance associated with the object.
    """

    _shared_instance: Optional["AnswerManager"] = None

    def __new__(cls) -> "AnswerManager":
        """
        Creates and returns a new instance of the AnswerManager class.

        If the instance does not exist, creates a new one by calling the parent class
        constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Returns:
            AnswerManager: The created or existing instance of AnswerManager class.
        """

        # Check if the shared instance does not exist
        if cls._shared_instance is None:
            # Create a new instance by calling the parent class constructor
            cls._shared_instance = super(AnswerManager, cls).__new__(cls)
            # Initialize the instance
            cls._shared_instance.init()

        # Return the shared instance
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes a new instance of the AnswerManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def count_answers(self) -> int:
        """
        Returns the number of answers in the database.

        Returns:
            int: The number of answers in the database.
        """
        try:
            # Count and return the number of answers in the database
            return asyncio.run(AnswerModel.count(database=Constants.DATABASE_PATH))
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
            # Initialize the result (optional) ImmutableAnswer to None
            result: Optional[ImmutableAnswer] = None

            # Check if the answer object is immutable
            if not answer.is_mutable():
                # If it is, convert it to a mutable answer
                answer = answer.to_mutable()

            # Set the created_at timestamp of the answer
            answer.created_at = Miscellaneous.get_current_datetime()

            # Set the custom_field_values of the answer
            answer.custom_field_values = answer.custom_field_values or []

            # Set the key of the answer
            answer.key = f"ANSWER_{self.count_answers() + 1}"

            # Set the metadata of the answer
            answer.metadata = answer.metadata or {}

            # Set the tags of the answer
            answer.tags = answer.tags or []

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

            # Check, if the ID is not None
            if not id:
                # Log a warning message indicating an error has occurred
                self.logger.warning(
                    message=f"It seems that an error has occured while attempting to create a answer ({answer.__repr__()}) in the database."
                )

                # Return early
                return

            kwargs: Dict[str, Any] = answer.to_dict(
                exclude=[
                    "_logger",
                ]
            )

            # Set the ID of the answer
            kwargs["id"] = id

            # Convert the answer to an immutable answer
            result = AnswerFactory.create_answer(**kwargs)

            # Check, if the result is not None
            if not result:
                # Log a warning message indicating an error has occurred
                self.logger.warning(
                    message=f"It seems that there was an error while attempting to create an ImmutableAnswer from the dictionary ({kwargs}) returned by the database. This is likely a serious issue."
                )

                # Return early
                return

            # Add the answer to the cache
            self.add_to_cache(
                key=result.key,
                value=result,
            )

            # Return the newly created immutable answer
            return result
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
                    object=AnswerFactory.create_answer(
                        **answer.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).delete()
            )

            # Remove the answer from the cache
            self.remove_from_cache(key=answer.key)

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
            if self.cache and len(self._cache) == self.count_answers():
                # Return the list of immutable answers from the cache
                return self.get_cache_values()

            # Get all answers from the database
            models: List[AnswerModel] = asyncio.run(
                AnswerModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of AnswerModel objects to a list of ImmutableAnswer objects
            answers: List[ImmutableAnswer] = [
                AnswerFactory.create_answer(
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
                # Add the immutable answer to the cache
                self.add_to_cache(
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
                answer: ImmutableAnswer = AnswerFactory.create_answer(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the answer to the cache
                self.add_to_cache(
                    key=answer.key,
                    value=answer,
                )

                # Return the answer
                return answer
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
                answer: ImmutableAnswer = AnswerFactory.create_answer(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the answer to the cache
                self.add_to_cache(
                    key=answer.key,
                    value=answer,
                )

                # Return the answer
                return answer
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
                return AnswerFactory.create_answer(
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

    def get_default_answers(self) -> Optional[List[ImmutableAnswer]]:
        """
        Retrieves the default answers from the database.

        Returns:
            Optional[List[ImmutableAnswer]]: A list of default answers if no exception occurs. Otherwise, None.

        Raises:
            Exception: If no 'status' defaults are found or any other exception occurs.
        """
        try:
            # Import necessary classes
            from core.default import ImmutableDefault, DefaultManager

            # Initialize an empty list to store the answers
            result: List[ImmutableAnswer] = []

            # Retrieve defaults with the name 'answer'
            defaults: Optional[List[ImmutableDefault]] = [
                DefaultManager().get_default_by(
                    field="name",
                    value=f"answer:{answer}",
                )
                for answer in [
                    Constants.INCORRECT,
                    Constants.CORRECT,
                ]
            ]

            # Raise exception if no defaults are found
            if not defaults:
                raise Exception("Found no 'answer' defaults in the database.")

            # Iterate over each default
            for default in defaults:
                # Check if the answer already exists
                existing_answer: Optional[ImmutableAnswer] = self.get_answer_by(
                    field="answer_text",
                    value=default.value,
                )

                if not existing_answer:
                    # Create a new answer if it doesn't exist
                    answer: ImmutableAnswer = AnswerFactory.create_answer(
                        answer_text=default.value,
                    )

                    # Add the newly created answer to the result
                    result.append(self.create_answer(answer=answer))
                else:
                    # If the answer exists, retrieve it from the database
                    result.append(existing_answer)

            # Return the list of answers
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_default_answers' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_from_answers(
        self,
        condition: Callable[[ImmutableAnswer], bool],
        limit: Optional[int] = None,
    ) -> Optional[List[ImmutableAnswer]]:
        """
        Returns a list of answers from the cache that match the given condition.

        Args:
            condition (Callable[[ImmutableAnswer], bool]): A function that takes an ImmutableAnswer instance and returns a boolean value.
            limit (Optional[int]): The maximum number of answers to return.

        Returns:
            Optional[List[ImmutableAnswer]]: The list of answers that match the given condition if no exception occurs. Otherwise, None.
        """
        try:
            # Initialize an empty list to store matching answers
            result: List[ImmutableAnswer] = []

            # Get all answers from the cache
            answers: List[ImmutableAnswer] = self.get_all_answers()

            # Iterate over the list of immutable answers in the cache
            for answer in answers:
                # Check if the answer matches the given condition
                if condition(answer):
                    # Add the answer that matches the given condition to the result list
                    result.append(answer)

            # Check if the limit is specified and if the result list exceeds the limit
            if limit is not None and len(result) > limit:
                # Return the first 'limit' number of answers
                return result[:limit]

            # Return the list of matching answers
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_from_answers' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def search_answers(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[Union[List[ImmutableAnswer]]]:
        """
        Searches for answers in the database.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            **kwargs: Any additional keyword arguments to be passed to the search method of the AnswerModel class.

        Returns:
            Optional[Union[List[ImmutableAnswer]]]: The found answers if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Search the stack for the passed keyword arguments
                cached_result: Optional[List[ImmutableAnswer]] = self.search_cache(
                    **kwargs
                )

                # Check, if any cached results exist
                if cached_result:
                    # Return the cached results
                    return cached_result

            # Search for answers in the database
            models: Optional[List[AnswerModel]] = asyncio.run(
                AnswerModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found answers if any
            if models is not None and len(models) > 0:
                answers: List[ImmutableAnswer] = [
                    AnswerFactory.create(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                    for model in models
                ]

                # Iterate over the found answers
                for answer in answers:
                    # Add the answer to the cache
                    self.add_to_cache(
                        key=answer.key,
                        value=answer,
                    )

                # Return the found answers
                return answers
            else:
                # Return None indicating that no answers were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
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
            # Check if the answer object is immutable
            if isinstance(
                answer,
                ImmutableAnswer,
            ):
                # If it is, convert it to a mutable answer
                answer = answer.to_mutable()

            # Update the updated_at timestamp of the answer
            answer.updated_at = Miscellaneous.get_current_datetime()

            # Convert the answer to an immutable answer and update the answer in the database
            result: bool = asyncio.run(
                AnswerConverter.object_to_model(
                    object=AnswerFactory.create_answer(
                        **answer.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).update(
                    database=Constants.DATABASE_PATH,
                    **answer.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Check, if the answer was updated successfully
            if result:
                # Update the answer in the cache
                self.update_in_cache(
                    key=answer.key,
                    value=answer,
                )

                # Return the updated answer
                return answer.to_immutable()
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
        answer_text_word_count (Optional[int]): The word count of the answer text.
        created_at (Optional[datetime]): The timestamp when the answer was created.
        custom_field_values (List[Dict[str, Any]]): The custom field values of the answer.
        icon (Optional[str]): The icon of the answer. Defaults to "💬".
        id (Optional[int]): The ID of the answer.
        key (Optional[str]): The key of the answer.
        metadata (Dict[str, Any]): The metadata of the answer.
        table (str): The table name of the answer model.
        tags (List[str]): The keys of the tags associated with the answer.
        total_word_count (Optional[int]): The total word count of the answer.
        updated_at (Optional[datetime]): The timestamp when the answer was last updated.
        uuid (Optional[str]): The UUID of the answer.
    """

    table: Final[str] = Constants.ANSWERS

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

    answer_text_word_count: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="answer_text_word_count",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="INTEGER",
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
        default="💬",
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

    metadata: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="metadata",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
        unique=False,
    )

    tags: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="tags",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
        unique=False,
    )

    total_word_count: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="total_word_count",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="INTEGER",
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
        answer_text: Optional[str] = None,
        answer_text_word_count: Optional[int] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        icon: Optional[str] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        tags: Optional[List[str]] = None,
        total_word_count: Optional[int] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the AnswerModel class.

        Args:
            answer_text (Optional[str]): The text of the answer.
            answer_text_word_count (Optional[int]): The word count of the answer text.
            created_at (Optional[datetime]): The timestamp when the answer was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): The values of the custom fields.
            icon (Optional[str]): The icon of the answer.
            id (Optional[int]): The ID of the answer.
            key (Optional[str]): The key of the answer.
            metadata (Optional[Dict[str, Any]]): The metadata of the answer.
            tags (Optional[List[str]]): The keys of the tags associated with the answer.
            total_word_count (Optional[int]): The total word count of the answer.
            updated_at (Optional[datetime]): The timestamp when the answer was last updated.
            uuid (Optional[str]): The UUID of the answer.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            answer_text=answer_text,
            answer_text_word_count=answer_text_word_count,
            created_at=created_at,
            icon="💬",
            id=id,
            key=key,
            metadata=metadata,
            table=Constants.ANSWERS,
            tags=tags,
            total_word_count=total_word_count,
            updated_at=updated_at,
            uuid=uuid,
        )


class Answers:
    """
    A utility class for managing answers.

    This class provides a set of methods for retrieving and saving answers.
    """

    configuration: Final[Dict[str, Any]] = {}

    # Initialize this class's Logger instance
    logger: Final[Logger] = Logger.get_logger(name="Answers")

    # Initialize this class's AnswerManager instance
    manager: Final[AnswerManager] = AnswerManager()

    @classmethod
    def build(
        cls,
        as_mutable: bool = False,
    ) -> Optional[
        Union[
            ImmutableAnswer,
            MutableAnswer,
        ]
    ]:
        """
        Builds an answer and returns it.

        Args:
            as_mutable (bool, optional): Whether to build the answer as mutable. Defaults to False.

        Returns:
            Optional[Union[ImmutableAnswer, MutableAnswer,]]: The answer if no exception occurs. Otherwise, None.
        """
        try:
            # Check, if the configuration dictionary is empty
            if not cls.configuration:
                # Log a warning message
                cls.logger.warning(
                    message="Configuration dictionary is empty. Use this class' 'set' method to set the configuration dictionary."
                )

                # Return early
                return None

            # Initialize the builder
            builder: AnswerBuilder = AnswerBuilder()

            # Update the builder's configuration
            builder.kwargs(**cls.configuration)

            # Build the answer
            answer: Union[ImmutableAnswer, MutableAnswer] = builder.build(
                as_mutable=as_mutable
            )

            # Clear the configuration
            cls.configuration.clear()

            # Return the answer
            return answer
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'build' method from '{cls.__name__}': {e}"
            )

            # Log the traceback of the exception
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def clear(cls) -> None:
        """
        Clears the configuration dictionary.

        Args:
            None

        Returns:
            None
        """

        # Clear the configuration dictionary
        cls.configuration.clear()

    @classmethod
    def configure(
        cls,
        **kwargs,
    ) -> None:
        """
        Configures the configuration dictionary.

        Args:
            **kwargs: Additional keyword arguments to pass to the configure method.

        Returns:
            None
        """

        # Update the configuration dictionary
        cls.configuration.update(kwargs)

    @classmethod
    def create(
        cls,
        **kwargs,
    ) -> Optional[ImmutableAnswer]:
        """
        Creates a new answer and returns it.

        Args:
            **kwargs: Additional keyword arguments to pass to the create_answer method.

        Returns:
            Optional[ImmutableAnswer]: The answer if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            return AnswerFactory.create_answer(**kwargs)
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create' method from '{cls.__name__}': {e}"
            )

            # Log the traceback of the exception
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def create_default(
        cls,
        answer_text: str,
        as_mutable: bool = False,
    ) -> Optional[ImmutableAnswer]:
        """
        Creates a new answer and returns it.

        Args:
            as_mutable (bool, optional): Whether to create the answer as mutable. Defaults to False.
            answer_text (str): The text of the answer.

        Returns:
            Optional[ImmutableAnswer]: The answer if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            return AnswerFactory.create_default_answer(
                as_mutable=as_mutable,
                answer_text=answer_text,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_default' method from '{cls.__name__}': {e}"
            )

            # Log the traceback of the exception
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def get(
        cls,
        id: Optional[int] = None,
        key: Optional[str] = None,
        **kwargs,
    ) -> Optional[ImmutableAnswer]:
        """
        Retrieves an answer by the given ID, key, or other fields.

        Args:
            id (Optional[int]): The ID of the answer.
            key (Optional[str]): The key of the answer.
            **kwargs: Additional keyword arguments to pass to the get_answer_by method.

        Returns:
            Optional[ImmutableAnswer]: The answer with the given ID, key, or other fields if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            if id:
                return cls.manager.get_answer_by_id(
                    force_refetch=True,
                    id=id,
                )
            elif key:
                return cls.manager.get_answer_by_key(
                    force_refetch=True,
                    key=key,
                )
            else:
                return cls.manager.get_answer_by(
                    force_refetch=True,
                    **kwargs,
                )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get' method from '{cls.__name__}': {e}"
            )

            # Log the traceback of the exception
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def get_all(cls) -> Optional[List[ImmutableAnswer]]:
        """
        Returns a list of all answers in the database.

        Returns:
            Optional[List[ImmutableAnswer]]: The answers if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            return cls.manager.get_all_answers(force_refetch=True)
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{cls.__name__}': {e}"
            )

            # Log the traceback of the exception
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def save(
        cls,
        answer: Union[
            ImmutableAnswer,
            MutableAnswer,
        ],
    ) -> ImmutableAnswer:
        """
        Saves the passed answer to the database and returns it.

        Args:
            answer (Union[ImmutableAnswer, MutableAnswer]): The answer to save.

        Returns:
            ImmutableAnswer: The saved answer if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            return cls.manager.create_answer(answer=answer)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'save' method from '{cls.__name__}': {e}"
            )

            # Log the traceback of the exception
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def search(
        cls,
        **kwargs,
    ) -> Optional[List[ImmutableAnswer]]:
        """
        Searches for answers in the database and returns them.

        Args:
            **kwargs: Additional keyword arguments to pass to the search_answers method.

        Returns:
            Optional[List[ImmutableAnswer]]: The answers if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            return cls.manager.search_answers(
                force_refetch=True,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{cls.__name__}': {e}"
            )

            # Log the traceback of the exception
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    @classmethod
    def set(
        cls,
        key: str,
        value: Optional[Any] = None,
    ) -> None:
        """
        Sets a configuration value.

        Args:
            key (str): The key of the configuration value.
            value (Optional[Any]): The value of the configuration value.

        Returns:
            None
        """

        # Check, if the key is already contained within the configuration dictionary
        if key in cls.configuration:
            # Log a warning message indicating that the key is already contained within the configuration dictionary
            cls.logger.warning(
                message=f"Key '{key}' is already contained within the configuration dictionary. Overwriting..."
            )

        # Set the configuration value corresponding to the passed key
        cls.configuration[key] = value
