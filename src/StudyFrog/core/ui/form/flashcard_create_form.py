"""
Author: lodego
Date: 2025-02-13
"""

import tkinter

from tkinter.constants import *
from tkinter import ttk
from typing import *

from core.ui.fields.select_fields import ComboboxField
from core.ui.fields.string_fields import MultiLineTextField

from core.ui.frames.frames import ScrolledFrame, TabbedFrame

from core.ui.ui_builder import UIBuilder

from core.stack import ImmutableStack

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
        self.logger: Final[Logger] = Logger.get_logger(name=self.__class__.__name__)

        # Store the dispatcher instance in an instance variable
        self.dispatcher: Dispatcher = dispatcher

        # Initialize the form dictionary instance variable as an empty dictionary
        self.form: Final[Dict[str, Any]] = {
            "object_data": {},
            "related_objects": {},
        }

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

    def _on_field_change(
        self,
        label: str,
        value: Any,
    ) -> None:
        """ """

        # Obtain the inner key as a snake case version of the passed label
        inner_key: str = Miscellaneous.any_to_snake(string=label.replace("*: ", ""))

        # Determine the outer key based on the inner key
        outer_key: str = "object_data" if inner_key != "stack" else "related_objects"

        # Update the value of the label in the form with the passed value
        self.form[outer_key][
            Miscellaneous.any_to_snake(string=label.replace("*: ", ""))
        ] = value

        # TODO:
        #   - implement check for 'front_text' field
        #   - if any other flashcard with an identical 'front_text' value exists, then there must be a warning for the user

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

        validation: Tuple[bool, List[str]] = self.validate_required_fields(
            object_data=object_data
        )

        # Validate the required fields using the helper method
        if validation[0]:
            # Return True if validation is successful
            return True

        # Show a dialog informing the user to fill all required fields
        okay: Optional[Dict[str, Any]] = UIBuilder.get_okay(
            dispatcher=self.dispatcher,
            message=f"Please fill in all required fields: {', '.join(validation[1])}",
            title="Required fields are missing.",
        )

        # Style the okay dialog's "Root" toplevel widget
        okay["root"].configure(background=Constants.BLUE_GREY["700"])

        # Style the okay dialog's "Button" button widget
        okay["button"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the okay dialog's "Message Label" label widget
        okay["message_label"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Style the okay dialog's "Title Label" label widget
        okay["title_label"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
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

    def create_core_attributes_widgets(
        self,
        master: TabbedFrame,
    ) -> tkinter.Frame:
        """ """

        # Create the scrolled frame widgets
        scrolled_frame: ScrolledFrame = ScrolledFrame(master=master)

        # Style the scrolled frame widget
        scrolled_frame.configure(background=Constants.BLUE_GREY["700"])

        # Style the scrolled frame "canvas" widget
        scrolled_frame.configure_canvas(background=Constants.BLUE_GREY["700"])

        # Style the scrolled frame "container frame" widget
        scrolled_frame.configure_container(background=Constants.BLUE_GREY["700"])

        # Create a combobox widget to select a stack
        self.stack_field: ComboboxField = ComboboxField(
            label="Stack*: ",
            master=scrolled_frame,
            on_change_callback=self._on_field_change,
            values=[stack.name for stack in self.unified_manager.get_all_stacks()],
        )

        # Style the stack field "Root" frame widget
        self.stack_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the stack field "Button" button widget
        self.stack_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the stack field "Combobox" combobox widget
        self.stack_field.configure_combobox(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            state="readonly",
        )

        # Style the stack field "Label" label widget
        self.stack_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Place the stack field in the grid
        self.stack_field.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a multi-line text field for the front text of the flashcard
        self.front_field: MultiLineTextField = MultiLineTextField(
            label="Front Text*: ",
            master=scrolled_frame,
            on_change_callback=self._on_field_change,
        )

        # Style the front field "Root" frame widget
        self.front_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the front field "Button" button widget
        self.front_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the front field "Label" label widget
        self.front_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the back field "Text" text widget
        self.front_field.configure_text(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Place the front field in the grid
        self.front_field.grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )

        # Create a multi-line text field for the back text of the flashcard
        self.back_field: MultiLineTextField = MultiLineTextField(
            label="Back Text*: ",
            master=scrolled_frame,
            on_change_callback=self._on_field_change,
        )

        # Style the back field "Root" frame widget
        self.back_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the back field "Button" button widget
        self.back_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the back field "Label" label widget
        self.back_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the back field "Text" text widget
        self.back_field.configure_text(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Place the back field in the grid
        self.back_field.grid(
            column=0,
            padx=5,
            pady=5,
            row=2,
            sticky=NSEW,
        )

        # Return the scrolled frame
        
        return scrolled_frame

    def create_secondary_attributes_widgets(
        self,
        master: tkinter.Misc,
    ) -> tkinter.Frame:
        """ """

        # Create the scrolled frame widgets
        scrolled_frame: ScrolledFrame = ScrolledFrame(master=master)

        # Style the scrolled frame widget
        scrolled_frame.configure(background=Constants.BLUE_GREY["700"])

        # Style the scrolled frame "canvas" widget
        scrolled_frame.configure_canvas(background=Constants.BLUE_GREY["700"])

        # Style the scrolled frame "container frame" widget
        scrolled_frame.configure_container(background=Constants.BLUE_GREY["700"])

        # Return the scrolled frame
        return scrolled_frame

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
                Constants.DEFAULT_FONT_FAMILY,
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

        # Attempt to create the tabbed frame widgets
        tabbed_frame: TabbedFrame = TabbedFrame(
            column=0,
            master=self,
            row=2,
        )

        # Style the tabbed frame widget
        tabbed_frame.configure(background=Constants.BLUE_GREY["700"])

        # Style the tabbed frame widget's "container frame" frame widget
        tabbed_frame.configure_container(background=Constants.BLUE_GREY["700"])

        # Style the tabbed frame widget's "top frame" frame widget
        tabbed_frame.configure_top_frame(background=Constants.BLUE_GREY["700"])

        # Add the scrolled frame widget to the tabbed frame
        tabbed_frame.add(
            label="Core attributes",
            widget=self.create_core_attributes_widgets(master=tabbed_frame),
        )

        # Add the scrolled frame widget to the tabbed frame
        tabbed_frame.add(
            label="Secondary attributes",
            widget=self.create_secondary_attributes_widgets(master=tabbed_frame),
        )

        # Style the "core attributes" button
        tabbed_frame.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            name="core_attributes",
            relief=FLAT,
        )

        # Style the "secondary attributes" button
        tabbed_frame.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            name="secondary_attributes",
            relief=FLAT,
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

            # Set the 'back text' word count for the flashcard
            self.form["object_data"]["back_word_count"] = len(
                self.form["object_data"]["back_text"].split()
            )

            # Copy the difficulty of the flashcard from the stack
            self.form["object_data"]["difficulty"] = stack.difficulty

            # Set the familiarity of the flashcard to 0.0
            self.form["object_data"]["familiarity"] = 0.0

            # Set the 'front text' word count for the flashcard
            self.form["object_data"]["front_word_count"] = len(
                self.form["object_data"]["back_text"].split()
            )

            # Copy the priority of the flashcard from the stack
            self.form["object_data"]["difficulty"] = stack.priority

            # Set the total word count for the flashcard
            self.form["object_data"]["total_word_count"] = (
                self.form["object_data"]["front_word_count"]
                + self.form["object_data"]["back_word_count"]
            )

            # Add the stack to the 'related object' nested dictionary
            self.form["related_object"]["stack"] = stack

            # Return the result dictionary
            return self.form
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
    ) -> Tuple[bool, List[str]]:
        """
        Validates the object data to ensure all required fields have been provided.

        Args:
            object_data (Dict[str, Any]): The object data to validate.

        Returns:
            bool: True if all required fields have been provided, False otherwise.
            List[str]: A list of missing fields if the validation fails.
        """

        # Define the required fields
        required_fields: List[str] = [
            "back_text",  # The back side of the flashcard
            "difficulty",  # The difficulty of the flashcard
            "front_text",  # The front side of the flashcard
            "priority",  # The priority of the flashcard
        ]

        missing_fields: List[str] = []

        checks: List[bool] = []

        # Iterate over all required fields
        for required_field in required_fields:
            # Check if the required field is in the object data
            if required_field in object_data.get(
                "object_data",
                {},
            ):
                # If the field is present, append True to the check list
                checks.append(True)
            # Check if the required field is in the related objects
            elif required_field in object_data.get(
                "related_objects",
                {},
            ):
                # If the field is present, append True to the check list
                checks.append(True)
            else:
                # If the field is not present, append the field to the missing fields
                # list and append False to the check list
                missing_fields.append(required_field)
                checks.append(False)

        # Return the result
        return (
            all(checks),
            missing_fields,
        )
