"""
Author: lodego
Date: 2025-02-09
"""

import traceback

from typing import *

from core.learning.learning_session import (
    ImmutableLearningSession,
    ImmutableLearningSessionAction,
    ImmutableLearningSessionItem,
)

from core.answer import ImmutableAnswer
from core.association import ImmutableAssociation
from core.change_history import ImmutableChangeHistory, ImmutableChangeHistoryItem
from core.custom_field import ImmutableCustomField
from core.default import ImmutableDefault
from core.difficulty import ImmutableDifficulty
from core.flashcard import ImmutableFlashcard
from core.note import ImmutableNote
from core.option import ImmutableOption
from core.priority import ImmutablePriority
from core.question import ImmutableQuestion
from core.setting import ImmutableSetting
from core.stack import ImmutableStack
from core.status import ImmutableStatus
from core.tag import ImmutableTag
from core.user import ImmutableUser

from utils.logger import Logger
from utils.miscellaneous import Miscellaneous
from utils.object import ImmutableBaseObject


__all__: Final[List[str]] = [
    "UnifiedObjectFactory",
    "UnifiedObjectManager",
    "UnifiedObjectService",
]


class UnifiedObjectFactory(ImmutableBaseObject):
    """
    A singleton Factory class for registering and managing multiple Factory instances.

    This class provides methods to create a single shared instance of the UnifiedObjectFactory,
    initialize it with a logger and a dictionary for storing registered Factorys, and
    register Factory instances using their class names as keys.

    Attributes:
        _shared_instance (Optional[UnifiedObjectFactory]): The shared singleton instance of the class.
        logger (Logger): The logger instance associated with the UnifiedObjectFactory.
        Factorys (Dict[str, Any]): The dictionary storing registered Factorys.
    """

    _shared_instance: Optional["UnifiedObjectFactory"] = None

    def __new__(cls) -> "UnifiedObjectFactory":
        """
        Creates and returns a new instance of the UnifiedObjectFactory class.

        If the instance does not exist, creates a new one by calling the parent class constructor.
        If the instance already exists, returns the existing instance.

        Returns:
            UnifiedObjectfactory: The created or existing instance of UnifiedObjectFactory class.
        """

        # Check if a shared instance already exists
        if cls._shared_instance is None:
            # Create a new instance
            cls._shared_instance = super(UnifiedObjectFactory, cls).__new__(cls)

            # Initialize the instance
            cls._shared_instance.init()

        # Return the shared instance
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes the UnifiedObjectFactory instance by creating a logger and an empty dictionary for storing registered Factorys.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

        # Initialize an empty dictionary for storing registered Factorys
        self.factories: Dict[str, Any] = {}

    @override
    def __getattr__(
        self,
        name: str,
    ) -> Optional[Any]:
        """
        Allows dynamic access to methods of registered Factorys.

        Args:
            name (str): The name of the method to retrieve.

        Returns:
            The method from the registered Factory or raises AttributeError.
        """

        # Iterate over the registered Factorys
        for Factory in self.factories.values():
            try:
                # Attempt to get the attribute from the Factory
                return getattr(
                    Factory,
                    name,
                )
            except AttributeError:
                # Ignore the attribute error and try the next Factory
                pass

        # Raise an AttributeError if the attribute is not found in any Factory
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{name}'"
        )

    def register_factory(
        self,
        name: str,
        factory: Type[Any],
    ) -> None:
        """
        Registers a factory instance with the UnifiedObjectFactory.

        Args:
            name (str): The name of the factory to be registered.
            factory (Type[Any]): The factory instance to be registered.

        Returns:
            None

        Raises:
            Exception: If an exception occurs during registration.
        """
        try:
            # Add the Factory to the Factorys dictionary using its class name as the key
            self.factories[name] = factory

            # Log a success message indicating the Factory has been registered
            self.logger.info(
                message=f"Registered Factory '{name}' with class '{factory.__name__}'"
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'register_Factory' from '{self.__class__.__name__}': {e}"
            )

            # Raise the exception to the caller
            raise e

    def run(
        self,
        factory: str,
        method: str,
        **kwargs,
    ) -> Any:
        """
        Dynamically calls a method on a specified factory.

        Args:
            factory (str): The name of the factory (e.g., 'flashcard').
            method (str): The name of the method to call (e.g., 'get_by_id').
            **kwargs: Additional parameters to pass to the method.

        Returns:
            Any: The result of the method execution.

        Raises:
            AttributeError: If the factory or method does not exist.
        """

        # Check if the specified Factory exists
        if factory not in self.factories:
            raise AttributeError(
                f"Factory '{factory}' not found in UnifiedObjectFactory."
            )

        # Get the Factory instance from the dictionary
        Factory_instance: Optional[Any] = self.factories.get(
            factory,
            None,
        )

        # Check if the Factory instance is None
        if not Factory_instance:
            raise AttributeError(
                f"Factory '{factory}' not found in UnifiedObjectFactory."
            )

        # Check if the specified method exists in the Factory
        if not hasattr(
            Factory_instance,
            method,
        ):
            raise AttributeError(f"Method '{method}' not found in factory '{factory}'.")

        # Dynamically call the method on the Factory instance
        try:
            return getattr(
                Factory_instance,
                method,
            )(**kwargs)
        except Exception as e:
            # Log an error message if an exception occurs
            self.logger.error(
                message=f"Caught an exception while attempting to run '{factory}.{method}' from '{self.__class__.__name__}': {e}"
            )

            # Raise the exception to the caller
            raise e


class UnifiedObjectManager(ImmutableBaseObject):
    """
    A singleton manager class for registering and managing multiple manager instances.

    This class provides methods to create a single shared instance of the UnifiedObjectManager,
    initialize it with a logger and a dictionary for storing registered managers, and
    register manager instances using their class names as keys.

    Attributes:
        _shared_instance (Optional[UnifiedObjectManager]): The shared singleton instance of the class.
        logger (Logger): The logger instance associated with the UnifiedObjectManager.
        managers (Dict[str, Any]): The dictionary storing registered managers.
    """

    _shared_instance: Optional["UnifiedObjectManager"] = None

    def __new__(cls) -> "UnifiedObjectManager":
        """
        Creates and returns a new instance of the UnifiedObjectManager class.

        If the instance does not exist, creates a new one by calling the parent class constructor.
        If the instance already exists, returns the existing instance.

        Returns:
            UnifiedObjectManager: The created or existing instance of UnifiedObjectManager class.
        """

        # Check if a shared instance already exists
        if cls._shared_instance is None:
            # Create a new instance
            cls._shared_instance = super(UnifiedObjectManager, cls).__new__(cls)

            # Initialize the instance
            cls._shared_instance.init()

        # Return the shared instance
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes the UnifiedObjectManager instance by creating a logger and an empty dictionary for storing registered managers.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

        # Initialize an empty dictionary for storing registered managers
        self.managers: Dict[str, Any] = {}

    @override
    def __getattr__(
        self,
        name: str,
    ) -> Optional[Any]:
        """
        Allows dynamic access to methods of registered managers.

        Args:
            name (str): The name of the method to retrieve.

        Returns:
            The method from the registered manager or raises AttributeError.
        """

        # Iterate over the registered managers
        for manager in self.managers.values():
            try:
                # Attempt to get the attribute from the manager
                return getattr(
                    manager,
                    name,
                )
            except AttributeError:
                # Ignore the attribute error and try the next manager
                pass

        # Raise an AttributeError if the attribute is not found in any manager
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{name}'"
        )

    def get_all(
        self,
        force_refetch: bool = False,
    ) -> Optional[
        List[
            Union[
                ImmutableAssociation,
                ImmutableCustomField,
                ImmutableStack,
                ImmutableFlashcard,
                ImmutableQuestion,
                ImmutableAnswer,
                ImmutableOption,
                ImmutableTag,
                ImmutableStatus,
                ImmutablePriority,
                ImmutableDifficulty,
                ImmutableSetting,
                ImmutableNote,
                ImmutableUser,
                ImmutableDefault,
            ]
        ]
    ]:
        """
        Retrieves all registered managers.

        This method iterates over all registered managers, calls the get_all method of each manager,
        and combines their results into a single list.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.

        Returns:
            Optional[List[Union[
                ImmutableAssociation,
                ImmutableCustomField,
                ImmutableStack,
                ImmutableFlashcard,
                ImmutableQuestion,
                ImmutableAnswer,
                ImmutableOption,
                ImmutableTag,
                ImmutableStatus,
                ImmutablePriority,
                ImmutableDifficulty,
                ImmutableSetting,
                ImmutableNote,
                ImmutableUser,
                ImmutableDefault,
            ]]]]: The list of all registered managers if no exception occurs. Otherwise, None.
        """
        try:
            result: List[
                Union[
                    ImmutableAssociation,
                    ImmutableCustomField,
                    ImmutableStack,
                    ImmutableFlashcard,
                    ImmutableQuestion,
                    ImmutableAnswer,
                    ImmutableOption,
                    ImmutableTag,
                    ImmutableStatus,
                    ImmutablePriority,
                    ImmutableDifficulty,
                    ImmutableSetting,
                    ImmutableNote,
                    ImmutableUser,
                    ImmutableDefault,
                ]
            ] = [
                manager.__getattr__(
                    name=f"get_all{Miscellaneous.pluralize(string=name.replace('_manager', ''))}"
                )(force_refetch=force_refetch)
                for (
                    name,
                    manager,
                ) in self.managers.items()
            ]

            # Combine the results of each manager into a single list
            result = [item for sublist in result for item in sublist]

            return result
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_all' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def get_by_key(
        self,
        key: str,
        force_refetch: bool = False,
    ) -> Optional[
        Union[
            ImmutableAssociation,
            ImmutableCustomField,
            ImmutableStack,
            ImmutableFlashcard,
            ImmutableQuestion,
            ImmutableAnswer,
            ImmutableOption,
            ImmutableTag,
            ImmutableStatus,
            ImmutablePriority,
            ImmutableDifficulty,
            ImmutableSetting,
            ImmutableNote,
            ImmutableUser,
            ImmutableDefault,
        ]
    ]:
        """
        Retrieves an object by its key.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            key (str): The key of the object to be retrieved.

        Returns:
            Optional[Union[ImmutableAssociation, ImmutableCustomField, ImmutableStack, ImmutableFlashcard, ImmutableQuestion, ImmutableAnswer, ImmutableOption, ImmutableTag, ImmutableStatus, ImmutablePriority, ImmutableDifficulty, ImmutableSetting, ImmutableNote, ImmutableUser, ImmutableDefault]]: The retrieved object if the key exists, otherwise None.

        Raises:
            Exception: If an exception occurs while attempting to run the 'get_by_key' method.
        """
        try:
            # Attempt to find a match in the given key
            match: Optional[str] = Miscellaneous.find_match(
                string=key,
                group=1,
                pattern=r"([A-Za-z]+)",
            )

            if not match:
                # Log an error message indicating that the key format is invalid
                self.logger.error(message=f"Invalid key format: '{key}'")

                # Return early since the key is invalid
                return

            # Run the 'get_by_key' method of the corresponding manager
            return self.run(
                force_refetch=force_refetch,
                manager=f"{match.lower()}_manager",
                method=f"get_{match.lower()}_by_key",
                key=key,
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_key' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def get_by_keys(
        self,
        keys: List[str],
        force_refetch: bool = False,
    ) -> Optional[
        List[
            Optional[
                Union[
                    ImmutableAssociation,
                    ImmutableCustomField,
                    ImmutableStack,
                    ImmutableFlashcard,
                    ImmutableQuestion,
                    ImmutableAnswer,
                    ImmutableOption,
                    ImmutableTag,
                    ImmutableStatus,
                    ImmutablePriority,
                    ImmutableDifficulty,
                    ImmutableSetting,
                    ImmutableNote,
                    ImmutableUser,
                    ImmutableDefault,
                ]
            ]
        ]
    ]:
        """
        Retrieves a list of objects by their keys.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            keys (List[str]): A list of keys for the objects to be retrieved.

        Returns:
            Optional[List[Union[ImmutableAssociation, ImmutableCustomField, ImmutableStack, ImmutableFlashcard, ImmutableQuestion, ImmutableAnswer, ImmutableOption, ImmutableTag, ImmutableStatus, ImmutablePriority, ImmutableDifficulty, ImmutableSetting, ImmutableNote, ImmutableUser, ImmutableDefault]]]: The list of retrieved objects if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to run the 'get_by_keys' method.
        """
        try:
            # Initialize an empty list to store the retrieved objects
            result: List[
                Optional[
                    Union[
                        ImmutableAssociation,
                        ImmutableCustomField,
                        ImmutableStack,
                        ImmutableFlashcard,
                        ImmutableQuestion,
                        ImmutableAnswer,
                        ImmutableOption,
                        ImmutableTag,
                        ImmutableStatus,
                        ImmutablePriority,
                        ImmutableDifficulty,
                        ImmutableSetting,
                        ImmutableNote,
                        ImmutableUser,
                        ImmutableDefault,
                    ]
                ]
            ] = []

            # Iterate over the list of keys
            for key in keys:
                # Get the object by key and append it to the result list
                result.append(
                    self.get_by_key(
                        force_refetch=force_refetch,
                        key=key,
                    )
                )

            # Return the list of retrieved objects
            return result
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_by_keys' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def register_manager(
        self,
        name: str,
        manager: Type[Any],
    ) -> None:
        """
        Registers a manager instance with the UnifiedObjectManager.

        Args:
            name (str): The name of the manager to be registered.
            manager (Type[Any]): The manager instance to be registered.

        Returns:
            None

        Raises:
            Exception: If an exception occurs during registration.
        """
        try:
            # Add the manager to the managers dictionary using its class name as the key
            self.managers[name] = manager()

            # Log a success message indicating the manager has been registered
            self.logger.info(
                message=f"Registered manager '{name}' with class '{manager.__name__}'"
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'register_manager' from '{self.__class__.__name__}': {e}"
            )

            # Raise the exception to the caller
            raise e

    def run(
        self,
        manager: str,
        method: str,
        **kwargs,
    ) -> Any:
        """
        Dynamically calls a method on a specified manager.

        Args:
            manager (str): The name of the manager (e.g., 'flashcard').
            method (str): The name of the method to call (e.g., 'get_by_id').
            **kwargs: Additional parameters to pass to the method.

        Returns:
            Any: The result of the method execution.

        Raises:
            AttributeError: If the manager or method does not exist.
        """

        # Check if the specified manager exists
        if manager not in self.managers:
            raise AttributeError(
                f"Manager '{manager}' not found in UnifiedObjectManager."
            )

        # Get the manager instance from the dictionary
        manager_instance: Optional[Any] = self.managers.get(manager, None)

        # Check if the manager instance is None
        if not manager_instance:
            raise AttributeError(
                f"Manager '{manager}' not found in UnifiedObjectManager."
            )

        # Check if the specified method exists in the manager
        if not hasattr(
            manager_instance,
            method,
        ):
            raise AttributeError(f"Method '{method}' not found in manager '{manager}'.")

        # Dynamically call the method on the manager instance
        try:
            return getattr(
                manager_instance,
                method,
            )(**kwargs)
        except Exception as e:
            # Log an error message if an exception occurs
            self.logger.error(
                message=f"Caught an exception while attempting to run '{manager}.{method}' from '{self.__class__.__name__}': {e}"
            )

            # Raise the exception to the caller
            raise e

    def update(
        self,
        update: Union[
            ImmutableAssociation,
            ImmutableCustomField,
            ImmutableStack,
            ImmutableFlashcard,
            ImmutableQuestion,
            ImmutableAnswer,
            ImmutableOption,
            ImmutableTag,
            ImmutableStatus,
            ImmutablePriority,
            ImmutableDifficulty,
            ImmutableSetting,
            ImmutableNote,
            ImmutableUser,
            ImmutableDefault,
        ],
    ) -> Optional[
        Union[
            ImmutableAssociation,
            ImmutableCustomField,
            ImmutableStack,
            ImmutableFlashcard,
            ImmutableQuestion,
            ImmutableAnswer,
            ImmutableOption,
            ImmutableTag,
            ImmutableStatus,
            ImmutablePriority,
            ImmutableDifficulty,
            ImmutableSetting,
            ImmutableNote,
            ImmutableUser,
            ImmutableDefault,
        ]
    ]:
        """
        Updates a unified object with the given key.

        Args:
            update (Union[ImmutableAssociation, ...]): The unified object to update.

        Returns:
            Optional[Union[ImmutableAssociation, ...]]: The updated unified object if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Attempt to find a match in the given key
            match: Optional[str] = Miscellaneous.find_match(
                string=update.__class__.__name__,
                group=1,
                pattern=r"([A-Za-z]+)",
            )

            if not match:
                # Log an error message indicating that the key format is invalid
                self.logger.error(
                    message=f"Invalid key format: '{update.__class__.__name__}'"
                )

                # Return early since the key is invalid
                return

            # Run the 'update' method of the corresponding manager
            return self.run(
                manager=f"{match.lower()}_manager",
                method=f"update_{match.lower()}",
                **{match.lower(): update},
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=traceback.format_exc())

            # Return None indicating that an exception has occurred
            return None

    def update_in_bulk(
        self,
        updates: List[
            Union[
                ImmutableAssociation,
                ImmutableCustomField,
                ImmutableStack,
                ImmutableFlashcard,
                ImmutableQuestion,
                ImmutableAnswer,
                ImmutableOption,
                ImmutableTag,
                ImmutableStatus,
                ImmutablePriority,
                ImmutableDifficulty,
                ImmutableSetting,
                ImmutableNote,
                ImmutableUser,
                ImmutableDefault,
            ]
        ],
    ) -> Optional[
        List[
            Union[
                ImmutableAssociation,
                ImmutableCustomField,
                ImmutableStack,
                ImmutableFlashcard,
                ImmutableQuestion,
                ImmutableAnswer,
                ImmutableOption,
                ImmutableTag,
                ImmutableStatus,
                ImmutablePriority,
                ImmutableDifficulty,
                ImmutableSetting,
                ImmutableNote,
                ImmutableUser,
                ImmutableDefault,
            ]
        ]
    ]:
        """
        Updates multiple unified objects in bulk.

        Args:
            updates (List[Union[...]]): A list of unified objects to update.

        Returns:
            Optional[List[Union[...]]]: The updated unified objects if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Initialize an empty list to store the updated objects
            result: List[
                Union[
                    ImmutableAssociation,
                    ImmutableCustomField,
                    ImmutableStack,
                    ImmutableFlashcard,
                    ImmutableQuestion,
                    ImmutableAnswer,
                    ImmutableOption,
                    ImmutableTag,
                    ImmutableStatus,
                    ImmutablePriority,
                    ImmutableDifficulty,
                    ImmutableSetting,
                    ImmutableNote,
                    ImmutableUser,
                    ImmutableDefault,
                ]
            ] = []

            # Iterate over the list of objects to update
            for update in updates:
                # Run the 'update' method for each object
                result.append(self.update(update=update))

            # Return the list of updated objects
            return result
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update_in_bulk' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=traceback.format_exc())

            # Return None indicating that an exception has occurred
            return None


class UnifiedObjectService(ImmutableBaseObject):
    """
    A singleton service class for managing unified objects.

    This class provides a shared instance that listens to events and dispatches
    events to registered handlers.

    Attributes:
        logger (Logger): The logger instance for logging information and errors.
    """

    _shared_instance: Optional["UnifiedObjectService"] = None

    def __new__(
        cls,
        unified_manager: UnifiedObjectManager,
    ) -> "UnifiedObjectService":
        """
        Creates and returns a new instance of UnifiedObjectService.

        If the instance does not exist, it creates a new one by calling the parent class constructor
        and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Args:
            unified_manager (UnifiedObjectManager): The manager instance to be used by the service.

        Returns:
            UnifiedObjectService: The created or existing instance of UnifiedObjectService class.
        """

        # Check if a shared instance already exists
        if cls._shared_instance is None:
            # Create a new instance
            cls._shared_instance = super(UnifiedObjectService, cls).__new__(cls)

            # Initialize the instance
            cls._shared_instance.init(unified_manager=unified_manager)

        # Return the shared instance
        return cls._shared_instance

    def init(
        self,
        unified_manager: UnifiedObjectManager,
    ) -> None:
        """
        Initializes the shared instance of UnifiedObjectService.

        Args:
            unified_manager (UnifiedObjectManager): The manager instance to be used by the service.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

        # Store the passed unified_manager instance in an instance variable
        self.unified_manager: UnifiedObjectManager = unified_manager

    def on_request_answer_create(
        self,
        answer: ImmutableAnswer,
    ) -> Optional[ImmutableAnswer]:
        """
        Handles the 'request_answer_create' event and creates a new answer in the database.

        Args:
            answer (ImmutableAnswer): The answer to be created.

        Returns:
            Optional[ImmutableAnswer]: The created answer object if no exception occurs. Otherwise, None.
        """

        # Create and return the answer
        return self.unified_manager.create_answer(answer=answer)

    def on_request_answer_delete(
        self,
        answer: ImmutableAnswer,
    ) -> bool:
        """
        Handles the 'request_answer_delete' event and deletes an answer from the database.

        Args:
            answer (ImmutableAnswer): The answer to be deleted.

        Returns:
            bool: True if the answer was deleted successfully. False otherwise.
        """

        # Delete the answer and return a boolean indicating success or failure
        return self.unified_manager.delete_answer(answer=answer)

    def on_request_answer_load(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableAnswer]]:
        """
        Handles the 'request_answer_load' event and loads answers from the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be passed to the database query.

        Returns:
            Optional[List[ImmutableAnswer]]: The loaded answers if no exception occurs. Otherwise, None.
        """

        # Load the answer and return it
        return self.unified_manager.get_answer_by(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_answer_lookup(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableAnswer]]:
        """
        Handles the 'request_answer_lookup' event and looks up answers in the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for querying the answers.

        Returns:
            Optional[List[ImmutableAnswer]]: The loaded immutable answers if no exception occurs. Otherwise, None.
        """

        # Search for answers using the provided keyword arguments and return them
        return self.unified_manager.search_answers(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_answer_update(
        self,
        answer: ImmutableAnswer,
    ) -> Optional[ImmutableAnswer]:
        """
        Handles the 'request_answer_update' event and updates an answer in the database.

        Args:
            answer (ImmutableAnswer): The answer to be updated.

        Returns:
            Optional[ImmutableAnswer]: The updated immutable answer if no exception occurs. Otherwise, None.
        """

        # Update the answer and return it
        return self.unified_manager.update_answer(answer=answer)

    def on_request_association_create(
        self,
        association: ImmutableAssociation,
    ) -> Optional[ImmutableAssociation]:
        """
        Handles the 'request_association_create' event and creates a new association in the database.

        Args:
            association (ImmutableAssociation): The association to be created.

        Returns:
            Optional[ImmutableAssociation]: The created association object if no exception occurs. Otherwise, None.
        """

        # Create and return the association
        return self.unified_manager.create_association(association=association)

    def on_request_association_delete(
        self,
        association: ImmutableAssociation,
    ) -> bool:
        """
        Handles the 'request_association_delete' event and deletes an association from the database.

        Args:
            association (ImmutableAssociation): The association to be deleted.

        Returns:
            bool: True if the association was deleted successfully. False otherwise.
        """

        # Delete the association and return a boolean indicating success or failure
        return self.unified_manager.delete_association(association=association)

    def on_request_association_load(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableAssociation]]:
        """
        Handles the 'request_association_load' event and loads associations from the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: Keyword arguments to be used for querying associations.

        Returns:
            Optional[List[ImmutableAssociation]]: A list of loaded associations if no exception occurs. Otherwise, None.
        """

        # Retrieve associations using the provided keyword arguments
        return self.unified_manager.get_association_by(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_association_lookup(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableAssociation]]:
        """
        Handles the 'request_association_lookup' event and looks up associations in the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for querying the associations.

        Returns:
            Optional[List[ImmutableAssociation]]: The loaded associations if no exception occurs. Otherwise, None.
        """

        # Search for associations using the provided keyword arguments and return them
        return self.unified_manager.search_associations(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_association_update(
        self,
        association: ImmutableAssociation,
    ) -> Optional[ImmutableAssociation]:
        """
        Handles the 'request_association_update' event and updates an association in the database.

        Args:
            association (ImmutableAssociation): The association to be updated.

        Returns:
            Optional[ImmutableAssociation]: The updated association object if no exception occurs. Otherwise, None.
        """

        # Update and return the association
        return self.unified_manager.update_association(association=association)

    def on_request_change_history_create(
        self,
        change_history: ImmutableChangeHistory,
    ) -> Optional[ImmutableChangeHistory]:
        """
        Handles the 'request_change_history_create' event and creates a new change history in the database.

        Args:
            change_history (ImmutableChangeHistory): The change history to be created.

        Returns:
            Optional[ImmutableChangeHistory]: The created change history object if no exception occurs. Otherwise, None.
        """

        # Create and return the change history
        return self.unified_manager.create_change_history(change_history=change_history)

    def on_request_change_history_delete(
        self,
        change_history: ImmutableChangeHistory,
    ) -> bool:
        """
        Handles the 'request_change_history_delete' event and deletes a change history from the database.

        Args:
            change_history (ImmutableChangeHistory): The change history to be deleted.

        Returns:
            bool: True if the change history was deleted successfully. False otherwise.
        """

        # Delete the change history and return a boolean indicating success or failure
        return self.unified_manager.delete_change_history(change_history=change_history)

    def on_request_change_history_load(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableChangeHistory]]:
        """
        Handles the 'request_change_history_load' event and loads change histories from the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: Keyword arguments to be used for querying change histories.

        Returns:
            Optional[List[ImmutableChangeHistory]]: A list of loaded change histories if no exception occurs. Otherwise, None.
        """

        # Retrieve change histories using the provided keyword arguments
        return self.unified_manager.get_change_history_by(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_change_history_lookup(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableChangeHistory]]:
        """
        Handles the 'request_change_history_lookup' event and looks up change histories in the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for querying the change histories.

        Returns:
            Optional[List[ImmutableChangeHistory]]: The loaded change histories if no exception occurs. Otherwise, None.
        """

        # Search for change histories using the provided keyword arguments and return them
        return self.unified_manager.search_change_histories(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_change_history_update(
        self,
        change_history: ImmutableChangeHistory,
    ) -> Optional[ImmutableChangeHistory]:
        """
        Handles the 'request_change_history_update' event and updates a change history in the database.

        Args:
            change_history (ImmutableChangeHistory): The change history to be updated.

        Returns:
            Optional[ImmutableChangeHistory]: The updated change history object if no exception occurs. Otherwise, None.
        """

        # Update and return the change history
        return self.unified_manager.update_change_history(change_history=change_history)

    def on_request_change_history_item_create(
        self,
        change_history_item: ImmutableChangeHistoryItem,
    ) -> Optional[ImmutableChangeHistoryItem]:
        """
        Handles the 'request_change_history_item_create' event and creates a new change history item in the database.

        Args:
            change_history_item (ImmutableChangeHistoryItem): The change history item to be created.

        Returns:
            Optional[ImmutableChangeHistoryItem]: The created change history item object if no exception occurs. Otherwise, None.
        """

        # Create and return the change history item
        return self.unified_manager.create_change_history_item(
            change_history_item=change_history_item
        )

    def on_request_change_history_item_delete(
        self,
        change_history_item: ImmutableChangeHistoryItem,
    ) -> bool:
        """
        Handles the 'request_change_history_item_delete' event and deletes a change history item from the database.

        Args:
            change_history_item (ImmutableChangeHistoryItem): The change history item to be deleted.

        Returns:
            bool: True if the change history item was deleted successfully. False otherwise.
        """

        # Delete the change history item and return a boolean indicating success or failure
        return self.unified_manager.delete_change_history_item(
            change_history_item=change_history_item
        )

    def on_request_change_history_item_load(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableChangeHistoryItem]]:
        """
        Handles the 'request_change_history_item_load' event and retrieves a list of change history items from the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for retrieving the change history items.

        Returns:
            Optional[List[ImmutableChangeHistoryItem]]: A list of loaded change history items if no exception occurs. Otherwise, None.
        """

        # Retrieve change history items using the provided keyword arguments
        return self.unified_manager.get_change_history_item_by(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_change_history_item_lookup(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableChangeHistoryItem]]:
        """
        Handles the 'request_change_history_item_lookup' event and looks up change history items in the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for querying the change history items.

        Returns:
            Optional[List[ImmutableChangeHistoryItem]]: The loaded change history items if no exception occurs. Otherwise, None.
        """

        # Search for change history items using the provided keyword arguments and return them
        return self.unified_manager.search_change_history_items(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_change_history_item_update(
        self,
        change_history_item: ImmutableChangeHistoryItem,
    ) -> Optional[ImmutableChangeHistoryItem]:
        """
        Handles the 'request_change_history_item_update' event and updates a change history item in the database.

        Args:
            change_history_item (ImmutableChangeHistoryItem): The change history item to be updated.

        Returns:
            Optional[ImmutableChangeHistoryItem]: The updated change history item object if no exception occurs. Otherwise, None.
        """

        # Update and return the change history item
        return self.unified_manager.update_change_history_item(
            change_history_item=change_history_item
        )

    def on_request_custom_field_create(
        self,
        custom_field: ImmutableCustomField,
    ) -> Optional[ImmutableCustomField]:
        """
        Handles the 'request_custom_field_create' event and creates a new custom field in the database.

        Args:
            custom_field (ImmutableCustomField): The custom field to be created.

        Returns:
            Optional[ImmutableCustomField]: The newly created custom field if no exception occurs. Otherwise, None.
        """

        # Create and return the custom field
        return self.unified_manager.create_custom_field(custom_field=custom_field)

    def on_request_custom_field_delete(
        self,
        custom_field: ImmutableCustomField,
    ) -> bool:
        """
        Handles the 'request_custom_field_delete' event and deletes a custom field from the database.

        Args:
            custom_field (ImmutableCustomField): The custom field to be deleted.

        Returns:
            bool: True if the custom field was deleted successfully. False otherwise.
        """

        # Delete and return the result of the deletion
        return self.unified_manager.delete_custom_field(custom_field=custom_field)

    def on_request_custom_field_load(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableCustomField]]:
        """
        Handles the 'request_custom_field_load' event and retrieves a list of custom fields from the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for retrieving the custom fields.

        Returns:
            Optional[List[ImmutableCustomField]]: A list of loaded custom fields if no exception occurs. Otherwise, None.
        """

        # Retrieve custom fields using the provided keyword arguments
        return self.unified_manager.get_custom_field_by(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_custom_field_lookup(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableCustomField]]:
        """
        Handles the 'request_custom_field_lookup' event and looks up custom fields in the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for querying the custom fields.

        Returns:
            Optional[List[ImmutableCustomField]]: The loaded custom fields if no exception occurs. Otherwise, None.
        """

        # Search for custom fields using the provided keyword arguments and return them
        return self.unified_manager.search_custom_fields(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_custom_field_update(
        self,
        custom_field: ImmutableCustomField,
    ) -> Optional[ImmutableCustomField]:
        """
        Handles the 'request_custom_field_update' event and updates a custom field in the database.

        Args:
            custom_field (ImmutableCustomField): The custom field to be updated.

        Returns:
            Optional[ImmutableCustomField]: The updated custom field object if no exception occurs. Otherwise, None.
        """

        # Update and return the custom field
        return self.unified_manager.update_custom_field(custom_field=custom_field)

    def on_request_difficulty_create(
        self,
        difficulty: ImmutableDifficulty,
    ) -> Optional[ImmutableDifficulty]:
        """
        Handles the 'request_difficulty_create' event and creates a new difficulty in the database.

        Args:
            difficulty (ImmutableDifficulty): The difficulty to be created.

        Returns:
            Optional[ImmutableDifficulty]: The newly created difficulty if no exception occurs. Otherwise, None.
        """

        # Create and return the difficulty
        return self.unified_manager.create_difficulty(difficulty=difficulty)

    def on_request_difficulty_delete(
        self,
        difficulty: ImmutableDifficulty,
    ) -> bool:
        """
        Handles the 'request_difficulty_delete' event and deletes a difficulty from the database.

        Args:
            difficulty (ImmutableDifficulty): The difficulty to be deleted.

        Returns:
            bool: True if the difficulty was deleted successfully. False otherwise.
        """

        # Delete and return the result of the deletion
        return self.unified_manager.delete_difficulty(difficulty=difficulty)

    def on_request_difficulty_load(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableDifficulty]]:
        """
        Handles the 'request_difficulty_load' event and loads difficulties from the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: Keyword arguments to be passed to the database query.

        Returns:
            Optional[List[ImmutableDifficulty]]: The loaded difficulties if no exception occurs. Otherwise, None.
        """

        # Load the difficulties from the database
        return self.unified_manager.get_difficulty_by(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_difficulty_lookup(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableDifficulty]]:
        """
        Handles the 'request_difficulty_lookup' event and looks up difficulties in the database.

        Args:
            **kwargs: The keyword arguments to be used for querying the difficulty.

        Returns:
            Optional[List[ImmutableDifficulty]]: The loaded immutable difficulties if no exception occurs. Otherwise, None.
        """

        # Load the difficulty from the database and return the loaded immutable difficulty
        return self.unified_manager.search_difficulties(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_difficulty_update(
        self,
        difficulty: ImmutableDifficulty,
    ) -> Optional[ImmutableDifficulty]:
        """
        Handles the 'request_difficulty_update' event and updates a difficulty in the database.

        Args:
            difficulty (ImmutableDifficulty): The difficulty to be updated.

        Returns:
            Optional[ImmutableDifficulty]: The updated difficulty if no exception occurs. Otherwise, None.
        """

        # Update and return the difficulty
        return self.unified_manager.update_difficulty(difficulty=difficulty)

    def on_request_flashcard_create(
        self,
        flashcard: ImmutableFlashcard,
    ) -> Optional[ImmutableFlashcard]:
        """
        Handles the 'request_flashcard_create' event and creates a new flashcard in the database.

        Args:
            flashcard (ImmutableFlashcard): The flashcard to be created.

        Returns:
            Optional[ImmutableFlashcard]: The newly created flashcard if no exception occurs. Otherwise, None.
        """

        # Create and return the flashcard
        return self.unified_manager.create_flashcard(flashcard=flashcard)

    def on_request_flashcard_delete(
        self,
        flashcard: ImmutableFlashcard,
    ) -> bool:
        """
        Handles the 'request_flashcard_delete' event and deletes a flashcard from the database.

        Args:
            flashcard (ImmutableFlashcard): The flashcard to be deleted.

        Returns:
            bool: True if the flashcard was deleted successfully. False otherwise.
        """

        # Delete the flashcard from the database and return the result of the deletion
        return self.unified_manager.delete_flashcard(flashcard=flashcard)

    def on_request_flashcard_load(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableFlashcard]]:
        """
        Handles the 'request_flashcard_load' event and retrieves a list of flashcards from the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be passed to the unified manager's get_flashcard_by method.

        Returns:
            Optional[List[ImmutableFlashcard]]: A list of flashcards retrieved from the database if no exception occurs. Otherwise, None.
        """

        # Load the flashcards from the database and return them
        return self.unified_manager.get_flashcard_by(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_flashcard_lookup(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableFlashcard]]:
        """
        Handles the 'request_flashcard_lookup' event and retrieves a list of flashcards from the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be passed to the unified manager's search_flashcards method.

        Returns:
            Optional[List[ImmutableFlashcard]]: A list of flashcards retrieved from the database if no exception occurs. Otherwise, None.
        """

        # Search for flashcards in the database and return them
        return self.unified_manager.search_flashcards(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_flashcard_update(
        self,
        flashcard: ImmutableFlashcard,
    ) -> Optional[ImmutableFlashcard]:
        """
        Handles the 'request_flashcard_update' event and updates a flashcard in the database.

        Args:
            flashcard (ImmutableFlashcard): The flashcard to be updated.

        Returns:
            Optional[ImmutableFlashcard]: The updated flashcard if no exception occurs. Otherwise, None.
        """

        # Update and return the flashcard
        return self.unified_manager.update_flashcard(flashcard=flashcard)

    def on_request_get_all_answers(self) -> Optional[List[ImmutableAnswer]]:
        """
        Handles the 'request_get_all_answers' event and gets all answers from the database.

        Returns:
            Optional[List[ImmutableAnswer]]: A list of all answers if no exception occurs. Otherwise, None.
        """

        # Get all answers from the database and return them
        return self.unified_manager.get_all_answers()

    def on_request_get_all_associations(self) -> Optional[List[ImmutableAssociation]]:
        """
        Handles the 'request_get_all_associations' event and gets all associations from the database.

        Returns:
            Optional[List[ImmutableAssociation]]: A list of all associations if no exception occurs. Otherwise, None.
        """

        # Get all associations from the database and return them
        return self.unified_manager.get_all_associations()

    def on_request_get_all_change_histories(
        self,
    ) -> Optional[List[ImmutableChangeHistory]]:
        """
        Handles the 'request_all_change_histories' event and gets all change histories from the database.

        Returns:
            Optional[List[ImmutableImmutableChangeHistory]]: A list of all change histories if no exception occurs. Otherwise, None.
        """

        # Get all change histories from the database and return them
        return self.unified_manager.get_all_change_histories()

    def on_request_get_all_change_history_items(
        self,
    ) -> Optional[List[ImmutableChangeHistoryItem]]:
        """
        Handles the 'request_all_change_history_items' event and gets all change history items from the database.

        Returns:
            Optional[List[ImmutableImmutableChangeHistoryItem]]: A list of all change history items if no exception occurs. Otherwise, None.
        """

        # Get all change history items from the database and return them
        return self.unified_manager.get_all_change_history_items()

    def on_request_get_all_custom_fields(self) -> Optional[List[ImmutableCustomField]]:
        """
        Handles the 'request_get_all_custom_fields' event and gets all custom fields from the database.

        Returns:
            Optional[List[ImmutableImmutableCustomField]]: A list of all custom fields if no exception occurs. Otherwise, None.
        """

        # Get all custom fields from the database and return them
        return self.unified_manager.get_all_custom_fields()

    def on_request_get_all_defaults(self) -> Optional[List[ImmutableDefault]]:
        """
        Handles the 'request_all_defaults' event and gets all defaults from the database.

        Returns:
            Optional[List[ImmutableDefault]]: A list of all defaults if no exception occurs. Otherwise, None.
        """

        # Get all defaults from the database and return them
        return self.unified_manager.get_all_defaults()

    def on_request_get_all_difficulties(self) -> Optional[List[ImmutableDifficulty]]:
        """
        Handles the 'request_get_all_difficulties' event and gets all difficulties from the database.

        Returns:
            Optional[List[ImmutableDifficulty]]: A list of all difficulties if no exception occurs. Otherwise, None.
        """

        # Get all difficulties from the database and return them
        return self.unified_manager.get_all_difficulties()

    def on_request_get_all_flashcards(self) -> Optional[List[ImmutableFlashcard]]:
        """
        Handles the 'request_all_flashcards' event and gets all flashcards from the database.

        Returns:
            Optional[List[ImmutableFlashcard]]: A list of all flashcards if no exception occurs. Otherwise, None.
        """

        # Get all flashcards from the database and return them
        return self.unified_manager.get_all_flashcards()

    def on_request_get_all_notes(self) -> Optional[List[ImmutableNote]]:
        """
        Handles the 'request_all_notes' event and gets all notes from the database.

        Returns:
            Optional[List[ImmutableNote]]: A list of all notes if no exception occurs. Otherwise, None.
        """

        # Get all notes from the database and return them
        return self.unified_manager.get_all_notes()

    def on_request_get_all_options(self) -> Optional[List[ImmutableOption]]:
        """
        Handles the 'request_get_all_options' event and gets all options from the database.

        Returns:
            Optional[List[ImmutableOption]]: A list of all options if no exception occurs. Otherwise, None.
        """

        # Get all options from the database and return them
        return self.unified_manager.get_all_options()

    def on_request_get_all_priorities(self) -> Optional[List[ImmutablePriority]]:
        """
        Handles the 'request_get_all_priorities' event and gets all priorities from the database.

        Returns:
            Optional[List[ImmutablePriority]]: A list of all priorities if no exception occurs. Otherwise, None.
        """

        # Get all priorities from the database and return them
        return self.unified_manager.get_all_priorities()

    def on_request_get_all_questions(self) -> Optional[List[ImmutableQuestion]]:
        """
        Handles the 'request_get_all_questions' event and gets all questions from the database.

        Returns:
            Optional[List[ImmutableQuestion]]: A list of all questions if no exception occurs. Otherwise, None.
        """

        # Get all questions from the database and return them
        return self.unified_manager.get_all_questions()

    def on_request_get_all_settings(self) -> Optional[List[ImmutableSetting]]:
        """
        Handles the 'request_get_all_settings' event and gets all settings from the database.

        Returns:
            Optional[List[ImmutableSetting]]: A list of all settings if no exception occurs. Otherwise, None.
        """

        # Get all settings from the database and return them
        return self.unified_manager.get_all_settings()

    def on_request_get_all_stacks(self) -> Optional[List[ImmutableStack]]:
        """
        Handles the 'request_get_all_stacks' event and gets all stacks from the database.

        Returns:
            Optional[List[ImmutableStack]]: A list of all stacks if no exception occurs. Otherwise, None.
        """

        # Get all stacks from the database and return them
        return self.unified_manager.get_all_stacks()

    def on_request_get_all_statuses(self) -> Optional[List[ImmutableStatus]]:
        """
        Handles the 'request_get_all_statuses' event and gets all statuses from the database.

        Returns:
            Optional[List[ImmutableStatus]]: A list of all statuses if no exception occurs. Otherwise, None.
        """

        # Get all statuses from the database and return them
        return self.unified_manager.get_all_statuses()

    def on_request_get_all_tags(self) -> Optional[List[ImmutableTag]]:
        """
        Handles the 'request_get_all_tags' event and gets all tags from the database.

        Returns:
            Optional[List[ImmutableTag]]: A list of all tags if no exception occurs. Otherwise, None.
        """

        # Get all tags from the database and return them
        return self.unified_manager.get_all_tags()

    def on_request_get_all_users(self) -> Optional[List[ImmutableUser]]:
        """
        Handles the 'request_get_all_users' event and gets all users from the database.

        Returns:
            Optional[List[ImmutableUser]]: A list of all users if no exception occurs. Otherwise, None.
        """

        # Get all users from the database and return them
        return self.unified_manager.get_all_users()

    def on_request_get_by_key(
        self,
        key: str,
        force_refetch: bool = False,
    ) -> Optional[
        Union[
            ImmutableAssociation,
            ImmutableCustomField,
            ImmutableStack,
            ImmutableFlashcard,
            ImmutableQuestion,
            ImmutableAnswer,
            ImmutableOption,
            ImmutableTag,
            ImmutableStatus,
            ImmutablePriority,
            ImmutableDifficulty,
            ImmutableSetting,
            ImmutableNote,
            ImmutableUser,
            ImmutableDefault,
        ]
    ]:
        """
        Retrieves an object by its key.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            key (str): The key of the object to be retrieved.

        Returns:
            Optional[Union[ImmutableAssociation, ImmutableCustomField, ImmutableStack, ImmutableFlashcard, ImmutableQuestion, ImmutableAnswer, ImmutableOption, ImmutableTag, ImmutableStatus, ImmutablePriority, ImmutableDifficulty, ImmutableSetting, ImmutableNote, ImmutableUser, ImmutableDefault]]: The retrieved object if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to run the 'get_by_key' method.
        """
        return self.unified_manager.get_by_key(
            force_refetch=force_refetch,
            key=key,
        )

    def on_request_get_by_keys(
        self,
        keys: List[str],
        force_refetch: bool = False,
    ) -> Optional[
        List[
            Union[
                ImmutableAssociation,
                ImmutableCustomField,
                ImmutableStack,
                ImmutableFlashcard,
                ImmutableQuestion,
                ImmutableAnswer,
                ImmutableOption,
                ImmutableTag,
                ImmutableStatus,
                ImmutablePriority,
                ImmutableDifficulty,
                ImmutableSetting,
                ImmutableNote,
                ImmutableUser,
                ImmutableDefault,
            ]
        ]
    ]:
        """
        Retrieves objects by their keys.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            keys (List[str]): The keys of the objects to be retrieved.

        Returns:
            Optional[List[Union[ImmutableAssociation, ImmutableCustomField, ImmutableStack, ImmutableFlashcard, ImmutableQuestion, ImmutableAnswer, ImmutableOption, ImmutableTag, ImmutableStatus, ImmutablePriority, ImmutableDifficulty, ImmutableSetting, ImmutableNote, ImmutableUser, ImmutableDefault]]]: The retrieved objects if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to run the 'get_by_keys' method.
        """
        return self.unified_manager.get_by_keys(
            force_refetch=force_refetch,
            keys=keys,
        )

    def on_request_learning_session_create(
        self,
        learning_session: ImmutableLearningSession,
    ) -> Optional[ImmutableLearningSession]:
        """
        Handles the 'request_learning_session_create' event and creates a new learning session in the database.

        Args:
            learning_session (ImmutableLearningSession): The learning session to be created.

        Returns:
            Optional[ImmutableLearningSession]: The created immutable learning session if no exception occurs. Otherwise, None.
        """

        # Create a new learning session in the database and return the created immutable learning session
        return self.unified_manager.create_learning_session(
            learning_session=learning_session
        )

    def on_request_learning_session_delete(
        self,
        learning_session: ImmutableLearningSession,
    ) -> Optional[ImmutableLearningSession]:
        """
        Handles the 'request_learning_session_delete' event and deletes a learning session from the database.

        Args:
            learning_session (ImmutableLearningSession): The learning session to be deleted.

        Returns:
            Optional[ImmutableLearningSession]: The deleted immutable learning session if no exception occurs. Otherwise, None.
        """

        # Delete the learning session from the database and return the deleted immutable learning session
        return self.unified_manager.delete_learning_session(
            learning_session=learning_session
        )

    def on_request_learning_session_load(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[ImmutableLearningSession]:
        """
        Handles the 'request_learning_session_load' event and loads a learning session from the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for querying the learning session.

        Returns:
            Optional[ImmutableLearningSession]: The loaded immutable learning session if no exception occurs. Otherwise, None.
        """

        # Load the learning session from the database and return the loaded immutable learning session
        return self.unified_manager.get_learning_session_by(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_learning_session_lookup(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[ImmutableLearningSession]:
        """
        Handles the 'request_learning_session_lookup' event and looks up a learning session in the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for querying the learning session.

        Returns:
            Optional[ImmutableLearningSession]: The looked up immutable learning session if no exception occurs. Otherwise, None.
        """

        # Look up the learning session in the database and return the looked up immutable learning session
        return self.unified_manager.search_learning_sessions(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_learning_session_update(
        self,
        learning_session: ImmutableLearningSession,
    ) -> Optional[ImmutableLearningSession]:
        """
        Handles the 'request_learning_session_update' event and updates a learning session in the database.

        Args:
            learning_session (ImmutableLearningSession): The learning session to be updated.

        Returns:
            Optional[ImmutableLearningSession]: The updated immutable learning session if no exception occurs. Otherwise, None.
        """

        # Update the learning session in the database and return the updated immutable learning session
        return self.unified_manager.update_learning_session(
            learning_session=learning_session
        )

    def on_request_learning_session_action_create(
        self,
        learning_session_action: ImmutableLearningSessionAction,
    ) -> Optional[ImmutableLearningSessionAction]:
        """
        Handles the 'request_learning_session_action_create' event and creates a new learning session action in the database.

        Args:
            learning_session_action (ImmutableLearningSessionAction): The learning session action to be created.

        Returns:
            Optional[ImmutableLearningSessionAction]: The created immutable learning session action if no exception occurs. Otherwise, None.
        """

        # Create a new learning session action in the database and return the created immutable learning session action
        return self.unified_manager.create_learning_session_action(
            learning_session_action=learning_session_action
        )

    def on_request_learning_session_action_delete(
        self,
        learning_session_action: ImmutableLearningSessionAction,
    ) -> bool:
        """
        Handles the 'request_learning_session_action_delete' event and deletes a learning session action from the database.

        Args:
            learning_session_action (ImmutableLearningSessionAction): The learning session action to be deleted.

        Returns:
            bool: True if the learning session action was deleted successfully. False otherwise.
        """

        # Delete the learning session action from the database and return the result of the deletion
        return self.unified_manager.delete_learning_session_action(
            learning_session_action=learning_session_action
        )

    def on_request_learning_session_action_load(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[ImmutableLearningSessionAction]:
        """
        Handles the 'request_learning_session_action_load' event and loads a learning session action from the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for querying the learning session action.

        Returns:
            Optional[ImmutableLearningSessionAction]: The loaded immutable learning session action if no exception occurs. Otherwise, None.
        """

        # Load the learning session action from the database and return the loaded immutable learning session action
        return self.unified_manager.get_learning_session_action_by(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_learning_session_action_lookup(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[ImmutableLearningSessionAction]:
        """
        Handles the 'request_learning_session_action_lookup' event and looks up a learning session action in the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for querying the learning session action.

        Returns:
            Optional[ImmutableLearningSessionAction]: The looked up immutable learning session action if no exception occurs. Otherwise, None.
        """

        # Look up the learning session action in the database and return the looked up immutable learning session action
        return self.unified_manager.search_learning_session_actions(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_learning_session_action_update(
        self,
        learning_session_action: ImmutableLearningSessionAction,
    ) -> Optional[ImmutableLearningSessionAction]:
        """
        Handles the 'request_learning_session_action_update' event and updates a learning session action in the database.

        Args:
            learning_session_action (ImmutableLearningSessionAction): The learning session action to be updated.

        Returns:
            Optional[ImmutableLearningSessionAction]: The updated immutable learning session action if no exception occurs. Otherwise, None.
        """

        # Update the learning session action in the database and return the updated immutable learning session action
        return self.unified_manager.update_learning_session_action(
            learning_session_action=learning_session_action
        )

    def on_request_learning_session_item_create(
        self,
        learning_session_item: ImmutableLearningSessionItem,
    ) -> Optional[ImmutableLearningSessionItem]:
        """
        Handles the 'request_learning_session_item_create' event and creates a new learning session item in the database.

        Args:
            learning_session_item (ImmutableLearningSessionItem): The learning session item to be created.

        Returns:
            Optional[ImmutableLearningSessionItem]: The created immutable learning session item if no exception occurs. Otherwise, None.
        """

        # Create a new learning session item in the database and return the created immutable learning session item
        return self.unified_manager.create_learning_session_item(
            learning_session_item=learning_session_item
        )

    def on_request_learning_session_item_delete(
        self,
        learning_session_item: ImmutableLearningSessionItem,
    ) -> bool:
        """
        Handles the 'request_learning_session_item_delete' event and deletes a learning session item from the database.

        Args:
            learning_session_item (ImmutableLearningSessionItem): The learning session item to be deleted.

        Returns:
            bool: True if the learning session item was deleted successfully. False otherwise.
        """

        # Delete the learning session item from the database and return the result of the deletion
        return self.unified_manager.delete_learning_session_item(
            learning_session_item=learning_session_item
        )

    def on_request_learning_session_item_load(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[ImmutableLearningSessionItem]:
        """
        Handles the 'request_learning_session_item_load' event and loads a learning session item from the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for querying the learning session item.

        Returns:
            Optional[ImmutableLearningSessionItem]: The loaded immutable learning session item if no exception occurs. Otherwise, None.
        """

        # Load the learning session item from the database and return the loaded immutable learning session item
        return self.unified_manager.get_learning_session_item_by(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_learning_session_item_lookup(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[ImmutableLearningSessionItem]:
        """
        Handles the 'request_learning_session_item_lookup' event and looks up a learning session item in the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for querying the learning session item.

        Returns:
            Optional[ImmutableLearningSessionItem]: The looked up immutable learning session item if no exception occurs. Otherwise, None.
        """

        # Look up the learning session item in the database and return the looked up immutable learning session item
        return self.unified_manager.search_learning_session_items(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_learning_session_item_update(
        self,
        learning_session_item: ImmutableLearningSessionItem,
    ) -> Optional[ImmutableLearningSessionItem]:
        """
        Handles the 'request_learning_session_item_update' event and updates a learning session item in the database.

        Args:
            learning_session_item (ImmutableLearningSessionItem): The learning session item to be updated.

        Returns:
            Optional[ImmutableLearningSessionItem]: The updated immutable learning session item if no exception occurs. Otherwise, None.
        """

        # Update the learning session item in the database and return the updated immutable learning session item
        return self.unified_manager.update_learning_session_item(
            learning_session_item=learning_session_item
        )

    def on_request_note_create(
        self,
        note: ImmutableNote,
    ) -> Optional[ImmutableNote]:
        """
        Handles the 'request_note_create' event and creates a new note in the database.

        Args:
            note (ImmutableNote): The note to be created.

        Returns:
            Optional[ImmutableNote]: The created immutable note if no exception occurs. Otherwise, None.
        """

        # Create a new note in the database and return the created immutable note
        return self.unified_manager.create_note(note=note)

    def on_request_note_delete(
        self,
        note: ImmutableNote,
    ) -> bool:
        """
        Handles the 'request_note_delete' event and deletes a note from the database.

        Args:
            note (ImmutableNote): The note to be deleted.

        Returns:
            bool: True if the note was deleted successfully. False otherwise.
        """

        # Delete the note from the database and return the result of the deletion
        return self.unified_manager.delete_note(note=note)

    def on_request_note_load(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[ImmutableNote]:
        """
        Handles the 'request_note_load' event and loads a note from the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for querying the note.

        Returns:
            Optional[ImmutableNote]: The loaded immutable note if no exception occurs. Otherwise, None.
        """

        # Load the note from the database and return the loaded immutable note
        return self.unified_manager.get_note_by(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_note_lookup(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[ImmutableNote]:
        """
        Handles the 'request_note_lookup' event and looks up notes in the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for querying the note.

        Returns:
            Optional[ImmutableNote]: The loaded immutable note if no exception occurs. Otherwise, None.
        """

        # Retrieve notes using the provided keyword arguments
        return self.unified_manager.search_notes(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_note_update(
        self,
        note: ImmutableNote,
    ) -> Optional[ImmutableNote]:
        """
        Handles the 'request_note_update' event and updates a note in the database.

        Args:
            note (ImmutableNote): The note to be updated.

        Returns:
            Optional[ImmutableNote]: The updated immutable note if no exception occurs. Otherwise, None.
        """

        # Update the note in the database and return the updated note
        return self.unified_manager.update_note(note=note)

    def on_request_option_create(
        self,
        option: ImmutableOption,
    ) -> Optional[ImmutableOption]:
        """
        Handles the 'request_option_create' event and creates a new option in the database.

        Args:
            option (ImmutableOption): The option to be created.

        Returns:
            Optional[ImmutableOption]: The newly created option if no exception occurs. Otherwise, None.
        """

        # Create and return the option
        return self.unified_manager.create_option(option=option)

    def on_request_option_delete(
        self,
        option: ImmutableOption,
    ) -> bool:
        """
        Handles the 'request_option_delete' event and deletes an option from the database.

        Args:
            option (ImmutableOption): The option to be deleted.

        Returns:
            bool: True if the option was deleted successfully. False otherwise.
        """

        # Delete the option from the database and return the result of the deletion
        return self.unified_manager.delete_option(option=option)

    def on_request_option_load(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableOption]]:
        """
        Handles the 'request_option_load' event and loads options from the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: Keyword arguments for filtering the options.

        Returns:
            Optional[List[ImmutableOption]]: A list of immutable options if found. None otherwise.
        """
        return self.unified_manager.get_option_by(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_option_lookup(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableOption]]:
        """
        Handles the 'request_option_lookup' event and looks up options in the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for querying the option.

        Returns:
            Optional[List[ImmutableOption]]: A list of found options if no exception occurs. Otherwise, None.
        """

        # Search for options using the provided keyword arguments and return them
        return self.unified_manager.search_options(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_option_update(
        self,
        option: ImmutableOption,
    ) -> Optional[ImmutableOption]:
        """
        Handles the 'request_option_update' event and updates an option in the database.

        Args:
            option (ImmutableOption): The option to be updated.

        Returns:
            Optional[ImmutableOption]: The updated immutable option if no exception occurs. Otherwise, None.
        """

        # Update the option in the database and return the updated option
        return self.unified_manager.update_option(option=option)

    def on_request_priority_create(
        self,
        priority: ImmutablePriority,
    ) -> Optional[ImmutablePriority]:
        """
        Handles the 'request_priority_create' event and creates a new priority in the database.

        Args:
            priority (ImmutablePriority): The priority to be created.

        Returns:
            Optional[ImmutablePriority]: The created priority object if no exception occurs. Otherwise, None.
        """

        # Create and return the priority
        return self.unified_manager.create_priority(priority=priority)

    def on_request_priority_delete(
        self,
        priority: ImmutablePriority,
    ) -> bool:
        """
        Handles the 'request_priority_delete' event and deletes a priority from the database.

        Args:
            priority (ImmutablePriority): The priority to be deleted.

        Returns:
            bool: True if no exception occurs. Otherwise, False.
        """

        # Delete the priority from the database and return the result
        return self.unified_manager.delete_priority(priority=priority)

    def on_request_priority_load(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutablePriority]]:
        """
        Handles the 'request_priority_load' event and loads a priority from the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for querying the priority.

        Returns:
            Optional[List[ImmutablePriority]]: The loaded immutable priority if no exception occurs. Otherwise, None.
        """

        # Load the priority from the database and return the loaded immutable priority
        return self.unified_manager.get_priority_by(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_priority_lookup(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutablePriority]]:
        """
        Handles the 'request_priority_lookup' event and looks up priorities in the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for querying the priority.

        Returns:
            Optional[List[ImmutablePriority]]: The loaded immutable priority if no exception occurs. Otherwise, None.
        """

        # Load the priority from the database and return the loaded immutable priority
        return self.unified_manager.search_priorities(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_priority_update(
        self,
        priority: ImmutablePriority,
    ) -> Optional[ImmutablePriority]:
        """
        Handles the 'request_priority_update' event and updates a priority in the database.

        Args:
            priority (ImmutablePriority): The priority to be updated.

        Returns:
            Optional[ImmutablePriority]: The updated priority object if no exception occurs. Otherwise, None.
        """

        # Update the priority in the database and return the updated priority
        return self.unified_manager.update_priority(priority=priority)

    def on_request_question_create(
        self,
        question: ImmutableQuestion,
    ) -> Optional[ImmutableQuestion]:
        """
        Handles the 'request_question_create' event and creates a new question in the database.

        Args:
            question (ImmutableQuestion): The question to be created.

        Returns:
            Optional[ImmutableQuestion]: The created immutable question if no exception occurs. Otherwise, None.
        """

        # Create and return the question
        return self.unified_manager.create_question(question=question)

    def on_request_question_delete(
        self,
        question: ImmutableQuestion,
    ) -> bool:
        """
        Handles the 'request_question_delete' event and deletes a question from the database.

        Args:
            question (ImmutableQuestion): The question to be deleted.

        Returns:
            bool: True if the question was deleted successfully. False otherwise.
        """

        # Delete the question from the database and return the result of the deletion
        return self.unified_manager.delete_question(question=question)

    def on_request_question_load(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableQuestion]]:
        """
        Handles the 'request_question_load' event and loads questions from the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be passed to the database query.

        Returns:
            Optional[List[ImmutableQuestion]]: A list of loaded questions if no exception occurs. Otherwise, None.
        """

        # Load the questions from the database using the provided keyword arguments
        return self.unified_manager.get_question_by(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_question_lookup(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableQuestion]]:
        """
        Handles the 'request_question_lookup' event and searches for questions in the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for searching questions.

        Returns:
            Optional[List[ImmutableQuestion]]: A list of found questions if no exception occurs. Otherwise, None.
        """

        # Search for questions using the provided keyword arguments and return them
        return self.unified_manager.search_questions(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_question_update(
        self,
        question: ImmutableQuestion,
    ) -> Optional[ImmutableQuestion]:
        """
        Handles the 'request_question_update' event and updates a question in the database.

        Args:
            question (ImmutableQuestion): The question to be updated.

        Returns:
            Optional[ImmutableQuestion]: The updated immutable question if no exception occurs. Otherwise, None.
        """

        # Update the question in the database and return the result of the update
        return self.unified_manager.update_question(question=question)

    def on_request_setting_create(
        self,
        setting: ImmutableSetting,
    ) -> Optional[ImmutableSetting]:
        """
        Handles the 'request_setting_create' event and creates a new setting in the database.

        Args:
            setting (ImmutableSetting): The setting to be created.

        Returns:
            Optional[ImmutableSetting]: The created immutable setting if no exception occurs. Otherwise, None.
        """

        # Create a new setting in the database and return the created setting
        return self.unified_manager.create_setting(setting=setting)

    def on_request_setting_delete(
        self,
        setting: ImmutableSetting,
    ) -> Optional[ImmutableSetting]:
        """
        Handles the 'request_setting_delete' event and deletes a setting from the database.

        Args:
            setting (ImmutableSetting): The setting to be deleted.

        Returns:
            Optional[ImmutableSetting]: The deleted immutable setting if no exception occurs. Otherwise, None.
        """

        # Delete the setting from the database and return the deleted setting
        return self.unified_manager.delete_setting(setting=setting)

    def on_request_setting_load(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableSetting]]:
        """
        Handles the 'request_setting_load' event and loads settings from the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: Keyword arguments to be passed to the database query.

        Returns:
            Optional[List[ImmutableSetting]]: The loaded settings if no exception occurs. Otherwise, None.
        """

        # Load the settings from the database and return them
        return self.unified_manager.load_settings(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_setting_lookup(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableSetting]]:
        """
        Handles the 'request_setting_lookup' event and searches for settings in the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for searching settings.

        Returns:
            Optional[List[ImmutableSetting]]: The found settings if no exception occurs. Otherwise, None.
        """

        # Search for settings using the provided keyword arguments and return them
        return self.unified_manager.search_settings(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_setting_update(
        self,
        setting: ImmutableSetting,
    ) -> Optional[ImmutableSetting]:
        """
        Handles the 'request_setting_update' event and updates an existing setting in the database.

        Args:
            setting (ImmutableSetting): The setting to be updated.

        Returns:
            Optional[ImmutableSetting]: The updated immutable setting if no exception occurs. Otherwise, None.
        """

        # Update the setting in the database and return the updated setting
        return self.unified_manager.update_setting(setting=setting)

    def on_request_stack_create(
        self,
        stack: ImmutableStack,
    ) -> Optional[ImmutableStack]:
        """
        Handles the 'request_stack_create' event and creates a new stack in the database.

        Args:
            stack (ImmutableStack): The stack to be created.

        Returns:
            Optional[ImmutableStack]: The created immutable stack if no exception occurs. Otherwise, None.
        """

        # Create a new stack in the database and return the created stack
        return self.unified_manager.create_stack(stack=stack)

    def on_request_stack_delete(
        self,
        stack: ImmutableStack,
    ) -> bool:
        """
        Handles the 'request_stack_delete' event and deletes a stack from the database.

        Args:
            stack (ImmutableStack): The stack to be deleted.

        Returns:
            bool: True if the stack is deleted successfully, False otherwise.
        """

        # Delete the stack from the database and return the result of the deletion
        return self.unified_manager.delete_stack(stack=stack)

    def on_request_stack_load(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableStack]]:
        """
        Handles the 'request_stack_load' event and loads stacks from the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for querying stacks.

        Returns:
            Optional[List[ImmutableStack]]: A list of loaded stacks if no exception occurs. Otherwise, None.
        """

        # Load stacks using the provided keyword arguments and return them
        return self.unified_manager.get_stack_by(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_stack_lookup(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableStack]]:
        """
        Handles the 'request_stack_lookup' event and searches for stacks in the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for searching stacks.

        Returns:
            Optional[List[ImmutableStack]]: A list of found stacks if no exception occurs. Otherwise, None.
        """

        # Search for stacks using the provided keyword arguments and return them
        return self.unified_manager.search_stacks(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_stack_update(
        self,
        stack: ImmutableStack,
    ) -> Optional[ImmutableStack]:
        """
        Handles the 'request_stack_update' event and updates a stack in the database.

        Args:
            stack (ImmutableStack): The stack to be updated.

        Returns:
            Optional[ImmutableStack]: The updated immutable stack if no exception occurs. Otherwise, None.
        """

        # Update the stack in the database and return the result of the update
        return self.unified_manager.update_stack(stack=stack)

    def on_request_status_create(
        self,
        status: ImmutableStatus,
    ) -> Optional[ImmutableStatus]:
        """
        Handles the 'request_status_create' event and creates a new status in the database.

        Args:
            status (ImmutableStatus): The status to be created.

        Returns:
            Optional[ImmutableStatus]: The created immutable status if no exception occurs. Otherwise, None.
        """

        # Create a new status in the database and return the created status
        return self.unified_manager.create_status(status=status)

    def on_request_status_delete(
        self,
        status: ImmutableStatus,
    ) -> bool:
        """
        Handles the 'request_status_delete' event and deletes a status from the database.

        Args:
            status (ImmutableStatus): The status to be deleted.

        Returns:
            bool: True if the status is deleted successfully, False otherwise.
        """

        # Delete the status from the database and return the result of the deletion
        return self.unified_manager.delete_status(status=status)

    def on_request_status_load(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableStatus]]:
        """
        Handles the 'request_status_load' event and loads statuses from the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for loading statuses.

        Returns:
            Optional[List[ImmutableStatus]]: A list of loaded statuses if no exception occurs. Otherwise, None.
        """

        # Load statuses using the provided keyword arguments and return them
        return self.unified_manager.get_status_by(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_status_lookup(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableStatus]]:
        """
        Handles the 'request_status_lookup' event and searches for statuses in the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for searching statuses.

        Returns:
            Optional[List[ImmutableStatus]]: A list of found statuses if no exception occurs. Otherwise, None.
        """

        # Search for statuses using the provided keyword arguments and return them
        return self.unified_manager.search_statuses(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_status_update(
        self,
        status: ImmutableStatus,
    ) -> Optional[ImmutableStatus]:
        """
        Handles the 'request_status_update' event and updates a status in the database.

        Args:
            status (ImmutableStatus): The status to be updated.

        Returns:
            Optional[ImmutableStatus]: The updated immutable status if no exception occurs. Otherwise, None.
        """

        # Update the status in the database and return the result of the update
        return self.unified_manager.update_status(status=status)

    def on_request_tag_create(
        self,
        tag: ImmutableTag,
    ) -> Optional[ImmutableTag]:
        """
        Handles the 'request_tag_create' event and creates a new tag in the database.

        Args:
            tag (ImmutableTag): The tag to be created.

        Returns:
            Optional[ImmutableTag]: The created immutable tag if no exception occurs. Otherwise, None.
        """

        # Create the tag in the database and return the result of the creation
        return self.unified_manager.create_tag(tag=tag)

    def on_request_tag_delete(
        self,
        tag: ImmutableTag,
    ) -> bool:
        """
        Handles the 'request_tag_delete' event and deletes a tag from the database.

        Args:
            tag (ImmutableTag): The tag to be deleted.

        Returns:
            bool: True if the tag was deleted successfully. False otherwise.
        """

        # Delete the tag in the database and return the result of the deletion
        return self.unified_manager.delete_tag(tag=tag)

    def on_request_tag_load(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableTag]]:
        """
        Handles the 'request_tag_load' event and loads tags from the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for querying tags.

        Returns:
            Optional[List[ImmutableTag]]: A list of loaded tags if no exception occurs. Otherwise, None.
        """

        # Retrieve tags using the provided keyword arguments
        return self.unified_manager.get_tag_by(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_tag_lookup(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableTag]]:
        """
        Handles the 'request_tag_lookup' event and looks up tags in the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for querying tags.

        Returns:
            Optional[List[ImmutableTag]]: A list of loaded tags if no exception occurs. Otherwise, None.
        """

        # Retrieve tags using the provided keyword arguments
        return self.unified_manager.search_tags(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_tag_update(
        self,
        tag: ImmutableTag,
    ) -> Optional[ImmutableTag]:
        """
        Handles the 'request_tag_update' event and updates a tag in the database.

        Args:
            tag (ImmutableTag): The tag to be updated.

        Returns:
            Optional[ImmutableTag]: The updated immutable tag if no exception occurs. Otherwise, None.
        """

        # Update the tag in the database and return the result of the update
        return self.unified_manager.update_tag(tag=tag)

    def on_request_update(
        self,
        update: Union[
            ImmutableAssociation,
            ImmutableCustomField,
            ImmutableStack,
            ImmutableFlashcard,
            ImmutableQuestion,
            ImmutableAnswer,
            ImmutableOption,
            ImmutableTag,
            ImmutableStatus,
            ImmutablePriority,
            ImmutableDifficulty,
            ImmutableSetting,
            ImmutableNote,
            ImmutableUser,
            ImmutableDefault,
        ],
    ) -> Union[
        ImmutableAssociation,
        ImmutableCustomField,
        ImmutableStack,
        ImmutableFlashcard,
        ImmutableQuestion,
        ImmutableAnswer,
        ImmutableOption,
        ImmutableTag,
        ImmutableStatus,
        ImmutablePriority,
        ImmutableDifficulty,
        ImmutableSetting,
        ImmutableNote,
        ImmutableUser,
        ImmutableDefault,
    ]:
        """
        Handles the 'request_update' event and updates an existing object in the database.

        Args:
            update (Union[ImmutableAssociation, ...]): The object to be updated.

        Returns:
            Union[ImmutableAssociation, ...]: The updated object if no exception occurs. Otherwise, None.
        """

        # Update the object in the database and return the result of the update
        return self.unified_manager.update(update=update)

    def on_request_update_in_bulk(
        self,
        updates: List[
            Union[
                ImmutableAssociation,
                ImmutableCustomField,
                ImmutableStack,
                ImmutableFlashcard,
                ImmutableQuestion,
                ImmutableAnswer,
                ImmutableOption,
                ImmutableTag,
                ImmutableStatus,
                ImmutablePriority,
                ImmutableDifficulty,
                ImmutableSetting,
                ImmutableNote,
                ImmutableUser,
                ImmutableDefault,
            ]
        ],
    ) -> List[
        Union[
            ImmutableAssociation,
            ImmutableCustomField,
            ImmutableStack,
            ImmutableFlashcard,
            ImmutableQuestion,
            ImmutableAnswer,
            ImmutableOption,
            ImmutableTag,
            ImmutableStatus,
            ImmutablePriority,
            ImmutableDifficulty,
            ImmutableSetting,
            ImmutableNote,
            ImmutableUser,
            ImmutableDefault,
        ]
    ]:
        """
        Handles the 'request_update_in_bulk' event and updates a existing objecta in the database.

        Args:
            updates (List[Union[ImmutableAssociation, ...]]): The objects to be updated.

        Returns:
            List[Union[ImmutableAssociation, ...]]: The updated objects if no exception occurs. Otherwise, None.
        """

        # Update the object in the database and return the result of the update
        return self.unified_manager.update_in_bulk(updates=updates)

    def on_request_user_create(
        self,
        user: ImmutableUser,
    ) -> Optional[ImmutableUser]:
        """
        Handles the 'request_user_create' event and creates a new user in the database.

        Args:
            user (ImmutableUser): The user to be created.

        Returns:
            Optional[ImmutableUser]: The newly created immutable user if no exception occurs. Otherwise, None.
        """

        # Create the user in the database and return the result of the creation
        return self.unified_manager.create_user(user=user)

    def on_request_user_delete(
        self,
        user: ImmutableUser,
    ) -> bool:
        """
        Handles the 'request_user_delete' event and deletes a user from the database.

        Args:
            user (ImmutableUser): The user to be deleted.

        Returns:
            bool: True if the user was deleted successfully. False otherwise.
        """

        # Delete the user in the database and return the result of the deletion
        return self.unified_manager.delete_user(user=user)

    def on_request_user_load(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableUser]]:
        """
        Handles the 'request_user_load' event and loads users from the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for querying users.

        Returns:
            Optional[List[ImmutableUser]]: A list of loaded users if no exception occurs. Otherwise, None.
        """

        # Retrieve users using the provided keyword arguments
        return self.unified_manager.get_user_by(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_user_lookup(
        self,
        force_refetch: bool = False,
        **kwargs,
    ) -> Optional[List[ImmutableUser]]:
        """
        Handles the 'request_user_lookup' event and looks up users in the database.

        Args:
            force_refetch (bool): Forces the manager to refetch from the database. Defaults to False.
            **kwargs: The keyword arguments to be used for querying users.

        Returns:
            Optional[List[ImmutableUser]]: A list of loaded users if no exception occurs. Otherwise, None.
        """

        # Retrieve users using the provided keyword arguments
        return self.unified_manager.search_users(
            force_refetch=force_refetch,
            **kwargs,
        )

    def on_request_user_update(
        self,
        user: ImmutableUser,
    ) -> Optional[ImmutableUser]:
        """
        Handles the 'request_user_update' event and updates a user in the database.

        Args:
            user (ImmutableUser): The user to be updated.

        Returns:
            Optional[ImmutableUser]: The updated immutable user if no exception occurs. Otherwise, None.
        """

        # Update the user in the database and return the result of the update
        return self.unified_manager.update_user(user=user)
