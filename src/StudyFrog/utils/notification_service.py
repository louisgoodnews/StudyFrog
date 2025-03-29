"""
Author: lodego
Date: 2025-03-26
"""

from typing import *

from core.ui.ui_builder import UIBuilder

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.logger import Logger


__all__: Final[List[str]] = ["NotificationService"]


class NotificationService:
    """
    A singleton class that provides functionality for showing UI notifications to the user.

    The class provides methods to subscribe to a dispatcher event, unsubscribe from a dispatcher event, and display a notification to the user.

    Attributes:
        _shared_instance (Optional[NotificationService]): The shared instance of the service.
        logger (Logger): The logger instance associated with the service.
        dispatcher (Dispatcher): The dispatcher instance used to dispatch notifications.
        subscriptions (List[str]): The list of subscriptions to track.
    """
    _shared_instance: Optional["NotificationService"] = None

    def __new__(
        cls,
        dispatcher: Dispatcher,
    ) -> "NotificationService":
        """
        Creates and returns a new instance of the NotificationService class.

        If the instance does not exist, creates a new one by calling the parent class constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Args:
            dispatcher (Dispatcher): The dispatcher instance to be used by the service.

        Returns:
            NotificationService: The created or existing instance of NotificationService class.
        """
        if cls._shared_instance is None:
            cls._shared_instance = super().__new__(cls)
            cls._shared_instance.init(dispatcher=dispatcher)
        return cls._shared_instance

    def init(
        self,
        dispatcher: Dispatcher,
    ) -> None:
        """
        Initializes the NotificationService instance.

        Args:
            dispatcher (Dispatcher): The dispatcher instance to be used by the service.

        Returns:
            None
        """
        # Initialize the logger instance for NotificationService
        self.logger: Final[Logger] = Logger.get_logger(name=self.__class__.__name__)

        # Store the dispatcher instance
        self.dispatcher: Final[Dispatcher] = dispatcher

        # Initialize an empty list to keep track of subscriptions
        self.subscriptions: Final[List[str]] = []
