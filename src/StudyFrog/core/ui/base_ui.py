"""
Author: lodego
Date: 2025-03-15
"""

import tkinter

from tkinter.constants import *

from typing import *

from core.setting import SettingService

from core.ui.ui_builder import UIBuilder

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous
from utils.navigation import NavigationHistoryItem, NavigationHistoryService
from utils.unified import UnifiedObjectManager


__all__: List[str] = ["BaseUI"]


class BaseUI(tkinter.Frame):
    """
    A base class for all UI components in the application.

    This class provides common functionality for all UI components, such as
    subscribing to events, unsubscribing from events, configuring the grid
    layout, creating widgets, and handling the destroy event. It also provides
    a logger instance that can be used to log messages.

    Attributes:
        dispatcher (Dispatcher): The dispatcher instance.
        logger (Logger): The logger instance.
        navigation_item (NavigationHistoryItem): The navigation history item instance.
        navigation_service (NavigationHistoryService): The navigation history service instance.
        setting_service (SettingService): The setting service instance.
        unified_manager (UnifiedObjectManager): The unified manager instance.
    """

    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        name: str,
        navigation_item: NavigationHistoryItem,
        navigation_service: NavigationHistoryService,
        setting_service: SettingService,
        unified_manager: UnifiedObjectManager,
    ) -> None:
        """
        Initializes a new instance of the BaseUI class.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.
            master (tkinter.Misc): The parent widget.
            name (str): The name of the UI component.
            navigation_item (NavigationHistoryItem): The navigation history item instance.
            navigation_service (NavigationHistoryService): The navigation history service instance.
            setting_service (SettingService): The setting service instance.
            unified_manager (UnifiedObjectManager): The unified manager instance.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            master=master,
            name=name,
        )

        # Initialize the logger instance
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed dispatcher instance in an instance variable
        self.dispatcher: Dispatcher = dispatcher

        # Store the passed navigation item instance in an instance variable
        self.navigation_item: NavigationHistoryItem = navigation_item

        # Store the passed navigation service instance in an instance variable
        self.navigation_service: NavigationHistoryService = navigation_service

        # Store the passed setting service instance in an instance variable
        self.setting_service: SettingService = setting_service

        # Store the passed unified manager instance in an instance variable
        self.unified_manager: UnifiedObjectManager = unified_manager

        # Configure the frame
        self.configure(background=Constants.BLUE_GREY["700"])

        # Configure the grid
        self.configure_grid()

        # Create widgets
        self.create_widgets()

        # Grid the frame
        self.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

    def collect_subscriptions(self) -> Dict[Any, Dict[str, Any]]:
        """
        Collects and returns a dictionary of subscriptions.

        This method should be implemented by subclasses to provide
        a dictionary containing event subscriptions. Each subscription
        is associated with specific events and their corresponding
        handlers.

        Returns:
            Dict[Any, Dict[str, Any]]: A dictionary representing
            the subscriptions for events.

        Raises:
            NotImplementedError: If the method is not implemented
            by a subclass.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement 'collect_subscriptions' method."
        )

    def configure_grid(self) -> None:
        """
        Configures the grid layout for the UI component.

        This method should be implemented by subclasses to set the
        grid configuration for the UI component. It is responsible for
        defining how the columns and rows should be weighted and aligned.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement 'configure_grid' method."
        )

    def create_widgets(self) -> None:
        """
        Creates and configures the widgets for the UI component.

        This method should be implemented by subclasses to create and configure
        the widgets that will be displayed in the UI component. It is responsible
        for setting up the layout and behavior of the widgets.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement 'create_widgets' method."
        )

    def destroy(self) -> None:
        """
        Cleans up resources and unsubscribes from events.

        This method attempts to unsubscribe from all events
        and calls the parent class's destroy method to clean
        up resources. Logs any exceptions that occur.

        Returns:
            None

        Raises:
            Exception: If an error occurs during the destroy process.
        """
        try:
            # Attempt to unsubscribe from all events
            self.unsubscribe_from_events()

            # Log an info message
            self.logger.info(
                message=f"Unsubscribed from all events. Destroying '{self.__class__.__name__}' instance..."
            )

            # Call the parent class's destroy method
            super().destroy()
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'destroy' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def subscribe_to_events(self) -> None:
        """
        Subscribes to all events in the subscriptions dictionary.

        This method iterates over the events and functions in the subscriptions
        dictionary and registers them with the dispatcher. It also stores the
        UUIDs of the subscriptions in the subscriptions list.

        Returns:
            None

        Raises:
            Exception: If an error occurs while subscribing to events.
        """
        try:
            # Check if a "subscriptions" list exists as instance variable
            if not hasattr(
                self,
                "subscriptions",
            ):
                # Initialize the subscriptions list as an empty list
                self.subscriptions: List[str] = []

            # Create a dictionary of events and functions
            subscriptions: Dict[Any, Dict[str, Any]] = self.collect_subscriptions()

            # Iterate over the events and functions in the subscriptions dictionary
            for (
                event,
                subscription,
            ) in subscriptions.items():
                # Store the UUID of the subscription in the subscriptions list
                self.subscriptions.append(
                    self.dispatcher.register(
                        event=event,
                        function=subscription["function"],
                        namespace=subscription["namespace"],
                        persistent=subscription["persistent"],
                    )
                )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'subscribe_to_events' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def unsubscribe_from_events(self) -> None:
        """
        Unsubscribes from all events subscribed in the edit UI.

        This method iterates over the UUIDs in the subscriptions dictionary and
        unregisters the event handlers associated with each UUID.

        Returns:
            None

        Raises:
            Exception: If an error occurs while unsubscribing from events.
        """
        try:
            # Iterate over the UUIDs in the subscriptions dictionary
            for uuid in self.subscriptions:
                # Unregister the handler for the given UUID
                self.dispatcher.unregister(uuid=uuid)
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'unsubscribe_from_events' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e
