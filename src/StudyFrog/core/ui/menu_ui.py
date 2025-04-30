"""
Author: lodego
Date: 2025-02-11
"""

import tkinter

from tkinter.constants import *

from typing import *

from core.setting import SettingService

from utils.base_ui import BaseUI
from core.ui.ui_builder import UIBuilder

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.navigation import NavigationHistoryItem, NavigationHistoryService
from utils.unified import UnifiedObjectFactory, UnifiedObjectManager


__all__: Final[List[str]] = ["MenuUI"]


class MenuUI(BaseUI):
    """
    A class representing the menu menu user interface (UI) of the application.

    This class is responsible for initializing and configuring the layout of the
    menu menu UI, including setting up the main frames and populating them with
    respective widgets. It extends the tkinter.Frame class and utilizes various
    utility classes for managing navigation, logging, and other functionalities.

    Attributes:
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
        unified_factory: UnifiedObjectFactory,
        unified_manager: UnifiedObjectManager,
    ) -> None:
        """
        Initializes a new instance of the MenuUI class.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.
            master (tkinter.Misc): The parent widget.
            navigation_item (NavigationHistoryItem): The navigation history item instance.
            navigation_service (NavigationHistoryService): The navigation history service instance.
            setting_service (SettingService): The setting service instance.
            unified_factory (UnifiedObjectFactory): The unified factory instance.
            unified_manager (UnifiedObjectManager): The unified manager instance.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            dispatcher=dispatcher,
            master=master,
            name="user_ui",
            navigation_item=navigation_item,
            navigation_service=navigation_service,
            setting_service=setting_service,
            unified_factory=unified_factory,
            unified_manager=unified_manager,
        )

    def collect_subscriptions(self) -> List[Dict[str, Any]]:
        """
        Collects and returns a list of subscriptions.

        This method should be implemented by subclasses to provide
        a list containing event subscriptions. Each subscription
        is associated with specific events and their corresponding
        handlers.

        Returns:
            List[Dict[str, Any]]: A list representing the subscriptions for events.
        """

        subscriptions: List[Dict[str, Any]] = super().collect_subscriptions()

        return subscriptions

    @override
    def configure_grid(self) -> None:
        """
        Configures the grid of the menu menu widget.

        This method configures the grid of the menu menu widget by setting the
        weights of the columns and rows.

        Returns:
            None
        """

        # Configure the menu menu widget's 1st column to weight 1.
        # This means that the 1st column will stretch when the window is resized.
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the menu menu widget's 1st and 3rd row to weight 0.
        # This means that the 1st and 3rd row will not stretch when the window is resized.
        self.grid_rowconfigure(
            index=(
                0,
                2,
            ),
            weight=0,
        )

        # Configure the menu menu widget's 2nd row to weight 1.
        # This means that the 2nd row will stretch when the window is resized.
        self.grid_rowconfigure(
            index=1,
            weight=1,
        )

    @override
    def create_widgets(self) -> None:
        """
        Helps and configures the main frames of the menu menu UI.

        This method initializes the top, center, and bottom frames within the
        menu menu UI, setting their layout configuration and invoking methods
        to populate each frame with its respective widgets.

        Args:
            None

        Returns:
            None
        """

        # Attempt to create the "Top Frame" frame widget
        top_frame: Optional[tkinter.Frame] = tkinter.Frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        # Check, if the creation of the top frame was successfull
        if not top_frame:
            # Log an error message to indicate that something went wrong
            logger.error(
                "Failed to create 'top' frame in main window. This is likely a bug."
            )

            # Return early
            return

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

        # Attempt to create the "Center Frame" frame widget
        center_frame: Optional[tkinter.Frame] = tkinter.Frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        # Check, if the creation of the center frame was successfull
        if not center_frame:
            # Log an error message to indicate that something went wrong
            logger.error(
                "Failed to create 'center' frame in main window. This is likely a bug."
            )

            # Return early
            return

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

        # Attempt to create the "Bottom Frame" frame widget
        bottom_frame: Optional[tkinter.Frame] = tkinter.Frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        # Check, if the creation of the bottom frame was successfull
        if not bottom_frame:
            # Log an error message to indicate that something went wrong
            logger.error(
                "Failed to create 'bottom' frame in main window. This is likely a bug."
            )

            # Return early
            return

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
        Helps and configures the main widgets of the bottom frame.

        This method initializes the main widgets of the bottom frame within the
        menu menu UI, setting their layout configuration.

        Args:
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """

        # Configure the bottom frame widget's 1st column to weight 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the bottom frame widget's 1st row to weight 0
        master.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the bottom frame widget's 2nd row to weight 1
        master.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Configure the bottom frame widget's 3rd row to weight 0
        master.grid_rowconfigure(
            index=2,
            weight=0,
        )

        # Attempt to create the close button
        close_button: Optional[tkinter.Button] = tkinter.Button(
            background=Constants.BLUE_GREY["700"],
            command=self.on_close_button_clicked,
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=master,
            relief=FLAT,
            text="Close",
        )

        # Check, if the creation of the close button was successfull
        if not close_button:
            # Log an error message to indicate that something went wrong
            logger.error(
                "Failed to create 'close' button in bottom frame widgets. This is likely a bug."
            )

            # Return early
            return

        # Place the close button in the bottom frame
        close_button.grid(
            column=0,
            padx=5,
            pady=5,
            row=2,
        )

    def create_center_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Helps and configures the main widgets of the center frame.

        This method initializes the main widgets of the center frame within the
        menu menu UI, setting their layout configuration.

        Args:
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """

        # Configure the center frame widget's 1st column to weight 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the center frame widget's 1st row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Attempt to create the scrolled frame widgets
        scrolled_frame: Optional[Dict[str, Any]] = UIBuilder.get_scrolled_frame(
            master=master
        )

        # Check, if the creation of the scrolled frame widgets was successfull
        if not scrolled_frame:
            # Log an error message to indicate that something went wrong
            logger.error(
                "Failed to create 'scrolled frame' in center frame widgets. This is likely a bug."
            )

            # Return early
            return

        # Style the scrolled frame widget's canvas widget
        scrolled_frame["canvas"].configure(background=Constants.BLUE_GREY["700"])

        # Style the scrolled frame widget's frame widget
        scrolled_frame["frame"].configure(background=Constants.BLUE_GREY["700"])

        # Style the scrolled frame widget's root widget
        scrolled_frame["root"].configure(background=Constants.BLUE_GREY["700"])

        # Place the scrolled frame widget in the center frame
        scrolled_frame["root"].grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Configure the scrolled frame widget's frame widget's 1st column to weight 0
        scrolled_frame["frame"].grid_columnconfigure(
            index=0,
            weight=0,
        )

        # Configure the scrolled frame widget's frame widget's 2nd column to weight 1
        scrolled_frame["frame"].grid_columnconfigure(
            index=1,
            weight=1,
        )

        home_button: Optional[tkinter.Button] = tkinter.Button(
            background=Constants.BLUE_GREY["700"],
            command=self.on_home_button_clicked,
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=scrolled_frame["frame"],
            relief=FLAT,
            text="🏠",
        )

        # Check, if the creation of the home button was successfull
        if not home_button:
            # Log an error message to indicate that something went wrong
            logger.error(
                "Failed to create 'home' button in center frame widgets. This is likely a bug."
            )

            # Return early
            return

        # Place the home button in the center frame
        home_button.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
        )

        home_label: Optional[tkinter.Label] = tkinter.Label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=scrolled_frame["frame"],
            text="Home",
        )

        # Check, if the creation of the home label was successfull
        if not home_label:
            # Log an error message to indicate that something went wrong
            logger.error(
                "Failed to create 'home' label in center frame widgets. This is likely a bug."
            )

            # Return early
            return

        # Bind the home label to the left mouse button click event
        home_label.bind(
            func=lambda event: self.on_home_button_clicked(),
            sequence="<ButtonRelease-1>",
        )

        # Place the home label in the center frame
        home_label.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
        )

    def create_top_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Helps and configures the main widgets of the top frame.

        This method initializes the main widgets of the top frame within the
        menu menu UI, setting their layout configuration.

        Args:
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """

        # Configure the top frame widget's 1st column to weight 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
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

        # Attempt to create the StudyFrog label
        study_frog_label: Optional[tkinter.Label] = tkinter.Label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.LARGE_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=master,
            text="StudyFrog",
        )

        # Check, if the creation of the StudyFrog label was successfull
        if not study_frog_label:
            # Log an error message to indicate that something went wrong
            logger.error(
                "Failed to create 'StudyFrog' label in top frame widgets. This is likely a bug."
            )

            # Return early
            return

        # Place the StudyFrog label in the top frame
        study_frog_label.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Attempt to create the shutdown button
        shutdown_button: Optional[tkinter.Button] = tkinter.Button(
            background=Constants.BLUE_GREY["700"],
            command=self.on_shutdown_button_clicked,
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=master,
            relief=FLAT,
            text="X",
        )

        # Check, if the creation of the shutdown button was successfull
        if not shutdown_button:
            # Log an error message to indicate that something went wrong
            logger.error(
                "Failed to create 'shutdown' button in top frame widgets. This is likely a bug."
            )

            # Return early
            return

        # Place the shutdown button in the top frame
        shutdown_button.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
        )

    def on_close_button_clicked(self) -> None:
        """
        Handles the event when the 'close' button is clicked.

        This method destroys the master widget, which will close the window.

        Returns:
            None
        """
        if not isinstance(
            self.master,
            tkinter.Toplevel,
        ):
            # Log an error message to indicate that something went wrong
            logger.error(
                "Failed to destroy master widget in 'on_close_button_clicked' method. This is likely a bug."
            )

            # Return early
            return

        # Destroy the master widget
        self.master.destroy()

    def on_home_button_clicked(self) -> None:
        """
        Handles the event when the 'home' button is clicked.

        This method dispatches the REQUEST_VALIDATE_NAVIGATION event in the global namespace,
        which will cause the application to navigate to the dashboard UI.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to dispatch the event.
        """
        try:
            # Attempt to dispatch the REQUEST_VALIDATE_NAVIGATION event in the global namespace
            self.dispatcher.dispatch(
                direction=Constants.FORWARD_DIRECTION,
                event=Events.REQUEST_VALIDATE_NAVIGATION,
                namespace=Constants.GLOBAL_NAMESPACE,
                source="menu_ui",
                target="dashboard_ui",
            )
        except Exception as e:
            # Log an error message to indicate that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_home_button_clicked' method from {self.__class__.__name__}: {e}"
            )

            # Re-raise the exception the caller
            raise e

    def on_shutdown_button_clicked(self) -> None:
        """
        Handles the event when the 'shutdown' button is clicked.

        This method dispatches the REQUEST_APPLICATION_STOP event in the global namespace,
        which will cause the application to stop.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to dispatch the event.
        """
        try:
            # Attempt to dispatch the REQUEST_APPLICATION_STOP event in the global namespace
            self.dispatcher.dispatch(
                event=Events.REQUEST_APPLICATION_STOP,
                namespace=Constants.GLOBAL_NAMESPACE,
            )
        except Exception as e:
            # Log an error message to indicate that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_shutdown_button_clicked' method from {self.__class__.__name__}: {e}"
            )

            # Re-raise the exception the caller
            raise e
