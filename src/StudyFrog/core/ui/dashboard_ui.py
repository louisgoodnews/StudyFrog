"""
Author: lodego
Date: 2025-02-08
"""

import tkinter

from tkinter.constants import *

from tkinter import ttk

from typing import *

from core.setting import SettingService

from core.ui.ui_builder import UIBuilder

from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherNotification
from utils.events import Events
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous
from utils.navigation import NavigationHistoryItem, NavigationHistoryService
from utils.unified import UnifiedObjectManager


__all__: List[str] = ["DashboardUI"]


class DashboardUI(tkinter.Frame):
    """
    A class representing the dashboard user interface (UI) of the application.

    Atrributes:
        dispatcher (Dispatcher): The dispatcher instance.
        logger (Logger): The logger instance.
        navigation_item (NavigationHistoryItem): The navigation history item instance.
        navigation_service (NavigationHistoryService): The navigation history service instance.
        setting_service (SettingService): The setting service instance.
        unified_manager (UnifiedObjectManager): The unified manager instance.
    """

    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        navigation_item: NavigationHistoryItem,
        navigation_service: NavigationHistoryService,
        setting_service: SettingService,
        unified_manager: UnifiedObjectManager,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the DashboardUI class.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.
            master (tkinter.Misc): The parent widget.
            navigation_item (NavigationHistoryItem): The navigation history item instance.
            navigation_service (NavigationHistoryService): The navigation history service instance.
            setting_service (SettingService): The setting service instance.
            unified_manager (UnifiedObjectManager): The unified manager instance.
            **kwargs: Any additional keyword arguments.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            master=master,
            name="dashboard_ui",
        )

        # Initialize the logger instance
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed dispatcher instance in an instance variable
        self.dispatcher: Dispatcher = dispatcher

        # Store the passed navigation item instance in an instance variable
        self.navigation_item: NavigationHistoryItem = navigation_item

        # Store the passed navigation service instance in an instance variable
        self.navigation_service: NavigationHistoryService = navigation_service

        # Store the passed setting service instance in an instance variable
        self.setting_service: SettingService = setting_service

        # Store the passed unified manager instance in an instance variable
        self.unified_manager: UnifiedObjectManager = unified_manager

        # Configure the DasboardUI's background to be grey
        self.configure(background=Constants.BLUE_GREY["700"])

        # Configure the grid
        self.configure_grid()

        # Create the widgets
        self.create_widgets()

        # Grid the dashboard widget in it's master
        self.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Debug function to look up the stacks
        self.lookup_stacks()

    def configure_grid(self) -> None:
        """
        Configures the grid of the dashboard widget.

        This method configures the grid of the dashboard widget by setting the
        weights of the columns and rows.

        Returns:
            None
        """

        # Configure the dashboard widget's 1st column to weight 1.
        # This means that the 1st column will stretch when the window is resized.
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the dashboard widget's 1st and 3rd row to weight 0.
        # This means that the 1st and 3rd row will not stretch when the window is resized.
        self.grid_rowconfigure(
            index=(
                0,
                2,
            ),
            weight=0,
        )

        # Configure the dashboard widget's 2nd row to weight 1.
        # This means that the 2nd row will stretch when the window is resized.
        self.grid_rowconfigure(
            index=1,
            weight=1,
        )

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
        top_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

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

        # Create the "Center Frame" frame widget
        center_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

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
        bottom_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

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

        # Configure the top frame widget's 1st column to weight 0
        master.grid_columnconfigure(
            index=0,
            weight=0,
        )

        # Configure the top frame widget's 2nd column to weight 1
        master.grid_columnconfigure(
            index=1,
            weight=1,
        )

        # Configure the top frame widget's 1st row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create a left frame within the master frame
        left_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=master,
        )

        # Configure the left frame widget's 1st column to weight 1
        left_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the left frame widget's 1st, 2nd and 3rd row to weight 0
        left_frame.grid_rowconfigure(
            index=(
                0,
                1,
                2,
            ),
            weight=0,
        )

        # Place the left frame widget in the master frame
        left_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create a new button within the left frame
        new_button: tkinter.Button = UIBuilder.get_button(
            background=Constants.BLUE_GREY["700"],
            command=lambda: self.dispatcher.dispatch(
                direction="forward",
                event=Events.REQUEST_VALIDATE_NAVIGATION,
                master=UIBuilder.get_toplevel(),
                namespace=Constants.GLOBAL_NAMESPACE,
                source="dashboard_ui",
                target="create_ui",
                type="stack",
            ),
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=left_frame,
            relief=FLAT,
            text="➕ New Stack",
        )

        # Place the new button within the left frame
        new_button.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
        )

        # Create a recent button within the left frame
        recent_button: tkinter.Button = UIBuilder.get_button(
            background=Constants.BLUE_GREY["700"],
            command=lambda: self.dispatcher.dispatch(
                direction="forward",
                event=Events.REQUEST_VALIDATE_NAVIGATION,
                master=UIBuilder.get_toplevel(),
                namespace=Constants.GLOBAL_NAMESPACE,
                navigation_service=self.navigation_service,
                source="dashboard_ui",
                target="search_ui",
                type="recent:staple",
                unified_manager=self.unified_manager,
            ),
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=left_frame,
            relief=FLAT,
            text="📜 Recent Stack(s)",
        )

        # Place the recent button within the left frame
        recent_button.grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
        )

        # Create a right frame within the master frame
        right_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=master,
        )

        # Configure the right frame widget's 1st column to weight 1
        right_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the right frame widget's 1st row to weight 0
        right_frame.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the right frame widget's 2nd row to weight 1
        right_frame.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Place the right frame widget in the master frame
        right_frame.grid(
            column=1,
            row=0,
            sticky=NSEW,
        )

        # Create the "Top Frame" frame widget
        top_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=right_frame,
        )

        # Configure the "Top Frame" frame widget's 1st column to weight 1
        top_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the "Top Frame" frame widget's 1st row to weight 1
        top_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Place the "Top Frame" frame widget in the master frame
        top_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create the "Notebook" frame widget
        notebook: Dict[str, Any] = UIBuilder.get_tabbed_view(master=right_frame)

        # Style the "Notebook" frame "Top Frame" widget
        notebook["top_frame"].configure(background=Constants.BLUE_GREY["700"])

        # Place the "Notebook" frame widget in the master frame
        notebook["root"].grid(
            column=0,
            row=1,
            sticky=NSEW,
        )

        # Create the "Notebook" widgets
        self.create_notebook_widgets(master=notebook)

    def create_notebook_widgets(
        self,
        master: Dict[str, Any],
    ) -> None:
        """
        Creates and configures the main widgets of the notebook.

        This method initializes the main widgets of the notebook within the
        dashboard UI, setting their layout configuration.

        Args:
            master (Dict[str, Any]): The parent widget assembly dictionary.

        Returns:
            None
        """

        # Create the "Active Stacks" frame widget
        active_stacks_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=master["center_frame"],
        )

        # Add the "Active Stacks" frame widget to the notebook
        master["adder"](
            label="My Active Stacks",
            sticky=NSEW,
            widget=active_stacks_frame,
        )

        # Configure the "My Active Stacks" button
        master["my active stacks_button"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Create the "Recently Viewed" frame widget
        recently_viewed_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=master["center_frame"],
        )

        # Add the "Recently Viewed" frame widget to the notebook
        master["adder"](
            label="Recently Viewed",
            sticky=NSEW,
            widget=recently_viewed_frame,
        )

        # Configure the "Recently Viewed" button
        master["recently viewed_button"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Create the "Completed Stacks" frame widget
        completed_stacks_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=master["center_frame"],
        )

        # Add the "Completed Stacks" frame widget to the notebook
        master["adder"](
            label="Completed Stacks",
            sticky=NSEW,
            widget=completed_stacks_frame,
        )

        # Configure the "Completed Stacks" button
        master["completed stacks_button"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Create the "Active Stacks" frame widgets
        self.create_active_stacks_frame_widgets(master=active_stacks_frame)

        # Create the "Recently Viewed" frame widgets
        self.create_recently_viewed_stacks_frame_widgets(master=recently_viewed_frame)

        # Create the "Completed Stacks" frame widgets
        self.create_completed_stacks_frame_widgets(master=completed_stacks_frame)

    def create_active_stacks_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Creates and configures the main widgets of the active stacks frame.

        This method initializes the main widgets of the active stacks frame
        within the dashboard UI, setting their layout configuration.

        Args:
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """

        # Configure the master widget's 1st column to weight 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the master widget's 1st row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Get a new scrolled frame widget
        scrolled_frame: Dict[str, Any] = UIBuilder.get_scrolled_frame(master=master)

        # Style the scrolled frame "Canvas" widget
        # Set the background color to the main background color
        scrolled_frame["canvas"].configure(background=Constants.BLUE_GREY["700"])

        # Style the scrolled frame "Frame" widget
        # Set the background color to the main background color
        scrolled_frame["frame"].configure(background=Constants.BLUE_GREY["700"])

        # Style the scrolled frame "Root" widget
        # Set the background color to the main background color
        scrolled_frame["root"].configure(background=Constants.BLUE_GREY["700"])

        # Place the scrolled frame widget in the main window
        scrolled_frame["root"].grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

    def create_recently_viewed_stacks_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Creates and configures the recently viewed stacks frame widgets.

        This method initializes a scrolled frame widget for displaying recently viewed stacks
        and configures its layout and styling within the dashboard UI.

        Args:
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """

        # Configure the master widget's 1st column to weight 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the master widget's 1st row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Get a new scrolled frame widget
        scrolled_frame: Dict[str, Any] = UIBuilder.get_scrolled_frame(master=master)

        # Style the scrolled frame "Canvas" widget
        # Set the background color to the main background color
        scrolled_frame["canvas"].configure(background=Constants.BLUE_GREY["700"])

        # Style the scrolled frame "Frame" widget
        # Set the background color to the main background color
        scrolled_frame["frame"].configure(background=Constants.BLUE_GREY["700"])

        # Style the scrolled frame "Root" widget
        # Set the background color to the main background color
        scrolled_frame["root"].configure(background=Constants.BLUE_GREY["700"])

        # Place the scrolled frame widget in the main window
        scrolled_frame["root"].grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

    def create_completed_stacks_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Creates and configures the completed stacks frame widgets.

        This method initializes a scrolled frame widget for displaying
        completed stacks and configures its layout and styling within the
        dashboard UI.

        Args:
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """

        # Configure the master widget's 1st column to weight 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the master widget's 1st row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Get a new scrolled frame widget
        scrolled_frame: Dict[str, Any] = UIBuilder.get_scrolled_frame(master=master)

        # Style the scrolled frame "Canvas" widget
        # Set the background color to the main background color
        scrolled_frame["canvas"].configure(background=Constants.BLUE_GREY["700"])

        # Style the scrolled frame "Frame" widget
        # Set the background color to the main background color
        scrolled_frame["frame"].configure(background=Constants.BLUE_GREY["700"])

        # Style the scrolled frame "Root" widget
        # Set the background color to the main background color
        scrolled_frame["root"].configure(background=Constants.BLUE_GREY["700"])

        # Place the scrolled frame widget in the main window
        scrolled_frame["root"].grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

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

        # Configure the top frame widget's 1st column to weight 0
        master.grid_columnconfigure(
            index=0,
            weight=0,
        )

        # Configure the top frame widget's 2nd column to weight 1
        master.grid_columnconfigure(
            index=1,
            weight=1,
        )

        # Configure the top frame widget's 1st row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create a left frame within the top frame
        left_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=master,
        )

        # Configure the left frame widget's 1st column to weight 1
        left_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the left frame widget's 1st row to weight 1
        left_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Place the left frame widget in the top frame
        left_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create a clock widget within the left frame
        clock: Dict[str, Any] = UIBuilder.get_clock(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.LARGE_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=left_frame,
        )

        # Configure the clock's root widget's background to be grey
        clock["root"].configure(background=Constants.BLUE_GREY["700"])

        # Place the clock widget in the left frame
        clock["root"].grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=EW,
        )

        # Create a right frame within the top frame
        right_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=master,
        )

        # Configure the right frame widget's 1st column to weight 1
        right_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the right frame widget's 1st row to weight 1
        right_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Place the right frame widget in the top frame
        right_frame.grid(
            column=1,
            row=0,
            sticky=NSEW,
        )

        # Create a continue label within the right frame
        continue_label: tkinter.Label = UIBuilder.get_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.LARGE_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=right_frame,
            text="Welcome back! Continue from where you left.",
        )

        # Place the continue label within the right frame
        continue_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=EW,
        )

    def lookup_stacks(self) -> None:
        """
        Looks up the stacks and displays them.

        This method sends a request to retrieve the stacks
        and displays them in the dashboard UI.

        Returns:
            None
        """

        # Dispatch the REQUEST_GET_ALL_STACKS event
        notification: DispatcherNotification = self.dispatcher.dispatch(
            event=Events.REQUEST_GET_ALL_STACKS,
            namespace=Constants.GLOBAL_NAMESPACE,
        )

        # Log a debug message indicating the number of stacks found
        self.logger.debug(
            message=f"Found {len(notification['result'].values())} stack(s) in the database."
        )
