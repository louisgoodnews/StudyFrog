"""
Author: lodego
Date: 2025-02-13
"""

import tkinter

from tkinter.constants import *

from tkinter import ttk

from typing import *

from core.stack import ImmutableStack

from core.ui.ui_builder import UIBuilder

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous
from utils.unified import UnifiedObjectManager


__all__: Final[List[str]] = ["FlashcardCreateForm"]


class FlashcardCreateForm(tkinter.Frame):
    """
    Represents a form for creating a new flashcard.

    This form contains fields for the front and back text of the flashcard, as well as a
    combobox for selecting a stack to add the flashcard to.

    Attributes:
        front_field (Dict[str, Any]): The single-line text field for the front text of the flashcard.
        back_field (Dict[str, Any]): The multi-line text field for the back text of the flashcard.
        dispatcher (Dispatcher): The dispatcher instance for the class.
        logger (Logger): The logger instance for the class.
        master (tkinter.Misc): The parent widget.
        stack_field (Dict[str, Any]): The combobox field for selecting a stack.
        unified_manager (UnifiedObjectManager): The unified manager instance.
    """

    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        unified_manager: UnifiedObjectManager,
    ) -> None:
        """
        Initializes a new instance of the FlashcardCreateForm class.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.
            master (tkinter.Misc): The parent widget.
            unified_manager (UnifiedObjectManager): The unified manager instance.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            master=master,
        )

        # Create a logger instance for the class
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Store the dispatcher instance in an instance variable
        self.dispatcher: Dispatcher = dispatcher

        # Store the unified manager instance in an instance variable
        self.unified_manager: UnifiedObjectManager = unified_manager

        # Set the background color of the flashcard create form widget
        self.configure(background=Constants.BLUE_GREY["700"])

        # Configure the grid of the flashcard create form widget
        self.configure_grid()

        # Initialize and place the widgets of the flashcard create form
        self.create_widgets()

        # Position the flashcard create form widget in the parent widget
        self.grid(
            column=0,
            row=0,
            sticky=NSEW,
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

    def configure_grid(self) -> None:
        """
        Configures the grid of the flashcard create form widget.

        This method configures the grid of the flashcard create form widget by setting the
        weights of the columns and rows.

        Returns:
            None
        """

        # Configure the flashcard create form widget's 1st column to weight 1.
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the flashcard create form widget's 1st and 2nd row to weight 0.
        self.grid_rowconfigure(
            index=(
                0,
                1,
            ),
            weight=0,
        )

        # Configure the flashcard create form widget's 3rd row to weight 1.
        self.grid_rowconfigure(
            index=2,
            weight=1,
        )

    def create_widgets(self) -> None:
        """
        Creates and configures the main widgets of the flashcard create form widget.

        This method sets up the necessary widgets for the flashcard creation form,
        including labels, text fields, and a combobox for selecting a stack.
        All widgets are styled and placed on the grid layout.

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
            text="Please fill in the fields below to create a new flashcard.\nFields marked with an asterisk (*) are required.",
        )

        # Place the instruction label in the grid
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

        # Create the scrolled frame widgets
        scrolled_frame: Dict[str, Any] = UIBuilder.get_scrolled_frame(master=self)

        # Style the scrolled frame "Canvas" widget
        scrolled_frame["canvas"].configure(background=Constants.BLUE_GREY["700"])

        # Style the scrolled frame "Frame" widget
        scrolled_frame["frame"].configure(background=Constants.BLUE_GREY["700"])

        # Style the scrolled frame "Root" frame widget
        scrolled_frame["root"].configure(background=Constants.BLUE_GREY["700"])

        # Place the "Root frame" frame widget within the passed master widget
        scrolled_frame["root"].grid(
            column=0,
            padx=5,
            pady=5,
            row=2,
            sticky=NSEW,
        )

        # Create a combobox widget to select a stack
        self.stack_field = UIBuilder.get_combobox_select_field(
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            label="Stack*: ",
            master=scrolled_frame["frame"],
            state="readonly",
            values=[stack.name for stack in self.unified_manager.get_all_stacks()],
        )

        # Style the stack field "Button" button widget
        self.stack_field["button"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the stack field "Label" label widget
        self.stack_field["label"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the stack field "Root" frame widget
        self.stack_field["root"].configure(background=Constants.BLUE_GREY["700"])

        # Place the stack field in the grid
        self.stack_field["root"].grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a multi-line text field for the front text of the flashcard
        self.front_field: Dict[str, Any] = UIBuilder.get_multi_line_text_field(
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            label="Front Text*: ",
            master=scrolled_frame["frame"],
        )

        # Style the front field "Button" button widget
        self.front_field["button"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the front field "Label" label widget
        self.front_field["label"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the front field "Root" frame widget
        self.front_field["root"].configure(background=Constants.BLUE_GREY["700"])

        # Place the front field in the grid
        self.front_field["root"].grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )

        # Create a multi-line text field for the back text of the flashcard
        self.back_field: Dict[str, Any] = UIBuilder.get_multi_line_text_field(
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            label="Back Text*: ",
            master=scrolled_frame["frame"],
        )

        # Style the back field "Button" button widget
        self.back_field["button"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the back field "Label" label widget
        self.back_field["label"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the back field "Root" frame widget
        self.back_field["root"].configure(background=Constants.BLUE_GREY["700"])

        # Place the back field in the grid
        self.back_field["root"].grid(
            column=0,
            padx=5,
            pady=5,
            row=2,
            sticky=NSEW,
        )

    def get(self) -> Optional[Dict[str, Any]]:
        """
        Retrieves the values from the form fields.

        Returns:
            Dict[str, Any]: A dictionary containing the name and description
            entered in the form fields.

        Raises:
            Exception: If an exception occurs while running the 'get' method.
        """
        try:
            # Get the stack from the stack field
            stack: Optional[ImmutableStack] = self.unified_manager.get_stack_by(
                field="name",
                value=self.stack_field["getter"](),
            )

            # Check, if a stack was found
            if not stack:
                # Log a warning message indicating that no stack was found
                self.logger.warning(
                    message=f"No stack found with name '{self.stack_field['getter']()}'",
                )

                # Return early
                return None

            # Initialize the result dictionary
            result: Dict[str, Any] = {
                "object_data": {
                    "back_text": self.back_field["getter"](),
                    "back_word_count": len(self.back_field["getter"]().split()),
                    "created_at": Miscellaneous.get_current_datetime(),
                    "custom_field_values": [],
                    "familiarity": 0.0,
                    "front_text": self.front_field["getter"](),
                    "front_word_count": len(self.front_field["getter"]().split()),
                    "icon": None,
                    "id": None,
                    "key": None,
                    "last_viewed_at": Miscellaneous.get_current_datetime(),
                    "total_word_count": (
                        len(self.front_field["getter"]().split())
                        + len(self.back_field["getter"]().split())
                    ),
                    "updated_at": Miscellaneous.get_current_datetime(),
                    "uuid": Miscellaneous.get_uuid(),
                    "difficulty": stack["difficulty"],
                    "priority": stack["priority"],
                },
                "related_objects": {"stack": stack},
            }

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

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
            "front_text",  # The front side of the flashcard
            "back_text",  # The back side of the flashcard
            "stack",  # The stack the flashcard belongs to
            "difficulty",  # The difficulty of the flashcard
            "priority",  # The priority of the flashcard
        ]

        # Validate all required fields
        result: bool = all(
            object_data.get(
                field,  # The field to validate
                None,  # The default value to return if the field is not present
            )
            is not None  # The condition to check (i.e., the field should not be None)
            for field in required_fields  # Iterate over all required fields
        )

        # Return the result
        return result
