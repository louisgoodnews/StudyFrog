"""
Author: lodego
Date: 2025-02-11
"""

import tkinter

from tkinter.constants import *

from typing import *

from core.answer import ImmutableAnswer
from core.flashcard import ImmutableFlashcard
from core.note import ImmutableNote
from core.question import ImmutableQuestion
from core.setting import SettingService
from core.stack import ImmutableStack

from core.ui.ui_builder import UIBuilder

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous
from utils.navigation import NavigationHistoryItem, NavigationHistoryService
from utils.unified import UnifiedObjectManager


__all__: List[str] = ["EditUI"]


class EditUI(tkinter.Frame):
    """
    A class representing the edit menu user interface (UI) of the application.

    This class is responsible for initializing and configuring the layout of the
    edit menu UI, including setting up the main frames and populating them with
    respective widgets. It extends the tkinter.Frame class and utilizes various
    utility classes for managing navigation, logging, and other functionalities.

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
        navigation_item: NavigationHistoryItem,
        navigation_service: NavigationHistoryService,
        setting_service: SettingService,
        unified_manager: UnifiedObjectManager,
        answer: Optional[ImmutableAnswer] = None,
        flashcard: Optional[ImmutableFlashcard] = None,
        note: Optional[ImmutableNote] = None,
        question: Optional[ImmutableQuestion] = None,
        stack: Optional[ImmutableStack] = None,
    ) -> None:
        """
        Initializes a new instance of the EditUI class.

        Args:
            answer (Optional[ImmutableAnswer]): The answer to edit.
            dispatcher (Dispatcher): The dispatcher instance.
            flashcard (Optional[ImmutableFlashcard]): The flashcard to edit.
            master (tkinter.Misc): The parent widget.
            navigation_item (NavigationHistoryItem): The navigation history item instance.
            navigation_service (NavigationHistoryService): The navigation history service instance.
            note (Optional[ImmutableNote]): The note to edit.
            question (Optional[ImmutableQuestion]): The question to edit.
            setting_service (SettingService): The setting service instance.
            stack (Optional[ImmutableStack]): The stack to edit.
            unified_manager (UnifiedObjectManager): The unified manager instance.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            master=master,
            name="create_ui",
        )

        # Initialize the logger instance
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed answer instance in an instance variable
        self.answer: Optional[ImmutableAnswer] = answer

        # Store the passed flashcard instance in an instance variable
        self.flashcard: Optional[ImmutableFlashcard] = flashcard

        # Store the passed dispatcher instance in an instance variable
        self.dispatcher: Dispatcher = dispatcher

        # Initialize the fields instance variable dictionary as an empty dictionary
        self.fields: Dict[str, Any] = {}

        # Store the passed navigation item instance in an instance variable
        self.navigation_item: NavigationHistoryItem = navigation_item

        # Store the passed navigation service instance in an instance variable
        self.navigation_service: NavigationHistoryService = navigation_service

        # Store the passed note instance in an instance variable
        self.note: Optional[ImmutableNote] = note

        # Store the passed question instance in an instance variable
        self.question: Optional[ImmutableQuestion] = question

        # Store the passed setting service instance in an instance variable
        self.setting_service: SettingService = setting_service

        # Store the passed stack instance in an instance variable
        self.stack: Optional[ImmutableStack] = stack

        # Store the passed unified manager instance in an instance variable
        self.unified_manager: UnifiedObjectManager = unified_manager

        # Configure the DasboardUI's background to be grey
        self.configure(background=Constants.BLUE_GREY["700"])

        # Subscribe to events relevant for this class
        self.subscribe_to_events()

        # Configure the grid
        self.configure_grid()

        # Edit the widgets
        self.create_widgets()

        # Grid the edit menu widget in its master
        self.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

    def configure_grid(self) -> None:
        """
        Configures the grid of the edit menu widget.

        This method configures the grid of the edit menu widget by setting the
        weights of the columns and rows.

        Returns:
            None
        """

        # Configure the edit menu widget's 1st column to weight 1.
        # This means that the 1st column will stretch when the window is resized.
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the edit menu widget's 1st and 3rd row to weight 0.
        # This means that the 1st and 3rd row will not stretch when the window is resized.
        self.grid_rowconfigure(
            index=(
                0,
                2,
            ),
            weight=0,
        )

        # Configure the edit menu widget's 2nd row to weight 1.
        # This means that the 2nd row will stretch when the window is resized.
        self.grid_rowconfigure(
            index=1,
            weight=1,
        )

    def create_widgets(self) -> None:
        """
        Edits and configures the main frames of the edit menu UI.

        This method initializes the top, center, and bottom frames within the
        edit menu UI, setting their layout configuration and invoking methods
        to populate each frame with its respective widgets.

        Args:
            None

        Returns:
            None
        """

        # Create the "Top Frame" frame widget
        top_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        # Configure the "Top Frame" frame widget's 1st column to weight 1
        top_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the "TOp Frame" frame widget's 1st row to weight 1
        top_frame.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Place the "Top Frame" frame widget in the main window
        top_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create the "Center Frame" frame widget
        center_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        # Configure the "Center Frame" frame widget's 1st column to weight 1
        center_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the "Center Frame" frame widget's 1st row to weight 1
        center_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Place the "Center Frame" frame widget in the main window
        center_frame.grid(
            column=0,
            row=1,
            sticky=NSEW,
        )

        # Create the "Bottom Frame" frame widget
        bottom_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        # Configure the "Bottom Frame" frame widget's 1st column to weight 1
        bottom_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the "Bottom Frame" frame widget's 1st row to weight 1
        bottom_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Place the "Bottom Frame" frame widget in the main window
        bottom_frame.grid(
            column=0,
            row=2,
            sticky=NSEW,
        )

        # Edit the "Bottom Frame" frame widgets
        self.create_bottom_frame_widgets(master=bottom_frame)

        # Edit the "Center Frame" frame widgets
        self.create_center_frame_widgets(master=center_frame)

        # Edit the "Top Frame" frame widgets
        self.create_top_frame_widgets(master=top_frame)

    def create_bottom_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Edits and configures the main widgets of the bottom frame.

        This method initializes the main widgets of the bottom frame within the
        edit menu UI, setting their layout configuration.

        Args:
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """

        # Configure the master widget's 1st column to weight 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the master widget's 2nd and 3rd column to weight 0
        master.grid_columnconfigure(
            index=(
                1,
                2,
            ),
            weight=0,
        )

        # Configure the master widget's 1st row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create the "Cancel button" button widget
        cancel_button: tkinter.Button = UIBuilder.get_button(
            background=Constants.BLUE_GREY["700"],
            command=self.on_cancel_button_click,
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=master,
            relief=FLAT,
            text="Cancel",
            width=10,
        )

        # Place the "Cancel button" button widget in the master frame widget
        cancel_button.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
        )

        # Create the "Save button" button widget
        save_button: tkinter.Button = UIBuilder.get_button(
            background=Constants.BLUE_GREY["700"],
            command=self.on_save_button_click,
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=master,
            relief=FLAT,
            text="Save",
            width=10,
        )

        # Place the "Save button" button widget in the master frame widget
        save_button.grid(
            column=2,
            padx=5,
            pady=5,
            row=0,
        )

    def create_center_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Edits and configures the main widgets of the center frame.

        This method initializes the main widgets of the center frame within the
        edit menu UI, setting their layout configuration.

        Args:
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """

        # Configure the master widget's 1st column to weight 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the master widget's 2nd column to weight 0
        master.grid_columnconfigure(
            index=1,
            weight=0,
        )

        # Configure the master widget's 1st row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create the "Left frame" frame widget
        left_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=master,
        )

        # Configure the "Left frame" frame widget's 1st column to weight 1
        left_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the "Left frame" frame widget's 1st and 2nd row to weight 1
        left_frame.grid_rowconfigure(
            index=(
                0,
                1,
            ),
            weight=1,
        )

        # Place the "Left frame" frame widget within the master frame widget
        left_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create the "Right frame" frame widget
        right_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=master,
        )

        # Place the "Right frame" frame widget within the master frame widget
        right_frame.grid(
            column=1,
            row=0,
            sticky=NSEW,
        )

        # Create the "Right frame" widgets
        self.create_right_frame_widgets(master=right_frame)

        # Create the "Left frame" widgets
        self.create_left_frame_widgets(master=left_frame)

    def create_top_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Edits and configures the main widgets of the top frame.

        This method initializes the main widgets of the top frame within the
        edit menu UI, setting their layout configuration.

        Args:
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """

        # Configure the master widget's 1st column to weight 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the master widget's 1st row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        if self.answer:
            pass
        elif self.flashcard:
            pass
        elif self.note:
            pass
        elif self.question:
            pass
        elif self.stack:
            pass

    def create_right_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Edits and configures the main widgets of the right frame.

        This method initializes the main widgets of the right frame within the
        edit menu UI, setting their layout configuration.

        Args:
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """
        pass

    def create_left_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Edits and configures the main widgets of the left frame.

        This method initializes the main widgets of the left frame within the
        edit menu UI, setting their layout configuration.

        Args:
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """
        pass

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

            # Call the parent class's destroy method
            super().destroy()
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'destroy' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def on_answer_updated(
        self,
        answer: ImmutableAnswer,
    ) -> None:
        try:
            # Update the answer instance variable to the passed (updated) answer
            self.answer = answer
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_answer_updated' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def on_cancel_button_click(self) -> None:
        try:
            self.dispatcher.dispatch(
                direction="backwards",
                event=Events.REQUEST_VALIDATE_NAVIGATION,
                namespace=Constants.GLOBAL_NAMESPACE,
                soure="edit_ui",
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_cancel_button_click' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def on_flashcard_updated(
        self,
        flashcard: ImmutableFlashcard,
    ) -> None:
        try:
            # Update the flashcard instance variable to the passed (updated) flashcard
            self.flashcard = flashcard
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_flashcard_updated' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def on_note_updated(
        self,
        note: ImmutableNote,
    ) -> None:
        try:
            # Update the note instance variable to the passed (updated) note
            self.note = note
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_note_updated' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def on_question_updated(
        self,
        question: ImmutableQuestion,
    ) -> None:
        try:
            # Update the question instance variable to the passed (updated) question
            self.question = question
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_question_updated' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def on_save_button_click(self) -> None:
        try:
            pass
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_save_button_click' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def on_stack_updated(
        self,
        stack: ImmutableStack,
    ) -> None:
        try:
            # Update the stack instance variable to the passed (updated) stack
            self.stack = stack
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_stack_updated' method from '{self.__class__.__name__}': {e}",
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
            subscriptions: Dict[Any, Dict[str, Any]] = {
                Events.ANSWER_UPDATED: {
                    "function": self.on_answer_updated,
                    "namespace": Constants.GLOBAL_NAMESPACE,
                    "persistent": True,
                },
                Events.FLASHCARD_UPDATED: {
                    "function": self.on_flashcard_updated,
                    "namespace": Constants.GLOBAL_NAMESPACE,
                    "persistent": True,
                },
                Events.NOTE_UPDATED: {
                    "function": self.on_note_updated,
                    "namespace": Constants.GLOBAL_NAMESPACE,
                    "persistent": True,
                },
                Events.QUESTION_UPDATED: {
                    "function": self.on_question_updated,
                    "namespace": Constants.GLOBAL_NAMESPACE,
                    "persistent": True,
                },
                Events.STACK_UPDATED: {
                    "function": self.on_stack_updated,
                    "namespace": Constants.GLOBAL_NAMESPACE,
                    "persistent": True,
                },
            }

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
