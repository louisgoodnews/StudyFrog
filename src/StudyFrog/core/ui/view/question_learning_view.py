"""
Author: lodego
Date: 2025-03-30
"""

import tkinter

from tkinter.constants import *
from typing import *

from core.question import ImmutableQuestion
from core.setting import SettingService

from core.ui.ui_builder import UIBuilder

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.logger import Logger


__all__: Final[List[str]] = ["QuestionLearningView"]


class QuestionLearningView(tkinter.Frame):
    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        namespace: str,
        question: ImmutableQuestion,
        setting_service: SettingService,
    ) -> None:
        """
        Initializes a new instance of the QuestionLearningView class.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.
            master (tkinter.Misc): The parent widget.
            namespace (str): The namespace.
            setting_service (SettingService): The setting service instance.
            question (ImmutableQuestion): The question instance.
        """

        # Configure the grid of the master widget's 0th column to weight 1.
        # This ensures that the frame will expand to fill the parent widget.
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the grid of the master widget's 0th row to weight 1.
        # This ensures that the frame will expand to fill the parent widget.
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create a logger instance
        self.logger: Final[Logger] = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed dispatcher instance in an instance variable
        self.dispatcher: Dispatcher = dispatcher

        # Store the passed namespace in an instance variable
        self.namespace: str = namespace

        # Store the passed question instance in an instance variable
        self.question: ImmutableQuestion = question

        # Store the passed setting service instance in an instance variable
        self.setting_service: SettingService = setting_service

        # Initialize a list to store subscription UUIDs
        # The subscription UUIDs are used to keep track of the subscriptions to events
        self.subscriptions: List[str] = []

        # Call the parent class constructor
        super().__init__(
            master=master,
            name="question_learning_view",
        )

        # Style the frame
        self.configure(background=Constants.BLUE_GREY["700"])

        # Configure the grid of the question learning form widget
        # This method is responsible for configuring the grid layout of the frame
        self.configure_grid()

        # Create the widgets of the question learning form
        self.create_widgets()

        # Place the question learning form widget in the parent widget
        # This method is responsible for placing the frame in the parent widget
        self.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

    def clear(self) -> None:
        """
        Clears the content of the question learning view widget.

        This method clears the content of the question learning view widget by destroying
        all its children widgets.

        Returns:
            None
        """

        # Attempt to get a list of all children widgets
        children: Optional[List[tkinter.Misc]] = self.winfo_children()

        # Check if there are any children
        if not children:
            # Return early if there are no children
            return

        # Iterate over the children
        for child in children:
            # Destroy the child widget
            child.destroy()

    def collect_subscriptions(self) -> List[Dict[str, Any]]:
        """
        Collects and returns a list of subscriptions.

        This method should be implemented by subclasses to provide
        a list containing event subscriptions. Each subscription
        is associated with specific events and their corresponding
        handlers.

        Returns:
            List[Dict[str, Any]]: A list representing the subscriptions for events.
        """

        # Collect the subscriptions
        subscriptions: List[Dict[str, Any]] = []

        # Return the subscriptions
        return subscriptions

    def configure_grid(self) -> None:
        """
        Configures the grid of the question learning view widget.

        This method configures the grid of the question learning view widget by setting
        the weights of the columns and rows.

        The 0th column is configured to weight 1, which means that the column will
        stretch when the window is resized.

        The 0th row is configured to weight 0, which means that the row will not
        stretch when the window is resized.

        The 1st row is configured to weight 1, which means that the row will
        stretch when the window is resized.

        The 2nd row is configured to weight 0, which means that the row will not
        stretch when the window is resized.

        Returns:
            None
        """

        # Configure the question learning view widget's 0th column to weight 1
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the question learning view widget's 0th row to weight 0
        self.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the question learning view widget's 1st row to weight 1
        self.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Configure the question learning view widget's 2nd row to weight 0
        self.grid_rowconfigure(
            index=2,
            weight=0,
        )

    def create_bottom_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        pass

    def create_center_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:

        # Configure the grid of the master widget's 0th column to weight 1.
        # This ensures that the frame will expand to fill the parent widget.
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the grid of the master widget's 0th row to weight 1.
        # This ensures that the frame will expand to fill the parent widget.
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create the scrolled frame widgets
        scrolled_frame: Optional[Dict[str, Any]] = UIBuilder.get_scrolled_frame(
            master=master
        )

        if not scrolled_frame:
            # Log a warning message
            self.logger.warning(
                message=f"Failed to create scrolled frame widgets in '{self.__class__.__name__}'. This is likely a bug."
            )

            # Return early
            return

        # Style the scrolled frame's "Canvas" widget
        scrolled_frame["canvas"].configure(background=Constants.BLUE_GREY["700"])

        # Style the scrolled frame's "Frame" widget
        scrolled_frame["frame"].configure(background=Constants.BLUE_GREY["700"])

        # Style the scrolled frame's "Root" widget
        scrolled_frame["root"].configure(background=Constants.BLUE_GREY["700"])

        # Place the scrolled frame's "root" widget within the master widget
        scrolled_frame["frame"].grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create the scrolled frame widgets
        self.create_scrolled_frame_widgets(master=scrolled_frame["frame"])

    def create_scrolled_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:

        # Configure the grid of the master widget's 0th column to weight 1.
        # This ensures that the frame will expand to fill the parent widget.
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the grid of the master widget's 0th row to weight 1.
        # This ensures that the frame will expand to fill the parent widget.
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

    def create_top_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:

        # Configure the grid of the master widget's 0th column to weight 1.
        # This ensures that the frame will expand to fill the parent widget.
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the grid of the master widget's 0th row to weight 1.
        # This ensures that the frame will expand to fill the parent widget.
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

    def create_widgets(self) -> None:
        """
        Creates and configures the main widgets of the question learning view widget.

        This method initializes the top, center, and bottom frames within the
        question learning view widget, setting their layout configuration.
        """

        # Create the top frame widget
        top_frame: Optional[tkinter.Frame] = tkinter.Frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        if not top_frame:
            # Log a warning message
            self.logger.warning(
                f"Failed to create top frame widget in {self.__class__.__name__}. This is likely a bug."
            )

            # Return early if the top frame widget could not be created
            return

        # Configure the grid of the top frame widget
        # The first column should weight 1 to allow the frame to expand horizontally
        top_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the grid of the top frame widget
        # The first row should weight 1 to allow the frame to expand vertically
        top_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Place the top frame widget within the question learning view widget
        top_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create the center frame widget
        center_frame: Optional[tkinter.Frame] = tkinter.Frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        if not center_frame:
            # Log a warning message
            self.logger.warning(
                f"Failed to create center frame widget in {self.__class__.__name__}. This is likely a bug."
            )

            # Return early if the center frame widget could not be created
            return

        # Configure the grid of the center frame widget
        # The first column should weight 1 to allow the frame to expand horizontally
        center_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the grid of the center frame widget
        # The first row should weight 1 to allow the frame to expand vertically
        center_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Place the center frame widget within the question learning view widget
        center_frame.grid(
            column=0,
            row=1,
            sticky=NSEW,
        )

        # Create the bottom frame widget
        bottom_frame: Optional[tkinter.Frame] = tkinter.Frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        if not bottom_frame:
            # Log a warning message
            self.logger.warning(
                f"Failed to create bottom frame widget in {self.__class__.__name__}. This is likely a bug."
            )

            # Return early if the bottom frame widget could not be created
            return

        # Configure the grid of the bottom frame widget
        # The first column should weight 1 to allow the frame to expand horizontally
        bottom_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the grid of the bottom frame widget
        # The first row should weight 1 to allow the frame to expand vertically
        bottom_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Place the bottom frame widget within the question learning view widget
        bottom_frame.grid(
            column=0,
            row=2,
            sticky=NSEW,
        )

        # Create the top frame widgets
        self.create_top_frame_widgets(master=top_frame)

        # Create the center frame widgets
        self.create_center_frame_widgets(master=center_frame)

        # Create the bottom frame widgets
        self.create_bottom_frame_widgets(master=bottom_frame)

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
                message=f"Caught an exception while attempting to run 'subscribe_to_events' method from '{self.__class__.__name__}': {e}"
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
                message=f"Caught an exception while attempting to run 'unsubscribe_from_events' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e
