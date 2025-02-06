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
    "ImmutableStack",
    "MutableStack",
    "StackConverter",
    "StackFactory",
    "StackManager",
    "StackModel",
]


class ImmutableStack(ImmutableBaseObject):
    """
    An immutable class representing a stack.

    A stack is a collection of Flashards, Notes and Questions.

    Attributes:
        contents (List[Dict[str, Any]]): The contents of the stack.
        created_at (datetime): The timestamp when the stack was created.
        id (int): The ID of the stack.
        key (str): The key of the stack.
        name (str): The name of the stack.
        updated_at (datetime): The timestamp when the stack was last updated.
        uuid (str): The UUID of the stack.
    """

    def __init__(
        self,
        name: str,
        contents: Optional[List[Dict[str, Any]]] = None,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableStack class.

        Args:
            name (str): The name of the stack.
            contents (Optional[List[Dict[str, Any]]]): The contents of the stack.
            created_at (Optional[datetime]): The timestamp when the stack was created.
            id (Optional[int]): The ID of the stack.
            key (Optional[str]): The key of the stack.
            updated_at (Optional[datetime]): The timestamp when the stack was last updated.
            uuid (Optional[str]): The UUID of the stack.
        """

        # Call the parent class constructor
        super().__init__(
            contents=contents,
            created_at=created_at,
            id=id,
            key=key,
            name=name,
            updated_at=updated_at,
            uuid=uuid,
        )

    def to_mutable(self) -> "MutableStack":
        """
        Returns a mutable copy of the ImmuutableStack instance.

        Returns:
            MutableStack: A mutable copy of the ImmuutableStack instance.
        """

        # Create a new MutableStack instance from the dictionary representation of the ImmutableStack instance
        return MutableStack(**self.to_dict(exclude=["logger"]))


class MutableStack(MutableBaseObject):
    """
    A mutable class representing a stack.

    A stack is a collection of Flashards, Notes and Questions.

    Attributes:
        contents (List[Dict[str, Any]]): The contents of the stack.
        created_at (datetime): The timestamp when the stack was created.
        id (int): The ID of the stack.
        key (str): The key of the stack.
        name (str): The name of the stack.
        updated_at (datetime): The timestamp when the stack was last updated.
        uuid (str): The UUID of the stack.
    """

    def __init__(
        self,
        contents: Optional[List[Dict[str, Any]]] = None,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        name: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableStack class.

        Args:
            contents (Optional[List[Dict[str, Any]]]): The contents of the stack.
            created_at (Optional[datetime]): The timestamp when the stack was created.
            id (Optional[int]): The ID of the stack.
            key (Optional[str]): The key of the stack.
            name (Optional[str]): The name of the stack.
            updated_at (Optional[datetime]): The timestamp when the stack was last updated.
            uuid (Optional[str]): The UUID of the stack.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            contents=contents,
            created_at=created_at,
            id=id,
            key=key,
            name=name,
            updated_at=updated_at,
            uuid=uuid,
        )

    def add_to_contents(
        self,
        content: Any,
    ) -> None:
        """
        Adds a content to the contents list.

        Args:
            content (Any): The content to be added to the contents list.

        Returns:
            None
        """

        # Append the content to the contents list
        self.contents.append(
            {
                "id": content.id,
                "type": content.__class__.__name__,
                "uuid": content.uuid,
            }
        )

        # Set the updated_at timestamp
        self.updated_at = datetime.now()

    def remove_from_contents(
        self,
        uuid: str,
    ) -> bool:
        """
        Removes a content from the contents list.

        Args:
            uuid (str): The uuid of the content to be removed.

        Returns:
            bool: True if the content was removed, False otherwise.
        """

        # Iterate over the contents list
        for content in self.contents:
            # Check if the content has the same uuid as the one to be removed
            if content["uuid"] == uuid:

                # Remove the content from the contents list
                self.contents.remove(content)

                # Update the timestamp
                self.updated_at = datetime.now()

                # Return True indicating the content was removed
                return True

        # Raise a ValueError if the content was not found
        raise ValueError(f"Content with uuid {uuid} not found")

    def to_immutable(self) -> ImmutableStack:
        """
        Returns an immutable copy of the MutableStack instance.

        Returns:
            ImmutableStack: A immutable copy of the MutableStack instance.
        """

        # Create a new ImmutableStack instance from the dictionary representation of the MutableStack instance
        return ImmutableStack(**self.to_dict(exclude=["logger"]))
