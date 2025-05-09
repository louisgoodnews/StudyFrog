"""
Author: lodego
Date: 2025-02-05
"""

import asyncio
import json
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
    "ImmutableStack",
    "MutableStack",
    "StackConverter",
    "StackFactory",
    "StackBuilder",
    "StackManager",
    "StackModel",
]


class ImmutableStack(ImmutableBaseObject):
    """
    An immutable class representing a stack.

    A stack is a collection of Flashards, Notes and Questions.

    Attributes:
        ancestor (int): The ID of the ancestor stack.
        contents (List[Dict[str, Any]]): The list of the contents of the stack.
        created_at (datetime): The timestamp when the stack was created.
        custom_field_values (List[Dict[str, Any]]): The custom field values of the stack.
        descendants (List[str]): The keys of the descendants stacks.
        description (str): The description of the stack.
        difficulty (int): The difficulty of the stack.
        due_by (datetime): The timestamp when the stack is due.
        icon (str): The icon of the stack.
        id (int): The ID of the stack.
        key (str): The key of the stack.
        last_viewed_at (datetime): The timestamp when the stack was last viewed.
        metadata (Dict[str, Any]): The metadata of the stack.
        name (str): The name of the stack.
        priority (int): The priority of the stack.
        status (int): The status of the stack.
        subject (int): The ID of the subject the stack is associated with.
        tags (List[str]): The keys of the tags associated with the stack.
        updated_at (datetime): The timestamp when the stack was last updated.
        uuid (str): The UUID of the stack.
    """

    def __init__(
        self,
        name: str,
        ancestor: Optional[int] = None,
        contents: Optional[List[str]] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        descendants: Optional[List[str]] = None,
        description: Optional[str] = None,
        difficulty: Optional[int] = None,
        due_by: Optional[datetime] = None,
        icon: Optional[str] = "📚",
        id: Optional[int] = None,
        key: Optional[str] = None,
        last_viewed_at: Optional[datetime] = None,
        metadata: Optional[Dict[str, Any]] = None,
        priority: Optional[int] = None,
        status: Optional[int] = None,
        subject: Optional[int] = None,
        tags: Optional[List[str]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableStack class.

        Args:
            name (str): The name of the stack.
            ancestor (Optional[int]): The ID of the ancestor stack.
            contents(Optional[List[str]]): The list of the contents of the stack.
            created_at (Optional[datetime]): The timestamp when the stack was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): The custom field values of the stack.
            descendants (Optional[List[str]]): The keys of the descendants stacks.
            description (Optional[str]): The description of the stack.
            difficulty (Optional[int]): The ID of the difficulty associated with the stack.
            due_by (Optional[datetime]): The timestamp when the stack is due.
            icon (Optional[str]): The icon of the stack. Defaults to "📚".
            id (Optional[int]): The ID of the stack.
            key (Optional[str]): The key of the stack.
            last_viewed_at (Optional[datetime]): The timestamp when the stack was last viewed.
            metadata (Optional[Dict[str, Any]]): The metadata of the stack.
            priority (Optional[int]): The ID of the priority associated with the stack.
            status (Optional[int]): The ID of the status associated with the stack.
            subject (Optional[int]): The ID of the subject the stack is associated with.
            tags (Optional[List[str]]): The keys of the tags associated with the stack.
            updated_at (Optional[datetime]): The timestamp when the stack was last updated.
            uuid (Optional[str]): The UUID of the stack.
        """

        # Call the parent class constructor
        super().__init__(
            ancestor=ancestor,
            contents=contents,
            created_at=created_at,
            custom_field_values=custom_field_values,
            descendants=descendants,
            description=description,
            difficulty=difficulty,
            due_by=due_by,
            icon=icon,
            id=id,
            key=key,
            last_viewed_at=last_viewed_at,
            metadata=metadata,
            name=name,
            priority=priority,
            status=status,
            subject=subject,
            tags=tags,
            updated_at=updated_at,
            uuid=uuid,
        )

    def get_content_grouped_by(
        self,
        type_key: Literal[
            "flashcard",
            "note",
            "question",
        ],
    ) -> List[str]:
        """
        Returns a list of the contents of the stack grouped by the given key.

        Args:
            type_key (Literal["flashcard", "note", "question"]): The key to group the contents by.

        Returns:
            List[str]: A list of the contents of the stack grouped by the given key.
        """

        # Check if the stack has content
        if not self.has_contents():
            # Return an empty list if the stack has no content
            return []

        # Return the list of the contents of the stack grouped by the given key
        return [
            key
            for key in self.get(
                default=[],
                name="contents",
            )
            if key.lower().startswith(type_key)
        ]

    def has_ancestor(self) -> bool:
        """
        Returns True if the stack has an ancestor, False otherwise.

        Returns:
            bool: True if the stack has an ancestor, False otherwise.
        """

        # Check if the stack has an ancestor
        return self.ancestor is not None

    def has_contents(self) -> bool:
        """
        Returns True if the stack has contents, False otherwise.

        Returns:
            bool: True if the stack has contents, False otherwise.
        """

        # Check if the stack has contents
        return self.contents is not None and len(self.contents) > 0

    def has_descendants(self) -> bool:
        """
        Returns True if the stack has descendants, False otherwise.

        Returns:
            bool: True if the stack has descendants, False otherwise.
        """

        # Check if the stack has descendants
        return self.descendants is not None and len(self.descendants) > 0

    def is_ancestor_of(
        self,
        key: str,
    ) -> bool:
        """
        Returns True if the stack is an ancestor of the given key, False otherwise.

        Args:
            key (str): The key of the stack.

        Returns:
            bool: True if the stack is an ancestor of the given key, False otherwise.
        """

        # Check if the stack has descendants
        if not self.has_descendants():
            # Return False if the stack has no descendants
            return False

        # Check if the stack is an ancestor of the given key
        return key in self.descendants

    def is_content_of(
        self,
        key: str,
    ) -> bool:
        """
        Returns True if the given key is a content of the stack, False otherwise.

        Args:
            key (str): The key of the content.

        Returns:
            bool: True if the given key is a content of the stack, False otherwise.
        """

        # Check if the stack has content
        if not self.has_contents():
            # Return False if the stack has no content
            return False

        # Check if the stack is a content of the given key
        return key in self.contents

    def is_descendant_of(
        self,
        key: str,
    ) -> bool:
        """
        Returns True if the stack is a descendant of the given key, False otherwise.

        Args:
            key (str): The key of the stack.

        Returns:
            bool: True if the stack is a descendant of the given key, False otherwise.
        """

        # Check if the stack has an ancestor
        if not self.has_ancestor():
            # Return False if the stack has no ancestor
            return False

        # Check if the stack is a descendant of the given key
        return key == self.ancestor

    def to_mutable(self) -> "MutableStack":
        """
        Returns a mutable copy of the ImmuutableStack instance.

        Returns:
            MutableStack: A mutable copy of the ImmuutableStack instance.
        """
        try:
            # Create a new MutableStack instance from the dictionary representation of the ImmutableStack instance
            return MutableStack(
                **self.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_mutable' method from '{self.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None


class MutableStack(MutableBaseObject):
    """
    A mutable class representing a stack.

    A stack is a collection of Flashards, Notes and Questions.

    Attributes:
        ancestor (int): The ID of the ancestor stack.
        contents (List[Dict[str, Any]]): The list of the contents of the stack.
        created_at (datetime): The timestamp when the stack was created.
        custom_field_values (List[Dict[str, Any]]): The custom field values of the stack.
        descendants (List[str]): The keys of the descendants stacks.
        description (str): The description of the stack.
        difficulty (int): The difficulty of the stack.
        due_by (datetime): The timestamp when the stack is due.
        icon (str): The icon of the stack.
        id (int): The ID of the stack.
        key (str): The key of the stack.
        last_viewed_at (datetime): The timestamp when the stack was last viewed.
        metadata (Dict[str, Any]): The metadata of the stack.
        name (str): The name of the stack.
        priority (int): The priority of the stack.
        status (int): The status of the stack.
        subject (int): The ID of the subject the stack is associated with.
        tags (List[int]): The IDs of the tags associated with the stack.
        updated_at (datetime): The timestamp when the stack was last updated.
        uuid (str): The UUID of the stack.
    """

    def __init__(
        self,
        name: str,
        ancestor: Optional[int] = None,
        contents: Optional[List[str]] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        descendants: Optional[List[str]] = None,
        description: Optional[str] = None,
        difficulty: Optional[int] = None,
        due_by: Optional[datetime] = None,
        icon: Optional[str] = "📚",
        id: Optional[int] = None,
        key: Optional[str] = None,
        last_viewed_at: Optional[datetime] = None,
        metadata: Optional[Dict[str, Any]] = None,
        priority: Optional[int] = None,
        status: Optional[int] = None,
        subject: Optional[int] = None,
        tags: Optional[List[str]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableStack class.

        Args:
            ancestor (Optional[int]): The ID of the ancestor stack.
            contents(Optional[List[str]]): The list of the contents of the stack.
            created_at (Optional[datetime]): The timestamp when the stack was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): The custom field values of the stack.
            descendants (Optional[List[str]]): The list of the descendants of the stack.
            description (Optional[str]): The description of the stack.
            difficulty (Optional[int]): The difficulty of the stack.
            due_by (Optional[datetime]): The timestamp when the stack is due.
            icon (Optional[str]): The icon of the stack. Defaults to "📚".
            id (Optional[int]): The ID of the stack.
            key (Optional[str]): The key of the stack.
            last_viewed_at (Optional[datetime]): The timestamp when the stack was last viewed.
            metadata (Optional[Dict[str, Any]]): The metadata of the stack.
            name (Optional[str]): The name of the stack.
            priority (Optional[int]): The priority of the stack.
            status (Optional[int]): The status of the stack.
            subject (Optional[int]): The ID of the subject the stack is associated with.
            tags (Optional[List[str]]): The keys of the tags associated with the stack.
            updated_at (Optional[datetime]): The timestamp when the stack was last updated.
            uuid (Optional[str]): The UUID of the stack.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            ancestor=ancestor,
            contents=contents,
            created_at=created_at,
            custom_field_values=custom_field_values,
            descendants=descendants,
            description=description,
            difficulty=difficulty,
            due_by=due_by,
            icon=icon,
            id=id,
            key=key,
            last_viewed_at=last_viewed_at,
            metadata=metadata,
            name=name,
            priority=priority,
            status=status,
            subject=subject,
            tags=tags,
            updated_at=updated_at,
            uuid=uuid,
        )

    def add_to_contents(
        self,
        content: Any,
    ) -> None:
        """
        Adds a given object to the contents of the stack.

        Args:
            content (Any): The object to add to the contents of the stack.
        """

        # If the stack currently has no contents, create an empty list
        if not self.contents:
            # Initialize the contents list as an empty list
            self.contents = []

        # Check, if the stack's contents is an instance of string
        if isinstance(
            self.contents,
            str,
        ):
            # Convert the contents string into a list
            self.contents = json.loads(self.contents)

        # Append the key of the given object to the stack's contents
        self.contents.append(content.get(name="key"))

    def add_to_descendants(
        self,
        descendant: Any,
    ) -> None:
        """
        Adds a given object to the descendants of the stack.

        Args:
            descendant (Any): The object to add to the descendants of the stack.
        """

        # If the stack currently has no descendants, create an empty list
        if not self.descendants:
            # Initialize the descendants list as an empty list
            self.descendants = []

        # Check, if the stack's descendants is an instance of string
        if isinstance(
            self.descendants,
            str,
        ):
            # Convert the descendants string into a list
            self.descendants = json.loads(self.descendants)

        # Append the key of the given object to the stack's descendants
        self.descendants.append(descendant.get(name="key"))

    def get_content_grouped_by(
        self,
        type_key: Literal[
            "flashcard",
            "note",
            "question",
        ],
    ) -> List[str]:
        """
        Returns a list of the contents of the stack grouped by the given key.

        Args:
            type_key (Literal["flashcard", "note", "question"]): The key to group the contents by.

        Returns:
            List[str]: A list of the contents of the stack grouped by the given key.
        """

        # Check if the stack has content
        if not self.has_contents():
            # Return an empty list if the stack has no content
            return []

        # Return the list of the contents of the stack grouped by the given key
        return [
            key
            for key in self.get(
                default=[],
                name="contents",
            )
            if key.lower().startswith(type_key)
        ]

    def has_ancestor(self) -> bool:
        """
        Returns True if the stack has an ancestor, False otherwise.

        Returns:
            bool: True if the stack has an ancestor, False otherwise.
        """

        # Check if the stack has an ancestor
        return self.ancestor is not None

    def has_contents(self) -> bool:
        """
        Returns True if the stack has contents, False otherwise.

        Returns:
            bool: True if the stack has contents, False otherwise.
        """

        # Check if the stack has contents
        return self.contents is not None and len(self.contents) > 0

    def has_descendants(self) -> bool:
        """
        Returns True if the stack has descendants, False otherwise.

        Returns:
            bool: True if the stack has descendants, False otherwise.
        """

        # Check if the stack has descendants
        return self.descendants is not None and len(self.descendants) > 0

    def is_ancestor_of(
        self,
        key: str,
    ) -> bool:
        """
        Returns True if the stack is an ancestor of the given key, False otherwise.

        Args:
            key (str): The key of the stack.

        Returns:
            bool: True if the stack is an ancestor of the given key, False otherwise.
        """

        # Check if the stack has descendants
        if not self.has_descendants():
            # Return False if the stack has no descendants
            return False

        # Check if the stack is an ancestor of the given key
        return key in self.descendants

    def is_content_of(
        self,
        key: str,
    ) -> bool:
        """
        Returns True if the given key is a content of the stack, False otherwise.

        Args:
            key (str): The key of the content.

        Returns:
            bool: True if the given key is a content of the stack, False otherwise.
        """

        # Check if the stack has content
        if not self.has_contents():
            # Return False if the stack has no content
            return False

        # Check if the stack is a content of the given key
        return key in self.contents

    def is_descendant_of(
        self,
        key: str,
    ) -> bool:
        """
        Returns True if the stack is a descendant of the given key, False otherwise.

        Args:
            key (str): The key of the stack.

        Returns:
            bool: True if the stack is a descendant of the given key, False otherwise.
        """

        # Check if the stack has an ancestor
        if not self.has_ancestor():
            # Return False if the stack has no ancestor
            return False

        # Check if the stack is a descendant of the given key
        return key == self.ancestor

    def remove_from_contents(
        self,
        content: Any,
    ) -> None:
        """
        Removes a given object from the contents of the stack.

        Args:
            content (Any): The object to remove from the contents of the stack.
        """

        # If the stack currently has no contents, return
        if not self["contents"]:
            # Return early
            return

        # Remove the key of the given object from the stack's contents
        self["contents"].remove(content.key)

    def remove_from_descendants(
        self,
        obj: Any,
    ) -> None:
        """
        Removes a given object from the descendants of the stack.

        Args:
            obj (Any): The object to remove from the descendants of the stack.
        """

        # If the stack currently has no descendants, return
        if not self["descendants"]:
            # Return early
            return

        # Remove the key of the given object from the stack's descendants
        self["descendants"].remove(obj.key)

    def to_immutable(self) -> ImmutableStack:
        """
        Returns an immutable copy of the MutableStack instance.

        Returns:
            ImmutableStack: A immutable copy of the MutableStack instance.
        """
        try:
            # Create a new ImmutableStack instance from the dictionary representation of the MutableStack instance
            return ImmutableStack(
                **self.to_dict(
                    exclude=[
                        "_logger",
                    ]
                )
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            self.logger.error(
                message=f"Caught an exception while attempting to run 'to_immutable' method from '{self.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None


class StackConverter:
    """
    A converter class for transforming between StackModel and ImmutableStack instances.

    This class provides methods to convert a StackModel instance to an ImmutableStack instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the StackConverter class.
    """

    logger: Final[Logger] = Logger.get_logger(name="StackConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "StackModel",
    ) -> Optional[ImmutableStack]:
        """
        Converts a given StackModel instance to an ImmutableStack instance.

        Args:
            model (StackModel): The StackModel instance to be converted.

        Returns:
            ImmutableStack: The converted ImmutableStack instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the StackModel instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableStack class from the dictionary representation of the StackModel instance
            return ImmutableStack(
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
        object: ImmutableStack,
    ) -> Optional["StackModel"]:
        """
        Converts a given ImmutableStack instance to a StackModel instance.

        Args:
            object (ImmutableStack): The ImmutableStack instance to be converted.

        Returns:
            StackModel: The converted StackModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ImmutableStack instance.
        """
        try:
            # Attempt to create and return a new instance of the StackModel class from the dictionary representation of the ImmutableStack instance
            return StackModel(
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


class StackFactory:
    """
    A factory class for creating Stack instances.

    Attributes:
        logger (Logger): The logger instance associated with the StackFactory class.
    """

    logger: Final[Logger] = Logger.get_logger(name="StackFactory")

    @classmethod
    def create_stack(
        cls,
        name: str,
        ancestor: Optional[int] = None,
        contents: Optional[List[str]] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        descendants: Optional[List[str]] = None,
        description: Optional[str] = None,
        difficulty: Optional[int] = None,
        due_by: Optional[datetime] = None,
        icon: Optional[str] = "📚",
        id: Optional[int] = None,
        key: Optional[str] = None,
        last_viewed_at: Optional[datetime] = None,
        metadata: Optional[Dict[str, Any]] = None,
        priority: Optional[int] = None,
        status: Optional[int] = None,
        subject: Optional[int] = None,
        tags: Optional[List[str]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutableStack]:
        """
        Creates and returns a new instance of the ImmutableStack class.

        Args:
            ancestor (Optional[int]): The ID of the ancestor stack.
            contents(Optional[List[str]]): The list of the contents of the stack.
            created_at (Optional[datetime]): The timestamp when the stack was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): The customfield values of the stack.
            descendants (Optional[List[str]]): The list of the descendants of the stack.
            description (Optional[str]): The description of the stack.
            difficulty (Optional[int]): The difficulty of the stack.
            due_by (Optional[datetime]): The timestamp when the stack is due.
            icon (Optional[str]): The icon of the stack. Defaults to "📚".
            id (Optional[int]): The ID of the stack.
            key (Optional[str]): The key of the stack.
            last_viewed_at (Optional[datetime]): The timestamp when the stack was last viewed.
            metadata (Optional[Dict[str, Any]]): The metadata of the stack.
            name (Optional[str]): The name of the stack.
            priority (Optional[int]): The priority of the stack.
            status (Optional[int]): The status of the stack.
            subject (Optional[int]): The ID of the subject the stack is associated with.
            tags (Optional[List[str]]): The keys of the tags associated with the stack.
            updated_at (Optional[datetime]): The timestamp when the stack was last updated.
            uuid (Optional[str]): The UUID of the stack.

        Returns:
            ImmutableStack: The created ImmutableStack instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to create the ImmutableStack instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableStack class
            return ImmutableStack(
                ancestor=ancestor,
                contents=contents,
                created_at=created_at,
                custom_field_values=custom_field_values,
                descendants=descendants,
                description=description,
                difficulty=difficulty,
                due_by=due_by,
                icon=icon,
                id=id,
                key=key,
                last_viewed_at=last_viewed_at,
                metadata=metadata,
                name=name,
                priority=priority,
                status=status,
                subject=subject,
                tags=tags,
                updated_at=updated_at,
                uuid=uuid,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_stack' method from '{cls.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class StackBuilder(BaseObjectBuilder):
    """
    A builder class for creating ImmutableStack instances.

    This class extends the BaseObjectBuilder class and is used to create
    new instances of the ImmutableStack class.

    Attributes:
        configuration (Dict[str, Any]): The configuration dictionary for the ImmutableStack instance.
        logger (Logger): The logger for the StackBuilder class.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the StackBuilder class.

        Args:
            None

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    @override
    def build(self) -> Optional[ImmutableStack]:
        """
        Builds an ImmutableStack instance based on the configuration.

        Args:
            None

        Returns:
            Optional[ImmutableStack]: The built ImmutableStack instance if successful, otherwise None.

        Raises:
            Exception: If an exception occurs while attempting to build the ImmutableStack instance.
        """
        try:
            # Attmept to create and return a new ImmutableStack instance
            return StackFactory.create_stack(**self.configuration)
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
        Sets the ancestor value in the configuration.

        Args:
            value (int): The ancestor value.

        Returns:
            Self: The builder instance.
        """

        # Set the ancestor value in the configuration
        self.configuration["ancestor"] = value

        # Return self
        return self

    def contents(
        self,
        value: Union[Dict[str, Any], List[Dict[str, Any]]],
    ) -> Self:
        """
        Sets the contents value in the configuration.

        Args:
            value (Union[Dict[str, Any], List[Dict[str, Any]]]): The contents value.

        Returns:
            Self: The builder instance.
        """

        # Check, if the 'contents' key exists in the 'configuration' dictionary
        if "contents" not in self.configuration:
            # Initialize the 'contents' key with an empty list
            self.configuration["contents"] = []

        # Check, if the passed value is a dictionary
        if isinstance(
            value,
            dict,
        ):
            # Append the dictionary to the 'contents' list
            self.configuration["contents"].append(value)

        # Check, if the passed value is a list
        elif isinstance(
            value,
            list,
        ):
            # Set the contents value in the configuration
            self.configuration["contents"] = value

        # Return self
        return self

    def custom_field_values(
        self,
        value: Union[
            Dict[str, Any],
            List[Dict[str, Any]],
        ],
    ) -> Self:
        """
        Sets the custom_field_values value in the configuration.

        Args:
            value (Union[Dict[str, Any], List[Dict[str, Any]]]): The custom_field_values value.

        Returns:
            Self: The builder instance.
        """

        # Check, if the 'custom_field_values' key exists in the 'configuration' dictionary
        if "custom_field_values" not in self.configuration:
            # Initialize the 'custom_field_values' key with an empty list
            self.configuration["custom_field_values"] = []

        # Check, if the passed value is a dictionary
        if isinstance(
            value,
            dict,
        ):
            # Append the dictionary to the 'custom_field_values' list
            self.configuration["custom_field_values"].append(value)

        # Check, if the passed value is a list
        elif isinstance(
            value,
            list,
        ):
            # Set the custom_field_values value in the configuration
            self.configuration["custom_field_values"] = value

        # Return self
        return self

    def descendants(
        self,
        value: Union[List[str], str],
    ) -> Self:
        """
        Sets the descendants value in the configuration.

        Args:
            value (Union[List[str], str]): The descendants value.

        Returns:
            Self: The builder instance.
        """

        # Check, if the 'descendants' key exists in the 'configuration' dictionary
        if "descendants" not in self.configuration:
            # Initialize the 'descendants' key with an empty list
            self.configuration["descendants"] = []

        # Check, if the passed value is a string
        if isinstance(
            value,
            str,
        ):
            # Append the string to the 'descendants' list
            self.configuration["descendants"].append(value)

        # Check, if the passed value is a list
        elif isinstance(
            value,
            list,
        ):
            # Set the descendants value in the configuration
            self.configuration["descendants"] = value

        # Return self
        return self

    def description(
        self,
        value: str,
    ) -> Self:
        """
        Sets the description value in the configuration.

        Args:
            value (str): The description value.

        Returns:
            Self: The builder instance.
        """

        # Set the description value in the configuration
        self.configuration["description"] = value

        # Return self
        return self

    def difficulty(
        self,
        value: int,
    ) -> Self:
        """
        Sets the difficulty value in the configuration.

        Args:
            value (int): The difficulty value.

        Returns:
            Self: The builder instance.
        """

        # Set the difficulty value in the configuration
        self.configuration["difficulty"] = value

        # Return self
        return self

    def due_by(
        self,
        value: datetime,
    ) -> Self:
        """
        Sets the due_by value in the configuration.

        Args:
            value (datetime): The due_by value.

        Returns:
            Self: The builder instance.
        """

        # Set the due_by value in the configuration
        self.configuration["due_by"] = value

        # Return self
        return self

    def metadata(
        self,
        value: Dict[str, Any],
    ) -> Self:
        """
        Sets the metadata value in the configuration.

        Args:
            value (Dict[str, Any]): The metadata value.

        Returns:
            Self: The builder instance.
        """

        # Check, if the 'metadata' key exists in the 'configuration' dictionary
        if "metadata" not in self.configuration:
            # Initialize the 'metadata' key with an empty dictionary
            self.configuration["metadata"] = {}
        else:
            # Update the 'metadata' key with the new value
            self.configuration["metadata"].update(**value)

        # Return self
        return self

    def name(
        self,
        value: str,
    ) -> Self:
        """
        Sets the name value in the configuration.

        Args:
            value (str): The name value.

        Returns:
            Self: The builder instance.
        """

        # Set the name value in the configuration
        self.configuration["name"] = value

        # Return self
        return self

    def priority(
        self,
        value: int,
    ) -> Self:
        """
        Sets the priority value in the configuration.

        Args:
            value (int): The priority value.

        Returns:
            Self: The builder instance.
        """

        # Set the priority value in the configuration
        self.configuration["priority"] = value

        # Return self
        return self

    def status(
        self,
        value: int,
    ) -> Self:
        """
        Sets the status value in the configuration.

        Args:
            value (int): The status value.

        Returns:
            Self: The builder instance.
        """

        # Set the status value in the configuration
        self.configuration["status"] = value

        # Return self
        return self

    def subject(
        self,
        value: int,
    ) -> Self:
        """
        Sets the subject value in the configuration.

        Args:
            value (int): The subject value.

        Returns:
            Self: The builder instance.
        """

        # Set the subject value in the configuration
        self.configuration["subject"] = value

        # Return self
        return self

    def tags(
        self,
        value: Union[List[str], str],
    ) -> Self:
        """
        Sets the tags value in the configuration.

        Args:
            value (Union[List[str], str]): The tags value.

        Returns:
            Self: The builder instance.
        """

        # Check, if the 'tags' key exists in the 'configuration' dictionary
        if "tags" not in self.configuration:
            # Initialize the 'tags' key with an empty list
            self.configuration["tags"] = []

        # Check, if the passed value is a list
        if isinstance(
            value,
            list,
        ):
            # Extend the 'tags' list with the new values
            self.configuration["tags"].extend(value)

        # Check, if the passed value is a string
        elif isinstance(
            value,
            str,
        ):
            # Append the string to the 'tags' list
            self.configuration["tags"].append(value)

        # Return self
        return self


class StackManager(BaseObjectManager):
    """
    A manager class for managing stacks in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for stacks.

    Attributes:
        cache: (List[Any]): The cache for storing stacks.
        logger (Logger): The logger instance associated with the object.
    """

    _shared_instance: Optional["StackManager"] = None

    def __new__(cls) -> "StackManager":
        """
        Creates and returns a new instance of the StackManager class.

        If the instance does not exist, creates a new one by calling the parent class
        constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Returns:
            StackManager: The created or existing instance of StackManager class.
        """
        # Check if the shared instance does not exist
        if cls._shared_instance is None:
            # Create a new instance by calling the parent class constructor
            cls._shared_instance = super(StackManager, cls).__new__(cls)
            # Initialize the instance with the dispatcher and stacks
            cls._shared_instance.init()
        # Return the shared instance
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes the stack manager.

        This method is responsible for initializing the stack manager by
        setting up the logger instance.

        Returns:
            None
        """
        pass

    def count_stacks(self) -> int:
        """
        Returns the number of stacks in the database.

        Returns:
            int: The number of stacks in the database.
        """
        try:
            # Count and return the number of stacks in the database
            return asyncio.run(StackModel.count(database=Constants.DATABASE_PATH))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_stack(
        self,
        stack: Union[ImmutableStack, MutableStack],
    ) -> Optional[ImmutableStack]:
        """
        Creates a new stack in the database.

        Args:
            stack (Union[ImmutableStack, MutableStack]): The stack to be created.

        Returns:
            Optional[ImmutableStack]: The newly created immutable stack if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the stack.
        """
        try:
            # Check if the stack object is immutable
            if isinstance(
                stack,
                ImmutableStack,
            ):
                # If it is, convert it to a mutable stack
                stack = stack.to_mutable()

            # Set the created_at timestamp of the stack
            stack.created_at = Miscellaneous.get_current_datetime()

            # Set the custom_field_values of the stack
            stack.custom_field_values = [] or stack.custom_field_values

            # Set the key of the stack
            stack.key = f"STACK_{self.count_stacks() + 1}"

            # Set the last_viewed_at timestamp of the stack
            stack.last_viewed_at = Miscellaneous.get_current_datetime()

            # Set the tags of the stack
            stack.tags = [] or stack.tags

            # Set the updated_at timestamp of the stack
            stack.updated_at = Miscellaneous.get_current_datetime()

            # Set the uuid of the stack
            stack.uuid = Miscellaneous.get_uuid()

            # Convert the stack object to a StackModel object
            model: StackModel = StackConverter.object_to_model(object=stack)

            # Create a new stack in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            if id:
                # Set the ID of the stack
                stack.id = id

                # Convert the stack to an immutable stack
                stack = StackFactory.create_stack(
                    **stack.to_dict(
                        exclude=[
                            "_logger",
                        ]
                    )
                )

                # Add the stack to the cache
                self.add_to_cache(
                    key=stack.key,
                    value=stack,
                )

                # Return the newly created immutable stack
                return stack

            # Log a warning message indicating an error has occurred
            self.logger.warning(
                message=f"It seems that an error has occured while attempting to create a stack ({stack}) in the database."
            )

            # Return None indicating an error has occurred
            return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_stack' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete_stack(
        self,
        stack: Union[ImmutableStack, MutableStack],
    ) -> bool:
        """
        Deletes a stack from the database.

        Args:
            stack (Union[ImmutableStack, MutableStack]): The stack to be deleted.

        Returns:
            bool: True if the stack was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the stack to an immutable stack and delete the stack from the database
            result: bool = asyncio.run(
                StackConverter.object_to_model(
                    object=StackFactory.create_stack(
                        **stack.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).delete()
            )

            # Remove the stack from the cache
            self.remove_from_cache(key=stack.key)

            # Return True if the stack was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_from_stacks(
        self,
        condition: Callable[[ImmutableStack], bool],
        limit: Optional[int] = None,
    ) -> Optional[List[ImmutableStack]]:
        """
        Returns a list of stacks from the cache that match the given condition.

        Args:
            condition (Callable[[ImmutableStack], bool]): A function that takes an ImmutableStack instance and returns a boolean value.
            limit (Optional[int]): The maximum number of stacks to return.

        Returns:
            Optional[ImmutableStack]: The stack that matches the given condition if no exception occurs. Otherwise, None.
        """
        try:
            # Initialize an empty list to store matching stacks
            result: List[ImmutableStack] = []

            # Get all stacks from the cache
            stacks: List[ImmutableStack] = self.get_all_stacks()

            # Iterate over the list of immutable stacks in the cache
            for stack in stacks:
                # Check if the stack matches the given condition
                if condition(stack):
                    # Add the stack that matches the given condition to the result list
                    result.append(stack)

            # Check if the limit is specified and if the result list exceeds the limit
            if limit is not None and len(result) > limit:
                # Return the first 'limit' number of stacks
                return result[:limit]

            # Return the list of matching stacks
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_from_stacks' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_all_stacks(
        self,
        force_refetch: bool = False,
    ) -> Optional[List[ImmutableStack]]:
        """
        Returns a list of all stacks in the database.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.

        Returns:
            Optional[List[ImmutableStack]]: A list of all stacks in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if cache and table size are equal
                if self.cache and len(self._cache) == self.count_stacks():
                    # Return the list of immutable stacks from the cache
                    return self.get_cache_values()

            # Get all stacks from the database
            models: List[StackModel] = asyncio.run(
                StackModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of StackModel objects to a list of ImmutableStack objects
            stacks: List[ImmutableStack] = [
                StackFactory.create_stack(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable stacks
            for stack in stacks:
                # Add the immutable stack to the cache
                self.add_to_cache(
                    key=stack.key,
                    value=stack,
                )

            # Return the list of immutable stacks
            return stacks
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_stack_by(
        self,
        field: str,
        value: Any,
        force_refetch: bool = False,
    ) -> Optional[ImmutableStack]:
        """
        Retrieves a stack by the given field and value.

        Args:
            field (str): The field to search by.
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            value (Any): The value to search for.

        Returns:
            Optional[ImmutableStack]: The stack with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if the stack is already in the cache
                if self.is_key_in_cache(key=field):
                    # Return the stack from the cache
                    return self.get_value_from_cache(key=field)

            # Get the stack with the given field and value from the database
            model: Optional[StackModel] = asyncio.run(
                StackModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Return the stack if it exists
            if model is not None:
                # Convert the StackModel object to an ImmutableStack object
                stack: ImmutableStack = StackFactory.create_stack(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the stack to the cache
                self.add_to_cache(
                    key=stack.key,
                    value=stack,
                )

                # Return the stack
                return stack
            else:
                # Return None indicating that the stack does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_stack_by_id(
        self,
        id: int,
        force_refetch: bool = False,
    ) -> Optional[ImmutableStack]:
        """
        Returns a stack with the given ID.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            id (int): The ID of the stack.

        Returns:
            Optional[ImmutableStack]: The stack with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if the stack is already in the cache
                if self.is_key_in_cache(key=f"STACK_{id}"):
                    # Return the stack from the cache
                    return self.get_value_from_cache(key=f"STACK_{id}")

            # Get the stack with the given ID from the database
            model: Optional[StackModel] = asyncio.run(
                StackModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the stack if it exists
            if model is not None:
                # Convert the StackModel object to an ImmutableStack object
                stack: ImmutableStack = StackFactory.create_stack(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the stack to the cache
                self.add_to_cache(
                    key=stack.key,
                    value=stack,
                )

                # Return the stack
                return stack
            else:
                # Return None indicating that the stack does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_stack_by_key(
        self,
        key: str,
        force_refetch: bool = False,
    ) -> Optional[ImmutableStack]:
        """
        Returns a stack with the given key.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            key (str): The key of the stack.

        Returns:
            Optional[ImmutableStack]: The stack with the given key if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if the stack is already in the cache
                if self.is_key_in_cache(key=key):
                    # Return the stack from the cache
                    return self.get_value_from_cache(key=key)

            # Get the stack with the given ID from the database
            model: Optional[StackModel] = asyncio.run(
                StackModel.get_by(
                    column="key",
                    database=Constants.DATABASE_PATH,
                    value=key,
                )
            )

            # Return the stack if it exists
            if model is not None:
                # Convert the StackModel object to an ImmutableStack object
                stack: ImmutableStack = StackFactory.create_stack(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the stack to the cache
                self.add_to_cache(
                    key=stack.key,
                    value=stack,
                )

                # Return the stack
                return stack
            else:
                # Return None indicating that the stack does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_key' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_stack_by_uuid(
        self,
        uuid: str,
        force_refetch: bool = False,
    ) -> Optional[ImmutableStack]:
        """
        Returns a stack with the given UUID.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            uuid (str): The UUID of the stack.

        Returns:
            Optional[ImmutableStack]: The stack with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Check if the stack is already in the cache
                if self.is_key_in_cache(key=uuid):
                    # Return the stack from the cache
                    return self.get_value_from_cache(key=uuid)

            # Get the stack with the given UUID from the database
            model: Optional[StackModel] = asyncio.run(
                StackModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the stack if it exists
            if model is not None:
                # Convert the StackModel object to an ImmutableStack object
                stack: ImmutableStack = StackFactory.create_stack(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the stack to the cache
                self.add_to_cache(
                    key=stack.key,
                    value=stack,
                )

                # Return the stack
                return stack
            else:
                # Return None indicating that the stack does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def search_stacks(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[Union[List[ImmutableStack]]]:
        """
        Searches for stacks in the database.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            **kwargs: Any additional keyword arguments to be passed to the search method of the StackModel class.

        Returns:
            Optional[Union[List[ImmutableStack]]]: The found stacks if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Search the stack for the passed keyword arguments
                cached_result: Optional[List[ImmutableStack]] = self.search_cache(
                    **kwargs
                )

                # Check, if any cached results exist
                if cached_result:
                    # Return the cached results
                    return cached_result

            # Search for stacks in the database
            models: Optional[List[StackModel]] = asyncio.run(
                StackModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found stacks if any
            if models is not None and len(models) > 0:
                stacks: List[ImmutableStack] = [
                    StackFactory.create_stack(
                        **model.to_dict(
                            exclude=[
                                "_logger",
                                "table",
                            ]
                        )
                    )
                    for model in models
                ]

                # Iterate over the found stacks
                for stack in stacks:
                    # Add the stack to the cache
                    self.add_to_cache(
                        key=stack.key,
                        value=stack,
                    )

                # Return the found stacks
                return stacks
            else:
                # Return None indicating that no stacks were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_stack(
        self,
        stack: Union[ImmutableStack, MutableStack],
    ) -> Optional[ImmutableStack]:
        """
        Updates a stack with the given ID.

        Args:
            stack (Union[ImmutableStack, MutableStack]): The stack to update.

        Returns:
            Optional[ImmutableStack]: The updated stack if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the stack object is immutable
            if isinstance(
                stack,
                ImmutableStack,
            ):
                # If it is, convert it to a mutable stack
                stack = stack.to_mutable()

            # Update the updated_at timestamp of the stack
            stack.updated_at = Miscellaneous.get_current_datetime()

            # Convert the stack to an immutable stack and update the stack in the database
            result: bool = asyncio.run(
                StackConverter.object_to_model(
                    object=StackFactory.create_stack(
                        **stack.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).update(
                    database=Constants.DATABASE_PATH,
                    **stack.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Check, if the stack was updated successfully
            if result:
                # Update the stack in the cache
                self.update_in_cache(
                    key=stack.key,
                    value=stack,
                )

                # Return the updated stack
                return stack.to_immutable()
            else:
                # Return None indicating that the stack does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class StackModel(ImmutableBaseModel):
    """
    Represents the structure of a stack model.

    Attributes:
        ancestor (Optional[int]): The ID of the ancestor stack.
        created_at (Optional[datetime]): The timestamp when the stack was created.
        custom_field_values (Optional[JSON]): The values of the custom fields.
        description (Optional[str]): The description of the stack.
        difficulty (Optional[int]): The difficulty of the stack.
        due_by (Optional[datetime]): The timestamp when the stack is due.
        icon (Optional[str]): The icon of the stack. Defaults to "📚".
        id (Optional[int]): The ID of the stack.
        key (Optional[str]): The key of the stack.
        last_viewed_at (Optional[datetime]): The timestamp when the stack was last viewed.
        metadata (Optional[Dict[str, Any]]): The metadata of the stack.
        name (Optional[str]): The name of the stack.
        priority (Optional[int]): The priority of the stack.
        status (Optional[int]): The status of the stack.
        subject (Optional[int]): The ID of the subject the stack is associated with.
        tags (Optional[List[str]]): The tags of the stack.
        updated_at (Optional[datetime]): The timestamp when the stack was last updated.
        uuid (Optional[str]): The UUID of the stack.
    """

    table: Final[str] = Constants.STACKS

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
        foreign_key=f"{Constants.STACKS}(id)",
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

    contents: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="contents",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
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
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
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

    description: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="description",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="TEXT",
        unique=False,
    )

    difficulty: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.DIFFICULTIES}(id)",
        index=False,
        name="difficulty",
        nullable=False,
        on_delete="NO ACTION",
        on_update="NO ACTION",
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    due_by: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="due_by",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="DATETIME",
        unique=False,
    )

    icon: Field = Field(
        autoincrement=False,
        default="📚",
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

    last_viewed_at: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="last_viewed_at",
        nullable=True,
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

    name: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="name",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=True,
    )

    priority: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.PRIORITIES}(id)",
        index=False,
        name="priority",
        nullable=False,
        on_delete="NO ACTION",
        on_update="NO ACTION",
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    status: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.STATUSES}(id)",
        index=False,
        name="status",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    subject: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=f"{Constants.SUBJECTS}(id)",
        index=False,
        name="subject",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="INTEGER",
        unique=False,
    )

    tags: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="tags",
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

    def __init__(
        self,
        ancestor: Optional[int] = None,
        contents: Optional[List[str]] = None,
        created_at: Optional[datetime] = None,
        custom_field_values: Optional[List[Dict[str, Any]]] = None,
        descendants: Optional[List[str]] = None,
        description: Optional[str] = None,
        difficulty: Optional[int] = None,
        due_by: Optional[datetime] = None,
        icon: Optional[str] = "📚",
        id: Optional[int] = None,
        key: Optional[str] = None,
        last_viewed_at: Optional[datetime] = None,
        metadata: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        priority: Optional[int] = None,
        status: Optional[Literal["New", "Learning", "Review", "Completed"]] = None,
        subject: Optional[int] = None,
        tags: Optional[List[str]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the StackModel class.

        Args:
            ancestor (Optional[int]): The ID of the ancestor stack.
            contents(Optional[List[str]]): The contents of the stack.
            created_at (Optional[datetime]): The timestamp when the stack was created.
            custom_field_values (Optional[List[Dict[str, Any]]]): The custom field values of the stack.
            descendants (Optional[List[str]]): The descendants of the stack.
            description (Optional[str]): The description of the stack.
            difficulty (Optional[int]): The difficulty of the stack.
            due_by (Optional[datetime]): The timestamp when the stack is due.
            icon (Optional[str]): The icon of the stack. Defaults to "📚".
            id (Optional[int]): The ID of the stack.
            key (Optional[str]): The key of the stack.
            last_viewed_at (Optional[datetime]): The timestamp when the stack was last viewed.
            metadata (Optional[Dict[str, Any]]): The metadata of the stack.
            name (Optional[str]): The name of the stack.
            priority (Optional[int]): The priority of the stack.
            status (Optional[int]): The ID of the status of the stack.
            subject (Optional[int]): The ID of the subject the stack is associated with.
            tags (Optional[List[str]]): The keys of the tags associated with the stack.
            updated_at (Optional[datetime]): The timestamp when the stack was last updated.
            uuid (Optional[str]): The UUID of the stack.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            ancestor=ancestor,
            contents=contents,
            created_at=created_at,
            custom_field_values=custom_field_values,
            descendants=descendants,
            description=description,
            difficulty=difficulty,
            due_by=due_by,
            icon="📚",
            id=id,
            key=key,
            last_viewed_at=last_viewed_at,
            metadata=metadata,
            name=name,
            priority=priority,
            status=status,
            subject=subject,
            tags=tags,
            table=Constants.STACKS,
            updated_at=updated_at,
            uuid=uuid,
        )
