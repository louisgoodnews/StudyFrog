"""
Author: lodego
Date: 2025-02-08
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
    "ImmutableTag",
    "MutableTag",
    "TagConverter",
    "TagFactory",
    "TagManager",
    "TagModel",
]


class ImmutableTag(ImmutableBaseObject):
    """
    An immutable class representing a tag.

    Attributes:
        created_at (datetime): The timestamp when the tag was created.
        icon (str): The icon of the tag.
        id (int): The ID of the tag.
        key (str): The key of the tag.
        metadata (Optional[Dict[str, Any]]): The metadata of the tag.
        updated_at (datetime): The timestamp when the tag was last updated.
        uuid (str): The UUID of the tag.
        value (str): The value of the tag.
    """

    def __init__(
        self,
        value: str,
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "🔖",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableTag class.

        Args:
            value (str): The value of the tag.
            created_at (Optional[datetime]): The timestamp when the tag was created.
            icon (Optional[str]): The icon of the tag. Defaults to "🔖".
            id (Optional[int]): The ID of the tag.
            key (Optional[str]): The key of the tag.
            metadata (Optional[Dict[str, Any]]): The metadata of the tag.
            updated_at (Optional[datetime]): The timestamp when the tag was last updated.
            uuid (Optional[str]): The UUID of the tag.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            hide_attributes=True,
            icon=icon,
            id=id,
            key=key,
            metadata=metadata,
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )

    @property
    def created_at(self) -> datetime:
        """
        Returns the timestamp when the tag was created.

        Returns:
            datetime: The timestamp when the tag was created.
        """

        # Return the created_at attribute
        return self._created_at

    @property
    def icon(self) -> str:
        """
        Returns the icon of the tag.

        Returns:
            str: The icon of the tag.
        """

        # Return the icon attribute
        return self._icon

    @property
    def id(self) -> int:
        """
        Returns the ID of the tag.

        Returns:
            int: The ID of the tag.
        """

        # Return the id attribute
        return self._id

    @property
    def key(self) -> str:
        """
        Returns the key of the tag.

        Returns:
            str: The key of the tag.
        """

        # Return the key attribute
        return self._key

    @property
    def metadata(self) -> Dict[str, Any]:
        """
        Returns the metadata of the tag.

        Returns:
            Dict[str, Any]: The metadata of the tag.
        """

        # Return the metadata attribute
        return self._metadata

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp when the tag was last updated.

        Returns:
            datetime: The timestamp when the tag was last updated.
        """

        # Return the updated_at attribute
        return self._updated_at

    @property
    def uuid(self) -> str:
        """
        Returns the UUID of the tag.

        Returns:
            str: The UUID of the tag.
        """

        # Return the uuid attribute
        return self._uuid

    @property
    def value(self) -> str:
        """
        Returns the value of the tag.

        Returns:
            str: The value of the tag.
        """

        # Return the value attribute
        return self._value

    def to_mutable(self) -> "MutableTag":
        """
        Converts the immutable tag to a mutable tag.

        Args:
            None

        Returns:
            MutableTag: The mutable tag.

        Raises:
            Exception: If an exception occurs while attempting to convert the ImmutableTag instance.
        """
        try:
            # Attempt to create and return a new instance of the MutableTag class from the dictionary representation of the current ImmutableTag instance
            return MutableTag(
                **self.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_mutable' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating that an exception has occurred
            return None


class MutableTag(MutableBaseObject):
    """
    A mutable class representing a tag.

    Attributes:
        created_at (datetime): The timestamp when the tag was created.
        icon (str): The icon of the tag.
        id (int): The ID of the tag.
        key (str): The key of the tag.
        metadata (Optional[Dict[str, Any]]): The metadata of the tag.
        updated_at (datetime): The timestamp when the tag was last updated.
        uuid (str): The UUID of the tag.
        value (str): The value of the tag.
    """

    def __init__(
        self,
        value: str,
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "🔖",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableTag class.

        Args:
            value (str): The value of the tag.
            created_at (Optional[datetime]): The timestamp when the tag was created.
            icon (Optional[str]): The icon of the tag. Defaults to "🔖".
            id (Optional[int]): The ID of the tag.
            key (Optional[str]): The key of the tag.
            metadata (Optional[Dict[str, Any]]): The metadata of the tag.
            updated_at (Optional[datetime]): The timestamp when the tag was last updated.
            uuid (Optional[str]): The UUID of the tag.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            hide_attributes=True,
            icon=icon,
            id=id,
            key=key,
            metadata=metadata,
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )

    @property
    def created_at(self) -> datetime:
        """
        Returns the timestamp when the tag was created.

        Returns:
            datetime: The timestamp when the tag was created.
        """

        # Return the created_at attribute
        return self._created_at

    @created_at.setter
    def created_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the timestamp when the tag was created.

        Args:
            value (datetime): The timestamp when the tag was created.

        Returns:
            None
        """

        # Set the created_at attribute
        self._created_at = value

    @property
    def icon(self) -> str:
        """
        Returns the icon of the tag.

        Returns:
            str: The icon of the tag.
        """

        # Return the icon attribute
        return self._icon

    @icon.setter
    def icon(
        self,
        value: str,
    ) -> None:
        """
        Sets the icon of the tag.

        Args:
            value (str): The icon of the tag.

        Returns:
            None
        """

        # Set the icon attribute
        self._icon = value

    @property
    def id(self) -> int:
        """
        Returns the ID of the tag.

        Returns:
            int: The ID of the tag.
        """

        # Return the id attribute
        return self._id

    @id.setter
    def id(
        self,
        value: int,
    ) -> None:
        """
        Sets the ID of the tag.

        Args:
            value (int): The ID of the tag.

        Returns:
            None
        """

        # Set the id attribute
        self._id = value

    @property
    def key(self) -> str:
        """
        Returns the key of the tag.

        Returns:
            str: The key of the tag.
        """

        # Return the key attribute
        return self._key

    @key.setter
    def key(
        self,
        value: str,
    ) -> None:
        """
        Sets the key of the tag.

        Args:
            value (str): The key of the tag.

        Returns:
            None
        """

        # Set the key attribute
        self._key = value

    @property
    def metadata(self) -> Dict[str, Any]:
        """
        Returns the metadata of the tag.

        Returns:
            Dict[str, Any]: The metadata of the tag.
        """

        # Return the metadata attribute
        return self._metadata

    @metadata.setter
    def metadata(
        self,
        **kwargs,
    ) -> None:
        """
        Updates the metadata of the tag.

        Args:
            **kwargs (Dict[str, Any]): The new metadata of the tag.

        Returns:
            None
        """

        # Check, if the metadata dictionary exists
        if not self.get(
            default=None,
            name="metadata",
        ):
            # Set the metadata of the tag to an empty dictionary
            self._metadata = {}

        # Update the metadata of the tag
        self._metadata.update(**kwargs)

    @property
    def updated_at(self) -> datetime:
        """
        Returns the timestamp when the tag was last updated.

        Returns:
            datetime: The timestamp when the tag was last updated.
        """

        # Return the updated_at attribute
        return self._updated_at

    @updated_at.setter
    def updated_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the timestamp when the tag was last updated.

        Args:
            value (datetime): The timestamp when the tag was last updated.

        Returns:
            None
        """

        # Set the updated_at attribute
        self._updated_at = value

    @property
    def uuid(self) -> str:
        """
        Returns the UUID of the tag.

        Returns:
            str: The UUID of the tag.
        """

        # Return the uuid attribute
        return self._uuid

    @uuid.setter
    def uuid(
        self,
        value: str,
    ) -> None:
        """
        Sets the UUID of the tag.

        Args:
            value (str): The UUID of the tag.

        Returns:
            None
        """

        # Set the uuid attribute
        self._uuid = value

    @property
    def value(self) -> str:
        """
        Returns the value of the tag.

        Returns:
            str: The value of the tag.
        """

        # Return the value attribute
        return self._value

    @value.setter
    def value(
        self,
        value: str,
    ) -> None:
        """
        Sets the value of the tag.

        Args:
            value (str): The value of the tag.

        Returns:
            None
        """

        # Set the value attribute
        self._value = value

    def to_immutable(self) -> ImmutableTag:
        """
        Returns an immutable copy of the MutableTag instance.

        Returns:
            ImmutableTag: A immutable copy of the MutableTag instance.
        """
        try:
            # Create a new ImmutableTag instance from the dictionary representation of the MutableTag instance
            return ImmutableTag(
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

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None


class TagConverter:
    """
    A converter class for transforming between TagModel and ImmutableTag instances.

    This class provides methods to convert a TagModel instance to an ImmutableTag instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the TagConverter class.
    """

    logger: Final[Logger] = Logger.get_logger(name="TagConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "TagModel",
    ) -> Optional[ImmutableTag]:
        """
        Converts a given TagModel instance to an ImmutableTag instance.

        Args:
            model (TagModel): The TagModel instance to be converted.

        Returns:
            ImmutableTag: The converted ImmutableTag instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the TagModel instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableTag class from the dictionary representation of the TagModel instance
            return ImmutableTag(
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
        object: ImmutableTag,
    ) -> Optional["TagModel"]:
        """
        Converts a given ImmutableTag instance to a TagModel instance.

        Args:
            object (ImmutableTag): The ImmutableTag instance to be converted.

        Returns:
            TagModel: The converted TagModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ImmutableTag instance.
        """
        try:
            # Attempt to create and return a new instance of the TagModel class from the dictionary representation of the ImmutableTag instance
            return TagModel(
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


class TagFactory:
    """
    A factory class for creating instances of the Tag class.

    Attributes:
        logger (Logger): The logger instance associated with the TagFactory class.
    """

    logger: Final[Logger] = Logger.get_logger(name="TagFactory")

    @classmethod
    def create_tag(
        cls,
        value: str,
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "🔖",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutableTag]:
        """
        Creates a new instance of the Tag class.

        Args:
            value (str): The value of the tag.
            created_at (Optional[datetime]): The timestamp when the tag was created.
            icon (Optional[str]): The icon of the tag. Defaults to "🔖".
            id (Optional[int]): The ID of the tag.
            key (Optional[str]): The key of the tag.
            metadata (Optional[Dict[str, Any]]): The metadata of the tag.
            updated_at (Optional[datetime]): The timestamp when the tag was last updated.
            uuid (Optional[str]): The UUID of the tag.

        Returns:
            Optional[ImmutableTag]: A new instance of the Tag class, or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create the Tag instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableTag class
            return ImmutableTag(
                created_at=created_at,
                icon=icon,
                id=id,
                key=key,
                metadata=metadata,
                updated_at=updated_at,
                uuid=uuid,
                value=value,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_tag' method from '{cls.__name__}': {e}"
            )

            # Log the traceback
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None


class TagBuilder(BaseObjectBuilder):
    """ """

    def __init__(self) -> None:
        """
        Initializes a new instance of the TagBuilder class.

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
            ImmutableTag,
            MutableTag,
        ]
    ]:
        """
        Builds a new instance of the Tag class.

        Args:
            as_mutable (bool): Whether to return the tag as a MutableTag instance. Defaults to False.

        Returns:
            Optional[Union[ImmutableTag, MutableTag]]: A new instance of the Tag class, or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to build the Tag instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableTag class
            tag: Optional[ImmutableTag] = TagFactory.create_tag(**self.configuration)

            # Check, if the tag exists
            if not tag:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create tag from configuration: {self.configuration}"
                )

                # Return early
                return None

            # Check, if the tag should be mutable
            if as_mutable:
                # Return the tag as MutableTag instance
                return tag.to_mutable()

            # Return the tag
            return tag
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'build' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None indicating an exception has occurred
            return None

    def created_at(
        self,
        value: datetime,
    ) -> Self:
        """
        Sets the created_at value.

        Args:
            value (datetime): The created_at value to set.

        Returns:
            Self: The builder instance.
        """

        # Set the created_at value
        self.configuration["created_at"] = value

        # Return self
        return self

    def metadata(
        self,
        value: Dict[str, Any],
    ) -> Self:
        """
        Sets the metadata of the tag.

        Args:
            value (Dict[str, Any]): The metadata of the tag.

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

    def updated_at(
        self,
        value: datetime,
    ) -> Self:
        """
        Sets the updated_at value.

        Args:
            value (datetime): The updated_at value to set.

        Returns:
            Self: The builder instance.
        """

        # Set the updated_at value in the configuration dictionary
        self.configuration["updated_at"] = value

        # Return the builder instance
        return self

    def value(
        self,
        value: str,
    ) -> Self:
        """
        Sets the value of the tag.

        Args:
            value (str): The value of the tag.

        Returns:
            Self: The builder instance.
        """

        # Set the value in the configuration dictionary
        self.configuration["value"] = value

        # Return the builder instance
        return self


class TagManager(BaseObjectManager):
    """
    A manager class for managing tags in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for tags.

    Attributes:
        cache: (List[Any]): The cache for storing tags.
        logger (Logger): The logger instance associated with the object.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the TagManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def _run_pre_create_tasks(
        self,
        tag: Union[
            ImmutableTag,
            MutableTag,
        ],
    ) -> MutableTag:
        """
        Runs pre-create tasks for the tag.

        Args:
            tag (Union[ImmutableTag, MutableTag]): The tag to run pre-create tasks for.

        Returns:
            MutableTag: The tag with pre-create tasks run.
        """

        # Check, if the tag is immutable
        if not tag.is_mutable():
            # Convert the tag to mutable
            tag: MutableTag = tag.to_mutable()

        # Set the created_at timestamp of the tag
        tag.created_at = tag.created_at or Miscellaneous.get_current_datetime()

        # Set the key of the tag
        tag.key = f"TAG_{self.count_tags() + 1}"

        # Set the updated_at timestamp of the tag
        tag.updated_at = tag.updated_at or Miscellaneous.get_current_datetime()

        # Set the uuid of the tag
        tag.uuid = Miscellaneous.get_uuid()

        # Return the tag
        return tag

    def count_tags(self) -> int:
        """
        Returns the number of tags in the database.

        Returns:
            int: The number of tags in the database.
        """
        try:
            # Count and return the number of tags in the database
            return asyncio.run(TagModel.count(database=Constants.DATABASE_PATH))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_tag(
        self,
        tag: Union[ImmutableTag, MutableTag],
    ) -> Optional[ImmutableTag]:
        """
        Creates a new tag in the database.

        Args:
            tag (Union[ImmutableTag, MutableTag]): The tag to be created.

        Returns:
            Optional[ImmutableTag]: The newly created immutable tag if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the tag.
        """
        try:
            
            # Initialize the result (optional) ImmutableTag to none
            result: Optional[ImmutableTag] = None

            # Run pre-create tasks
            tag: MutableTag = self._run_pre_create_tasks(
                tag=tag
            )

            # Convert the tag object to a TagModel object
            model: TagModel = TagConverter.object_to_model(object=tag)

            # Create a new tag in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            # Check, if the ID is not None
            if not id:
                # Log a warning message indicating an error has occurred
                self.logger.warning(
                    message=f"It seems that an error has occured while attempting to create a tag ({tag.__repr__()}) in the database."
                )

                # Return early
                return

            # Convert the tag to a dictionary
            kwargs: Dict[str, Any] = tag.to_dict(
                exclude=[
                    "_logger",
                ]
            )

            # Set the ID of the tag
            kwargs["id"] = id

            # Create a new ImmutableTag object
            result = TagFactory.create_tag(**kwargs)

            # Check, if the result is not None
            if not result:
                # Log an error message indicating an error has occurred
                self.logger.error(
                    message=f"It seems that there was an error while attempting to create an ImmutableTag from the dictionary ({kwargs}) returned by the database. This is likely a serious issue."
                )

                # Return early
                return

            # Add the tag to the cache
            self.add_to_cache(
                key=result.key,
                value=result,
            )

            # Return the newly created ImmutableTag instance
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_tag' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete_tag(
        self,
        tag: Union[ImmutableTag, MutableTag],
    ) -> bool:
        """
        Deletes a tag from the database.

        Args:
            tag (Union[ImmutableTag, MutableTag]): The tag to be deleted.

        Returns:
            bool: True if the tag was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the tag to an immutable tag and delete the tag from the database
            result: bool = asyncio.run(
                TagConverter.object_to_model(
                    object=ImmutableTag(
                        **tag.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).delete()
            )

            # Return True if the tag was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all_tags(self) -> Optional[List[ImmutableTag]]:
        """
        Returns a list of all tags in the database.

        Returns:
            Optional[List[ImmutableTag]]: A list of all tags in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if cache and table size are equal
            if self.cache and len(self._cache) == self.count_tags():
                # Return the list of immutable tags from the cache
                return self.get_cache_values()

            # Get all tags from the database
            models: List[TagModel] = asyncio.run(
                TagModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of TagModel objects to a list of ImmutableTag objects
            tags: List[ImmutableTag] = [
                ImmutableTag(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable tags
            for tag in tags:
                if not self.is_key_in_cache(key=tag.key):
                    # Add the immutable tag to the cache
                    self.add_to_cache(
                        key=tag.key,
                        value=tag,
                    )
                else:
                    # Update the immutable tag in the cache
                    self.update_in_cache(
                        key=tag.key,
                        value=tag,
                    )

            # Return the list of immutable tags
            return tags
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_from_tags(
        self,
        condition: Callable[[ImmutableTag], bool],
        limit: Optional[int] = None,
    ) -> Optional[List[ImmutableTag]]:
        """
        Returns a list of tags from the cache that match the given condition.

        Args:
            condition (Callable[[ImmutableTag], bool]): A function that takes an ImmutableTag instance and returns a boolean value.
            limit (Optional[int]): The maximum number of tags to return.

        Returns:
            Optional[List[ImmutableTag]]: The list of tags that match the given condition if no exception occurs. Otherwise, None.
        """
        try:
            # Initialize an empty list to store matching tags
            result: List[ImmutableTag] = []

            # Get all tags from the cache
            tags: List[ImmutableTag] = self.get_all_tags()

            # Iterate over the list of immutable tags in the cache
            for tag in tags:
                # Check if the tag matches the given condition
                if condition(tag):
                    # Add the tag that matches the given condition to the result list
                    result.append(tag)

            # Check if the limit is specified and if the result list exceeds the limit
            if limit is not None and len(result) > limit:
                # Return the first 'limit' number of tags
                return result[:limit]

            # Return the list of matching tags
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_from_tags' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_tag_by(
        self,
        field: str,
        value: Any,
    ) -> Optional[ImmutableTag]:
        """
        Returns a tag with the given field and value.

        Args:
            field (str): The field to search for.
            value (Any): The value to search for.

        Returns:
            Optional[ImmutableTag]: The tag with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Get the tag with the given field and value from the database
            model: Optional[TagModel] = asyncio.run(
                TagModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Convert the TagModel object to an ImmutableTag object
            tag: Optional[ImmutableTag] = TagConverter.model_to_object(model=model)

            # Return the tag if it exists
            if model is not None:
                # Return the tag
                return tag
            else:
                # Return None indicating that the tag does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_tag_by_id(
        self,
        id: int,
    ) -> Optional[ImmutableTag]:
        """
        Returns a tag with the given ID.

        Args:
            id (int): The ID of the tag.

        Returns:
            Optional[ImmutableTag]: The tag with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the tag is already in the cache
            if self.is_key_in_cache(key=f"TAG_{id}"):
                # Return the tag from the cache
                return self.get_value_from_cache(key=f"TAG_{id}")

            # Get the tag with the given ID from the database
            model: Optional[TagModel] = asyncio.run(
                TagModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the tag if it exists
            if model is not None:
                # Convert the TagModel object to an ImmutableTag object
                return ImmutableTag(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the tag does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_tag_by_uuid(
        self,
        uuid: str,
    ) -> Optional[ImmutableTag]:
        """
        Returns a tag with the given UUID.

        Args:
            uuid (str): The UUID of the tag.

        Returns:
            Optional[ImmutableTag]: The tag with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the tag is already in the cache
            if self.is_key_in_cache(key=uuid):
                # Return the tag from the cache
                return self.get_value_from_cache(key=uuid)

            # Get the tag with the given UUID from the database
            model: Optional[TagModel] = asyncio.run(
                TagModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the tag if it exists
            if model is not None:
                # Convert the TagModel object to an ImmutableTag object
                return ImmutableTag(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the tag does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def search_tags(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[Union[List[ImmutableTag]]]:
        """
        Searches for tags in the database.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            **kwargs: Any additional keyword arguments to be passed to the search method of the TagModel class.

        Returns:
            Optional[Union[List[ImmutableTag]]]: The found tags if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Search the stack for the passed keyword arguments
                cached_result: Optional[List[ImmutableTag]] = self.search_cache(
                    **kwargs
                )

                # Check, if any cached results exist
                if cached_result:
                    # Return the cached results
                    return cached_result

            # Search for tags in the database
            models: Optional[List[TagModel]] = asyncio.run(
                TagModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found tags if any
            if models is not None and len(models) > 0:
                return [
                    ImmutableTag(
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
                # Return None indicating that no tags were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_tag(
        self,
        tag: Union[ImmutableTag, MutableTag],
    ) -> Optional[ImmutableTag]:
        """
        Updates a tag with the given ID.

        Args:
            tag (Union[ImmutableTag, MutableTag]): The tag to update.

        Returns:
            Optional[ImmutableTag]: The updated tag if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the tag to an immutable tag and update the tag in the database
            model: Optional[TagModel] = asyncio.run(
                TagConverter.object_to_model(
                    object=ImmutableTag(
                        **tag.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).update(
                    database=Constants.DATABASE_PATH,
                    **tag.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Return the updated tag if it exists
            if model is not None:
                # Convert the TagModel object to an ImmutableTag object
                tag = ImmutableTag(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the tag to the cache
                self.update_in_cache(
                    key=tag.key,
                    value=tag,
                )

                # Return the updated tag
                return tag
            else:
                # Return None indicating that the tag does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class TagModel(ImmutableBaseModel):
    """
    Represents the structure of a tag model.

    Attributes:
        table (str): The table name of the tag model.
        id (Field): The ID of the tag.
        created_at (Field): The timestamp when the tag was created.
        icon (Field): The icon of the tag. Defaults to "🔖".
        key (Field): The key of the tag.
        metadata (Field): The metadata of the tag.
        updated_at (Field): The timestamp when the tag was last updated.
        uuid (Field): The UUID of the tag.
        value (Field): The value of the tag.
    """

    table: Final[str] = Constants.TAGS

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

    icon: Field = Field(
        autoincrement=False,
        default="🔖",
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

    value: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="value",
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
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "🔖",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
        value: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the TagModel class.

        Args:
            created_at (Optional[datetime]): The timestamp when the tag was created.
            icon (Optional[str]): The icon of the tag. Defaults to "🔖".
            id (Optional[int]): The ID of the tag.
            key (Optional[str]): The key of the tag.
            metadata (Optional[Dict[str, Any]]): The metadata of the tag.
            updated_at (Optional[datetime]): The timestamp when the tag was last updated.
            uuid (Optional[str]): The UUID of the tag.
            value (Optional[str]): The value of the tag.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            icon="🔖",
            id=id,
            key=key,
            metadata=metadata,
            table=Constants.TAGS,
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )
