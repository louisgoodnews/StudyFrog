"""
Author: lodego
Date: 2025-02-13
"""

import tkinter

from tkinter.constants import *

from tkinter import ttk

from typing import *

from core.ui.ui_builder import UIBuilder

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous
from utils.unified import UnifiedObjectManager


__all__: Final[List[str]] = ["StackCreateForm"]


class StackCreateForm(tkinter.Frame):
    """
    A class representing the stack create form widget of the application.

    This class is responsible for initializing and configuring the layout of the
    stack create form widget, including setting up the main frames and populating them
    with respective widgets. It also provides methods for retrieving the values from
    the form fields.

    Attributes:
        description (Dict[str, Any]): The multi-line text field for the stack description.
        dispatcher (Dispatcher): The dispatcher instance.
        logger (Logger): The logger instance.
        name (Dict[str, Any]): The single-line text field for the stack name.
    """

    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        unified_manager: UnifiedObjectManager,
    ) -> None:
        """
        Initializes a new instance of the StackCreateForm class.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.
            master (tkinter.Misc): The parent widget.
            unified_manager (UnifiedObjectManager): The unified object manager instance.
        """

        # Call the parent class constructor
        super().__init__(master=master)

        # Create a logger instance
        self.logger: Final[Logger] = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed dispatcher instance in an instance variable
        self.dispatcher: Dispatcher = dispatcher

        # Store the passed unified manager instance in an instance variable
        self.unified_manager: UnifiedObjectManager = unified_manager

        self.configure(background=Constants.BLUE_GREY["700"])

        # Configure the grid of the stack create form widget
        self.configure_grid()

        # Create the widgets of the stack create form
        self.create_widgets()

        # Place the stack create form widget in the parent widget
        self.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

    def configure_grid(self) -> None:
        """
        Configures the grid of the stack create form widget.

        This method configures the grid of the stack create form widget by setting the
        weights of the columns and rows.

        Returns:
            None
        """

        # Configure the stack create form widget's 1st column to weight 1.
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the stack create form widget's 0th and 1st row to weight 0.
        self.grid_rowconfigure(
            index=(
                0,
                1,
            ),
            weight=0,
        )

        # Configure the stack create form widget's 2nd row to weight 1.
        self.grid_rowconfigure(
            index=2,
            weight=1,
        )

    def check_required_fields(
        self,
        object_data: Dict[str, Any],
    ) -> bool:
        """
        Checks if all required fields are filled in the object data.

        Args:
            object_data (Dict[str, Any]): The data to be validated.

        Returns:
            bool: True if all required fields are filled, False otherwise.
        """

        # Validate the required fields using the helper method
        if self.validate_required_fields(object_data=object_data):
            # Return True if validation is successful
            return True

        # Show a dialog informing the user to fill all required fields
        okay: Optional[Dict[str, Any]] = UIBuilder.get_okay(
            dispatcher=self.dispatcher,
            message="Please fill in all required fields.",
            title="Required fields missing.",
        )

        # Style the okay dialog's "Root" toplevel widget
        okay["root"].configure(background=Constants.BLUE_GREY["700"])

        # Style the okay dialog's "Button" button widget
        okay["button"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the okay dialog's "Message Label" label widget
        okay["message_label"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Style the okay dialog's "Title Label" label widget
        okay["title_label"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Return False if validation fails
        return False

    def create_widgets(self) -> None:
        """
        Creates and configures the main widgets of the stack create form widget.

        This method creates and configures the main widgets of the stack create form
        widget.

        Returns:
            None
        """

        # Create a label widget to display instructions
        instruction_label: tkinter.Label = UIBuilder.get_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=self,
            text="Please fill in the fields below to create a new stack.\nFields marked with an asterisk (*) are required.",
        )

        # Place the label in the grid.
        instruction_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a separator widget to divide the flashcard create form widget
        separator: ttk.Separator = UIBuilder.get_separator(
            master=self,
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

        # Create tabbed view widgets
        notebook: Dict[str, Any] = UIBuilder.get_tabbed_view(master=self)

        # Style the notebook "Center frame" frame widget
        notebook["center_frame"].configure(background=Constants.BLUE_GREY["700"])

        # Style the notebook "Root" frame widget
        notebook["root"].configure(background=Constants.BLUE_GREY["700"])

        # Style the notebook "Top frame" frame widget
        notebook["top_frame"].configure(background=Constants.BLUE_GREY["700"])

        # Place the tabbed view widget frame in the grid
        notebook["root"].grid(
            column=0,
            row=2,
            sticky=NSEW,
        )

        # Create a scrolled frame to hold the question create form widget
        core_attributes_frame: Dict[str, Any] = UIBuilder.get_scrolled_frame(
            master=notebook["center_frame"]
        )

        # Style the scrolled frame "Canvas" widget
        core_attributes_frame["canvas"].configure(background=Constants.BLUE_GREY["700"])

        # Style the scrolled frame "Frame" widget
        core_attributes_frame["frame"].configure(background=Constants.BLUE_GREY["700"])

        # Style the scrolled frame "Root" frame widget
        core_attributes_frame["root"].configure(background=Constants.BLUE_GREY["700"])

        # Create a scrolled frame to hold the question create form widget
        secondary_attributes_frame: Dict[str, Any] = UIBuilder.get_scrolled_frame(
            master=notebook["center_frame"]
        )

        # Style the scrolled frame "Canvas" widget
        secondary_attributes_frame["canvas"].configure(
            background=Constants.BLUE_GREY["700"]
        )

        # Style the scrolled frame "Frame" widget
        secondary_attributes_frame["frame"].configure(
            background=Constants.BLUE_GREY["700"]
        )

        # Style the scrolled frame "Root" frame widget
        secondary_attributes_frame["root"].configure(
            background=Constants.BLUE_GREY["700"]
        )

        # Add the scrolled frame to the notebook widget's children
        notebook["adder"](
            label="Core Attributes",
            state=NORMAL,
            sticky=NSEW,
            widget=core_attributes_frame["root"],
        )

        # Style the scrolled frame "Core attributes" button widget
        notebook["core_attributes_button"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Add the scrolled frame to the notebook widget's children
        notebook["adder"](
            label="Secondary Attributes",
            state=NORMAL,
            sticky=NSEW,
            widget=secondary_attributes_frame["root"],
        )

        # Style the scrolled frame "Secondary attributes" button widget
        notebook["secondary_attributes_button"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Create a combobox widget to select a stack
        self.ancestor_stack_field = UIBuilder.get_combobox_select_field(
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            label="Ancestor Stack: ",
            master=core_attributes_frame["frame"],
            state="readonly",
            values=[stack.name for stack in self.unified_manager.get_all_stacks()],
        )

        # Style the stack field "Button" button widget
        self.ancestor_stack_field["button"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Bind the combobox widget to the on_ancestor_stack_select method
        self.ancestor_stack_field["combobox"].bind(
            func=self.on_ancestor_stack_select,
            sequence="<<ComboboxSelected>>",
        )

        # Style the stack field "Label" label widget
        self.ancestor_stack_field["label"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the stack field "Root" frame widget
        self.ancestor_stack_field["root"].configure(
            background=Constants.BLUE_GREY["700"]
        )

        # Place the stack field in the grid
        self.ancestor_stack_field["root"].grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a single-line text field for the stack name.
        self.name: Dict[str, Any] = UIBuilder.get_single_line_text_field(
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            label="Name* : ",
            master=core_attributes_frame["frame"],
        )

        # Style the single-line text field "Button" button widget
        self.name["button"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the single-line text field "Label" widget
        self.name["label"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
        )

        # Style the single-line text field "Root" frame widget
        self.name["root"].configure(background=Constants.BLUE_GREY["700"])

        # Focus the name entry field
        self.name["entry"].focus_set()

        # Place the single-line text field in the grid.
        self.name["root"].grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )

        # Create a stack field for the difficulty
        self.difficulty_field: Dict[str, Any] = UIBuilder.get_combobox_select_field(
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            label="Difficulty* : ",
            master=core_attributes_frame["frame"],
            state="readonly",
            value=Constants.MEDIUM.capitalize(),
            values=[
                difficulty.name
                for difficulty in self.unified_manager.get_all_difficulties()
            ],
        )

        # Set the default value for the difficulty field
        self.difficulty_field["setter"](value=Constants.MEDIUM.capitalize())

        # Style the stack field "Button" button widget
        self.difficulty_field["button"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the stack field "Label" label widget
        self.difficulty_field["label"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the stack field "Root" frame widget
        self.difficulty_field["root"].configure(background=Constants.BLUE_GREY["700"])

        # Place the stack field in the grid
        self.difficulty_field["root"].grid(
            column=0,
            padx=5,
            pady=5,
            row=2,
            sticky=NSEW,
        )

        # Create a stack field for the priority
        self.priority_field: Dict[str, Any] = UIBuilder.get_combobox_select_field(
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            label="Priority* : ",
            master=core_attributes_frame["frame"],
            state="readonly",
            values=[
                priority.name for priority in self.unified_manager.get_all_priorities()
            ],
        )

        # Set the default value for the priority field
        self.priority_field["setter"](value=Constants.MEDIUM.capitalize())

        # Style the stack field "Button" button widget
        self.priority_field["button"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the stack field "Label" label widget
        self.priority_field["label"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the stack field "Root" frame widget
        self.priority_field["root"].configure(background=Constants.BLUE_GREY["700"])

        # Place the stack field in the grid
        self.priority_field["root"].grid(
            column=0,
            padx=5,
            pady=5,
            row=3,
            sticky=NSEW,
        )

        # Create a multi-line text field for the stack description.
        self.description: Dict[str, Any] = UIBuilder.get_multi_line_text_field(
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            label="Description: ",
            master=core_attributes_frame["frame"],
        )

        self.description["button"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        self.description["label"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
        )

        self.description["root"].configure(background=Constants.BLUE_GREY["700"])

        # Place the multi-line text field in the grid.
        self.description["root"].grid(
            column=0,
            padx=5,
            pady=5,
            row=4,
            sticky=NSEW,
        )

        # Create a date entry widget for the due by date
        self.due_by: Dict[str, Any] = UIBuilder.get_date_entry(
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            label="Due by*: ",
            master=core_attributes_frame["frame"],
        )

        self.due_by["button"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        self.due_by["label"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
        )

        self.due_by["root"].configure(background=Constants.BLUE_GREY["700"])

        # Place the date entry widget in the grid.
        self.due_by["root"].grid(
            column=0,
            padx=5,
            pady=5,
            row=5,
            sticky=NSEW,
        )

        # Set the default value to the next 30 days
        self.due_by["setter"](
            value=Miscellaneous.datetime_to_string(
                datetime=Miscellaneous.get_date_increment(increment=30),
                format="%Y-%m-%d",
            )
        )

    def get(self) -> Dict[str, Any]:
        """
        Retrieves the values from the form fields.

        Returns:
            Dict[str, Any]: A dictionary containing the name and description
            entered in the form fields.
        """

        # Initialize the result dictionary as an empty dictionary
        result: Dict[str, Any] = {
            "object_data": {
                "ancestor": None,
                "contents": [],
                "created_at": Miscellaneous.get_current_datetime(),
                "custom_field_values": [],
                "descendants": [],
                "description": "",
                "due_by": None,
                "difficulty": None,
                "icon": "📚",
                "last_viewed_at": Miscellaneous.get_current_datetime(),
                "name": "",
                "priority": None,
                "status": None,
                "tags": [],
                "updated_at": Miscellaneous.get_current_datetime(),
                "uuid": Miscellaneous.get_uuid(),
            },
            "related_objects": {},
        }

        # Get the value of the stack name from the single-line text field
        result["object_data"]["name"] = self.name["getter"]()

        # Get the value of the stack description from the multi-line text field
        result["object_data"]["description"] = self.description["getter"]() or ""

        # Get the value of the due by date from the date entry widget
        result["object_data"]["due_by"] = self.due_by["getter"]()

        # Get the difficulty from the difficulty field
        result["related_objects"]["ancestor_stack"] = self.unified_manager.get_stack_by(
            field="name",
            value=self.ancestor_stack_field["getter"](),
        )

        # Get the difficulty from the difficulty field
        result["related_objects"]["difficulty"] = (
            self.unified_manager.get_difficulty_by(
                field="name",
                value=self.difficulty_field["getter"](),
            )
        )

        # Get the priority from the priority field
        result["related_objects"]["priority"] = self.unified_manager.get_priority_by(
            field="name",
            value=self.priority_field["getter"](),
        )

        if result["related_objects"]["ancestor_stack"]:
            # Get the value of the difficulty from the difficulty field
            result["object_data"]["ancestor"] = result["related_objects"][
                "ancestor_stack"
            ]["id"]

        if result["related_objects"]["difficulty"]:
            # Get the value of the difficulty from the difficulty field
            result["object_data"]["difficulty"] = result["related_objects"][
                "difficulty"
            ]["id"]

        if result["related_objects"]["priority"]:
            # Get the value of the priority from the priority field
            result["object_data"]["priority"] = result["related_objects"]["priority"][
                "id"
            ]

        # Return the result dictionary
        return result

    def on_ancestor_stack_select(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        Handles the selection event of the ancestor stack field.

        Args:
            event (tkinter.Event): The event object. Defaults to None

        Returns:
            None

        Raises:
            Exception: If an exception occurs
        """
        try:
            # Get the value from the ancestor stack field
            value: Optional[str] = self.ancestor_stack_field["getter"]()

            if not value:
                # Log a warning message
                self.logger.warning(message="Got no value from 'Ancestor stack' field.")

                # Return early
                return

            stack: Optional[ImmutableStack] = self.unified_manager.get_stack_by(
                field="name",
                value=value,
            )

            if not stack:
                # Log a warning message
                self.logger.warning(message="Got no stack from 'Ancestor stack' field.")

                # Return early
                return

            # Set the due by date
            self.due_by["setter"](value=stack["due_by"])
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_ancestor_stack_select' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def validate_required_fields(
        self,
        object_data: Dict[str, Any],
    ) -> bool:
        """
        Validates the object data to ensure all required fields have been provided.

        Args:
            object_data (Dict[str, Any]): The object data to validate.

        Returns:
            bool: True if all required fields have been provided, False otherwise.
        """

        # Define the required fields
        required_fields: List[str] = [
            "name",  # The name of the stack
            "due_by",  # The due by date of the stack
            "difficulty",  # The difficulty of the stack
            "priority",  # The priority of the stack
        ]

        # Validate all required fields
        result: bool = all(
            object_data["object_data"].get(
                field,  # The field to validate
                None,  # The default value to return if the field is not present
            )
            is not None  # The condition to check (i.e., the field should not be None)
            for field in required_fields  # Iterate over all required fields
        )

        # Return the result
        return result
