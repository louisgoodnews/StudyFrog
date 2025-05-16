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

from core.ui.fields.boolean_fields import CheckbuttonField
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
from utils.unified import UnifiedObjectFactory, UnifiedObjectManager

__all__: Final[List[str]] = ["LearningStackSelectionUI"]


class LearningStackSelectionUI(BaseUI):
    """ """

    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        navigation_service: NavigationHistoryService,
        setting_service: SettingService,
        unified_factory: UnifiedObjectFactory,
        unified_manager: UnifiedObjectManager,
        navigation_item: Optional[NavigationHistoryItem] = None,
    ) -> None:
        """ """

        # Initialize the field dictionary instance variable as an empty dictionary
        self.field_dict: Dict[str, Any] = {}

        # Initialize the value dictionary instance variable as an empty dictionary
        self.value_dict: Dict[str, Any] = {"mode": {"value": "Default"}}

        # Call the parent class constructor with the passed arguments
        super().__init__(
            dispatcher=dispatcher,
            master=master,
            name="learning_stack_selection_ui",
            navigation_item=navigation_item,
            navigation_service=navigation_service,
            setting_service=setting_service,
            unified_factory=unified_factory,
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

        # Get the ImmutableDifficulty objects from the database
        difficulties: Optional[
            Union[ImmutableDifficulty, List[ImmutableDifficulty]]
        ] = self._dispatch_request_event(event=Events.REQUEST_GET_ALL_DIFFICULTIES)

        # Check, if the database returned a list of or a singular ImmutableDifficulty
        if isinstance(
            difficulties,
            ImmutableDifficulty,
        ):
            # Convert the singular ImmutableDifficulty into a list of ImmutableDifficulty objects
            difficulties = [difficulties]

        # Return all ImmutableDifficulty objects from the database or an empty list
        return difficulties or []

    def _get_priorities(self) -> Optional[List[ImmutablePriority]]:
        """ """

        # Get the ImmutablePriority objects from the database
        priorities: Optional[Union[ImmutablePriority, List[ImmutablePriority]]] = (
            self._dispatch_request_event(event=Events.REQUEST_GET_ALL_PRIORITIES)
        )

        # Check, if the database returned a list of or a singular ImmutablePriority
        if isinstance(
            priorities,
            ImmutablePriority,
        ):
            # Convert the singular ImmutablePriority into a list of ImmutablePriority objects
            priorities = [priorities]

        # Return all ImmutablePriority objects from the database or an empty list
        return priorities or []

    def _get_stacks(self) -> Optional[List[ImmutableStack]]:
        """ """

        # Get the ImmutableStack objects from the database
        stacks: Optional[Union[ImmutableStack, List[ImmutableStack]]] = (
            self._dispatch_request_event(event=Events.REQUEST_GET_ALL_STACKS)
        )

        # Check, if the database returned a list of or a singular ImmutableStack
        if isinstance(
            stacks,
            ImmutableStack,
        ):
            # Convert the singular ImmutableStack into a list of ImmutableStack objects
            stacks = [stacks]

        # Return all ImmutableStack objects from the database or an empty list
        return stacks or []

    def _on_cancel_button_click(self) -> None:
        """ """

        # Dispatch the REQUEST_VALIDATE_NAVIGATION event in the 'global' namespace
        self.dispatcher.dispatch(
            direction="forward",
            event=Events.REQUEST_VALIDATE_NAVIGATION,
            namespace=Constants.GLOBAL_NAMESPACE,
            source="learning_stack_selection_ui",
            target="learning_dashboard_ui",
        )

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
            )
            .replace(
                "?",
                "",
            ),
        )

        # Check, if the passed label is not already contained in the value dictionary instance variable
        if label not in self.value_dict.keys():
            # Add an empty dictionary to the value dictionary instance variable under the passed label
            self.value_dict[label] = {"value": None}

        # Add the passed value to the value dictionary instance variable under the passed label
        self.value_dict[label]["value"] = value

    def _on_start_button_click(self) -> None:
        """ """

        # Get the completed form
        form: Dict[str, Any] = self.get()

        # Dispatch the REQUEST_VALIDATE_NAVIGATION event in the 'global' namespace
        self.dispatcher.dispatch(
            difficulties=[
                difficulty
                for difficulty in self._get_difficulties()
                if difficulty.name.lower() in f"{form["difficulties"]["value"]}".lower()
            ],
            direction="forward",
            event=Events.REQUEST_VALIDATE_NAVIGATION,
            mode=form["mode"]["value"],
            namespace=Constants.GLOBAL_NAMESPACE,
            priorities=[
                priority
                for priority in self._get_priorities()
                if priority.name.lower() in f"{form["priorities"]["value"]}".lower()
            ],
            settings={
                "enable_countdown": form["timing_fields"]["value"][
                    "Enable Countdown*? "
                ][1],
                "enable_countup": form["timing_fields"]["value"]["Enable Countup*? "][
                    1
                ],
                "enable_randomsiation": form["enable_randomsiation"]["value"],
                "enable_spaced_repetition": form["enable_spaced_repetition"]["value"],
            },
            source="learning_stack_selection_ui",
            stacks=[
                stack
                for stack in self._get_stacks()
                if stack.name.lower() in f"{form["stacks"]["value"]}".lower()
            ],
            target="learning_session_ui",
        )

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
            )
            .replace(
                "?",
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
        scrolled_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the 'scrolled frame' ScrolledFrame widget's 'container frame' widget's 0th row to weight 1
        scrolled_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Configure the 'scrolled frame' ScrolledFrame widget's 'container frame' widget's 1st row to weight 1
        scrolled_frame.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Configure the 'scrolled frame' ScrolledFrame widget's 'container frame' widget's 2nd row to weight 1
        scrolled_frame.grid_rowconfigure(
            index=2,
            weight=1,
        )

        # Configure the 'scrolled frame' ScrolledFrame widget's 'container frame' widget's 3rd row to weight 1
        scrolled_frame.grid_rowconfigure(
            index=3,
            weight=1,
        )

        # Configure the 'scrolled frame' ScrolledFrame widget's 'container frame' widget's 4th row to weight 1
        scrolled_frame.grid_rowconfigure(
            index=4,
            weight=1,
        )

        # Configure the 'scrolled frame' ScrolledFrame widget's 'container frame' widget's 5ft row to weight 1
        scrolled_frame.grid_rowconfigure(
            index=5,
            weight=1,
        )

        # Configure the 'scrolled frame' ScrolledFrame widget's 'container frame' widget's 6th row to weight 1
        scrolled_frame.grid_rowconfigure(
            index=6,
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

        # Create the 'stacks field' MultiOptionSelectField widget
        stacks_field: MultiOptionSelectField = MultiOptionSelectField(
            display_name="Stacks*: ",
            master=scrolled_frame,
            namespace=Constants.STACK_SELECTION_NAMESPACE,
            on_change_callback=self._on_field_change,
            values=[
                stack.get(
                    default="",
                    name="name",
                )
                for stack in stacks
            ]
            or [],
        )

        # Configure the 'stacks field' MultiOptionSelectField widget
        stacks_field.configure(background=Constants.BLUE_GREY["700"])

        # Configure the 'stacks field' MultiOptionSelectField widget's 'clear button' tkinter.Button widget
        stacks_field.configure_clear_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Configure the 'stacks field' MultiOptionSelectField widget's 'container frame' tkinter.Frame widget
        stacks_field.configure_container_frame(background=Constants.BLUE_GREY["700"])

        # Configure the 'stacks field' MultiOptionSelectField widget's 'label' tkinter.Label widget
        stacks_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Configure the 'stacks field' MultiOptionSelectField widget's 'select button' tkinter.Button widget
        stacks_field.configure_select_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Place the 'stacks field' MultiOptionSelectField widget in the grid
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
            master=scrolled_frame,
            on_change_callback=self._on_field_change,
            values=[
                difficulty.get(
                    default="",
                    name="name",
                )
                for difficulty in difficulties
            ]
            or [],
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
            master=scrolled_frame,
            on_change_callback=self._on_field_change,
            values=[
                priority.get(
                    default="",
                    name="name",
                )
                for priority in priorities
            ]
            or [],
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
            master=scrolled_frame,
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
            master=scrolled_frame,
            namespace=Constants.STACK_SELECTION_NAMESPACE,
            on_change_callback=self._on_field_change,
            selection_mode="single",
        )

        # Configure the 'timing fields' CheckbuttonSelectField widget
        timing_fields.configure(background=Constants.BLUE_GREY["700"])

        # Configure the 'timing fields' CheckbuttonSelectField widget's 'checkbutton' tkinter.Checkbutton widgets
        timing_fields.configure_checkbuttons(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Configure the 'timing fields' CheckbuttonSelectField widget's CheckbuttonField widgets
        timing_fields.configure_fields(background=Constants.BLUE_GREY["700"])

        # Configure the 'timing fields' CheckbuttonSelectField widget's 'label' tkinter.Label widget
        timing_fields.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Configure the 'timing fields' CheckbuttonSelectField widget's 'label' tkinter.Label widgets
        timing_fields.configure_labels(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

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

        # Create the 'enable randomisation' CheckbuttonField widget
        randomisation_field: CheckbuttonField = CheckbuttonField(
            display_name="Enable Randomsiation?",
            master=scrolled_frame,
            namespace=Constants.STACK_SELECTION_NAMESPACE,
            on_change_callback=self._on_field_change,
        )

        # Configure the 'enable randomisation' CheckbuttonField widget
        randomisation_field.configure(background=Constants.BLUE_GREY["700"])

        # Configure the 'enable randomisation' CheckbuttonField widget's 'checkbutton' tkinter.Checkbutton widget
        randomisation_field.configure_checkbutton(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Configure the 'enable randomisation' CheckbuttonField widget's 'label' tkinter.Label widget
        randomisation_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Place the 'enable randomisation' CheckbuttonField widget in the grid
        randomisation_field.grid(
            column=0,
            padx=5,
            pady=5,
            row=5,
            sticky=NSEW,
        )

        # Register the 'enable randomisation' CheckbuttonField widget
        self._register_field(
            field=randomisation_field,
            label="Enable Randomsiation?",
            required=True,
        )

        # Create the 'enable spaced repetition' CheckbuttonField widget
        spaced_repetition_field: CheckbuttonField = CheckbuttonField(
            display_name="Enable Spaced Repetition?",
            master=scrolled_frame,
            namespace=Constants.STACK_SELECTION_NAMESPACE,
            on_change_callback=self._on_field_change,
            value=True,
        )

        # Configure the 'enable spaced repetition' CheckbuttonField widget
        spaced_repetition_field.configure(background=Constants.BLUE_GREY["700"])

        # Configure the 'enable spaced repetition' CheckbuttonField widget's 'checkbutton' tkinter.Checkbutton widget
        spaced_repetition_field.configure_checkbutton(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Configure the 'enable spaced repetition' CheckbuttonField widget's 'label' tkinter.Label widget
        spaced_repetition_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Place the 'enable spaced repetition' CheckbuttonField widget in the grid
        spaced_repetition_field.grid(
            column=0,
            padx=5,
            pady=5,
            row=6,
            sticky=NSEW,
        )

        # Register the 'enable spaced repetition' CheckbuttonField widget
        self._register_field(
            field=spaced_repetition_field,
            label="Enable Spaced Repetition?",
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

    def get(self) -> Dict[str, Any]:
        """
        Returns the current values of the form.

        Args:
            None

        Returns:
            Dict[str, Any]: A dictionary containing all field values by normalized label.
        """

        # Update the value dictionary instance variable
        for (
            key,
            value,
        ) in self.field_dict.items():
            self.value_dict[
                key.strip()
                .replace(
                    ":",
                    "",
                )
                .replace(
                    "*",
                    "",
                )
                .replace(
                    "?",
                    "",
                )
            ] = {
                "type": type(value["widget"].get()[1]),
                "value": value["widget"].get()[1],
            }

        # Return a the value dictionary to the caller
        return self.value_dict
