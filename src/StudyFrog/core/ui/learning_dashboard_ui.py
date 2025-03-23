"""
Author: lodego
Date: 2025-03-15
"""

import tkinter

from tkinter.constants import *

from typing import *

from core.setting import SettingService

from core.ui.base_ui import BaseUI
from core.ui.ui_builder import UIBuilder

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous
from utils.navigation import NavigationHistoryItem, NavigationHistoryService
from utils.unified import UnifiedObjectManager


__all__: Final[List[str]] = ["LearningDashboardUI"]


class LearningDashboardUI(BaseUI):
    """
    A class representing the learning dashboard user interface (UI) of the application.

    This class is responsible for initializing and configuring the layout of the
    learning dashboard UI, including setting up the main frames and populating them with
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
        unified_manager: UnifiedObjectManager,
    ) -> None:
        """
        Initializes a new instance of the LearningDashboardUI class.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.
            master (tkinter.Misc): The parent widget.
            navigation_item (NavigationHistoryItem): The navigation history item instance.
            navigation_service (NavigationHistoryService): The navigation history service instance.
            setting_service (SettingService): The setting service instance.
            unified_manager (UnifiedObjectManager): The unified manager instance.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            dispatcher=dispatcher,
            master=master,
            name="learning_dashboard_ui",
            navigation_item=navigation_item,
            navigation_service=navigation_service,
            setting_service=setting_service,
            unified_manager=unified_manager,
        )

    @override
    def collect_subscriptions(self) -> List[Dict[str, Any]]:
        """
        Collects and returns a list of subscriptions.

        This method should be implemented by subclasses to provide
        a list containing event subscriptions. Each subscription
        is associated with specific events and their corresponding
        handlers.

        Returns:
            List[Dict[str, Any]]: A list representing the subscriptions for events.

        Raises:
            NotImplementedError: If the method is not implemented
            by a subclass.
        """

        return []

    @override
    def configure_grid(self) -> None:
        """
        Configures the grid of the stack selection user interface.

        This method configures the grid of the stack selection user interface by setting the
        weights of the columns and rows.

        Returns:
            None
        """

        # Configure the weight of the 0th column to 1.
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the weight of the 0th row to 0.
        self.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the weight of the 1st row to 1.
        self.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Configure the weight of the 2nd row to 0.
        self.grid_rowconfigure(
            index=2,
            weight=0,
        )

    @override
    def create_widgets(self) -> None:
        """
        Creates and configures the main widgets of the stack selection user interface.

        This method creates and configures the main widgets of the stack selection user
        interface, setting their layout configuration and invoking methods to populate
        each frame with its respective widgets.

        Returns:
            None

        Raises:
            Exception: If an exception occurs during the creation or configuration of the widgets.
        """
        try:
            # Create the top frame widget
            top_frame: Optional[tkinter.Frame] = UIBuilder.get_frame(
                background=Constants.BLUE_GREY["700"],
                height=25,
                master=self,
            )

            # Create the center frame widget
            center_frame: Optional[tkinter.Frame] = UIBuilder.get_frame(
                background=Constants.BLUE_GREY["700"],
                master=self,
            )

            # Create the bottom frame widget
            bottom_frame: Optional[tkinter.Frame] = UIBuilder.get_frame(
                background=Constants.BLUE_GREY["700"],
                height=25,
                master=self,
            )

            # Check if all frames were created successfully
            if not all(
                [
                    top_frame,
                    center_frame,
                    bottom_frame,
                ]
            ):
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create frames in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Place the top frame widget in the main window
            top_frame.grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Place the center frame widget in the main window
            center_frame.grid(
                column=0,
                row=1,
                sticky=NSEW,
            )

            # Place the bottom frame widget in the main window
            bottom_frame.grid(
                column=0,
                row=2,
                sticky=NSEW,
            )

            # Create and configure the top frame widgets
            self.create_top_frame_widgets(master=top_frame)

            # Create and configure the center frame widgets
            self.create_center_frame_widgets(master=center_frame)

            # Create and configure the bottom frame widgets
            self.create_bottom_frame_widgets(master=bottom_frame)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def create_bottom_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        try:
            # Configure the weight of the 0th column to 1.
            master.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 0th row to 1.
            master.grid_rowconfigure(
                index=0,
                weight=1,
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_bottom_frame_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def create_center_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        try:
            # Configure the weight of the 0th column to 1.
            master.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 0th row to 1.
            master.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create tabbed view widgets within the passed master widget
            tabbed_view: Optional[Dict[str, Any]] = UIBuilder.get_tabbed_view(
                master=master
            )

            if not tabbed_view:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create tabbed view widgets from '{self.__class__.__name__}'"
                )

                # Return early
                return

            # Style the tabbed view's center frame widget
            tabbed_view["center_frame"].configure(background=Constants.BLUE_GREY["700"])

            # Style the tabbed view's root frame widget
            tabbed_view["root"].configure(background=Constants.BLUE_GREY["700"])

            # Style the tabbed view's top frame widget
            tabbed_view["top_frame"].configure(background=Constants.BLUE_GREY["700"])

            # Place the tabbed view widget within the passed master widget
            tabbed_view["root"].grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Create tabbed view widgets within the passed master widget
            tabbed_view_widgets: Optional[Dict[str, tkinter.Frame]] = (
                self.create_tabbed_view_widgets(master=tabbed_view["center_frame"])
            )

            if not tabbed_view_widgets:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create tabbed view widgets from '{self.__class__.__name__}'"
                )

                # Return early
                return

            # Iterate over the tabbed view widgets dictionary's key-value pairs
            for (
                label,
                widget,
            ) in tabbed_view_widgets.items():
                # Add the tab to the tabbed view
                tabbed_view["adder"](
                    label=label,
                    state=NORMAL,
                    sticky=NSEW,
                    widget=widget,
                )

                # Style the button widget corresponding to the label
                tabbed_view[f"{label.lower()}_button"].configure(
                    background=Constants.BLUE_GREY["700"],
                    font=(
                        Constants.DEFAULT_FONT_FAMILIY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    foreground=Constants.WHITE,
                    relief=FLAT,
                )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_center_frame_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def create_learning_overview_widgets(
        self,
        master: tkinter.Frame,
    ) -> Optional[tkinter.Frame]:
        try:
            # Configure the weight of the 0th column to 1.
            master.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 0th row to 1.
            master.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # TODO:
            #   - implement basic statistics visualization
            #   - implement visualization of learning progress
            #   - implement visualization of last session data (with ability to continue last session if unfinished)

            # Create a tkinter.Frame widget within the passed master widget
            frame: Optional[tkinter.Frame] = UIBuilder.get_frame(
                background=Constants.BLUE_GREY["700"],
                master=master,
            )

            if not frame:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create frame in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Configure the weight of the 0th column to 1.
            frame.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 0th row to 0.
            frame.grid_rowconfigure(
                index=0,
                weight=0,
            )

            # Configure the weight of the 1st row to 1.
            frame.grid_rowconfigure(
                index=1,
                weight=1,
            )

            # Create a tkinter.Button widget within the frame widget
            select_stacks_button: Optional[tkinter.Button] = UIBuilder.get_button(
                background=Constants.BLUE_GREY["700"],
                command=self.on_select_stacks_button_click,
                font=(
                    Constants.DEFAULT_FONT_FAMILIY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=frame,
                relief=FLAT,
                text="Select Stack(s) for run",
            )

            if not select_stacks_button:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create 'Select Stack(s) for run' button in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Place the button widget within the frame widget
            select_stacks_button.grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=E,
            )

            # Create scrolled frame widgets within the frame widget
            scrolled_frame: Optional[Dict[str, Any]] = UIBuilder.get_scrolled_frame(
                master=frame
            )

            if not scrolled_frame:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create scrolled frame in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Style the scrolled frame's canvas widget
            scrolled_frame["canvas"].configure(
                background=Constants.BLUE_GREY["700"],
            )

            # Style the scrolled frame's scrollbar widget
            scrolled_frame["frame"].configure(
                background=Constants.BLUE_GREY["700"],
            )

            # Style the scrolled frame's root frame widget
            scrolled_frame["root"].configure(
                background=Constants.BLUE_GREY["700"],
            )

            # Place the scrolled frame's root frame widget within the frame widget
            scrolled_frame["root"].grid(
                column=0,
                padx=5,
                pady=5,
                row=1,
                sticky=NSEW,
            )

            # Return the frame widget
            return frame
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_learning_overview_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def create_learning_planning_widgets(
        self,
        master: tkinter.Frame,
    ) -> Optional[tkinter.Frame]:
        try:
            # Configure the weight of the 0th column to 1.
            master.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 0th row to 1.
            master.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # TODO:
            #   - calendar for scheduling sessions, exams, and due dates

            # Create a tkinter.Frame widget within the passed master widget
            frame: Optional[tkinter.Frame] = UIBuilder.get_frame(
                background=Constants.BLUE_GREY["700"],
                master=master,
            )

            if not frame:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create frame from '{self.__class__.__name__}'"
                )

                # Return early
                return

            # Return the frame widget
            return frame
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_learning_planning_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def create_learning_statistics_widgets(
        self,
        master: tkinter.Frame,
    ) -> Optional[tkinter.Frame]:
        try:
            # Configure the weight of the 0th column to 1.
            master.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 0th row to 1.
            master.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # TODO:
            #   - implement in-depth learning statistics and reporting

            # Create a tkinter.Frame widget within the passed master widget
            frame: Optional[tkinter.Frame] = UIBuilder.get_frame(
                background=Constants.BLUE_GREY["700"],
                master=master,
            )

            if not frame:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create frame from '{self.__class__.__name__}'"
                )

                # Return early
                return

            # Return the frame widget
            return frame
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_learning_statistics_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def create_tabbed_view_widgets(
        self,
        master: tkinter.Frame,
    ) -> Optional[Dict[str, tkinter.Frame]]:
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, tkinter.Frame] = {}

            # Create the learning overview widgets
            result["Learning overview"] = self.create_learning_overview_widgets(
                master=master,
            )

            # Create the learning planning widgets
            result["Learning planning"] = self.create_learning_planning_widgets(
                master=master,
            )

            # Create the learning statistics widgets
            result["Learning statistics"] = self.create_learning_statistics_widgets(
                master=master,
            )

            # Iterate over the result dictionary's key-value pairs
            for (
                key,
                value,
            ) in result.items():
                # Check if the value is not None
                if value:
                    continue

                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create '{key}' tab in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Remove the key from the result dictionary
                del result[key]

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_tabbed_view_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def create_top_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        try:
            # Configure the weight of the 0th column to 1.
            master.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 0th row to 1.
            master.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create a tkinter.Label widget within the passed master widget
            label: Optional[tkinter.Label] = UIBuilder.get_label(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILIY,
                    Constants.LARGE_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=master,
                text="Learning Dashboard",
            )

            if not label:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create label from '{self.__class__.__name__}'"
                )

                # Return early
                return

            # Place the label widget within the passed master widget
            label.grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_top_frame_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def on_select_stacks_button_click(self) -> None:
        """
        Handles the event when the 'Select Stacks' button is clicked.

        This function dispatches a navigation request to the global namespace
        with the target 'stack_selection_ui' and the source 'learning_dashboard_ui'.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to dispatch the
                navigation request.
        """
        try:
            # Create a tkinter.Toplevel widget
            master: Optional[tkinter.Toplevel] = UIBuilder.get_toplevel()

            if not master:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create toplevel in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Style the toplevel widget
            master.configure(background=Constants.BLUE_GREY["700"])

            # Configure the weight of the 0th column to 1.
            master.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 0th row to 1.
            master.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Set the geometry of the toplevel window
            master.wm_geometry(newGeometry=Constants.DEFAULT_GEOMETRY)

            # Dispatch the REQUEST_VALIDATE_NAVIGATION event in the global namespace
            self.dispatcher.dispatch(
                direction=Constants.FORWARD_DIRECTION,  # Set the navigation direction to 'forward'
                event=Events.REQUEST_VALIDATE_NAVIGATION,  # The event to be dispatched
                master=master,
                namespace=Constants.GLOBAL_NAMESPACE,  # Specify the global namespace
                source="learning_dashboard_ui",  # Source of the navigation request
                target="stack_selection_ui",  # Target UI for navigation
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_select_stacks_button_click' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e
