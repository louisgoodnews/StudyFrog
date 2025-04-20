"""
Author: lodego
Date: 2025-04-20
"""

import tkinter
import traceback

from tkinter.constants import *
from typing import *

from core.difficulty import ImmutableDifficulty
from core.priority import ImmutablePriority
from core.setting import SettingService
from core.stack import ImmutableStack

from core.ui.fields.select_fields import (
    CheckbuttonSelectField,
    ComboboxField,
    MultiOptionSelectField,
)

from core.ui.frames.frames import ScrolledFrame

from utils.base_ui import BaseUI
from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherEvent, DispatcherNotification
from utils.events import Events
from utils.miscellaneous import Miscellaneous
from utils.navigation import NavigationHistoryItem, NavigationHistoryService
from utils.unified import UnifiedObjectManager

__all__: Final[List[str]] = ["LearningStackSelectionUI"]


class LearningStackSelectionUI(BaseUI):
    """ """

    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        navigation_service: NavigationHistoryService,
        setting_service: SettingService,
        unified_manager: UnifiedObjectManager,
        navigation_item: Optional[NavigationHistoryItem] = None,
    ) -> None:
        """ """

        # Initialize the field dictionary instance variable as an empty dictionary
        self.field_dict: Dict[str, Any] = {}

        # Initialize the value dictionary instance variable as an empty dictionary
        self.value_dict: Dict[str, Any] = {}

        # Call the parent class constructor with the passed arguments
        super().__init__(
            dispatcher=dispatcher,
            master=master,
            name="learning_stack_selection_ui",
            navigation_item=navigation_item,
            navigation_service=navigation_service,
            setting_service=setting_service,
            unified_manager=unified_manager,
        )

    def _dispatch_request_event(
        self,
        event: DispatcherEvent,
    ) -> Optional[Any]:
        """ """
        try:
            # Dispatch the the passed event in the 'global' namespace
            notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
                event=event,
                namespace=Constants.GLOBAL_NAMESPACE,
            )

            # Check, if the notification exists or has errors
            if not notification or notification.has_errors():
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to notify '{event.name}' in 'global' namespace: {notification.get_errors() if notification else None}"
                )

                # Return early
                return

            # Return the one and only result of the notification
            return notification.get_one_and_only_result()
        except Exception as e:
            # Log an error message
            self.logger.error(
                message=f"Caught an exception while attempting to run the '_dispatch_request_event' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    def _get_difficulties(self) -> Optional[List[ImmutableDifficulty]]:
        """ """

        # Return all ImmutableDifficulty objects from the database or an empty list
        return (
            self._dispatch_request_event(event=Events.REQUEST_GET_ALL_DIFFICULTIES)
            or []
        )

    def _get_priorities(self) -> Optional[List[ImmutablePriority]]:
        """ """

        # Return all ImmutablePriority objects from the database or an empty list
        return (
            self._dispatch_request_event(event=Events.REQUEST_GET_ALL_PRIORITIES) or []
        )

    def _get_stacks(self) -> Optional[List[ImmutableStack]]:
        """ """

        # Return all ImmutableStack objects from the database or an empty list
        return self._dispatch_request_event(event=Events.REQUEST_GET_ALL_STACKS) or []

    def _on_cancel_button_click(self) -> None:
        """ """

        pass

    def _on_field_change(
        self,
        label: str,
        value: Optional[Any] = None,
    ) -> None:
        """ """

        # Convert the passed label string to snake case
        label = Miscellaneous.any_to_snake(
            string=label.strip()
            .replace(
                "*",
                "",
            )
            .replace(
                "*",
                "",
            ),
        )

        # Check, if the passed label is not already contained in the value dictionary instance variable
        if label not in self.value_dict.keys():
            # Add an empty dictionary to the value dictionary instance variable under the passed label
            self.value_dict[label] = {"value": None}

        # Add the passed value to the value dictionary instance variable under the passed label
        self.value_dict[label]["value"] = (
            value
            if not isinstance(
                value,
                (
                    list,
                    set,
                    tuple,
                ),
            )
            else value[0]
        )

    def _on_start_button_click(self) -> None:
        """ """

        self.logger.debug(message=self.value_dict)

    def _register_field(
        self,
        field: tkinter.Misc,
        label: str,
        required: bool = False,
    ) -> None:
        """ """

        # Convert the passed label string to snake case
        label = Miscellaneous.any_to_snake(
            string=label.strip()
            .replace(
                "*",
                "",
            )
            .replace(
                "*",
                "",
            ),
        )

        # Check, if the passed label is already contained in the field dictionary instance variable
        if label in self.field_dict.keys():
            # Log a warning message
            self.logger.warning(
                message=f"'{label}' '{field.__class__.__name__}' instance already registered in field dict. Aborting..."
            )

            # Return early
            return

        # Add the passed field widget and bool flag to the field dictionary instance variable under the passed label
        self.field_dict[label] = {
            "required": required,
            "widget": field,
        }

    @override
    def collect_subscriptions(self) -> List[Dict[str, Any]]:
        # Call the parent class' 'collect_subscriptions' method to get the subscriptions list
        subscriptions: List[Dict[str, Any]] = super().collect_subscriptions()

        # Return the subscriptions list to the caller
        return subscriptions

    @override
    def configure_grid(self) -> None:
        """ """

        # Configure this widget's 0th column to weight 1
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure this widget's 0th row to weight 0
        self.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure this widget's 1st row to weight 1
        self.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Configure this widget's 2nd row to weight 0
        self.grid_rowconfigure(
            index=2,
            weight=0,
        )

    def create_bottom_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """ """

        # Configure the passed master widget's 0th column to weight 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the passed master widget's 1st column to weight 0
        master.grid_columnconfigure(
            index=1,
            weight=0,
        )

        # Configure the passed master widget's 2nd column to weight 0
        master.grid_columnconfigure(
            index=2,
            weight=0,
        )

        # Configure the passed master widget's 0th row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create a 'start button' tkinter.Button widget
        start_button: tkinter.Button = tkinter.Button(
            background=Constants.BLUE_GREY["700"],
            command=self._on_start_button_click,
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=master,
            relief=FLAT,
            text="Start",
        )

        # Place the 'start button' tkinter.Button widget in the grid
        start_button.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=E,
        )

        # Create a 'cancel button' tkinter.Button widget
        cancel_button: tkinter.Button = tkinter.Button(
            background=Constants.BLUE_GREY["700"],
            command=self._on_cancel_button_click,
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=master,
            relief=FLAT,
            text="Cancel",
        )

        # Place the 'cancel button' tkinter.Button widget in the grid
        cancel_button.grid(
            column=2,
            padx=5,
            pady=5,
            row=0,
            sticky=E,
        )

        # Update the idletasks
        self.update_idletasks()

    def create_center_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """ """

        # Configure the passed master widget's 0th column to weight 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the passed master widget's 0th row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create the 'scrolled frame' ScrolledFrame widget
        scrolled_frame: ScrolledFrame = ScrolledFrame(master=master)

        # Configure the 'scrolled frame' ScrolledFrame widget itself
        scrolled_frame.configure(background=Constants.BLUE_GREY["700"])

        # Configure the 'scrolled frame' ScrolledFrame widget's canvas widget
        scrolled_frame.configure_canvas(background=Constants.BLUE_GREY["700"])

        # Configure the 'scrolled frame' ScrolledFrame widget's 'container frame' widget
        scrolled_frame.configure_container_frame(background=Constants.BLUE_GREY["700"])

        # Configure the 'scrolled frame' ScrolledFrame widget's 'container frame' widget's 0th column to weight 1
        scrolled_frame.container.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the 'scrolled frame' ScrolledFrame widget's 'container frame' widget's 0th row to weight 1
        scrolled_frame.container.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Configure the 'scrolled frame' ScrolledFrame widget's 'container frame' widget's 1st row to weight 1
        scrolled_frame.container.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Configure the 'scrolled frame' ScrolledFrame widget's 'container frame' widget's 2nd row to weight 1
        scrolled_frame.container.grid_rowconfigure(
            index=2,
            weight=1,
        )

        # Configure the 'scrolled frame' ScrolledFrame widget's 'container frame' widget's 3rd row to weight 1
        scrolled_frame.container.grid_rowconfigure(
            index=3,
            weight=1,
        )

        # Configure the 'scrolled frame' ScrolledFrame widget's 'container frame' widget's 4th row to weight 1
        scrolled_frame.container.grid_rowconfigure(
            index=4,
            weight=1,
        )

        # Place the 'scrolled frame' ScrolledFrame widget in the grid
        scrolled_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Attempt to get all ImmutableStack objects from the database
        stacks: List[ImmutableStack] = self._get_stacks()

        # Create the 'stacks field' ComboboxField widget
        stacks_field: ComboboxField = ComboboxField(
            display_name="Stacks*: ",
            master=scrolled_frame.container,
            namespace=Constants.STACK_SELECTION_NAMESPACE,
            on_change_callback=self._on_field_change,
            readonly=True,
            values=[
                stack.get(
                    default="",
                    name="name",
                )
                for stack in stacks
            ],
        )

        # Configure the 'stacks field' ComboboxField widget
        stacks_field.configure(background=Constants.BLUE_GREY["700"])

        # Configure the 'stacks field' ComboboxField widget's 'button' tkinter.Button widget
        stacks_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Configure the 'stacks field' ComboboxField widget's 'combobox' ttk.Combobox widget
        stacks_field.configure_combobox(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Configure the 'stacks field' ComboboxField widget's 'label' tkinter.Label widget
        stacks_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Place the 'stacks field' ComboboxField widget in the grid
        stacks_field.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Register the 'stacks field' ComboboxField widget
        self._register_field(
            field=stacks_field,
            label="Stacks*: ",
            required=False,
        )

        # Attempt to get all ImmutableDifficulty objects from the database
        difficulties: List[ImmutableDifficulty] = self._get_difficulties()

        # Create the 'difficulties field' MultiOptionSelectField widget
        difficulties_field: MultiOptionSelectField = MultiOptionSelectField(
            display_name="Difficulties: ",
            master=scrolled_frame.container,
            on_change_callback=self._on_field_change,
            values=[
                difficulty.get(
                    default="",
                    name="name",
                )
                for difficulty in difficulties
            ],
        )

        # Configure the 'difficulties field' MultiOptionSelectField widget
        difficulties_field.configure(background=Constants.BLUE_GREY["700"])

        # Configure the 'difficulties field' MultiOptionSelectField widget's 'container frame' tkinter.Frame widget
        difficulties_field.configure_container_frame(
            background=Constants.BLUE_GREY["700"]
        )

        # Configure the 'difficulties field' MultiOptionSelectField widget's 'clear button' tkinter.Button widget
        difficulties_field.configure_clear_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Configure the 'difficulties field' MultiOptionSelectField widget's 'label' tkinter.Label widget
        difficulties_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Configure the 'difficulties field' MultiOptionSelectField widget's 'select button' tkinter.Button widget
        difficulties_field.configure_select_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Place the 'difficulties field' MultiOptionSelectField widget in the grid
        difficulties_field.grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )

        # Register the 'difficulties field' MultiOptionSelectField widget
        self._register_field(
            field=difficulties_field,
            label="Difficulties: ",
            required=False,
        )

        # Attempt to get all ImmutablePriority objects from the database
        priorities: List[ImmutablePriority] = self._get_priorities()

        # Create the 'priorities field' MultiOptionSelectField widget
        priorities_field: MultiOptionSelectField = MultiOptionSelectField(
            display_name="Priorities: ",
            master=scrolled_frame.container,
            on_change_callback=self._on_field_change,
            values=[
                priority.get(
                    default="",
                    name="name",
                )
                for priority in priorities
            ],
        )

        # Configure the 'priorities field' MultiOptionSelectField widget
        priorities_field.configure(background=Constants.BLUE_GREY["700"])

        # Configure the 'priorities field' MultiOptionSelectField widget's 'container frame' tkinter.Frame widget
        priorities_field.configure_container_frame(
            background=Constants.BLUE_GREY["700"]
        )

        # Configure the 'priorities field' MultiOptionSelectField widget's 'clear button' tkinter.Button widget
        priorities_field.configure_clear_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Configure the 'priorities field' MultiOptionSelectField widget's 'label' tkinter.Label widget
        priorities_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Configure the 'priorities field' MultiOptionSelectField widget's 'select button' tkinter.Button widget
        priorities_field.configure_select_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Place the 'priorities field' MultiOptionSelectField widget in the grid
        priorities_field.grid(
            column=0,
            padx=5,
            pady=5,
            row=2,
            sticky=NSEW,
        )

        # Register the 'priorities field' MultiOptionSelectField widget
        self._register_field(
            field=priorities_field,
            label="Priorities: ",
            required=False,
        )

        # Create the 'mode field' ComboboxField widget
        mode_field: ComboboxField = ComboboxField(
            display_name="Mode*: ",
            master=scrolled_frame.container,
            namespace=Constants.STACK_SELECTION_NAMESPACE,
            on_change_callback=self._on_field_change,
            readonly=True,
            value="Default",
            values=Constants.LEARNING_MODES,
        )

        # Configure the 'mode field' ComboboxField widget
        mode_field.configure(background=Constants.BLUE_GREY["700"])

        # Configure the 'mode field' ComboboxField widget's 'button' tkinter.Button widget
        mode_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Configure the 'mode field' ComboboxField widget's 'combobox' ttk.Combobox widget
        mode_field.configure_combobox(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Configure the 'mode field' ComboboxField widget's 'label' tkinter.Label widget
        mode_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Place the 'mode field' ComboboxField widget in the grid
        mode_field.grid(
            column=0,
            padx=5,
            pady=5,
            row=3,
            sticky=NSEW,
        )

        # Register the 'mode field' ComboboxField widget
        self._register_field(
            field=mode_field,
            label="Mode*: ",
            required=True,
        )

        # Create the 'timing fields' CheckbuttonSelectField widget
        timing_fields: CheckbuttonSelectField = CheckbuttonSelectField(
            display_name="Timing Fields*: ",
            labels=[
                "Enable Countdown*? ",
                "Enable Countup*? ",
            ],
            master=scrolled_frame.container,
            namespace=Constants.STACK_SELECTION_NAMESPACE,
            on_change_callback=self._on_field_change,
            selection_mode="single",
        )

        # Configure the 'timing fields' CheckbuttonSelectField widget
        timing_fields.configure(background=Constants.BLUE_GREY["700"])

        # Place the 'timing fields' CheckbuttonSelectField widget in the grid
        timing_fields.grid(
            column=0,
            padx=5,
            pady=5,
            row=4,
            sticky=NSEW,
        )

        # Register the 'timing fields' CheckbuttonSelectField widget
        self._register_field(
            field=timing_fields,
            label="Timing Fields*: ",
            required=True,
        )

        # Update the idletasks
        self.update_idletasks()

    def create_top_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """ """

        # Update the idletasks
        self.update_idletasks()

    @override
    def create_widgets(self) -> None:
        """ """

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

        # Create the 'top frame' widgets
        self.create_top_frame_widgets(master=top_frame)

        # Create the 'center frame' widgets
        self.create_center_frame_widgets(master=center_frame)

        # Create the 'bottom frame' widgets
        self.create_bottom_frame_widgets(master=bottom_frame)

        # Update the idletasks
        self.update_idletasks()
