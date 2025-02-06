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
    "ImmutableNote",
    "MutableNote",
    "NoteConverter",
    "NoteFactory",
    "NoteManager",
    "NoteModel",
]


class ImmutableNote(ImmutableBaseObject):
    """
    An immutable class representing a Note.

    A Note is a learning tool used to aid memorization by providing a question on one side and the answer on the other.

    Attributes:
        ancestor (int): The ID of the ancestor Note.
        body_text (str): The body of the Note.
        children (List[int]): The IDs of the children Notes.
        created_at (datetime): The timestamp when the Note was created.
        title_text (str): The title of the Note.
        id (int): The ID of the Note.
        key (str): The key of the Note.
        updated_at (datetime): The timestamp when the Note was last updated.
        uuid (str): The UUID of the Note.
    """

    def __init__(
        self,
        body_text: str,
        title_text: str,
        ancestor: Optional[int] = None,
        children: Optional[List[int]] = None,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableNote class.

        Args:
            body_text (str): The body of the Note.
            title_text (str): The title of the Note.
            ancestor (int): The ID of the ancestor Note.
            children (List[int]): The IDs of the children Notes.
            created_at (datetime): The timestamp when the Note was created.
            id (int): The ID of the Note.
            key (str): The key of the Note.
            updated_at (datetime): The timestamp when the Note was last updated.
            uuid (str): The UUID of the Note.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            body_text=body_text,
            title_text=title_text,
            ancestor=ancestor,
            children=children,
            created_at=created_at,
            id=id,
            key=key,
            updated_at=updated_at,
            uuid=uuid or str(uuid.uuid4()),
        )


class MutableNote(MutableBaseObject):
    """
    An immutable class representing a Note.

    A Note is a learning tool used to aid memorization by providing a question on one side and the answer on the other.

    Attributes:
        ancestor (int): The ID of the ancestor Note.
        body_text (str): The body of the Note.
        children (List[int]): The IDs of the children Notes.
        created_at (datetime): The timestamp when the Note was created.
        title_text (str): The title of the Note.
        id (int): The ID of the Note.
        key (str): The key of the Note.
        updated_at (datetime): The timestamp when the Note was last updated.
        uuid (str): The UUID of the Note.
    """

    def __init__(
        self,
        body_text: str,
        title_text: str,
        ancestor: Optional[int] = None,
        children: Optional[List[int]] = None,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableNote class.

        Args:
            body_text (str): The body of the Note.
            title_text (str): The title of the Note.
            ancestor (int): The ID of the ancestor Note.
            children (List[int]): The IDs of the children Notes.
            created_at (datetime): The timestamp when the Note was created.
            id (int): The ID of the Note.
            key (str): The key of the Note.
            updated_at (datetime): The timestamp when the Note was last updated.
            uuid (str): The UUID of the Note.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            body_text=body_text,
            title_text=title_text,
            ancestor=ancestor,
            children=children,
            created_at=created_at,
            id=id,
            key=key,
            updated_at=updated_at,
            uuid=uuid or str(uuid.uuid4()),
        )


class NoteConverter:
    logger: Logger = Logger.get_logger(name="NoteConverter")


class NoteFactory:
    """
    A factory class used to create instances of ImmutableNote class.

    Attributes:
        logger (Logger): The logger instance associated with the object.
    """

    logger: Logger = Logger.get_logger(name="NoteFactory")

    @classmethod
    def create_Note(
        cls,
        body_text: str,
        title_text: str,
        ancestor: Optional[int] = None,
        children: Optional[List[int]] = None,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutableNote]:
        """
        Creates and returns a new instance of ImmutableNote class.

        Args:
            body_text (str): The body of the Note.
            title_text (str): The title of the Note.
            ancestor (Optional[int]): The ID of the ancestor Note.
            children (Optional[List[int]]): The IDs of the children Notes.
            created_at (Optional[datetime]): The timestamp when the Note was created.
            id (Optional[int]): The ID of the Note.
            key (Optional[str]): The key of the Note.
            updated_at (Optional[datetime]): The timestamp when the Note was last updated.
            uuid (Optional[str]): The UUID of the Note.

        Returns:
            Optional[ImmutableNote]: The created Note object if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the Note.
        """
        try:
            # Attempt to create an d return an ImmutableNote object
            return ImmutableNote(
                body_text=body_text,
                title_text=title_text,
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
                message=f"Caught an exception while attempting to run 'create_Note' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class NoteManager(BaseObjectManager):
    pass


class NoteModel(BaseModel):
    def __init__(self) -> None:
        super().__init__()
