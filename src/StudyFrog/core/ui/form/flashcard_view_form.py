"""
Author: lodego
Date 2025-03-03
"""

import tkinter

from tkinter.constants import *

from tkinter import ttk

from typing import *

from core.difficulty import ImmutableDifficulty
from core.flashcard import ImmutableFlashcard, MutableFlashcard
from core.note import ImmutableNote
from core.priority import ImmutablePriority
from core.question import ImmutableQuestion

from core.ui.ui_builder import UIBuilder

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous
from utils.unified import UnifiedObjectManager


__all__: Final[List[str]] = ["FlashcardViewForm"]


class FlashcardViewForm(tkinter.Frame):
    """
    Represents the stack view form widget of the application.

    This class is responsible for initializing and configuring the layout of the
    stack view form widget, including setting up the main frames and populating them
    with respective widgets.

    Attributes:
        dispatcher (Dispatcher): The dispatcher instance.
        logger (Logger): The logger instance.
        flashcard (Union[ImmutableFlashcard, MutableFlashcard]): The flashcard instance.
        unified_manager (UnifiedObjectManager): The unified manager instance.
    """

    def __init__(
        self,
        dispatcher: Dispatcher,
        flashcard: Union[ImmutableFlashcard, MutableFlashcard],
        master: tkinter.Misc,
        unified_manager: UnifiedObjectManager,
    ) -> None:
        """
        Initializes a new instance of the FlashcardViewForm class.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.
            flashcard (Union[ImmutableFlashcard, MutableFlashcard]): The flashcard instance.
            master (tkinter.Misc): The parent widget.
            unified_manager (UnifiedObjectManager): The unified manager instance.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(master=master)

        # Create an instance variable for the logger
        self.logger: Final[Logger] = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed dispatcher instance in an instance variable
        self.dispatcher: Dispatcher = dispatcher

        # Store the passed flashcard instance in an instance variable
        self.flashcard: Union[ImmutableFlashcard, MutableFlashcard] = flashcard

        # Initialize the timestamp datetime instance variable as None
        self.timestamp: Optional[datetime] = None

        # Store the passed unified manager instance in an instance variable
        self.unified_manager: UnifiedObjectManager = unified_manager

        # Set the background color of the stack view form widget
        self.configure(background=Constants.BLUE_GREY["700"])

        # Subscribe to events relevant for this class
        self.subscribe_to_events()

        # Configure the grid of the stack view form widget
        self.configure_grid()

        # Create the widgets of the stack view form
        self.create_widgets()

    def configure_grid(self) -> None:
        """
        Configures the grid of the stack view form widget.

        This method configures the grid of the stack view form widget by setting
        the weights of the columns and rows.

        Args:
            None

        Returns:
            None
        """

        # Configure the stack view form widget's 0th column to weight 1.
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the stack view form widget's 0th row to weight 0.
        self.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the stack view form widget's 1st row to weight 1.
        self.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Configure the stack view form widget's 2nd row to weight 1.
        self.grid_rowconfigure(
            index=2,
            weight=1,
        )

    def create_widgets(self):
        """
        Creates the widgets of the stack view form.

        This method initializes the main widgets of the stack view form, setting
        their layout configuration.

        Args:
            None

        Returns:
            None
        """

        # Create the top frame
        top_frame: tkinter.Frame = UIBuilder.get_frame(master=self)

        # Configure the top frame
        top_frame.configure(background=Constants.BLUE_GREY["700"])

        # Configure the top frame widget's 0th column to weight 1
        top_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the top frame widget's 0th row to weight 1
        top_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Place the top frame widget within the stack view form
        top_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create the center frame
        center_frame: tkinter.Frame = UIBuilder.get_frame(master=self)

        # Configure the center frame
        center_frame.configure(background=Constants.BLUE_GREY["700"])

        # Configure the center frame
        center_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the center frame widget's 1st row to weight 1
        center_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Place the center frame widget within the stack view form
        center_frame.grid(
            column=0,
            row=1,
            sticky=NSEW,
        )

        # Create the bottom frame
        bottom_frame: tkinter.Frame = UIBuilder.get_frame(master=self)

        # Configure the bottom frame
        bottom_frame.configure(background=Constants.BLUE_GREY["700"])

        # Configure the bottom frame widget's 0th column to weight 1
        bottom_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the bottom frame widget's 0th row to weight 1
        bottom_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Place the bottom frame widget within the stack view form
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

    def create_top_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Creates and configures the main widgets of the top frame.

        This method initializes the main widgets of the top frame within the
        flashcard view form, setting their layout configuration.

        Args:
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """

        # Configure the master widget's 0th column to weight 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the master widget's 0th row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create the single line text field for the stack name
        self.front_text_field: Optional[Dict[str, Any]] = (
            UIBuilder.get_scrolled_text_field(
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                height=5,
                label="Front Text*: ",
                master=master,
            )
        )

        # Style the name field's button widget
        self.front_text_field["button"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Bind the name field to the on_front_text_field_changed function
        self.front_text_field["scrolled_text_field"]["text"].bind(
            func=lambda event: self.on_front_text_field_changed(),
            sequence="<KeyRelease>",
        )

        # Style the name field's label widget
        self.front_text_field["label"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
        )

        # Style the name field's root widget
        self.front_text_field["root"].configure(background=Constants.BLUE_GREY["700"])

        # Set the name field's value to the flashcard's front text
        self.front_text_field["setter"](value=self.flashcard.front_text)

        # Configure the name field
        self.front_text_field["label"].configure(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Place the name field in the top frame
        self.front_text_field["root"].grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create a separator widget to divide the flashcard view form widget
        separator: ttk.Separator = UIBuilder.get_separator(
            master=master,
            orient=HORIZONTAL,
        )

        # Place the separator in the grid
        separator.grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
            sticky=EW,
        )

    def create_center_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Creates and configures the main widgets of the center frame.

        This method initializes the main widgets of the center frame within the
        stack view form, setting their layout configuration.

        Args:
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """

        # Configure the master widget's 0th column to weight 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the master widget's 1st column to weight 0
        master.grid_columnconfigure(
            index=1,
            weight=0,
        )

        # Configure the master widget's 2nd column to weight 0
        master.grid_columnconfigure(
            index=2,
            weight=0,
        )

        # Configure the master widget's 0th row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create the left frame
        left_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=master,
        )

        # Configure the left frame widget's 0th column to weight 1
        left_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the left frame widget's 0th row to weight 1
        left_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Configure the left frame widget's 1st row to weight 1
        left_frame.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Configure the left frame widget's 2nd row to weight 1
        left_frame.grid_rowconfigure(
            index=2,
            weight=1,
        )

        # Place the left frame widget within the center frame
        left_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create the separator widget
        separator: ttk.Separator = UIBuilder.get_separator(
            master=master,
            orient=VERTICAL,
        )

        # Place the separator within the center frame
        separator.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=NS,
        )

        # Create the right frame
        right_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=master,
        )

        # Place the right frame widget within the center frame
        right_frame.grid(
            column=2,
            row=0,
            sticky=NSEW,
        )

        # Create the left frame widgets
        self.create_left_frame_widgets(master=left_frame)

        # Create the right frame widgets
        self.create_right_frame_widgets(master=right_frame)

    def create_left_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        # Configure the master widget's 0th column to weight 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the master widget's 0th row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Configure the master widget's 1st row to weight 1
        master.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Configure the master widget's 2nd row to weight 1
        master.grid_rowconfigure(
            index=2,
            weight=1,
        )

        # Create the tabbed view widget
        tabbed_view: Optional[Dict[str, Any]] = UIBuilder.get_tabbed_view(master=master)

        # Configure the tabbed view widget's root frame
        tabbed_view["root"].configure(background=Constants.BLUE_GREY["700"])

        # Configure the tabbed view widget's top frame
        tabbed_view["top_frame"].configure(background=Constants.BLUE_GREY["700"])

        # Place the tabbed view widget within the center frame
        tabbed_view["root"].grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create the Core attributes frame
        core_attributes_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=tabbed_view["center_frame"],
        )

        # Configure the Core attributes frame's 0th column to weight 1
        core_attributes_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the Core attributes frame's 0th row to weight 1
        core_attributes_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Add the Core attributes frame to the tabbed view
        tabbed_view["adder"](
            label="Core Attributes",
            widget=core_attributes_frame,
        )

        # Style the Core attributes button
        tabbed_view["core_attributes_button"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Create the description field
        self.back_text_field: Optional[Dict[str, Any]] = (
            UIBuilder.get_multi_line_text_field(
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.MEDIUM_FONT_SIZE,
                ),
                label="Back Text*: ",
                master=core_attributes_frame,
            )
        )

        # Style the description field's button widget
        self.back_text_field["button"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the description field's label widget
        self.back_text_field["label"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Style the description field's root widget
        self.back_text_field["root"].configure(background=Constants.BLUE_GREY["700"])

        # Configure the description field's label widget
        self.back_text_field["setter"](value=self.flashcard.back_text)

        # Place the description field within the Core attributes frame
        self.back_text_field["root"].grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create the secondary attributes frame
        secondary_attributes_frame: tkinter.Frame = UIBuilder.get_scrolled_frame(
            background=Constants.BLUE_GREY["700"],
            master=tabbed_view["center_frame"],
        )

        # Style the secondary attributes frame's canvas widget
        secondary_attributes_frame["canvas"].configure(
            background=Constants.BLUE_GREY["700"]
        )

        # Style the secondary attributes frame's root widget
        secondary_attributes_frame["frame"].configure(
            background=Constants.BLUE_GREY["700"]
        )

        # Style the secondary attributes frame's root widget
        secondary_attributes_frame["root"].configure(
            background=Constants.BLUE_GREY["700"]
        )

        # Add the secondary attributes frame to the tabbed view
        tabbed_view["adder"](
            label="Secondary Attributes",
            widget=secondary_attributes_frame["root"],
        )

        # Style the secondary attributes button
        tabbed_view["secondary_attributes_button"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Create the scrolled frame comments frame
        comments_frame: Optional[Dict[str, Any]] = UIBuilder.get_scrolled_frame(
            master=master
        )

        # Configure the scrolled frame comments frame's canvas frame
        comments_frame["canvas"].configure(background=Constants.BLUE_GREY["700"])

        # Configure the scrolled frame comments frame's frame widget
        comments_frame["frame"].configure(background=Constants.BLUE_GREY["700"])

        # Configure the scrolled frame comments frame's root frame
        comments_frame["root"].configure(background=Constants.BLUE_GREY["700"])

        # Place the comments frame widget within the center frame
        comments_frame["root"].grid(
            column=0,
            row=1,
            sticky=NSEW,
        )

        # Store the comments frame's frame widget in an instance variable
        self.comments_frame: tkinter.Frame = comments_frame["frame"]

    def create_right_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Creates and configures the main widgets of the right frame.

        Args:
            master: The parent widget.

        Returns:
            None
        """

        # Create a label widget to display the stack ID
        self.id_field: Optional[Dict[str, Any]] = UIBuilder.get_readonly_field(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            label="ID: ",
            master=master,
            value=self.flashcard.id,
        )

        # Style the ID field's label widget
        self.id_field["label"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Style the ID field's root frame
        self.id_field["root"].configure(background=Constants.BLUE_GREY["700"])

        # Place the ID field's root frame in the master widget
        self.id_field["root"].grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a label widget to display the stack UUID
        self.uuid_field: Optional[Dict[str, Any]] = UIBuilder.get_readonly_field(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            label="UUID: ",
            master=master,
            value=self.flashcard.uuid,
        )

        # Style the UUID field's label widget
        self.uuid_field["label"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Style the UUID field's root frame
        self.uuid_field["root"].configure(background=Constants.BLUE_GREY["700"])

        # Place the UUID field's root frame in the master widget
        self.uuid_field["root"].grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )

        # Create a label widget to display the stack creation date
        self.created_at_field: Optional[Dict[str, Any]] = UIBuilder.get_readonly_field(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            label="Created at: ",
            master=master,
            value=Miscellaneous.datetime_to_string(datetime=self.flashcard.created_at),
        )

        # Style the created at field's label widget
        self.created_at_field["label"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Style the created at field's root frame
        self.created_at_field["root"].configure(background=Constants.BLUE_GREY["700"])

        # Place the created at field's root frame in the master widget
        self.created_at_field["root"].grid(
            column=0,
            padx=5,
            pady=5,
            row=2,
            sticky=NSEW,
        )

        # Create a label widget to display the stack update date
        self.updated_at_field: Optional[Dict[str, Any]] = UIBuilder.get_readonly_field(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            label="Updated at: ",
            master=master,
            value=Miscellaneous.datetime_to_string(datetime=self.flashcard.updated_at),
        )

        # Style the updated at field's label widget
        self.updated_at_field["label"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Style the updated at field's root frame
        self.updated_at_field["root"].configure(background=Constants.BLUE_GREY["700"])

        # Place the updated at field's root frame in the master widget
        self.updated_at_field["root"].grid(
            column=0,
            padx=5,
            pady=5,
            row=3,
            sticky=NSEW,
        )

        # Create a separator widget
        separator: tkinter.Frame = UIBuilder.get_separator(
            master=master,
        )

        # Place the separator in the master widget
        separator.grid(
            column=0,
            padx=5,
            pady=5,
            row=4,
            sticky=NSEW,
        )

        # Retrieve all the difficulties from the database
        difficulties: Optional[List[ImmutableDifficulty]] = (
            self.unified_manager.get_all_difficulties()
        )

        # Create a combobox select field for the difficulty
        self.difficulty_field: Optional[Dict[str, Any]] = (
            UIBuilder.get_combobox_select_field(
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.MEDIUM_FONT_SIZE,
                ),
                label="Difficulty*: ",
                master=master,
                state="readonly",
                values=[difficulty.name for difficulty in difficulties],
            )
        )

        # Style the difficulty field's button widget
        self.difficulty_field["button"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the difficulty field's label widget
        self.difficulty_field["label"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Style the difficulty field's root frame
        self.difficulty_field["root"].configure(background=Constants.BLUE_GREY["700"])

        # Set the difficulty field's value to the current difficulty
        self.difficulty_field["setter"](
            value=next(
                (
                    difficulty.name
                    for difficulty in difficulties
                    if difficulty.id == self.flashcard.difficulty
                ),
                "Medium",
            )
        )

        # Place the difficulty field's root frame in the master widget
        self.difficulty_field["root"].grid(
            column=0,
            padx=5,
            pady=5,
            row=5,
            sticky=NSEW,
        )

        # Retrieve all the priorities from the database
        priorities: Optional[List[ImmutablePriority]] = (
            self.unified_manager.get_all_priorities()
        )

        # Create a combobox select field for the priority
        self.priority_field: Optional[Dict[str, Any]] = (
            UIBuilder.get_combobox_select_field(
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.MEDIUM_FONT_SIZE,
                ),
                label="Priority*: ",
                master=master,
                state="readonly",
                values=[priority.name for priority in priorities],
            )
        )

        # Style the priority field's button widget
        self.priority_field["button"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the priority field's label widget
        self.priority_field["label"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Style the priority field's root frame
        self.priority_field["root"].configure(background=Constants.BLUE_GREY["700"])

        # Set the priority field's value to the current priority
        self.priority_field["setter"](
            value=next(
                (
                    priority.name
                    for priority in priorities
                    if priority.id == self.flashcard.priority
                ),
                "Medium",
            )
        )

        # Place the priority field's root frame in the master widget
        self.priority_field["root"].grid(
            column=0,
            padx=5,
            pady=5,
            row=6,
            sticky=NSEW,
        )

    def create_bottom_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Creates and configures the main widgets of the bottom frame.

        This method initializes the main widgets of the bottom frame within the
        stack view form, setting their layout configuration.

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

    def on_front_text_field_changed(self) -> None:
        try:
            value: Optional[str] = self.front_text_field["getter"]()

            if not value:
                # Return early
                return

            flashcards: Optional[List[ImmutableFlashcard]] = (
                self.unified_manager.search_flashcards(
                    name=value,
                )
            )

            if not flashcards:
                # Log a warning message
                self.logger.warning(
                    message=f"Found no flashcard(s) in database with name '{value}'."
                )

                # Return early
                return

            if len(flashcards) == 1:
                if self.flashcard.compare_to(
                    key=[
                        "id",
                        "key",
                        "front_text",
                    ],
                    other=flashcards[0],
                ):
                    # Return early
                    return

            if len(flashcards) > 1:
                # Log a warning message
                self.logger.warning(
                    message=f"Found too many flashcards ({len(flashcards)}) in database with front text '{value}'."
                )

                # Return early
                return
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_front_text_field_changed' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def on_flashcard_updated(
        self,
        flashcard: ImmutableFlashcard,
    ) -> None:
        """
        Updates the current flashcard if the provided flashcard matches certain keys.

        This method compares the provided flashcard with the current flashcard instance
        using specific keys. If they match, the current flashcard is updated to the
        provided flashcard.

        Args:
            flashcard (ImmutableFlashcard): The flashcard to be compared and potentially updated.

        Raises:
            Exception: If an error occurs during the update process.
        """
        try:
            # Compare the current stack with the provided stack using specific keys
            if self.flashcard.compare_to(
                key=[
                    "id",
                    "key",
                    "uuid",
                ],
                other=flashcard,
            ):
                # Update the current flashcard to the provided flashcard if they match
                self.flashcard = flashcard

                # Log an info message about updating the current flashcard
                self.logger.info(message=f"Updated current flashcard: {self.flashcard}")
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_flashcard_updated' method from '{self.__class__.__name__}': {e}",
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
            subscriptions: List["dict[str, Any]"] = [
                {
                    "event": Events.FLASHCARD_UPDATED,
                    "function": self.on_flashcard_updated,
                    "namespace": Constants.GLOBAL_NAMESPACE,
                    "persistent": True,
                },
            ]

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

            # Re-raise the exception to the caller
            raise e

    def unsubscribe_from_events(self) -> None:
        """
        Unsubscribes from all events subscribed in the stack view form.

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

    def update_flashcard(self) -> None:
        """
        Updates the flashcard and saves it into the database.

        This method updates the flashcard object and saves it into the database.
        It also raises an exception if any exception has occurred during the
        update process.

        Raises:
            Exception: If an exception occurs while updating the flashcard.
        """
        try:
            # Update the flashcard object
            self.flashcard = self.unified_manager.update_flashcard(
                flashcard=self.flashcard
            )

            # Set the timestamp datetime instance variable to the current datetime
            self.timestamp = Miscellaneous.get_current_datetime()
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update_flashcard' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e
