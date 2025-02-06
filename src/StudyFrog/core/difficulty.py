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
    "Difficulty",
    "DifficultyConverter",
    "DifficultyFactory",
    "DifficultyManager",
    "DifficultyModel",
]


class Difficulty(ImmutableBaseObject):
    """
    An immutable class representing a difficulty.

    A difficulty has a value between 0 and 1 that represents the importance of an object.

    Attributes:
        name (str): The name of the difficulty.
        value (float): The value of the difficulty.
        created_at (datetime): The timestamp when the difficulty was created.
        id (int): The ID of the difficulty.
        key (str): The key of the difficulty.
        updated_at (datetime): The timestamp when the difficulty was last updated.
        uuid (str): The UUID of the difficulty.
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
        Initializes a new instance of the Difficulty class.

        Args:
            name (str): The name of the difficulty.
            value (float): The value of the difficulty.
            created_at (Optional[datetime]): The timestamp when the difficulty was created.
            id (Optional[int]): The ID of the difficulty.
            key (Optional[str]): The key of the difficulty.
            updated_at (Optional[datetime]): The timestamp when the difficulty was last updated.
            uuid (Optional[str]): The UUID of the difficulty.

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


class DifficultyConverter:
    """
    A converter class for transforming between DifficultyModel and Difficulty instances.

    This class provides methods to convert a DifficultyModel instance to an Difficulty instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the DifficultyConverter class.
    """

    logger: Logger = Logger.get_logger(name="DifficultyConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "DifficultyModel",
    ) -> Optional[Difficulty]:
        """
        Converts a given DifficultyModel instance to an Difficulty instance.

        Args:
            model (DifficultyModel): The DifficultyModel instance to be converted.

        Returns:
            Difficulty: The converted Difficulty instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the DifficultyModel instance.
        """
        try:
            # Attempt to create and return a new instance of the Difficulty class from the dictionary representation of the DifficultyModel instance
            return Difficulty(**model.to_dict(exclude=["logger"])["fields"])
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
        object: Difficulty,
    ) -> Optional["DifficultyModel"]:
        """
        Converts a given Difficulty instance to a DifficultyModel instance.

        Args:
            object (Difficulty): The Difficulty instance to be converted.

        Returns:
            DifficultyModel: The converted DifficultyModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the Difficulty instance.
        """
        try:
            # Attempt to create and return a new instance of the DifficultyModel class from the dictionary representation of the Difficulty instance
            return DifficultyModel(**object.to_dict(exclude=["logger"]))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'object_to_model' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class DifficultyFactory:
    logger: Logger = Logger.get_logger(name="DifficultyFactory")

    @classmethod
    def create_difficulty(
        cls,
        name: str,
        value: float,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[Difficulty]:
        """
        Creates a new instance of the Difficulty class.

        Args:
            name (str): The name of the difficulty.
            value (float): The value of the difficulty.
            created_at (Optional[datetime]): The timestamp when the difficulty was created.
            id (Optional[int]): The ID of the difficulty.
            key (Optional[str]): The key of the difficulty.
            updated_at (Optional[datetime]): The timestamp when the difficulty was last updated.
            uuid (Optional[str]): The UUID of the difficulty.

        Returns:
            Optional[Difficulty]: The new instance of the Difficulty class.
        """
        try:
            # Attempt to create and return a Difficulty object
            return Difficulty(
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
                message=f"Caught an exception while attempting to run 'create_difficulty' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class DifficultyManager(BaseObjectManager):
    pass


class DifficultyModel(ImmutableBaseModel):
    """
    A model class representing a difficulty.

    A difficulty has a value between 0 and 1 that represents the importance of an object.

    Attributes:
        name (str): The name of the difficulty.
        value (float): The value of the difficulty.
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
        Initializes a new instance of the DifficultyModel class.

        Args:
            created_at (Optional[datetime]): The timestamp when the difficulty was created.
            id (Optional[int]): The ID of the difficulty.
            key (Optional[str]): The key of the difficulty.
            name (Optional[str]): The name of the difficulty.
            updated_at (Optional[datetime]): The timestamp when the difficulty was last updated.
            uuid (Optional[str]): The UUID of the difficulty.
            value (Optional[float]): The value of the difficulty.

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
