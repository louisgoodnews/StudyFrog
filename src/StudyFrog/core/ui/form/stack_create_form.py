"""
Author: lodego
Date: 2025-02-13
"""

import tkinter
import traceback

from tkinter.constants import *

from tkinter import ttk

from typing import *

from core.stack import ImmutableStack

from core.ui.ui_builder import UIBuilder

from core.ui.fields.datetime_fields import DateSelectField

from core.ui.fields.select_fields import ComboboxField

from core.ui.fields.string_fields import MultiLineTextField, SingleLineTextField

from core.ui.frames.frames import ScrolledFrame, TabbedFrame

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

        # Initialize the form dictionary instance variable as an empty dictionary
        self.form: Dict[str, Any] = {
            "object_data": {
                "contents": [],
                "custom_field_values": [],
                "descendants": [],
                "tags": [],
            },
            "related_objects": {},
        }

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

    def _on_field_change(
        self,
        labeL: str,
        value: Optional[Any] = None,
    ) -> None:
        try:
            self.form[labeL] = value
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run '_on_field_change' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

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

    def create_core_attributes_widgets(
        self,
        master: tkinter.Misc,
    ) -> tkinter.Frame:
        """ """

        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create the scrolled frame widgets
        scrolled_frame: ScrolledFrame = ScrolledFrame(master=master)

        scrolled_frame.container.grid_columnconfigure(
            index=0,
            weight=1,
        )

        scrolled_frame.container.grid_rowconfigure(
            index=0,
            weight=1,
        )

        scrolled_frame.container.grid_rowconfigure(
            index=1,
            weight=1,
        )

        scrolled_frame.container.grid_rowconfigure(
            index=2,
            weight=1,
        )

        scrolled_frame.container.grid_rowconfigure(
            index=3,
            weight=1,
        )

        scrolled_frame.container.grid_rowconfigure(
            index=4,
            weight=1,
        )

        scrolled_frame.container.grid_rowconfigure(
            index=5,
            weight=1,
        )

        # Style the scrolled frame widget
        scrolled_frame.configure(background=Constants.BLUE_GREY["700"])

        # Style the scrolled frame "canvas" widget
        scrolled_frame.configure_canvas(background=Constants.BLUE_GREY["700"])

        # Style the scrolled frame "container frame" widget
        scrolled_frame.configure_container(background=Constants.BLUE_GREY["700"])

        # Create a combobox widget to select a stack
        self.ancestor_stack_field: ComboboxField = ComboboxField(
            label="Ancestor Stack: ",
            master=scrolled_frame.container,
            on_change_callback=self._on_field_change,
            readonly=True,
            values=[stack.name for stack in self.unified_manager.get_all_stacks()],
        )

        # Style the stack field "Root" frame widget
        self.ancestor_stack_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the stack field "Button" button widget
        self.ancestor_stack_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the stack field "Label" label widget
        self.ancestor_stack_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Place the stack field in the grid
        self.ancestor_stack_field.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a single-line text field for the stack name.
        self.name: SingleLineTextField = SingleLineTextField(
            label="Name* : ",
            master=scrolled_frame.container,
            on_change_callback=self._on_field_change,
        )

        # Style the single-line text field "Root" frame widget
        self.name.configure(background=Constants.BLUE_GREY["700"])

        # Style the single-line text field "Button" button widget
        self.name.configure_button(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the single-line text field "Label" widget
        self.name.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Focus the name entry field
        self.name.entry.focus_set()

        # Place the single-line text field in the grid.
        self.name.grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )

        # Create a stack field for the difficulty
        self.difficulty_field: ComboboxField = ComboboxField(
            label="Difficulty* : ",
            master=scrolled_frame.container,
            on_change_callback=self._on_field_change,
            readonly=True,
            value=Constants.MEDIUM.capitalize(),
            values=[
                difficulty.name
                for difficulty in self.unified_manager.get_all_difficulties()
            ],
        )

        # Style the stack field "Root" frame widget
        self.difficulty_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the stack field "Button" button widget
        self.difficulty_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the stack field "Label" label widget
        self.difficulty_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Place the stack field in the grid
        self.difficulty_field.grid(
            column=0,
            padx=5,
            pady=5,
            row=2,
            sticky=NSEW,
        )

        # Create a stack field for the priority
        self.priority_field: ComboboxField = ComboboxField(
            label="Priority* : ",
            master=scrolled_frame.container,
            readonly=True,
            value=Constants.MEDIUM.capitalize(),
            values=[
                priority.name for priority in self.unified_manager.get_all_priorities()
            ],
        )

        # Style the stack field "Root" frame widget
        self.priority_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the stack field "Button" button widget
        self.priority_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the stack field "Label" label widget
        self.priority_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Place the stack field in the grid
        self.priority_field.grid(
            column=0,
            padx=5,
            pady=5,
            row=3,
            sticky=NSEW,
        )

        # Create a multi-line text field for the stack description.
        self.description: MultiLineTextField = MultiLineTextField(
            label="Description: ",
            master=scrolled_frame.container,
            on_change_callback=self._on_field_change,
        )

        self.description.configure(background=Constants.BLUE_GREY["700"])

        self.description.configure_button(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        self.description.configure_label(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
        )

        self.description.configure_text(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            )
        )

        # Place the multi-line text field in the grid.
        self.description.grid(
            column=0,
            padx=5,
            pady=5,
            row=4,
            sticky=NSEW,
        )

        # Create a date entry widget for the due by date
        self.due_by: DateSelectField = DateSelectField(
            label="Due by*: ",
            master=scrolled_frame.container,
            on_change_callback=self._on_field_change,
            value=Miscellaneous.get_date_increment(increment=30),
        )

        self.due_by.configure(background=Constants.BLUE_GREY["700"])

        self.due_by.configure_clear_button(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        self.due_by.configure_select_button(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        self.due_by.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Place the date entry widget in the grid.
        self.due_by.grid(
            column=0,
            padx=5,
            pady=5,
            row=5,
            sticky=NSEW,
        )

        # Return the scrolled frame
        return scrolled_frame

    def create_secondary_attributes_widgets(
        self,
        master: tkinter.Misc,
    ) -> tkinter.Frame:
        """ """

        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

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
        Creates and configures the main widgets of the stack create form widget.

        This method creates and configures the main widgets of the stack create form
        widget.

        Returns:
            None
        """

        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        self.grid_rowconfigure(
            index=0,
            weight=0,
        )

        self.grid_rowconfigure(
            index=1,
            weight=0,
        )

        self.grid_rowconfigure(
            index=2,
            weight=1,
        )

        # Create a label widget to display instructions
        instruction_label: tkinter.Label = UIBuilder.get_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
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
        tabbed_view: TabbedFrame = TabbedFrame(
            column=0,
            master=self,
            row=2,
        )

        # Style the tabbed_view "Root" frame widget
        tabbed_view.configure(background=Constants.BLUE_GREY["700"])

        # Style the tabbed_view "container frame" frame widget
        tabbed_view.configure_container(background=Constants.BLUE_GREY["700"])

        # Style the tabbed_view "top frame" frame widget
        tabbed_view.configure_top_frame(background=Constants.BLUE_GREY["700"])

        # Add the scrolled frame to the tabbed_view widget's children
        tabbed_view.add(
            label="Core Attributes",
            widget=self.create_core_attributes_widgets(master=tabbed_view),
        )

        # Add the scrolled frame to the tabbed_view widget's children
        tabbed_view.add(
            label="Secondary Attributes",
            widget=self.create_secondary_attributes_widgets(master=tabbed_view),
        )

        # Style the scrolled frame "Core attributes" button widget
        tabbed_view.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            name="Core attributes",
            relief=FLAT,
        )

        # Style the scrolled frame "Secondary attributes" button widget
        tabbed_view.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            name="Secondary attributes",
            relief=FLAT,
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
        result["object_data"]["name"] = self.name.get()

        # Get the value of the stack description from the multi-line text field
        result["object_data"]["description"] = self.description.get() or ""

        # Get the value of the due by date from the date entry widget
        result["object_data"]["due_by"] = self.due_by.get()

        # Get the difficulty from the difficulty field
        result["related_objects"]["ancestor_stack"] = self.unified_manager.get_stack_by(
            field="name",
            value=self.ancestor_stack_field["getter"](),
        )

        # Get the difficulty from the difficulty field
        result["related_objects"]["difficulty"] = (
            self.unified_manager.get_difficulty_by(
                field="name",
                value=self.difficulty_field.get(),
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
