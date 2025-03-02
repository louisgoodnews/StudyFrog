"""
Author: lodego
Date 2ß25-03-02
"""

import tkinter

from tkinter.constants import *

from tkinter import ttk

from typing import *

from core.difficulty import ImmutableDifficulty
from core.priority import ImmutablePriority
from core.stack import ImmutableStack, MutableStack

from core.ui.ui_builder import UIBuilder

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous
from utils.unified import UnifiedObjectManager


__all__: List[str] = ["StackViewForm"]


class StackViewForm(tkinter.Frame):
    """
    Represents the stack view form widget of the application.

    This class is responsible for initializing and configuring the layout of the
    stack view form widget, including setting up the main frames and populating them
    with respective widgets.

    Attributes:
        logger (Logger): The logger instance.
        stack (Union[ImmutableStack, MutableStack]): The stack instance.
        unified_manager (UnifiedObjectManager): The unified manager instance.
    """

    def __init__(
        self,
        master: tkinter.Misc,
        stack: Union[ImmutableStack, MutableStack],
        unified_manager: UnifiedObjectManager,
    ) -> None:
        """
        Initializes a new instance of the StackViewForm class.

        Args:
            master (tkinter.Misc): The parent widget.
            stack (Union[ImmutableStack, MutableStack]): The stack instance.
            unified_manager (UnifiedObjectManager): The unified manager instance.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(master=master)

        # Create an instance variable for the logger
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed stack instance in an instance variable
        self.stack: Union[ImmutableStack, MutableStack] = stack

        # Store the passed unified manager instance in an instance variable
        self.unified_manager: UnifiedObjectManager = unified_manager

        # Set the background color of the stack view form widget
        self.configure(background=Constants.BLUE_GREY["700"])

        # Configure the grid of the stack view form widget
        self.configure_grid()

        # Create the widgets of the stack view form
        self.create_widgets()

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
        top_frame: tkinter.Frame = UIBuilder.get_frame(master=self)

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
        center_frame: tkinter.Frame = UIBuilder.get_frame(master=self)

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
        bottom_frame: tkinter.Frame = UIBuilder.get_frame(master=self)

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
                    Constants.DEFAULT_FONT_FAMILIY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                label="Name*: ",
                master=master,
            )
        )

        # Style the name field's label widget
        self.name_field["label"].configure(
            background=Constants.BLUE_GREY["700"],
            foreground=Constants.WHITE,
        )

        # Style the name field's button widget
        self.name_field["button"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the name field's root widget
        self.name_field["root"].configure(background=Constants.BLUE_GREY["700"])

        # Set the name field's value to the stack's name
        self.name_field["setter"](value=self.stack.name)

        # Configure the name field
        self.name_field["entry"].configure(
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.MEDIUM_FONT_SIZE,
            ),
        )

        # Configure the name field
        self.name_field["label"].configure(
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
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
        left_frame: tkinter.Frame = UIBuilder.get_frame(
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
        right_frame: tkinter.Frame = UIBuilder.get_frame(
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

        # Create the primary attributes frame
        primary_attributes_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=tabbed_view["center_frame"],
        )

        # Configure the primary attributes frame's 0th column to weight 1
        primary_attributes_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the primary attributes frame's 0th row to weight 1
        primary_attributes_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Add the primary attributes frame to the tabbed view
        tabbed_view["adder"](
            label="Primary Attributes",
            widget=primary_attributes_frame,
        )

        # Style the primary attributes button
        tabbed_view["primary attributes_button"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Create the description field
        self.description_field: Optional[Dict[str, Any]] = (
            UIBuilder.get_multi_line_text_field(
                font=(
                    Constants.DEFAULT_FONT_FAMILIY,
                    Constants.MEDIUM_FONT_SIZE,
                ),
                label="Description: ",
                master=primary_attributes_frame,
            )
        )

        # Style the description field's button widget
        self.description_field["button"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the description field's label widget
        self.description_field["label"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Style the description field's root widget
        self.description_field["root"].configure(background=Constants.BLUE_GREY["700"])

        # Configure the description field's label widget
        self.description_field["setter"](value=self.stack.description)

        # Place the description field within the primary attributes frame
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
        tabbed_view["secondary attributes_button"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
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
                Constants.DEFAULT_FONT_FAMILIY,
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
                Constants.DEFAULT_FONT_FAMILIY,
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
                Constants.DEFAULT_FONT_FAMILIY,
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
                Constants.DEFAULT_FONT_FAMILIY,
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
                Constants.DEFAULT_FONT_FAMILIY,
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
                Constants.DEFAULT_FONT_FAMILIY,
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
                Constants.DEFAULT_FONT_FAMILIY,
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
                Constants.DEFAULT_FONT_FAMILIY,
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
            UIBuilder.get_combobox_select_field(
                font=(
                    Constants.DEFAULT_FONT_FAMILIY,
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
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the difficulty field's label widget
        self.difficulty_field["label"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
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
            UIBuilder.get_combobox_select_field(
                font=(
                    Constants.DEFAULT_FONT_FAMILIY,
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
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the priority field's label widget
        self.priority_field["label"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
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
