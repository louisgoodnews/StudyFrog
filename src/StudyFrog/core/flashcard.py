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
    "ImmutableFlashcard",
    "MutableFlashcard",
    "FlashcardConverter",
    "FlashcardFactory",
    "FlashcardManager",
    "FlashcardModel",
]


class ImmutableFlashcard(ImmutableBaseObject):
    """
    An immutable class representing a flashcard.

    A flashcard is a learning tool used to aid memorization by providing a question on one side and the answer on the other.

    Attributes:
        back_text (str): The back side of the flashcard.
        created_at (datetime): The timestamp when the flashcard was created.
        front_text (str): The front side of the flashcard.
        id (int): The ID of the flashcard.
        key (str): The key of the flashcard.
        updated_at (datetime): The timestamp when the flashcard was last updated.
        uuid (str): The UUID of the flashcard.
    """

    def __init__(
        self,
        back_text: str,
        front_text: str,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableFlashcard class.

        Args:
            back_text (str): The back side of the flashcard.
            created_at (datetime): The timestamp when the flashcard was created.
            front_text (str): The front side of the flashcard.
            id (int): The ID of the flashcard.
            key (str): The key of the flashcard.
            updated_at (datetime): The timestamp when the flashcard was last updated.
            uuid (str): The UUID of the flashcard.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            back_text=back_text,
            created_at=created_at,
            front_text=front_text,
            id=id,
            key=key,
            updated_at=updated_at,
            uuid=uuid,
        )

    def to_mutable(self) -> "MutableFlashcard":
        """
        Returns a mutable copy of the ImmutableFlashcard instance.

        Returns:
            MutableFlashcard: A mutable copy of the ImmutableFlashcard instance.
        """

        # Create a new MutableFlashcard instance from the dictionary representation of the ImmutableFlashcard instance
        return MutableFlashcard(**self.to_dict())


class MutableFlashcard(MutableBaseObject):
    """
    An immutable class representing a flashcard.

    A flashcard is a learning tool used to aid memorization by providing a question on one side and the answer on the other.

    Attributes:
        back_text (str): The back side of the flashcard.
        created_at (datetime): The timestamp when the flashcard was created.
        front_text (str): The front side of the flashcard.
        id (int): The ID of the flashcard.
        key (str): The key of the flashcard.
        updated_at (datetime): The timestamp when the flashcard was last updated.
        uuid (str): The UUID of the flashcard.
    """

    def __init__(
        self,
        back_text: str,
        front_text: str,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableFlashcard class.

        Args:
            back_text (str): The back side of the flashcard.
            created_at (datetime): The timestamp when the flashcard was created.
            front_text (str): The front side of the flashcard.
            id (int): The ID of the flashcard.
            key (str): The key of the flashcard.
            updated_at (datetime): The timestamp when the flashcard was last updated.
            uuid (str): The UUID of the flashcard.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            back_text=back_text,
            created_at=created_at,
            front_text=front_text,
            id=id,
            key=key,
            updated_at=updated_at,
            uuid=uuid,
        )

    def to_immutable(self) -> ImmutableFlashcard:
        """
        Returns an immutable copy of the MutableFlashcard instance.

        Returns:
            ImmutableFlashcard: An immutable copy of the MutableFlashcard instance.
        """

        # Create a new ImmutableFlashcard instance from the dictionary representation of the MutableFlashcard instance
        return ImmutableFlashcard(**self.to_dict())


class FlashcardConverter:
    """
    A converter class for transforming between FlashcardModel and ImmutableFlashcard instances.

    This class provides methods to convert a FlashcardModel instance to an ImmutableFlashcard instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the FlashcardConverter class.
    """

    logger: Logger = Logger.get_logger(name="FlashcardConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "FlashcardModel",
    ) -> Optional[ImmutableFlashcard]:
        """
        Converts a given FlashcardModel instance to an ImmutableFlashcard instance.

        Args:
            model (FlashcardModel): The FlashcardModel instance to be converted.

        Returns:
            ImmutableFlashcard: The converted ImmutableFlashcard instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the FlashcardModel instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableFlashcard class from the dictionary representation of the FlashcardModel instance
            return ImmutableFlashcard(**model.to_dict(exclude=["_logger"]))
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
        object: ImmutableFlashcard,
    ) -> Optional["FlashcardModel"]:
        """
        Converts a given ImmutableFlashcard instance to a FlashcardModel instance.

        Args:
            object (ImmutableFlashcard): The ImmutableFlashcard instance to be converted.

        Returns:
            FlashcardModel: The converted FlashcardModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ImmutableFlashcard instance.
        """
        try:
            # Attempt to create and return a new instance of the FlashcardModel class from the dictionary representation of the ImmutableFlashcard instance
            return FlashcardModel(**object.to_dict(exclude=["_logger"]))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'object_to_model' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class FlashcardFactory:
    """
    A factory class used to create instances of ImmutableFlashcard class.

    Attributes:
        logger (Logger): The logger instance associated with the object.
    """

    logger: Logger = Logger.get_logger(name="FlashcardFactory")

    @classmethod
    def create_flashcard(
        cls,
        back_text: str,
        front_text: str,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutableFlashcard]:
        """
        Creates and returns a new instance of ImmutableFlashcard class.

        Args:
            back_text (str): The back side of the flashcard.
            created_at (Optional[datetime]): The timestamp when the flashcard was created.
            front_text (str): The front side of the flashcard.
            id (Optional[int]): The ID of the flashcard.
            key (Optional[str]): The key of the flashcard.
            updated_at (Optional[datetime]): The timestamp when the flashcard was last updated.
            uuid (Optional[str]): The UUID of the flashcard.

        Returns:
            Optional[ImmutableFlashcard]: The created flashcard object if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the flashcard.
        """
        try:
            # Attempt to create an d return an ImmutableFlashcard object
            return ImmutableFlashcard(
                created_at=created_at,
                back_text=back_text,
                front_text=front_text,
                id=id,
                key=key,
                updated_at=updated_at,
                uuid=uuid,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_flashcard' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class FlashcardManager(BaseObjectManager):
    """
    A manager class for managing flashcards in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for flashcards.

    Attributes:
        cache: (List[Any]): The cache for storing flashcards.
        logger (Logger): The logger instance associated with the object.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the FlashcardManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def count(self) -> int:
        """
        Returns the number of flashcards in the database.

        Returns:
            int: The number of flashcards in the database.
        """
        try:
            # Count the number of flashcards in the database
            result: Any = asyncio.run(
                FlashcardModel.execute(
                    database=Constants.DATABASE_PATH,
                    sql=f"SELECT COUNT(*) FROM {Constants.FLASHCARDS};",
                )
            )

            # Return the number of flashcards in the database
            return result[0][0] if result else 0
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create(
        self,
        flashcard: Union[ImmutableFlashcard, MutableFlashcard],
    ) -> Optional[ImmutableFlashcard]:
        """
        Creates a new flashcard in the database.

        Args:
            flashcard (Union[ImmutableFlashcard, MutableFlashcard]): The flashcard to be created.

        Returns:
            Optional[ImmutableFlashcard]: The newly created immutable flashcard if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the flashcard.
        """
        try:
            # Check if the flashcard object is immutable
            if isinstance(
                flashcard,
                ImmutableFlashcard,
            ):
                # If it is, convert it to a mutable flashcard
                flashcard = MutableFlashcard(**flashcard.to_dict(exclude=["_logger"]))

            # Set the created_at timestamp of the flashcard
            flashcard.created_at = Miscellaneous.get_current_datetime()

            # Set the key of the flashcard
            flashcard.key = f"FLASHCARD_{self.count() + 1}"

            # Set the updated_at timestamp of the flashcard
            flashcard.updated_at = Miscellaneous.get_current_datetime()

            # Set the uuid of the flashcard
            flashcard.uuid = str(uuid.uuid4())

            # Convert the flashcard object to a FlashcardModel object
            model: FlashcardModel = FlashcardConverter.object_to_model(object=flashcard)

            # Create a new flashcard in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            if id:
                # Set the ID of the flashcard
                flashcard.id = id

                # Convert the flashcard to an immutable flashcard
                flashcard = ImmutableFlashcard(**flashcard.to_dict(exclude=["_logger"]))

                # Add the flashcard to the cache
                self.add_to_cache(
                    key=flashcard.key,
                    value=flashcard,
                )

                # Return the newly created immutable flashcard
                return flashcard

            # Log a warning message indicating an error has occurred
            self.logger.warning(
                message=f"It seems that an error has occured while attempting to create a flashcard ({flashcard}) in the database."
            )

            # Return None indicating an error has occurred
            return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_flashcard' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete(
        self,
        flashcard: Union[ImmutableFlashcard, MutableFlashcard],
    ) -> bool:
        """
        Deletes a flashcard from the database.

        Args:
            flashcard (Union[ImmutableFlashcard, MutableFlashcard]): The flashcard to be deleted.

        Returns:
            bool: True if the flashcard was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the flashcard to an immutable flashcard and delete the flashcard from the database
            result: bool = asyncio.run(
                FlashcardConverter.object_to_model(
                    object=ImmutableFlashcard(**flashcard.to_dict(exclude=["_logger"]))
                ).delete()
            )

            # Return True if the flashcard was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all(self) -> Optional[List[ImmutableFlashcard]]:
        """
        Returns a list of all flashcards in the database.

        Returns:
            Optional[List[ImmutableFlashcard]]: A list of all flashcards in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if cache and table size are equal
            if self.cache and len(self._cache) == self.count():
                # Return the list of immutable flashcards from the cache
                return self.get_cache_values()

            # Get all flashcards from the database
            models: List[FlashcardModel] = asyncio.run(
                FlashcardModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of FlashcardModel objects to a list of ImmutableFlashcard objects
            flashcards: List[ImmutableFlashcard] = [
                ImmutableFlashcard(**model.to_dict(exclude=["_logger"]))
                for model in models
            ]

            # Iterate over the list of immutable flashcards
            for flashcard in flashcards:
                if not self.is_key_in_cache(key=flashcard.key):
                    # Add the immutable flashcard to the cache
                    self.add_to_cache(
                        key=flashcard.key,
                        value=flashcard,
                    )
                else:
                    # Update the immutable flashcard in the cache
                    self.update_in_cache(
                        key=flashcard.key,
                        value=flashcard,
                    )

            # Return the list of immutable flashcards
            return flashcards
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_by_id(
        self,
        id: int,
    ) -> Optional[ImmutableFlashcard]:
        """
        Returns a flashcard with the given ID.

        Args:
            id (int): The ID of the flashcard.

        Returns:
            Optional[ImmutableFlashcard]: The flashcard with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the flashcard is already in the cache
            if self.is_key_in_cache(key=f"FLASHCARD_{id}"):
                # Return the flashcard from the cache
                return self.get_value_from_cache(key=f"FLASHCARD_{id}")

            # Get the flashcard with the given ID from the database
            model: Optional[FlashcardModel] = asyncio.run(
                FlashcardModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the flashcard if it exists
            if model is not None:
                # Convert the FlashcardModel object to an ImmutableFlashcard object
                return ImmutableFlashcard(**model.to_dict(exclude=["_logger"]))
            else:
                # Return None indicating that the flashcard does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_by_uuid(
        self,
        uuid: str,
    ) -> Optional[ImmutableFlashcard]:
        """
        Returns a flashcard with the given UUID.

        Args:
            uuid (str): The UUID of the flashcard.

        Returns:
            Optional[ImmutableFlashcard]: The flashcard with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the flashcard is already in the cache
            if self.is_key_in_cache(key=uuid):
                # Return the flashcard from the cache
                return self.get_value_from_cache(key=uuid)

            # Get the flashcard with the given UUID from the database
            model: Optional[FlashcardModel] = asyncio.run(
                FlashcardModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the flashcard if it exists
            if model is not None:
                # Convert the FlashcardModel object to an ImmutableFlashcard object
                return ImmutableFlashcard(**model.to_dict(exclude=["_logger"]))
            else:
                # Return None indicating that the flashcard does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update(
        self,
        flashcard: Union[ImmutableFlashcard, MutableFlashcard],
    ) -> Optional[ImmutableFlashcard]:
        """
        Updates a flashcard with the given ID.

        Args:
            flashcard (Union[ImmutableFlashcard, MutableFlashcard]): The flashcard to update.

        Returns:
            Optional[ImmutableFlashcard]: The updated flashcard if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the flashcard to an immutable flashcard and update the flashcard in the database
            model: Optional[FlashcardModel] = asyncio.run(
                FlashcardConverter.object_to_model(
                    object=ImmutableFlashcard(**flashcard.to_dict(exclude=["_logger"]))
                ).update(
                    **flashcard.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    )
                )
            )

            # Return the updated flashcard if it exists
            if model is not None:
                # Convert the FlashcardModel object to an ImmutableFlashcard object
                flashcard = ImmutableFlashcard(**model.to_dict(exclude=["_logger"]))

                # Add the flashcard to the cache
                self.update_in_cache(
                    key=flashcard.key,
                    value=flashcard,
                )

                # Return the updated flashcard
                return flashcard
            else:
                # Return None indicating that the flashcard does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class FlashcardModel(ImmutableBaseModel):
    """
    Represents the structure of a flashcard model.

    Attributes:
        back_text (Optional[str]): The back side of the flashcard.
        created_at (Optional[datetime]): The timestamp when the flashcard was created.
        front_text (Optional[str]): The front side of the flashcard.
        id (Optional[int]): The ID of the flashcard.
        key (Optional[str]): The key of the flashcard.
        updated_at (Optional[datetime]): The timestamp when the flashcard was last updated.
        uuid (Optional[str]): The UUID of the flashcard.
    """

    table: str = Constants.FLASHCARDS

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

    back_text: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="back_text",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=False,
    )

    created_at: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="created_at",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="DATETIME",
        unique=False,
    )

    front_text: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="front_text",
        nullable=True,
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
        unique=False,
    )

    updated_at: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="updated_at",
        nullable=True,
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
        back_text: Optional[str] = None,
        created_at: Optional[datetime] = None,
        front_text: Optional[str] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the FlashcardModel class.

        Args:
            back_text (Optional[str]): The back side of the flashcard.
            created_at (Optional[datetime]): The timestamp when the flashcard was created.
            front_text (Optional[str]): The front side of the flashcard.
            key (Optional[str]): The key of the flashcard.
            updated_at (Optional[datetime]): The timestamp when the flashcard was last updated.
            uuid (Optional[str]): The UUID of the flashcard.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            back_text=back_text,
            created_at=created_at,
            front_text=front_text,
            id=id,
            key=key,
            table=Constants.FLASHCARDS,
            updated_at=updated_at,
            uuid=uuid,
        )
