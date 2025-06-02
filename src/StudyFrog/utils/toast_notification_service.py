"""
Author: lodego
Date: 2025-05-20
"""

import traceback

from tkinter.constants import *
from typing import *

from core.ui.notifications.notifications import ToplevelPositions, ToplevelToastNotification

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.object import ImmutableBaseObject


__all__: Final[List[str]] = ["ToastNotificationService"]


class ToastNotificationService(ImmutableBaseObject):
    """
    A class representing a toast notification service.

    This class provides a singleton instance for the toast notification service, which is accessible via the `ToastNotificationService` class.

    Attributes:
        None
    """

    # The shared instance of the toast notification service
    _shared_instance: Optional["ToastNotificationService"] = None

    def __new__(
        cls,
        dispatcher: Dispatcher,
    ) -> "ToastNotificationService":
        """
        Creates and returns a new instance of the ToastNotificationService class.

        If the instance does not exist, creates a new one by calling the parent class constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.

        Returns:
            ToastNotificationService: The created or existing instance of ToastNotificationService class.
        """
        if cls._shared_instance is None:
            cls._shared_instance = super(ToastNotificationService, cls).__new__(cls)
            cls._shared_instance.init(dispatcher=dispatcher)
        return cls._shared_instance

    def init(
        self,
        dispatcher: Dispatcher,
    ) -> None:
        """
        Initializes the toast notification service.

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
                "event": Events.REQUEST_SHOW_DEBUG_TOAST,
                "function": self.on_request_show_debug_toast,
                "namespace": Constants.GLOBAL_NAMESPACE,
                "persistent": True,
            },
            {
                "event": Events.REQUEST_SHOW_ERROR_TOAST,
                "function": self.on_request_show_error_toast,
                "namespace": Constants.GLOBAL_NAMESPACE,
                "persistent": True,
            },
            {
                "event": Events.REQUEST_SHOW_GENERIC_TOAST,
                "function": self.on_request_show_generic_toast,
                "namespace": Constants.GLOBAL_NAMESPACE,
                "persistent": True,
            },
            {
                "event": Events.REQUEST_SHOW_INFO_TOAST,
                "function": self.on_request_show_info_toast,
                "namespace": Constants.GLOBAL_NAMESPACE,
                "persistent": True,
            },
            {
                "event": Events.REQUEST_SHOW_SUCCESS_TOAST,
                "function": self.on_request_show_success_toast,
                "namespace": Constants.GLOBAL_NAMESPACE,
                "persistent": True,
            },
            {
                "event": Events.REQUEST_SHOW_WARNING_TOAST,
                "function": self.on_request_show_warning_toast,
                "namespace": Constants.GLOBAL_NAMESPACE,
                "persistent": True,
            },
        ]

        # Return the list to the caller
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

    def on_request_show_debug_toast(
        self,
        message: str,
        title: str,
        on_click_callback: Optional[Callable[[], None]] = None,
        position: Union[ToplevelPositions, str] = ToplevelPositions.TOP_LEFT,
    ) -> None:
        """
        Shows a debug toast notification.

        This method shows a toast notification with the given message and title.
        The ToplevelToastNotification object has no special styling.

        Args:
            message (str): The message to display.
            on_click_callback (Optional[Callable[[], None]]): The callback to execute when the toast notification is clicked.
            position (Union[ToplevelPositions, str]): The position of the toast notification. Defaults to ToplevelPositions.TOP_LEFT.
            title (str): The title of the toast notification.

        Returns:
            None

        Raises:
            Exception: If an error occurs while showing the toast notification.
        """
        try:
            # Initialize and show the toast notification
            ToplevelToastNotification(
                message=message,
                message_label={
                    "background": Constants.BLUE["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                on_click_callback=on_click_callback,
                position=position,
                title=title,
                title_label={
                    "background": Constants.BLUE["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.LARGE_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                toast={
                    "background": Constants.BLUE["700"],
                },
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_show_debug_toast' method from '{self.__class__.__name__}': {e}",
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def on_request_show_error_toast(
        self,
        message: str,
        title: str,
        on_click_callback: Optional[Callable[[], None]] = None,
        position: Union[ToplevelPositions, str] = ToplevelPositions.TOP_LEFT,
    ) -> None:
        """
        Shows an error toast notification.

        This method shows a toast notification with the given message and title.
        The ToplevelToastNotification object special styling to reflect an error.

        Args:
            message (str): The message to display.
            on_click_callback (Optional[Callable[[], None]]): The callback to execute when the toast notification is clicked.
            position (Union[ToplevelPositions, str]): The position of the toast notification. Defaults to ToplevelPositions.TOP_LEFT.
            title (str): The title of the toast notification.

        Returns:
            None

        Raises:
            Exception: If an error occurs while showing the toast notification.
        """
        try:
            # Initialize and show the toast notification
            ToplevelToastNotification(
                message=message,
                message_label={
                    "background": Constants.RED["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    "foreground": Constants.BLACK,
                },
                on_click_callback=on_click_callback,
                position=position,
                title=title,
                title_label={
                    "background": Constants.RED["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.LARGE_FONT_SIZE,
                    ),
                    "foreground": Constants.BLACK,
                },
                toast={
                    "background": Constants.RED["700"],
                },
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_show_error_toast' method from '{self.__class__.__name__}': {e}",
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def on_request_show_generic_toast(
        self,
        message: str,
        title: str,
        on_click_callback: Optional[Callable[[], None]] = None,
        position: Union[ToplevelPositions, str] = ToplevelPositions.TOP_LEFT,
    ) -> None:
        """
        Shows a generic toast notification.

        This method shows a toast notification with the given message and title.
        The ToplevelToastNotification object has no special styling.

        Args:
            message (str): The message to display.
            on_click_callback (Optional[Callable[[], None]]): The callback to execute when the toast notification is clicked.
            position (Union[ToplevelPositions, str]): The position of the toast notification. Defaults to ToplevelPositions.TOP_LEFT.
            title (str): The title of the toast notification.

        Returns:
            None

        Raises:
            Exception: If an error occurs while showing the toast notification.
        """
        try:
            # Initialize and show the toast notification
            ToplevelToastNotification(
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
                position=position,
                title=title,
                title_label={
                    "background": Constants.BLUE_GREY["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.LARGE_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                toast={
                    "background": Constants.BLUE_GREY["700"],
                },
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_show_generic_toast' method from '{self.__class__.__name__}': {e}",
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def on_request_show_info_toast(
        self,
        message: str,
        title: str,
        on_click_callback: Optional[Callable[[], None]] = None,
        position: Union[ToplevelPositions, str] = ToplevelPositions.TOP_LEFT,
    ) -> None:
        """
        Shows an info toast notification.

        This method shows a toast notification with the given message and title.
        The ToplevelToastNotification object special styling to reflect an info.

        Args:
            message (str): The message to display.
            on_click_callback (Optional[Callable[[], None]]): The callback to execute when the toast notification is clicked.
            position (Union[ToplevelPositions, str]): The position of the toast notification. Defaults to ToplevelPositions.TOP_LEFT.
            title (str): The title of the toast notification.

        Returns:
            None

        Raises:
            Exception: If an error occurs while showing the toast notification.
        """
        try:
            # Initialize and show the toast notification
            ToplevelToastNotification(
                message=message,
                message_label={
                    "background": Constants.GREY["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                on_click_callback=on_click_callback,
                position=position,
                title=title,
                title_label={
                    "background": Constants.GREY["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.LARGE_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                toast={
                    "background": Constants.GREY["700"],
                },
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_show_info_toast' method from '{self.__class__.__name__}': {e}",
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def on_request_show_success_toast(
        self,
        message: str,
        title: str,
        on_click_callback: Optional[Callable[[], None]] = None,
        position: Union[ToplevelPositions, str] = ToplevelPositions.TOP_LEFT,
    ) -> None:
        """
        Shows a success toast notification.

        This method shows a toast notification with the given message and title.
        The ToplevelToastNotification object special styling to reflect a success.

        Args:
            message (str): The message to display.
            on_click_callback (Optional[Callable[[], None]]): The callback to execute when the toast notification is clicked.
            position (Union[ToplevelPositions, str]): The position of the toast notification. Defaults to ToplevelPositions.TOP_LEFT.
            title (str): The title of the toast notification.

        Returns:
            None

        Raises:
            Exception: If an error occurs while showing the toast notification.
        """
        try:
            # Initialize and show the toast notification
            ToplevelToastNotification(
                message=message,
                message_label={
                    "background": Constants.GREEN["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                on_click_callback=on_click_callback,
                position=position,
                title=title,
                title_label={
                    "background": Constants.GREEN["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.LARGE_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                toast={
                    "background": Constants.GREEN["700"],
                },
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_show_success_toast' method from '{self.__class__.__name__}': {e}",
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def on_request_show_warning_toast(
        self,
        message: str,
        title: str,
        on_click_callback: Optional[Callable[[], None]] = None,
        position: Union[ToplevelPositions, str] = ToplevelPositions.TOP_LEFT,
    ) -> None:
        """
        Shows a warning toast notification.

        This method shows a toast notification with the given message and title.
        The ToplevelToastNotification object special styling to reflect a warning.

        Args:
            message (str): The message to display.
            on_click_callback (Optional[Callable[[], None]]): The callback to execute when the toast notification is clicked.
            position (Union[ToplevelPositions, str]): The position of the toast notification. Defaults to ToplevelPositions.TOP_LEFT.
            title (str): The title of the toast notification.

        Returns:
            None

        Raises:
            Exception: If an error occurs while showing the toast notification.
        """
        try:
            # Initialize and show the toast notification
            ToplevelToastNotification(
                message=message,
                message_label={
                    "background": Constants.ORANGE["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                on_click_callback=on_click_callback,
                position=position,
                title=title,
                title_label={
                    "background": Constants.ORANGE["700"],
                    "font": (
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.LARGE_FONT_SIZE,
                    ),
                    "foreground": Constants.WHITE,
                },
                toast={
                    "background": Constants.ORANGE["700"],
                },
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_show_warning_toast' method from '{self.__class__.__name__}': {e}",
            )

            # Log the traceback of the exception
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

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
