"""
Author: lodego
Date 2025-04-21
"""

import tkinter
import traceback

from tkinter.constants import *
from typing import *

from core.setting import SettingService

from core.ui.frames.frames import ScrolledFrame, TabbedFrame

from utils.base_ui import BaseUI
from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherNotification
from utils.events import Events
from utils.navigation import NavigationHistoryItem, NavigationHistoryService
from utils.unified import UnifiedObjectFactory, UnifiedObjectManager


__all__: Final[List[str]] = ["LearningDashboardUI"]


class LearningDashboardUI(BaseUI):
    """
    A class that represents the learning dashboard UI in the StudyFrog application.

    This class extends the BaseUI class and is responsible for creating and
    managing the learning dashboard UI.

    Attributes:
        dispatcher (Dispatcher): The dispatcher instance.
        logger (Logger): The logger instance.
        master (tkinter.Misc): The parent widget.
        navigation_service (NavigationHistoryService): The navigation history service instance.
        setting_service (SettingService): The setting service instance.
        unified_factory (UnifiedObjectFactory): The unified factory instance.
        unified_manager (UnifiedObjectManager): The unified manager instance.
        navigation_item (NavigationHistoryItem): The navigation history item instance.
    """

    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        navigation_service: NavigationHistoryService,
        setting_service: SettingService,
        unified_manager: UnifiedObjectManager,
        unified_factory: UnifiedObjectFactory,
        navigation_item: Optional[NavigationHistoryItem] = None,
    ) -> None:
        """
        Initializes a new instance of the LearningDashboardUI class.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.
            master (tkinter.Misc): The parent widget.
            navigation_service (NavigationHistoryService): The navigation history service instance.
            setting_service (SettingService): The setting service instance.
            unified_manager (UnifiedObjectManager): The unified manager instance.
            unified_factory (UnifiedObjectFactory): The unified factory instance.
            navigation_item (NavigationHistoryItem): The navigation history item instance.

        Returns:
            None
        """

        # Call the parent class constructor with the passed arguments
        super().__init__(
            dispatcher=dispatcher,
            master=master,
            name="learning_dashboard_ui",
            navigation_item=navigation_item,
            navigation_service=navigation_service,
            setting_service=setting_service,
            unified_factory=unified_factory,
            unified_manager=unified_manager,
        )

        # Update idletasks
        self.update_idletasks()

    def _on_stack_select_button_click(self) -> None:
        """
        Handles the click event of the stack select button in the learning dashboard UI.

        This method dispatches the REQUEST_VALIDATE_NAVIGATION event in the 'global' namespace
        to request that the navigation service validate the navigation to the
        'learning_stack_selection_ui' target.

        Returns:
            None

        Raises:
            Exception: If an error occurs during dispatch or internal processing.
        """
        try:
            # Dispatch the REQUEST_VALIDATE_NAVIGATION event in the 'global' namespace
            notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
                direction=Constants.FORWARD_DIRECTION,
                event=Events.REQUEST_VALIDATE_NAVIGATION,
                namespace=Constants.GLOBAL_NAMESPACE,
                source="learning_dashboard_ui",
                target="learning_stack_selection_ui",
            )

            # Check, if the notification exists or has errors
            if not notification or notification.has_errors():
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to dispatch 'REQUEST_VALIDATE_NAVIGATION' event in 'global' namespace in '{self.__class__.__name__}' class. Errors: {notification.get_errors() if notification else None}"
                )

                # Return early
                return
        except Exception as e:
            # Log an error message
            self.logger.error(
                message=f"Caught an exception while attempting to run '_on_stack_select_button_click' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    @override
    def configure_grid(self) -> None:
        """
        Configures the grid of the LearningDashboardUI widget.

        This method configures the grid of the LearningDashboardUI widget by setting
        the weights of the columns and rows.

        Args:
            None

        Returns:
            None
        """

        # Configure the LearningDashbardUI widget's 0th column to weight 1
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the LearningDashbardUI widget's 0th row to weight 0
        self.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the LearningDashbardUI widget's 1st row to weight 1
        self.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Configure the LearningDashbardUI widget's 2nd row to weight 0
        self.grid_rowconfigure(
            index=2,
            weight=0,
        )

    def create_bottom_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """ """

        # Configure the passed master tkinter.Frame widget's 0th column to weight 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the passed master tkinter.Frame widget's 0th row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Update idletasks
        self.update_idletasks()

    def create_center_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """
        Creates and configures the main widgets of the center frame.

        This method initializes the main widgets of the center frame within the
        dashboard UI, setting their layout and configuration for different tabs
        such as Planning, Overview, and Statistics.

        Args:
            master (tkinter.Frame): The parent frame for the center widgets.

        Returns:
            None
        """
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the passed master tkinter.Frame widget's 0th row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create a TabbedFrame widget
        tabbed_frame: TabbedFrame = TabbedFrame(master=master)

        # Place the TabbedFrame widget in the grid
        tabbed_frame.grid(
            column=0,
            padx=5,
            pady=5,
            sticky=NSEW,
        )

        # Configure the TabbedFrame widget
        tabbed_frame.configure(background=Constants.BLUE_GREY["700"])

        # Configure the TabbedFrame widget's 'container frame' tkinter.Frame widget
        tabbed_frame.configure_container_frame(background=Constants.BLUE_GREY["700"])

        # Configure the TabbedFrame widget's 'top frame' tkinter.Frame widget
        tabbed_frame.configure_top_frame(background=Constants.BLUE_GREY["700"])

        # Create and add the 'planning' widgets to the TabbedFrame widget
        planning_frame: ScrolledFrame = self.create_planning_widgets(
            master=tabbed_frame,
        )

        # Add the 'planning' widgets to the TabbedFrame widget
        tabbed_frame.add(
            label="Planning",
            widget=planning_frame,
        )

        # Configure the TabbedFrame widget's 'planning button' tkinter.Button widget
        tabbed_frame.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            name="planning",
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Create and add the 'overview' widgets to the TabbedFrame widget
        overview_frame: ScrolledFrame = self.create_overview_widgets(
            master=tabbed_frame,
        )

        # Add the 'overview' widgets to the TabbedFrame widget
        tabbed_frame.add(
            label="Overview",
            widget=overview_frame,
        )

        # Configure the TabbedFrame widget's 'overview button' tkinter.Button widget
        tabbed_frame.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            name="overview",
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Create and add the 'statistics' widgets to the TabbedFrame widget
        statistics_frame: ScrolledFrame = self.create_statistics_widgets(
            master=tabbed_frame,
        )

        # Add the 'statistics' widgets to the TabbedFrame widget
        tabbed_frame.add(
            label="Statistics",
            widget=statistics_frame,
        )

        # Configure the TabbedFrame widget's 'statistics button' tkinter.Button widget
        tabbed_frame.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            name="statistics",
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Update idletasks
        self.update_idletasks()

    def create_planning_widgets(
        self,
        master: tkinter.Frame,
    ) -> ScrolledFrame:
        """
        Creates and configures the main widgets of the planning frame.

        This method initializes the main widgets of the planning frame
        within the learning dashboard UI and sets their layout
        configuration.

        Args:
            master (tkinter.Frame): The parent frame for the planning widgets.

        Returns:
            ScrolledFrame: The created ScrolledFrame widget.
        """

        # Create a ScrolledFrame widget
        scrolled_frame: ScrolledFrame = ScrolledFrame(master=master)

        # Place the ScrolledFrame widget in the grid
        scrolled_frame.grid(
            column=0,
            padx=5,
            pady=5,
            sticky=NSEW,
        )

        # Configure the ScrolledFrame widget
        scrolled_frame.configure(background=Constants.BLUE_GREY["700"])

        # Configure the ScrolledFrame widget's tkinter.Canvas widget
        scrolled_frame.configure_canvas(background=Constants.BLUE_GREY["700"])

        # Configure the ScrolledFrame widget's 'container frame' tkinter.Frame widget
        scrolled_frame.configure_container_frame(background=Constants.BLUE_GREY["700"])

        # Update idletasks
        self.update_idletasks()

        # Return the ScrolledFrame widget to the caller
        return scrolled_frame

    def create_overview_widgets(
        self,
        master: tkinter.Frame,
    ) -> ScrolledFrame:
        """
        Creates and configures the main widgets of the overview frame.

        This method initializes the main widgets of the overview frame
        within the learning dashboard UI and sets their layout
        configuration.

        Args:
            master (tkinter.Frame): The parent frame for the overview widgets.

        Returns:
            ScrolledFrame: The created ScrolledFrame widget.
        """

        # Create a ScrolledFrame widget
        scrolled_frame: ScrolledFrame = ScrolledFrame(master=master)

        # Place the ScrolledFrame widget in the grid
        scrolled_frame.grid(
            column=0,
            padx=5,
            pady=5,
            sticky=NSEW,
        )

        # Configure the ScrolledFrame widget
        scrolled_frame.configure(background=Constants.BLUE_GREY["700"])

        # Configure the ScrolledFrame widget's tkinter.Canvas widget
        scrolled_frame.configure_canvas(background=Constants.BLUE_GREY["700"])

        # Configure the ScrolledFrame widget's 'container frame' tkinter.Frame widget
        scrolled_frame.configure_container_frame(background=Constants.BLUE_GREY["700"])

        # Update idletasks
        self.update_idletasks()

        # Return the ScrolledFrame widget to the caller
        return scrolled_frame

    def create_statistics_widgets(
        self,
        master: tkinter.Frame,
    ) -> ScrolledFrame:
        """
        Creates and configures the main widgets of the statistics frame.

        This method initializes the main widgets of the statistics frame within the
        learning dashboard UI, setting their layout configuration.

        Args:
            master (tkinter.Frame): The parent widget.

        Returns:
            ScrolledFrame: The created ScrolledFrame widget.
        """

        # Create a ScrolledFrame widget
        scrolled_frame: ScrolledFrame = ScrolledFrame(master=master)

        # Place the ScrolledFrame widget in the grid
        scrolled_frame.grid(
            column=0,
            padx=5,
            pady=5,
            sticky=NSEW,
        )

        # Configure the ScrolledFrame widget
        scrolled_frame.configure(background=Constants.BLUE_GREY["700"])

        # Configure the ScrolledFrame widget's tkinter.Canvas widget
        scrolled_frame.configure_canvas(background=Constants.BLUE_GREY["700"])

        # Configure the ScrolledFrame widget's 'container frame' tkinter.Frame widget
        scrolled_frame.configure_container_frame(background=Constants.BLUE_GREY["700"])

        # Update idletasks
        self.update_idletasks()

        # Return the ScrolledFrame widget to the caller
        return scrolled_frame

    def create_top_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """
        Creates and configures the main widgets of the top frame.

        This method initializes the main widgets of the top frame within the
        learning dashboard UI, setting their layout configuration.

        Args:
            master (tkinter.Frame): The parent widget.

        Returns:
            None
        """

        # Configure the passed master tkinter.Frame widget's 0th column to weight 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the passed master tkinter.Frame widget's 0th row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create the 'select stacks' tkinter.Button widget
        select_stacks_button: tkinter.Button = tkinter.Button(
            background=Constants.BLUE_GREY["700"],
            command=self._on_stack_select_button_click,
            foreground=Constants.WHITE,
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            master=master,
            relief=FLAT,
            text="Select Stacks",
        )

        # Place the 'select stacks' tkinter.Button widget in the grid
        select_stacks_button.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=E,
        )

        # Update idletasks
        self.update_idletasks()

    @override
    def create_widgets(self) -> None:
        """
        Creates and configures the main frames of the learning dashboard UI.

        This method initializes the top, center, and bottom frames within the
        learning dashboard UI, setting their layout configuration and invoking
        methods to populate each frame with its respective widgets.

        Args:
            None

        Returns:
            None
        """

        # Create the 'bottom frame' tkinter.Frame widget
        bottom_frame: tkinter.Frame = tkinter.Frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        # Place the 'bottom frame' tkinter.Frame widget in the grid
        bottom_frame.grid(
            column=0,
            row=2,
            sticky=NSEW,
        )

        # Create the 'bottom frame' widgets
        self.create_bottom_frame_widgets(master=bottom_frame)

        # Create the 'center frame' tkinter.Frame widget
        center_frame: tkinter.Frame = tkinter.Frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        # Place the 'center frame' tkinter.Frame widget in the grid
        center_frame.grid(
            column=0,
            row=1,
            sticky=NSEW,
        )

        # Create the 'center frame' widgets
        self.create_center_frame_widgets(master=center_frame)

        # Create the 'top frame' tkinter.Frame widget
        top_frame: tkinter.Frame = tkinter.Frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        # Place the 'top frame' tkinter.Frame widget in the grid
        top_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create the 'top frame' widgets
        self.create_top_frame_widgets(master=top_frame)

        # Update idletasks
        self.update_idletasks()
