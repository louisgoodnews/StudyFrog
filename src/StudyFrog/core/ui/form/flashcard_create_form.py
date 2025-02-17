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


__all__: List[str] = ["FlashcardCreateForm"]


class FlashcardCreateForm(tkinter.Frame):
    """
    Represents a form for creating a new flashcard.

    This form contains fields for the front and back text of the flashcard, as well as a
    combobox for selecting a stack to add the flashcard to.

    Attributes:
        master (tkinter.Misc): The parent widget.
        unified_manager (UnifiedObjectManager): The unified manager instance.
        logger (Logger): The logger instance for the class.
        stack_field (Dict[str, Any]): The combobox field for selecting a stack.
        front_field (Dict[str, Any]): The single-line text field for the front text of the flashcard.
        back_field (Dict[str, Any]): The multi-line text field for the back text of the flashcard.
    """

    def __init__(
        self,
        master: tkinter.Misc,
        unified_manager: UnifiedObjectManager,
    ) -> None:
        """
        Initializes a new instance of the FlashcardCreateForm class.

        Args:
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

        # Configure the flashcard create form widget's 1st row to weight 0.
        self.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the flashcard create form widget's 2nd row to weight 0.
        self.grid_rowconfigure(
            index=1,
            weight=0,
        )

        # Configure the flashcard create form widget's 3rd row to weight 0.
        self.grid_rowconfigure(
            index=2,
            weight=0,
        )

        # Configure the flashcard create form widget's 4th row to weight 0.
        self.grid_rowconfigure(
            index=3,
            weight=0,
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

        # Create a combobox widget to select a stack
        self.stack_field = UIBuilder.get_combobox_select_field(
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            label="Stack*: ",
            master=self,
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
            row=1,
            sticky=NSEW,
        )

        # Create a single-line text field for the front text of the flashcard
        self.front_field: Dict[str, Any] = UIBuilder.get_single_line_text_field(
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            label="Front Text*: ",
            master=self,
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
            row=2,
            sticky=NSEW,
        )

        # Create a multi-line text field for the back text of the flashcard
        self.back_field: Dict[str, Any] = UIBuilder.get_multi_line_text_field(
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            label="Back Text*: ",
            master=self,
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
            row=3,
            sticky=NSEW,
        )

    def get(self) -> Dict[str, Any]:
        """
        Retrieves the values from the form fields.

        Returns:
            Dict[str, Any]: A dictionary containing the name and description
            entered in the form fields.

        Raises:
            Exception: If an exception occurs while running the 'get' method.
        """
        try:
            # Initialize the result dictionary with empty lists and default values
            result: Dict[str, Any] = {
                "object_data": {
                    "created_at": Miscellaneous.get_current_datetime(),
                    "custom_field_values": [],
                    "last_viewed_at": Miscellaneous.get_current_datetime(),
                    "updated_at": Miscellaneous.get_current_datetime(),
                    "uuid": Miscellaneous.get_uuid(),
                },
                "related_objects": {},
            }

            # Get the back text from the back field
            result["object_data"]["back_text"] = self.back_field["getter"]()

            # Get the front text from the front field
            result["object_data"]["front_text"] = self.front_field["getter"]()

            # Get the stack from the stack field
            result["related_objects"]["stack"] = self.unified_manager.get_stack_by(
                field="name",
                value=self.stack_field["getter"](),
            )

            # Copy the difficulty from the stack
            result["object_data"]["difficulty"] = result["related_objects"]["stack"][
                "difficulty"
            ]

            # Copy the priority from the stack
            result["object_data"]["priority"] = result["related_objects"]["stack"][
                "priority"
            ]

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None
