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
from utils.navigation import NavigationHistoryItem, NavigationHistoryService
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
    ) -> None:
        """
        Initializes a new instance of the StackCreateForm class.

        Args:
            master (tkinter.Misc): The parent widget.
        """

        # Call the parent class constructor
        super().__init__(master=master)

        # Create a logger instance
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

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
            index=0,
            weight=0,
        )

        # Configure the stack create form widget's 2nd row to weight 0.
        self.grid_rowconfigure(
            index=1,
            weight=0,
        )

        # Configure the stack create form widget's 3rd row to weight 1.
        self.grid_rowconfigure(
            index=2,
            weight=0,
        )

    def create_widgets(self) -> None:
        """
        Creates and configures the main widgets of the stack create form widget.

        This method creates and configures the main widgets of the stack create form
        widget. The main widgets are: a single-line text field for the stack name
        and a multi-line text field for the stack description.

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
            row=2,
            sticky=NSEW,
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
            "contents": [],
            "created_at": Miscellaneous.get_current_datetime(),
            "customfield_values": [],
            "description": "",
            "name": "",
            "updated_at": Miscellaneous.get_current_datetime(),
            "uuid": Miscellaneous.get_uuid(),
        }

        # Get the value of the stack name from the single-line text field
        result["name"] = self.name["getter"]()

        # Get the value of the stack description from the multi-line text field
        result["description"] = self.description["getter"]()

        # Return the result dictionary
        return result
