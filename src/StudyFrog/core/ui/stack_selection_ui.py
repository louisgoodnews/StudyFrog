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

from core.ui.base_ui import BaseUI
from core.ui.ui_builder import UIBuilder

from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherNotification
from utils.events import Events
from utils.logger import Logger
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
        """

        return [
            {
                "event": Events.STACK_CREATED,
                "function": self.on_stack_created,
                "namespace": Constants.GLOBAL_NAMESPACE,
                "persistent": True,
            },
        ]

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
                    Constants.DEFAULT_FONT_FAMILIY,
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
                    Constants.DEFAULT_FONT_FAMILIY,
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

            # Configure the weight of the 1st row to 0.
            master.grid_rowconfigure(
                index=1,
                weight=0,
            )

            # Configure the weight of the 2nd row to 0.
            master.grid_rowconfigure(
                index=2,
                weight=0,
            )

            # Configure the weight of the 3rd row to 0.
            master.grid_rowconfigure(
                index=3,
                weight=0,
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
                row=0,
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
            stacks: List[ImmutableStack] = stacks_response.get_result(
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
                row=1,
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
            difficulties: List[ImmutableDifficulty] = difficulties_response.get_result(
                key="on_request_get_all_difficulties"
            )

            # Create the difficulty select widgets within the passed master frame
            difficulty_select: Optional[Dict[str, Any]] = (
                UIBuilder.get_multi_select_field(
                    label="Difficulties: ",
                    master=master,
                    values=[difficulty["name"] for difficulty in difficulties],
                )
            )

            if not difficulty_select:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create difficulty select in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Style the difficulty select widget's button
            difficulty_select["select_button"].configure(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILIY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                relief=FLAT,
            )

            # Style the difficulty select widget's label
            difficulty_select["label"].configure(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILIY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
            )

            # Style the difficulty select widget's root frame
            difficulty_select["root"].configure(background=Constants.BLUE_GREY["700"])

            # Place the difficulty select widget in the main window
            difficulty_select["root"].grid(
                column=0,
                padx=5,
                pady=5,
                row=2,
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
            priorities: List[ImmutablePriority] = priorities_response.get_result(
                key="on_request_get_all_priorities"
            )

            # Create the priority select widgets within the passed master frame
            priority_select: Optional[Dict[str, Any]] = (
                UIBuilder.get_multi_select_field(
                    label="Priorities: ",
                    master=master,
                    values=[priority["name"] for priority in priorities],
                )
            )

            if not priority_select:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create priority select in '{self.__class__.__name__}'. This is likely a bug."
                )

                # Return early
                return

            # Style the priority select widget's button
            priority_select["select_button"].configure(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILIY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                relief=FLAT,
            )

            # Style the priority select widget's label
            priority_select["label"].configure(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILIY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
            )

            # Style the priority select widget's root frame
            priority_select["root"].configure(background=Constants.BLUE_GREY["700"])

            # Place the priority select widget in the main window
            priority_select["root"].grid(
                column=0,
                padx=5,
                pady=5,
                row=3,
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
            frame: tkinter.Frame = UIBuilder.get_frame(
                background=Constants.GREY["default"],
                master=master,
            )

            # Dispatch events to lookup stack attribute details
            difficulty_notification: DispatcherNotification = self.dispatcher.dispatch(
                event=Events.REQUEST_DIFFICULTY_LOOKUP,
                id=stack["difficulty"],
                namespace=Constants.GLOBAL_NAMESPACE,
            )
            priority_notification: DispatcherNotification = self.dispatcher.dispatch(
                event=Events.REQUEST_PRIORITY_LOOKUP,
                id=stack["priority"],
                namespace=Constants.GLOBAL_NAMESPACE,
            )
            status_notification: DispatcherNotification = self.dispatcher.dispatch(
                event=Events.REQUEST_STATUS_LOOKUP,
                id=stack["status"],
                namespace=Constants.GLOBAL_NAMESPACE,
            )

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
                ]
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
                    text = priority_notification.get_result(
                        key="on_request_priority_lookup"
                    )[0]["emoji"]
                elif column == "difficulty":
                    text = difficulty_notification.get_result(
                        key="on_request_difficulty_lookup"
                    )[0]["emoji"]
                elif column == "status":
                    text = status_notification.get_result(
                        key="on_request_status_lookup"
                    )[0]["emoji"]
                else:
                    text = data[column]

                # Create a tkinter.Label widget for each stack attribute
                label: tkinter.Label = UIBuilder.get_label(
                    background=Constants.BLUE_GREY["700"],
                    font=(
                        Constants.DEFAULT_FONT_FAMILIY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    foreground=Constants.WHITE,
                    master=frame,
                    text=text,
                )

                # Place the label widget in the stack item frame
                label.grid(
                    column=index,
                    row=0,
                    sticky=NSEW,
                )

                # Bind the label widget to a command that dispatches an event when clicked
                label.bind(
                    func=lambda event, stack=stack: self.dispatcher.dispatch(
                        direction="forward",
                        event=Events.REQUEST_VALIDATE_NAVIGATION,
                        namespace=Constants.GLOBAL_NAMESPACE,
                        source="dashboard_ui",
                        stack=stack,
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
        try:
            pass
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_cancel_button_click' method from '{self.__class__.__name__}': {e}"
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
            # Dispatch the REQUEST_VALIDATE_NAVIGATION event
            self.dispatcher.dispatch(
                direction=Constants.FORWARD_DIRECTION,
                event=Events.REQUEST_VALIDATE_NAVIGATION,
                namespace=Constants.GLOBAL_NAMESPACE,
                source="stack_selection_ui",
                target="learning_session_ui",
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_start_button_click' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e
