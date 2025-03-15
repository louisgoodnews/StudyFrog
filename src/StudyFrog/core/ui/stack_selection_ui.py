"""
Author: lodego
Date: 2025-03-15
"""

import tkinter

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


__all__: List[str] = ["StackSelectionUI"]


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

        # Subscribe to events
        self.subscribe_to_events()

    @override
    def collect_subscriptions(self) -> Dict[Any, Dict[str, Any]]:
        return {
            Events.STACK_CREATED: {
                "function": self.on_stack_creaed,
                "namespace": Constants.GLOBAL_NAMESPACE,
                "persistent": True,
            },
        }

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
            top_frame: tkinter.Frame = UIBuilder.get_frame(
                background=Constants.BLUE_GREY["700"],
                height=25,
                master=self,
            )

            # Create the center frame widget
            center_frame: tkinter.Frame = UIBuilder.get_frame(
                background=Constants.BLUE_GREY["700"],
                master=self,
            )

            # Create the bottom frame widget
            bottom_frame: tkinter.Frame = UIBuilder.get_frame(
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

            self.logger.debug(
                message=f"Got {len(difficulties)} difficulties in '{self.__class__.__name__}'"
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

            self.logger.debug(
                message=f"Got {len(priorities)} priorities in '{self.__class__.__name__}'"
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

            self.logger.debug(
                message=f"Got {len(stacks)} stacks in '{self.__class__.__name__}'"
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_center_frame_widgets' method from '{self.__class__.__name__}': {e}"
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

    def on_stack_creaed(
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
                message=f"Caught an exception while attempting to run 'on_stack_creaed' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e
