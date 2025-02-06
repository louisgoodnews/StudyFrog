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

    def to_mutable(self) -> "MutableNote":
        """
        Returns a mutable copy of the ImmutableNote instance.

        Returns:
            MutableNote: A mutable copy of the ImmutableNote instance.
        """

        # Create a new MutableNote instance from the dictionary representation of the ImmutableNote instance
        return MutableNote(**self.to_dict(exclude=["logger"]))


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

    def to_immutable(self) -> ImmutableNote:
        """
        Returns an immutable copy of the MutableNote instance.

        Returns:
            ImmutableNote: An immutable copy of the MutableNote instance.
        """

        # Create a new ImmutableNote instance from the dictionary representation of the MutableNote instance
        return ImmutableNote(**self.to_dict(exclude=["logger"]))


class NoteConverter:
    """
    A converter class for transforming between NoteModel and ImmutableNote instances.

    This class provides methods to convert a NoteModel instance to an ImmutableNote instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the NoteConverter class.
    """

    logger: Logger = Logger.get_logger(name="NoteConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "NoteModel",
    ) -> Optional[ImmutableNote]:
        """
        Converts a given NoteModel instance to an ImmutableNote instance.

        Args:
            model (NoteModel): The NoteModel instance to be converted.

        Returns:
            ImmutableNote: The converted ImmutableNote instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the NoteModel instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableNote class from the dictionary representation of the NoteModel instance
            return ImmutableNote(**model.to_dict(exclude=["logger"])["fields"])
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
        object: ImmutableNote,
    ) -> Optional["NoteModel"]:
        """
        Converts a given ImmutableNote instance to a NoteModel instance.

        Args:
            object (ImmutableNote): The ImmutableNote instance to be converted.

        Returns:
            NoteModel: The converted NoteModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ImmutableNote instance.
        """
        try:
            # Attempt to create and return a new instance of the NoteModel class from the dictionary representation of the ImmutableNote instance
            return NoteModel(**object.to_dict(exclude=["logger"]))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'object_to_model' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


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


class NoteModel(ImmutableBaseModel):
    """
    Represents the structure of a Note model.

    Attributes:
        ancestor (Optional[int]): The ID of the ancestor Note.
        body_text (Optional[str]): The body of the Note.
        children (Optional[List[int]]): The IDs of the children Notes.
        created_at (Optional[datetime]): The timestamp when the Note was created.
        id (Optional[int]): The ID of the Note.
        key (Optional[str]): The key of the Note.
        title_text (Optional[str]): The title of the Note.
        updated_at (Optional[datetime]): The timestamp when the Note was last updated.
        uuid (Optional[str]): The UUID of the Note.
    """

    def __init__(
        self,
        ancestor: Optional[int] = None,
        body_text: Optional[str] = None,
        children: Optional[List[int]] = None,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        title_text: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the NoteModel class.

        Args:
            ancestor (Optional[int]): The ID of the ancestor Note.
            body_text (Optional[str]): The body of the Note.
            children (Optional[List[int]]): The IDs of the children Notes.
            created_at (Optional[datetime]): The timestamp when the Note was created.
            id (Optional[int]): The ID of the Note.
            key (Optional[str]): The key of the Note.
            title_text (Optional[str]): The title of the Note.
            updated_at (Optional[datetime]): The timestamp when the Note was last updated.
            uuid (Optional[str]): The UUID of the Note.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            table="notes",
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
                    foreign_key="notes(id)",
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
            body_text=(
                body_text
                or Field(
                    autoincrement=False,
                    default=None,
                    description="",
                    foreign_key=None,
                    index=False,
                    name="body_text",
                    nullable=True,
                    on_delete="CASCADE",
                    on_update="CASCADE",
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
                    on_delete="CASCADE",
                    on_update="CASCADE",
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
            title_text=(
                title_text
                or Field(
                    autoincrement=False,
                    default=None,
                    description="",
                    foreign_key=None,
                    index=False,
                    name="title_text",
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
