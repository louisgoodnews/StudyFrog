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
    "Priority",
    "PriorityConverter",
    "PriorityFactory",
    "PriorityManager",
    "PriorityModel",
]


class Priority(ImmutableBaseObject):
    """
    An immutable class representing a priority.

    A priority has a value between 0 and 1 that represents the importance of an object.

    Attributes:
        name (str): The name of the priority.
        value (float): The value of the priority.
        created_at (datetime): The timestamp when the priority was created.
        id (int): The ID of the priority.
        key (str): The key of the priority.
        updated_at (datetime): The timestamp when the priority was last updated.
        uuid (str): The UUID of the priority.
    """

    def __init__(
        self,
        name: str,
        value: float,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the Priority class.

        Args:
            name (str): The name of the priority.
            value (float): The value of the priority.
            created_at (Optional[datetime]): The timestamp when the priority was created.
            id (Optional[int]): The ID of the priority.
            key (Optional[str]): The key of the priority.
            updated_at (Optional[datetime]): The timestamp when the priority was last updated.
            uuid (Optional[str]): The UUID of the priority.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            id=id,
            key=key,
            name=name,
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )


class PriorityConverter:
    """
    A converter class for transforming between PriorityModel and Priority instances.

    This class provides methods to convert a PriorityModel instance to an Priority instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the PriorityConverter class.
    """

    logger: Logger = Logger.get_logger(name="PriorityConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "PriorityModel",
    ) -> Optional[Priority]:
        """
        Converts a given PriorityModel instance to an Priority instance.

        Args:
            model (PriorityModel): The PriorityModel instance to be converted.

        Returns:
            Priority: The converted Priority instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the PriorityModel instance.
        """
        try:
            # Attempt to create and return a new instance of the Priority class from the dictionary representation of the PriorityModel instance
            return Priority(**model.to_dict(exclude=["logger"])["fields"])
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
        object: Priority,
    ) -> Optional["PriorityModel"]:
        """
        Converts a given Priority instance to a PriorityModel instance.

        Args:
            object (Priority): The Priority instance to be converted.

        Returns:
            PriorityModel: The converted PriorityModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the Priority instance.
        """
        try:
            # Attempt to create and return a new instance of the PriorityModel class from the dictionary representation of the Priority instance
            return PriorityModel(**object.to_dict(exclude=["logger"]))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'object_to_model' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class PriorityFactory:
    logger: Logger = Logger.get_logger(name="PriorityFactory")

    @classmethod
    def create_priority(
        cls,
        name: str,
        value: float,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[Priority]:
        """
        Creates a new instance of the Priority class.

        Args:
            name (str): The name of the priority.
            value (float): The value of the priority.
            created_at (Optional[datetime]): The timestamp when the priority was created.
            id (Optional[int]): The ID of the priority.
            key (Optional[str]): The key of the priority.
            updated_at (Optional[datetime]): The timestamp when the priority was last updated.
            uuid (Optional[str]): The UUID of the priority.

        Returns:
            Optional[Priority]: The new instance of the Priority class.
        """
        try:
            # Attempt to create and return a Priority object
            return Priority(
                name=name,
                value=value,
                created_at=created_at,
                id=id,
                key=key,
                updated_at=updated_at,
                uuid=uuid,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_priority' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class PriorityManager(BaseObjectManager):
    pass


class PriorityModel(ImmutableBaseModel):
    """
    A model class representing a priority.

    A priority has a value between 0 and 1 that represents the importance of an object.

    Attributes:
        name (str): The name of the priority.
        value (float): The value of the priority.
    """

    def __init__(
        self,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[float] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the PriorityModel class.

        Args:
            created_at (Optional[datetime]): The timestamp when the priority was created.
            id (Optional[int]): The ID of the priority.
            key (Optional[str]): The key of the priority.
            name (Optional[str]): The name of the priority.
            updated_at (Optional[datetime]): The timestamp when the priority was last updated.
            uuid (Optional[str]): The UUID of the priority.
            value (Optional[float]): The value of the priority.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            table="flashcards",
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
                    on_delete="NO ACTION",
                    on_update="NO ACTION",
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
            name=(
                name
                or Field(
                    autoincrement=False,
                    default=None,
                    description="",
                    foreign_key=None,
                    index=False,
                    name="name",
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
            value=(
                value
                or Field(
                    autoincrement=False,
                    default=None,
                    description="",
                    foreign_key=None,
                    index=False,
                    name="value",
                    nullable=True,
                    on_delete="NO ACTION",
                    on_update="NO ACTION",
                    primary_key=False,
                    size=None,
                    type="DOUBLE",
                    unique=False,
                )
            ),
        )
