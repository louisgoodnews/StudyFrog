"""
Author: lodego
Date: 2025-03-15
"""

import tkinter

from tkinter import ttk
from tkinter.constants import *

from typing import *

from core.difficulty import ImmutableDifficulty
from core.priority import ImmutablePriority
from core.setting import SettingService
from core.stack import ImmutableStack

from utils.base_ui import BaseUI
from core.ui.ui_builder import UIBuilder

from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherNotification
from utils.events import Events
from utils.miscellaneous import Miscellaneous
from utils.navigation import NavigationHistoryItem, NavigationHistoryService
from utils.unified import UnifiedObjectManager


__all__: Final[List[str]] = ["StackSelectionUI"]


class StackSelectionUI(BaseUI):
    """
    A class representing the stack selection user interface (UI) of the application.

    This class is responsible for initializing and configuring the layout of the
    stack selection UI, including setting up the main frames and populating them with
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
        Initializes a new instance of the StackSelectionUI class.

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
            name="stack_selection_ui",
            navigation_item=navigation_item,
            navigation_service=navigation_service,
            setting_service=setting_service,
            unified_manager=unified_manager,
        )

        # Initialize the selected_stacks attribute
        self.selected_stacks: List[ImmutableStack] = []

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

        subscriptions.extend(
            [
                {
                    "event": Events.STACK_CREATED,
                    "function": self.on_stack_created,
                    "namespace": Constants.GLOBAL_NAMESPACE,
                    "persistent": True,
                },
            ]
        )

        return subscriptions

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

            if not top_frame:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create top frame in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Configure the weight of the 0th column to weight 1.
            top_frame.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 0th row to weight 1.
            top_frame.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Place the top frame widget in the main window
            top_frame.grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the center frame widget
            center_frame: Optional[tkinter.Frame] = UIBuilder.get_frame(
                background=Constants.BLUE_GREY["700"],
                master=self,
            )

            if not center_frame:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create center frame in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Configure the weight of the 0th column to weight 1.
            center_frame.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 0th row to weight 1.
            center_frame.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Place the center frame widget in the main window
            center_frame.grid(
                column=0,
                row=1,
                sticky=NSEW,
            )

            # Create the bottom frame widget
            bottom_frame: Optional[tkinter.Frame] = UIBuilder.get_frame(
                background=Constants.BLUE_GREY["700"],
                height=25,
                master=self,
            )

            if not bottom_frame:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create bottom frame in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Configure the weight of the 0th column to weight 1.
            bottom_frame.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 0th row to weight 1.
            bottom_frame.grid_rowconfigure(
                index=0,
                weight=1,
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
        """
        Creates and configures the widgets of the bottom frame.

        This method initializes the Cancel and Start buttons within the bottom frame
        and places them in the grid layout.

        Args:
            master (tkinter.Frame): The parent frame widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to create or configure the widgets.
        """
        try:
            # Configure the weight of the 0th column to 1.
            master.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 0th column to 1.
            master.grid_columnconfigure(
                index=1,
                weight=1,
            )

            # Configure the weight of the 0th row to 1.
            master.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the Cancel button widget
            cancel_button: Optional[tkinter.Button] = UIBuilder.get_button(
                background=Constants.BLUE_GREY["700"],
                command=self.on_cancel_button_click,
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=master,
                relief=FLAT,
                text="Cancel",
            )

            # Check if the Cancel button was created successfully
            if not cancel_button:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create Cancel button in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Place the Cancel button widget in the main window
            cancel_button.grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=W,
            )

            # Create the Start button widget
            start_button: Optional[tkinter.Button] = UIBuilder.get_button(
                background=Constants.BLUE_GREY["700"],
                command=self.on_start_button_click,
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=master,
                relief=FLAT,
                text="Start",
            )

            # Check if the Start button was created successfully
            if not start_button:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create Start button in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Place the Start button widget in the main window
            start_button.grid(
                column=1,
                padx=5,
                pady=5,
                row=0,
                sticky=E,
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
        """
        Creates and configures widgets in the center frame of the stack selection UI.

        This method initializes the label, scrolled frame, separator, difficulty select, and priority select widgets
        within the center frame and places them in the grid layout.

        Args:
            master (tkinter.Frame): The parent frame widget.

        Returns:
            None

        Raises:
            Exception: If an error occurs during widget creation or data lookup.
        """
        try:
            # Configure the weight of the 0th column to 1.
            master.grid_columnconfigure(
                index=0,
                weight=1,
            )

            for index in range(12):
                # Configure the weight of the current row index to 1.
                master.grid_rowconfigure(
                    index=index,
                    weight=1,
                )

            # Create the label widget
            label: Optional[tkinter.Label] = UIBuilder.get_label(
                anchor=W,
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=master,
                text="Select one or more stacks: ",
            )

            # Check if the label was created successfully
            if not label:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create label in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Place the label widget in the main window
            label.grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Create the scrolled frame widgets
            scrolled_frame: Optional[Dict[str, Any]] = UIBuilder.get_scrolled_frame(
                master=master,
            )

            if not scrolled_frame:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create scrolled frame in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Style the scrolled frame widget's canvas
            scrolled_frame["canvas"].configure(background=Constants.BLUE_GREY["700"])

            # Style the scrolled frame widget's frame
            scrolled_frame["frame"].configure(background=Constants.BLUE_GREY["700"])

            # Style the scrolled frame widget's root frame
            scrolled_frame["root"].configure(background=Constants.BLUE_GREY["700"])

            # Place the scrolled frame widget's root frame in the main window
            scrolled_frame["root"].grid(
                column=0,
                padx=5,
                pady=5,
                row=1,
                sticky=NSEW,
            )

            # Get the dispatcher response
            stacks_response: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_GET_ALL_STACKS,
                    namespace=Constants.GLOBAL_NAMESPACE,
                )
            )

            if not stacks_response:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to get stacks in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Get the result from the dispatcher notification
            stacks: List[ImmutableStack] = stacks_response.get_result_by_key(
                key="on_request_get_all_stacks"
            )

            # Iterate over the stacks
            for stack in stacks:
                # Create the stack item widgets
                self.create_stack_item_widgets(
                    master=scrolled_frame["frame"],
                    stack=stack,
                )

            # Create the separator widget
            separator: Optional[ttk.Separator] = UIBuilder.get_separator(
                master=master,
                orient=HORIZONTAL,
            )

            if not separator:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create separator in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Place the separator widget in the main window
            separator.grid(
                column=0,
                padx=5,
                pady=5,
                row=2,
                sticky=EW,
            )

            # Get the dispatcher response
            difficulties_response: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_GET_ALL_DIFFICULTIES,
                    namespace=Constants.GLOBAL_NAMESPACE,
                )
            )

            if not difficulties_response:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to get difficulties in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Get the result from the dispatcher notification
            difficulties: List[ImmutableDifficulty] = (
                difficulties_response.get_result_by_key(
                    key="on_request_get_all_difficulties"
                )
            )

            # Create the difficulty select widgets within the passed master frame
            self.difficulty_select: Optional[Dict[str, Any]] = (
                UIBuilder.get_multi_select_field(
                    label="Difficulties: ",
                    master=master,
                    values=[difficulty["name"] for difficulty in difficulties],
                )
            )

            if not self.difficulty_select:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create difficulty select in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Style the difficulty select widget's button
            self.difficulty_select["select_button"].configure(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                relief=FLAT,
            )

            # Style the difficulty select widget's label
            self.difficulty_select["label"].configure(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
            )

            # Style the difficulty select widget's root frame
            self.difficulty_select["root"].configure(
                background=Constants.BLUE_GREY["700"]
            )

            # Place the difficulty select widget in the main window
            self.difficulty_select["root"].grid(
                column=0,
                padx=5,
                pady=5,
                row=3,
                sticky=NSEW,
            )

            # Get the dispatcher response
            priorities_response: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_GET_ALL_PRIORITIES,
                    namespace=Constants.GLOBAL_NAMESPACE,
                )
            )

            if not priorities_response:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to get priorities in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Get the result from the dispatcher notification
            priorities: List[ImmutablePriority] = priorities_response.get_result_by_key(
                key="on_request_get_all_priorities"
            )

            # Create the priority select widgets within the passed master frame
            self.priority_select: Optional[Dict[str, Any]] = (
                UIBuilder.get_multi_select_field(
                    label="Priorities: ",
                    master=master,
                    values=[priority["name"] for priority in priorities],
                )
            )

            if not self.priority_select:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create priority select in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Style the priority select widget's button
            self.priority_select["select_button"].configure(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                relief=FLAT,
            )

            # Style the priority select widget's label
            self.priority_select["label"].configure(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
            )

            # Style the priority select widget's root frame
            self.priority_select["root"].configure(
                background=Constants.BLUE_GREY["700"]
            )

            # Place the priority select widget in the main window
            self.priority_select["root"].grid(
                column=0,
                padx=5,
                pady=5,
                row=4,
                sticky=NSEW,
            )

            # Create the mode select widget
            self.mode_select: Optional[Dict[str, Any]] = UIBuilder.get_combobox_field(
                label="Mode: ",
                master=master,
                values=Constants.LEARNING_MODES,
                value=Constants.LEARNING_MODES[0],
            )

            if not self.mode_select:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create mode select in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Style the mode select widget's button
            self.mode_select["button"].configure(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                relief=FLAT,
            )

            # Style the mode select widget's combobox
            self.mode_select["combobox"].configure(
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                state="readonly",
            )

            # Style the mode select widget's label
            self.mode_select["label"].configure(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                relief=FLAT,
            )

            # Style the mode select widget's root frame
            self.mode_select["root"].configure(background=Constants.BLUE_GREY["700"])

            # Place the mode select widget in the main window
            self.mode_select["root"].grid(
                column=0,
                padx=5,
                pady=5,
                row=5,
                sticky=NSEW,
            )

            # Create the randomisation check widget
            self.randomisation_check: Optional[Dict[str, Any]] = (
                UIBuilder.get_checkbutton_field(
                    label="Enable randomisation?: ",
                    master=master,
                    namespace=Constants.STACK_SELECTION_NAMESPACE,
                )
            )

            if not self.randomisation_check:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create randomisation check in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Style the randomisation check widget's checkbutton
            self.randomisation_check["checkbutton"].configure(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                relief=FLAT,
            )

            # Style the randomisation check widget's label
            self.randomisation_check["label"].configure(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
            )

            # Style the randomisation check widget's root frame
            self.randomisation_check["root"].configure(
                background=Constants.BLUE_GREY["700"]
            )

            # Place the randomisation check widget in the main window
            self.randomisation_check["root"].grid(
                column=0,
                padx=5,
                pady=5,
                row=6,
                sticky=NSEW,
            )

            # Create the countup check widget
            self.countup_check: Optional[Dict[str, Any]] = (
                UIBuilder.get_checkbutton_field(
                    label="Enable countup timer?: ",
                    master=master,
                    namespace=Constants.STACK_SELECTION_NAMESPACE,
                    on_change_callback=self.on_countup_check_toggle,
                )
            )

            if not self.countup_check:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create countup check in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Style the countup check widget's checkbutton
            self.countup_check["checkbutton"].configure(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                relief=FLAT,
            )

            # Style the countup check widget's label
            self.countup_check["label"].configure(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
            )

            # Style the countup check widget's root frame
            self.countup_check["root"].configure(background=Constants.BLUE_GREY["700"])

            # Place the countup check widget in the main window
            self.countup_check["root"].grid(
                column=0,
                padx=5,
                pady=5,
                row=7,
                sticky=NSEW,
            )

            # Create the countdown check widget
            self.countdown_check: Optional[Dict[str, Any]] = (
                UIBuilder.get_checkbutton_field(
                    label="Enable countdown timer?: ",
                    master=master,
                    namespace=Constants.STACK_SELECTION_NAMESPACE,
                    on_change_callback=self.on_countdown_check_toggle,
                )
            )

            if not self.countdown_check:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create countdown check in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Style the countdown check widget's checkbutton
            self.countdown_check["checkbutton"].configure(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                relief=FLAT,
            )

            # Style the countdown check widget's label
            self.countdown_check["label"].configure(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
            )

            # Style the countdown check widget's root frame
            self.countdown_check["root"].configure(
                background=Constants.BLUE_GREY["700"]
            )

            # Place the countdown check widget in the main window
            self.countdown_check["root"].grid(
                column=0,
                padx=5,
                pady=5,
                row=8,
                sticky=NSEW,
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_center_frame_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def create_stack_item_widgets(
        self,
        master: tkinter.Misc,
        stack: ImmutableStack,
    ) -> None:
        """
        Creates and configures widgets for a single stack item.

        This method initializes a frame for the stack item and populates it with
        labels displaying various stack attributes, such as priority, difficulty,
        and status, each represented by an emoji.

        Args:
            master (tkinter.Misc): The parent widget.
            stack (ImmutableStack): The immutable stack data.

        Returns:
            None

        Raises:
            Exception: If an error occurs during widget creation or data lookup.
        """
        try:
            # Create a tkinter.Frame widget for the stack item
            frame: Optional[tkinter.Frame] = UIBuilder.get_frame(
                background=Constants.GREY["default"],
                master=master,
            )

            if not frame:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create stack item frame in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Create a tkinter.Checkbutton widget for the stack item
            checkbutton: Optional[tkinter.Checkbutton] = UIBuilder.get_checkbutton(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=frame,
                relief=FLAT,
                text="",
                variable=UIBuilder.get_bool_variable(),
            )

            if not checkbutton:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create stack item checkbutton in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            checkbutton.bind(
                func=lambda event: self.on_stack_item_checkbutton_click(stack=stack),
                sequence="<ButtonRelease-1>",
            )

            # Place the checkbutton in the frame
            checkbutton.grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
            )

            # Dispatch events to lookup stack attribute details
            difficulty_notification: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_DIFFICULTY_LOOKUP,
                    id=stack["difficulty"],
                    namespace=Constants.GLOBAL_NAMESPACE,
                )
            )

            if not difficulty_notification:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to lookup difficulty in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            priority_notification: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_PRIORITY_LOOKUP,
                    id=stack["priority"],
                    namespace=Constants.GLOBAL_NAMESPACE,
                )
            )

            if not priority_notification:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to lookup priority in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            status_notification: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_STATUS_LOOKUP,
                    id=stack["status"],
                    namespace=Constants.GLOBAL_NAMESPACE,
                )
            )

            if not status_notification:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to lookup status in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Iterate over stack attributes to configure the frame and create labels
            for (
                index,
                column,
            ) in enumerate(
                iterable=[
                    "icon",
                    "name",
                    "priority",
                    "difficulty",
                    "last_viewed_at",
                    "status",
                    "due_by",
                ],
                start=1,
            ):
                # Configure the frame widget's column to weight 1
                frame.grid_columnconfigure(
                    index=index,
                    weight=1,
                )

                # Convert stack data to database format
                data: Dict[str, Any] = Miscellaneous.convert_to_db_format(
                    data=stack.to_dict(
                        exclude=[
                            "_logger",
                        ]
                    )
                )

                # Determine the text to display based on column type
                if column == "priority":
                    text = priority_notification.get_result_by_key(
                        key="on_request_priority_lookup"
                    )[0]["emoji"]
                elif column == "difficulty":
                    text = difficulty_notification.get_result_by_key(
                        key="on_request_difficulty_lookup"
                    )[0]["emoji"]
                elif column == "status":
                    text = status_notification.get_result_by_key(
                        key="on_request_status_lookup"
                    )[0]["emoji"]
                else:
                    text = data[column]

                # Create a tkinter.Label widget for each stack attribute
                label: Optional[tkinter.Label] = UIBuilder.get_label(
                    background=Constants.BLUE_GREY["700"],
                    font=(
                        Constants.DEFAULT_FONT_FAMILY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    foreground=Constants.WHITE,
                    master=frame,
                    text=text,
                )

                if not label:
                    # Log a warning message
                    self.logger.warning(
                        message=f"Failed to create stack item label in '{self.__class__.__name__}'. This is likely a bug."
                    )

                    # Return early
                    return

                # Place the label widget in the stack item frame
                label.grid(
                    column=index,
                    row=0,
                    sticky=NSEW,
                )

                # Bind the label widget to a command that dispatches an event when clicked
                label.bind(
                    func=lambda event, obj=stack: self.dispatcher.dispatch(
                        direction="forward",
                        event=Events.REQUEST_VALIDATE_NAVIGATION,
                        namespace=Constants.GLOBAL_NAMESPACE,
                        source="dashboard_ui",
                        stack=obj,
                        target="edit_ui",
                    ),
                    sequence="<ButtonRelease-1>",
                )

            # Place the stack item frame within the new stacks frame
            frame.grid(
                column=0,
                padx=5,
                pady=10,
                row=len(master.winfo_children()),
                sticky=NSEW,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to create stack item widgets: {e}"
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
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_top_frame_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def on_cancel_button_click(self) -> None:
        """
        Handles the click event of the "Cancel" button.

        If the user clicks "Cancel", the method will create an okay/cancel dialog
        to confirm the cancellation. If the user clicks "Okay" in the dialog,
        the method will log an info message and destroy the current window.

        Returns:
            None
        """
        try:
            # Create an okay/cancel dialog to confirm the cancellation
            okay_cancel: Optional[Dict[str, Any]] = UIBuilder.get_okay_cancel(
                dispatcher=self.dispatcher,
                message="Are you sure you want to cancel?",
                title="Confirm cancel",
            )

            if not okay_cancel:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create okay/cancel dialog in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            if okay_cancel["getter"]() == "okay":
                # Log an info message:
                self.logger.info(
                    message=f"Stack selection cancelled in '{self.__class__.__name__}'."
                )

                if isinstance(
                    self.master,
                    tkinter.Toplevel,
                ):
                    # Destroy the current window
                    self.master.destroy()
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_cancel_button_click' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def on_countdown_check_toggle(
        self,
        value: bool,
    ) -> None:
        """
        Handles the toggle event for the countdown checkbutton.

        This method ensures that the countup checkbutton is not
        selected when the countdown checkbutton is toggled.

        Args:
            value (bool): The new value for the countdown checkbutton.

        Returns:
            None

        Raises:
            Exception: If an error occurs during the handling of the toggle event.
        """
        try:
            # Check if the countup checkbutton is selected
            if self.countdown_check["getter"]() == self.countup_check["getter"]():
                # Deselect the countup checkbutton
                self.countup_check["setter"](value=not value)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_countdown_check_toggle' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def on_countup_check_toggle(
        self,
        value: bool,
    ) -> None:
        """
        Handles the toggle event for the countup checkbutton.

        This method ensures that the countdown checkbutton is not
        selected when the countup checkbutton is toggled.

        Args:
            value (bool): The new value for the countup checkbutton.

        Returns:
            None

        Raises:
            Exception: If an error occurs during the handling of the toggle event.
        """
        try:
            # Check if the countup and countdown checkbuttons have the same state
            if self.countup_check["getter"]() == self.countdown_check["getter"]():
                # Set the countdown checkbutton to the opposite state
                self.countdown_check["setter"](value=not value)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_countup_check_toggle' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def on_stack_item_checkbutton_click(
        self,
        stack: ImmutableStack,
    ) -> None:
        """
        Handles the click event of a stack item checkbutton and adds or removes the stack from the list of selected stacks.

        Args:
            stack (ImmutableStack): The stack that was clicked

        Returns:
            None
        """
        try:
            # Check if the stack is currently selected
            if stack not in self.selected_stacks:
                # Add the stack to the list of selected stacks
                self.selected_stacks.append(stack)

                # Log an info message:
                self.logger.info(
                    message=f"Stack '{stack.name}' with ID ({stack.id}) added to selected stacks in '{self.__class__.__name__}'."
                )
            else:
                # Remove the stack from the list of selected stacks
                self.selected_stacks.remove(stack)

                # Log an info message:
                self.logger.info(
                    message=f"Stack '{stack.name}' with ID ({stack.id}) removed from selected stacks in '{self.__class__.__name__}'."
                )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_stack_item_checkbutton_click' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def on_stack_created(
        self,
        stack: ImmutableStack,
    ) -> None:
        try:
            # TODO:
            #   - Update the UI to display the new stack
            #   - Add the new stack to the list of available stacks
            #   - Add the new stack to list of selected stacks
            #   - Open a Toplevel to the SearchUI to select stack contents
            #   - Add the selected stack contents to the new stack
            #   - Save the new stack
            #   - Close the Toplevel
            pass
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_stack_created' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def on_start_button_click(self) -> None:
        """
        Handles the event when the 'Start' button is clicked.

        This function dispatches a navigation request to the global namespace
        with the target 'learning_session_ui' and the source 'stack_selection_ui'.

        Returns:
            None

        Raises:
            Exception: If an exception occurs during the dispatching of the event.
        """
        try:
            # Initialize the kwargs dictionary
            kwargs: Dict[str, Any] = {
                "direction": Constants.FORWARD_DIRECTION,
                "event": Events.REQUEST_VALIDATE_NAVIGATION,
                "mode": Miscellaneous.any_to_snake(string=self.mode_select["getter"]()),
                "namespace": Constants.GLOBAL_NAMESPACE,
                "settings": {
                    "enable_randomisation": self.randomisation_check["getter"](),
                    "enable_countdown": self.countdown_check["getter"](),
                    "enable_countup": self.countup_check["getter"](),
                },
                "source": "stack_selection_ui",
                "stacks": self.selected_stacks,
                "target": "learning_session_ui",
            }

            # Get the priority selection
            priority_selection: Optional[List[str]] = self.priority_select["getter"]()

            if not priority_selection:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to get priority selection in '{self.__class__.__name__}'. This is likely due to no value being selected."
                )
            else:
                # Dispatch a request to look up the priority by name
                priority_notification: Optional[DispatcherNotification] = (
                    self.dispatcher.dispatch(
                        event=Events.REQUEST_PRIORITY_LOOKUP,
                        namespace=Constants.GLOBAL_NAMESPACE,
                        name=priority_selection,
                    )
                )

                if not priority_notification:
                    # Log a warning message
                    self.logger.warning(
                        message=f"Priority with name '{priority_selection}' not found in '{self.__class__.__name__}'."
                    )
                else:
                    # Get the priority from the notification
                    priority: Union[ImmutablePriority, List[ImmutablePriority]] = (
                        priority_notification.get_one_and_only_result()
                    )

                    # Store the priority in the kwargs dictionary
                    kwargs["priorities"] = (
                        priority if isinstance(priority, list) else [priority]
                    )

            # Get the difficulty selection
            difficulty_selection: Optional[List[str]] = self.difficulty_select[
                "getter"
            ]()

            if not difficulty_selection:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to get difficulty selection in '{self.__class__.__name__}'. This is likely due to no value being selected."
                )
            else:
                # Dispatch a request to look up the difficulty by name
                difficulty_notification: Optional[DispatcherNotification] = (
                    self.dispatcher.dispatch(
                        event=Events.REQUEST_DIFFICULTY_LOOKUP,
                        namespace=Constants.GLOBAL_NAMESPACE,
                        name=difficulty_selection,
                    )
                )

                if not difficulty_notification:
                    # Log a warning message
                    self.logger.warning(
                        message=f"Difficulty with name '{difficulty_selection}' not found in '{self.__class__.__name__}'."
                    )
                else:
                    # Get the difficulty from the notification
                    difficulty: Union[
                        ImmutableDifficulty, List[ImmutableDifficulty]
                    ] = difficulty_notification.get_one_and_only_result()

                    # Store the difficulty in the kwargs dictionary
                    kwargs["difficulties"] = (
                        difficulty if isinstance(difficulty, list) else [difficulty]
                    )

            # Check if "difficulties" key is missing (to prevent it from being None)
            if "difficulties" not in kwargs:
                # Set the difficulties to an empty list
                kwargs["difficulties"] = []

            # Check if "priorities" key is missing (to prevent it from being None)
            if "priorities" not in kwargs:
                # Set the priorities to an empty list
                kwargs["priorities"] = []

            # Dispatch the REQUEST_VALIDATE_NAVIGATION event
            self.dispatcher.dispatch(**kwargs)

            if isinstance(
                self.master,
                tkinter.Toplevel,
            ):
                # Destroy the current window
                self.master.destroy()
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_start_button_click' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e
