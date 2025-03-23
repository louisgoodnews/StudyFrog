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


__all__: Final[List[str]] = ["QuestionCreateForm"]


class QuestionCreateForm(tkinter.Frame):
    """
    Represents a form for creating a new question.

    This form contains fields for the question text and a combobox for selecting a stack to add the question to.

    Attributes:
        dispatcher (Dispatcher): The dispatcher instance.
        logger (Logger): The logger instance for the class.
        master (tkinter.Misc): The parent widget.
        unified_manager (UnifiedObjectManager): The unified manager instance.
    """

    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        unified_manager: UnifiedObjectManager,
    ) -> None:
        """
        Initializes a new instance of the QuestionCreateForm class.

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

        # Initialize an empty list for the answer fields
        self.answer_fields: List[tkinter.Misc] = []

        # Store the dispatcher instance in an instance variable
        self.dispatcher: Dispatcher = dispatcher

        # Store the question type in an instance variable
        self.question_type: str = ""

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

    def clear(self) -> None:
        """
        Clears the content of the answers frame widget.

        This method clears the content of the answers frame widget by destroying all its children
        widgets.

        Returns:
            None
        """

        # Get a list of all children widgets in the answers frame widget
        children: List[tkinter.Misc] = self.answers_frame.winfo_children()

        # Check if the answers frame widget has any children widgets
        if len(children) == 0:
            # Return early if there are no children widgets
            return

        # Iterate over the children of the answers frame widget
        for child in children:
            # Destroy each child widget
            child.destroy()

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
        Configures the grid of the question create form widget.
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

        # Configure the question create form widget's 2nd row to weight 0
        self.grid_rowconfigure(
            index=1,
            weight=0,
        )

        # Configure the question create form widget's 3rd row to weight 1
        self.grid_rowconfigure(
            index=2,
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

        # Create a separator widget to divide the question create form widget
        separator: ttk.Separator = UIBuilder.get_separator(
            master=self,
            orient=VERTICAL,
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
        notebook["core attributes_button"].configure(
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
        notebook["secondary attributes_button"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Create a combobox widget to select a stack
        self.stack_field = UIBuilder.get_combobox_select_field(
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            label="Stack*: ",
            master=core_attributes_frame["frame"],
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
        self.question_text_field: Dict[str, Any] = UIBuilder.get_scrolled_text_field(
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            height=15,
            label="Question Text*: ",
            master=core_attributes_frame["frame"],
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
            master=core_attributes_frame["frame"],
            state="readonly",
            values=[
                "Multiple Choice",
                "Open Answer",
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

        self.question_type_field["combobox"].bind(
            func=lambda e: self.on_question_type_select(),
            sequence="<<ComboboxSelected>>",
        )

        # Place the question type field in the grid
        self.question_type_field["root"].grid(
            column=0,
            padx=5,
            pady=5,
            row=2,
            sticky=NSEW,
        )

        # Create the answers frame
        self.answers_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=core_attributes_frame["frame"],
        )

        # Place the answers frame in the grid
        self.answers_frame.grid(
            column=0,
            padx=5,
            pady=5,
            row=3,
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
                    "question_text": self.question_text_field["getter"](),
                    "question_type": Miscellaneous.any_to_snake(
                        string=self.question_type_field["getter"]().replace(
                            "/",
                            "_",
                        )
                    ).upper(),
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

            if result["object_data"]["question_type"] == "MULTIPLE_CHOICE":
                # Get the answers from the answer fields
                result["related_objects"]["answers"] = [
                    answer_field["getter"]() for answer_field in self.answer_fields
                ]
            elif result["object_data"]["question_type"] == "OPEN_ANSWER":
                # Get the open answer from the open answer field
                result["related_objects"]["answers"] = [
                    self.answer_fields[0]["getter"]()
                ]
            elif result["object_data"]["question_type"] == "TRUE_FALSE":
                # Get the true false answer from the true false answer field
                result["related_objects"]["answers"] = [
                    self.answer_fields[0]["getter"]()
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

    def on_add_answer_button_click(self) -> None:
        """
        Handles the event when the "Add Answer" button is clicked.

        This method is called when the "Add Answer" button is clicked. It creates a
        new multiple choice answer field and adds it to the list of fields.
        """
        try:
            # Create a new multiple choice answer field
            answer_field: Dict[str, Any] = UIBuilder.get_multiple_choice_answer_field(
                font=(
                    Constants.DEFAULT_FONT_FAMILIY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                master=self.answers_frame,
            )

            # Configure the answer field's checkbutton widget
            answer_field["checkbutton"].configure(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILIY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
            )

            # Configure the answer field's entry widget
            answer_field["entry"].configure(
                font=(
                    Constants.DEFAULT_FONT_FAMILIY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
            )

            # Add the answer field to the list of fields
            self.answer_fields.append(answer_field)

            # Configure the answers frame's xth row to weight 0
            self.answers_frame.grid_rowconfigure(
                index=(1 + len(self.answer_fields)),
                weight=0,
            )

            # Place the answer field in the grid
            answer_field["root"].grid(
                column=0,
                padx=5,
                pady=5,
                row=(1 + len(self.answer_fields)),
                sticky=NSEW,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_add_answer_button_click' method from '{self.__class__.__name__}': {e}"
            )

            # Return None indicating an exception has occurred
            return None

    def on_question_type_select(self) -> None:
        """
        Handles the event when the question type field selection is changed.

        This method is called when the question type field selection is changed.
        It attempts to obtain the current value of the question type field and
        updates the question type instance variable. Depending on the selected
        question type, it creates the corresponding widgets.

        The question type field can have the following values:

            - "Multiple Choice"
            - "Open Answer"
            - "True/False"

        If the question type value is not one of the above, this method logs a
        warning message and returns early.

        If the question type value is "Multiple Choice", this method creates a
        button with the text "Add Answer" and places it within the scrolled
        frame. The button is configured to call the
        on_add_answer_button_click method when clicked.

        If the question type value is "Open Answer", this method creates an open
        answer field and places it within the scrolled frame.

        If the question type value is "True/False", this method creates a true
        false answer field and places it within the scrolled frame.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while running the SQL query.
        """
        try:
            # Attempt to obtain the current value of the question type field
            value: Optional[str] = self.question_type_field["getter"]()

            # Check if the value is an empty string or None
            if not value or value not in [
                "Multiple Choice",
                "Open Answer",
                "True/False",
            ]:
                # Log a warning message, if the question type is not supported
                self.logger.warning(
                    message=f"Unsupported question type '{value}'. This is likely a bug."
                )

                # Return early
                return None

            # Update the question type instance variable
            self.question_type = value

            # Clear the answers frame widget
            self.clear()

            # Clear the answer_fields list attribute
            self.answer_fields.clear()

            # Check if the question type value is any of "Multiple Choice", "Open Answer" or "True/False"
            if value == "Multiple Choice":
                # Configure the answers frame widget's 0th column to weight 0
                self.answers_frame.grid_columnconfigure(
                    index=0,
                    weight=1,
                )

                # Configure the answers frame widget's 1st row to weight 0
                self.answers_frame.grid_rowconfigure(
                    index=0,
                    weight=0,
                )

                # Create a button with the text "Add Answer"
                button: tkinter.Button = UIBuilder.get_button(
                    background=Constants.BLUE_GREY["700"],
                    command=self.on_add_answer_button_click,
                    font=(
                        Constants.DEFAULT_FONT_FAMILIY,
                        Constants.MEDIUM_FONT_SIZE,
                    ),
                    foreground=Constants.WHITE,
                    master=self.answers_frame,
                    relief=FLAT,
                    text="Add Answer",
                )

                # Place the button within the scrolled frame
                button.grid(
                    column=0,
                    padx=5,
                    pady=5,
                    row=0,
                )
            elif value == "Open Answer":
                # Configure the answers frame widget's 0th column to weight 1
                self.answers_frame.grid_columnconfigure(
                    index=0,
                    weight=1,
                )

                # Configure the answers frame widget's 1st row to weight 1
                self.answers_frame.grid_rowconfigure(
                    index=0,
                    weight=1,
                )

                # Create the open answer field widgets
                open_answer_field: Dict[str, Any] = UIBuilder.get_open_answer_field(
                    font=(
                        Constants.DEFAULT_FONT_FAMILIY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    master=self.answers_frame,
                )

                # Style the open answer field's "button" widget
                open_answer_field["button"].configure(
                    background=Constants.BLUE_GREY["700"],
                    font=(
                        Constants.DEFAULT_FONT_FAMILIY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    foreground=Constants.WHITE,
                    relief=FLAT,
                )

                # Style the open answer field's "container" frame widget
                open_answer_field["container"].configure(
                    background=Constants.BLUE_GREY["700"]
                )

                # Style the open answer field's "label" widget
                open_answer_field["label"].configure(
                    background=Constants.BLUE_GREY["700"],
                    font=(
                        Constants.DEFAULT_FONT_FAMILIY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    foreground=Constants.WHITE,
                )

                # Style the open answer field's "root" frame widget
                open_answer_field["root"].configure(
                    background=Constants.BLUE_GREY["700"]
                )

                # Place the open answer field's "root" frame widget within the answers frame widget
                open_answer_field["root"].grid(
                    column=0,
                    row=0,
                    sticky=NSEW,
                )

                # Append the open answer field to the answer fields list
                self.answer_fields.append(open_answer_field)
            elif value == "True/False":
                # Configure the answers frame widget's 0th column to weight 1
                self.answers_frame.grid_columnconfigure(
                    index=0,
                    weight=1,
                )

                # Configure the answers frame widget's 1st row to weight 1
                self.answers_frame.grid_rowconfigure(
                    index=0,
                    weight=1,
                )

                # Create the true/false answer field widgets
                true_false_answer_field: Dict[str, Any] = (
                    UIBuilder.get_true_false_answer_field(
                        master=self.answers_frame,
                    )
                )

                # Style the true/false answer field's "container" frame widget
                true_false_answer_field["container"].configure(
                    background=Constants.BLUE_GREY["700"]
                )

                # Style the true/false answer field's "false_radiobutton" widget
                true_false_answer_field["false_radiobutton"].configure(
                    background=Constants.BLUE_GREY["700"],
                    font=(
                        Constants.DEFAULT_FONT_FAMILIY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    foreground=Constants.WHITE,
                )

                # Style the true/false answer field's "label" widget
                true_false_answer_field["label"].configure(
                    background=Constants.BLUE_GREY["700"],
                    font=(
                        Constants.DEFAULT_FONT_FAMILIY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    foreground=Constants.WHITE,
                )

                # Style the true/false answer field's "root" frame widget
                true_false_answer_field["root"].configure(
                    background=Constants.BLUE_GREY["700"]
                )

                # Style the true/false answer field's "true_radiobutton" widget
                true_false_answer_field["true_radiobutton"].configure(
                    background=Constants.BLUE_GREY["700"],
                    font=(
                        Constants.DEFAULT_FONT_FAMILIY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    foreground=Constants.WHITE,
                )

                # Place the true/false answer field's "root" frame widget within the answers frame widget
                true_false_answer_field["root"].grid(
                    column=0,
                    row=0,
                    sticky=NSEW,
                )

                # Append the true/false answer field to the answer fields list
                self.answer_fields.append(true_false_answer_field)
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_question_type_select' method from '{self.__class__.__name__}': {e}"
            )

            # Raise the exception to the caller
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
            "question_text",  # The text of the question
            "question_type",  # The question type
            "stack",  # The stack the question belongs to
            "difficulty",  # The difficulty of the question
            "priority",  # The priority of the question
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
