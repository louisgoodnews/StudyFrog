"""
Author: lodego
Date: 2025-04-13
"""

import tkinter

from tkinter.constants import *
from typing import *

from core.ui.fields.boolean_fields import CheckbuttonField
from core.ui.fields.datetime_fields import DateSelectField
from core.ui.fields.select_fields import ComboboxField
from core.ui.fields.string_fields import (
    MultiSelectAnswerField,
    MultiLineTextField,
    SingleLineTextField,
)

from core.ui.frames.frames import ScrolledFrame

from core.ui.notifications.notifications import ToplevelToastNotification

from core.stack import ImmutableStack

from utils.base_create_form import BaseCreateForm
from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherNotification
from utils.events import Events
from utils.miscellaneous import Miscellaneous


__all__: Final[List[str]] = ["StackCreateForm"]


class StackCreateForm(BaseCreateForm):
    """ """

    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        namespace: str,
        **kwargs,
    ) -> None:
        """ """

        # Call the parent class constructor with the passed arguments
        super().__init__(
            dispatcher=dispatcher,
            master=master,
            namespace=namespace,
            **kwargs,
        )

    def _on_stack_created(
        self,
        stack: ImmutableStack,
    ) -> None:
        """ """

        # Append the passed stack ImmutableStack object's name to the ComboboxField's value
        self.field_dict["ancestor"]["widget"].add(value=stack.name)

    @override
    def collect_subscriptions(self) -> List[Dict[str, Any]]:
        # Call the parent class' 'collect_subscriptions' Method
        subscriptions: List[Dict[str, Any]] = super().collect_subscriptions()

        # Append event subscription configurations to the list
        subscriptions.append(
            {
                "event": Events.STACK_CREATED,
                "function": self._on_stack_created,
                "namespace": Constants.GLOBAL_NAMESPACE,
                "persistent": True,
            }
        )

        # Return the subscriptions list
        return subscriptions

    @override
    def _on_field_change(
        self,
        label: str,
        value: Any,
    ) -> None:
        """ """

        # Call the super class' '_on_field_change' method with the passed arguments
        super()._on_field_change(
            label=label,
            value=value,
        )

        # Check, if the changed field is the 'name' field
        if label != "Name*: ":
            # Return early
            return

        # Dispatch the REQUEST_STACK_LOOKUP event in the 'global' namespace
        notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
            event=Events.REQUEST_STACK_LOOKUP,
            namespace=Constants.GLOBAL_NAMESPACE,
            name=self._value_dict["name"]["value"],
        )

        if not notification or notification.has_errors():
            # Log a warning message
            self.logger.warning(message=f"")

            # Return early
            return

        # Obtain the ImmutableStack or ImmutableStack list from the DispatcherNotification's one an only result
        stacks: Optional[Union[ImmutableStack, List[ImmutableStack]]] = notification.get_one_and_only_result()

        # Check, if no ImmutableStack or ImmutableStack list could be obtained
        if not stacks:
            # Return early
            return

        # Display a toast message to the user
        ToplevelToastNotification(
            title=f"Illegal value for 'name' field",
            message=f"Stacks need to have a unique name in StudyFrog. It seems that a '{value}' stack already exists.",
        )

    @override
    def create_primary_attribute_widgets(
        self,
        master: ScrolledFrame,
    ) -> None:
        """ """

        # Configure the weight of the 0th column to 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the weight of the 0th row to 0
        master.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the weight of the 1st row to 0
        master.grid_rowconfigure(
            index=1,
            weight=0,
        )

        # Configure the weight of the 1st row to 0
        master.grid_rowconfigure(
            index=1,
            weight=0,
        )

        # Configure the weight of the 3rd row to 0
        master.grid_rowconfigure(
            index=3,
            weight=0,
        )

        # Configure the weight of the 4th row to 0
        master.grid_rowconfigure(
            index=4,
            weight=0,
        )

        # Configure the weight of the 5ft row to 1
        master.grid_rowconfigure(
            index=5,
            weight=1,
        )

        # Create the 'name' SingleLineTextField widget
        name_field: SingleLineTextField = SingleLineTextField(
            display_name="Name*: ",
            master=master,
            on_change_callback=self._on_field_change,
        )

        # Place the 'name' SingleLineTextField widget in the grid
        name_field.grid(
            column=0,
            padx=10,
            pady=10,
            row=0,
            sticky=NSEW,
        )

        # Style the 'name' SingleLineTextField widget
        name_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the 'name' SingleLineTextField widget's button
        name_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the 'name' SingleLineTextField widget's text
        name_field.configure_entry(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Register the 'name' SingleLineTextField widget
        self._register_field(
            label="Name*: ",
            field=name_field,
            required=True,
        )

        # Dispatch the REQUEST_GET_ALL_STACKS event in the global namespace
        stack_notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
            event=Events.REQUEST_GET_ALL_STACKS,
            namespace=Constants.GLOBAL_NAMESPACE,
        )

        # Check, if the notification exists
        if not stack_notification:
            # Log a warning message
            self.logger.warning(
                message=f"Failed to dispatch the REQUEST_GET_ALL_STACKS event in the global namespace."
            )

            # Return early
            return

        # Obtain the ImmutableStack list from the DispatcherNotification's one and only result
        stacks: Optional[Union[ImmutableStack, List[ImmutableStack]]] = (
            stack_notification.get_one_and_only_result()
        )

        # Check, if the ImmutableStack list exists
        if not stacks:
            # Set the ImmutableStack list to an empty list
            stacks = []
        # Check if the ImmutableStack is an instance of ImmutableStack
        elif stacks and isinstance(
            stacks,
            ImmutableStack,
        ):
            # Set the ImmutableStack list to an ImmutableStack list
            stacks = [stacks]

        # Create the 'ancestor field' ComboboxField widget
        ancestor_field: ComboboxField = ComboboxField(
            display_name="Ancestor: ",
            master=master,
            on_change_callback=self._on_field_change,
            readonly=True,
            values=[stack.name for stack in stacks] if stacks else [],
        )

        # Place the 'ancestor field' ComboboxField widget in the grid
        ancestor_field.grid(
            column=0,
            padx=10,
            pady=10,
            row=1,
            sticky=NSEW,
        )

        # Style the 'ancestor field' ComboboxField widget
        ancestor_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the 'ancestor field' ComboboxField widget's button
        ancestor_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the 'ancestor field' ComboboxField widget's combobox
        ancestor_field.configure_combobox(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Register the 'ancestor field' ComboboxField widget
        self._register_field(
            label="Ancestor: ",
            field=ancestor_field,
            required=False,
        )

        # Dispatch the REQUEST_GET_ALL_DIFFICULTIES event in the global namespace
        difficulty_notification: Optional[DispatcherNotification] = (
            self.dispatcher.dispatch(
                event=Events.REQUEST_GET_ALL_DIFFICULTIES,
                namespace=Constants.GLOBAL_NAMESPACE,
            )
        )

        # Check, if the notification exists
        if not difficulty_notification:
            # Log a warning message
            self.logger.warning(
                message=f"Failed to dispatch the REQUEST_GET_ALL_DIFFICULTIES event in the global namespace."
            )

            # Return early
            return

        # Create the 'difficulty' ComboboxField widget
        difficulty_field: ComboboxField = ComboboxField(
            display_name="Difficulty*: ",
            master=master,
            on_change_callback=self._on_field_change,
            readonly=True,
            values=[
                difficulty.name
                for difficulty in difficulty_notification.get_one_and_only_result()
            ],
        )

        # Place the 'difficulty' ComboboxField widget in the grid
        difficulty_field.grid(
            column=0,
            padx=10,
            pady=10,
            row=2,
            sticky=NSEW,
        )

        # Style the 'difficulty' ComboboxField widget
        difficulty_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the 'difficulty' ComboboxField widget's button
        difficulty_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the 'difficulty' ComboboxField widget's combobox
        difficulty_field.configure_combobox(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Register the 'difficulty' ComboboxField widget
        self._register_field(
            label="Difficulty*: ",
            field=difficulty_field,
            required=True,
        )

        # Dispatch the REQUEST_GET_ALL_PRIORITIES event in the global namespace
        priority_notification: Optional[DispatcherNotification] = (
            self.dispatcher.dispatch(
                event=Events.REQUEST_GET_ALL_PRIORITIES,
                namespace=Constants.GLOBAL_NAMESPACE,
            )
        )

        # Check, if the notification exists
        if not priority_notification:
            # Log a warning message
            self.logger.warning(
                message=f"Failed to dispatch the REQUEST_GET_ALL_PRIORITIES event in the global namespace."
            )

            # Return early
            return

        # Create the 'priority' ComboboxField widget
        priority_field: ComboboxField = ComboboxField(
            display_name="Priority*: ",
            master=master,
            on_change_callback=self._on_field_change,
            readonly=True,
            values=[
                priority.name
                for priority in priority_notification.get_one_and_only_result()
            ],
        )

        # Place the 'priority' ComboboxField widget in the grid
        priority_field.grid(
            column=0,
            padx=10,
            pady=10,
            row=3,
            sticky=NSEW,
        )

        # Style the 'priority' ComboboxField widget
        priority_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the 'priority' ComboboxField widget's button
        priority_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the 'priority' ComboboxField widget's combobox
        priority_field.configure_combobox(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Register the 'priority' ComboboxField widget
        self._register_field(
            label="Priority*: ",
            field=priority_field,
            required=True,
        )

        # Create the 'due by' DateSelectField widget
        due_by_field: DateSelectField = DateSelectField(
            date_format=Constants.DEFAULT_DATE_FORMAT,
            display_name="Due By*: ",
            master=master,
            on_change_callback=self._on_field_change,
            value=Miscellaneous.get_date_increment(days=45),
        )

        # Place the 'due by' DateSelectField widget in the grid
        due_by_field.grid(
            column=0,
            padx=10,
            pady=10,
            row=4,
            sticky=NSEW,
        )

        # Style the 'due by' DateSelectField widget
        due_by_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the 'due by' DateSelectField widget's 'clear button'
        due_by_field.configure_clear_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the 'due by' DateSelectField widget's entry
        due_by_field.configure_entry(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
        )

        # Style the 'due by' DateSelectField widget's label
        due_by_field.configure_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
        )

        # Style the 'due by' DateSelectField widget's 'select button'
        due_by_field.configure_select_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Register the 'due by' DateSelectField widget
        self._register_field(
            label="Due By*: ",
            field=due_by_field,
            required=True,
        )

        # Call the 'on_field_change' method with the 'due by' DateSelectField widget's value
        self._on_field_change(
            label="Due By*: ",
            value=due_by_field.get(),
        )

        # Create the 'description' MultiLineTextField widget
        description_field: MultiLineTextField = MultiLineTextField(
            display_name="Description: ",
            master=master,
            on_change_callback=self._on_field_change,
        )

        # Place the 'description' MultiLineTextField widget in the grid
        description_field.grid(
            column=0,
            padx=10,
            pady=10,
            row=5,
            sticky=NSEW,
        )

        # Style the 'description' MultiLineTextField widget
        description_field.configure(background=Constants.BLUE_GREY["700"])

        # Style the 'description' MultiLineTextField widget's button
        description_field.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the 'description' MultiLineTextField widget's text
        description_field.configure_text(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            height=10,
        )

        # Register the 'description' MultiLineTextField widget
        self._register_field(
            label="Description: ",
            field=description_field,
            required=False,
        )

    @override
    def create_secondary_attribute_widgets(
        self,
        master: ScrolledFrame,
    ) -> None:
        """ """

        pass
