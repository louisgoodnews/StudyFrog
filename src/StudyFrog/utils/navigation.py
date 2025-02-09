"""
Author: lodego
Date: 2025-02-08
"""

import tkinter
import uuid

from tkinter.constants import *


from typing import *

from core.ui.ui_registry import UIRegistry

from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherEvent
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
        self.navigation_stack: List[NavigationItem] = []

    def navigate(
        self,
        source: str,
        target: str,
        **kwargs,
    ) -> None:
        """
        Navigates to the given target.

        Args:
            source (str): The source of the navigation item.
            target (str): The target of the navigation item.
            **kwargs: Additional keyword arguments to be passed to the event handler.

        Returns:
            None
        """
        try:
            # Attempt to create a new instance of NavigationItem
            navigation_item: NavigationItem = (
                NavigationItemFactory.create_navigation_item(
                    source=source,
                    target=target,
                )
            )

            if not navigation_item:
                # Log a warning message indicating that no navigation item was created
                self.logger.warning(
                    message=f"No navigation item was created for source '{source}' and target '{target}'."
                )

                # Return early
                return

            # Push to history stack
            self.navigation_stack.append(navigation_item)

            # Log an info message indicating navigation is being attempted
            self.logger.info(
                message=f"Attempting to navigate from '{source}' to '{target}'."
            )

            # Attempt to get the UI class that corresponds to the target
            ui_class: Optional[Type[tkinter.Misc]] = UIRegistry.get(name=target)

            # Check if a UI class was found
            if not ui_class:
                # Log a warning message indicating that no UI class was found
                self.logger.warning(
                    message=f"No UI class was found for target '{target}'."
                )

                # Return early
                return

            # Call the __init__ method of the UI class with the passed kwargs
            ui_class(**kwargs)

            # Grid the UI class widget
            ui_class.grid(
                column=0,
                row=0,
                sitcky=NSEW,
            )

            # Dispatch the "NAVIGATION_COMPLETED" event
            self.dispatcher.dispatch(
                event=Events.NAVIGATION_COMPLETED,
                namespace=Constants.GLOBAL_NAMESPACE,
            )
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
        """
        Handles backward navigation.

        Moves the current navigation item to the forward stack and navigates to the previous item.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            None
        """
        try:
            # Get the target from the kwargs
            target: Optional[Union[int, str]] = kwargs.get("target")

            if target is None:
                # Log a warning message indicating that no target was specified
                self.logger.warning("No target specified for backward navigation.")

                # Return early
                return

            if not isinstance(target, (int, str)):
                # Log a warning message indicating an invalid target type
                self.logger.warning(f"Invalid target type: {type(target)}")

                # Return early
                return

            # Attempt to find the navigation item in the navigation stack
            navigation_item: Optional[NavigationItem] = next(
                (
                    item
                    for item in self.navigation_stack
                    if item.id == target or item.uuid == target
                ),
                None,
            )

            if not navigation_item:
                # Log a warning message indicating that no navigation item was found
                self.logger.warning(
                    message=f"No navigation item found for target: {target}"
                )

                # Return early
                return

            # Log an info message indicating that we are navigating backward
            self.logger.info(
                message=f"Navigating backward to '{navigation_item.target}'."
            )

            # Navigate to the found navigation item
            self.navigate(
                source=navigation_item.source,
                target=navigation_item.target,
                **kwargs,
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
        **kwargs,
    ) -> None:
        """
        Handles forward navigation.

        Moves an item from the forward stack back to the navigation stack and navigates to it.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            None
        """
        try:
            if "source" not in kwargs or "target" not in kwargs:
                # Log a warning message indicating an invalid forward navigation request
                self.logger.warning(
                    "Invalid forward navigation request: 'source' or 'target' is missing."
                )

                # Return early
                return

            # Attempt to navigate to the target
            self.navigate(
                source=kwargs.pop("source"),
                target=kwargs.pop("target"),
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_forward_navigation' method from '{self.__class__.__name__}': {e}"
            )

            # Raise the exception
            raise e
