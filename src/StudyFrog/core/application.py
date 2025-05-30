"""
Author: lodego
Date: 2025-02-06
"""

import traceback

from datetime import datetime

from typing import *

from core.ui.main_ui import MainUI

from utils.bootstrap_service import BootstrapService
from utils.constants import Constants
from utils.events import Events
from utils.logger import Logger
from utils.utils import DateUtil
from utils.toast_notification_service import ToastNotificationService
from utils.toplevel_notification_service import ToplevelNotificationService


__all__: Final[List[str]] = ["Application"]


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

        Initializes the Application instance by setting a logger to the logger with the name of the class,
        bootstrapping the application services, and initializing the main UI.

        Returns:
            None
        """

        # Get the start time
        self.start_time: datetime = DateUtil.now()

        # Initialize a logger
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Bootstrap the application services
        self.bootstrap_service: BootstrapService = BootstrapService()

        # Initialize the dispatcher, navigation service, notification service, setting service, unified manager, and unified object service
        (
            self.dispatcher,
            self.navigation_service,
            self.notification_service,
            self.setting_service,
            self.unified_factory,
            self.unified_manager,
            self.unified_object_service,
        ) = self.bootstrap_service.run_startup_tasks()

        # Initialize the main UI
        self.main_ui: MainUI = MainUI(
            dispatcher=self.dispatcher,
            navigation_service=self.navigation_service,
            setting_service=self.setting_service,
            unified_factory=self.unified_factory,
            unified_manager=self.unified_manager,
        )

        # Initialize the toast and toplevel notification services
        self.toast_notification_service: ToastNotificationService = ToastNotificationService(
            dispatcher=self.dispatcher,
        )

        # Initialize the toplevel notification service
        self.toplevel_notification_service: ToplevelNotificationService = ToplevelNotificationService(
            dispatcher=self.dispatcher,
        )

    def start_application(self) -> None:
        try:
            # Dispatch the "APPLICATION_STARTED" event in the global namespace
            self.dispatcher.dispatch(
                event=Events.APPLICATION_STARTED,
                namespace=Constants.GLOBAL_NAMESPACE,
            )

            # Dispatch the "REQUEST_VALIDATE_NAVIGATION" event in the global namespace
            self.dispatcher.dispatch(
                direction="forward",
                event=Events.REQUEST_VALIDATE_NAVIGATION,
                namespace=Constants.GLOBAL_NAMESPACE,
                source="application",
                target="dashboard_ui",
            )

            # Log a info message indicating the application has started
            self.logger.info(message=f"Started {Constants.APPLICATION_NAME}")

            # Subscribe to events
            self.subscribe_to_events()

            # Show the main UI
            self.main_ui.mainloop()
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'start' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Exit the application with a non-zero exit code indicating an exception occurred
            exit(1)
    
    def subscribe_to_events(self) -> None:
        """
        Registers the stop application function with the dispatcher.

        This method subscribes the stop_application method to the REQUEST_APPLICATION_STOP
        event in the global namespace. It ensures that the stop_application method is called
        whenever the corresponding event is triggered.

        Returns:
            None

        Raises:
            Exception: If an error occurs during the registration process.
        """
        try:
            # Register the stop_application function with the dispatcher
            self.dispatcher.register(
                event=Events.REQUEST_APPLICATION_STOP,
                function=self.stop_application,
                namespace=Constants.GLOBAL_NAMESPACE,
                persistent=False,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'subscribe_to_events' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def stop_application(self) -> None:
        """
        Stops the application.

        Runs the shutdown tasks and dispatches the "APPLICATION_STOPPED" event in the global namespace.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while running the shutdown tasks.
        """
        try:
            # Run the shutdown tasks
            self.bootstrap_service.run_shutdown_tasks()

            # Dispatch the "APPLICATION_STOPPED" event in the global namespace
            self.dispatcher.dispatch(
                event=Events.APPLICATION_STOPPED,
                namespace=Constants.GLOBAL_NAMESPACE,
            )

            # Log an info message indicating the application has been stopped
            self.logger.info(
                message=f"{Constants.APPLICATION_NAME} ran for {DateUtil.calculate_duration(start=self.start_time)} seconds"
            )

            # Log an info message indicating the application has been stopped
            self.logger.info(
                message=f"{Constants.APPLICATION_NAME} has been stopped. Goodbye!"
            )

            # Exit the application with a zero exit code indicating no exception occurred
            exit(0)
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'stop' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Exit the application with a non-zero exit code indicating an exception occurred
            exit(1)
