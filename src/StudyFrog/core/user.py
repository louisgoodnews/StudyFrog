"""
Author: lodego
Date: 2025-02-09
"""

import asyncio

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
    "ImmutableUser",
    "MutableUser",
    "UserConverter",
    "UserFactory",
    "UserManager",
    "UserModel",
]


class ImmutableUser(ImmutableBaseObject):
    """
    An immutable class representing a user.

    Attributes:
        name (str): The name of the user.
        created_at (Optional[datetime]): The timestamp when the user was created.
        icon (Optional[str]): The icon of the user.
        id (Optional[int]): The ID of the user.
        key (Optional[str]): The key of the user.
        metadata (Optional[Dict[str, Any]]): The metadata of the user.
        updated_at (Optional[datetime]): The timestamp when the user was last updated.
        uuid (Optional[str]): The UUID of the user.
    """

    def __init__(
        self,
        name: str,
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "👤",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the ImmutableUser class.

        Args:
            name (str): The name of the user.
            created_at (Optional[datetime]): The timestamp when the user was created.
            icon (Optional[str]): The icon of the user. Defaults to "👤".
            id (Optional[int]): The ID of the user.
            key (Optional[str]): The key of the user.
            metadata (Optional[Dict[str, Any]]): The metadata of the user.
            updated_at (Optional[datetime]): The timestamp when the user was last updated.
            uuid (Optional[str]): The UUID of the user.

        Returns:
            None
        """
        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            icon=icon,
            id=id,
            key=key,
            metadata=metadata,
            name=name,
            updated_at=updated_at,
            uuid=uuid,
        )

    def to_mutable(self) -> "MutableUser":
        """
        Converts the immutable user to a mutable user.

        Returns:
            MutableUser: The mutable user.
        """
        return MutableUser(
            **self.to_dict(
                exclude=[
                    "_logger",
                ]
            )
        )


class MutableUser(MutableBaseObject):
    """
    A mutable class representing a user.

    Attributes:
        name (str): The name of the user.
        created_at (Optional[datetime]): The timestamp when the user was created.
        icon (Optional[str]): The icon of the user.
        id (Optional[int]): The ID of the user.
        key (Optional[str]): The key of the user.
        metadata (Optional[Dict[str, Any]]): The metadata of the user.
        updated_at (Optional[datetime]): The timestamp when the user was last updated.
        uuid (Optional[str]): The UUID of the user.
    """

    def __init__(
        self,
        name: str,
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "👤",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableUser class.

        Args:
            name (str): The name of the user.
            created_at (Optional[datetime]): The timestamp when the user was created.
            icon (Optional[str]): The icon of the user. Defaults to "👤".
            id (Optional[int]): The ID of the user.
            key (Optional[str]): The key of the user.
            metadata (Optional[Dict[str, Any]]): The metadata of the user.
            updated_at (Optional[datetime]): The timestamp when the user was last updated.
            uuid (Optional[str]): The UUID of the user.

        Returns:
            None
        """
        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            icon=icon,
            id=id,
            key=key,
            metadata=metadata,
            name=name,
            updated_at=updated_at,
            uuid=uuid,
        )

    def to_immutable(self) -> ImmutableUser:
        """
        Converts the mutable user to an immutable user.

        Returns:
            ImmutableUser: The immutable user.
        """
        return ImmutableUser(
            **self.to_dict(
                exclude=[
                    "_logger",
                ]
            )
        )


class UserConverter:
    """
    A converter class for transforming between UserModel and ImmutableUser instances.

    This class provides methods to convert a UserModel instance to an ImmutableUser instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the UserConverter class.
    """

    logger: Final[Logger] = Logger.get_logger(name="UserConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "UserModel",
    ) -> Optional[ImmutableUser]:
        """
        Converts a given UserModel instance to an ImmutableUser instance.

        Args:
            model (UserModel): The UserModel instance to be converted.

        Returns:
            ImmutableUser: The converted ImmutableUser instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the UserModel instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableUser class from the dictionary representation of the UserModel instance
            return ImmutableUser(
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
        object: ImmutableUser,
    ) -> Optional["UserModel"]:
        """
        Converts a given ImmutableUser instance to a UserModel instance.

        Args:
            object (ImmutableUser): The ImmutableUser instance to be converted.

        Returns:
            UserModel: The converted UserModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the ImmutableUser instance.
        """
        try:
            # Attempt to create and return a new instance of the UserModel class from the dictionary representation of the ImmutableUser instance
            return UserModel(
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


class UserFactory:
    """
    A factory class for creating instances of the ImmutableUser class.

    Attributes:
        logger (Logger): The logger instance associated with the UserFactory class.
    """

    logger: Final[Logger] = Logger.get_logger(name="UserFactory")

    @classmethod
    def create_user(
        cls,
        name: str,
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "👤",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutableUser]:
        """
        Creates and returns a new instance of the ImmutableUser class.

        Args:
            name (str): The name of the user.
            created_at (Optional[datetime]): The timestamp when the user was created.
            icon (Optional[str]): The icon of the user. Defaults to "👤".
            id (Optional[int]): The ID of the user.
            key (Optional[str]): The key of the user.
            metadata (Optional[Dict[str, Any]]): The metadata of the user.
            updated_at (Optional[datetime]): The timestamp when the user was last updated.
            uuid (Optional[str]): The UUID of the user.

        Returns:
            ImmutableUser: The created ImmutableUser instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to create the ImmutableUser instance.
        """
        try:
            # Attempt to create and return a new instance of the ImmutableUser class
            return ImmutableUser(
                created_at=created_at,
                icon=icon,
                id=id,
                key=key,
                metadata=metadata,
                name=name,
                updated_at=updated_at,
                uuid=uuid,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_user' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class UserBuilder(BaseObjectBuilder):
    """ """

    pass


class UserManager(BaseObjectManager):
    """
    A manager class for managing users in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for users.

    Attributes:
        cache: (List[Any]): The cache for storing users.
        logger (Logger): The logger instance associated with the object.
    """

    _shared_instance: Optional["UserManager"] = None

    def __new__(cls) -> "UserManager":
        """
        Creates and returns a new instance of the UserManager class.

        If the instance does not exist, creates a new one by calling the parent class
        constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Returns:
            UserManager: The created or existing instance of UserManager class.
        """
        if cls._shared_instance is None:
            # Create a new instance by calling the parent class constructor
            cls._shared_instance = super(UserManager, cls).__new__(cls)
            # Initialize the instance
            cls._shared_instance.init()
        # Return the shared instance
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes a new instance of the UserManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def count_users(self) -> int:
        """
        Returns the number of users in the database.

        Returns:
            int: The number of users in the database.
        """
        try:
            # Count and return the number of users in the database
            return asyncio.run(UserModel.count(database=Constants.DATABASE_PATH))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_user(
        self,
        user: Union[ImmutableUser, MutableUser],
    ) -> Optional[ImmutableUser]:
        """
        Creates a new user in the database.

        Args:
            user (Union[ImmutableUser, MutableUser]): The user to be created.

        Returns:
            Optional[ImmutableUser]: The newly created immutable user if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the user.
        """
        try:
            # Check if the user object is immutable
            if isinstance(
                user,
                ImmutableUser,
            ):
                # If it is, convert it to a mutable user
                user = MutableUser(
                    **user.to_dict(
                        exclude=[
                            "_logger",
                        ]
                    )
                )

            # Set the created_at timestamp of the user
            user.created_at = Miscellaneous.get_current_datetime()

            # Set the key of the user
            user.key = f"USER_{self.count_users() + 1}"

            # Set the updated_at timestamp of the user
            user.updated_at = Miscellaneous.get_current_datetime()

            # Set the uuid of the user
            user.uuid = Miscellaneous.get_uuid()

            # Convert the user object to a UserModel object
            model: UserModel = UserConverter.object_to_model(object=user)

            # Create a new user in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            if id:
                # Set the ID of the user
                user.id = id

                # Convert the user to an immutable user
                user = ImmutableUser(
                    **user.to_dict(
                        exclude=[
                            "_logger",
                        ]
                    )
                )

                # Add the user to the cache
                self.add_to_cache(
                    key=user.key,
                    value=user,
                )

                # Return the newly created immutable user
                return user

            # Log a warning message indicating an error has occurred
            self.logger.warning(
                message=f"It seems that an error has occured while attempting to create a user ({user}) in the database."
            )

            # Return None indicating an error has occurred
            return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_user' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete_user(
        self,
        user: Union[ImmutableUser, MutableUser],
    ) -> bool:
        """
        Deletes a user from the database.

        Args:
            user (Union[ImmutableUser, MutableUser]): The user to be deleted.

        Returns:
            bool: True if the user was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the user to an immutable user and delete the user from the database
            result: bool = asyncio.run(
                UserConverter.object_to_model(
                    object=ImmutableUser(
                        **user.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).delete()
            )

            # Return True if the user was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all_users(self) -> Optional[List[ImmutableUser]]:
        """
        Returns a list of all users in the database.

        Returns:
            Optional[List[ImmutableUser]]: A list of all users in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if cache and table size are equal
            if self.cache and len(self._cache) == self.count_users():
                # Return the list of immutable users from the cache
                return self.get_cache_values()

            # Get all users from the database
            models: List[UserModel] = asyncio.run(
                UserModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of UserModel objects to a list of ImmutableUser objects
            users: List[ImmutableUser] = [
                ImmutableUser(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable users
            for user in users:
                if not self.is_key_in_cache(key=user.key):
                    # Add the immutable user to the cache
                    self.add_to_cache(
                        key=user.key,
                        value=user,
                    )
                else:
                    # Update the immutable user in the cache
                    self.update_in_cache(
                        key=user.key,
                        value=user,
                    )

            # Return the list of immutable users
            return users
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_user_by(
        self,
        field: str,
        value: Any,
    ) -> Optional[ImmutableUser]:
        """
        Returns a user with the given field and value.

        Args:
            field (str): The field to search by.
            value (Any): The value to search for.

        Returns:
            Optional[ImmutableUser]: The user with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Get the user with the given field and value from the database
            model: Optional[UserModel] = asyncio.run(
                UserModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Convert the UserModel object to an ImmutableUser object
            user: Optional[ImmutableUser] = UserConverter.model_to_object(
                model=model,
            )

            # Return the user if it exists
            if model is not None:
                # Return the user
                return user
            else:
                # Return None indicating that the user does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_user_by_id(
        self,
        id: int,
    ) -> Optional[ImmutableUser]:
        """
        Returns a user with the given ID.

        Args:
            id (int): The ID of the user.

        Returns:
            Optional[ImmutableUser]: The user with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the user is already in the cache
            if self.is_key_in_cache(key=f"USER_{id}"):
                # Return the user from the cache
                return self.get_value_from_cache(key=f"USER_{id}")

            # Get the user with the given ID from the database
            model: Optional[UserModel] = asyncio.run(
                UserModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the user if it exists
            if model is not None:
                # Convert the UserModel object to an ImmutableUser object
                return ImmutableUser(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the user does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_user_by_uuid(
        self,
        uuid: str,
    ) -> Optional[ImmutableUser]:
        """
        Returns a user with the given UUID.

        Args:
            uuid (str): The UUID of the user.

        Returns:
            Optional[ImmutableUser]: The user with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the user is already in the cache
            if self.is_key_in_cache(key=uuid):
                # Return the user from the cache
                return self.get_value_from_cache(key=uuid)

            # Get the user with the given UUID from the database
            model: Optional[UserModel] = asyncio.run(
                UserModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the user if it exists
            if model is not None:
                # Convert the UserModel object to an ImmutableUser object
                return ImmutableUser(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the user does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def search_users(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[Union[List[ImmutableUser]]]:
        """
        Searches for users in the database.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            **kwargs: Any additional keyword arguments to be passed to the search method of the UserModel class.

        Returns:
            Optional[Union[List[ImmutableUser]]]: The found users if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Search the stack for the passed keyword arguments
                cached_result: Optional[List[ImmutableUser]] = self.search_cache(
                    **kwargs
                )

                # Check, if any cached results exist
                if cached_result:
                    # Return the cached results
                    return cached_result

            # Search for users in the database
            models: Optional[List[UserModel]] = asyncio.run(
                UserModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found users if any
            if models is not None and len(models) > 0:
                return [
                    ImmutableUser(
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
                # Return None indicating that no users were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_user(
        self,
        user: Union[ImmutableUser, MutableUser],
    ) -> Optional[ImmutableUser]:
        """
        Updates a user with the given ID.

        Args:
            user (Union[ImmutableUser, MutableUser]): The user to update.

        Returns:
            Optional[ImmutableUser]: The updated user if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the user to an immutable user and update the user in the database
            model: Optional[UserModel] = asyncio.run(
                UserConverter.object_to_model(
                    object=ImmutableUser(
                        **user.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).update(
                    database=Constants.DATABASE_PATH,
                    **user.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Return the updated user if it exists
            if model is not None:
                # Convert the UserModel object to an ImmutableUser object
                user = ImmutableUser(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the user to the cache
                self.update_in_cache(
                    key=user.key,
                    value=user,
                )

                # Return the updated user
                return user
            else:
                # Return None indicating that the user does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class UserModel(ImmutableBaseModel):
    """
    Represents the structure of the user model.

    Attributes:
        created_at (Field): The timestamp when the user was created.
        id (Field): The ID of the user.
        icon (Field): The icon of the user. Defaults to "👤".
        key (Field): The key of the user.
        metadata (Field): The metadata of the user.
        name (Field): The name of the user.
        table (str): The table name of the user model.
        updated_at (Field): The timestamp when the user was last updated.
        uuid (Field): The UUID of the user.
    """

    table: Final[str] = Constants.USERS

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
        default="👤",
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
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "👤",
        id: Optional[int] = None,
        key: Optional[str] = None,
        metadata: Optional[dict] = None,
        name: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the UserModel class.

        Args:
            created_at (Optional[datetime]): The timestamp when the user was created.
            icon (Optional[str]): The icon of the user. Defaults to "👤".
            id (Optional[int]): The ID of the user.
            key (Optional[str]): The key of the user.
            metadata (Optional[dict]): The metadata of the user.
            name (Optional[str]): The name of the user.
            updated_at (Optional[datetime]): The timestamp when the user was last updated.
            uuid (Optional[str]): The UUID of the user.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            created_at=created_at,
            icon="👤",
            id=id,
            key=key,
            metadata=metadata,
            name=name,
            table=Constants.USERS,
            updated_at=updated_at,
            uuid=uuid,
        )
