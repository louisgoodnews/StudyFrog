"""
Author: lodego
Date: 2025-02-08
"""

import tkinter

from tkinter.constants import *
from typing import *

from core.difficulty import ImmutableDifficulty
from core.priority import ImmutablePriority
from core.setting import SettingService
from core.stack import ImmutableStack
from core.status import ImmutableStatus

from utils.base_ui import BaseUI

from core.ui.frames.frames import ScrolledFrame, TabbedFrame
from core.ui.miscellaneous import DateClockWidget

from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherNotification
from utils.events import Events
from utils.miscellaneous import Miscellaneous
from utils.navigation import NavigationHistoryItem, NavigationHistoryService
from utils.unified import UnifiedObjectFactory, UnifiedObjectManager


__all__: Final[List[str]] = ["DashboardUI"]


class DashboardUI(BaseUI):
    """
    A class representing the dashboard user interface (UI) of the application.

    Atrributes:
        dispatcher (Dispatcher): The dispatcher instance.
        logger (Logger): The logger instance.
        navigation_item (NavigationHistoryItem): The navigation history item instance.
        navigation_service (NavigationHistoryService): The navigation history service instance.
        setting_service (SettingService): The setting service instance.
        unified_factory (UnifiedObjectFactory): The unified factory instance.
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
            unified_factory (UnifiedObjectFactory): The unified factory instance.
            unified_manager (UnifiedObjectManager): The unified manager instance.
            **kwargs: Any additional keyword arguments.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            dispatcher=dispatcher,
            master=master,
            name="dashboard_ui",
            navigation_item=navigation_item,
            navigation_service=navigation_service,
            setting_service=setting_service,
            unified_factory=unified_factory,
            unified_manager=unified_manager,
        )

        # Lookup the new stacks
        self.lookup_new_stacks()

        # Lookup the recently viewed stacks
        self.lookup_recently_viewed_stacks()

        # Lookup the completed stacks
        self.lookup_completed_stacks()

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
                }
            ]
        )

        return subscriptions

    @override
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

    @override
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
        top_frame: tkinter.Frame = tkinter.Frame(
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
        center_frame: tkinter.Frame = tkinter.Frame(
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
        bottom_frame: tkinter.Frame = tkinter.Frame(
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
        left_frame: tkinter.Frame = tkinter.Frame(
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
        new_button: tkinter.Button = tkinter.Button(
            background=Constants.BLUE_GREY["700"],
            command=lambda: self.dispatcher.dispatch(
                direction="forward",
                event=Events.REQUEST_VALIDATE_NAVIGATION,
                master=tkinter.Toplevel(),
                namespace=Constants.GLOBAL_NAMESPACE,
                source="dashboard_ui",
                target="create_ui",
                type="stack",
            ),
            font=(
                Constants.DEFAULT_FONT_FAMILY,
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
        recent_button: tkinter.Button = tkinter.Button(
            background=Constants.BLUE_GREY["700"],
            command=lambda: self.dispatcher.dispatch(
                direction="forward",
                event=Events.REQUEST_VALIDATE_NAVIGATION,
                master=tkinter.Toplevel(),
                namespace=Constants.GLOBAL_NAMESPACE,
                source="dashboard_ui",
                target="search_ui",
                type="recent:staple",
            ),
            font=(
                Constants.DEFAULT_FONT_FAMILY,
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
        right_frame: tkinter.Frame = tkinter.Frame(
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
        top_frame: tkinter.Frame = tkinter.Frame(
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

        # Create a TabbedFrame widget
        tabbed_frame: TabbedFrame = TabbedFrame(
            master=right_frame,
        )

        # Place the TabbedFrame widget in the master frame
        tabbed_frame.grid(
            column=0,
            row=1,
            sticky=NSEW,
        )

        # Configure the TabbedFrame widget's 1st column to weight 1
        tabbed_frame.container.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the TabbedFrame widget's 1st row to weight 1
        tabbed_frame.container.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Configure the TabbedFrame widget's "Container Frame" widget
        tabbed_frame.configure_container(background=Constants.BLUE_GREY["700"])

        # Configure the TabbedFrame widget's "Top Frame" widget
        tabbed_frame.configure_top_frame(background=Constants.BLUE_GREY["700"])

        # Create the TabbedFrame widgets
        self.create_tabbed_frame_widgets(master=tabbed_frame)

    def create_tabbed_frame_widgets(
        self,
        master: TabbedFrame,
    ) -> None:
        """
        Creates and configures the main widgets of the TabbedFrame.

        This method initializes the main widgets of the TabbedFrame within the
        dashboard UI, setting their layout configuration.

        Args:
            master (TabbedFrame): The parent widget assembly dictionary.

        Returns:
            None
        """
        try:
            # Create the "New Stacks" frame widget
            new_stacks_frame: tkinter.Frame = tkinter.Frame(
                background=Constants.BLUE_GREY["700"],
                master=master.container,
            )

            # Add the "New Stacks" frame widget to the TabbedFrame
            master.add(
                label="My New Stacks",
                widget=new_stacks_frame,
            )

            # Configure the "My New Stacks" button
            master.configure_button(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                name="My New Stacks",
                relief=FLAT,
            )

            # Create the "Recently Viewed" frame widget
            recently_viewed_frame: tkinter.Frame = tkinter.Frame(
                background=Constants.BLUE_GREY["700"],
                master=master.container,
            )

            # Add the "Recently Viewed" frame widget to the TabbedFrame
            master.add(
                label="Recently Viewed",
                widget=recently_viewed_frame,
            )

            # Configure the "Recently Viewed" button
            master.configure_button(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                name="Recently Viewed",
                relief=FLAT,
            )

            # Create the "Completed Stacks" frame widget
            completed_stacks_frame: tkinter.Frame = tkinter.Frame(
                background=Constants.BLUE_GREY["700"],
                master=master.container,
            )

            # Add the "Completed Stacks" frame widget to the TabbedFrame
            master.add(
                label="Completed Stacks",
                widget=completed_stacks_frame,
            )

            # Configure the "Completed Stacks" button
            master.configure_button(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                name="Completed Stacks",
                relief=FLAT,
            )

            # Create the "New Stacks" frame widgets
            self.create_new_stacks_frame_widgets(master=new_stacks_frame)

            # Create the "Recently Viewed" frame widgets
            self.create_recently_viewed_stacks_frame_widgets(
                master=recently_viewed_frame
            )

            # Create the "Completed Stacks" frame widgets
            self.create_completed_stacks_frame_widgets(master=completed_stacks_frame)
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_tabbed_frame_widgets' method from '{self.__class__.__name__}' class: {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def create_new_stacks_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Creates and configures the main widgets of the new stacks frame.

        This method initializes the main widgets of the new stacks frame
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

        # Configure the master widget's 1st row to weight 0
        master.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the master widget's 2nd row to weight 1
        master.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Create a tkinter.Frame widget
        frame: tkinter.Frame = tkinter.Frame(master=master)

        for (
            index,
            column,
        ) in enumerate(
            iterable=[
                "icon",
                "name",
                "priority",
                "difficulty",
                "last viewed at",
                "status",
                "due by",
            ]
        ):
            # Configure the frame widget's column to weight 1
            frame.grid_columnconfigure(
                index=index,
                weight=1,
            )

            # Create a tkinter.Label widget
            label: tkinter.Label = tkinter.Label(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=frame,
                text=column.capitalize(),
            )

            # Place the tkinter.Label widget in the tkinter.Frame widget
            label.grid(
                column=index,
                row=0,
                sticky=NSEW,
            )

        # Place the frame widget in the master widget
        frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Get a new scrolled frame widget
        self.new_stacks_frame: ScrolledFrame = ScrolledFrame(
            background=Constants.BLUE_GREY["700"],
            horizontal_scrollbar=True,
            master=master,
        )

        # Place the scrolled frame widget in the main window
        self.new_stacks_frame.grid(
            column=0,
            row=1,
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

        # Configure the master widget's 1st row to weight 0
        master.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the master widget's 2nd row to weight 1
        master.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Create a tkinter.Frame widget
        frame: tkinter.Frame = tkinter.Frame(master=master)

        for (
            index,
            column,
        ) in enumerate(
            iterable=[
                "icon",
                "name",
                "priority",
                "difficulty",
                "last viewed at",
                "status",
                "due by",
            ]
        ):
            # Configure the frame widget's column to weight 1
            frame.grid_columnconfigure(
                index=index,
                weight=1,
            )

            # Create a tkinter.Label widget
            label: tkinter.Label = tkinter.Label(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=frame,
                text=column.capitalize(),
            )

            # Place the tkinter.Label widget in the tkinter.Frame widget
            label.grid(
                column=index,
                row=0,
                sticky=NSEW,
            )

        # Place the frame widget in the master widget
        frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Get a new scrolled frame widget
        self.recently_viewed_stacks_frame: ScrolledFrame = ScrolledFrame(
            background=Constants.BLUE_GREY["700"],
            horizontal_scrollbar=True,
            master=master,
        )

        # Place the scrolled frame widget in the main window
        self.recently_viewed_stacks_frame.grid(
            column=0,
            row=1,
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

        # Configure the master widget's 1st row to weight 0
        master.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the master widget's 2nd row to weight 1
        master.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Create a tkinter.Frame widget
        frame: tkinter.Frame = tkinter.Frame(master=master)

        for (
            index,
            column,
        ) in enumerate(
            iterable=[
                "icon",
                "name",
                "priority",
                "difficulty",
                "last viewed at",
                "status",
                "due by",
            ]
        ):
            # Configure the frame widget's column to weight 1
            frame.grid_columnconfigure(
                index=index,
                weight=1,
            )

            # Create a tkinter.Label widget
            label: tkinter.Label = tkinter.Label(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=frame,
                text=column.capitalize(),
            )

            # Place the tkinter.Label widget in the tkinter.Frame widget
            label.grid(
                column=index,
                row=0,
                sticky=NSEW,
            )

        # Place the frame widget in the master widget
        frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Get a new scrolled frame widget
        self.completed_stacks_frame: ScrolledFrame = ScrolledFrame(
            background=Constants.BLUE_GREY["700"],
            horizontal_scrollbar=True,
            master=master,
        )

        # Place the scrolled frame widget in the main window
        self.completed_stacks_frame.grid(
            column=0,
            row=1,
            sticky=NSEW,
        )

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
            frame: tkinter.Frame = tkinter.Frame(
                background=Constants.GREY["default"],
                master=master,
            )

            # Dispatch the REQUEST_DIFFICULTY_LOOKUP event in the GLOBAL namespace
            difficulty_notification: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_DIFFICULTY_LOOKUP,
                    id=stack.difficulty,
                    namespace=Constants.GLOBAL_NAMESPACE,
                )
            )

            # Check, if the notification exists or has errors
            if not difficulty_notification or difficulty_notification.has_errors():
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to dispatch 'REQUEST_DIFFICULTY_LOOKUP' event in 'global' namespace in 'lookup_recently_viewed_stacks' method: {difficulty_notification.get_errors() if difficulty_notification else None}"
                )

                # Return early
                return

            # Obtain the difficulty from the one and only result of the notification
            difficulty: Optional[ImmutableDifficulty] = (
                difficulty_notification.get_one_and_only_result()
            )

            # Check, if the priority exists
            if not difficulty:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to get ImmutableDifficulty from DispatcherNotification object."
                )

                # Return early
                return

            # Dispatch the REQUEST_PRIORITY_LOOKUP event in the GLOBAL namespace
            priority_notification: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_PRIORITY_LOOKUP,
                    id=stack.priority,
                    namespace=Constants.GLOBAL_NAMESPACE,
                )
            )

            # Check, if the notification exists or has errors
            if not priority_notification or priority_notification.has_errors():
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to dispatch 'REQUEST_PRIORITY_LOOKUP' event in 'global' namespace in 'lookup_recently_viewed_stacks' method: {priority_notification.get_errors() if priority_notification else None}"
                )

                # Return early
                return

            # Obtain the priority from the one and only result of the notification
            priority: Optional[ImmutablePriority] = (
                priority_notification.get_one_and_only_result()
            )

            # Check, if the priority exists
            if not priority:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to get ImmutablePriority from DispatcherNotification object."
                )

                # Return early
                return

            # Dispatch the REQUEST_STATUS_LOOKUP event in the GLOBAL namespace
            status_notification: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_STATUS_LOOKUP,
                    id=stack.status,
                    namespace=Constants.GLOBAL_NAMESPACE,
                )
            )

            # Check, if the notification exists or has errors
            if not status_notification or status_notification.has_errors():
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to dispatch 'REQUEST_STATUS_LOOKUP' event in 'global' namespace in 'lookup_recently_viewed_stacks' method: {status_notification.get_errors() if status_notification else None}"
                )

                # Return early
                return

            # Obtain the status from the one and only result of the notification
            status: Optional[ImmutableStatus] = (
                status_notification.get_one_and_only_result()
            )

            # Check, if the priority exists
            if not status:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to get ImmutableStatus from DispatcherNotification object."
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
                    text = priority.emoji
                elif column == "difficulty":
                    text = difficulty.emoji
                elif column == "status":
                    text = status.emoji
                else:
                    text = data[column]

                # Create a tkinter.Label widget for each stack attribute
                label: tkinter.Label = tkinter.Label(
                    background=Constants.BLUE_GREY["700"],
                    font=(
                        Constants.DEFAULT_FONT_FAMILY,
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
                    func=lambda event: self.dispatcher.dispatch(
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

            # Update idletasks
            self.update_idletasks()
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to create stack item widgets: {e}"
            )

            # Re-raise the exception to the caller
            raise e

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
        left_frame: tkinter.Frame = tkinter.Frame(
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

        # Create a date clock widget within the left frame
        date_clock: DateClockWidget = DateClockWidget(
            background=Constants.BLUE_GREY["700"],
            master=left_frame,
        )

        # Configure the date clock's root widget's background to be grey
        date_clock.configure(background=Constants.BLUE_GREY["700"])

        # Configure the date clock's date label widget's background to be grey
        date_clock.configure_date_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.LARGE_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Configure the date clock's time label widget's background to be grey
        date_clock.configure_time_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.LARGE_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Place the date clock widget in the left frame
        date_clock.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=EW,
        )

        # Create a right frame within the top frame
        right_frame: tkinter.Frame = tkinter.Frame(
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
        continue_label: tkinter.Label = tkinter.Label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
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

    def lookup_completed_stacks(self) -> None:
        """
        Looks up the stacks and displays them.

        This method sends a request to retrieve the stacks
        and displays them in the dashboard UI.

        Returns:
            None

        Raises:
            Exception: If an error occurs during the lookup process.
        """
        try:
            # Dispatch the REQUEST_GET_ALL_STACKS event
            status_notification: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_STATUS_LOOKUP,
                    name="Completed",
                    namespace=Constants.GLOBAL_NAMESPACE,
                )
            )

            # Check, if the notification exists or has errors
            if not status_notification or status_notification.has_errors():
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to dispatch 'REQUEST_STATUS_LOOKUP' event in 'global' namespace in 'lookup_completed_stacks' method: {status_notification.get_errors() if status_notification else None}"
                )

                # Return early
                return

            # Dispatch the REQUEST_GET_ALL_STACKS event
            stacks_notification: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_STACK_LOOKUP,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    status=status_notification.get_one_and_only_result().id,
                )
            )

            # Check, if the notification exists or has errors
            if not stacks_notification or stacks_notification.has_errors():
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to dispatch 'REQUEST_STACK_LOOKUP' event in 'global' namespace in 'lookup_completed_stacks' method: {stacks_notification.get_errors() if stacks_notification else None}"
                )

                # Return early
                return

            # Lookup the stacks from the DispatcherNotification
            stacks: Optional[Union[ImmutableStack, List[ImmutableStack]]] = (
                stacks_notification.get_one_and_only_result()
            )

            # Check, if the stacks list is None
            if not stacks:
                # Log a warning message indicating that no stacks were found
                self.logger.warning(
                    message="No stacks found while looking up completed stacks.",
                )

                # Return early
                return

            # Check, if stacks list is instance of ImmutableStack
            if not isinstance(
                stacks,
                list,
            ):
                # Convert ImmutableStack instance to a list of ImmutableStack
                stacks = [stacks]

            # Iterate over the list of stacks
            for stack in stacks:
                # Create the stack item widgets
                self.create_stack_item_widgets(
                    master=self.completed_stacks_frame.container,
                    stack=stack,
                )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'lookup_completed_stacks' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def lookup_new_stacks(self) -> None:
        """
        Looks up the stacks and displays them.

        This method sends a request to retrieve the stacks
        and displays them in the dashboard UI.

        Returns:
            None

        Raises:
            Exception: If an error occurs during the lookup process.
        """
        try:
            # Dispatch the REQUEST_GET_ALL_STACKS event
            status_notification: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_STATUS_LOOKUP,
                    name="New",
                    namespace=Constants.GLOBAL_NAMESPACE,
                )
            )

            # Check, if the notification exists or has errors
            if not status_notification or status_notification.has_errors():
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to dispatch 'REQUEST_STATUS_LOOKUP' event in 'global' namespace in 'lookup_recently_viewed_stacks' method: {status_notification.get_errors() if status_notification else None}"
                )

                # Return early
                return

            # Dispatch the REQUEST_GET_ALL_STACKS event
            stacks_notification: Optional[DispatcherNotification] = (
                self.dispatcher.dispatch(
                    event=Events.REQUEST_STACK_LOOKUP,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    status=status_notification.get_one_and_only_result().id,
                )
            )

            # Check, if the notification exists or has errors
            if not stacks_notification or stacks_notification.has_errors():
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to dispatch 'REQUEST_STACK_LOOKUP' event in 'global' namespace in 'lookup_recently_viewed_stacks' method: {stacks_notification.get_errors() if stacks_notification else None}"
                )

                # Return early
                return

            # Obtain the ImmutableStack object list from the one and only result of the notification
            stacks: Optional[Union[ImmutableStack, List[ImmutableStack]]] = (
                stacks_notification.get_one_and_only_result()
            )

            # Check, if the stacks list is None
            if not stacks:
                # Log a warning message indicating that no stacks were found
                self.logger.warning(
                    message="No stacks found while looking up new stacks.",
                )

                # Return early
                return

            # Check, if stacks list is instance of ImmutableStack
            if not isinstance(
                stacks,
                list,
            ):
                # Convert ImmutableStack instance to a list of ImmutableStack
                stacks = [stacks]

            # Iterate over the list of stacks
            for stack in stacks:
                # Create the stack item widgets
                self.create_stack_item_widgets(
                    master=self.new_stacks_frame.container,
                    stack=stack,
                )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'lookup_new_stacks' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def lookup_recently_viewed_stacks(self) -> None:
        """
        Looks up the recently viewed stacks and displays them.

        This method sends a request to retrieve the stacks
        and displays them in the dashboard UI.

        The stacks are filtered to only include stacks that were viewed
        within the current week.

        Returns:
            None

        Raises:
            Exception: If an error occurs during the lookup process.
        """
        try:
            # Dispatch the REQUEST_GET_ALL_STACKS event
            notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
                event=Events.REQUEST_GET_ALL_STACKS,
                namespace=Constants.GLOBAL_NAMESPACE,
            )

            # Check, if the notification exists or has errors
            if not notification or notification.has_errors():
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to dispatch 'REQUEST_GET_ALL_STACKS' event in 'global' namespace in 'lookup_recently_viewed_stacks' method: {notification.get_errors() if notification else None}"
                )

                # Return early
                return

            # Obtain the ImmutableStack object list from the one and only result of the notification
            stacks: Optional[Union[ImmutableStack, List[ImmutableStack]]] = (
                notification.get_one_and_only_result()
            )

            # Check, if the stacks list is None
            if not stacks:
                # Log a warning message indicating that no stacks were found
                self.logger.warning(
                    message="No stacks found while looking up recently viewed stacks.",
                )

                # Return early
                return

            # Check, if stacks list is instance of ImmutableStack
            if not isinstance(
                stacks,
                list,
            ):
                # Convert ImmutableStack instance to a list of ImmutableStack
                stacks = [stacks]

            # Iterate over the list of stacks
            for stack in stacks:
                # Skip the stack, if it was not viewed yet
                if not stack.last_viewed_at:
                    # Skip the current iteration
                    continue

                # Check, if the ImmutableStack's 'last_viewed_at' date is within the current week
                if (
                    not Constants.START_OF_WEEK
                    <= stack.last_viewed_at
                    <= Constants.END_OF_WEEK
                ):
                    # Skip the current iteration
                    continue

                # Create the stack item widgets
                self.create_stack_item_widgets(
                    master=self.recently_viewed_stacks_frame.container,
                    stack=stack,
                )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'lookup_recently_viewed_stacks' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def on_label_clicked(
        self,
        stack: ImmutableStack,
    ) -> None:
        try:
            # Log a debug message indicating that the label was clicked
            self.logger.debug(message=f"Clicked on label for stack: {stack}.")
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_label_clicked' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def on_label_hover(
        self,
        stack: ImmutableStack,
    ) -> None:
        try:
            # Log a debug message indicating that the label was hovered
            self.logger.debug(message=f"Hovered on label for stack: {stack}.")
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_label_hover' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def on_stack_created(
        self,
        stack: ImmutableStack,
    ) -> None:
        """
        Handles the STACK_CREATED event and creates a new tkinter.Frame widget
        within the new stacks frame.

        This method creates a new tkinter.Frame widget and places it within the
        new stacks frame. It also creates a tkinter.Label widget within the
        tkinter.Frame widget and sets its text to the name of the stack.

        Args:
            stack (ImmutableStack): The immutable stack that was created.

        Returns:
            None

        Raises:
            Exception: If an error occurs during the lookup process.
        """
        try:
            # Create the stack item widgets
            self.create_stack_item_widgets(
                master=self.new_stacks_frame.container,
                stack=stack,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_stack_created' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e
