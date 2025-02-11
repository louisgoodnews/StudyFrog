"""
Author: lodego
Date: 2025-02-11
"""

import tkinter

from tkinter.constants import *

from typing import *

from core.ui.ui_builder import UIBuilder

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous
from utils.navigation import NavigationHistoryItem, NavigationHistoryService
from utils.unified import UnifiedObjectManager


__all__: List[str] = ["EditUI"]


class EditUI(tkinter.Frame):
    """
    A class representing the edit menu user interface (UI) of the application.

    This class is responsible for initializing and configuring the layout of the
    edit menu UI, including setting up the main frames and populating them with
    respective widgets. It extends the tkinter.Frame class and utilizes various
    utility classes for managing navigation, logging, and other functionalities.

    Attributes:
        dispatcher (Dispatcher): The dispatcher instance.
        logger (Logger): The logger instance.
        navigation_item (NavigationHistoryItem): The navigation history item instance.
        navigation_service (NavigationHistoryService): The navigation history service instance.
        unified_manager (UnifiedObjectManager): The unified manager instance.
    """

    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        navigation_item: NavigationHistoryItem,
        navigation_service: NavigationHistoryService,
        unified_manager: UnifiedObjectManager,
    ) -> None:
        """
        Initializes a new instance of the EditUI class.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.
            master (tkinter.Misc): The parent widget.
            navigation_item (NavigationHistoryItem): The navigation history item instance.
            navigation_service (NavigationHistoryService): The navigation history service instance.
            unified_manager (UnifiedObjectManager): The unified manager instance.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            master=master,
            name="edit_ui",
        )

        # Initialize the logger instance
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed dispatcher instance in an instance variable
        self.dispatcher: Dispatcher = dispatcher

        # Store the passed navigation item instance in an instance variable
        self.navigation_item: NavigationHistoryItem = navigation_item

        # Store the passed navigation service instance in an instance variable
        self.navigation_service: NavigationHistoryService = navigation_service

        # Store the passed unified manager instance in an instance variable
        self.unified_manager: UnifiedObjectManager = unified_manager

        # Configure the grid
        self.configure_grid()

        # Edit the widgets
        self.edit_widgets()

        # Grid the edit menu widget in its master
        self.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

    def configure_grid(self) -> None:
        """
        Configures the grid of the edit menu widget.

        This method configures the grid of the edit menu widget by setting the
        weights of the columns and rows.

        Returns:
            None
        """

        # Configure the edit menu widget's 1st column to weight 1.
        # This means that the 1st column will stretch when the window is resized.
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the edit menu widget's 1st and 3rd row to weight 0.
        # This means that the 1st and 3rd row will not stretch when the window is resized.
        self.grid_rowconfigure(
            index=(
                0,
                2,
            ),
            weight=0,
        )

        # Configure the edit menu widget's 2nd row to weight 1.
        # This means that the 2nd row will stretch when the window is resized.
        self.grid_rowconfigure(
            index=1,
            weight=1,
        )

    def edit_widgets(self) -> None:
        """
        Edits and configures the main frames of the edit menu UI.

        This method initializes the top, center, and bottom frames within the
        edit menu UI, setting their layout configuration and invoking methods
        to populate each frame with its respective widgets.

        Args:
            None

        Returns:
            None
        """

        # Edit the "Top Frame" frame widget
        top_frame: tkinter.Frame = UIBuilder.get_frame(master=self)

        # Configure the "Top Frame" frame widget's 1st column to weight 1
        top_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the "TOp Frame" frame widget's 1st row to weight 1
        top_frame.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Place the "Top Frame" frame widget in the main window
        top_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Edit the "Center Frame" frame widget
        center_frame: tkinter.Frame = UIBuilder.get_frame(master=self)

        # Configure the "Center Frame" frame widget's 1st column to weight 1
        center_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the "Center Frame" frame widget's 1st row to weight 1
        center_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Place the "Center Frame" frame widget in the main window
        center_frame.grid(
            column=0,
            row=1,
            sticky=NSEW,
        )

        # Edit the "Bottom Frame" frame widget
        bottom_frame: tkinter.Frame = UIBuilder.get_frame(master=self)

        # Configure the "Bottom Frame" frame widget's 1st column to weight 1
        bottom_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the "Bottom Frame" frame widget's 1st row to weight 1
        bottom_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Place the "Bottom Frame" frame widget in the main window
        bottom_frame.grid(
            column=0,
            row=2,
            sticky=NSEW,
        )

        # Edit the "Bottom Frame" frame widgets
        self.edit_bottom_frame_widgets(master=bottom_frame)

        # Edit the "Center Frame" frame widgets
        self.edit_center_frame_widgets(master=center_frame)

        # Edit the "Top Frame" frame widgets
        self.edit_top_frame_widgets(master=top_frame)

    def edit_bottom_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Edits and configures the main widgets of the bottom frame.

        This method initializes the main widgets of the bottom frame within the
        edit menu UI, setting their layout configuration.

        Args:
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """
        pass

    def edit_center_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Edits and configures the main widgets of the center frame.

        This method initializes the main widgets of the center frame within the
        edit menu UI, setting their layout configuration.

        Args:
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """
        pass

    def edit_top_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Edits and configures the main widgets of the top frame.

        This method initializes the main widgets of the top frame within the
        edit menu UI, setting their layout configuration.

        Args:
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """
        pass
