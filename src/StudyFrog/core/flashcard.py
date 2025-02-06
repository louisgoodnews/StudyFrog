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


class FlashcardConverter:
    logger: Logger = Logger.get_logger(name="FlashcardConverter")


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


class FlashcardModel(BaseModel):
    def __init__(self) -> None:
        super().__init__()
