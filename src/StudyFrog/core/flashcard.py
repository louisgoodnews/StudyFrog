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
        ancestor (int): The ID of the ancestor flashcard.
        back_text (str): The back side of the flashcard.
        children (List[int]): The IDs of the children flashcards.
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
        ancestor: Optional[int] = None,
        children: Optional[List[int]] = None,
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
            front_text (str): The front side of the flashcard.
            ancestor (int): The ID of the ancestor flashcard.
            children (List[int]): The IDs of the children flashcards.
            created_at (datetime): The timestamp when the flashcard was created.
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
            front_text=front_text,
            ancestor=ancestor,
            children=children,
            created_at=created_at,
            id=id,
            key=key,
            updated_at=updated_at,
            uuid=uuid or str(uuid.uuid4()),
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
        ancestor (int): The ID of the ancestor flashcard.
        back_text (str): The back side of the flashcard.
        children (List[int]): The IDs of the children flashcards.
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
        ancestor: Optional[int] = None,
        children: Optional[List[int]] = None,
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
            front_text (str): The front side of the flashcard.
            ancestor (int): The ID of the ancestor flashcard.
            children (List[int]): The IDs of the children flashcards.
            created_at (datetime): The timestamp when the flashcard was created.
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
            front_text=front_text,
            ancestor=ancestor,
            children=children,
            created_at=created_at,
            id=id,
            key=key,
            updated_at=updated_at,
            uuid=uuid or str(uuid.uuid4()),
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
            return ImmutableFlashcard(**model.to_dict(exclude=["logger"])["fields"])
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
            return FlashcardModel(**object.to_dict(exclude=["logger"]))
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
        ancestor: Optional[int] = None,
        children: Optional[List[int]] = None,
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
            front_text (str): The front side of the flashcard.
            ancestor (Optional[int]): The ID of the ancestor flashcard.
            children (Optional[List[int]]): The IDs of the children flashcards.
            created_at (Optional[datetime]): The timestamp when the flashcard was created.
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
                back_text=back_text,
                front_text=front_text,
                ancestor=ancestor,
                children=children,
                created_at=created_at,
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
    pass


class FlashcardModel(ImmutableBaseModel):
    """
    Represents the structure of a flashcard model.

    Attributes:
        ancestor (Optional[int]): The ID of the ancestor flashcard.
        back_text (Optional[str]): The back side of the flashcard.
        children (Optional[List[int]]): The IDs of the children flashcards.
        created_at (Optional[datetime]): The timestamp when the flashcard was created.
        front_text (Optional[str]): The front side of the flashcard.
        id (Optional[int]): The ID of the flashcard.
        key (Optional[str]): The key of the flashcard.
        updated_at (Optional[datetime]): The timestamp when the flashcard was last updated.
        uuid (Optional[str]): The UUID of the flashcard.
    """

    def __init__(
        self,
        ancestor: Optional[int] = None,
        back_text: Optional[str] = None,
        children: Optional[List[int]] = None,
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
            ancestor (Optional[int]): The ID of the ancestor flashcard.
            back_text (Optional[str]): The back side of the flashcard.
            children (Optional[List[int]]): The IDs of the children flashcards.
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
            table="flashcards",
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
            ancestor=(
                ancestor
                or Field(
                    autoincrement=False,
                    default=None,
                    description="",
                    foreign_key="flashcards(id)",
                    index=False,
                    name="ancestor",
                    nullable=True,
                    on_delete="CASCADE",
                    on_update="CASCADE",
                    primary_key=False,
                    size=None,
                    type="INTEGER",
                    unique=False,
                )
            ),
            back_text=(
                back_text
                or Field(
                    autoincrement=False,
                    default=None,
                    description="",
                    foreign_key=None,
                    index=False,
                    name="back_text",
                    nullable=True,
                    on_delete="NO ACTION",
                    on_update="NO ACTION",
                    primary_key=False,
                    size=255,
                    type="VARCHAR",
                    unique=False,
                )
            ),
            children=(
                children
                or Field(
                    autoincrement=False,
                    default=None,
                    description="",
                    foreign_key=None,
                    index=False,
                    name="children",
                    nullable=True,
                    on_delete="NO ACTION",
                    on_update="NO ACTION",
                    primary_key=False,
                    size=None,
                    type="JSON",
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
            front_text=(
                front_text
                or Field(
                    autoincrement=False,
                    default=None,
                    description="",
                    foreign_key=None,
                    index=False,
                    name="front_text",
                    nullable=True,
                    on_delete="NO ACTION",
                    on_update="NO ACTION",
                    primary_key=False,
                    size=255,
                    type="VARCHAR",
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
