"""
Author: lodego
Date: 2025-03-02
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
    "ImmutableComment",
    "MutableComment",
    "CommentConverter",
    "CommentFactory",
    "CommentManager",
    "CommentModel",
]


class ImmutableComment(ImmutableBaseObject):
    """
    An immutable class representing a comment.

    Attributes:
        parent (str): The key of the parent object.
        comment_text (str): The text of the comment.
        ancestor (int): The ID of the ancestor comment.
        created_at (datetime): The timestamp when the comment was created.
        descendants (List[str]): The IDs of the descendant comments.
        icon (str): The icon of the comment. Defaults to "💭".
        id (int): The ID of the comment.
        key (str): The key of the comment.
        last_edited_at (datetime): The timestamp when the comment was last edited.
        updated_at (datetime): The timestamp when the comment was last updated.
        uuid (str): The UUID of the comment.
        version (int): The version of the comment.
    """

    def __init__(
        self,
        parent: str,
        comment_text: str,
        ancestor: Optional[int] = None,
        created_at: Optional[datetime] = None,
        descendants: Optional[List[str]] = None,
        icon: Optional[str] = "💭",
        id: Optional[int] = None,
        key: Optional[str] = None,
        last_edited_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
        version: Optional[int] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableComment class.

        Args:
            parent (str): The key of the parent object.
            comment_text (str): The text of the comment.
            ancestor (Optional[int]): The ID of the ancestor comment.
            created_at (Optional[datetime]): The timestamp when the comment was created.
            descendants (Optional[List[str]]): The IDs of the descendant comments.
            icon (Optional[str]): The icon of the comment.
            id (Optional[int]): The ID of the comment.
            key (Optional[str]): The key of the comment.
            last_edited_at (Optional[datetime]): The timestamp when the comment was last edited.
            updated_at (Optional[datetime]): The timestamp when the comment was last updated.
            uuid (Optional[str]): The UUID of the comment.
            version (Optional[int]): The version of the comment.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            ancestor=ancestor,
            comment_text=comment_text,
            created_at=created_at,
            descendants=descendants,
            icon=icon,
            id=id,
            key=key,
            last_edited_at=last_edited_at,
            parent=parent,
            updated_at=updated_at,
            uuid=uuid,
            version=version,
        )


class MutableComment(MutableBaseObject):
    """
    A mutable class representing a comment.

    Attributes:
        parent (str): The key of the parent object.
        comment_text (str): The text of the comment.
        ancestor (int): The ID of the ancestor comment.
        created_at (datetime): The timestamp when the comment was created.
        descendants (List[str]): The IDs of the descendant comments.
        icon (str): The icon of the comment. Defaults to "💭".
        id (int): The ID of the comment.
        key (str): The key of the comment.
        last_edited_at (datetime): The timestamp when the comment was last edited.
        updated_at (datetime): The timestamp when the comment was last updated.
        uuid (str): The UUID of the comment.
        version (int): The version of the comment.
    """

    def __init__(
        self,
        parent: str,
        comment_text: str,
        ancestor: Optional[int] = None,
        created_at: Optional[datetime] = None,
        descendants: Optional[List[str]] = None,
        icon: Optional[str] = "💭",
        id: Optional[int] = None,
        key: Optional[str] = None,
        last_edited_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
        version: Optional[int] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableComment class.

        Args:
            parent (str): The key of the parent object.
            comment_text (str): The text of the comment.
            ancestor (Optional[int]): The ID of the ancestor comment.
            created_at (Optional[datetime]): The timestamp when the comment was created.
            descendants (Optional[List[str]]): The IDs of the descendant comments.
            icon (Optional[str]): The icon of the comment.
            id (Optional[int]): The ID of the comment.
            key (Optional[str]): The key of the comment.
            last_edited_at (Optional[datetime]): The timestamp when the comment was last edited.
            updated_at (Optional[datetime]): The timestamp when the comment was last updated.
            uuid (Optional[str]): The UUID of the comment.
            version (Optional[int]): The version of the comment.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            ancestor=ancestor,
            comment_text=comment_text,
            created_at=created_at,
            descendants=descendants,
            icon=icon,
            id=id,
            key=key,
            last_edited_at=last_edited_at,
            parent=parent,
            updated_at=updated_at,
            uuid=uuid,
            version=version,
        )

    def to_immutable(self) -> Optional[ImmutableComment]:
        """
        Converts the mutable comment to an immutable comment.

        Returns:
            Optional[ImmutableComment]: The immutable comment, or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while converting the comment.
        """
        try:
            # Attempt to create an ImmutableComment instance from the current MutableComment instance
            return ImmutableComment(**self.to_dict(exclude=["_logger"]))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_immutable' method from {self.__class__.__name__}: {e}"
            )

            # Return None indicating an exception has occurred
            return None


class CommentConverter:
    """
    A converter class for transforming between CommentModel and ImmutableComment instances.

    This class provides methods to convert a CommentModel instance to an ImmutableComment instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the CommentConverter class.
    """

    logger: Logger = Logger.get_logger(name="CommentConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "CommentModel",
    ) -> Optional[ImmutableComment]:
        """
        Converts a given CommentModel instance to an ImmutableComment instance.

        Args:
            model (CommentModel): The CommentModel instance to be converted.

        Returns:
            ImmutableComment: The converted ImmutableComment instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the CommentModel instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableComment class from the dictionary representation of the CommentModel instance
            return ImmutableComment(
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
        object: ImmutableComment,
    ) -> Optional["CommentModel"]:
        """
        Converts a given ImmutableComment instance to a CommentModel instance.

        Args:
            object (ImmutableComment): The ImmutableComment instance to be converted.

        Returns:
            CommentModel: The converted CommentModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ImmutableComment instance.
        """
        try:
            # Attempt to create and return a new instance of the CommentModel class from the dictionary representation of the ImmutableComment instance
            return CommentModel(
                **object.to_dict(
                    exclude=[
                        "_logger",
                        "_values",
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


class CommentFactory:
    logger: Logger = Logger.get_logger(name="CommentFactory")

    @classmethod
    def creeate_comment(
        cls,
        parent: str,
        comment_text: str,
        ancestor: Optional[int] = None,
        created_at: Optional[datetime] = None,
        descendants: Optional[List[str]] = None,
        icon: Optional[str] = "💭",
        id: Optional[int] = None,
        key: Optional[str] = None,
        last_edited_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
        version: Optional[int] = None,
    ) -> Optional[ImmutableComment]:
        """
        Creates a new instance of the CommentModel class.

        Args:
            parent (int): The parent ID of the comment.
            comment_text (str): The text content of the comment.
            ancestor (Optional[int]): The ancestor ID of the comment.
            created_at (Optional[datetime]): The creation timestamp of the comment.
            descendants (Optional[List[str]]): The list of descendants of the comment.
            icon (Optional[str]): The icon of the comment.
            id (Optional[int]): The ID of the comment.
            key (Optional[str]): The key of the comment.
            last_edited_at (Optional[datetime]): The last edited timestamp of the comment.
            updated_at (Optional[datetime]): The update timestamp of the comment.
            uuid (Optional[str]): The UUID of the comment.
            version (Optional[int]): The version of the comment.

        Returns:
            CommentModel: The created CommentModel instance if no exception occurs. Otherwise, None.
        """
        try:
            # Attempt to create and return a new instance of the CommentModel class
            return CommentModel(
                ancestor=ancestor,
                comment_text=comment_text,
                created_at=created_at,
                descendants=descendants,
                icon=icon,
                id=id,
                key=key,
                last_edited_at=last_edited_at,
                parent=parent,
                updated_at=updated_at,
                uuid=uuid,
                version=version,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'creeate_comment' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class CommentManager(BaseObjectManager):
    """
    A manager class for managing comments in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for comments.

    Attributes:
        cache: (List[Any]): The cache for storing comments.
        logger (Logger): The logger instance associated with the object.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the CommentManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def count_comments(self) -> int:
        """
        Returns the number of comments in the database.

        Returns:
            int: The number of comments in the database.
        """
        try:
            # Count the number of comments in the database
            result: Any = asyncio.run(
                CommentModel.execute(
                    database=Constants.DATABASE_PATH,
                    sql=f"SELECT COUNT(*) FROM {Constants.COMMENTS};",
                )
            )

            # Return the number of comments in the database
            return result[0][0] if result else 0
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_comment(
        self,
        comment: Union[ImmutableComment, MutableComment],
    ) -> Optional[ImmutableComment]:
        """
        Creates a new comment in the database.

        Args:
            comment (Union[ImmutableComment, MutableComment]): The comment to be created.

        Returns:
            Optional[ImmutableComment]: The newly created immutable comment if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the comment.
        """
        try:
            # Check if the comment object is immutable
            if isinstance(
                comment,
                ImmutableComment,
            ):
                # If it is, convert it to a mutable comment
                comment = MutableComment(
                    **comment.to_dict(
                        exclude=[
                            "_logger",
                            "_values",
                        ]
                    )
                )

            # Set the created_at timestamp of the comment
            comment.created_at = Miscellaneous.get_current_datetime()

            # Set the custom_field_values of the comment
            comment.custom_field_values = [] or comment.custom_field_values

            # Set the key of the comment
            comment.key = f"COMMENT_{self.count_comments() + 1}"

            # Set the updated_at timestamp of the comment
            comment.updated_at = Miscellaneous.get_current_datetime()

            # Set the uuid of the comment
            comment.uuid = Miscellaneous.get_uuid()

            # Convert the comment object to a CommentModel object
            model: CommentModel = CommentConverter.object_to_model(object=comment)

            # Create a new comment in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            if id:
                # Set the ID of the comment
                comment.id = id

                # Convert the comment to an immutable comment
                comment = ImmutableComment(
                    **comment.to_dict(
                        exclude=[
                            "_logger",
                            "_values",
                        ]
                    )
                )

                # Add the comment to the cache
                self.add_to_cache(
                    key=comment.key,
                    value=comment,
                )

                # Return the newly created immutable comment
                return comment

            # Log a warning message indicating an error has occurred
            self.logger.warning(
                message=f"It seems that an error has occured while attempting to create a comment ({comment}) in the database."
            )

            # Return None indicating an error has occurred
            return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_comment' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete_comment(
        self,
        comment: Union[ImmutableComment, MutableComment],
    ) -> bool:
        """
        Deletes a comment from the database.

        Args:
            comment (Union[ImmutableComment, MutableComment]): The comment to be deleted.

        Returns:
            bool: True if the comment was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the comment to an immutable comment and delete the comment from the database
            result: bool = asyncio.run(
                CommentConverter.object_to_model(
                    object=ImmutableComment(
                        **comment.to_dict(
                            exclude=[
                                "_logger",
                                "_values",
                            ]
                        )
                    )
                ).delete()
            )

            # Return True if the comment was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all_comments(self) -> Optional[List[ImmutableComment]]:
        """
        Returns a list of all comments in the database.

        Returns:
            Optional[List[ImmutableComment]]: A list of all comments in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if cache and table size are equal
            if self.cache and len(self._cache) == self.count_comments():
                # Return the list of immutable comments from the cache
                return self.get_cache_values()

            # Get all comments from the database
            models: List[CommentModel] = asyncio.run(
                CommentModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of CommentModel objects to a list of ImmutableComment objects
            comments: List[ImmutableComment] = [
                ImmutableComment(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable comments
            for comment in comments:
                if not self.is_key_in_cache(key=comment.key):
                    # Add the immutable comment to the cache
                    self.add_to_cache(
                        key=comment.key,
                        value=comment,
                    )
                else:
                    # Update the immutable comment in the cache
                    self.update_in_cache(
                        key=comment.key,
                        value=comment,
                    )

            # Return the list of immutable comments
            return comments
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_comment_by(
        self,
        field: str,
        value: Any,
    ) -> Optional[ImmutableComment]:
        """
        Retrieves a comment by the given field and value.

        Args:
            field (str): The field to search by.
            value (Any): The value to search for.

        Returns:
            Optional[ImmutableComment]: The comment with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the comment is already in the cache
            if self.is_key_in_cache(key=field):
                # Return the comment from the cache
                return self.get_value_from_cache(key=field)

            # Get the comment with the given field and value from the database
            model: Optional[CommentModel] = asyncio.run(
                CommentModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Return the comment if it exists
            if model is not None:
                # Convert the CommentModel object to an ImmutableComment object
                return ImmutableComment(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the comment does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_comment_by_id(
        self,
        id: int,
    ) -> Optional[ImmutableComment]:
        """
        Returns a comment with the given ID.

        Args:
            id (int): The ID of the comment.

        Returns:
            Optional[ImmutableComment]: The comment with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the comment is already in the cache
            if self.is_key_in_cache(key=f"COMMENT_{id}"):
                # Return the comment from the cache
                return self.get_value_from_cache(key=f"COMMENT_{id}")

            # Get the comment with the given ID from the database
            model: Optional[CommentModel] = asyncio.run(
                CommentModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the comment if it exists
            if model is not None:
                # Convert the CommentModel object to an ImmutableComment object
                return ImmutableComment(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the comment does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_comment_by_uuid(
        self,
        uuid: str,
    ) -> Optional[ImmutableComment]:
        """
        Returns a comment with the given UUID.

        Args:
            uuid (str): The UUID of the comment.

        Returns:
            Optional[ImmutableComment]: The comment with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the comment is already in the cache
            if self.is_key_in_cache(key=uuid):
                # Return the comment from the cache
                return self.get_value_from_cache(key=uuid)

            # Get the comment with the given UUID from the database
            model: Optional[CommentModel] = asyncio.run(
                CommentModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the comment if it exists
            if model is not None:
                # Convert the CommentModel object to an ImmutableComment object
                return ImmutableComment(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the comment does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def search_comments(
        self,
        **kwargs,
    ) -> Optional[Union[List[ImmutableComment]]]:
        """
        Searches for comments in the database.

        Args:
            **kwargs: Any additional keyword arguments to be passed to the search method of the CommentModel class.

        Returns:
            Optional[Union[List[ImmutableComment]]]: The found comments if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Search for comments in the database
            models: Optional[List[CommentModel]] = asyncio.run(
                CommentModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found comments if any
            if models is not None and len(models) > 0:
                return [
                    ImmutableComment(
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
                # Return None indicating that no comments were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_comment(
        self,
        comment: Union[ImmutableComment, MutableComment],
    ) -> Optional[ImmutableComment]:
        """
        Updates a comment with the given ID.

        Args:
            comment (Union[ImmutableComment, MutableComment]): The comment to update.

        Returns:
            Optional[ImmutableComment]: The updated comment if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the comment to an immutable comment and update the comment in the database
            model: Optional[CommentModel] = asyncio.run(
                CommentConverter.object_to_model(
                    object=ImmutableComment(
                        **comment.to_dict(
                            exclude=[
                                "_logger",
                                "_values",
                            ]
                        )
                    )
                ).update(
                    database=Constants.DATABASE_PATH,
                    **comment.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Return the updated comment if it exists
            if model is not None:
                # Convert the CommentModel object to an ImmutableComment object
                comment = ImmutableComment(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the comment to the cache
                self.update_in_cache(
                    key=comment.key,
                    value=comment,
                )

                # Return the updated comment
                return comment
            else:
                # Return None indicating that the comment does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class CommentModel(ImmutableBaseModel):
    """
    Represents the structure of a comment model

    Attributes:
        ancestor (Optional[int]): The ID of the ancestor comment.
        comment_text (Optional[str]): The text of the comment.
        created_at (Optional[datetime]): The timestamp when the comment was created.
        descendants (Optional[List[int]]): The IDs of the descendant comments.
        icon (Optional[str]): The icon of the comment. Defaults to "💭".
        id (Optional[int]): The ID of the comment.
        key (Optional[str]): The key of the comment.
        last_viewed_at (Optional[datetime]): The timestamp when the comment was last viewed.
        priority (Optional[int]): The priority of the comment.
        status (Optional[int]): The status of the comment.
        updated_at (Optional[datetime]): The timestamp when the comment was last updated.
        uuid (Optional[str]): The UUID of the comment.
    """

    table: str = Constants.COMMENTS

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

    ancestor: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.COMMENTS}(id)",
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

    comment_text: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="comment_text",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="TEXT",
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

    descendants: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="descendants",
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
        default="💭",
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

    parent: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="parent",
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

    version: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="version",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    def __init__(
        self,
        ancestor: Optional[int] = None,
        comment_text: Optional[str] = None,
        created_at: Optional[datetime] = None,
        descendants: Optional[int] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        last_edited_at: Optional[datetime] = None,
        parent: Optional[int] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
        version: Optional[int] = None,
    ) -> None:
        """
        Initializes a new instance of the CommentModel class.

        Args:
            ancestor (Optional[int]): The ID of the ancestor comment.
            comment_text (Optional[str]): The text of the comment.
            created_at (Optional[datetime]): The timestamp when the comment was created.
            descendants (Optional[int]): The IDs of the descendant comments.
            id (Optional[int]): The ID of the comment.
            key (Optional[str]): The key of the comment.
            last_edited_at (Optional[datetime]): The timestamp when the comment was last edited.
            parent (Optional[int]): The key of the parent object.
            updated_at (Optional[datetime]): The timestamp when the comment was last updated.
            uuid (Optional[str]): The UUID of the comment.
            version (Optional[int]): The version of the comment.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            ancestor=ancestor,
            comment_text=comment_text,
            created_at=created_at,
            descendants=descendants,
            icon="💭",
            id=id,
            key=key,
            last_edited_at=last_edited_at,
            parent=parent,
            updated_at=updated_at,
            uuid=uuid,
            version=version,
        )
