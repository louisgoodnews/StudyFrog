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
        body_text (str): The body of the Note.
        created_at (datetime): The timestamp when the Note was created.
        custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
        icon (str): The icon of the Note.
        id (int): The ID of the Note.
        key (str): The key of the Note.
        title_text (str): The title of the Note.
        updated_at (datetime): The timestamp when the Note was last updated.
        uuid (str): The UUID of the Note.
    """

    def __init__(
        self,
        body_text: str,
        title_text: str,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        icon: Optional[str] = "📝",
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
            created_at (datetime): The timestamp when the Note was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
            icon (str): The icon of the Note. Defaults to "📝".
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
            created_at=created_at,
            custom_field_values=custom_field_values,
            icon=icon,
            id=id,
            key=key,
            title_text=title_text,
            updated_at=updated_at,
            uuid=uuid,
        )

    def to_mutable(self) -> "MutableNote":
        """
        Returns a mutable copy of the ImmutableNote instance.

        Returns:
            MutableNote: A mutable copy of the ImmutableNote instance.
        """

        # Create a new MutableNote instance from the dictionary representation of the ImmutableNote instance
        return MutableNote(
            **self.to_dict(
                exclude=[
                    "_logger",
                ]
            )
        )


class MutableNote(MutableBaseObject):
    """
    An immutable class representing a Note.

    A Note is a learning tool used to aid memorization by providing a question on one side and the answer on the other.

    Attributes:
        body_text (str): The body of the Note.
        created_at (datetime): The timestamp when the Note was created.
        custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
        icon (str): The icon of the Note.
        id (int): The ID of the Note.
        key (str): The key of the Note.
        title_text (str): The title of the Note.
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
        icon: Optional[str] = "📝",
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
            icon (str): The icon of the Note. Defaults to "📝".
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
            icon=icon,
            id=id,
            key=key,
            updated_at=updated_at,
            uuid=uuid,
        )

    def to_immutable(self) -> ImmutableNote:
        """
        Returns an immutable copy of the MutableNote instance.

        Returns:
            ImmutableNote: An immutable copy of the MutableNote instance.
        """

        # Create a new ImmutableNote instance from the dictionary representation of the MutableNote instance
        return ImmutableNote(
            **self.to_dict(
                exclude=[
                    "_logger",
                ]
            )
        )


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
            return ImmutableNote(
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
            return NoteModel(
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
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        icon: Optional[str] = "📝",
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
            created_at (Optional[datetime]): The timestamp when the Note was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): A list of custom field values.
            icon (Optional[str]): The icon of the Note. Defaults to "📝".
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
                created_at=created_at,
                custom_field_values=custom_field_values,
                icon=icon,
                id=id,
                key=key,
                title_text=title_text,
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
    """
    A manager class for managing notes in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for notes.

    Attributes:
        cache: (List[Any]): The cache for storing notes.
        logger (Logger): The logger instance associated with the object.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the NoteManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def count_notes(self) -> int:
        """
        Returns the number of notes in the database.

        Returns:
            int: The number of notes in the database.
        """
        try:
            # Count the number of notes in the database
            result: Any = asyncio.run(
                NoteModel.execute(
                    database=Constants.DATABASE_PATH,
                    sql=f"SELECT COUNT(*) FROM {Constants.NOTES};",
                )
            )

            # Return the number of notes in the database
            return result[0][0] if result else 0
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_note(
        self,
        note: Union[ImmutableNote, MutableNote],
    ) -> Optional[ImmutableNote]:
        """
        Creates a new note in the database.

        Args:
            note (Union[ImmutableNote, MutableNote]): The note to be created.

        Returns:
            Optional[ImmutableNote]: The newly created immutable note if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the note.
        """
        try:
            # Check if the note object is immutable
            if isinstance(
                note,
                ImmutableNote,
            ):
                # If it is, convert it to a mutable note
                note = MutableNote(
                    **note.to_dict(
                        exclude=[
                            "_logger",
                        ]
                    )
                )

            # Set the created_at timestamp of the note
            note.created_at = Miscellaneous.get_current_datetime()

            # Set the custom_field_values of the note
            note.custom_field_values = [] or note.custom_field_values

            # Set the key of the note
            note.key = f"NOTE_{self.count_notes() + 1}"

            # Set the updated_at timestamp of the note
            note.updated_at = Miscellaneous.get_current_datetime()

            # Set the uuid of the note
            note.uuid = Miscellaneous.get_uuid()

            # Convert the note object to a NoteModel object
            model: NoteModel = NoteConverter.object_to_model(object=note)

            # Create a new note in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            if id:
                # Set the ID of the note
                note.id = id

                # Convert the note to an immutable note
                note = ImmutableNote(
                    **note.to_dict(
                        exclude=[
                            "_logger",
                        ]
                    )
                )

                # Add the note to the cache
                self.add_to_cache(
                    key=note.key,
                    value=note,
                )

                # Return the newly created immutable note
                return note

            # Log a warning message indicating an error has occurred
            self.logger.warning(
                message=f"It seems that an error has occured while attempting to create a note ({note}) in the database."
            )

            # Return None indicating an error has occurred
            return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_note' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete_note(
        self,
        note: Union[ImmutableNote, MutableNote],
    ) -> bool:
        """
        Deletes a note from the database.

        Args:
            note (Union[ImmutableNote, MutableNote]): The note to be deleted.

        Returns:
            bool: True if the note was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the note to an immutable note and delete the note from the database
            result: bool = asyncio.run(
                NoteConverter.object_to_model(
                    object=ImmutableNote(
                        **note.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).delete()
            )

            # Return True if the note was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all_notes(self) -> Optional[List[ImmutableNote]]:
        """
        Returns a list of all notes in the database.

        Returns:
            Optional[List[ImmutableNote]]: A list of all notes in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if cache and table size are equal
            if self.cache and len(self._cache) == self.count_notes():
                # Return the list of immutable notes from the cache
                return self.get_cache_values()

            # Get all notes from the database
            models: List[NoteModel] = asyncio.run(
                NoteModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of NoteModel objects to a list of ImmutableNote objects
            notes: List[ImmutableNote] = [
                ImmutableNote(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable notes
            for note in notes:
                if not self.is_key_in_cache(key=note.key):
                    # Add the immutable note to the cache
                    self.add_to_cache(
                        key=note.key,
                        value=note,
                    )
                else:
                    # Update the immutable note in the cache
                    self.update_in_cache(
                        key=note.key,
                        value=note,
                    )

            # Return the list of immutable notes
            return notes
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_note_by(
        self,
        field: str,
        value: Any,
    ) -> Optional[ImmutableNote]:
        """
        Retrieves a note by the given field and value.

        Args:
            field (str): The field to search by.
            value (Any): The value to search for.

        Returns:
            Optional[ImmutableNote]: The note with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the note is already in the cache
            if self.is_key_in_cache(key=field):
                # Return the note from the cache
                return self.get_value_from_cache(key=field)

            # Get the note with the given field and value from the database
            model: Optional[NoteModel] = asyncio.run(
                NoteModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Return the note if it exists
            if model is not None:
                # Convert the NoteModel object to an ImmutableNote object
                return ImmutableNote(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the note does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_note_by_id(
        self,
        id: int,
    ) -> Optional[ImmutableNote]:
        """
        Returns a note with the given ID.

        Args:
            id (int): The ID of the note.

        Returns:
            Optional[ImmutableNote]: The note with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the note is already in the cache
            if self.is_key_in_cache(key=f"NOTE_{id}"):
                # Return the note from the cache
                return self.get_value_from_cache(key=f"NOTE_{id}")

            # Get the note with the given ID from the database
            model: Optional[NoteModel] = asyncio.run(
                NoteModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the note if it exists
            if model is not None:
                # Convert the NoteModel object to an ImmutableNote object
                return ImmutableNote(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the note does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_note_by_uuid(
        self,
        uuid: str,
    ) -> Optional[ImmutableNote]:
        """
        Returns a note with the given UUID.

        Args:
            uuid (str): The UUID of the note.

        Returns:
            Optional[ImmutableNote]: The note with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the note is already in the cache
            if self.is_key_in_cache(key=uuid):
                # Return the note from the cache
                return self.get_value_from_cache(key=uuid)

            # Get the note with the given UUID from the database
            model: Optional[NoteModel] = asyncio.run(
                NoteModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the note if it exists
            if model is not None:
                # Convert the NoteModel object to an ImmutableNote object
                return ImmutableNote(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the note does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def search_notes(
        self,
        **kwargs,
    ) -> Optional[Union[List[ImmutableNote]]]:
        """
        Searches for notes in the database.

        Args:
            **kwargs: Any additional keyword arguments to be passed to the search method of the NoteModel class.

        Returns:
            Optional[Union[List[ImmutableNote]]]: The found notes if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Search for notes in the database
            models: Optional[List[NoteModel]] = asyncio.run(
                NoteModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found notes if any
            if models is not None and len(models) > 0:
                return [
                    ImmutableNote(
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
                # Return None indicating that no notes were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_note(
        self,
        note: Union[ImmutableNote, MutableNote],
    ) -> Optional[ImmutableNote]:
        """
        Updates a note with the given ID.

        Args:
            note (Union[ImmutableNote, MutableNote]): The note to update.

        Returns:
            Optional[ImmutableNote]: The updated note if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the note to an immutable note and update the note in the database
            model: Optional[NoteModel] = asyncio.run(
                NoteConverter.object_to_model(
                    object=ImmutableNote(
                        **note.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).update(
                    database=Constants.DATABASE_PATH,
                    **note.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Return the updated note if it exists
            if model is not None:
                # Convert the NoteModel object to an ImmutableNote object
                note = ImmutableNote(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the note to the cache
                self.update_in_cache(
                    key=note.key,
                    value=note,
                )

                # Return the updated note
                return note
            else:
                # Return None indicating that the note does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class NoteModel(ImmutableBaseModel):
    """
    Represents the structure of a Note model.

    Attributes:
        body_text (Optional[str]): The body of the Note.
        created_at (Optional[datetime]): The timestamp when the Note was created.
        custom_field_values (Optional[List[Dict[str, Any]]]): The custom fields of the Note.
        icon (Optional[str]): The icon of the Note. Defaults to "📝".
        id (Optional[int]): The ID of the Note.
        key (Optional[str]): The key of the Note.
        title_text (Optional[str]): The title of the Note.
        updated_at (Optional[datetime]): The timestamp when the Note was last updated.
        uuid (Optional[str]): The UUID of the Note.
    """

    table: str = Constants.NOTES

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

    body_text: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="body_text",
        nullable=False,
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

    icon: Field = Field(
        autoincrement=False,
        default="📝",
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

    title_text: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="title_text",
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
        body_text: Optional[str] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        icon: Optional[str] = "📝",
        id: Optional[int] = None,
        key: Optional[str] = None,
        title_text: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the NoteModel class.

        Args:
            body_text (Optional[str]): The body of the Note.
            created_at (Optional[datetime]): The timestamp when the Note was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): The custom fields of the Note.
            icon (Optional[str]): The icon of the Note. Defaults to "📝".
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
            body_text=body_text,
            created_at=created_at,
            custom_field_values=custom_field_values,
            icon="📝",
            id=id,
            key=key,
            table=Constants.NOTES,
            title_text=title_text,
            updated_at=updated_at,
            uuid=uuid,
        )
