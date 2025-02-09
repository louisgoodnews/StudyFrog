"""
Author: lodego
Date: 2025-02-06
"""

from typing import *

from core.ui.main_ui import MainUI

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.logger import Logger
from utils.navigation import NavigationService


__all__: List[str] = ["Application"]


class Application:
    """
    Represents the application.

    This class provides a singleton instance for the application, which is accessible via the `Application` class.

    Attributes:
        logger (Logger): The logger instance associated with the application.
    """

    _shared_instance: Optional["Application"] = None

    def __new__(cls) -> "Application":
        """
        Creates and returns a new instance of Application class.

        If the instance does not exist, creates a new one by calling the parent class constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Returns:
            Application: The created or existing instance of Application class.
        """
        if cls._shared_instance is None:
            cls._shared_instance = super().__new__(cls)
            cls._shared_instance.init()
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes the Application instance.

        Initializes the Application instance by setting a logger to the logger with the name of the class.

        Returns:
            None
        """

        # Initialize a logger
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Initialize the dispatcher
        self.dispatcher: Dispatcher = Dispatcher()

        # Initialize the navigation service
        self.navigation_service: NavigationService = NavigationService(
            dispatcher=self.dispatcher
        )

        # Initialize the main UI
        self.main_ui: MainUI = MainUI(
            dispatcher=self.dispatcher,
            navigation_service=self.navigation_service,
        )

    def start(self) -> None:
        try:
            # Dispatch the "APPLICATION_STARTED" event in the global namespace
            self.dispatcher.dispatch(
                event=Events.APPLICATION_STARTED,
                namespace=Constants.GLOBAL_NAMESPACE,
            )

            # Show the main UI
            self.main_ui.mainloop()
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'start' method from '{self.__class__.__name__}': {e}"
            )

            # Exit the application with a non-zero exit code indicating an exception occurred
            exit(1)

    def stop(self) -> None:
        try:
            # Exit the application with a zero exit code indicating no exception occurred
            exit(0)
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'stop' method from '{self.__class__.__name__}': {e}"
            )

            # Exit the application with a non-zero exit code indicating an exception occurred
            exit(1)
