"""
Author: lodego
Date: 2025-02-08
"""

import tkinter

from tkinter import ttk

from tkinter.constants import *

from typing import *

from core.setting import SettingService

from core.ui.ui_registry import UIRegistry
from core.ui.topbar import TopBar

from core.ui.ui_builder import UIBuilder
from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherNotification
from utils.events import Events
from utils.logger import Logger
from utils.navigation import NavigationHistoryService
from utils.unified import UnifiedObjectManager


__all__: List[str] = ["MainUI"]


class MainUI(tkinter.Tk):
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

        # Call the parent class constructor
        super().__init__()

        # Initialize a logger instance
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed dispatcher instance in an instance variable
        self.dispatcher: Dispatcher = dispatcher

        # Store the passed navigation service instance in an instance variable
        self.navigation_service: NavigationHistoryService = navigation_service

        # Store the passed setting service instance in an instance variable
        self.setting_service: SettingService = setting_service

        # Store the passed unified object manager instance in an instance variable
        self.unified_manager: UnifiedObjectManager = unified_manager

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
        self.wm_protocol(
            name="WM_DELETE_WINDOW",
            func=self.on_exit_ui_mainloop,
        )

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
            navigation_service=self.navigation_service,
            unified_manager=self.unified_manager,
        )

        # Grid the "TopBar" widget in the "Top Frame" frame widget
        self.topbar.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Register a subscription for the APPLICATION_STOPPED event in the global namespace
        self.dispatcher.register(
            event=Events.APPLICATION_STOPPED,
            function=self.on_application_stopped,
            namespace=Constants.GLOBAL_NAMESPACE,
            persistent=True,
        )

        # Register a subscription for the REQUEST_VALIDATE_NAVIGATION event in the global namespace
        self.dispatcher.register(
            event=Events.REQUEST_VALIDATE_NAVIGATION,
            function=self.on_request_validate_navigation,
            namespace=Constants.GLOBAL_NAMESPACE,
            persistent=True,
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
                self.clear(name="center_frame")

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
