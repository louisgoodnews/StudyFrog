"""
Author: lodego
Date 2025-03-02
"""

import tkinter

from tkinter.constants import *

from tkinter import ttk

from typing import *

from core.difficulty import ImmutableDifficulty
from core.flashcard import ImmutableFlashcard
from core.note import ImmutableNote
from core.priority import ImmutablePriority
from core.question import ImmutableQuestion
from core.stack import ImmutableStack, MutableStack

from core.ui.ui_builder import UIBuilder

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous
from utils.unified import UnifiedObjectManager


__all__: Final[List[str]] = ["StackViewForm"]


class StackViewForm(tkinter.Frame):
    """
    Represents the stack view form widget of the application.

    This class is responsible for initializing and configuring the layout of the
    stack view form widget, including setting up the main frames and populating them
    with respective widgets.

    Attributes:
        dispatcher (Dispatcher): The dispatcher instance.
        logger (Logger): The logger instance.
        stack (Union[ImmutableStack, MutableStack]): The stack instance.
        unified_manager (UnifiedObjectManager): The unified manager instance.
    """

    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        stack: Union[ImmutableStack, MutableStack],
        unified_manager: UnifiedObjectManager,
    ) -> None:
        """
        Initializes a new instance of the StackViewForm class.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.
            master (tkinter.Misc): The parent widget.
            stack (Union[ImmutableStack, MutableStack]): The stack instance.
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

        # Store the passed stack instance in an instance variable
        self.stack: Union[ImmutableStack, MutableStack] = stack

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

        # Load the content of the stack by iterating over its contents
        for key in self.stack["contents"]:
            self.load_content_by_key(key=key)

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
        top_frame: tkinter.Frame = tkinter.Frame(master=self)

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
        center_frame: tkinter.Frame = tkinter.Frame(master=self)

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
        bottom_frame: tkinter.Frame = tkinter.Frame(master=self)

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

        # Configure the master widget's 0th row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create the single line text field for the stack name
        self.name_field: Optional[Dict[str, Any]] = (
            UIBuilder.get_single_line_text_field(
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                label="Name*: ",
                master=master,
            )
        )

        # Style the name field's button widget
        self.name_field["button"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Bind the name field to the on_name_field_changed function
        self.name_field["entry"].bind(
            func=lambda event: self.on_name_field_changed(),
            sequence="<KeyRelease>",
        )

        # Style the name field's label widget
        self.name_field["label"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
        )

        # Style the name field's root widget
        self.name_field["root"].configure(background=Constants.BLUE_GREY["700"])

        # Set the name field's value to the stack's name
        self.name_field["setter"](value=self.stack.name)

        # Configure the name field
        self.name_field["entry"].configure(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.MEDIUM_FONT_SIZE,
            ),
        )

        # Configure the name field
        self.name_field["label"].configure(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Place the name field in the top frame
        self.name_field["root"].grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create a separator widget to divide the stack view form widget
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
        left_frame: tkinter.Frame = tkinter.Frame(
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
        right_frame: tkinter.Frame = tkinter.Frame(
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

        # Create the core attributes frame
        core_attributes_frame: tkinter.Frame = tkinter.Frame(
            background=Constants.BLUE_GREY["700"],
            master=tabbed_view["center_frame"],
        )

        # Configure the core attributes frame's 0th column to weight 1
        core_attributes_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the core attributes frame's 0th row to weight 1
        core_attributes_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Add the core attributes frame to the tabbed view
        tabbed_view["adder"](
            label="Core Attributes",
            widget=core_attributes_frame,
        )

        # Style the core attributes button
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
        self.description_field: Optional[Dict[str, Any]] = (
            UIBuilder.get_multi_line_text_field(
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.MEDIUM_FONT_SIZE,
                ),
                label="Description: ",
                master=core_attributes_frame,
            )
        )

        # Style the description field's button widget
        self.description_field["button"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the description field's label widget
        self.description_field["label"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Style the description field's root widget
        self.description_field["root"].configure(background=Constants.BLUE_GREY["700"])

        # Configure the description field's label widget
        self.description_field["setter"](value=self.stack.description or "")

        # Place the description field within the core attributes frame
        self.description_field["root"].grid(
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

        # Create the scrolled frame contents frame
        contents_frame: Optional[Dict[str, Any]] = UIBuilder.get_scrolled_frame(
            master=master
        )

        # Configure the scrolled frame contents frame's canvas frame
        contents_frame["canvas"].configure(background=Constants.BLUE_GREY["700"])

        # Configure the scrolled frame contents frame's frame widget
        contents_frame["frame"].configure(background=Constants.BLUE_GREY["700"])

        # Configure the scrolled frame contents frame's root frame
        contents_frame["root"].configure(background=Constants.BLUE_GREY["700"])

        # Place the contents frame widget within the center frame
        contents_frame["root"].grid(
            column=0,
            row=1,
            sticky=NSEW,
        )

        # Store the contents frame's frame widget in an instance variable
        self.contents_frame: tkinter.Frame = contents_frame["frame"]

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
            row=2,
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
            value=self.stack.id,
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
            value=self.stack.uuid,
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
            value=Miscellaneous.datetime_to_string(datetime=self.stack.created_at),
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
            value=Miscellaneous.datetime_to_string(datetime=self.stack.updated_at),
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
            ttk.Combobox_field(
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
                    if difficulty.id == self.stack.difficulty
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
            ttk.Combobox_field(
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
                    if priority.id == self.stack.priority
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

    def load_content_by_key(
        self,
        key: str,
        object: Optional[
            Union[
                ImmutableFlashcard,
                ImmutableNote,
                ImmutableQuestion,
            ]
        ] = None,
    ) -> None:
        """
        Loads content by key.

        This method attempts to load content by key using the unified object manager.
        If the object is not provided, it will be loaded from the unified object manager.
        If the object is not found, a warning message is logged.
        If an exception occurs, an error message is logged and the exception is re-raised.

        Args:
            key (str): The key of the object to be loaded.
            object (Optional[Union[ImmutableFlashcard, ImmutableNote, ImmutableQuestion]], optional): The object to be loaded. Defaults to None.

        Raises:
            Exception: If an exception occurs during the load process.
        """

        try:
            # Try to match any characters of the key
            match: Optional[str] = Miscellaneous.find_match(
                group=1,
                pattern=r"([A-Za-z]+)",
                string=key,
            )

            if not match:
                # Return early
                return

            if not object:
                object = self.unified_manager.__getattr__(
                    name=f"get_{match.lower()}_by_key"
                )(key=key)

            if not object:
                # Log a warning message
                self.logger.warning(message=f"Failed to load content by key '{key}'.")

                # Return early
                return

            # Get the index of the next available row of the contents frame
            row: int = len(self.contents_frame.winfo_children())

            # Create a tkinter.Frame widget
            frame: tkinter.Frame = tkinter.Frame(master=self.contents_frame)

            # Configure the frame widget's 0th column to weight 0
            frame.grid_columnconfigure(
                index=0,
                weight=0,
            )

            # Configure the frame widget's 1st column to weight 0
            frame.grid_columnconfigure(
                index=1,
                weight=0,
            )

            # Configure the frame widget's 2nd column to weight 1
            frame.grid_columnconfigure(
                index=2,
                weight=1,
            )

            # Configure the frame widget
            frame.configure(background=Constants.BLUE_GREY["700"])

            # Place the frame in the contents frame widget
            frame.grid(
                column=0,
                padx=5,
                pady=10,
                row=row,
                sticky=NSEW,
            )

            # Create a tkinter.Label widget to display the object's icon
            icon_label: tkinter.Label = tkinter.Label(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=frame,
                text=object["icon"],
            )

            # Bind the label to the on_label_left_click function
            icon_label.bind(
                func=lambda event: self.on_label_left_click(object=object),
                sequence="<ButtonRelease-1>",
            )

            # Bind the label to the on_label_right_click function
            icon_label.bind(
                func=lambda event: self.on_label_right_click(
                    event=event, object=object
                ),
                sequence="<ButtonRelease-2>",
            )

            # Place the icon label in the grid
            icon_label.grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Create a tkinter.Label widget to display the object's key
            key_label: tkinter.Label = tkinter.Label(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=frame,
                text=object["key"],
            )

            # Bind the label to the on_label_left_click function
            key_label.bind(
                func=lambda event: self.on_label_left_click(object=object),
                sequence="<ButtonRelease-1>",
            )

            # Bind the label to the on_label_right_click function
            key_label.bind(
                func=lambda event: self.on_label_right_click(
                    event=event, object=object
                ),
                sequence="<ButtonRelease-2>",
            )

            # Place the key label in the grid
            key_label.grid(
                column=1,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            text: str

            if isinstance(
                object,
                ImmutableFlashcard,
            ):
                text = object["front_text"]
            elif isinstance(
                object,
                ImmutableNote,
            ):
                text = object["title"]
            elif isinstance(
                object,
                ImmutableQuestion,
            ):
                text = object["question_text"]
            else:
                text = "None"

            # Create a tkinter.Label widget to display the object's title
            title_label: tkinter.Label = tkinter.Label(
                anchor=W,
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                justify=LEFT,
                master=frame,
                text=text,
            )

            # Bind the label to the on_label_left_click function
            title_label.bind(
                func=lambda event: self.on_label_left_click(object=object),
                sequence="<ButtonRelease-1>",
            )

            # Bind the label to the on_label_right_click function
            title_label.bind(
                func=lambda event: self.on_label_right_click(
                    event=event,
                    object=object,
                ),
                sequence="<ButtonRelease-2>",
            )

            # Place the title label in the grid
            title_label.grid(
                column=2,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'load_content_by_key' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def on_name_field_changed(self) -> None:
        try:
            value: Optional[str] = self.name_field["getter"]()

            if not value:
                # Return early
                return

            stacks: Optional[List[ImmutableStack]] = self.unified_manager.search_stacks(
                name=value,
            )

            if not stacks:
                # Log a warning message
                self.logger.warning(
                    message=f"Found no stack(s) in database with name '{value}'."
                )

                # Return early
                return

            if len(stacks) == 1:
                if self.stack.compare_to(
                    key=[
                        "id",
                        "key",
                        "name",
                    ],
                    other=stacks[0],
                ):
                    # Return early
                    return

            if len(stacks) > 1:
                # Log a warning message
                self.logger.warning(
                    message=f"Found too many stacks ({len(stacks)}) in database with name '{value}'."
                )

                # Return early
                return

        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_name_field_changed' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def on_flashcard_created(
        self,
        flashcard: ImmutableFlashcard,
    ) -> None:
        """
        Handles the 'on_flashcard_created' event and loads the flashcard into the UI.

        Args:
            flashcard (ImmutableFlashcard): The flashcard to be loaded into the UI.

        Raises:
            Exception: If an exception occurs while loading the flashcard.
        """
        try:
            # Load the flashcard into the UI
            self.load_content_by_key(
                key=flashcard.key,
                object=flashcard,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_flashcard_created' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def on_label_left_click(
        self,
        object: Union[
            ImmutableFlashcard,
            ImmutableNote,
            ImmutableQuestion,
        ],
    ) -> None:
        """
        Handles the 'on_label_left_click' event and navigates to the next item in the navigation history.

        Args:
            object (ImmutableFlashcard | ImmutableNote | ImmutableQuestion): The object associated with the label that was clicked.

        Raises:
            Exception: If an exception occurs while attempting to navigate to the next item in the navigation history.
        """
        try:
            # Initialize the kwargs dictionary as an empty dictionary
            kwargs: Dict[str, Any] = {}

            # Try to match any characters of the key
            # The pattern is a regular expression that matches any characters of the key
            # The group=1 argument specifies that we want to match the first group (the first argument of the regular expression)
            # The string=object.key argument specifies that we want to match the key of the object
            match: Optional[str] = Miscellaneous.find_match(
                group=1,
                pattern=r"([A-Za-z]+)",
                string=object.key,
            )

            if not match:
                # Return early if no match is found
                return

            # Set the direction to "forward"
            kwargs["direction"] = "forward"

            # Create the "Master" toplevel widget
            kwargs["master"] = tkinter.Toplevel()

            # Configure the toplevel widget's 0th column to weight 1
            kwargs["master"].grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the toplevel widget's 0th row to weight 1
            kwargs["master"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Add the object to the kwargs
            # The key is the type of the object (e.g. flashcard, note, question)
            # The value is the object itself
            kwargs[match.lower()] = object

            # Set the source of the navigation history item to "edit_ui"
            kwargs["source"] = "edit_ui"

            # Set the target of the navigation history item to "edit_ui"
            kwargs["target"] = "edit_ui"

            # Dispatch the request to validate the navigation history item
            self.dispatcher.dispatch(
                event=Events.REQUEST_VALIDATE_NAVIGATION,
                namespace=Constants.GLOBAL_NAMESPACE,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_label_left_click' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def on_label_right_click(
        self,
        event: tkinter.Event,
        object: Union[
            ImmutableFlashcard,
            ImmutableNote,
            ImmutableQuestion,
        ],
    ) -> None:
        """
        Handles the 'on_label_right_click' event and displays a context menu for the label.

        The context menu contains two items:
            1. Edit: Navigates to the next item in the navigation history.
            2. Delete: Deletes the object associated with the label.

        Args:
            event (tkinter.Event): The event object.
            object (ImmutableFlashcard | ImmutableNote | ImmutableQuestion): The object associated with the label.

        Raises:
            Exception: If an exception occurs while displaying the context menu.
        """
        try:
            # Find the type of the object from the key
            match: Optional[str] = Miscellaneous.find_match(
                group=1,
                pattern=r"([A-Za-z]+)",
                string=object.key,
            )

            if not match:
                # Return early if no match is found
                return

            # Create a new instance of tkinter.Menu
            menu: tkinter.Menu = UIBuilder.get_menu(
                master=self,
                tearoff=0,
            )

            # Add the "Edit" item to the menu
            # The command is a lambda function that calls the on_label_left_click method
            menu.add_command(
                label="Edit",
                command=lambda: self.on_label_left_click(
                    event=event,
                    object=object,
                ),
            )

            # Add the "Delete" item to the menu
            # The command is a lambda function that calls the delete method of the unified object manager
            menu.add_command(
                label="Delete",
                command=lambda: (
                    self.unified_manager.__getattr__(name=f"delete_{match.lower()}")(
                        object
                    )
                ),
            )

            # Post the menu at the location of the event
            menu.post(
                x=event.x_root,
                y=event.y_root,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_label_right_click' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def on_note_created(
        self,
        note: ImmutableNote,
    ) -> None:
        """
        Handles the 'on_note_created' event and loads the note into the UI.

        Args:
            note (ImmutableNote): The note to be loaded into the UI.

        Raises:
            Exception: If an exception occurs while loading the note.
        """
        try:
            # Load the note into the UI
            self.load_content_by_key(
                key=note.key,
                object=note,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_note_created' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def on_question_created(
        self,
        question: ImmutableQuestion,
    ) -> None:
        """
        Handles the 'on_question_created' event and loads the question into the UI.

        Args:
            question (ImmutableQuestion): The question to be loaded into the UI.

        Raises:
            Exception: If an exception occurs while loading the question.
        """
        try:
            # Load the content by the key of the provided question
            self.load_content_by_key(
                key=question.key,
                object=question,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_question_created' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def on_stack_updated(
        self,
        stack: ImmutableStack,
    ) -> None:
        """
        Updates the current stack if the provided stack matches certain keys.

        This method compares the provided stack with the current stack instance
        using specific keys. If they match, the current stack is updated to the
        provided stack.

        Args:
            stack (ImmutableStack): The stack to be compared and potentially updated.

        Raises:
            Exception: If an error occurs during the update process.
        """
        try:
            # Compare the current stack with the provided stack using specific keys
            if self.stack.compare_to(
                key=[
                    "id",
                    "key",
                    "uuid",
                ],
                other=stack,
            ):
                # Update the current stack to the provided stack if they match
                self.stack = stack

                # Log an info message about updating the current stack
                self.logger.info(message=f"Updated current stack: {self.stack}")
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
            subscriptions: List[Dict[str, Any]] = [
                {
                    "event": Events.FLASHCARD_CREATED,
                    "function": self.on_flashcard_created,
                    "namespace": Constants.GLOBAL_NAMESPACE,
                    "persistent": True,
                },
                {
                    "event": Events.NOTE_CREATED,
                    "function": self.on_note_created,
                    "namespace": Constants.GLOBAL_NAMESPACE,
                    "persistent": True,
                },
                {
                    "event": Events.QUESTION_CREATED,
                    "function": self.on_question_created,
                    "namespace": Constants.GLOBAL_NAMESPACE,
                    "persistent": True,
                },
                {
                    "event": Events.STACK_UPDATED,
                    "function": self.on_stack_updated,
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

    def update_stack(self) -> None:
        """
        Updates the stack and saves it into the database.

        This method updates the stack object and saves it into the database.
        It also raises an exception if any exception has occurred during the
        update process.

        Raises:
            Exception: If an exception occurs while updating the stack.
        """
        try:
            # Update the stack object
            self.stack = self.unified_manager.update_stack(stack=self.stack)

            # Set the timestamp datetime instance variable to the current datetime
            self.timestamp = Miscellaneous.get_current_datetime()
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'update_stack' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e
