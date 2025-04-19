"""
Author: lodego
Date: 2025-02-05
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


__all__: Final[List[str]] = [
    "ImmutableDifficulty",
    "MutableDifficulty",
    "DifficultyConverter",
    "DifficultyFactory",
    "DifficultyManager",
    "DifficultyModel",
]


class ImmutableDifficulty(ImmutableBaseObject):
    """
    An immutable class representing a difficulty.

    A difficulty has a value between 0 and 1 that represents the importance of an object.

    Attributes:
        emoji (str): The emoji of the difficulty.
        name (str): The name of the difficulty.
        value (float): The value of the difficulty.
        created_at (datetime): The timestamp when the difficulty was created.
        icon (str): The icon of the difficulty.
        id (int): The ID of the difficulty.
        key (str): The key of the difficulty.
        updated_at (datetime): The timestamp when the difficulty was last updated.
        uuid (str): The UUID of the difficulty.
    """

    def __init__(
        self,
        emoji: str,
        name: str,
        value: float,
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "⭐",
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the Difficulty class.

        Args:
            emoji (str): The emoji of the difficulty.
            name (str): The name of the difficulty.
            value (float): The value of the difficulty.
            created_at (Optional[datetime]): The timestamp when the difficulty was created.
            icon (Optional[str]): The icon of the difficulty. Defaults to "⭐".
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
            emoji=emoji,
            icon=icon,
            id=id,
            key=key,
            name=name,
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )

    def to_mutable(self) -> "MutableDifficulty":
        """
        Converts the immutable difficulty to a mutable difficulty.

        Returns:
            MutableDifficulty: The mutable difficulty.
        """

        # Return a new instance of the MutableDifficulty class
        return MutableDifficulty(
            **self.to_dict(
                exclude=[
                    "_logger",
                ]
            )
        )


class MutableDifficulty(MutableBaseObject):
    """
    A mutable class representing a difficulty.

    A difficulty has a value between 0 and 1 that represents the importance of an object.

    Attributes:
        emoji (str): The emoji of the difficulty.
        name (str): The name of the difficulty.
        value (float): The value of the difficulty.
        created_at (datetime): The timestamp when the difficulty was created.
        icon (str): The icon of the difficulty.
        id (int): The ID of the difficulty.
        key (str): The key of the difficulty.
        updated_at (datetime): The timestamp when the difficulty was last updated.
        uuid (str): The UUID of the difficulty.
    """

    def __init__(
        self,
        emoji: str,
        name: str,
        value: float,
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "⭐",
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the MutableDifficulty class.

        Args:
            emoji (str): The emoji of the difficulty.
            name (str): The name of the difficulty.
            value (float): The value of the difficulty.
            created_at (Optional[datetime]): The timestamp when the difficulty was created.
            icon (Optional[str]): The icon of the difficulty. Defaults to "⭐".
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
            emoji=emoji,
            icon=icon,
            id=id,
            key=key,
            name=name,
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )

    def to_immutable(self) -> ImmutableDifficulty:
        """
        Converts the mutable difficulty to an immutable difficulty.

        Returns:
            ImmutableDifficulty: The immutable difficulty.
        """

        # Return a new instance of the ImmutableDifficulty class
        return ImmutableDifficulty(
            **self.to_dict(
                exclude=[
                    "_logger",
                ]
            )
        )


class DifficultyConverter:
    """
    A converter class for transforming between DifficultyModel and Difficulty instances.

    This class provides methods to convert a DifficultyModel instance to an Difficulty instance,
    and vice versa. It utilizes a logger to capture and log exceptions that may occur during the conversion process.

    Attributes:
        logger (Logger): The logger instance associated with the DifficultyConverter class.
    """

    logger: Final[Logger] = Logger.get_logger(name="DifficultyConverter")

    @classmethod
    def model_to_object(
        cls,
        model: "DifficultyModel",
    ) -> Optional[ImmutableDifficulty]:
        """
        Converts a given DifficultyModel instance to an ImmutableDifficulty instance.

        Args:
            model (DifficultyModel): The DifficultyModel instance to be converted.

        Returns:
            ImmutableDifficulty: The converted ImmutableDifficulty instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the DifficultyModel instance.
        """
        try:
            # Attempt to create and return a new instance of the Difficulty class from the dictionary representation of the DifficultyModel instance
            return ImmutableDifficulty(
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
        object: ImmutableDifficulty,
    ) -> Optional["DifficultyModel"]:
        """
        Converts a given ImmutableDifficulty instance to a DifficultyModel instance.

        Args:
            object (ImmutableDifficulty): The ImmutableDifficulty instance to be converted.

        Returns:
            DifficultyModel: The converted DifficultyModel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to convert the Difficulty instance.
        """
        try:
            # Attempt to create and return a new instance of the DifficultyModel class from the dictionary representation of the Difficulty instance
            return DifficultyModel(
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


class DifficultyFactory:
    """
    Factory class for creating Difficulty instances.

    Attributes:
        logger (Logger): The logger instance associated with the DifficultyFactory class.
    """

    logger: Final[Logger] = Logger.get_logger(name="DifficultyFactory")

    @classmethod
    def create_difficulty(
        cls,
        emoji: str,
        name: str,
        value: float,
        created_at: Optional[datetime] = None,
        icon: Optional[str] = "⭐",
        id: Optional[int] = None,
        key: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
    ) -> Optional[ImmutableDifficulty]:
        """
        Creates a new instance of the Difficulty class.

        Args:
            emoji (str): The emoji of the difficulty.
            name (str): The name of the difficulty.
            value (float): The value of the difficulty.
            created_at (Optional[datetime]): The timestamp when the difficulty was created.
            icon (Optional[str]): The icon of the difficulty. Defaults to "⭐".
            id (Optional[int]): The ID of the difficulty.
            key (Optional[str]): The key of the difficulty.
            updated_at (Optional[datetime]): The timestamp when the difficulty was last updated.
            uuid (Optional[str]): The UUID of the difficulty.

        Returns:
            Optional[ImmutableDifficulty]: The new instance of the Difficulty class.
        """
        try:
            # Attempt to create and return a Difficulty object
            return ImmutableDifficulty(
                created_at=created_at,
                emoji=emoji,
                icon=icon,
                id=id,
                key=key,
                name=name,
                updated_at=updated_at,
                uuid=uuid,
                value=value,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_difficulty' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class DifficultyManager(BaseObjectManager):
    """
    A manager class for managing difficulties in the application.

    This class extends the BaseObjectManager class and provides CRUD (Create, Read, Update, Delete) methods for difficulties.

    Attributes:
        cache: (List[Any]): The cache for storing difficulties.
        logger (Logger): The logger instance associated with the object.
    """

    _shared_instance: Optional["DifficultyManager"] = None

    def __new__(cls) -> "DifficultyManager":
        """
        Creates and returns a new instance of the DifficultyManager class.

        If the instance does not exist, creates a new one by calling the parent class
        constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Returns:
            DifficultyManager: The created or existing instance of DifficultyManager class.
        """
        if cls._shared_instance is None:
            # Create a new instance by calling the parent class constructor
            cls._shared_instance = super(DifficultyManager, cls).__new__(cls)
            # Initialize the instance
            cls._shared_instance.init()
        # Return the shared instance
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes a new instance of the DifficultyManager class.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

    def count_difficulties(self) -> int:
        """
        Returns the number of difficulties in the database.

        Returns:
            int: The number of difficulties in the database.
        """
        try:
            # Count the number of difficulties in the database
            result: Any = asyncio.run(
                DifficultyModel.execute(
                    database=Constants.DATABASE_PATH,
                    sql=f"SELECT COUNT(*) FROM {Constants.DIFFICULTIES};",
                )
            )

            # Return the number of difficulties in the database
            return result[0][0] if result else 0
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'count' method from '{self.__class__.__name__}': {e}"
            )

            # Return 0 indicating an exception has occurred
            return 0

    def create_difficulty(
        self,
        difficulty: ImmutableDifficulty,
    ) -> Optional[ImmutableDifficulty]:
        """
        Creates a new difficulty in the database.

        Args:
            difficulty (ImmutableDifficulty): The difficulty to be created.

        Returns:
            Optional[ImmutableDifficulty]: The newly created immutable difficulty if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the difficulty.
        """
        try:
            # Check if the difficulty object is immutable
            if isinstance(
                difficulty,
                ImmutableDifficulty,
            ):
                # If it is, convert it to a mutable difficulty
                difficulty = MutableDifficulty(
                    **difficulty.to_dict(
                        exclude=[
                            "_logger",
                        ]
                    )
                )

            # Set the created_at timestamp of the difficulty
            difficulty.created_at = Miscellaneous.get_current_datetime()

            # Set the key of the difficulty
            difficulty.key = f"DIFFICULTY_{self.count_difficulties() + 1}"

            # Set the updated_at timestamp of the difficulty
            difficulty.updated_at = Miscellaneous.get_current_datetime()

            # Set the uuid of the difficulty
            difficulty.uuid = Miscellaneous.get_uuid()

            # Convert the difficulty object to a DifficultyModel object
            model: DifficultyModel = DifficultyConverter.object_to_model(
                object=difficulty
            )

            # Create a new difficulty in the database
            id: Optional[int] = asyncio.run(
                model.create(database=Constants.DATABASE_PATH)
            )

            if id:
                # Set the ID of the difficulty
                difficulty.id = id

                # Convert the difficulty to an immutable difficulty
                difficulty = ImmutableDifficulty(
                    **difficulty.to_dict(
                        exclude=[
                            "_logger",
                        ]
                    )
                )

                # Add the difficulty to the cache
                self.add_to_cache(
                    key=difficulty.key,
                    value=difficulty,
                )

                # Return the newly created immutable difficulty
                return difficulty

            # Log a warning message indicating an error has occurred
            self.logger.warning(
                message=f"It seems that an error has occured while attempting to create a difficulty ({difficulty}) in the database."
            )

            # Return None indicating an error has occurred
            return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_difficulty' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def delete_difficulty(
        self,
        difficulty: ImmutableDifficulty,
    ) -> bool:
        """
        Deletes a difficulty from the database.

        Args:
            difficulty (ImmutableDifficulty): The difficulty to be deleted.

        Returns:
            bool: True if the difficulty was deleted successfully. False otherwise.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the difficulty to an immutable difficulty and delete the difficulty from the database
            result: bool = asyncio.run(
                DifficultyConverter.object_to_model(
                    object=ImmutableDifficulty(
                        **difficulty.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).delete()
            )

            # Return True if the difficulty was deleted successfully
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'delete' method from '{self.__class__.__name__}': {e}"
            )

            # Return False indicating an exception has occurred
            return False

    def get_all_difficulties(self) -> Optional[List[ImmutableDifficulty]]:
        """
        Returns a list of all difficulties in the database.

        Returns:
            Optional[List[ImmutableDifficulty]]: A list of all difficulties in the database if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if cache and table size are equal
            if self.cache and len(self._cache) == self.count_difficulties():
                # Return the list of immutable difficulties from the cache
                return self.get_cache_values()

            # Get all difficulties from the database
            models: List[DifficultyModel] = asyncio.run(
                DifficultyModel.get_all(database=Constants.DATABASE_PATH)
            )

            # Convert the list of DifficultyModel objects to a list of Difficulty objects
            difficulties: List[ImmutableDifficulty] = [
                ImmutableDifficulty(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
                for model in models
            ]

            # Iterate over the list of immutable difficulties
            for difficulty in difficulties:
                if not self.is_key_in_cache(key=difficulty.key):
                    # Add the immutable difficulty to the cache
                    self.add_to_cache(
                        key=difficulty.key,
                        value=difficulty,
                    )
                else:
                    # Update the immutable difficulty in the cache
                    self.update_in_cache(
                        key=difficulty.key,
                        value=difficulty,
                    )

            # Return the list of immutable difficulties
            return difficulties
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_default_difficulties(self) -> Optional[List[ImmutableDifficulty]]:
        """
        Retrieves the default difficulties from the database.

        Returns:
            Optional[List[ImmutableDifficulty]]: A list of default difficulties if no exception occurs. Otherwise, None.

        Raises:
            Exception: If no 'difficulty' defaults are found or any other exception occurs.
        """
        try:
            # Import necessary classes
            from core.default import ImmutableDefault, DefaultManager

            # Initialize an empty list to store the difficulties
            result: List[ImmutableDifficulty] = []

            # Retrieve defaults with the name 'difficulty'
            defaults: Optional[List[ImmutableDefault]] = [
                DefaultManager().get_default_by(
                    field="name",
                    value=f"difficulty:{difficulty}",
                )
                for difficulty in [
                    Constants.HARD,
                    Constants.MEDIUM,
                    Constants.EASY,
                ]
            ]

            # Raise exception if no defaults are found
            if not defaults:
                raise Exception("Found no 'difficulty' defaults in the database.")

            # Iterate over each default
            for default in defaults:
                # Check if the difficulty already exists
                existing_difficulty: Optional[ImmutableDifficulty] = (
                    self.get_difficulty_by(
                        field="name",
                        value=default.value,
                    )
                )

                if not existing_difficulty:
                    # Create a new difficulty if it doesn't exist
                    difficulty: ImmutableDifficulty = (
                        DifficultyFactory.create_difficulty(
                            emoji=(
                                "⭐"
                                if default.value.lower() == Constants.EASY
                                else (
                                    "⭐⭐"
                                    if default.value.lower() == Constants.MEDIUM
                                    else "⭐⭐⭐"
                                )
                            ),
                            name=default.value,
                            value=(
                                float(1 / 3)
                                if default.value.lower() == Constants.EASY
                                else (
                                    float(2 / 3)
                                    if default.value.lower() == Constants.MEDIUM
                                    else 1.0
                                )
                            ),
                        )
                    )

                    # Add the newly created difficulty to the result
                    result.append(self.create_difficulty(difficulty=difficulty))
                else:
                    # If the difficulty exists, retrieve it from the database
                    result.append(existing_difficulty)

            # Return the list of difficulties
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_default_difficulties' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_difficulty_by(
        self,
        field: str,
        value: Any,
    ) -> Optional[ImmutableDifficulty]:
        """
        Retrieves a difficulty by the given field and value.

        Args:
            field (str): The field to search by.
            value (Any): The value to search for.

        Returns:
            Optional[ImmutableDifficulty]: The difficulty with the given field and value if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the difficulty is already in the cache
            if self.is_key_in_cache(key=field):
                # Return the difficulty from the cache
                return self.get_value_from_cache(key=field)

            # Get the difficulty with the given field and value from the database
            model: Optional[DifficultyModel] = asyncio.run(
                DifficultyModel.get_by(
                    column=field,
                    database=Constants.DATABASE_PATH,
                    value=value,
                )
            )

            # Return the difficulty if it exists
            if model is not None:
                # Convert the DifficultyModel object to an Difficulty object
                return ImmutableDifficulty(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the difficulty does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_difficulty_by_id(
        self,
        id: int,
    ) -> Optional[ImmutableDifficulty]:
        """
        Returns a difficulty with the given ID.

        Args:
            id (int): The ID of the difficulty.

        Returns:
            Optional[ImmutableDifficulty]: The difficulty with the given ID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the difficulty is already in the cache
            if self.is_key_in_cache(key=f"DIFFICULTY_{id}"):
                # Return the difficulty from the cache
                return self.get_value_from_cache(key=f"DIFFICULTY_{id}")

            # Get the difficulty with the given ID from the database
            model: Optional[DifficultyModel] = asyncio.run(
                DifficultyModel.get_by(
                    column="id",
                    database=Constants.DATABASE_PATH,
                    value=id,
                )
            )

            # Return the difficulty if it exists
            if model is not None:
                # Convert the DifficultyModel object to an Difficulty object
                return ImmutableDifficulty(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the difficulty does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_id' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_difficulty_by_uuid(
        self,
        uuid: str,
    ) -> Optional[ImmutableDifficulty]:
        """
        Returns a difficulty with the given UUID.

        Args:
            uuid (str): The UUID of the difficulty.

        Returns:
            Optional[ImmutableDifficulty]: The difficulty with the given UUID if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check if the difficulty is already in the cache
            if self.is_key_in_cache(key=uuid):
                # Return the difficulty from the cache
                return self.get_value_from_cache(key=uuid)

            # Get the difficulty with the given UUID from the database
            model: Optional[DifficultyModel] = asyncio.run(
                DifficultyModel.get_by(
                    column="uuid",
                    database=Constants.DATABASE_PATH,
                    value=uuid,
                )
            )

            # Return the difficulty if it exists
            if model is not None:
                # Convert the DifficultyModel object to an Difficulty object
                return ImmutableDifficulty(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )
            else:
                # Return None indicating that the difficulty does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_uuid' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def search_difficulties(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[Union[List[ImmutableDifficulty]]]:
        """
        Searches for difficulties in the database.

        Args:
            force_refetch (bool): Forces a search in the database, bypassing the cache. Defaults to False.
            **kwargs: Any additional keyword arguments to be passed to the search method of the DifficultyModel class.

        Returns:
            Optional[Union[List[ImmutableDifficulty]]]: The found difficulties if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Check, if the force refetch flag is set to False
            if not force_refetch:
                # Search the stack for the passed keyword arguments
                cached_result: Optional[List[ImmutableDifficulty]] = self.search_cache(**kwargs)

                # Check, if any cached results exist
                if cached_result:
                    # Return the cached results
                    return cached_result

            # Search for difficulties in the database
            models: Optional[List[DifficultyModel]] = asyncio.run(
                DifficultyModel.search(
                    database=Constants.DATABASE_PATH,
                    **kwargs,
                )
            )

            # Return the found difficulties if any
            if models is not None and len(models) > 0:
                return [
                    ImmutableDifficulty(
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
                # Return None indicating that no difficulties were found
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'search' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def update_difficulty(
        self,
        difficulty: ImmutableDifficulty,
    ) -> Optional[ImmutableDifficulty]:
        """
        Updates a difficulty with the given ID.

        Args:
            difficulty (ImmutableDifficulty): The difficulty to update.

        Returns:
            Optional[ImmutableDifficulty]: The updated difficulty if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Convert the difficulty to an immutable difficulty and update the difficulty in the database
            model: Optional[DifficultyModel] = asyncio.run(
                DifficultyConverter.object_to_model(
                    object=ImmutableDifficulty(
                        **difficulty.to_dict(
                            exclude=[
                                "_logger",
                            ]
                        )
                    )
                ).update(
                    database=Constants.DATABASE_PATH,
                    **difficulty.to_dict(
                        exclude=[
                            "_id",
                            "_key",
                            "_logger",
                            "_uuid",
                        ]
                    ),
                )
            )

            # Return the updated difficulty if it exists
            if model is not None:
                # Convert the DifficultyModel object to an Difficulty object
                difficulty = ImmutableDifficulty(
                    **model.to_dict(
                        exclude=[
                            "_logger",
                            "table",
                        ]
                    )
                )

                # Add the difficulty to the cache
                self.update_in_cache(
                    key=difficulty.key,
                    value=difficulty,
                )

                # Return the updated difficulty
                return difficulty
            else:
                # Return None indicating that the difficulty does not exist
                return None
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class DifficultyModel(ImmutableBaseModel):
    """
    A model class representing a difficulty.

    A difficulty has a value between 0 and 1 that represents the importance of an object.

    Attributes:
        id (int): The ID of the difficulty.
        created_at (datetime): The timestamp when the difficulty was created.
        emoji (str): The emoji of the difficulty.
        icon (str): The icon of the difficulty. Defaults to "⭐".
        key (str): The key of the difficulty.
        name (str): The name of the difficulty.
        value (float): The value of the difficulty.
        updated_at (datetime): The timestamp when the difficulty was last updated.
        uuid (str): The UUID of the difficulty.
    """

    table: Final[str] = Constants.DIFFICULTIES

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

    emoji: Field = Field(
        autoincrement=False,
        default=None,
        description="",
        index=False,
        name="emoji",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=255,
        type="VARCHAR",
        unique=True,
    )

    icon: Field = Field(
        autoincrement=False,
        default="⭐",
        description="",
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

    name: Field = Field(
        autoincrement=False,
        default=None,
        description="",
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
        index=False,
        name="value",
        nullable=False,
        on_delete=None,
        on_update=None,
        primary_key=False,
        size=None,
        type="DOUBLE",
        unique=False,
    )

    def __init__(
        self,
        created_at: Optional[datetime] = None,
        emoji: Optional[str] = None,
        icon: Optional[str] = "⭐",
        id: Optional[int] = None,
        key: Optional[str] = None,
        name: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        uuid: Optional[str] = None,
        value: Optional[float] = None,
    ) -> None:
        """
        Initializes a new instance of the DifficultyModel class.

        Args:
            created_at (Optional[datetime]): The timestamp when the difficulty was created.
            emoji (Optional[str]): The emoji of the difficulty.
            icon (Optional[str]): The icon of the difficulty. Defaults to "⭐".
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
            created_at=created_at,
            emoji=emoji,
            icon="⭐",
            id=id,
            key=key,
            name=name,
            table=Constants.DIFFICULTIES,
            updated_at=updated_at,
            uuid=uuid,
            value=value,
        )
