"""
Author: lodego
Date: 2025-02-06
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
    "Association",
    "AssociationConverter",
    "AssociationFactory",
    "AssociationManager",
    "AssociationModel",
]


class Association(ImmutableBaseObject):
    """
    An immutable class representing an association between two entities.

    Attributes:
        source (Dict[str, Any]): The source of the association.
        target (Dict[str, Any]): The target of the association.
        created_at (datetime): The timestamp when the association was created.
        id (int): The ID of the association.
        key (str): The key of the association.
        updated_at (datetime): The timestamp when the association was last updated.
        uuid (str): The UUID of the association.
    """

    def __init__(
        self,
        source: Dict[str, Any],
        target: Dict[str, Any],
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the Association class.

        Args:
            source (Dict[str, Any]): The source of the association.
            target (Dict[str, Any]): The target of the association.
            created_at (Optional[datetime]): The timestamp when the association was created.
            id (Optional[int]): The ID of the association.
            key (Optional[str]): The key of the association.
            updated_at (Optional[datetime]): The timestamp when the association was last updated.
            uuid (Optional[str]): The UUID of the association.

        Returns:
            None
        """

        if not all(
            [
                key in source
                for key in [
                    "id",
                    "type",
                    "uuid",
                ]
            ]
        ):
            raise ValueError("'source' must have id, type, and uuid.")

        if not all(
            [
                key in target
                for key in [
                    "id",
                    "type",
                    "uuid",
                ]
            ]
        ):
            raise ValueError("'target' must have id, type, and uuid.")

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            id=id,
            key=key,
            source=source,
            target=target,
            updated_at=updated_at,
            uuid=uuid,
        )


class AssociationConverter:
    """
    A converter class for transforming between AssociationModel and Association instances.

    This class provides methods to convert a AssociationModel instance to an Association instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the AssociationConverter class.
    """

    logger: Logger = Logger.get_logger(name="AssociationConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "AssociationModel",
    ) -> Optional[Association]:
        """
        Converts a given AssociationModel instance to an Association instance.

        Args:
            model (AssociationModel): The AssociationModel instance to be converted.

        Returns:
            Association: The converted Association instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the AssociationModel instance.
        """
        try:
            # Attempt to create and return a new instance of the Association class from the dictionary representation of the AssociationModel instance
            return Association(**model.to_dict(exclude=["logger"])["fields"])
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
        object: Association,
    ) -> Optional["AssociationModel"]:
        """
        Converts a given Association instance to a AssociationModel instance.

        Args:
            object (Association): The Association instance to be converted.

        Returns:
            AssociationModel: The converted AssociationModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the Association instance.
        """
        try:
            # Attempt to create and return a new instance of the AssociationModel class from the dictionary representation of the Association instance
            return AssociationModel(**object.to_dict(exclude=["logger"]))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'object_to_model' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class AssociationFactory:
    """
    A factory class used to create instances of Association class.

    Attributes:
        logger (Logger): The logger instance associated with the object.
    """

    logger: Logger = Logger.get_logger(name="AssociationFactory")

    @classmethod
    def create_association(
        cls,
        source: Dict[str, Any],
        target: Dict[str, Any],
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[Association]:
        """
        Creates and returns a new instance of Association class.

        Args:
            source (Dict[str, Any]): The dictionary representation of the source object.
            target (Dict[str, Any]): The dictionary representation of the target object.
            created_at (Optional[datetime]): The timestamp when the association was created.
            id (Optional[int]): The ID of the association.
            key (Optional[str]): The key of the association.
            updated_at (Optional[datetime]): The timestamp when the association was last updated.
            uuid (Optional[str]): The UUID of the association.

        Returns:
            Optional[Association]: The created association object if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the association.
        """
        try:
            # Attempt to create an d return an Association object
            return Association(
                created_at=created_at,
                id=id,
                key=key,
                source=source,
                target=target,
                updated_at=updated_at,
                uuid=uuid,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_association' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class AssociationManager(BaseObjectManager):
    pass


class AssociationModel(ImmutableBaseModel):
    """
    Represents the structure of a association model.

    Attributes:
        ancestor (Optional[int]): The ID of the ancestor association.
        back_text (Optional[str]): The back side of the association.
        children (Optional[List[int]]): The IDs of the children associations.
        created_at (Optional[datetime]): The timestamp when the association was created.
        front_text (Optional[str]): The front side of the association.
        id (Optional[int]): The ID of the association.
        key (Optional[str]): The key of the association.
        updated_at (Optional[datetime]): The timestamp when the association was last updated.
        uuid (Optional[str]): The UUID of the association.
    """

    def __init__(
        self,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
        key: Optional[str] = None,
        source: Optional[Dict[str, Any]] = None,
        target: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the AssociationModel class.

        Args:
            created_at (Optional[datetime]): The timestamp when the association was created.
            key (Optional[str]): The key of the association.
            source (Optional[Dict[str, Any]]): The dictionary representation of the source object.
            target (Optional[Dict[str, Any]]): The dictionary representation of the target object.
            updated_at (Optional[datetime]): The timestamp when the association was last updated.
            uuid (Optional[str]): The UUID of the association.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            table="associations",
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
            source=(
                source
                or Field(
                    autoincrement=False,
                    default=None,
                    description="",
                    foreign_key=None,
                    index=False,
                    name="source",
                    nullable=True,
                    on_delete="NO ACTION",
                    on_update="NO ACTION",
                    primary_key=False,
                    size=None,
                    type="JSON",
                    unique=False,
                )
            ),
            target=(
                target
                or Field(
                    autoincrement=False,
                    default=None,
                    description="",
                    foreign_key=None,
                    index=False,
                    name="target",
                    nullable=True,
                    on_delete="NO ACTION",
                    on_update="NO ACTION",
                    primary_key=False,
                    size=None,
                    type="JSON",
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
