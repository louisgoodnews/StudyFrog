"""
Author: lodego
Date: 2025-02-09
"""

from typing import *

from utils.logger import Logger


class UnifiedManager:
    """
    A singleton manager class for registering and managing multiple manager instances.

    This class provides methods to create a single shared instance of the UnifiedManager,
    initialize it with a logger and a dictionary for storing registered managers, and
    register manager instances using their class names as keys.

    Attributes:
        _shared_instance (Optional[UnifiedManager]): The shared singleton instance of the class.
        logger (Logger): The logger instance associated with the UnifiedManager.
        managers (Dict[str, Any]): The dictionary storing registered managers.
    """

    _shared_instance: Optional["UnifiedManager"] = None

    def __new__(cls) -> "UnifiedManager":
        """
        Creates and returns a new instance of the UnifiedManager class.

        If the instance does not exist, creates a new one by calling the parent class constructor.
        If the instance already exists, returns the existing instance.

        Returns:
            UnifiedManager: The created or existing instance of UnifiedManager class.
        """
        if cls._shared_instance is None:
            cls._shared_instance = super().__new__(cls)
            cls._shared_instance.init()
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes the UnifiedManager instance by creating a logger and an empty dictionary for storing registered managers.

        Returns:
            None
        """
        # Create a logger instance for the UnifiedManager class
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Initialize an empty dictionary for storing registered managers
        self.managers: Dict[str, Any] = {}

    def __getattr__(
        self,
        name: str,
    ) -> Any:
        """
        Automatically routes method calls to the appropriate manager.

        If `unified_manager.get_flashcard_by_id(1234)` is called,
        this method automatically forwards it to `FlashcardManager.get_flashcard_by_id(1234)`.
        """

        # Check if the method is available on the UnifiedManager instance
        if not hasattr(
            self,
            name,
        ):
            # Iterate over the registered managers and check if the method is available
            for (
                manager_name,
                manager_instance,
            ) in self.managers.items():
                if hasattr(
                    manager_instance,
                    name,
                ):
                    return getattr(
                        manager_instance,
                        name,
                    )

        # If the method is available, return the result of calling it
        return getattr(
            self,
            name,
        )

    def register_manager(
        self,
        name: str,
        manager: Type[Any],
    ) -> None:
        """
        Registers a manager instance with the UnifiedManager.

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
            raise AttributeError(f"Manager '{manager}' not found in UnifiedManager.")

        # Get the manager instance from the dictionary
        manager_instance: Any = self.managers[manager]

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
