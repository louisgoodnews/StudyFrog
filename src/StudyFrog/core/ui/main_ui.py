"""
Author: lodego
Date: 2025-02-08
"""

import tkinter

from tkinter.constants import *

from typing import *

from core.setting import SettingService

from core.ui.base_ui import BaseUI
from core.ui.ui_registry import UIRegistry
from core.ui.topbar import TopBar

from core.ui.ui_builder import UIBuilder
from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherNotification
from utils.events import Events
from utils.navigation import NavigationHistoryService
from utils.unified import UnifiedObjectManager


__all__: List[str] = ["MainUI"]


class MainUI(BaseUI):
    """
    The main user interface (UI) of the StudyFrog application.

    Attributes:
        dispatcher (Dispatcher): The dispatcher instance.
        logger (Logger): The logger instance.
        navigation_service (NavigationHistoryService): The navigation history service instance.
        setting_service (SettingService): The setting service instance.
        unified_manager (UnifiedObjectManager): The unified object manager instance.
    """

    def __init__(
        self,
        dispatcher: Dispatcher,
        navigation_service: NavigationHistoryService,
        setting_service: SettingService,
        unified_manager: UnifiedObjectManager,
    ) -> None:
        """
        Initializes a new instance of the MainUI class.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.
            navigation_service (NavigationHistoryService): The navigation history service instance.
            setting_service (SettingService): The setting service instance.
            unified_manager (UnifiedObjectManager): The unified object manager instance.

        Returns:
            None
        """

        # Get the root window
        root: Optional[tkinter.Tk] = UIBuilder.get_tk()

        if not root:
            # Log a warning message
            self.logger.warning(
                message=f"Failed to get root window in '{self.__class__.__name__}'. This is likely a bug."
            )

            # Return early
            return

        # Configure the root window's 1st column to weight 1
        root.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the root window's 1st row to weight 1
        root.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Set the window geometry
        root.wm_geometry(newGeometry=Constants.DEFAULT_GEOMETRY)

        # Register a handler for the "WM_DELETE_WINDOW" event
        root.wm_protocol(
            name="WM_DELETE_WINDOW",
            func=self.on_exit_ui_mainloop,
        )

        # Set the window title
        root.wm_title(string=Constants.APPLICATION_NAME)

        # Call the parent class constructor
        super().__init__(
            dispatcher=dispatcher,
            master=root,
            name="main_ui",
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
                "event": Events.APPLICATION_STOPPED,
                "function": self.on_application_stopped,
                "namespace": Constants.GLOBAL_NAMESPACE,
                "persistent": True,
            },
            {
                "event": Events.REQUEST_VALIDATE_NAVIGATION,
                "function": self.on_request_validate_navigation,
                "namespace": Constants.GLOBAL_NAMESPACE,
                "persistent": True,
            },
        ]

    @override
    def configure_grid(self) -> None:
        """
        Configures the grid layout for the MainUI widget.

        This method configures the grid layout for the MainUI widget by setting
        the weights and alignment of the columns and rows.
        """

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

    def clear_center_frame(self) -> None:
        """
        Clears the center frame.

        This method removes all children widgets from the center frame, clearing
        its content.

        Returns:
            None
        """

        # Get a list of the children widgets in the center frame
        children: List[tkinter.Misc] = self.center_frame.winfo_children()

        # Check if the list is empty
        if len(children) == 0:
            # Return early if empty
            return

        # Iterate over the children widgets
        for child in children:
            # Destroy the widget
            child.destroy()

    @override
    def create_widgets(self) -> None:
        """
        Creates and configures the main frames of the MainUI widget.

        This method initializes the top, center, and bottom frames within the
        MainUI widget, setting their layout configuration and invoking methods
        to populate each frame with its respective widgets.

        Args:
            None

        Returns:
            None
        """

        # Create the "Top Frame" frame widget
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

        # Grid the "Top Frame" frame widget in the MainUI widget
        top_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create the "Center Frame" frame widget
        self.center_frame: Optional[tkinter.Frame] = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        if not self.center_frame:
            # Log a warning message
            self.logger.warning(
                message=f"Failed to create center frame in '{self.__class__.__name__}'. This is likely a bug."
            )

            # Return early
            return

        # Configure the "Center Frame" frame widget's 1st column to weight 1
        self.center_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Configure the "Center Frame" frame widget's 1st column to weight 1
        self.center_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Grid the "Center Frame" frame widget in the MainUI widget
        self.center_frame.grid(
            column=0,
            row=1,
            sticky=NSEW,
        )

        # Create the "Bottom Frame" frame widget
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

        # Configure the "Bottom Frame" frame widget's 1st column to weight 1
        bottom_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Grid the "Bottom Frame" frame widget in the MainUI widget
        bottom_frame.grid(
            column=0,
            row=2,
            sticky=NSEW,
        )

        # Create the top frame widgets
        self.create_top_frame_widgets(master=top_frame)

    def create_top_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """
        Creates and configures the widgets for the top frame.

        This method creates and configures the widgets that will be displayed
        in the top frame of the MainUI widget. It is responsible for setting
        up the layout and behavior of the widgets.

        Args:
            master (tkinter.Frame): The parent frame widget.

        Returns:
            None
        """

        # Create the "TopBar" topbar widget
        topbar: TopBar = TopBar(
            dispatcher=self.dispatcher,
            master=master,
            navigation_service=self.navigation_service,
            unified_manager=self.unified_manager,
        )

        # Grid the "TopBar" widget in the "Top Frame" frame widget
        topbar.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

    def on_application_stopped(self) -> None:
        """
        A handler method for the APPLICATION_STOPPED event.

        Quits the Tcl interpreter. All widgets will be destroyed.

        Returns:
            None
        """

        # Quit the Tcl interpreter and destroy all widgets
        super().quit()

    def on_exit_ui_mainloop(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        A handler method for the REQUEST_EXIT_UI_MAINLOOP event.

        Dispatches the REQUEST_APPLICATION_STOP event in the global namespace
        and quits the Tcl interpreter. All widgets will be destroyed.

        Args:
            event (Optional[tkinter.Event], optional): The event that triggered this handler. Defaults to None.

        Returns:
            None
        """

        # Dispatch the REQUEST_APPLICATION_STOP event in the global namespace
        self.dispatcher.dispatch(
            event=Events.REQUEST_APPLICATION_STOP,
            namespace=Constants.GLOBAL_NAMESPACE,
        )

        # Quit the Tcl interpreter and destroy all widgets
        super().quit()

    def on_request_validate_navigation(
        self,
        direction: str,
        source: str,
        target: str,
        master: Optional[tkinter.Misc] = None,
        **kwargs,
    ) -> Optional[Any]:
        """
        Validates the navigation request and initializes the new UI if valid.

        Args:
            direction (str): The direction of the navigation, either "backward" or "forward".
            source (str): The source of the navigation request.
            target (str): The target of the navigation request.
            master (Optional[tkinter.Misc], optional): The optional master widget to use. Defaults to None.
            **kwargs: Any additional keyword arguments to pass to the UI class.

        Returns:
            Optional[Any]: None if an exception occurs, otherwise any value returned by the UI class.
        """

        try:
            # Check if the direction is valid
            if direction not in [
                "backward",
                "forward",
            ]:
                # Raise an exception indicating an invalid direction
                raise ValueError(
                    f"Invalid direction: {direction}. Must be either 'backward' or 'forward'."
                )

            # Check, if a master is given
            if not master:
                # Clear the MainUI's center frame if no other master is given
                self.clear_center_frame()

                # Set the master to the MainUI center frame
                master = self.center_frame

            # Attempt to get the UI class
            ui_class: Optional[Type[tkinter.Misc]] = UIRegistry.get(name=target)

            if not ui_class:
                # Raise an exception indicating an invalid target
                raise ValueError(f"Invalid target: {target}. Must be a valid UI name.")

            # Dispatch the REQUEST_BACKWARD_NAVIGATION or REQUEST_FORWARD_NAVIGATION event in the global namespace
            response: DispatcherNotification = self.dispatcher.dispatch(
                event=(
                    Events.REQUEST_BACKWARD_NAVIGATION
                    if direction == "backward"
                    else Events.REQUEST_FORWARD_NAVIGATION
                ),
                namespace=Constants.GLOBAL_NAMESPACE,
                navigation_service=self.navigation_service,
                source=source,
                target=target,
                unified_manager=self.unified_manager,
                **kwargs,
            )

            # Initialize the UI class
            ui_class(
                dispatcher=self.dispatcher,
                master=master,
                navigation_service=self.navigation_service,
                setting_service=self.setting_service,
                unified_manager=self.unified_manager,
                navigation_item=list(response["result"].values())[0],
                **kwargs,
            )

            # Dispatch the NAVIGATE_VALIDATE_SUCCESS event in the global namespace indicating a success
            self.dispatcher.dispatch(
                event=Events.NAVIGATE_VALIDATE_SUCCESS,
                namespace=Constants.GLOBAL_NAMESPACE,
            )

            # Dispatch the "NAVIGATION_COMPLETED" event in the global namespace indicating a success
            self.dispatcher.dispatch(
                event=Events.NAVIGATION_COMPLETED,
                namespace=Constants.GLOBAL_NAMESPACE,
            )
        except Exception as e:
            # Log an error message indicating an exception has ocurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_request_validate_navigation' method from '{self.__class__.__name__}': {e}"
            )

            # Dispatch the NAVIGATE_VALIDATE_FAILURE event in the global namespace indicating a failure
            self.dispatcher.dispatch(
                event=Events.NAVIGATE_VALIDATE_FAILURE,
                namespace=Constants.GLOBAL_NAMESPACE,
            )

            # Return None indicating an exception has ocurred
            return None
