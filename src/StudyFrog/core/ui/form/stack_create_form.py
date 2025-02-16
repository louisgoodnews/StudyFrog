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


__all__: List[str] = ["StackCreateForm"]


class StackCreateForm(tkinter.Frame):
    """
    A class representing the stack create form widget of the application.

    This class is responsible for initializing and configuring the layout of the
    stack create form widget, including setting up the main frames and populating them
    with respective widgets. It also provides methods for retrieving the values from
    the form fields.

    Attributes:
        logger (Logger): The logger instance.
        name (Dict[str, Any]): The single-line text field for the stack name.
        description (Dict[str, Any]): The multi-line text field for the stack description.
    """

    def __init__(
        self,
        master: tkinter.Misc,
        unified_manager: UnifiedObjectManager,
    ) -> None:
        """
        Initializes a new instance of the StackCreateForm class.

        Args:
            master (tkinter.Misc): The parent widget.
            unified_manager (UnifiedObjectManager): The unified object manager instance.
        """

        # Call the parent class constructor
        super().__init__(master=master)

        # Create a logger instance
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

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

        # Configure the stack create form widget's 1st row to weight 0.
        self.grid_rowconfigure(
            index=tuple(range(6)),
            weight=0,
        )

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

        # Create a single-line text field for the stack name.
        self.name: Dict[str, Any] = UIBuilder.get_single_line_text_field(
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            label="Name* : ",
            master=self,
        )

        self.name["button"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        self.name["label"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
        )

        self.name["root"].configure(background=Constants.BLUE_GREY["700"])

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
            master=self,
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
            master=self,
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
            master=self,
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
            master=self,
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
                "contents": [],
                "created_at": Miscellaneous.get_current_datetime(),
                "custom_field_values": [],
                "description": "",
                "last_viewed_at": Miscellaneous.get_current_datetime(),
                "name": "",
                "updated_at": Miscellaneous.get_current_datetime(),
                "uuid": Miscellaneous.get_uuid(),
            },
            "related_objects": {},
        }

        # Get the value of the stack name from the single-line text field
        result["object_data"]["name"] = self.name["getter"]()

        # Get the value of the stack description from the multi-line text field
        result["object_data"]["description"] = self.description["getter"]()

        # Get the value of the due by date from the date entry widget
        result["object_data"]["due_by"] = self.due_by["getter"]()

        # Get the difficulty from the difficulty field
        result["related_objects"]["difficulty"] = (
            self.unified_manager.get_difficulty_by(
                field="name",
                value=self.difficulty_field["getter"](),
            )
        )

        # Get the value of the difficulty from the difficulty field
        result["object_data"]["difficulty"] = result["related_objects"]["difficulty"][
            "id"
        ]

        # Get the priority from the priority field
        result["related_objects"]["priority"] = self.unified_manager.get_priority_by(
            field="name",
            value=self.priority_field["getter"](),
        )

        # Get the value of the priority from the priority field
        result["object_data"]["priority"] = result["related_objects"]["priority"]["id"]

        # Return the result dictionary
        return result
