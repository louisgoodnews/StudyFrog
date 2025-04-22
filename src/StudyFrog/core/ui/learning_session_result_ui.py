"""
Author: lodego
Date: 2025-03-15
"""

import tkinter
import traceback

from tkinter.constants import *

from typing import *

from core.setting import SettingService

from core.ui.frames.frames import ScrolledFrame, TabbedFrame

from utils.base_ui import BaseUI
from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.navigation import NavigationHistoryItem, NavigationHistoryService
from utils.unified import UnifiedObjectManager


__all__: Final[List[str]] = ["LearningSessionResultUI"]


class LearningSessionResultUI(BaseUI):
    """
    A class representing the learning session result user interface (UI) of the application.

    This class is responsible for initializing and configuring the layout of the
    learning session UI, including setting up the main frames and populating them with
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
        Initializes a new instance of the LearningSessionResultUI class.

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
            name="learning_session_result_ui",
            navigation_item=navigation_item,
            navigation_service=navigation_service,
            setting_service=setting_service,
            unified_manager=unified_manager,
        )

        # Update idletasks
        self.update_idletasks()

    def _on_continue_button_click(self) -> None:
        """
        Handles the click event of the 'Continue' button.

        This method dispatches the REQUEST_VALIDATE_NAVIGATION event in the 'global' namespace
        to request that the navigation service validate the navigation to the 'learning_dashboard_ui'
        target.

        Args:
            None

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
                source="learning_session_result_ui",
                target="learning_dashboard_ui",
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
                message=f"Caught an exception while attempting to run '_on_continue_button_click' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def _on_retry_button_click(self) -> None:
        """
        Handles the click event of the 'Retry' button.

        Dispatches the REQUEST_VALIDATE_NAVIGATION event in the 'global' namespace
        to request that the navigation service validate the navigation to the
        'learning_session_stack_selection_ui' target.

        Args:
            None

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
                source="learning_session_result_ui",
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
                message=f"Caught an exception while attempting to run '_on_retry_button_click' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def collect_subscriptions(self) -> List[Dict[str, Any]]:
        """
        Collects and returns a list of subscriptions.

        This method should be implemented by subclasses to provide
        a list containing event subscriptions. Each subscription
        is associated with specific events and their corresponding
        handlers.

        Args:
            None

        Returns:
            List[Dict[str, Any]]: A list representing the subscriptions for events.
        """

        # Call the parent class 'collect_subscriptions' method
        subscriptions: List[Dict[str, Any]] = super().collect_subscriptions()

        # Return the list of subscriptions to the caller
        return subscriptions

    @override
    def configure_grid(self) -> None:
        """
        Configures the grid of the learning session result user interface.

        This method configures the grid of the learning session result user interface by setting the
        weights of the columns and rows.

        Returns:
            None
        """

        # Configure the weight of the LearningSessionUI widget's 0th column to 1.
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the weight of the LearningSessionUI widget's 0th row to 0.
        self.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the weight of the LearningSessionUI widget's 1st row to 1.
        self.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Configure the weight of the LearningSessionUI widget's 2nd row to 0.
        self.grid_rowconfigure(
            index=2,
            weight=0,
        )

    def create_bottom_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """
        Creates and configures the main widgets of the bottom frame.

        This method initializes the main widgets of the bottom frame within the
        learning session result UI, setting their layout configuration and
        adding functionalities to the 'retry' and 'continue' buttons.

        Args:
            master (tkinter.Frame): The parent widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs during the execution of the method.
        """
        try:
            # Configure the weight of the 0th column of the passed master tkinter.Frame widget to 1.
            master.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 1st column of the passed master tkinter.Frame widget to 0.
            master.grid_columnconfigure(
                index=1,
                weight=0,
            )

            # Configure the weight of the 2nd column of the passed master tkinter.Frame widget to 0.
            master.grid_columnconfigure(
                index=2,
                weight=0,
            )

            # Configure the weight of the 0th row of the passed master tkinter.Frame widget to 1.
            master.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the 'retry button' tkinter.Button widget
            retry_button: tkinter.Button = tkinter.Button(
                background=Constants.BLUE_GREY["700"],
                command=self._on_retry_button_click,
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=master,
                relief=FLAT,
                text="Retry",
            )

            # Place the 'retry button' tkinter.Button widget in the grid
            retry_button.grid(
                column=1,
                padx=5,
                pady=5,
                row=0,
                sticky=E,
            )

            # Create the 'continue button' tkinter.Button widget
            continue_button: tkinter.Button = tkinter.Button(
                background=Constants.BLUE_GREY["700"],
                command=self._on_continue_button_click,
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=master,
                relief=FLAT,
                text="Continue",
            )

            # Place the 'continue button' tkinter.Button widget in the grid
            continue_button.grid(
                column=2,
                padx=5,
                pady=5,
                row=0,
                sticky=E,
            )

            # Update idletasks
            self.update_idletasks()
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_bottom_frame_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def create_center_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """
        Creates and configures the main widgets of the center frame.

        This method initializes the main widgets of the center frame within the
        learning session result user interface, setting their layout configuration.

        Args:
            master (tkinter.Frame): The parent widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs during the creation of the TabbedFrame widget.
        """
        try:
            # Configure the weight of the 0th column of the passed master tkinter.Frame widget to 1.
            master.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 0th row of the passed master tkinter.Frame widget to 1.
            master.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create a TabbedFrame widget
            tabbed_frame: TabbedFrame = TabbedFrame(master=master)

            # Create and add the overview widgets to the TabbedFrame widget
            tabbed_frame.add(
                label="Overview",
                widget=self.create_overview_widgets(master=tabbed_frame),
            )

            # Configure the TabbedFrame widget's 'overview button' widget
            tabbed_frame.configure_button(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                name="overview",
                relief=FLAT,
            )

            # Create and add the details widgets to the TabbedFrame widget
            tabbed_frame.add(
                label="Details", widget=self.create_details_widgets(master=tabbed_frame)
            )

            # Configure the TabbedFrame widget's 'details button' widget
            tabbed_frame.configure_button(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                name="details",
                relief=FLAT,
            )

            # Update idletasks
            self.update_idletasks()
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_center_frame_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def create_details_widgets(
        self,
        master: tkinter.Frame,
    ) -> ScrolledFrame:
        """
        Creates and configures the main widgets of the details frame.

        This method initializes the main widgets of the details frame within the
        learning session result user interface, setting their layout configuration.

        Args:
            master (tkinter.Frame): The parent widget.

        Returns:
            ScrolledFrame: The ScrolledFrame widget.

        Raises:
            Exception: If an exception occurs during the creation of the ScrolledFrame widget.
        """
        try:
            # Configure the weight of the 0th column of the passed master tkinter.Frame widget to 1.
            master.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 0th row of the passed master tkinter.Frame widget to 1.
            master.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the ScrolledFrame widget
            scrolled_frame: ScrolledFrame = ScrolledFrame(master=master)

            # Place the ScrolledFrame in the grid
            scrolled_frame.grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Configure the ScrolledFrame widget
            scrolled_frame.configure(background=Constants.BLUE_GREY["700"])

            # Configure the ScrolledFrame widget's tkinter.Canvas widget
            scrolled_frame.configure_canvas(background=Constants.BLUE_GREY["700"])

            # Configure the ScrolledFrame widget's 'container frame' tkinter.Frame widget
            scrolled_frame.configure_container_frame(
                background=Constants.BLUE_GREY["700"]
            )

            # Update idletasks
            self.update_idletasks()

            # Return the ScrolledFrame widget to the caller
            return scrolled_frame
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_details_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def create_overview_widgets(
        self,
        master: tkinter.Frame,
    ) -> ScrolledFrame:
        """
        Creates and configures the main widgets of the overview frame.

        This method initializes the main widgets of the overview frame within the
        learning session result user interface, setting their layout configuration.

        Args:
            master (tkinter.Frame): The parent widget.

        Returns:
            ScrolledFrame: The ScrolledFrame widget.
        
        Raises:
            Exception: If an exception occurs during the creation of the ScrolledFrame widget.
        """
        try:
            # Configure the weight of the 0th column of the passed master tkinter.Frame widget to 1.
            master.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 0th row of the passed master tkinter.Frame widget to 1.
            master.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the ScrolledFrame widget
            scrolled_frame: ScrolledFrame = ScrolledFrame(master=master)

            # Place the ScrolledFrame in the grid
            scrolled_frame.grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Configure the ScrolledFrame widget
            scrolled_frame.configure(background=Constants.BLUE_GREY["700"])

            # Configure the ScrolledFrame widget's tkinter.Canvas widget
            scrolled_frame.configure_canvas(background=Constants.BLUE_GREY["700"])

            # Configure the ScrolledFrame widget's 'container frame' tkinter.Frame widget
            scrolled_frame.configure_container_frame(
                background=Constants.BLUE_GREY["700"]
            )

            # Update idletasks
            self.update_idletasks()

            # Return the ScrolledFrame widget to the caller
            return scrolled_frame
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_overview_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def create_top_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """
        Creates and configures the main widgets of the top frame.

        This method initializes the main widgets of the top frame within the
        learning session result user interface, setting their layout configuration.

        Args:
            master (tkinter.Frame): The parent widget.

        Returns:
            None
        """
        try:
            # Configure the weight of the 0th column of the passed master tkinter.Frame widget to 1.
            master.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 0th row of the passed master tkinter.Frame widget to 1.
            master.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create a tkinter.Label widget
            label: tkinter.Label = tkinter.Label(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.LARGE_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=master,
                text="Congrats! You've completed this learning session run.",
            )

            # Place the tkinter.Label widget in the grid
            label.grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Update idletasks
            self.update_idletasks()
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_top_frame_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @override
    def create_widgets(self) -> None:
        """
        Creates and configures the main widgets of the learning session result user interface.

        This method creates and configures the main widgets of the learning session result user
        interface, setting their layout configuration and invoking methods to populate
        each frame with its respective widgets.

        Args:
            None

        Returns:
            None

        Raises:
            Exception: If an exception occurs during the creation or configuration of the widgets.
        """
        try:
            # Create the bottom frame widget
            bottom_frame: tkinter.Frame = tkinter.Frame(
                background=Constants.BLUE_GREY["700"],
                height=25,
                master=self,
            )

            # Place the bottom frame widget in the main window
            bottom_frame.grid(
                column=0,
                row=2,
                sticky=NSEW,
            )

            # Create and configure the bottom frame widgets
            self.create_bottom_frame_widgets(master=bottom_frame)

            # Create the center frame widget
            center_frame: tkinter.Frame = tkinter.Frame(
                background=Constants.BLUE_GREY["700"],
                master=self,
            )

            # Place the center frame widget in the main window
            center_frame.grid(
                column=0,
                row=1,
                sticky=NSEW,
            )

            # Create and configure the center frame widgets
            self.create_center_frame_widgets(master=center_frame)

            # Create the top frame widget
            top_frame: tkinter.Frame = tkinter.Frame(
                background=Constants.BLUE_GREY["700"],
                height=25,
                master=self,
            )

            # Place the top frame widget in the main window
            top_frame.grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create and configure the top frame widgets
            self.create_top_frame_widgets(master=top_frame)

            # Update idletasks
            self.update_idletasks()
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e
