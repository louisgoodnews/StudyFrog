"""
Author: lodego
Date: 2025-02-08
"""

import uuid

import tkinter

from typing import *

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.logger import Logger
from utils.object import ImmutableBaseObject


__all__: List[str] = [
    "NavigationItem",
    "NavigationItemFactory",
    "NavigationService",
]


class NavigationItem(ImmutableBaseObject):
    """
    A class representing a navigation item in the application.

    Attributes:
        id (int): The ID of the navigation item.
        source (str): The source of the navigation item.
        target (str): The target of the navigation item.
        uuid (str): The UUID of the navigation item.
    """

    def __init__(
        self,
        id: int,
        source: str,
        target: str,
        uuid: str,
    ) -> None:
        """
        Initializes a new instance of the NavigationItem class.

        Args:
            id (int): The ID of the navigation item.
            source (str): The source of the navigation item.
            target (str): The target of the navigation item.
            uuid (str): The UUID of the navigation item.

        Returns:
            None
        """
        # Call the parent class constructor
        super().__init__(
            id=id,
            source=source,
            target=target,
            uuid=uuid,
        )


class NavigationItemFactory:
    """
    A factory class used to create instances of NavigationItem class.

    Attributes:
        index (int): The index used to create unique IDs for navigation items.
        logger (Logger): The logger instance associated with the object.
    """

    index: int = 10000
    logger: Logger = Logger.get_logger(name="NavigationItemFactory")

    @classmethod
    def create_navigation_item(
        cls,
        source: str,
        target: str,
    ) -> Optional[NavigationItem]:
        """
        Creates and returns a new instance of NavigationItem class.

        Args:
            source (str): The source of the navigation item.
            target (str): The target of the navigation item.

        Returns:
            Optional[NavigationItem]: The created navigation item if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the navigation item.
        """
        try:
            # Attempt to create and return a new instance of NavigationItem
            navigation_item: NavigationItem = NavigationItem(
                id=cls.index,
                source=source,
                target=target,
                uuid=str(uuid.uuid4()),
            )

            # Increment the index for the next navigation item
            cls.index += 1

            # Return the created navigation item
            return navigation_item
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_navigation_item' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class NavigationService:
    """
    A service for managing navigation within the application.

    This service handles requests for backward and forward navigation by
    registering event handlers with the dispatcher. It listens for
    REQUEST_BACKWARD_NAVIGATION and REQUEST_FORWARD_NAVIGATION events
    and executes the corresponding navigation logic when these events
    are triggered.

    Attributes:
        dispatcher (Dispatcher): The dispatcher instance for managing events.
        logger (Logger): The logger instance for logging information.
    """

    def __init__(
        self,
        dispatcher: Dispatcher,
    ) -> None:
        """
        Initializes a new instance of NavigationService class.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.

        Returns:
            None
        """
        # Initialize a logger
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed dispatcher instance in an instance variable
        self.dispatcher: Dispatcher = dispatcher

        # Initialize a list of navigation items as an empty list and store it in an instance variable
        self.forward_stack: List[NavigationItem] = []

        # Initialize a list of navigation items as an empty list and store it in an instance variable
        self.navigation_stack: List[NavigationItem] = []

        # Register a function to be called when the REQUEST_BACKWARD_NAVIGATION event is dispatched
        self.dispatcher.register(
            event=Events.REQUEST_BACKWARD_NAVIGATION,
            function=self.on_request_backward_navigation,
            namespace=Constants.GLOBAL_NAMESPACE,
            persistent=True,
        )

        # Register a function to be called when the REQUEST_FORWARD_NAVIGATION event is dispatched
        self.dispatcher.register(
            event=Events.REQUEST_FORWARD_NAVIGATION,
            function=self.on_request_forward_navigation,
            namespace=Constants.GLOBAL_NAMESPACE,
            persistent=True,
        )

    def navigate(self) -> None:
        try:
            pass
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'navigate' method from '{self.__class__.__name__}': {e}"
            )

            # Raise the exception
            raise e

    def on_request_backward_navigation(
        self,
        **kwargs,
    ) -> None:
        try:
            # Remove the last navigation item from the list
            navigation_item: NavigationItem = self.navigation_stack.pop(
                self.navigation_stack[-1]
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_backward_navigation' method from '{self.__class__.__name__}': {e}"
            )

            # Raise the exception
            raise e

    def on_request_forward_navigation(
        self,
        source: str,
        target: str,
    ) -> None:
        try:
            # Create a new instance of NavigationItem
            navigation_item: NavigationItem = (
                NavigationItemFactory.create_navigation_item(
                    source=source,
                    target=target,
                )
            )

            # Append the navigation item to the list
            self.navigation_stack.append(navigation_item=navigation_item)
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_forward_navigation' method from '{self.__class__.__name__}': {e}"
            )

            # Raise the exception
            raise e
