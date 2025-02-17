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


__all__: List[str] = ["QuestionCreateForm"]


class QuestionCreateForm(tkinter.Frame):
    """
    Represents a form for creating a new question.

    This form contains fields for the question text and a combobox for selecting a stack to add the question to.

    Attributes:
        master (tkinter.Misc): The parent widget.
        unified_manager (UnifiedObjectManager): The unified manager instance.
        logger (Logger): The logger instance for the class.
    """

    def __init__(
        self,
        master: tkinter.Misc,
        unified_manager: UnifiedObjectManager,
    ) -> None:
        """
        Initializes a new instance of the QuestionCreateForm class.

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

        # Set the background color of the question create form widget
        self.configure(background=Constants.BLUE_GREY["700"])

        # Configure the grid of the question create form widget
        self.configure_grid()

        # Initialize and place the widgets of the question create form
        self.create_widgets()

        # Position the question create form widget in the parent widget
        self.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

    def configure_grid(self) -> None:
        """
        Configures the grid of the question create form widget.

        This method configures the grid of the question create form widget by setting the
        weights of the columns and rows.

        Returns:
            None
        """

        # Configure the question create form widget's 1st column to weight 1
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the question create form widget's 1st row to weight 0
        self.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the question create form widget's 2nd row to weight 1
        self.grid_rowconfigure(
            index=1,
            weight=1,
        )

    def create_widgets(self) -> None:
        """
        Creates and configures the main widgets of the question create form widget.

        This method sets up the necessary widgets for the question creation form,
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
            text="Please fill in the fields below to create a new question.\nFields marked with an asterisk (*) are required.",
        )

        # Place the instruction label in the grid
        instruction_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a scrolled frame to hold the question create form widget
        scrolled_frame: Dict[str, Any] = UIBuilder.get_scrolled_frame(master=self)

        # Style the scrolled frame "Frame" widget
        scrolled_frame["frame"].configure(background=Constants.BLUE_GREY["700"])

        # Style the scrolled frame "Root" frame widget
        scrolled_frame["root"].configure(background=Constants.BLUE_GREY["700"])

        # Place the scrolled frame in the grid
        scrolled_frame["root"].grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
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

        # Create a multi-line text field for the question text of the question
        self.question_text_field: Dict[str, Any] = UIBuilder.get_multi_line_text_field(
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            label="Question Text*: ",
            master=scrolled_frame["frame"],
        )

        # Style the question text field "Button" button widget
        self.question_text_field["button"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the question text field "Label" label widget
        self.question_text_field["label"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the question text field "Root" frame widget
        self.question_text_field["root"].configure(
            background=Constants.BLUE_GREY["700"]
        )

        # Place the question text field in the grid
        self.question_text_field["root"].grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )

        # Create a combobox widget to select a question type
        self.question_type_field = UIBuilder.get_combobox_select_field(
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            label="Question Type*: ",
            master=scrolled_frame["frame"],
            state="readonly",
            values=[
                "Multiple Choice",
                "True/False",
            ],
        )

        # Style the question type field "Button" button widget
        self.question_type_field["button"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the question type field "Label" label widget
        self.question_type_field["label"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the question type field "Root" frame widget
        self.question_type_field["root"].configure(
            background=Constants.BLUE_GREY["700"]
        )

        # Place the question type field in the grid
        self.question_type_field["root"].grid(
            column=0,
            padx=5,
            pady=5,
            row=2,
            sticky=NSEW,
        )

    def get(self) -> Optional[Dict[str, Any]]:
        """
        Retrieves the values from the form fields.

        This method retrieves the values from the form fields and returns a
        dictionary containing the question data and related objects.

        Returns:
            Optional[Dict[str, Any]]: The result dictionary containing the question data
            and related objects, or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while running the SQL query.
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

    def on_question_type_select(self) -> None:
        try:
            pass
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_question_type_select' method from '{self.__class__.__name__}': {e}"
            )

            # Raise the exception to the caller
            raise e
