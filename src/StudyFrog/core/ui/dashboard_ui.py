"""
Author: lodego
Date: 2025-02-08
"""

import tkinter

import uuid

from tkinter.constants import *

from typing import *

from core.ui.ui_builder import UIBuilder

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.logger import Logger
from utils.navigation import NavigationItem, NavigationService


__all__: List[str] = ["DashboardUI"]


class DashboardUI(tkinter.Frame):
    """
    A class representing the dashboard user interface (UI) of the application.

    Atrributes:
        dispatcher (Dispatcher): The dispatcher instance.
        logger (Logger): The logger instance.
    """

    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        navigation_item: NavigationItem,
        navigation_service: NavigationService,
    ) -> None:
        """
        Initializes a new instance of the DashboardUI class.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.
            master (tkinter.Misc): The parent widget.
            navigation_item (NavigationItem): The navigation item instance.
            navigation_service (NavigationService): The navigation service instance.

        Returns:
            None
        """
        # Call the parent class constructor
        super().__init__(master=master)

        # Initialize the logger instance
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed dispatcher instance in an instance variable
        self.dispatcher: Dispatcher = dispatcher

        # Store the passed navigation item instance in an instance variable
        self.navigation_item: NavigationItem = navigation_item

        # Store the passed navigation service instance in an instance variable
        self.navigation_service: NavigationService = navigation_service

        # Configure the dashboard widget's 1st column to weight 1
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the dashboard widget's 1st and 3rd row to weight 0
        self.grid_rowconfigure(
            index=(
                0,
                2,
            ),
            weight=0,
        )

        # Configure the dashboard widget's 2nd row to weight 1
        self.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Create the widgets
        self.create_widgets()

    def create_widgets(self) -> None:
        """
        Creates and configures the main frames of the dashboard UI.

        This method initializes the top, center, and bottom frames within the
        dashboard UI, setting their layout configuration and invoking methods
        to populate each frame with its respective widgets.

        Args:
            None

        Returns:
            None
        """

        # Create the "Top Frame" frame widget
        top_frame: tkinter.Frame = UIBuilder.get_frame(master=self)

        # Configure the "Top Frame" frame widget's 1st column to weight 1
        top_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the "TOp Frame" frame widget's 1st row to weight 1
        main_frame.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Place the "Top Frame" frame widget in the main window
        top_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create the "Center Frame" frame widget
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

        # Create the "Bottom Frame" frame widget
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

        # Create the "Bottom Frame" frame widgets
        self.create_bottom_frame_widgets(master=bottom_frame)

        # Create the "Center Frame" frame widgets
        self.create_center_frame_widgets(master=center_frame)

        # Create the "Top Frame" frame widgets
        self.create_top_frame_widgets(master=top_frame)

    def create_bottom_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Creates and configures the main widgets of the bottom frame.

        This method initializes the main widgets of the bottom frame within the
        dashboard UI, setting their layout configuration.

        Args:
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """
        pass

    def create_center_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Creates and configures the main widgets of the center frame.

        This method initializes the main widgets of the center frame within the
        dashboard UI, setting their layout configuration.

        Args:
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """
        pass

    def create_top_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Creates and configures the main widgets of the top frame.

        This method initializes the main widgets of the top frame within the
        dashboard UI, setting their layout configuration.

        Args:
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """
        pass
