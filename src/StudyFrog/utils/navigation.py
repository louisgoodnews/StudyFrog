"""
Author: lodego
Date: 2025-02-08
"""

import tkinter

from tkinter.constants import *


from typing import *

from core.ui.ui_registry import UIRegistry

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous
from utils.object import ImmutableBaseObject


__all__: Final[List[str]] = [
    "NavigationHistoryItem",
    "NavigationHistoryItemFactory",
    "NavigationHistoryService",
]


class NavigationHistoryItem(ImmutableBaseObject):
    """
    A class representing a navigation  history item in the application.

    Attributes:
        id (int): The ID of the navigation  history item.
        source (str): The source of the navigation  history item.
        target (str): The target of the navigation  history item.
        uuid (str): The UUID of the navigation  history item.
    """

    def __init__(
        self,
        id: int,
        source: str,
        target: str,
        uuid: str,
    ) -> None:
        """
        Initializes a new instance of the NavigationHistoryItem class.

        Args:
            id (int): The ID of the navigation  history item.
            source (str): The source of the navigation  history item.
            target (str): The target of the navigation  history item.
            uuid (str): The UUID of the navigation  history item.

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


class NavigationHistoryItemFactory:
    """
    A factory class used to create instances of NavigationHistoryItem class.

    Attributes:
        index (int): The index used to create unique IDs for navigation  history items.
        logger (Logger): The logger instance associated with the object.
    """

    index: int = Constants.get_base_id()
    logger: Logger = Logger.get_logger(name="NavigationHistoryItemFactory")

    @classmethod
    def create_navigation_item(
        cls,
        source: str,
        target: str,
    ) -> Optional[NavigationHistoryItem]:
        """
        Creates and returns a new instance of NavigationHistoryItem class.

        Args:
            source (str): The source of the navigation  history item.
            target (str): The target of the navigation  history item.

        Returns:
            Optional[NavigationHistoryItem]: The created navigation  history item if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the navigation  history item.
        """
        try:
            # Attempt to create and return a new instance of NavigationHistoryItem
            navigation_item: NavigationHistoryItem = NavigationHistoryItem(
                id=cls.index,
                source=source,
                target=target,
                uuid=Miscellaneous.get_uuid(),
            )

            # Increment the index for the next navigation  history item
            cls.index += 1

            # Return the created navigation  history item
            return navigation_item
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_navigation_item' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None


class NavigationHistoryService:
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
        Initializes a new instance of NavigationHistoryService class.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.

        Returns:
            None
        """
        # Initialize a logger
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed dispatcher instance in an instance variable
        self.dispatcher: Dispatcher = dispatcher

        # Initialize a list of navigation  history items as an empty list and store it in an instance variable
        self.navigation_stack: List[NavigationHistoryItem] = []

    def navigate(
        self,
        source: str,
        target: str,
        **kwargs,
    ) -> Optional[NavigationHistoryItem]:
        """
        Navigates to the given target.

        Args:
            source (str): The source of the navigation  history item.
            target (str): The target of the navigation  history item.
            **kwargs: Additional keyword arguments to be passed to the event handler.

        Returns:
            Optional[NavigationHistoryItem]: The created navigation  history item if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while creating the navigation  history item.
        """
        try:
            # Attempt to create a new instance of NavigationHistoryItem
            navigation_item: NavigationHistoryItem = (
                NavigationHistoryItemFactory.create_navigation_item(
                    source=source,
                    target=target,
                )
            )

            if not navigation_item:
                # Log a warning message indicating that no navigation  history item was created
                self.logger.warning(
                    message=f"No navigation  history item was created for source '{source}' and target '{target}'."
                )

                # Return early
                return

            # Push to history stack
            self.navigation_stack.append(navigation_item)

            # Return the navigation  history item
            return navigation_item
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
    ) -> Optional[NavigationHistoryItem]:
        """
        Handles backward navigation.

        Moves the current navigation  history item to the forward stack and navigates to the previous item.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            Optional[NavigationHistoryItem]: The navigation  history item that was navigated to. Otherwise, None.

        Raises:
            Exception: If an exception occurs while navigating backward.
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

            # Attempt to find the navigation  history item in the navigation stack
            navigation_item: Optional[NavigationHistoryItem] = next(
                (
                    item
                    for item in self.navigation_stack
                    if item.id == target or item.uuid == target
                ),
                None,
            )

            if not navigation_item:
                # Log a warning message indicating that no navigation  history item was found
                self.logger.warning(
                    message=f"No navigation  history item found for target: {target}"
                )

                # Return early
                return

            # Log an info message indicating that we are navigating backward
            self.logger.info(
                message=f"Navigating backward to '{navigation_item.target}'."
            )

            # Navigate to the found navigation  history item
            return self.navigate(
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
    ) -> Optional[NavigationHistoryItem]:
        """
        Handles forward navigation.

        Moves an item from the forward stack back to the navigation stack and navigates to it.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            Optional[NavigationHistoryItem]: The navigation  history item that was navigated to. Otherwise, None.

        Raises:
            Exception: If an exception occurs while navigating forward.
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
            return self.navigate(
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
