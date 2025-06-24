"""
Author: lodego
Date: 2025-05-20
"""

import traceback

from tkinter.constants import *
from typing import *

from core.ui.notifications.notifications import ToplevelNotification

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.object import ImmutableBaseObject


__all__: Final[List[str]] = ["ToplevelNotificationService"]


class ToplevelNotificationService(ImmutableBaseObject):
    """
    A class representing a toplevel notification service.

    This class provides a singleton instance for the toplevel notification service, which is accessible via the `ToplevelNotificationService` class.

    Attributes:
        None
    """

    # The shared instance of the toplevel notification service
    _shared_instance: Optional["ToplevelNotificationService"] = None

    def __new__(
        cls,
        dispatcher: Dispatcher,
    ) -> "ToplevelNotificationService":
        """
        Creates and returns a new instance of the ToplevelNotificationService class.

        If the instance does not exist, creates a new one by calling the parent class constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.

        Returns:
            ToplevelNotificationService: The created or existing instance of ToplevelNotificationService class.
        """
        if cls._shared_instance is None:
            cls._shared_instance = super(ToplevelNotificationService, cls).__new__(cls)
            cls._shared_instance.init(dispatcher=dispatcher)
        return cls._shared_instance

    def init(
        self,
        dispatcher: Dispatcher,
    ) -> None:
        """
        Initializes the toplevel notification service.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            dispatcher=dispatcher,
            subscriptions=[],
        )

        # Subscribe to events
        self.subscribe_to_events()

        # Log an info message about successfull initialization
        self.logger.info(
            message=f"Successfully initialized '{self.__class__.__name__}'"
        )

    def collect_subscriptions(self) -> List[Dict[str, Any]]:
        """
        Collects and returns a list of subscriptions.

        This method creates a list of dictionaries containing event subscription configurations.

        Args:
            None

        Returns:
            List[Dict[str, Any]]: A list representing the subscriptions for events.
        """

        # Initialize the list of subscriptions
        subscriptions: List[Dict[str, Any]] = [
            {
                "event": Events.APPLICATION_STOPPED,
                "function": self.on_application_stopped,
                "namespace": Constants.GLOBAL_NAMESPACE,
                "persistent": False,
            },
            {
                "event": Events.REQUEST_SHOW_CANCEL_TOPLEVEL,
                "function": self.on_request_show_cancel,
                "namespace": Constants.GLOBAL_NAMESPACE,
                "persistent": True,
            },
            {
                "event": Events.REQUEST_SHOW_OKAY_TOPLEVEL,
                "function": self.on_request_show_okay,
                "namespace": Constants.GLOBAL_NAMESPACE,
                "persistent": True,
            },
            {
                "event": Events.REQUEST_SHOW_OKAY_CANCEL_TOPLEVEL,
                "function": self.on_request_show_okay_cancel,
                "namespace": Constants.GLOBAL_NAMESPACE,
                "persistent": True,
            },
            {
                "event": Events.REQUEST_SHOW_RETRY_TOPLEVEL,
                "function": self.on_request_show_retry,
                "namespace": Constants.GLOBAL_NAMESPACE,
                "persistent": True,
            },
            {
                "event": Events.REQUEST_SHOW_RETRY_CANCEL_TOPLEVEL,
                "function": self.on_request_show_retry_cancel,
                "namespace": Constants.GLOBAL_NAMESPACE,
                "persistent": True,
            },
            {
                "event": Events.REQUEST_SHOW_YES_NO_TOPLEVEL,
                "function": self.on_request_show_yes_no,
                "namespace": Constants.GLOBAL_NAMESPACE,
                "persistent": True,
            },
            {
                "event": Events.REQUEST_SHOW_YES_NO_CANCEL_TOPLEVEL,
                "function": self.on_request_show_yes_no_cancel,
                "namespace": Constants.GLOBAL_NAMESPACE,
                "persistent": True,
            },
        ]

        # Return the list of subscriptions
        return subscriptions

    def on_application_stopped(self) -> bool:
        """
        Unsubscribes from all events subscribed in the edit UI.

        This method iterates over the UUIDs in the subscriptions dictionary and
        unregisters the event handlers associated with each UUID.

        Returns:
            bool: True if the events were unsubscribed successfully, False otherwise.
        """
        try:
            # Unsubscribe from events
            self.unsubscribe_from_events()

            # Log an info message about successful shutdown
            self.logger.info(
                message=f"Successfully shut down '{self.__class__.__name__}'"
            )

            # Return True to the caller
            return True
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_application_stopped' method from '{self.__class__.__name__}': {e}",
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Log a warning message about failed shutdown
            self.logger.warning(
                message=f"Failed to shut down '{self.__class__.__name__}'"
            )

            # Return False to the caller
            return False

    def on_request_show_cancel(
        self,
        message: str,
        title: str,
        on_click_callback: Optional[Callable[[str], None]] = None,
    ) -> Optional[str]:
        """
        Shows a cancel toplevel notification.

        This method shows a toplevel notification with a cancel button and a message label.
        It also sets up the geometry of the widget and places the widgets within the grid.

        Args:
            message (str): The message to display in the message label
            title (str): The title of the toplevel widget
            on_click_callback (Optional[Callable[[str], None]]): The callback to execute when the cancel button is clicked

        Returns:
            Optional[str]: The result of the callback function

        Raises:
            Exception: If an error occurs while showing the toplevel notification
        """
        try:
            # Initialize and return the value of the 'cancel' method from the 'ToplevelNotification' class
            return ToplevelNotification.cancel(
                cancel_button={
                    "background": Constants.BLUE_GREY["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                message=message,
                message_label={
                    "background": Constants.BLUE_GREY["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                on_click_callback=on_click_callback,
                title=title,
                title_label={
                    "background": Constants.BLUE_GREY["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.LARGE_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                toplevel={"background": Constants.BLUE_GREY["700"]},
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_show_cancel' method from '{self.__class__.__name__}': {e}",
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None to the caller
            return None

    def on_request_show_okay(
        self,
        message: str,
        title: str,
        on_click_callback: Optional[Callable[[str], None]] = None,
    ) -> Optional[str]:
        """
        Shows a okay toplevel notification.

        This method shows a toplevel notification with an okay button and a message label.
        It also sets up the geometry of the widget and places the widgets within the grid.

        Args:
            message (str): The message to display in the message label
            title (str): The title of the toplevel widget
            on_click_callback (Optional[Callable[[str], None]]): The callback to execute when the cancel button is clicked

        Returns:
            Optional[str]: The result of the callback function

        Raises:
            Exception: If an error occurs while showing the toplevel notification
        """
        try:
            # Initialize and return the value of the 'okay' method from the 'ToplevelNotification' class
            return ToplevelNotification.okay(
                message=message,
                message_label={
                    "background": Constants.BLUE_GREY["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                okay_button={
                    "background": Constants.BLUE_GREY["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                on_click_callback=on_click_callback,
                title=title,
                title_label={
                    "background": Constants.BLUE_GREY["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.LARGE_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                toplevel={"background": Constants.BLUE_GREY["700"]},
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_show_okay' method from '{self.__class__.__name__}': {e}",
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None to the caller
            return None

    def on_request_show_okay_cancel(
        self,
        message: str,
        title: str,
        on_click_callback: Optional[Callable[[str], None]] = None,
    ) -> Optional[str]:
        """
        Shows an okay/cancel toplevel notification.

        This method shows a toplevel notification with an okay and cancel button and a message label.
        It also sets up the geometry of the widget and places the widgets within the grid.

        Args:
            message (str): The message to display in the message label
            title (str): The title of the toplevel widget
            on_click_callback (Optional[Callable[[str], None]]): The callback to execute when the cancel button is clicked

        Returns:
            Optional[str]: The result of the callback function

        Raises:
            Exception: If an error occurs while showing the toplevel notification
        """
        try:
            # Initialize and return the value of the 'okay_cancel' method from the 'ToplevelNotification' class
            return ToplevelNotification.okay_cancel(
                cancel_button={
                    "background": Constants.RED["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                message=message,
                message_label={
                    "background": Constants.BLUE_GREY["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                okay_button={
                    "background": Constants.GREEN["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                on_click_callback=on_click_callback,
                title=title,
                title_label={
                    "background": Constants.BLUE_GREY["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.LARGE_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                toplevel={"background": Constants.BLUE_GREY["700"]},
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_show_okay_cancel' method from '{self.__class__.__name__}': {e}",
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None to the caller
            return None

    def on_request_show_retry(
        self,
        message: str,
        title: str,
        on_click_callback: Optional[Callable[[str], None]] = None,
    ) -> Optional[str]:
        """
        Shows a retry toplevel notification.

        This method shows a toplevel notification with a retry button and a message label.
        It also sets up the geometry of the widget and places the widgets within the grid.

        Args:
            message (str): The message to display in the message label
            title (str): The title of the toplevel widget
            on_click_callback (Optional[Callable[[str], None]]): The callback to execute when the cancel button is clicked

        Returns:
            Optional[str]: The result of the callback function

        Raises:
            Exception: If an error occurs while showing the toplevel notification
        """
        try:
            # Initialize and return the value of the 'retry' method from the 'ToplevelNotification' class
            return ToplevelNotification.retry(
                message=message,
                message_label={
                    "background": Constants.BLUE_GREY["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                on_click_callback=on_click_callback,
                retry_button={
                    "background": Constants.BLUE_GREY["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                title=title,
                title_label={
                    "background": Constants.BLUE_GREY["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.LARGE_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                toplevel={"background": Constants.BLUE_GREY["700"]},
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_show_retry' method from '{self.__class__.__name__}': {e}",
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None to the caller
            return None

    def on_request_show_retry_cancel(
        self,
        message: str,
        title: str,
        on_click_callback: Optional[Callable[[str], None]] = None,
    ) -> Optional[str]:
        """
        Shows a retry/cancel toplevel notification.

        This method shows a toplevel notification with a retry button and a cancel button and a message label.
        It also sets up the geometry of the widget and places the widgets within the grid.

        Args:
            message (str): The message to display in the message label
            title (str): The title of the toplevel widget
            on_click_callback (Optional[Callable[[str], None]]): The callback to execute when the cancel button is clicked

        Returns:
            Optional[str]: The result of the callback function

        Raises:
            Exception: If an error occurs while showing the toplevel notification
        """
        try:
            # Initialize and return the value of the 'retry_cancel' method from the 'ToplevelNotification' class
            return ToplevelNotification.retry_cancel(
                cancel_button={
                    "background": Constants.RED["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                message=message,
                message_label={
                    "background": Constants.BLUE_GREY["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                on_click_callback=on_click_callback,
                retry_button={
                    "background": Constants.YELLOW["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                title=title,
                title_label={
                    "background": Constants.BLUE_GREY["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.LARGE_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                toplevel={"background": Constants.BLUE_GREY["700"]},
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_show_retry_cancel' method from '{self.__class__.__name__}': {e}",
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None to the caller
            return None

    def on_request_show_yes_no(
        self,
        message: str,
        title: str,
        on_click_callback: Optional[Callable[[str], None]] = None,
    ) -> Optional[str]:
        """
        Shows a yes/no toplevel notification.

        This method shows a toplevel notification with a yes and no button and a message label.
        It also sets up the geometry of the widget and places the widgets within the grid.

        Args:
            message (str): The message to display in the message label
            title (str): The title of the toplevel widget
            on_click_callback (Optional[Callable[[str], None]]): The callback to execute when the cancel button is clicked

        Returns:
            Optional[str]: The result of the callback function

        Raises:
            Exception: If an error occurs while showing the toplevel notification
        """
        try:
            # Initialize and return the value of the 'yes_no' method from the 'ToplevelNotification' class
            return ToplevelNotification.yes_no(
                message=message,
                message_label={
                    "background": Constants.BLUE_GREY["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                no_button={
                    "background": Constants.RED["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                on_click_callback=on_click_callback,
                title=title,
                title_label={
                    "background": Constants.BLUE_GREY["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.LARGE_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                yes_button={
                    "background": Constants.GREEN["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                toplevel={"background": Constants.BLUE_GREY["700"]},
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_show_yes_no' method from '{self.__class__.__name__}': {e}",
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None to the caller
            return None

    def on_request_show_yes_no_cancel(
        self,
        message: str,
        title: str,
        on_click_callback: Optional[Callable[[str], None]] = None,
    ) -> Optional[str]:
        """
        Shows a yes/no/cancel toplevel notification.

        This method shows a toplevel notification with a yes, no, and cancel button and a message label.
        It also sets up the geometry of the widget and places the widgets within the grid.

        Args:
            message (str): The message to display in the message label
            title (str): The title of the toplevel widget
            on_click_callback (Optional[Callable[[str], None]]): The callback to execute when the cancel button is clicked

        Returns:
            Optional[str]: The result of the callback function

        Raises:
            Exception: If an error occurs while showing the toplevel notification
        """
        try:
            # Initialize and return the value of the 'yes_no_cancel' method from the 'ToplevelNotification' class
            return ToplevelNotification.yes_no_cancel(
                cancel_button={
                    "background": Constants.YELLOW["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                message=message,
                message_label={
                    "background": Constants.BLUE_GREY["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                no_button={
                    "background": Constants.RED["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                on_click_callback=on_click_callback,
                title=title,
                title_label={
                    "background": Constants.BLUE_GREY["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.LARGE_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                toplevel={"background": Constants.BLUE_GREY["700"]},
                yes_button={
                    "background": Constants.GREEN["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_show_yes_no_cancel' method from '{self.__class__.__name__}': {e}",
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return None to the caller
            return None

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
            # Create a dictionary of events and functions
            subscriptions: List[Dict[str, Any]] = self.collect_subscriptions()

            # Iterate over the events and functions in the subscriptions dictionary
            for subscription in subscriptions:
                # Store the UUID of the subscription in the subscriptions list
                self.subscriptions.append(
                    self.dispatcher.register(
                        event=subscription["event"],
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

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

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

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e
