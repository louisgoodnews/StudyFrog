"""
Author: lodego
Date: 2025-03-02
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
        metadata (Dict[str, Any]): The metadata of the comment.
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
        metadata: Optional[Dict[str, Any]] = None,
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
            metadata (Optional[Dict[str, Any]]): The metadata of the comment.
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
            hide_attributes=True,
            icon=icon,
            id=id,
            key=key,
            last_edited_at=last_edited_at,
            metadata=metadata,
            parent=parent,
            updated_at=updated_at,
            uuid=uuid,
            version=version,
        )

    @property
    def ancestor(self) -> int:
        """
        Returns the ID of the ancestor comment.

        Returns:
            int: The ID of the ancestor comment.
        """

        # Return the ancestor comment ID
        return self._ancestor

    @property
    def comment_text(self) -> str:
        """
        Returns the text of the comment.

        Returns:
            str: The text of the comment.
        """

        # Return the comment text
        return self._comment_text

    @property
    def descendants(self) -> List[str]:
        """
        Returns the IDs of the descendant comments.

        Returns:
            List[str]: The IDs of the descendant comments.
        """

        # Return the list of descendant comment IDs
        return self._descendants

    @property
    def icon(self) -> str:
        """
        Returns the icon of the comment.

        Returns:
            str: The icon of the comment.
        """

        # Return the comment icon
        return self._icon

    @property
    def id(self) -> int:
        """
        Returns the ID of the comment.

        Returns:
            int: The ID of the comment.
        """

        # Return the comment ID
        return self._id

    @property
    def key(self) -> str:
        """
        Returns the key of the comment.

        Returns:
            str: The key of the comment.
        """

        # Return the comment key
        return self._key

    @property
    def last_edited_at(self) -> datetime:
        """
        Returns the timestamp when the comment was last edited.

        Returns:
            datetime: The timestamp when the comment was last edited.
        """

        # Return the timestamp when the comment was last edited
        return self._last_edited_at

    @property
    def metadata(self) -> Dict[str, Any]:
        """
        Returns the metadata of the comment.

        Returns:
            Dict[str, Any]: The metadata of the comment.
        """

        # Return the comment metadata
        return self._metadata

    @property
    def parent(self) -> str:
        """
        Returns the key of the parent object.

        Returns:
            str: The key of the parent object.
        """

        # Return the parent object key
        return self._parent

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp when the comment was last updated.

        Returns:
            datetime: The timestamp when the comment was last updated.
        """

        # Return the timestamp when the comment was last updated
        return self._updated_at

    @property
    def uuid(self) -> str:
        """
        Returns the UUID of the comment.

        Returns:
            str: The UUID of the comment.
        """

        # Return the comment UUID
        return self._uuid

    @property
    def version(self) -> int:
        """
        Returns the version of the comment.

        Returns:
            int: The version of the comment.
        """

        # Return the comment version
        return self._version

    def to_mutable(self) -> Optional["MutableComment"]:
        """
        Converts the immutable comment to a mutable comment.

        Returns:
            Optional[MutableComment]: The mutable comment, or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while converting the comment.
        """
        try:
            # Attempt to create a MutableComment instance from the current ImmutableComment instance
            return MutableComment(**self.to_dict(exclude=["_logger"]))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_mutable' method from {self.__class__.__name__}: {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None


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
        metadata (Dict[str, Any]): The metadata of the comment.
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
        metadata: Optional[Dict[str, Any]] = None,
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
            metadata (Optional[Dict[str, Any]]): The metadata of the comment.
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
            hide_attributes=True,
            icon=icon,
            id=id,
            key=key,
            last_edited_at=last_edited_at,
            metadata=metadata,
            parent=parent,
            updated_at=updated_at,
            uuid=uuid,
            version=version,
        )

    @property
    def ancestor(self) -> int:
        """
        Returns the ID of the ancestor comment.

        Returns:
            int: The ID of the ancestor comment.
        """

        # Return the ancestor comment ID
        return self._ancestor

    @ancestor.setter
    def ancestor(
        self,
        value: int,
    ) -> None:
        """
        Sets the ID of the ancestor comment.

        Args:
            value (int): The ID of the ancestor comment.

        Returns:
            None
        """

        # Set the ancestor comment ID
        self._ancestor = value

    @property
    def comment_text(self) -> str:
        """
        Returns the text of the comment.

        Returns:
            str: The text of the comment.
        """

        # Return the comment text
        return self._comment_text

    @comment_text.setter
    def comment_text(
        self,
        value: str,
    ) -> None:
        """
        Sets the text of the comment.

        Args:
            value (str): The text of the comment.

        Returns:
            None
        """

        # Set the comment text
        self._comment_text = value

    @property
    def descendants(self) -> List[str]:
        """
        Returns the IDs of the descendant comments.

        Returns:
            List[str]: The IDs of the descendant comments.
        """

        # Return the list of descendant comment IDs
        return self._descendants

    @descendants.setter
    def descendants(
        self,
        value: Union[List[str], str],
    ) -> None:
        """
        Sets the IDs of the descendant comments.

        Args:
            value (Union[List[str], str]): The IDs of the descendant comments.

        Returns:
            None
        """

        # Check, if the 'descendants' list exists
        if not self.get(
            default=None,
            name="descendants",
        ):
            # Initialize the 'descendants' list
            self._descendants = []

        # Check, if the value is a string
        if isinstance(
            value,
            str,
        ):
            # Append the string to the 'descendants' list
            self._descendants.append(value)
        else:
            # Extend the 'descendants' list with the list of strings
            self._descendants.extend(value)

    @property
    def icon(self) -> str:
        """
        Returns the icon of the comment.

        Returns:
            str: The icon of the comment.
        """

        # Return the comment icon
        return self._icon

    @icon.setter
    def icon(
        self,
        value: str,
    ) -> None:
        """
        Sets the icon of the comment.

        Args:
            value (str): The icon of the comment.

        Returns:
            None
        """

        # Set the comment icon
        self._icon = value

    @property
    def id(self) -> int:
        """
        Returns the ID of the comment.

        Returns:
            int: The ID of the comment.
        """

        # Return the comment ID
        return self._id

    @id.setter
    def id(
        self,
        value: int,
    ) -> None:
        """
        Sets the ID of the comment.

        Args:
            value (int): The ID of the comment.

        Returns:
            None
        """

        # Set the comment ID
        self._id = value

    @property
    def key(self) -> str:
        """
        Returns the key of the comment.

        Returns:
            str: The key of the comment.
        """

        # Return the comment key
        return self._key

    @key.setter
    def key(
        self,
        value: str,
    ) -> None:
        """
        Sets the key of the comment.

        Args:
            value (str): The key of the comment.

        Returns:
            None
        """

        # Set the comment key
        self._key = value

    @property
    def last_edited_at(self) -> datetime:
        """
        Returns the timestamp when the comment was last edited.

        Returns:
            datetime: The timestamp when the comment was last edited.
        """

        # Return the timestamp when the comment was last edited
        return self._last_edited_at

    @last_edited_at.setter
    def last_edited_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the timestamp when the comment was last edited.

        Args:
            value (datetime): The timestamp when the comment was last edited.

        Returns:
            None
        """

        # Set the timestamp when the comment was last edited
        self._last_edited_at = value

    @property
    def metadata(self) -> Dict[str, Any]:
        """
        Returns the metadata of the comment.

        Returns:
            Dict[str, Any]: The metadata of the comment.
        """

        # Return the comment metadata
        return self._metadata

    @metadata.setter
    def metadata(
        self,
        **kwargs,
    ) -> None:
        """
        Sets the metadata of the comment.

        Args:
            value (Dict[str, Any]): The metadata of the comment.

        Returns:
            None
        """

        # Check, if the 'metadata' dictionary exists
        if not self.get(
            default=None,
            name="metadata",
        ):
            # Initialize the 'metadata' dictionary
            self._metadata = {}

        # Update the comment metadata
        self._metadata.update(**kwargs)

    @property
    def parent(self) -> str:
        """
        Returns the key of the parent object.

        Returns:
            str: The key of the parent object.
        """

        # Return the parent object key
        return self._parent

    @parent.setter
    def parent(
        self,
        value: str,
    ) -> None:
        """
        Sets the key of the parent object.

        Args:
            value (str): The key of the parent object.

        Returns:
            None
        """

        # Set the parent object key
        self._parent = value

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp when the comment was last updated.

        Returns:
            datetime: The timestamp when the comment was last updated.
        """

        # Return the timestamp when the comment was last updated
        return self._updated_at

    @updated_at.setter
    def updated_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the timestamp when the comment was last updated.

        Args:
            value (datetime): The timestamp when the comment was last updated.

        Returns:
            None
        """

        # Set the timestamp when the comment was last updated
        self._updated_at = value

    @property
    def uuid(self) -> str:
        """
        Returns the UUID of the comment.

        Returns:
            str: The UUID of the comment.
        """

        # Return the comment UUID
        return self._uuid

    @uuid.setter
    def uuid(
        self,
        value: str,
    ) -> None:
        """
        Sets the UUID of the comment.

        Args:
            value (str): The UUID of the comment.

        Returns:
            None
        """

        # Set the comment UUID
        self._uuid = value

    @property
    def version(self) -> int:
        """
        Returns the version of the comment.

        Returns:
            int: The version of the comment.
        """

        # Return the comment version
        return self._version

    @version.setter
    def version(
        self,
        value: int,
    ) -> None:
        """
        Sets the version of the comment.

        Args:
            value (int): The version of the comment.

        Returns:
            None
        """

        # Set the comment version
        self._version = value

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

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

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

    logger: Final[Logger] = Logger.get_logger(name="CommentConverter")

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

            # Log the traceback
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

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
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'object_to_model' method from '{cls.__name__}': {e}"
            )

            # Log the traceback
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None


class CommentFactory:
    """
    A factory class for creating CommentModel instances.

    This class extends the BaseObjectFactory class and provides a method to create CommentModel instances.

    Attributes:
        logger (Logger): The logger instance associated with the CommentFactory class.
    """

    logger: Final[Logger] = Logger.get_logger(name="CommentFactory")

    @classmethod
    def create_comment(
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
        metadata: Optional[Dict[str, Any]] = None,
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
            metadata (Optional[Dict[str, Any]]): The metadata of the comment.
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
                metadata=metadata,
                parent=parent,
                updated_at=updated_at,
                uuid=uuid,
                version=version,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_comment' method from '{cls.__name__}': {e}"
            )

            # Log the traceback
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None


class ComentBuilder(BaseObjectBuilder):
    """ """

    def __init__(self) -> None:
        """
        Initializes a new instance of the ComentBuilder class.

        Args:
            None

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    @override
    def build(
        self,
        as_mutable: bool = False,
    ) -> Optional[
        Union[
            ImmutableComment,
            MutableComment,
        ]
    ]:
        """
        Builds a new instance of the ImmutableComment class.

        Args:
            as_mutable (bool): A flag indicating whether to return the comment as a MutableComment instance.

        Returns:
            Optional[Union[ImmutableComment, MutableComment]]: The built ImmutableComment instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to build the ImmutableComment instance.
        """
        try:
            # Attempt to create a new ImmutableComment instance
            comment: Optional[ImmutableComment] = CommentFactory.create_comment(
                **self.configuration
            )

            # Check, if the comment exists
            if not comment:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create a new comment from '{self.configuration}'"
                )

                # Return early
                return

            # Check, if the 'as_mutable' attribute is True
            if as_mutable:
                # Return the comment as a MutableComment instance
                return comment.to_mutable()

            # Return the comment as an ImmutableComment instance
            return comment
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'build' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    def ancestor(
        self,
        value: int,
    ) -> Self:
        """
        Sets the 'ancestor' attribute of the builder.

        Args:
            value (int): The value to set for the 'ancestor' attribute.

        Returns:
            Self: The builder instance.
        """

        # Set the 'ancestor' attribute
        self.configuration["ancestor"] = value

        # Return the builder instance
        return self

    def comment_text(
        self,
        value: str,
    ) -> Self:
        """
        Sets the 'comment_text' attribute of the builder.

        Args:
            value (str): The value to set for the 'comment_text' attribute.

        Returns:
            Self: The builder instance.
        """

        # Set the 'comment_text' attribute
        self.configuration["comment_text"] = value

        # Return the builder instance
        return self

    def created_at(
        self,
        value: datetime,
    ) -> Self:
        """
        Sets the 'created_at' attribute of the builder.

        Args:
            value (datetime): The value to set for the 'created_at' attribute.

        Returns:
            Self: The builder instance.
        """

        # Set the 'created_at' attribute
        self.configuration["created_at"] = value

        # Return the builder instance
        return self

    def descendants(
        self,
        value: Union[List[str], str],
    ) -> Self:
        """
        Sets the 'descendants' attribute of the builder.

        Args:
            value (Union[List[str], str]): The value to set for the 'descendants' attribute.

        Returns:
            Self: The builder instance.
        """

        # Check, if the 'descendants' key exists in the configuration dictionary
        if "descendants" not in self.configuration:
            # Set the 'descendants' key to an empty list
            self.configuration["descendants"] = []

        # Check, if the value is a list
        if isinstance(
            value,
            list,
        ):
            # Extend the 'descendants' list with the new values
            self.configuration["descendants"].extend(value)
        else:
            # Append the new value to the 'descendants' list
            self.configuration["descendants"].append(value)

        # Return the builder instance
        return self

    def parent(
        self,
        value: str,
    ) -> Self:
        """
        Sets the 'parent' attribute of the builder.

        Args:
            value (str): The value to set for the 'parent' attribute.

        Returns:
            Self: The builder instance.
        """

        # Set the 'parent' attribute
        self.configuration["parent"] = value

        # Return the builder instance
        return self

    def updated_at(
        self,
        value: datetime,
    ) -> Self:
        """
        Sets the 'updated_at' attribute of the builder.

        Args:
            value (datetime): The value to set for the 'updated_at' attribute.

        Returns:
            Self: The builder instance.
        """

        # Set the 'updated_at' attribute
        self.configuration["updated_at"] = value

        # Return the builder instance
        return self

    def version(
        self,
        value: int,
    ) -> Self:
        """
        Sets the 'version' attribute of the builder.

        Args:
            value (int): The value to set for the 'version' attribute.

        Returns:
            Self: The builder instance.
        """

        # Set the 'version' attribute
        self.configuration["version"] = value

        # Return the builder instance
        return self


class CommentManager(BaseObjectManager):
    """
    A manager class for managing comments in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for comments.

    Attributes:
        cache: (List[Any]): The cache for storing comments.
        logger (Logger): The logger instance associated with the object.
    """

    _shared_instance: Optional["CommentManager"] = None

    def __new__(cls) -> "CommentManager":
        """
        Creates and returns a new instance of the CommentManager class.

        If the instance does not exist, creates a new one by calling the parent class
        constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Returns:
            CommentManager: The created or existing instance of CommentManager class.
        """

        # Check if the shared instance does not exist
        if cls._shared_instance is None:
            # Create a new instance by calling the parent class constructor
            cls._shared_instance = super(CommentManager, cls).__new__(cls)
            # Initialize the instance
            cls._shared_instance.init()

        # Return the shared instance
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes a new instance of the CommentManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def _run_pre_create_tasks(self, comment: Union[ImmutableComment, MutableComment,],) -> MutableComment:
        """
        Runs pre-create tasks for the comment.

        Args:
            comment (Union[ImmutableComment, MutableComment]): The comment to run pre-create tasks for.

        Returns:
            MutableComment: The comment with pre-create tasks run.
        """

        # Check, if the comment is not mutable
        if not comment.is_mutable():
            # Convert the comment to a MutableComment
            comment: MutableComment = comment.to_mutable()

        # Set the created_at timestamp of the comment
        comment.created_at = comment.created_at or Miscellaneous.get_current_datetime()

        # Set the custom_field_values of the comment
        comment.custom_field_values = [] or comment.custom_field_values

        # Set the key of the comment
        comment.key = f"COMMENT_{self.count_comments() + 1}"

        # Set the updated_at timestamp of the comment
        comment.updated_at = comment.updated_at or Miscellaneous.get_current_datetime()

        # Set the uuid of the comment
        comment.uuid = Miscellaneous.get_uuid()

        # Return the comment
        return comment

    def count_comments(self) -> int:
        """
        Returns the number of comments in the database.

        Returns:
            int: The number of comments in the database.
        """
        try:
            # Count and return the number of comments in the database
            return asyncio.run(CommentModel.count(database=Constants.DATABASE_PATH))
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
            # Initialize the result (optional) ImmutableComment to none
            result: Optional[ImmutableComment] = None

            # Run pre-create tasks
            comment: MutableComment = self._run_pre_create_tasks(
                comment=comment
            )

            # Convert the comment object to a CommentModel object
            model: CommentModel = CommentConverter.object_to_model(object=comment)

            # Create a new comment in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            # Check, if the ID is not None
            if not id:
                # Log a warning message indicating an error has occurred
                self.logger.warning(
                    message=f"It seems that an error has occured while attempting to create a comment ({comment.__repr__()}) in the database."
                )

                # Return early
                return

            # Convert the comment to a dictionary
            kwargs: Dict[str, Any] = comment.to_dict(
                exclude=[
                    "_logger",
                ]
            )

            # Set the ID of the comment
            kwargs["id"] = id

            # Create a new ImmutableComment object
            result = CommentFactory.create_comment(**kwargs)

            # Check, if the result is not None
            if not result:
                # Log an error message indicating an error has occurred
                self.logger.error(
                    message=f"It seems that there was an error while attempting to create an ImmutableComment from the dictionary ({kwargs}) returned by the database. This is likely a serious issue."
                )

                # Return early
                return

            # Add the comment to the cache
            self.add_to_cache(
                key=result.key,
                value=result,
            )

            # Return the newly created ImmutableComment instance
            return result
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
                    object=CommentFactory.create_comment(
                        **comment.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).delete()
            )

            # Remove the comment from the cache
            self.remove_from_cache(key=comment.key)

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
                CommentFactory.create_comment(
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
                # Add the immutable comment to the cache
                self.add_to_cache(
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
                comment: ImmutableComment = CommentFactory.create_comment(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the comment to the cache
                self.add_to_cache(
                    key=comment.key,
                    value=comment,
                )

                # Return the comment
                return comment
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
                comment: ImmutableComment = CommentFactory.create_comment(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the comment to the cache
                self.add_to_cache(
                    key=comment.key,
                    value=comment,
                )

                # Return the comment
                return comment
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
                return CommentFactory.create_comment(
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
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[Union[List[ImmutableComment]]]:
        """
        Searches for comments in the database.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            **kwargs: Any additional keyword arguments to be passed to the search method of the CommentModel class.

        Returns:
            Optional[Union[List[ImmutableComment]]]: The found comments if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Search the stack for the passed keyword arguments
                cached_result: Optional[List[ImmutableComment]] = self.search_cache(
                    **kwargs
                )

                # Check, if any cached results exist
                if cached_result:
                    # Return the cached results
                    return cached_result

            # Search for comments in the database
            models: Optional[List[CommentModel]] = asyncio.run(
                CommentModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found comments if any
            if models is not None and len(models) > 0:
                comments: List[ImmutableComment] = [
                    CommentFactory.create(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                    for model in models
                ]

                # Iterate over the found comments
                for comment in comments:
                    # Add the comment to the cache
                    self.add_to_cache(
                        key=comment.key,
                        value=comment,
                    )

                # Return the found comments
                return comments
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
            # Check if the comment object is immutable
            if isinstance(
                comment,
                ImmutableComment,
            ):
                # If it is, convert it to a mutable comment
                comment = comment.to_mutable()

            # Update the updated_at timestamp of the comment
            comment.updated_at = Miscellaneous.get_current_datetime()

            # Convert the comment to an immutable comment and update the comment in the database
            result: bool = asyncio.run(
                CommentConverter.object_to_model(
                    object=CommentFactory.create_comment(
                        **comment.to_dict(
                            exclude=[
                                "_logger",
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

            # Check, if the comment was updated successfully
            if result:
                # Update the comment in the cache
                self.update_in_cache(
                    key=comment.key,
                    value=comment,
                )

                # Return the updated comment
                return comment.to_immutable()
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
        last_edited_at (Optional[datetime]): The timestamp when the comment was last edited.
        metadata (Optional[Dict[str, Any]]): The metadata of the comment.
        priority (Optional[int]): The priority of the comment.
        status (Optional[int]): The status of the comment.
        updated_at (Optional[datetime]): The timestamp when the comment was last updated.
        uuid (Optional[str]): The UUID of the comment.
    """

    table: Final[str] = Constants.COMMENTS

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

    last_edited_at: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="last_edited_at",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="DATETIME",
        unique=False,
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
        default=1,
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
        metadata: Optional[Dict[str, Any]] = None,
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
            metadata (Optional[Dict[str, Any]]): The metadata of the comment.
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
            metadata=metadata,
            parent=parent,
            updated_at=updated_at,
            uuid=uuid,
            version=version,
        )
