"""
Author: lodego
Date: 2025-02-08
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
            updated_at (Optional[datetime]): The timestamp when the tag was last updated.
            uuid (Optional[str]): The UUID of the tag.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            icon=icon,
            id=id,
            key=key,
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )

    def to_mutable(self) -> "MutableTag":
        """
        Converts the immutable tag to a mutable tag.

        Returns:
            MutableTag: The mutable tag.
        """
        return MutableTag(**self.to_dict(exclude=["_logger"]))


class MutableTag(MutableBaseObject):
    """
    A mutable class representing a tag.

    Attributes:
        created_at (datetime): The timestamp when the tag was created.
        icon (str): The icon of the tag.
        id (int): The ID of the tag.
        key (str): The key of the tag.
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
            updated_at (Optional[datetime]): The timestamp when the tag was last updated.
            uuid (Optional[str]): The UUID of the tag.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            icon=icon,
            id=id,
            key=key,
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )

    def to_immutable(self) -> ImmutableTag:
        """
        Returns an immutable copy of the MutableTag instance.

        Returns:
            ImmutableTag: A immutable copy of the MutableTag instance.
        """

        # Create a new ImmutableTag instance from the dictionary representation of the MutableTag instance
        return ImmutableTag(**self.to_dict(exclude=["_logger"]))


class TagConverter:
    """
    A converter class for transforming between TagModel and ImmutableTag instances.

    This class provides methods to convert a TagModel instance to an ImmutableTag instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the TagConverter class.
    """

    logger: Logger = Logger.get_logger(name="TagConverter")

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
            return TagModel(**object.to_dict(exclude=["_logger"]))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'object_to_model' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class TagFactory:
    """
    A factory class for creating instances of the Tag class.

    Attributes:
        logger (Logger): The logger instance associated with the TagFactory class.
    """

    logger: Logger = Logger.get_logger(name="TagFactory")

    @classmethod
    def create_tag(
        cls,
        value: str,
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "🔖",
        id: Optional[int] = None,
        key: Optional[str] = None,
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
                updated_at=updated_at,
                uuid=uuid,
                value=value,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_tag' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


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

    def count_tags(self) -> int:
        """
        Returns the number of tags in the database.

        Returns:
            int: The number of tags in the database.
        """
        try:
            # Count the number of tags in the database
            result: Any = asyncio.run(
                TagModel.execute(
                    database=Constants.DATABASE_PATH,
                    sql=f"SELECT COUNT(*) FROM {Constants.TAGS};",
                )
            )

            # Return the number of tags in the database
            return result[0][0] if result else 0
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
            # Check if the tag object is immutable
            if isinstance(
                tag,
                ImmutableTag,
            ):
                # If it is, convert it to a mutable tag
                tag = MutableTag(**tag.to_dict(exclude=["_logger"]))

            # Set the created_at timestamp of the tag
            tag.created_at = Miscellaneous.get_current_datetime()

            # Set the key of the tag
            tag.key = f"TAG_{self.count_tags() + 1}"

            # Set the updated_at timestamp of the tag
            tag.updated_at = Miscellaneous.get_current_datetime()

            # Set the uuid of the tag
            tag.uuid = Miscellaneous.get_uuid()

            # Convert the tag object to a TagModel object
            model: TagModel = TagConverter.object_to_model(object=tag)

            # Create a new tag in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            if id:
                # Set the ID of the tag
                tag.id = id

                # Convert the tag to an immutable tag
                tag = ImmutableTag(**tag.to_dict(exclude=["_logger"]))

                # Add the tag to the cache
                self.add_to_cache(
                    key=tag.key,
                    value=tag,
                )

                # Return the newly created immutable tag
                return tag

            # Log a warning message indicating an error has occurred
            self.logger.warning(
                message=f"It seems that an error has occured while attempting to create a tag ({tag}) in the database."
            )

            # Return None indicating an error has occurred
            return None
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
                    object=ImmutableTag(**tag.to_dict(exclude=["_logger"]))
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
        **kwargs,
    ) -> Optional[Union[List[ImmutableTag]]]:
        """
        Searches for tags in the database.

        Args:
            **kwargs: Any additional keyword arguments to be passed to the search method of the TagModel class.

        Returns:
            Optional[Union[List[ImmutableTag]]]: The found tags if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
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
                    object=ImmutableTag(**tag.to_dict(exclude=["_logger"]))
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
        updated_at (Field): The timestamp when the tag was last updated.
        uuid (Field): The UUID of the tag.
        value (Field): The value of the tag.
    """

    table: str = Constants.TAGS

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
            table=Constants.TAGS,
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )
