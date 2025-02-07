"""
Author: lodego
Date: 2025-02-06
"""

import asyncio

import uuid

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
        association_type (str): The type of the association.
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
        association_type: str,
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
            association_type (str): The type of the association.
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
            association_type=association_type,
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
            return Association(**model.to_dict(exclude=["_logger"])["fields"])
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
            return AssociationModel(**object.to_dict(exclude=["_logger"]))
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
        association_type: str,
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
            association_type (str): The type of the association.
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
                association_type=association_type,
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
    """
    A manager class for managing associations in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for associations.

    Attributes:
        cache: (List[Any]): The cache for storing associations.
        logger (Logger): The logger instance associated with the object.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the AssociationManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def associate(
        self,
        association_type: str,
        source: Any,
        target: Any,
    ) -> bool:
        """
        Associates two objects in the database by creating an Association.

        Args:
            association_type (str): The type of the association.
            source (Any): The first object in the association.
            target (Any): The second object in the association.

        Returns:
            bool: True if the association was created successfully, False otherwise.

        Raises:
            Exception: If an exception occurs while attempting to associate the objects.
        """
        try:
            # Create an Association object
            association: Association = AssociationFactory.create_association(
                association_type=association_type,
                source=source,
                target=target,
            )

            # Create the association in the database
            self.create(association=association)

            # Return True indicating the association was created successfully
            return True
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'associate' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def count(self) -> int:
        """
        Returns the number of associations in the database.

        Returns:
            int: The number of associations in the database.
        """
        try:
            # Count the number of associations in the database
            result: Any = asyncio.run(
                AssociationModel.execute(
                    database=Constants.DATABASE_PATH,
                    sql=f"SELECT COUNT(*) FROM {Constants.ASSOCIATIONS};",
                )
            )

            # Return the number of associations in the database
            return result[0][0] if result else 0
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create(
        self,
        association: Association,
    ) -> Optional[Association]:
        """
        Creates a new association in the database.

        Args:
            association (Association): The association to be created.

        Returns:
            Optional[Association]: The newly created immutable association if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the association.
        """
        try:
            # Set the created_at timestamp of the association
            association.created_at = Miscellaneous.get_current_datetime()

            # Set the key of the association
            association.key = f"FLASHCARD_{self.count() + 1}"

            # Set the updated_at timestamp of the association
            association.updated_at = Miscellaneous.get_current_datetime()

            # Set the uuid of the association
            association.uuid = str(uuid.uuid4())

            # Convert the association object to a AssociationModel object
            model: AssociationModel = AssociationConverter.object_to_model(
                object=association
            )

            # Create a new association in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            if id:
                # Set the ID of the association
                association.id = id

                # Convert the association to an immutable association
                association = Association(**association.to_dict(exclude=["_logger"]))

                # Add the association to the cache
                self.add_to_cache(
                    key=association.key,
                    value=association,
                )

                # Return the newly created immutable association
                return association

            # Log a warning message indicating an error has occurred
            self.logger.warning(
                message=f"It seems that an error has occured while attempting to create a association ({association}) in the database."
            )

            # Return None indicating an error has occurred
            return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_association' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete(
        self,
        association: Association,
    ) -> bool:
        """
        Deletes a association from the database.

        Args:
            association (Association): The association to be deleted.

        Returns:
            bool: True if the association was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the association to an immutable association and delete the association from the database
            result: bool = asyncio.run(
                AssociationConverter.object_to_model(
                    object=Association(**association.to_dict(exclude=["_logger"]))
                ).delete()
            )

            # Return True if the association was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all(self) -> Optional[List[Association]]:
        """
        Returns a list of all associations in the database.

        Returns:
            Optional[List[Association]]: A list of all associations in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if cache and table size are equal
            if self.cache and len(self._cache) == self.count():
                # Return the list of immutable associations from the cache
                return self.get_cache_values()

            # Get all associations from the database
            models: List[AssociationModel] = asyncio.run(
                AssociationModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of AssociationModel objects to a list of Association objects
            associations: List[Association] = [
                Association(**model.to_dict(exclude=["_logger"])) for model in models
            ]

            # Iterate over the list of immutable associations
            for association in associations:
                if not self.is_key_in_cache(key=association.key):
                    # Add the immutable association to the cache
                    self.add_to_cache(
                        key=association.key,
                        value=association,
                    )
                else:
                    # Update the immutable association in the cache
                    self.update_in_cache(
                        key=association.key,
                        value=association,
                    )

            # Return the list of immutable associations
            return associations
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_by_id(
        self,
        id: int,
    ) -> Optional[Association]:
        """
        Returns a association with the given ID.

        Args:
            id (int): The ID of the association.

        Returns:
            Optional[Association]: The association with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the association is already in the cache
            if self.is_key_in_cache(key=f"FLASHCARD_{id}"):
                # Return the association from the cache
                return self.get_value_from_cache(key=f"FLASHCARD_{id}")

            # Get the association with the given ID from the database
            model: Optional[AssociationModel] = asyncio.run(
                AssociationModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the association if it exists
            if model is not None:
                # Convert the AssociationModel object to an Association object
                return Association(**model.to_dict(exclude=["_logger"]))
            else:
                # Return None indicating that the association does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_by_uuid(
        self,
        uuid: str,
    ) -> Optional[Association]:
        """
        Returns a association with the given UUID.

        Args:
            uuid (str): The UUID of the association.

        Returns:
            Optional[Association]: The association with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the association is already in the cache
            if self.is_key_in_cache(key=uuid):
                # Return the association from the cache
                return self.get_value_from_cache(key=uuid)

            # Get the association with the given UUID from the database
            model: Optional[AssociationModel] = asyncio.run(
                AssociationModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the association if it exists
            if model is not None:
                # Convert the AssociationModel object to an Association object
                return Association(**model.to_dict(exclude=["_logger"]))
            else:
                # Return None indicating that the association does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update(
        self,
        association: Association,
    ) -> Optional[Association]:
        """
        Updates a association with the given ID.

        Args:
            association (Association): The association to update.

        Returns:
            Optional[Association]: The updated association if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the association to an immutable association and update the association in the database
            model: Optional[AssociationModel] = asyncio.run(
                AssociationConverter.object_to_model(
                    object=Association(**association.to_dict(exclude=["_logger"]))
                ).update(
                    **association.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    )
                )
            )

            # Return the updated association if it exists
            if model is not None:
                # Convert the AssociationModel object to an Association object
                association = Association(**model.to_dict(exclude=["_logger"]))

                # Add the association to the cache
                self.update_in_cache(
                    key=association.key,
                    value=association,
                )

                # Return the updated association
                return association
            else:
                # Return None indicating that the association does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


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

    table: str = Constants.ASSOCIATIONS

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

    association_type: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="association_type",
        nullable=True,
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
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="DATETIME",
        unique=False,
    )

    key: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="key",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=True,
    )

    source: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="source",
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="JSON",
        unique=False,
    )

    target: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        foreign_key=None,
        index=False,
        name="target",
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
        nullable=True,
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
        nullable=True,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=False,
    )

    def __init__(
        self,
        association_type: Optional[str] = None,
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
            association_type (Optional[str]): The type of the association.
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
            association_type=association_type,
            created_at=created_at,
            id=id,
            key=key,
            source=source,
            table=Constants.ASSOCIATIONS,
            target=target,
            updated_at=updated_at,
            uuid=uuid,
        )
