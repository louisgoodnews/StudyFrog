"""
Author: lodego
Date: 2025-02-08
"""

import tkinter

from tkinter import ttk

from tkinter.constants import *

from typing import *

from ui.topbar import TopBar

from utils.ui_builder import UIBuilder
from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.logger import Logger
from utils.navigation import NavigationService


__all__: List[str] = ["MainUI"]


class MainUI(tkinter.Tk):
    """
    The main user interface (UI) of the StudyFrog application.

    Attributes:
        dispatcher (Dispatcher): The dispatcher instance.
        logger (Logger): The logger instance.
    """

    def __init__(
        self,
        dispatcher: Dispatcher,
        navigation_service: NavigationService,
    ) -> None:
        """
        Initializes a new instance of the MainUI class.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__()

        # Initialize a logger instance
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed dispatcher instance in an instance variable
        self.dispatcher: Dispatcher = dispatcher

        # Store the passed navigation service instance in an instance variable
        self.navigation_service: NavigationService = navigation_service

        # Configure the MainUI widget's 1st column to weight 1
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the MainUI widget's 1st and 3rd row to weight 0
        self.grid_rowconfigure(
            index=(
                0,
                2,
            ),
            weight=0,
        )

        # Configure the MainUI widget's 1st row to weight 1
        self.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Set the window geometry
        self.wm_geometry(newGeometry=Constants.DEFAULT_GEOMETRY)

        # Register a handler for the "WM_DELETE_WINDOW" event
        # self.wm_protocol(
        #   name="WM_DELETE_WINDOW",
        #   func=lambda: dispatcher.dispatch(
        #       event=Events.REQUEST_APPLICATION_STOP,
        #       namespace=Constants.GLOBAL_NAMESPACE,
        #   ),
        # )

        # Set the window title
        self.wm_title(string=Constants.APPLICATION_NAME)

        # Create the "Top Frame" frame widget
        self._top_frame: tkinter.Frame = UIBuilder.get_frame(
            height=25,
            master=self,
        )

        # Configure the "Top Frame" frame widget's 1st column to weight 1
        self._top_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the "Top Frame" frame widget's 1st row to weight 1
        self._top_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create the "Center Frame" frame widget
        self._center_frame: tkinter.Frame = UIBuilder.get_frame(master=self)

        # Configure the "Center Frame" frame widget's 1st column to weight 1
        self._center_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Configure the "Center Frame" frame widget's 1st column to weight 1
        self._center_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Create the "Bottom Frame" frame widget
        self._bottom_frame: tkinter.Frame = UIBuilder.get_frame(
            height=25,
            master=self,
        )

        # Configure the "Bottom Frame" frame widget's 1st column to weight 1
        self._bottom_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Grid the "Top Frame" frame widget in the MainUI widget
        self._top_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Grid the "Center Frame" frame widget in the MainUI widget
        self._center_frame.grid(
            column=0,
            row=1,
            sticky=NSEW,
        )

        # Grid the "Bottom Frame" frame widget in the MainUI widget
        self._bottom_frame.grid(
            column=0,
            row=2,
            sticky=NSEW,
        )

        # Create the "TopBar" topbar widget
        self.topbar: TopBar = TopBar(
            dispatcher=self.dispatcher,
            master=self._top_frame,
        )

        # Grid the "TopBar" widget in the "Top Frame" frame widget
        self.topbar.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

    @property
    def top_frame(self) -> tkinter.Frame:
        """
        Returns the "Top Frame" frame widget of the MainUI widget.

        The "Top Frame" frame widget is the topmost frame widget in the MainUI widget.

        Returns:
            tkinter.Frame: The "Top Frame" frame widget.
        """

        # Return the "Top Frame" frame widget
        return self._top_frame

    @property
    def center_frame(self) -> tkinter.Frame:
        """
        Returns the "Center Frame" frame widget of the MainUI widget.

        The "Center Frame" frame widget is the middle frame widget in the MainUI widget.

        Returns:
            tkinter.Frame: The "Center Frame" frame widget.
        """

        # Return the "Center Frame" frame widget
        return self._center_frame

    @property
    def bottom_frame(self) -> tkinter.Frame:
        """
        Returns the "Bottom Frame" frame widget of the MainUI widget.

        The "Bottom Frame" frame widget is the bottommost frame widget in the MainUI widget.

        Returns:
            tkinter.Frame: The "Bottom Frame" frame widget.
        """

        # Return the "Bottom Frame" frame widget
        return self._bottom_frame

    def clear(
        self,
        name: str,
    ) -> None:
        """
        Clears the given widget.

        Args:
            name (str): The name of the widget to clear.

        Returns:
            None
        """

        # Cehck if the given widget exists and is an instance of tkinter.Misc
        if hasattr(
            self,
            name,
        ) and isinstance(
            getattr(
                self,
                name,
            ),
            tkinter.Misc,
        ):
            # Iterate over the children of the widget
            for child in getattr(
                self,
                name,
            ).winfo_children():
                # Destroy each child widget
                child.destroy()
