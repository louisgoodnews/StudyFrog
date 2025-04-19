"""
Author: lodego
Date: 2025-04-06
"""

import tkinter
import traceback
import uuid

from enum import Enum
from tkinter.constants import *
from tkinter import ttk
from typing import *

from core.ui.fields.boolean_fields import CheckbuttonField, RadiobuttonField

from utils.base_field import BaseField
from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherEvent, DispatcherNotification
from utils.events import Events
from utils.logger import Logger
from utils.unified import UnifiedObjectFactory


__all__: Final[List[str]] = [
    "ComboboxField",
    "ComboboxSelectField",
    "EntityComboboxField",
    "EntityMultiOptionSelectField",
    "EntitySelectTypes",
    "EntitSingleOptionSelectField",
    "ListboxField",
    "MultiOptionSelectField",
    "SingleOptionSelectField",
]


class EntitySelectTypes(Enum):
    """ """

    ANSWER: Literal["answer"] = "answer"
    DIFFICULTY: Literal["difficulty"] = "difficulty"
    FLASHCARD: Literal["Flashcard"] = "flashcard"
    NOTE: Literal["note"] = "note"
    PRIORITY: Literal["priority"] = "priority"
    QUESTION: Literal["question"] = "question"
    STACK: Literal["stack"] = "stack"
    STATUS: Literal["status"] = "status"
    SUBJECT: Literal["subject"] = "subject"
    TAG: Literal["tag"] = "tag"
    TEACHER: Literal["teacher"] = "teacher"
    USER: Literal["user"] = "user"


class CheckbuttonSelectField(BaseField):
    """
    A grouped boolean selection field using multiple checkbuttons.

    CheckbuttonSelectField represents a set of binary input fields, each rendered as a CheckbuttonField.
    It allows users to select one or multiple options from a list of labels, depending on the defined
    selection mode ("single" or "multi").

    The field layout consists of:
        [ Label ]
        [ Label 1 | Checkbutton 1 ]
        [ Label 2 | Checkbutton 2 ]
        ...
        [ Label n | Checkbutton n ]

    Attributes:
        fields (Dict[str, CheckbuttonField]): A dictionary mapping option labels to their respective checkbutton fields.
        selection_mode (Literal["multi", "single"]): Defines whether multiple options can be selected simultaneously.

    Inherits from:
        BaseField
    """

    def __init__(
        self,
        label: str,
        labels: List[str],
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, Dict[str, bool]], None]] = None,
        selection_mode: Literal["multi", "single"] = "single",
    ) -> None:
        """
        Initializes a new instance of the CheckbuttonSelectField class.

        This constructor sets up a group of checkbutton widgets corresponding to the given labels.
        It allows configuration of a selection mode ('multi' or 'single') and manages individual
        CheckbuttonField instances in a centralized layout.

        Args:
            label (str): The label text describing the group of checkbuttons.
            labels (List[str]): A list of strings representing the options to display as checkbuttons.
            master (tkinter.Misc): The parent container in which this widget is placed.
            namespace (str, optional): The namespace identifier for event dispatching. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[str, Dict[str, bool]], None]], optional): Callback function invoked on any change in the selection.
            selection_mode (Literal["multi", "single"], optional): Determines whether one or multiple selections are allowed. Defaults to "single".

        Returns:
            None
        """

        # Initialize the fields dictionary
        self.fields: Dict[str, Optional[CheckbuttonField]] = {
            field: None for field in labels
        }

        # Store the passed selection mode in an instance variable
        self.selection_mode: Final[str] = selection_mode

        # Call the parent class constructor with the passed arguments
        super().__init__(
            label=label,
            master=master,
            namespace=namespace,
            on_change_callback=on_change_callback,
        )

    @property
    def label(self) -> tkinter.Label:
        """
        Returns the label widget associated with this field.

        The label displays the name or description of the field.

        Returns:
            tkinter.Label: The label widget.
        """

        # Return the tkinter.Label label widget
        return self._label

    def _enforce_selection_mode(
        self,
        label: str,
        value: bool,
    ) -> None:
        """
        Enforces the configured selection mode across checkbuttons.

        In 'single' mode, this method ensures that only the field corresponding to the given label
        remains active (True), while all others are reset to False. In 'multi' mode, no action is taken.

        Args:
            label (str): The label of the field that was selected.
            value (bool): The boolean value indicating the new selection state.

        Returns:
            None
        """

        # Check, if the selection mode string instance variable is set to 'multi'
        if self.selection_mode == "multi":
            # Return early
            return

        # Iterate over the keys and values of the fields dictionary instance variable
        for (
            key,
            value,
        ) in self.fields.items():
            # Check if the key and the passed label are identical
            if key == label:
                # Update the value of the corresponding checkbutton field with the passed value
                value.set(
                    dispatch=False,
                    value=value,
                )
            else:
                # Update the value of the non-corresponding checkbutton field with the opposite of the passed value
                value.set(
                    dispatch=False,
                    value=not value,
                )

    def _on_field_change(
        self,
        label: str,
        value: bool,
    ) -> None:
        """
        Internal handler for state changes in individual checkbuttons.

        This method is triggered whenever a CheckbuttonField changes its value. It enforces
        the selection mode (e.g. unselecting other fields in 'single' mode), dispatches
        a change event, and invokes the on_change_callback if provided.

        Args:
            label (str): The label of the field that triggered the change.
            value (bool): The new boolean value of the changed field.

        Returns:
            None
        """

        # Enforce the selection mode
        self._enforce_selection_mode(label=label, value=value)

        # Dispatch the CHECKBUTTON_SELECT_FIELD_CHANGED event
        self.dispatcher.dispatch(
            event=Events.CHECKBUTTON_SELECT_FIELD_CHANGED,
            label=self.display_name,
            namespace=self.namespace,
            value=self.get(),
        )

        # Check, if the 'on_change_callback' function exists
        if self.on_change_callback:
            # Call the 'on_change_callback' function and pass the display name as well as the current selection to it
            self.on_change_callback(
                self.display_name,
                self.get(dispatch=False),
            )

    @override
    def clear(
        self,
        dispatch: bool = False,
    ) -> None:
        """
        Clears all selected checkbuttons in the field.

        Resets all checkbuttons to an unselected state. Optionally dispatches a
        CHECKBUTTON_SELECT_FIELD_CLEARED event with the current selection state.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            None
        """

        # Iterate over the keys and values of the fields dictionary instance variable
        for (
            key,
            value,
        ) in self.fields.items():
            # Update the value of the checkbutton field to False
            value.set(
                dispatch=False,
                value=False,
            )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the CHECKBUTTON_SELECT_FIELD_CLEARED event
            self.dispatcher.dispatch(
                event=Events.CHECKBUTTON_SELECT_FIELD_CLEARED,
                label=self.display_name,
                namespace=self.namespace,
                value=self.get(dispatch=False),
            )

    def configure_field(
        self,
        field: str,
        attribute: Literal["checkbutton", "label"],
        **kwargs,
    ) -> None:
        """
        Attempts to configure the passed attribute of the passed field.

        This method attempts to configure the checkbutton field widget based on the passed 'field' and 'attribute' keywords
        using the provided keyword arguments.

        Args:
            field (str): The name (label) of the field of which the attribute is to be configured.
            attribute (Literal["checkbutton", "label"]): The attribute of the field that is to be configured.
            **kwargs: The keyword arguments to be passed to the configure method
                of the corresponding field's attribute widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                label widget.
        """
        try:
            # Check, if the passed field is in the keys of fields dictionary instance variable
            if field not in self.fields.keys():
                # Log a warning message
                self.logger.warning(
                    message=f"Field with label '{field}' not found in 'fields' dictionary. This is likely due to a typo."
                )

                # Return early
                return

            # Store the looked up field in a variable
            field: CheckbuttonField = self.fields[field]

            # Generate the corresponding method name
            method: str = f"configure_{attribute}"

            # Check if the field has the 'configure_{attribute}' method
            if not hasattr(
                field,
                method,
            ):
                # Log a warning message
                self.logger.warning(
                    message=f"Field with label '{field}' does not have any 'configure_{attribute}' attribute. This is likely due the method not being implemented."
                )

                # Return early
                return

            # Call the corresponding field's 'configure_{attribute}' and pass **kwargs to it
            getattr(
                field,
                method,
            )(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_field' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @override
    def configure_grid(self) -> None:
        """
        Configures the grid layout for the CheckbuttonSelectField widget.

        Sets the column and row weights to ensure the layout behaves responsively
        when the parent window is resized. This method is called during initialization.

        Returns:
            None
        """

        # Set the weight of the 0th column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_columnconfigure(
            index=0,
            weight=0,
        )

        # Set the weight of the 0th row to 0
        # This means that the row will not stretch when the window is resized
        self.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Iterate over the values in the fields dictionary
        for index in enumerate(
            iterable=[value for value in self.fields.values() if value is not None],
            start=1,
        ):
            # Set the weight of the row at the index to 0
            # This means that the row will not stretch when the window is resized
            self.grid_rowconfigure(
                index=index,
                weight=0,
            )

    def configure_label(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the label widget in this field.

        This method configures the label widget in this field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the label widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                label widget.
        """
        try:
            # Attempt to configure the label widget
            self._label.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_label' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @override
    def create_widgets(
        self,
        label: str,
        **kwargs,
    ) -> None:
        """
        Creates and configures all widgets for the CheckbuttonSelectField.

        This method creates the label and all checkbuttons based on the provided options.
        Each checkbutton is placed in its own row within the widget's grid.

        Args:
            label (str): The display label for the field.
            options (List[str]): A list of option strings to create individual checkbuttons for.
            **kwargs: Additional keyword arguments for field customization.

        Returns:
            None
        """

        # Create a label widget
        self._label: tkinter.Label = tkinter.Label(
            master=self, text=label, **kwargs.get("label", {})
        )

        # Place the label widget within the grid
        self._label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Iterate over the labels in the keys of the fields dictionary instance variable
        for (
            row,
            label,
        ) in enumerate(
            iterable=self.fields.keys(),
            start=1,
        ):
            # Create a checkbutton field widget
            checkbutton_field: CheckbuttonField = CheckbuttonField(
                label=label,
                master=self,
                namespace=self.namespace,
                on_change_callback=self._on_field_change,
            )

            # Place the checkbutton field widget within the grid
            checkbutton_field.grid(column=0, padx=5, pady=5, row=row)

            # Add the checkbutton field widget to the fields dictionary instance variable
            self.fields[label] = checkbutton_field

        # Configure the grid
        self.configure_grid()

    @override
    def get(
        self,
        label: str,
        dispatch: bool = False,
    ) -> Tuple[str, Dict[str, bool]]:
        """
        Retrieves the current selection from the field.

        Returns the selected option(s) based on the current state of the checkbuttons
        and the selection mode. If dispatch is True, an event will be emitted.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            Tuple[str, Union[str, List[str]]]: A tuple containing the field label and the current selection.
        """

        # Check, if the passed label is present within the keys of the 'fields' dictionary instance variable
        if label not in self.fields.keys():
            # Log a warning message
            self.logger.warning(
                message=f"Field with label '{label}' not found in 'fields' dictionary. This is likely due to a typo."
            )

            # Return early
            return

        # Obtain the label of the field as well as the labels and values of the fields
        (
            label,
            value,
        ) = (
            self.display_name,
            {
                key: value.get(dispatch=False)
                for (
                    key,
                    value,
                ) in self.fields.items()
            },
        )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the CHECKBUTTON_SELECT_FIELD_GET event
            self.dispatcher.dispatch(
                event=Events.CHECKBUTTON_SELECT_FIELD_GET,
                label=self.display_name,
                namespace=self.namespace,
                value=value,
            )

        # Return the label of this field and the values of the checkbutton fields
        return (
            label,
            value,
        )

    @override
    def set(
        self,
        label: str,
        value: bool,
        dispatch: bool = False,
    ) -> None:
        """
        Sets the selection state of the checkbuttons based on the given value(s).

        Updates each checkbutton to match the provided selection(s). If dispatch is True,
        a CHECKBUTTON_SELECT_FIELD_SET event will be emitted.

        Args:
            value (Union[str, List[str]]): A single option or list of options to select.
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.
        """

        # Check, if the passed label is present within the keys of the 'fields' dictionary instance variable
        if label not in self.fields.keys():
            # Log a warning message
            self.logger.warning(
                message=f"Field with label '{label}' not found in 'fields' dictionary. This is likely due to a typo."
            )

            # Return early
            return

        # Set the value of the corresponding checkbutton field
        self.fields[label].set(value=value)

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the CHECKBUTTON_SELECT_FIELD_SET event
            self.dispatcher.dispatch(
                event=Events.CHECKBUTTON_SELECT_FIELD_SET,
                label=self.display_name,
                namespace=self.namespace,
                value=self.get(dispatch=False),
            )


class ComboboxField(BaseField):
    """
    A string selection field using a tkinter Combobox.

    ComboboxField represents a selectable user input field consisting of a label, a combobox,
    and an optional clear button. It supports both readonly and editable input modes, making it
    suitable for predefined options as well as user-defined values.

    The field layout consists of:
        [ Label | Combobox | Button ]

    Attributes:
        values (List[str]): List of predefined selectable values shown in the dropdown.
        label (tkinter.Label): The label widget associated with this field.
        combobox (ttk.Combobox): The interactive dropdown widget.
        button (tkinter.Button): A button used to clear the combobox content.
        variable (tkinter.StringVar): A string variable bound to the combobox value.
        readonly (bool): Whether the combobox is readonly (non-editable).

    Inherits from:
        BaseField
    """

    def __init__(
        self,
        label: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, str], None]] = None,
        readonly: bool = False,
        value: Optional[str] = None,
        values: Optional[List[str]] = None,
    ) -> None:
        """
        Initializes a new instance of the ComboboxField class.

        This method sets up the label, combobox, and optional clear button. It also initializes
        the list of selectable values and optionally sets a default value.

        Args:
            label (str): The label text displayed next to the field.
            master (tkinter.Misc): The parent container in which this widget is placed.
            namespace (str, optional): The namespace identifier for event dispatching. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[str, str], None]], optional): Callback function called when the selected value changes.
            readonly (bool, optional): Whether the combobox should be readonly (i.e., selection only). Defaults to False.
            value (Optional[str], optional): Initial value to pre-fill the combobox. Defaults to None.
            values (Optional[List[str]], optional): The list of selectable options. Defaults to an empty list.

        Returns:
            None
        """

        # Store the passed 'values' list or initialize it as an empty list
        self.values: List[str] = values if values is not None else []

        # Call the parent class constructor with the passed arguments
        super().__init__(
            label=label,
            master=master,
            namespace=namespace,
            on_change_callback=on_change_callback,
        )

        # Check, if the passed value is not None
        if value is not None:
            # Set the value of the field to the passed value
            self.set(value=value)

        # Configure the combobox widget's state to normal or readonly
        self._combobox.configure(state=NORMAL if not readonly else "readonly")

    @property
    def button(self) -> tkinter.Button:
        """
        Returns the clear button widget associated with this field.

        This button allows the user to clear the current selection in the combobox.

        Returns:
            tkinter.Button: The button widget.
        """

        # Return the tkinter.Button button widget
        return self._button

    @property
    def combobox(self) -> ttk.Combobox:
        """
        Returns the combobox widget used for selecting or entering a value.

        Returns:
            ttk.Combobox: The combobox widget tied to this field.
        """

        # Return the ttk.Combobox combobox widget
        return self._combobox

    @property
    def label(self) -> tkinter.Label:
        """
        Returns the label widget associated with this field.

        The label displays the name or description of the field.

        Returns:
            tkinter.Label: The label widget.
        """

        # Return the tkinter.Label label widget
        return self._label

    def _on_combobox_return(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        Handles manual text entry in the combobox (when not readonly).

        This method is triggered when the user confirms a manually entered value via the Return key.
        It adds the new value to the available options if it's not already present, then dispatches
        a change event.

        Args:
            event (Optional[tkinter.Event], optional): The event object triggered by pressing <Return>. Defaults to None.

        Returns:
            None
        """

        # Obtain the current value of the tkinter.StringVar variable
        value: str = self.variable.get()

        # Check, if the value obtained from the tkinter.StringVar variableis an empty string
        if value == "":
            # Return early
            return

        # Check, if the value string is not already within the list of values
        if value not in self.values:
            # Append the value string to the list of values
            self.values.append(value)

        # Dispatch the COMBOBOX_FIELD_CHANGED event
        self.dispatcher.dispatch(
            event=Events.COMBOBOX_FIELD_CHANGED,
            label=self.display_name,
            namespace=self.namespace,
            value=self.variable.get(),
        )

        # Check, if the 'on_change_callback' function exists
        if self.on_change_callback:
            # Call the 'on_change_callback' function and pass the display name as well as the variable's value to it
            self.on_change_callback(
                self.display_name,
                self.variable.get(),
            )

    def _on_combobox_select(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        Handles selection from the dropdown menu of the combobox.

        This method is triggered when the user selects an existing item from the dropdown list.
        It dispatches a change event with the selected value.

        Args:
            event (Optional[tkinter.Event], optional): The event object triggered by <<ComboboxSelected>>. Defaults to None.

        Returns:
            None
        """

        # Dispatch the COMBOBOX_FIELD_CHANGED event
        self.dispatcher.dispatch(
            event=Events.COMBOBOX_FIELD_CHANGED,
            label=self.display_name,
            namespace=self.namespace,
            value=self.variable.get(),
        )

        # Check, if the 'on_change_callback' function exists
        if self.on_change_callback:
            # Call the 'on_change_callback' function and pass the display name as well as the variable's value to it
            self.on_change_callback(
                self.display_name,
                self.variable.get(),
            )

    def add(
        self,
        value: str,
    ) -> None:
        """ """

        # Check, if the value is not already contained within the values list instacne variable
        if value not in self.values:
            # Append the passed value to the list of values
            self.values.append(value)

    @override
    def clear(
        self,
        dispatch: bool = False,
    ) -> None:
        """
        Clears the current selection or entry in the combobox.

        If `dispatch` is set to True, a clear event is dispatched to notify listeners
        that the combobox has been cleared.

        Args:
            dispatch (bool, optional): Whether to dispatch a clear event. Defaults to False.

        Returns:
            None
        """

        # Update the variable's value to an empty string
        self.variable.set(value="")

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the COMBOBOX_FIELD_CLEARED event
            self.dispatcher.dispatch(
                event=Events.COMBOBOX_FIELD_CLEARED,
                label=self.display_name,
                namespace=self.namespace,
                value=self.variable.get(),
            )

    def configure_button(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the button widget in the date select field.

        This method configures the button widget in the date select field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the button widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                button widget.
        """
        try:
            # Attempt to configure the button widget
            self._button.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_button' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_combobox(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the combobox widget in the date select field.

        This method configures the combobox widget in the date select field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the combobox widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                combobox widget.
        """
        try:
            # Attempt to configure the combobox widget
            self._combobox.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_combobox' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @override
    def configure_grid(self) -> None:
        """
        Configures the grid layout of the ComboboxField widget.

        This method sets the column and row weights for the internal layout of the ComboboxField.
        It ensures proper resizing behavior and alignment of label, combobox, and buttons.

        Columns:
            - Column 0: Label (fixed width)
            - Column 1: Combobox field (expandable)
            - Column 2: Button (fixed width)

        Rows:
            - Row 0: Main field layout (fixed height)

        Returns:
            None
        """

        # Set the weight of the 0th column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_columnconfigure(
            index=0,
            weight=0,
        )

        # Set the weight of the 1st column to 1
        # This means that the column will stretch when the window is resized
        self.grid_columnconfigure(
            index=1,
            weight=1,
        )

        # Set the weight of the 2nd column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_columnconfigure(
            index=2,
            weight=0,
        )

        # Set the weight of the 0th row to 0
        # This means that the row will not stretch when the window is resized
        self.grid_rowconfigure(
            index=0,
            weight=0,
        )

    def configure_label(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the label widget in this field.

        This method configures the label widget in this field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the label widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                label widget.
        """
        try:
            # Attempt to configure the label widget
            self._label.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_label' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @override
    def create_widgets(
        self,
        label: str,
        **kwargs,
    ) -> None:
        """
        Creates and configures the widgets for the ComboboxField.

        This method initializes the label, combobox (with optional readonly state),
        and clear button. It also binds keyboard and selection events to appropriate
        handlers and sets the widget layout within the grid.

        Args:
            label (str): The text to display in the label.
            values (Optional[List[str]], optional): The list of values to populate the combobox with.
            value (Optional[str], optional): The default value to pre-fill the combobox. Defaults to None.
            **kwargs: Additional keyword arguments for the individual widgets (label, combobox, button).

        Returns:
            None
        """

        # Create a label widget
        self._label: tkinter.Label = tkinter.Label(
            master=self, text=label, **kwargs.get("label", {})
        )

        # Place the label widget within the grid
        self._label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a string variable
        self.variable: tkinter.StringVar = tkinter.StringVar(value="")

        # Create a combobox widget
        self._combobox: ttk.Combobox = ttk.Combobox(
            master=self,
            textvariable=self.variable,
            values=self.values,
            **kwargs.get(
                "combobox",
                {},
            ),
        )

        # Place the combobox widget within the grid
        self._combobox.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Bind the 'on_combobox_change' method to the combobox via the '<Return>' event
        self._combobox.bind(
            func=self._on_combobox_return,
            sequence="<Return>",
        )

        # Bind the 'on_combobox_select' method to the combobox via the '<<ComboboxSelected>>' event
        self._combobox.bind(
            func=self._on_combobox_select,
            sequence="<<ComboboxSelected>>",
        )

        # Create the button widget
        self._button: tkinter.Button = tkinter.Button(
            command=lambda: self.clear(dispatch=True),
            master=self,
            text="X",
            **kwargs.get(
                "button",
                {},
            ),
        )

        # Place the button widget within the grid
        self._button.grid(
            column=2,
            padx=5,
            pady=5,
            row=0,
        )

    @override
    def get(
        self,
        dispatch: bool = False,
    ) -> Tuple[str, Any]:
        """
        Retrieves the current selected or entered value of the combobox.

        If `dispatch` is set to True, a get event is dispatched.

        Args:
            dispatch (bool, optional): Whether to dispatch a get event. Defaults to False.

        Returns:
            Tuple[str, Any]: A tuple containing the label and the current value of the field.
        """

        # Obtain the label and value strings from the widgets
        (
            label,
            value,
        ) = (
            self.display_name,
            self.variable.get(),
        )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the COMBOBOX_FIELD_GET event
            self.dispatcher.dispatch(
                event=Events.COMBOBOX_FIELD_GET,
                label=label,
                namespace=self.namespace,
                value=value,
            )

        # Return the text of the label and the value of the text field
        return (
            label,
            value,
        )

    @override
    def set(
        self,
        value: str,
        dispatch: bool = False,
    ) -> None:
        """
        Sets the combobox value to the specified input.

        If the value is not already in the list of values, it is added. Optionally,
        a set event is dispatched if `dispatch` is True.

        Args:
            value (str): The value to be set in the combobox.
            dispatch (bool, optional): Whether to dispatch a set event. Defaults to False.

        Returns:
            None
        """

        # Check, if the value string is not already within the list of values
        if value not in self.values:
            # Append the value string to the list of values
            self.values.append(value)

        # Update the variable with the passed value string
        self.variable.set(value=value)

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the COMBOBOX_FIELD_SET event
            self.dispatcher.dispatch(
                event=Events.COMBOBOX_FIELD_SET,
                label=self.display_name,
                namespace=self.namespace,
                value=self.variable.get(),
            )


class ComboboxSelectField(BaseField):
    """
    A grouped dropdown selection field using multiple ComboboxFields.

    ComboboxSelectField represents a group of labeled dropdowns (comboboxes), where each dropdown is
    an independent selection field. It is useful for capturing multiple structured selections from
    the user, such as assigning a category to each option label.

    The layout consists of:
        [ Label ]
        [ Label 1 | Combobox 1 | Button 1 ]
        [ Label 2 | Combobox 2 | Button 2 ]
        ...
        [ Label n | Combobox n | Button n ]

    Attributes:
        fields (Dict[str, Optional[ComboboxField]]): A dictionary mapping option labels to their ComboboxField widgets.

    Inherits from:
        BaseField
    """

    def __init__(
        self,
        label: str,
        labels: List[str],
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, Dict[str, str]], None]] = None,
        values: Optional[Dict[str, List[str]]] = None,
    ) -> None:
        """
        Initializes a new instance of the ComboboxelectField class.

        This constructor sets up multiple ComboboxFields, each associated with a specific label,
        and arranges them in a unified vertical layout. Optionally, predefined values can be
        assigned to each dropdown.

        Args:
            label (str): The overarching label describing the field group.
            labels (List[str]): A list of labels for individual comboboxes.
            master (tkinter.Misc): The parent container for the widget group.
            namespace (str, optional): The namespace for event dispatching.
            on_change_callback (Optional[Callable[[str, Dict[str, str]]]]): Optional callback for value changes.
            values (Optional[Dict[str, List[str]]]): Optional dict of predefined values for each combobox.

        Returns:
            None
        """

        # Initialize the fields dictionary
        self.fields: Dict[str, Optional[ComboboxField]] = {
            field: None for field in labels
        }

        # Call the parent class constructor with the passed arguments
        super().__init__(
            label=label,
            master=master,
            namespace=namespace,
            on_change_callback=on_change_callback,
            values=values,
        )

    @property
    def label(self) -> tkinter.Label:
        """
        Returns the label widget associated with this field.

        The label displays the name or description of the field.

        Returns:
            tkinter.Label: The label widget.
        """

        # Return the tkinter.Label label widget
        return self._label

    def _on_field_change(
        self,
        label: str,
        value: str,
    ) -> None:
        """
        Handles internal changes from individual ComboboxFields.

        This method is triggered when the user selects or enters a value in one of the comboboxes.
        It triggers event dispatching and invokes any on_change_callback provided.

        Args:
            label (str): The label of the combobox that triggered the change.
            value (str): The new selected or entered value.

        Returns:
            None
        """

        # Dispatch the COMBOBOX_SELECT_FIELD_CHANGED event
        self.dispatcher.dispatch(
            event=Events.COMBOBOX_SELECT_FIELD_CHANGED,
            label=self.display_name,
            namespace=self.namespace,
            value=self.get(),
        )

        # Check, if the 'on_change_callback' function exists
        if self.on_change_callback:
            # Call the 'on_change_callback' function and pass the display name as well as the current selection to it
            self.on_change_callback(
                self.display_name,
                self.get(dispatch=False),
            )

    def add_value(
        self,
        label,
        value: Union[List[str], str],
    ) -> None:
        """
        Adds new option(s) to a specified combobox field.

        This method supports both single string inputs and lists of strings. The values are added
        to the dropdown list for the combobox matching the provided label.

        Args:
            label (str): The label of the combobox to update.
            value (Union[List[str], str]): One or more values to add to the dropdown list.

        Returns:
            None
        """

        # Check, if the passed label is present within the keys of the 'fields' dictionary instance variable
        if label not in self.fields.keys():
            # Log a warning message
            self.logger.warning(
                message=f"Field with label '{label}' not found in 'fields' dictionary. This is likely due to a typo."
            )

            # Return early
            return

        # Check, if value is not an instance of list
        if not isinstance(
            value,
            list,
        ):
            value = [value]

        # Extend the 'values' of the corresponding combobox field with the passed values
        self.fields[label].cget("values").extend(value)

    @override
    def clear(
        self,
        dispatch: bool = False,
    ) -> None:
        """
        Clears all combobox fields in the field.

        Sets all combobox fields to an empty string. Optionally dispatches a
        COMBOBOXS_SELECT_FIELD_CLEARED event with the current selection state.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            None
        """

        # Iterate over the keys and values of the fields dictionary instance variable
        for (
            key,
            value,
        ) in self.fields.items():
            # Update the value of the checkbutton field to an empty string
            value.set(
                dispatch=False,
                value="",
            )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the COMBOBOXS_SELECT_FIELD_CLEARED event
            self.dispatcher.dispatch(
                event=Events.COMBOBOXS_SELECT_FIELD_CLEARED,
                label=self.display_name,
                namespace=self.namespace,
                value=self.get(dispatch=False),
            )

    def configure_field(
        self,
        field: str,
        attribute: Literal["checkbutton", "label"],
        **kwargs,
    ) -> None:
        """
        Attempts to configure the passed attribute of the passed field.

        This method attempts to configure the checkbutton field widget based on the passed 'field' and 'attribute' keywords
        using the provided keyword arguments.

        Args:
            field (str): The name (label) of the field of which the attribute is to be configured.
            attribute (Literal["checkbutton", "label"]): The attribute of the field that is to be configured.
            **kwargs: The keyword arguments to be passed to the configure method
                of the corresponding field's attribute widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                label widget.
        """
        try:
            # Check, if the passed field is in the keys of fields dictionary instance variable
            if field not in self.fields.keys():
                # Log a warning message
                self.logger.warning(
                    message=f"Field with label '{field}' not found in 'fields' dictionary. This is likely due to a typo."
                )

                # Return early
                return

            # Store the looked up field in a variable
            field: ComboboxField = self.fields[field]

            # Generate the corresponding method name
            method: str = f"configure_{attribute}"

            # Check if the field has the 'configure_{attribute}' method
            if not hasattr(
                field,
                method,
            ):
                # Log a warning message
                self.logger.warning(
                    message=f"Field with label '{field}' does not have any 'configure_{attribute}' attribute. This is likely due the method not being implemented."
                )

                # Return early
                return

            # Call the corresponding field's 'configure_{attribute}' and pass **kwargs to it
            getattr(
                field,
                method,
            )(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_field' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @override
    def configure_grid(self) -> None:
        """
        Configures the grid layout for the ComboboxSelectField widget.

        Sets the column and row weights to ensure the layout behaves responsively
        when the parent window is resized. This method is called during initialization.

        Returns:
            None
        """

        # Set the weight of the 0th column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_columnconfigure(
            index=0,
            weight=0,
        )

        # Set the weight of the 0th row to 0
        # This means that the row will not stretch when the window is resized
        self.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Iterate over the values in the fields dictionary
        for index in enumerate(
            iterable=[value for value in self.fields.values() if value is not None],
            start=1,
        ):
            # Set the weight of the row at the index to 0
            # This means that the row will not stretch when the window is resized
            self.grid_rowconfigure(
                index=index,
                weight=0,
            )

    def configure_label(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the label widget in this field.

        This method configures the label widget in this field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the label widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                label widget.
        """
        try:
            # Attempt to configure the label widget
            self._label.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_label' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @override
    def create_widgets(
        self,
        label: str,
        **kwargs,
    ) -> None:
        """
        Creates and configures all widgets for the ComboboxSelectField.

        This method creates the label and all combobox fields based on the provided keyword arguments.
        Each combobox field is placed in its own row within the widget's grid.

        Args:
            label (str): The display label for the field.
            **kwargs: Additional keyword arguments for field customization.

        Returns:
            None
        """

        # Create a label widget
        self._label: tkinter.Label = tkinter.Label(
            master=self, text=label, **kwargs.get("label", {})
        )

        # Place the label widget within the grid
        self._label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Obtain the value associated with the "values" key from the kwargs
        values: Dict[str, Any] = kwargs.get(
            "values",
            {},
        )

        # Iterate over the labels in the keys of the fields dictionary instance variable
        for (
            row,
            label,
        ) in enumerate(
            iterable=self.fields.keys(),
            start=1,
        ):
            # Create a combobox field widget
            combobox_field: ComboboxField = ComboboxField(
                label=label,
                master=self,
                namespace=self.namespace,
                on_change_callback=self._on_field_change,
                values=values.get(
                    label,
                    [],
                ),
            )

            # Place the combobox field widget within the grid
            combobox_field.grid(column=0, padx=5, pady=5, row=row)

            # Add the combobox field widget to the fields dictionary instance variable
            self.fields[label] = combobox_field

        # Configure the grid
        self.configure_grid()

    @override
    def get(
        self,
        label: str,
        dispatch: bool = False,
    ) -> Tuple[str, Dict[str, str]]:
        """
        Retrieves the current selection from the field.

        Returns the selected option(s) based on the current state of the checkbuttons
        and the selection mode. If dispatch is True, an event will be emitted.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            Tuple[str, Dict[str, str]]: A tuple containing this field's label
            and a dictionary containing the checkbutton fields labels and current values.
        """

        # Check, if the passed label is present within the keys of the 'fields' dictionary instance variable
        if label not in self.fields.keys():
            # Log a warning message
            self.logger.warning(
                message=f"Field with label '{label}' not found in 'fields' dictionary. This is likely due to a typo."
            )

            # Return early
            return

        # Obtain the label of the field as well as the labels and values of the fields
        (
            label,
            value,
        ) = (
            self.display_name,
            {
                key: value.get(dispatch=False)
                for (
                    key,
                    value,
                ) in self.fields.items()
            },
        )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the CHECKBUTTON_SELECT_FIELD_GET event
            self.dispatcher.dispatch(
                event=Events.CHECKBUTTON_SELECT_FIELD_GET,
                label=self.display_name,
                namespace=self.namespace,
                value=value,
            )

        # Return the label of this field and the values of the checkbutton fields
        return (
            label,
            value,
        )

    @override
    def set(
        self,
        label: str,
        value: str,
        dispatch: bool = False,
    ) -> None:
        """
        Sets the value of the combobox fields based on the given value.

        Updates the combobox field corresponding to the passed label with the passed value. If dispatch is True,
        a COMBOBOX_SELECT_FIELD_SET event will be emitted.

        Args:
            value (Union[str, List[str]]): A single option or list of options to select.
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            None
        """

        # Check, if the passed label is present within the keys of the 'fields' dictionary instance variable
        if label not in self.fields.keys():
            # Log a warning message
            self.logger.warning(
                message=f"Field with label '{label}' not found in 'fields' dictionary. This is likely due to a typo."
            )

            # Return early
            return

        # Set the value of the corresponding checkbutton field
        self.fields[label].set(value=value)

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the COMBOBOX_SELECT_FIELD_SET event
            self.dispatcher.dispatch(
                event=Events.COMBOBOX_SELECT_FIELD_SET,
                label=self.display_name,
                namespace=self.namespace,
                value=self.get(dispatch=False),
            )


class EntityComboboxField(BaseField):
    """
    A generic field widget for selecting entities via a combobox.

    The `EntityComboboxField` is a reusable form element that displays a combobox
    with selectable entity labels (e.g., names of stacks, questions, teachers, etc.).
    It supports filtering, mapping, and selection handling through callback logic
    and dynamic internal storage.

    Features:
    - Automatically maps a list of entities to a dictionary of display labels and corresponding objects.
    - Supports dynamic filtering of the entity list via a user-defined `filter_func`.
    - Notifies selection changes via dispatcher events and optional callback handlers.
    - Can optionally support the creation of new entities via Return key input.

    Args:
        label (str): The label displayed to the left of the combobox.
        master (tkinter.Misc): The parent widget for this field.
        namespace (str): The namespace used for dispatching events.
        on_change_callback (Optional[Callable[[str, Any], None]]): Callback function triggered on value change.
        value (Optional[Any]): The initial value to display and map from.
        entities (Optional[List[Any]]): The list of entities to populate the combobox with.
        key (Optional[str]): The name of the attribute to use as the display label for each entity.
        filter_func (Optional[Callable[[Any], bool]]): An optional filtering function to narrow down shown entities.
        **kwargs: Additional keyword arguments passed to sub-widgets (label, combobox, etc.).
    """

    def __init__(
        self,
        entity_select_type: EntitySelectTypes,
        label,
        master,
        display_callback: Optional[Callable[[Any], str]] = None,
        filter_callback: Optional[Callable[[Any], bool]] = None,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, Any], None]] = None,
        readonly: bool = False,
        value: Optional[Any] = None,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the EntityComboboxField class.

        This special field displays a combobox populated with entities from the database,
        allowing the user to select one. It supports filtering and custom display formatting
        through optional callbacks.

        Args:
            entity_select_type (EntitySelectTypes): The type of entity to be displayed and selected.
            label (str): The label to display next to the combobox.
            master (tkinter.Misc): The parent widget for this field.
            display_callback (Optional[Callable[[Any], str]]): A function used to convert entities into display strings.
            filter_callback (Optional[Callable[[Any], bool]]): A function used to filter the list of available entities.
            namespace (str, optional): The namespace for event dispatching.
            on_change_callback (Optional[Callable[[str, Any], None]], optional): A callback invoked when the selection changes.
            readonly (bool, optional): Whether the combobox should be read-only. Defaults to False.
            value (Optional[Any], optional): The initial value of the field.
            **kwargs: Additional keyword arguments for styling and widget customization.
        """

        # Store the passed entity select type in an instance variable
        self.entity_select_type: EntitySelectTypes = entity_select_type

        self.values: Dict[str, Any] = self._compile_values(
            display_callback=display_callback,
            filter_callback=filter_callback,
        )

        # Call the parent class constructor with the passed arguments
        super().__init__(
            label=label,
            master=master,
            namespace=namespace,
            on_change_callback=on_change_callback,
            value=value,
            **kwargs,
        )

        # Check, if the passed value is not None
        if value is not None:
            # Set the value of the field to the passed value
            self.set(value=value)

        # Configure the combobox widget's state to normal or readonly
        self._combobox.configure(state=NORMAL if not readonly else "readonly")

    @property
    def button(self) -> tkinter.Button:
        """
        Returns the clear button widget associated with this field.

        This button allows the user to clear the current selection in the combobox.

        Returns:
            tkinter.Button: The button widget.
        """

        # Return the tkinter.Button button widget
        return self._button

    @property
    def combobox(self) -> ttk.Combobox:
        """
        Returns the combobox widget used for selecting or entering a value.

        Returns:
            ttk.Combobox: The combobox widget tied to this field.
        """

        # Return the ttk.Combobox combobox widget
        return self._combobox

    @property
    def label(self) -> tkinter.Label:
        """
        Returns the label widget associated with this field.

        The label displays the name or description of the field.

        Returns:
            tkinter.Label: The label widget.
        """

        # Return the tkinter.Label label widget
        return self._label

    def _apply_display_callback(
        self,
        entity: Any,
        display_callback: Optional[Callable[[Any], str]] = None,
    ) -> str:
        """
        Applies a display formatting function to the given entity.

        This method determines how a given entity will be shown in the combobox.
        If no display_callback is provided, a default representation (ID and key) is used.

        Args:
            entity (Any): The entity to format.
            display_callback (Optional[Callable[[Any], str]]): The formatting function.

        Returns:
            str: A string representing the entity for display in the combobox.
        """

        # Check, if a display callback has been passed
        if not display_callback:
            # Return a string of the entity's ID and key attributes
            return f"{entity.id} - {entity.key}"

        try:
            # Attempt to run the display callback and return its result
            return display_callback(entity)
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to call 'filter_callback' function ('{display_callback:__name__}') with '{entity.__repr__()}' entity. in '{self.__class__.__name__}' class."
            )

            # Log the traceback
            self.logger.error(message=traceback.format_exc())

            # Return a string of the entity's ID and key attributes
            return f"{entity.id} - {entity.key}"

    def _apply_filter_callback(
        self,
        entity: Any,
        filter_callback: Callable[[Any], bool],
    ) -> Any:
        """
        Applies a filter function to determine if the given entity should be included.

        If no filter_callback is defined, all entities are included.

        Args:
            entity (Any): The entity to evaluate.
            filter_callback (Optional[Callable[[Any], bool]]): The filtering function.

        Returns:
            Any: The original entity if included, or None if filtered out.
        """

        # Check, if a filter callback has been passed
        if not filter_callback:
            # Return the entity early
            return entity

        try:
            # Attempt to run the filter callback and return its result
            return filter_callback(entity)
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to call 'filter_callback' function ('{filter_callback:__name__}') with '{entity.__repr__()}' entity. in '{self.__class__.__name__}' class."
            )

            # Log the traceback
            self.logger.error(message=traceback.format_exc())

            # Return the entity
            return entity

    def _compile_values(
        self,
        display_callback: Optional[Callable[[Any], str]] = None,
        filter_callback: Optional[Callable[[Any], bool]] = None,
    ) -> Dict[str, Any]:
        """
        Compiles the values to be displayed in the combobox.

        This method fetches all available entities of the specified type from the database
        and applies the optional filter and display callbacks. It returns a dictionary that maps
        display strings to the actual entity instances.

        Args:
            display_callback (Optional[Callable[[Any], str]]): A function to convert each entity to a string.
            filter_callback (Optional[Callable[[Any], bool]]): A function to filter which entities are included.

        Returns:
            Dict[str, Any]: A dictionary where the keys are display names and the values are the original entities.
        """

        # Obtain the entities from the database
        entities: List[Any] = self._get_entities()

        # Filter the entities list by applying the filter function
        entities = [
            entity
            for entity in entities
            if self._apply_filter_callback(
                entity=entity,
                filter_callback=filter_callback,
            )
        ]

        # Return a dictionary where the keys are generated through the display name callable
        return {
            self._apply_display_callback(
                entity=entity,
                display_callback=display_callback,
            ): entity
            for entity in entities
        }

    def _get_entities(self) -> List[Any]:
        """
        Retrieves all entities of the specified type from the database.

        Returns:
            List[Any]: A list of entities corresponding to the selected EntitySelectType.
                    Returns an empty list if no entities are found or if an error occurs.
        """
        try:
            # Notify the REQUEST_GET_ALL event corresponding to the EntitySelectType
            notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
                event=self._get_fetch_event(),
                namespace=Constants.GLOBAL_NAMESPACE,
            )

            # Check, if the notification exists or if it has errors
            if not notification or notification.has_errors():
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to notify {self._get_fetch_event(entity_select_type=self.entity_select_type).__repr__()} event for 'global' namespace in {self.__class__.__name__} class."
                )

                # Return an empty list early
                return []

            # Return the one and only result of the notification
            return notification.get_one_and_only_result()
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run '_get_entities' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Return an empty list
            return []

    def _get_create_event(self) -> Optional[DispatcherEvent]:
        """
        Retrieves the DispatcherEvent for creating new entities of the current type.

        This event is used when the user wants to create a new instance of the selected entity type.

        Returns:
            Optional[DispatcherEvent]: The DispatcherEvent associated with creating this type of entity.
                                        Returns None if the event is not defined.
        """

        # A dictionary of EntitySelectTypes literals associated to DispatcherEvent objects
        dictionary: Dict[str, DispatcherEvent] = {
            "answer": Events.REQUEST_ANSWER_CREATE,
            "difficulty": Events.REQUEST_DIFFICULTY_CREATE,
            "flashcard": Events.REQUEST_FLASHCARD_CREATE,
            "note": Events.REQUEST_NOTE_CREATE,
            "priority": Events.REQUEST_PRIORITY_CREATE,
            "question": Events.REQUEST_QUESTION_CREATE,
            "stack": Events.REQUEST_STACK_CREATE,
            "status": Events.REQUEST_STATUS_CREATE,
            "subject": Events.REQUEST_SUBJECT_CREATE,
            "teacher": Events.REQUEST_TEACHER_CREATE,
            "user": Events.REQUEST_USER_CREATE,
        }

        # Attemt to get the DispatcherEvent associated with the passed EntitySelectTypes literal or None
        result: Optional[DispatcherEvent] = dictionary.get(
            self.entity_select_type,
            None,
        )

        # Check, if the result is not None
        if not result:
            # Log a warning message
            self.logger.warning(
                message=f"Unexpected EntitySelectTypes literal '{self.entity_select_type}'. This is likely due to it not being implemented in the '{self.__class__.__name__}' class."
            )

        # Return the result, no matter what
        return result

    def _get_fetch_event(self) -> Optional[DispatcherEvent]:
        """
        Retrieves the DispatcherEvent used to fetch entities of the current type from the database.

        This method helps centralize the event logic for loading data dynamically.

        Returns:
            Optional[DispatcherEvent]: The DispatcherEvent associated with fetching entities of the current type.
                                        Returns None if the event is not defined.
        """

        # A dictionary of EntitySelectTypes literals associated to DispatcherEvent objects
        dictionary: Dict[str, DispatcherEvent] = {
            "answer": Events.REQUEST_GET_ALL_ANSWERS,
            "difficulty": Events.REQUEST_GET_ALL_DIFFICULTIES,
            "flashcard": Events.REQUEST_GET_ALL_FLASHCARDS,
            "note": Events.REQUEST_GET_ALL_NOTES,
            "priority": Events.REQUEST_GET_ALL_PRIORITIES,
            "question": Events.REQUEST_GET_ALL_QUESTIONS,
            "stack": Events.REQUEST_GET_ALL_STACKS,
            "status": Events.REQUEST_GET_ALL_STATUSES,
            "subject": Events.REQUEST_GET_ALL_SUBJECTS,
            "teacher": Events.REQUEST_GET_ALL_TEACHERS,
            "user": Events.REQUEST_GET_ALL_USERS,
        }

        # Attemt to get the DispatcherEvent associated with the passed EntitySelectTypes literal or None
        result: Optional[DispatcherEvent] = dictionary.get(
            self.entity_select_type,
            None,
        )

        # Check, if the result is not None
        if not result:
            # Log a warning message
            self.logger.warning(
                message=f"Unexpected EntitySelectTypes literal '{self.entity_select_type}'. This is likely due to it not being implemented in the '{self.__class__.__name__}' class."
            )

        # Return the result, no matter what
        return result

    def _on_combobox_return(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        Handles the Return (Enter) key event for the combobox.

        This method is triggered when the user presses the Return key while the combobox
        is focused. If the current input does not match any known entity, a new one may be
        created by dispatching the corresponding creation event.

        Args:
            event (tkinter.Event): The keypress event object containing context about the Return keypress.

        Returns:
            None
        """

        # Obtain the entity from the values dictionary instance variable based on the user's current selection
        entity: Optional[Any] = UnifiedObjectFactory.create_default(
            factory=self.entity_select_type, **{"unspecified": self.variable.get()}
        )

        notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
            event=self._get_create_event(),
            namespace=self.namespace,
            **{
                entity.__class__.__name__.replace(
                    "Immutable",
                    "",
                ): entity
            },
        )

        # Check, if the notification exists or has errors
        if not notification or notification.has_errors():
            # Log a warning message
            self.logger.warning(
                message=f"Failed to notify {self._get_fetch_event(entity_select_type=self.entity_select_type).__repr__()} event for 'global' namespace in {self.__class__.__name__} class."
            )

            # Return early
            return

        # Update the entity with the notification's result
        entity = notification.get_one_and_only_result()

        # Add the newly created entity to the values dictionary instance variable
        self.values[self._apply_display_callback(entity=entity)] = (
            notification.get_one_and_only_result()
        )

        # Dispatch the ENTITY_COMBOBOX_FIELD_CHANGED event
        self.dispatcher.dispatch(
            event=Events.ENTITY_COMBOBOX_FIELD_CHANGED,
            label=self.display_name,
            namespace=self.namespace,
            value=entity,
        )

        # Check, if the 'on_change_callback' function exists
        if self.on_change_callback:
            # Call the 'on_change_callback' function and pass the display name as well as the entity to it
            self.on_change_callback(
                self.display_name,
                entity,
            )

    def _on_combobox_select(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        Handles the selection of an item from the combobox dropdown.

        When the user selects an item, this method updates the internal value,
        dispatches a corresponding change event, and invokes the on_change_callback
        if one is defined.

        Args:
            event (tkinter.Event): The event object triggered by the selection action.

        Returns:
            None
        """

        # Obtain the entity from the values dictionary instance variable based on the user's current selection
        entity: Optional[Any] = self.values.get(
            self.variable.get(),
            None,
        )

        # Dispatch the ENTITY_COMBOBOX_FIELD_CHANGED event
        self.dispatcher.dispatch(
            event=Events.ENTITY_COMBOBOX_FIELD_CHANGED,
            label=self.display_name,
            namespace=self.namespace,
            value=entity,
        )

        # Check, if the 'on_change_callback' function exists
        if self.on_change_callback:
            # Call the 'on_change_callback' function and pass the display name as well as the entity to it
            self.on_change_callback(
                self.display_name,
                entity,
            )

    @override
    def clear(
        self,
        dispatch: bool = False,
    ) -> None:
        """
        Clears the current selection in the combobox and optionally dispatches a clear event.

        Args:
            dispatch (bool): Whether to dispatch a clear event. Defaults to False.
        """
        self.variable.set(value="")

        if dispatch:
            self.dispatcher.dispatch(
                event=Events.ENTITY_COMBOBOX_FIELD_CLEARED,
                label=self.display_name,
                namespace=self.namespace,
                value=None,
            )

    def configure_button(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the button widget in the date select field.

        This method configures the button widget in the date select field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the button widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                button widget.
        """
        try:
            # Attempt to configure the button widget
            self._button.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_button' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_combobox(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the combobox widget in the date select field.

        This method configures the combobox widget in the date select field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the combobox widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                combobox widget.
        """
        try:
            # Attempt to configure the combobox widget
            self._combobox.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_combobox' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @override
    def configure_grid(self) -> None:
        """
        Configures the grid layout of the ComboboxField widget.

        This method sets the column and row weights for the internal layout of the ComboboxField.
        It ensures proper resizing behavior and alignment of label, combobox, and buttons.

        Columns:
            - Column 0: Label (fixed width)
            - Column 1: Combobox field (expandable)
            - Column 2: Button (fixed width)

        Rows:
            - Row 0: Main field layout (fixed height)

        Returns:
            None
        """

        # Set the weight of the 0th column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_columnconfigure(
            index=0,
            weight=0,
        )

        # Set the weight of the 1st column to 1
        # This means that the column will stretch when the window is resized
        self.grid_columnconfigure(
            index=1,
            weight=1,
        )

        # Set the weight of the 2nd column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_columnconfigure(
            index=2,
            weight=0,
        )

        # Set the weight of the 0th row to 0
        # This means that the row will not stretch when the window is resized
        self.grid_rowconfigure(
            index=0,
            weight=0,
        )

    def configure_label(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the label widget in this field.

        This method configures the label widget in this field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the label widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                label widget.
        """
        try:
            # Attempt to configure the label widget
            self._label.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_label' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @override
    def create_widgets(
        self,
        label: str,
        **kwargs,
    ) -> None:
        """
        Creates and configures the widgets for the EntityComboboxField.

        This method initializes the label, combobox (with optional readonly state),
        and clear button. It also binds keyboard and selection events to appropriate
        handlers and sets the widget layout within the grid.

        Args:
            label (str): The text to display in the label.
            values (Optional[List[str]], optional): The list of values to populate the combobox with.
            value (Optional[str], optional): The default value to pre-fill the combobox. Defaults to None.
            **kwargs: Additional keyword arguments for the individual widgets (label, combobox, button).

        Returns:
            None
        """

        # Create a label widget
        self._label: tkinter.Label = tkinter.Label(
            master=self,
            text=label,
            **kwargs.get(
                "label",
                {},
            ),
        )

        # Place the label widget within the grid
        self._label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a string variable
        self.variable: tkinter.StringVar = tkinter.StringVar(value="")

        # Create a combobox widget
        self._combobox: ttk.Combobox = ttk.Combobox(
            master=self,
            textvariable=self.variable,
            values=list(self.values.keys()),
            **kwargs.get(
                "combobox",
                {},
            ),
        )

        # Place the combobox widget within the grid
        self._combobox.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Bind the 'on_combobox_change' method to the combobox via the '<Return>' event
        self._combobox.bind(
            func=self._on_combobox_return,
            sequence="<Return>",
        )

        # Bind the 'on_combobox_select' method to the combobox via the '<<ComboboxSelected>>' event
        self._combobox.bind(
            func=self._on_combobox_select,
            sequence="<<ComboboxSelected>>",
        )

        # Create the button widget
        self._button: tkinter.Button = tkinter.Button(
            command=lambda: self.clear(dispatch=True),
            master=self,
            text="X",
            **kwargs.get(
                "button",
                {},
            ),
        )

        # Place the button widget within the grid
        self._button.grid(
            column=2,
            padx=5,
            pady=5,
            row=0,
        )

    @override
    def get(
        self,
        dispatch: bool = False,
    ) -> Tuple[str, Any]:
        """
        Retrieves the current selected or entered value of the combobox.

        If `dispatch` is set to True, a get event is dispatched.

        Args:
            dispatch (bool, optional): Whether to dispatch a get event. Defaults to False.

        Returns:
            Tuple[str, Any]: A tuple containing the label and the current value of the field.
        """

        # Obtain the label and value strings from the widgets
        (
            label,
            value,
        ) = (
            self.display_name,
            self.values.get(
                self.variable.get(),
                None,
            ),
        )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the COMBOBOX_FIELD_GET event
            self.dispatcher.dispatch(
                event=Events.COMBOBOX_FIELD_GET,
                label=label,
                namespace=self.namespace,
                value=value,
            )

        # Return the text of the label and the value of the text field
        return (
            label,
            value,
        )

    @override
    def set(
        self,
        value: Any,
        dispatch: bool = False,
    ) -> None:
        """
        Sets the combobox value to the specified input.

        If the value is not already in the list of values, it is added. Optionally,
        a set event is dispatched if `dispatch` is True.

        Args:
            value (Any): The value to be set in the combobox.
            dispatch (bool, optional): Whether to dispatch a set event. Defaults to False.

        Returns:
            None
        """

        # Generate a string key by calling the display callback on the passed value
        key: str = self._apply_display_callback(entity=value)

        # Check, if the value string is not already within the list of values
        if key not in self.values.keys():
            # Append the value string to the list of values
            self.values[key] = value

        # Update the variable with the passed value string
        self.variable.set(value=key)

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the COMBOBOX_FIELD_SET event
            self.dispatcher.dispatch(
                event=Events.COMBOBOX_FIELD_SET,
                label=self.display_name,
                namespace=self.namespace,
                value=self.variable.get(),
            )


class EntityMultiOptionSelectField(BaseField):
    """ """

    pass


class EntitySingleOptionSelectField(BaseField):
    """ """

    pass


class ListboxField(BaseField):
    """
    A field for selecting one or multiple values from a predefined list using a Listbox.

    This widget provides a user interface consisting of a label, a listbox, and a clear button.
    It supports both single and multiple selection modes and allows dynamic handling of selection
    changes and callbacks.

    The field layout consists of:
        [ Label ]
        [          Listbox          ]
                      [ Clearbutton ]

    Attributes:
        values (List[str]): The list of selectable values shown in the listbox.
        selection (List[str]): The currently selected values.
        variable (tkinter.StringVar): The underlying variable for the listbox items.
        listbox (tkinter.Listbox): The listbox widget.
        button (tkinter.Button): The button used to clear the selection.
        label (tkinter.Label): The descriptive label for the listbox field.

    Inherits from:
        BaseField
    """

    def __init__(
        self,
        label: str,
        master: tkinter.Misc,
        values: List[str],
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, List[str]], None]] = None,
        selectmode: Literal["expanded", "single"] = "single",
        value: Union[str, List[str]] = None,
        **kwargs,
    ) -> None:
        """ """

        # Initialize an empty list instance variable to hold the user's selection
        self.selection: Final[List[str]] = []

        # Store the passed values string list in an instance variable
        self.values: List[str] = values

        # Call the parent clas constructor
        super().__init__(
            label=label,
            master=master,
            namespace=namespace,
            on_change_callback=on_change_callback,
            selectmode=selectmode,
            **kwargs,
        )

        # Check, if the passed value is not None
        if value is not None:
            # Set the value of the listbox field
            self.set(value=value)

    @property
    def button(self) -> tkinter.Button:
        """
        Returns the clear button widget.

        Returns:
            tkinter.Button: The button used to clear the listbox selection.
        """

        # Return the tkinter.Button button widget
        return self._button

    @property
    def label(self) -> tkinter.Label:
        """
        Returns the label widget.

        Returns:
            tkinter.Label: The label describing the listbox field.
        """

        # Return the tkinter.Label label widget
        return self._label

    @property
    def listbox(self) -> tkinter.Listbox:
        """
        Returns the listbox widget.

        Returns:
            tkinter.Listbox: The listbox containing selectable values.
        """

        # Return the tkinter.Listbox listbox widget
        return self._listbox

    def _on_button_click(self) -> None:
        """
        Handles the clear button click.

        This method clears the current selection and resets the internal selection list.
        """

        # Clear the current selection of the listbox widget
        self._listbox.selection_clear(
            index1=0,
            index2=END,
        )

        # Clear the selection string list instace variable
        self.selection.clear()

    def _on_listbox_select(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        Handles selection events from the listbox.

        Updates the internal selection state and optionally calls the change callback and dispatches
        a change event.
        """

        # Obtain the indeces of the currently selected items of the listbox widget
        selection: Tuple[int, ...] = self.listbox.curselection()

        # Iterate over the indexes in the selection
        for index in selection:
            # Append the values from the index of the values list to the current selection
            self.selection.append(self.values[index])

        # Dispatch the LISTBOX_FIELD_CHANGED event
        self.dispatcher.dispatch(
            event=Events.LISTBOX_FIELD_CHANGED,
            label=self.display_name,
            namespace=self.namespace,
            value=self.selection,
        )

    @override
    def clear(
        self,
        dispatch: bool = False,
    ) -> None:
        """
        Clears the listbox selection.

        Args:
            dispatch (bool, optional): Whether to dispatch a clear event. Defaults to False.
        """

        # Clear the selection string list instace variable
        self.selection.clear()

    @override
    def configure_button(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the clear button widget.

        Args:
            **kwargs: Keyword arguments for tkinter.Button.configure.
        """
        try:
            # Attempt to configure the button widget
            self._button.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_button' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @override
    def configure_grid(self) -> None:
        """ """

        # Set the weight of the 0th column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_columnconfigure(
            index=0,
            weight=0,
        )

        # Set the weight of the 1st column to 1
        # This means that the column will stretch when the window is resized
        self.grid_columnconfigure(
            index=1,
            weight=1,
        )

        # Set the weight of the 2nd column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_columnconfigure(
            index=2,
            weight=0,
        )

        # Set the weight of the 0th row to 1
        # This means that the row will stretch when the window is resized
        self.grid_rowconfigure(
            index=0,
            weight=1,
        )

    @override
    def configure_label(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the label widget.

        Args:
            **kwargs: Keyword arguments for tkinter.Label.configure.
        """
        try:
            # Attempt to configure the label widget
            self._label.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_label' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @override
    def configure_listbox(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the listbox widget.

        Args:
            **kwargs: Keyword arguments for tkinter.Listbox.configure.
        """
        try:
            # Attempt to configure the listbox widget
            self._listbox.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_listbox' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @override
    def create_widgets(
        self,
        label: str,
        selectmode: Literal["expanded", "single"] = "single",
        **kwargs,
    ) -> None:
        """
        Creates and places the label, listbox, and clear button.

        Args:
            label (str): The field's label.
            selectmode (Literal["expanded", "single"], optional): Listbox selection mode. Defaults to "single".
            **kwargs: Additional customization for label, listbox, and button.
        """

        # Create a label widget
        self._label: tkinter.Label = tkinter.Label(
            master=self,
            text=label,
            **kwargs.get(
                "label",
                {},
            ),
        )

        # Place the label within the grid
        self._label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a string variable
        self.variable: tkinter.StringVar = tkinter.StringVar(value=dir(self.values))

        # Create the listbox widget
        self._listbox: tkinter.Listbox = tkinter.Listbox(
            listvariable=self.variable,
            master=self,
            selectmode=selectmode,
            **kwargs.get(
                "listbox",
                {},
            ),
        )

        # Place the listbox within the grid
        self._listbox.grid(
            column=1,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )

        # Bind the 'on_listbox_select' method to the listbox widget via the "<<ListboxSelected>>" event
        self._listbox.bind(
            func=self._on_listbox_select,
            sequence="<<ListboxSelect>>",
        )

        # Create a button widget
        self._button: tkinter.Button = tkinter.Button(
            command=self._on_button_click,
            master=self,
            text="X",
            **kwargs.get(
                "button",
                {},
            ),
        )

        # Place the label within the grid
        self._button.grid(
            column=2,
            padx=5,
            pady=5,
            row=2,
        )

    @override
    def get(
        self,
        dispatch: bool = False,
    ) -> Tuple[str, List[str]]:
        """
        Returns the current selection from the listbox.

        Args:
            dispatch (bool, optional): Whether to dispatch a get event. Defaults to False.

        Returns:
            Tuple[str, List[str]]: A tuple of field label and the selected values.
        """

        (
            label,
            value,
        ) = (
            self.display_name,
            self.selection,
        )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the LISTBOX_FIELD_GET event
            self.dispatcher.dispatch(
                event=Events.LISTBOX_FIELD_GET,
                label=self.display_name,
                namespace=self.namespace,
                value=value,
            )

        return (
            label,
            value,
        )

    @override
    def set(
        self,
        value: Union[List[str], str],
        dispatch: bool = False,
    ) -> None:
        """
        Sets the selection of the listbox to the given value(s).

        Args:
            value (Union[List[str], str]): A single or list of values to select.
            dispatch (bool, optional): Whether to dispatch a set event. Defaults to False.
        """

        if not isinstance(
            value,
            list,
        ):
            value = [value]

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the LISTBOX_FIELD_SET event
            self.dispatcher.dispatch(
                event=Events.LISTBOX_FIELD_SET,
                label=self.display_name,
                namespace=self.namespace,
                value=value,
            )


class OptionSelectFieldItem(tkinter.Frame):
    """ """

    def __init__(
        self,
        dispatcher: Dispatcher,
        id: int,
        namespace: str,
        master: tkinter.Misc,
        uuid: str,
        value: str,
        **kwargs,
    ) -> None:
        """ """

        # Initialize the logger instance of this clas
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed Dispatcher in an instance variable
        self.dispatcher: Final[Dispatcher] = dispatcher

        # Store the passed ID in an instance variable
        self._id: Final[int] = id

        # Store the passed namespace in an instance variable
        self.namespace: Final[str] = namespace

        # Store the passed UUID in an instance variable
        self._uuid: Final[str] = uuid

        # Store the passed value in an instance variable
        self._value: Final[str] = value

        # Configure the grid
        self.configure_grid()

        # Create the widgets
        self.create_widgets(
            value=value,
            **kwargs,
        )

    @property
    def id(self) -> int:
        """ """

        # Return the ID int
        return self._int

    @property
    def uuid(self) -> str:
        """ """

        # Return the UUID str
        return self._uuid

    @property
    def value(self) -> str:
        """ """

        # Return the value str
        return self._value

    def _on_button_click(self) -> None:
        """
        Handles the click event of the 'X' button in the option select field item.

        This method dispatches the REQUEST_OPTION_SELECT_FIELD_ITEM_DESTROY event to request
        that the corresponding item be removed from the parent field's selection.

        Returns:
            None

        Raises:
            Exception: If an error occurs during dispatch or internal processing.
        """
        try:
            # Attempt to disptach the REQUEST_OPTION_SELECT_FIELD_ITEM_DESTROY event in the local namespace
            self.dispatcher.dispatch(
                event=Events.REQUEST_OPTION_SELECT_FIELD_ITEM_DESTROY,
                namespace=self.namespace,
                value=self._value,
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run '_on_button_click' method from {self.__class__.__name__}: {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_button(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the button widget in this field.

        This method configures the button widget in this field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the button widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                button widget.
        """
        try:
            # Attempt to configure the button widget
            self.button.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_button' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_grid(self) -> None:
        """
        Configures the grid layout for the option select field item.

        This method defines the row and column weights for the item, ensuring proper layout
        behavior when resizing the window.

        Returns:
            None
        """

        # Set the weight of the 0th column to 1
        # This means that the column will stretch when the window is resized
        self.grid_columnconfigure(index=0, weight=1)

        # Set the weight of the 1st column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_columnconfigure(index=1, weight=0)

        # Set the weight of the 0th row to 1
        # This means that the row will stretch when the window is resized
        self.grid_rowconfigure(index=0, weight=1)

    def configure_label(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the label widget in this field.

        This method configures the label widget in this field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the label widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                label widget.
        """
        try:
            # Attempt to configure the label widget
            self.label.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_label' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def create_widgets(
        self,
        value: str,
        **kwargs,
    ) -> None:
        """ """

        # Create a label widget
        self.label: tkinter.Label = tkinter.Label(
            master=self,
            text=value,
            **kwargs,
        )

        # Place the label widget within the grid
        self.label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a button widget
        self.button: tkinter.Button = tkinter.Button(
            command=self._on_button_click,
            master=self,
            text="X",
            **kwargs,
        )

        # Place the button widget within the grid
        self.button.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
        )


class OptionSelectFieldItemFactory:
    """ """

    index: int = Constants.get_base_id()

    logger: Final[Logger] = Logger.get_logger(name="DispatcherEventFactory")

    @classmethod
    def create_option_select_field_item(
        cls,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        namespace: str,
        value: str,
        **kwargs,
    ) -> Optional[OptionSelectFieldItem]:
        """ """
        try:
            # Generate a new UUID code
            uuid: str = str(uuid.uuid4())

            # Attempt to create an OptionSelectFieldItem instance
            option_select_field_item: OptionSelectFieldItem = OptionSelectFieldItem(
                dispatcher=dispatcher,
                id=cls.index,
                master=master,
                namespace=namespace,
                uuid=uuid,
                value=value,
                **kwargs,
            )

            # Increment the class index
            cls.index += 1

            # Return the OptionSelectFieldItem instance
            return option_select_field_item
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'create_option_select_field_item' method from '{cls.__name__}' class: {e}"
            )

            # Log the traceback as error message
            cls.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e


class MultiOptionSelectField(BaseField):
    """ """

    def __init__(
        self,
        label: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, str], None]] = None,
        values: Optional[List[str]] = None,
    ) -> None:
        """ """

        # Generate a uniqe internal namespace
        self.internal_namespace: str = f"MULTI_OPTION_SELECT_FIELD({str(uuid.uuid4())})"

        # Initialize the (optional) listbox instance variable as None
        self.listbox: Optional[tkinter.Listbox] = None

        # Iniitialize the selection dictionary instance variable as an empty dictionary
        self.selection: Dict[str, Optional[OptionSelectFieldItem]] = {}

        # Initialize the (optional) toplevel instance variable as None
        self.toplevel: Optional[tkinter.Toplevel] = None

        # Initialize the tkinter.StringVar instance variable
        self.variable: tkinter.StringVar = tkinter.StringVar()

        # Store the passed values list of strings in an instance variable or initialize it as an empty list
        self.values: List[str] = values if values is not None else []

        # Call the parent class constructor with the passed arguments
        super().__init__(
            label=label,
            master=master,
            namespace=namespace,
            on_change_callback=on_change_callback,
        )

    @property
    def clear_button(self) -> tkinter.Button:
        """
        Returns the 'clear button' button widget associated with this field.

        Returns:
            tkinter.Button: The 'clear button' button widget.
        """

        # Return the 'clear button' button widget
        return self._clear_button

    @property
    def container_frame(self) -> tkinter.Frame:
        """
            Returns the 'container frame' frame widget associated with this field.

        The 'container frame' frame widget holds the selected values.

            Returns:
                tkinter.Frame: The 'container frame' frame widget.
        """

        # Return the 'container frame' frame widget
        return self._container_frame

    @property
    def label(self) -> tkinter.Label:
        """
        Returns the label widget associated with this field.

        The label displays the name or description of the field.

        Returns:
            tkinter.Label: The label widget.
        """

        # Return the tkinter.Label label widget
        return self._label

    @property
    def select_button(self) -> tkinter.Button:
        """
        Returns the 'select button' button widget associated with this field.

        Returns:
            tkinter.Button: The 'select button' button widget.
        """

        # Return the 'select button' button widget
        return self._clear_button

    def _on_clear_button_click(self) -> None:
        """ """

        # Get a list of  childr widgets of the container frame
        children: List[tkinter.Misc] = self._container_frame.winfo_children()

        # Check,  if any child widgets exist
        if len(children) == 0:
            # Return early
            return

        # Iterate over the list of child widgets
        for child in children:
            # Destroy the child
            child.destroy()

        # Clear the selection dictionary instance variable
        self.selection.clear()

    def _on_close_button_click(self) -> None:
        """
        Handles the 'close button' button click.

        This method will destroy the selection toplevel.

        Returns:
            None
        """

        # Destroy the toplevel widget
        self.toplevel.destroy()

    def _on_listbox_select(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """ """

        # Obtain the current selection from the listbox
        value_tuple: Tuple[int] = self.listbox.curselection()

        # Check,  if any values have been selected
        if len(value_tuple) == 0:
            # Return early
            return

        # Create a list from the string values obtained from the string variable instance variable
        string_values: List[str] = self.variable.get().split(",")

        # Check,  if any values have been selected
        if len(string_values) == 0:
            # Return early
            return

        # Initialize an empty list to store the selected values in
        value_list: List[str] = []

        # Iterate over the current selection of the listbox
        for index in value_tuple:
            # Append the value at the index to the empty values list
            value_list.append(string_values[index])

        for (
            row,
            value,
        ) in enumerate(
            iterable=value_list,
            start=len(
                self.container_frame.winfo_children(),
            ),
        ):
            # Check, if the current value already has been selected
            if value in self.selection.keys():
                # Skip the current iteration
                continue

            # Attempt to create a OptionSelectFieldItem instance
            select_option_field_item: Optional[OptionSelectFieldItem] = (
                OptionSelectFieldItemFactory.create_select_option_field_item(
                    dispatcher=self.dispatcher,
                    master=self.container,
                    namespace=self.internal_namespace,
                    value=value,
                )
            )

            # Check, if the creation of the OptionSelectFieldItem instance was successfull
            if not select_option_field_item:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create OptionSelectFieldItem instance in '{self.__class__.__name__}' class. This is likely due to something serious having gone wrong."
                )

                # Skip the current iteration
                continue

            # Place the OptionSelectFieldItem instace within the grid
            select_option_field_item.grid(
                column=0,
                padx=5,
                pady=5,
                row=row,
                sticky=NSEW,
            )

            # Add the select option field item to the selection dictionary instance variable
            self.selection[value] = select_option_field_item

        # Dispatch the MULTI_OPTION_SELECT_FIELD_CHANGED event
        self.dispatcher.dispatch(
            event=Events.MULTI_OPTION_SELECT_FIELD_CHANGED,
            label=self.display_name,
            namespace=self.namespace,
            value=self.selection.keys(),
        )

    def _on_request_option_select_field_item_destroy(
        self,
        value: str,
    ) -> None:
        """
        Handles the event for removing a selected item from the option select field.

        This method removes the corresponding OptionSelectFieldItem from the internal selection
        and destroys its widget.

        Args:
            value (str): The string label of the item to be removed.

        Returns:
            None
        """
        try:
            # Check, if the value is contained within the list of the selection dictionaries instance variable
            if value not in self.selection.keys():
                # Return early
                return

            # Obtain the OptionSelectFieldItem instance from the selection
            option_select_field_item: OptionSelectFieldItem = self.selection.pop(value)

            # Destroy the OptionSelectFieldItem instance
            option_select_field_item.destroy()

            # Dispatch the MULTI_OPTION_SELECT_FIELD_CHANGED event
            self.dispatcher.dispatch(
                event=Events.MULTI_OPTION_SELECT_FIELD_CHANGED,
                label=self.display_name,
                namespace=self.namespace,
                value=self.selection.keys(),
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run '_request_option_select_field_item_destroy' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def _on_select_button_click(self) -> None:
        """
        Opens the selection popup window for the option select field.

        This method creates a Toplevel window with a label, entry field, listbox, and close button,
        allowing the user to select one or more options.

        Returns:
            None
        """

        # Check, if the toplevel instance variable is not None
        if self.toplevel is not None:
            # Return early
            return

        # Create a toplevel widget and store it in the (optional) toplevel instance variable
        self.toplevel = tkinter.Toplevel(master=self)

        # Set the weight of the 0th column to 1
        # This means that the column will stretch when the window is resized
        self.toplevel.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Set the weight of the 0th row to 0
        # This means that the row will not stretch when the window is resized
        self.toplevel.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Set the weight of the 1st row to 1
        # This means that the row will not stretch when the window is resized
        self.toplevel.grid_rowconfigure(
            index=1,
            weight=0,
        )

        # Set the weight of the 2nd row to 1
        # This means that the row will stretch when the window is resized
        self.toplevel.grid_rowconfigure(
            index=2,
            weight=1,
        )

        # Set the weight of the 3rd row to 0
        # This means that the row will not stretch when the window is resized
        self.toplevel.grid_rowconfigure(
            index=3,
            weight=0,
        )

        # Configure the toplevel widget's title attribute
        self.toplevel.title("Please select a date")

        # Configure the toplevel widget's transient attribute
        self.toplevel.transient(self)

        # Route all events for this application to the toplevel widget
        self.toplevel.grab_set()

        # Bind the 'on_toplevel_destroy' to the toplevel widget via the 'WM_DESTROY' event
        self.toplevel.protocol(
            func=self._on_toplevel_destroy,
            sequence="WM_DESTROY",
        )

        # Create a label widget
        label: tkinter.Label = tkinter.Label(
            master=self.toplevel,
            text="Select on or more options",
        )

        # Place the label widget within the grid
        label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a frame widget
        frame: tkinter.Frame = tkinter.Frame(master=self.toplevel)

        # Place the frame widget within the grid
        frame.grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )

        # Create the 'search label' label widget
        search_label: tkinter.Label = tkinter.Label(
            master=frame,
            text="Search: ",
        )

        # Place the label widget within the grid
        search_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        def _on_entry_change(
            entry: tkinter.Entry,
            event: Optional[tkinter.Event] = None,
        ) -> None:
            """ """

            # Obtain the string value from the entry
            string_value: str = entry.get()

            # Check, if the value is an empty string
            if string_value == "":
                # Update the value of the tkinter.StringVar instance variable
                self.variable.set(value=dir(self.values))

                # Return early
                return

            # Initialize an empty list to store the values matching the string value obtained from the entry
            string_values: List[str] = []

            # Iterate over the list of values
            for string in self.values:
                # check, if the string value obtained from the entry is a part of the current string value from the values list
                if string_value.lower() not in string.lower():
                    continue

            # Append the matching string to the list of string values
            string_values.append(string)

            # Update the value of the tkinter.StringVar instance variable
            self.variable.set(value=dir(self.string_values))

        # Create a entry widget
        entry: tkinter.Entry = tkinter.Entry(master=frame)

        # Place the entry widget within the grid
        entry.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Bind the 'on_entry_change' method to the listbox widget via the '<KeyRelease>' event
        self.listbox.bind(
            func=lambda entry, event: _on_entry_change(
                entry=entry,
                event=event,
            ),
            sequence="<KeyRelease>",
        )

        # Update the value of the tkinter.StringVar instance variable
        self.variable(value=dir(self.values))

        # Create a listbox widget and store it in the (optional) listbox instance variable
        self.listbox = tkinter.Listbox(
            listvariable=self.variable,
            master=self.toplevel,
            selectmode="extended",
        )

        # Place the listbox widget within the grid
        self.listbox.grid(
            column=0,
            padx=5,
            pady=5,
            row=2,
            sticky=NSEW,
        )

        # Bind the 'on_listbox_select' method to the listbox widget via the '<<ListboxSelect>>' event
        self.listbox.bind(
            func=self._on_listbox_select,
            sequence="<<ListboxSelect>>",
        )

        # Create a button widget
        button: tkinter.Button = tkinter.Button(
            command=self._on_close_button_click,
            master=self.toplevel,
            text="Close",
        )

        # Place the label widget within the grid
        button.grid(
            column=0,
            padx=5,
            pady=5,
            row=3,
        )

    def _on_toplevel_destroy(self) -> None:
        """
        Cleans up internal references when the selection popup is closed.

        Returns:
            None
        """

        # Update the listbox instance variable to None
        self.listbox = None

        # Update the toplevel instance variable to None
        self.toplevel = None

    def add_value(
        self,
        values: Union[List[str], str],
    ) -> None:
        """
        Adds one or more values to the option select field.

        This method checks whether the given values are already part of the field's allowed values,
        and appends them if valid.

        Args:
            values (Union[List[str], str]): A single string or a list of strings to be added.

        Returns:
            None
        """

        # Check, if the passed values argument is not an instance of list
        if not isinstance(
            values,
            list,
        ):
            # Convert the passed values argument to a list
            values = [values]

        # Iterate over the list of values
        for value in values:
            # Check, if the current value is already in values the string list instance variable
            if value not in self.values:
                # Skip the current iteration
                continue

            # Append the value to the list of values
            self.values.append(value)

    @override
    def clear(
        self,
        dispatch: bool = False,
    ) -> None:
        """
        Clears the selected items from the option select field.

        This method destroys all currently selected OptionSelectFieldItem widgets,
        clears the internal selection dictionary, and optionally dispatches an event.

        Args:
            dispatch (bool): If True, an event is dispatched to signal that the field was cleared.

        Returns:
            None
        """

        # Get a list of  childr widgets of the container frame
        children: List[tkinter.Misc] = self._container_frame.winfo_children()

        # Check,  if any child widgets exist
        if len(children) == 0:
            # Return early
            return

        # Iterate over the list of child widgets
        for child in children:
            # Destroy the child
            child.destroy()

        # Clear the selection dictionary instance variable
        self.selection.clear()

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the MULTI_OPTION_SELECT_FIELD_CLEARED event
            self.dispatcher.dispatch(
                event=Events.MULTI_OPTION_SELECT_FIELD_CLEARED,
                label=self.display_name,
                namespace=self.namespace,
                value=[],
            )

    @override
    def configure_grid(self) -> None:
        """ """

        # Set the weight of the 0th column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_columnconfigure(
            index=0,
            weight=0,
        )

        # Set the weight of the 1st column to 1
        # This means that the column will stretch when the window is resized
        self.grid_columnconfigure(
            index=1,
            weight=1,
        )

        # Set the weight of the 2nd column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_columnconfigure(
            index=2,
            weight=0,
        )

        # Set the weight of the 3rd column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_columnconfigure(
            index=3,
            weight=0,
        )

        # Set the weight of the 0th row to 0
        # This means that the row will not stretch when the window is resized
        self.grid_rowconfigure(
            index=0,
            weight=0,
        )

    def configure_option(
        self,
        option: str,
        attribute: Literal["button", "label"],
        **kwargs,
    ) -> None:
        """
        Attempts to configure the passed attribute of the passed option.

        This method attempts to configure the option select field widget based on the passed 'option' and 'attribute' keywords
        using the provided keyword arguments.

        Args:
            option (str): The name (label) of the option of which the attribute is to be configured.
            attribute (Literal["checkbutton", "label"]): The attribute of the option that is to be configured.
            **kwargs: The keyword arguments to be passed to the configure method
                of the corresponding option's attribute widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                label widget.
        """
        try:
            # Check, if the passed option is in the keys of selection dictionary instance variable
            if option not in self.selection.keys():
                # Log a warning message
                self.logger.warning(
                    message=f"Option with value '{option}' not found in 'selection' dictionary. This is likely due to a typo."
                )

                # Return early
                return

            # Store the looked up option in a variable
            option: OptionSelectFieldItem = self.selection[option]

            # Generate the corresponding method name
            method: str = f"configure_{attribute}"

            # Check if the option has the 'configure_{attribute}' method
            if not hasattr(
                option,
                method,
            ):
                # Log a warning message
                self.logger.warning(
                    message=f"Option with value '{option}' does not have any 'configure_{attribute}' attribute. This is likely due the method not being implemented."
                )

                # Return early
                return

            # Call the corresponding option's 'configure_{attribute}' and pass **kwargs to it
            getattr(
                option,
                method,
            )(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_option' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @override
    def create_widgets(
        self,
        label: str,
        **kwargs,
    ) -> None:
        """ """

        # Create a label widget
        self._label: tkinter.Label = tkinter.Label(
            master=self, text=label, **kwargs.get("label", {})
        )

        # Place the label widget within the grid
        self._label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a 'container frame' frame widget
        self._container_frame: tkinter.Frame = tkinter.Frame(
            master=self, **kwargs.get("container_frame", {})
        )

        # Place the 'container frame' frame widget within the grid
        self._container_frame.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a 'clear button' button widget
        self._clear_button: tkinter.Button = tkinter.Button(
            command=self._on_clear_button_click,
            master=self,
            text="X",
            **kwargs.get(
                "clear_button",
                {},
            ),
        )

        # Place the 'clear button' button widget within the grid
        self._clear_button.grid(
            column=2,
            padx=5,
            pady=5,
            row=0,
        )

        # Create a 'select button' button widget
        self._select_button: tkinter.Button = tkinter.Button(
            command=self._on_select_button_click,
            master=self,
            text="Select",
            **kwargs.get(
                "select_button",
                {},
            ),
        )

        # Place the 'select button' button widget within the grid
        self._select_button.grid(
            column=3,
            padx=5,
            pady=5,
            row=0,
        )

    @override
    def get(
        self,
        dispatch: bool = False,
    ) -> Tuple[str, List[str]]:
        """ """

        # Obtain the label and values of this field
        (
            label,
            value,
        ) = (
            self.display_name,
            list(self.selection.keys()),
        )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the MULTI_OPTION_SELECT_FIELD_GET event
            self.dispatcher.dispatch(
                event=Events.MULTI_OPTION_SELECT_FIELD_GET,
                label=self.display_name,
                namespace=self.namespace,
                value=value,
            )

        # Return the label and the values of this field
        return (
            label,
            value,
        )

    @override
    def set(
        self,
        values: Union[List[str], str],
        dispatch: bool = False,
    ) -> None:
        """ """

        # Check, if the passed values argument is not an instance of list
        if not isinstance(
            values,
            list,
        ):
            # Convert the passed values argument to a list
            values = [values]

        # Iterate over the list of values
        for value in values:
            # Check, if the current value is already in values the string list instance variable
            if value not in self.values:
                # Skip the current iteration
                continue

            # Append the value to the list of values
            self.values.append(value)

        for (
            row,
            value,
        ) in enumerate(
            iterable=self.values, start=len(self.container_frame.winfo_children())
        ):
            # Check, if the current value already has been selected
            if value in self.selection.keys():
                # Skip the current iteration
                continue

            # Attempt to create a OptionSelectFieldItem instance
            select_option_field_item: Optional[OptionSelectFieldItem] = (
                OptionSelectFieldItemFactory.create_select_option_field_item(
                    dispatcher=self.dispatcher,
                    master=self.container,
                    namespace=self.internal_namespace,
                    value=value,
                )
            )

            # Check, if the creation of the OptionSelectFieldItem instance was successfull
            if not select_option_field_item:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create OptionSelectFieldItem instance in '{self.__class__.__name__}' class. This is likely due to something serious having gone wrong."
                )

                # Skip the current iteration
                continue

            # Place the OptionSelectFieldItem instace within the grid
            select_option_field_item.grid(
                column=0,
                padx=5,
                pady=5,
                row=row,
                sticky=NSEW,
            )

            # Add the select option field item to the selection dictionary instance variable
            self.selection[value] = select_option_field_item

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the MULTI_OPTION_SELECT_FIELD_SET event
            self.dispatcher.dispatch(
                event=Events.MULTI_OPTION_SELECT_FIELD_SET,
                label=self.display_name,
                namespace=self.namespace,
                value=value,
            )


class RadiobuttonSelectField(BaseField):
    """
    A grouped boolean selection field using multiple radiobuttons.

    RadiobuttonSelectField represents a set of binary input fields, each rendered as a RadiobuttonField.
    It allows users to select one option from a list of radiobuttons, depending on the defined.

    The field layout consists of:
        [ Label ]
        [ Label 1 | Radiobutton 1 ]
        [ Label 2 | Radiobutton 2 ]
        ...
        [ Label n | Radiobutton n ]

    Attributes:
        fields (Dict[str, RadiobuttonField]): A dictionary mapping option labels to their respective radiobutton fields.
        selection_mode (Literal["multi", "single"]): Defines whether multiple options can be selected simultaneously.

    Inherits from:
        BaseField
    """

    def __init__(
        self,
        label: str,
        labels: List[str],
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, Dict[str, bool]], None]] = None,
    ) -> None:
        """
        Initializes a new instance of the RadiobuttonSelectField class.

        This constructor sets up a group of radiobutton widgets corresponding to the given labels.
        It manages individual RadiobuttonField instances in a centralized layout.

        Args:
            label (str): The label text describing the group of radiobuttons.
            labels (List[str]): A list of strings representing the options to display as radiobuttons.
            master (tkinter.Misc): The parent container in which this widget is placed.
            namespace (str, optional): The namespace identifier for event dispatching. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[str, Dict[str, bool]], None]], optional): Callback function invoked on any change in the selection.

        Returns:
            None
        """

        # Initialize the fields dictionary
        self.fields: Dict[str, Optional[RadiobuttonField]] = {
            label: None for label in labels
        }

        # Call the parent class constructor with the passed arguments
        super().__init__(
            label=label,
            master=master,
            namespace=namespace,
            on_change_callback=on_change_callback,
        )

    @property
    def label(self) -> tkinter.Label:
        """
        Returns the label widget associated with this field.

        The label displays the name or description of the field.

        Returns:
            tkinter.Label: The label widget.
        """

        # Return the tkinter.Label label widget
        return self._label

    def _enforce_selection(
        self,
        label: str,
        value: bool,
    ) -> None:
        """
        Enforces the configured selection across radiobuttons.

        tthis method ensures that only the field corresponding to the given label remains active (True),
        while all others are reset to False.

        Args:
            label (str): The label of the field that was selected.
            value (bool): The boolean value indicating the new selection state.

        Returns:
            None
        """

        # Iterate over the keys and values of the fields dictionary instance variable
        for (
            key,
            value,
        ) in self.fields.items():
            # Radio if the key and the passed label are identical
            if key == label:
                # Update the value of the corresponding radiobutton field with the passed value
                value.set(
                    dispatch=False,
                    value=value,
                )
            else:
                # Update the value of the non-corresponding radiobutton field with the opposite of the passed value
                value.set(
                    dispatch=False,
                    value=not value,
                )

    def _on_field_change(
        self,
        label: str,
        value: bool,
    ) -> None:
        """
        Internal handler for state changes in individual radiobuttons.

        This method is triggered whenever a RadiobuttonField changes its value. It enforces
        the selection (e.g. unselecting other fields), dispatches
        a change event, and invokes the on_change_callback if provided.

        Args:
            label (str): The label of the field that triggered the change.
            value (bool): The new boolean value of the changed field.

        Returns:
            None
        """

        # Enforce the selection
        self._enforce_selection(label=label, value=value)

        # Dispatch the RADIOBUTTON_SELECT_FIELD_CHANGED event
        self.dispatcher.dispatch(
            event=Events.RADIOBUTTON_SELECT_FIELD_CHANGED,
            label=self.display_name,
            namespace=self.namespace,
            value=self.get(),
        )

        # Check, if the 'on_change_callback' function exists
        if self.on_change_callback:
            # Call the 'on_change_callback' function and pass the display name as well as the current selection to it
            self.on_change_callback(
                self.display_name,
                self.get(dispatch=False),
            )

    @override
    def clear(
        self,
        dispatch: bool = False,
    ) -> None:
        """
        Clears all selected radiobuttons in the field.

        Resets all radiobuttons to an unselected state. Optionally dispatches a
        RADIOBUTTON_SELECT_FIELD_CLEARED event with the current selection state.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            None
        """

        # Iterate over the keys and values of the fields dictionary instance variable
        for (
            key,
            value,
        ) in self.fields.items():
            # Update the value of the radiobutton field to False
            value.set(
                dispatch=False,
                value=False,
            )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the RADIOBUTTON_SELECT_FIELD_CLEARED event
            self.dispatcher.dispatch(
                event=Events.RADIOBUTTON_SELECT_FIELD_CLEARED,
                label=self.display_name,
                namespace=self.namespace,
                value=self.get(dispatch=False),
            )

    def configure_field(
        self,
        field: str,
        attribute: Literal["radiobutton", "label"],
        **kwargs,
    ) -> None:
        """
        Attempts to configure the passed attribute of the passed field.

        This method attempts to configure the radiobutton field widget based on the passed 'field' and 'attribute' keywords
        using the provided keyword arguments.

        Args:
            field (str): The name (label) of the field of which the attribute is to be configured.
            attribute (Literal["radiobutton", "label"]): The attribute of the field that is to be configured.
            **kwargs: The keyword arguments to be passed to the configure method
                of the corresponding field's attribute widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                label widget.
        """
        try:
            # Check, if the passed field is in the keys of fields dictionary instance variable
            if field not in self.fields.keys():
                # Log a warning message
                self.logger.warning(
                    message=f"Field with label '{field}' not found in 'fields' dictionary. This is likely due to a typo."
                )

                # Return early
                return

            # Store the looked up field in a variable
            field: RadiobuttonField = self.fields[field]

            # Generate the corresponding method name
            method: str = f"configure_{attribute}"

            # Radio if the field has the 'configure_{attribute}' method
            if not hasattr(
                field,
                method,
            ):
                # Log a warning message
                self.logger.warning(
                    message=f"Field with label '{field}' does not have any 'configure_{attribute}' attribute. This is likely due the method not being implemented."
                )

                # Return early
                return

            # Call the corresponding field's 'configure_{attribute}' and pass **kwargs to it
            getattr(
                field,
                method,
            )(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_label' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @override
    def configure_grid(self) -> None:
        """
        Configures the grid layout for the RadiobuttonSelectField widget.

        Sets the column and row weights to ensure the layout behaves responsively
        when the parent window is resized. This method is called during initialization.

        Returns:
            None
        """

        # Set the weight of the 0th column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_columnconfigure(
            index=0,
            weight=0,
        )

        # Set the weight of the 0th row to 0
        # This means that the row will not stretch when the window is resized
        self.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Iterate over the values in the fields dictionary
        for index in enumerate(
            iterable=[value for value in self.fields.values() if value is not None],
            start=1,
        ):
            # Set the weight of the row at the index to 0
            # This means that the row will not stretch when the window is resized
            self.grid_rowconfigure(
                index=index,
                weight=0,
            )

    def configure_label(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the label widget in this field.

        This method configures the label widget in this field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the label widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                label widget.
        """
        try:
            # Attempt to configure the label widget
            self._label.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_label' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @override
    def create_widgets(
        self,
        label: str,
        **kwargs,
    ) -> None:
        """
        Creates and configures all widgets for the RadiobuttonSelectField.

        This method creates the label and all radiobuttons based on the provided options.
        Each radiobutton is placed in its own row within the widget's grid.

        Args:
            label (str): The display label for the field.
            options (List[str]): A list of option strings to create individual radiobuttons for.
            **kwargs: Additional keyword arguments for field customization.

        Returns:
            None
        """

        # Create a label widget
        self._label: tkinter.Label = tkinter.Label(
            master=self, text=label, **kwargs.get("label", {})
        )

        # Place the label widget within the grid
        self._label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Iterate over the labels in the keys of the fields dictionary instance variable
        for (
            row,
            label,
        ) in enumerate(
            iterable=self.fields.keys(),
            start=1,
        ):
            # Create a radiobutton field widget
            radiobutton_field: RadiobuttonField = RadiobuttonField(
                label=label,
                master=self,
                namespace=self.namespace,
                on_change_callback=self._on_field_change,
            )

            # Place the radiobutton field widget within the grid
            radiobutton_field.grid(column=0, padx=5, pady=5, row=row)

            # Add the radiobutton field widget to the fields dictionary instance variable
            self.fields[label] = radiobutton_field

        # Configure the grid
        self.configure_grid()

    @override
    def get(
        self,
        label: str,
        dispatch: bool = False,
    ) -> Tuple[str, Dict[str, bool]]:
        """
        Retrieves the current selection from the field.

        Returns the selected option(s) based on the current state of the radiobuttons
        and the selection mode. If dispatch is True, an event will be emitted.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            Tuple[str, Union[str, List[str]]]: A tuple containing the field label and the current selection.
        """

        # Check, if the passed label is present within the keys of the 'fields' dictionary instance variable
        if label not in self.fields.keys():
            # Log a warning message
            self.logger.warning(
                message=f"Field with label '{label}' not found in 'fields' dictionary. This is likely due to a typo."
            )

            # Return early
            return

        # Obtain the label of the field as well as the labels and values of the fields
        (
            label,
            value,
        ) = (
            self.display_name,
            {
                key: value.get(dispatch=False)
                for (
                    key,
                    value,
                ) in self.fields.items()
            },
        )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the RADIOBUTTON_SELECT_FIELD_GET event
            self.dispatcher.dispatch(
                event=Events.RADIOBUTTON_SELECT_FIELD_GET,
                label=self.display_name,
                namespace=self.namespace,
                value=value,
            )

        # Return the label of this field and the values of the radiobutton fields
        return (
            label,
            value,
        )

    @override
    def set(
        self,
        label: str,
        value: bool,
        dispatch: bool = False,
    ) -> None:
        """
        Sets the selection state of the radiobuttons based on the given value(s).

        Updates each radiobutton to match the provided selection(s). If dispatch is True,
        a RADIOBUTTON_SELECT_FIELD_SET event will be emitted.

        Args:
            value (Union[str, List[str]]): A single option or list of options to select.
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.
        """

        # Check, if the passed label is present within the keys of the 'fields' dictionary instance variable
        if label not in self.fields.keys():
            # Log a warning message
            self.logger.warning(
                message=f"Field with label '{label}' not found in 'fields' dictionary. This is likely due to a typo."
            )

            # Return early
            return

        # Set the value of the corresponding radiobutton field
        self.fields[label].set(value=value)

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the RADIOBUTTON_SELECT_FIELD_SET event
            self.dispatcher.dispatch(
                event=Events.RADIOBUTTON_SELECT_FIELD_SET,
                label=self.display_name,
                namespace=self.namespace,
                value=self.get(dispatch=False),
            )


class SingleOptionSelectField(BaseField):
    """ """

    def __init__(
        self,
        label: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, str], None]] = None,
        values: Optional[List[str]] = None,
    ) -> None:
        """ """

        # Generate a uniqe internal namespace
        self.internal_namespace: str = (
            f"SINGLE_OPTION_SELECT_FIELD({str(uuid.uuid4())})"
        )

        # Initialize the (optional) listbox instance variable as None
        self.listbox: Optional[tkinter.Listbox] = None

        # Iniitialize the selection dictionary instance variable as an empty dictionary
        self.selection: Dict[str, Optional[OptionSelectFieldItem]] = {}

        # Initialize the (optional) toplevel instance variable as None
        self.toplevel: Optional[tkinter.Toplevel] = None

        # Initialize the tkinter.StringVar instance variable
        self.variable: tkinter.StringVar = tkinter.StringVar()

        # Store the passed values list of strings in an instance variable or initialize it as an empty list
        self.values: List[str] = values if values is not None else []

        # Call the parent class constructor with the passed arguments
        super().__init__(
            label=label,
            master=master,
            namespace=namespace,
            on_change_callback=on_change_callback,
        )

    @property
    def clear_button(self) -> tkinter.Button:
        """
        Returns the 'clear button' button widget associated with this field.

        Returns:
            tkinter.Button: The 'clear button' button widget.
        """

        # Return the 'clear button' button widget
        return self._clear_button

    @property
    def container_frame(self) -> tkinter.Frame:
        """
            Returns the 'container frame' frame widget associated with this field.

        The 'container frame' frame widget holds the selected values.

            Returns:
                tkinter.Frame: The 'container frame' frame widget.
        """

        # Return the 'container frame' frame widget
        return self._container_frame

    @property
    def label(self) -> tkinter.Label:
        """
        Returns the label widget associated with this field.

        The label displays the name or description of the field.

        Returns:
            tkinter.Label: The label widget.
        """

        # Return the tkinter.Label label widget
        return self._label

    @property
    def select_button(self) -> tkinter.Button:
        """
        Returns the 'select button' button widget associated with this field.

        Returns:
            tkinter.Button: The 'select button' button widget.
        """

        # Return the 'select button' button widget
        return self._clear_button

    def _on_clear_button_click(self) -> None:
        """ """

        # Get a list of  childr widgets of the container frame
        children: List[tkinter.Misc] = self._container_frame.winfo_children()

        # Check,  if any child widgets exist
        if len(children) == 0:
            # Return early
            return

        # Iterate over the list of child widgets
        for child in children:
            # Destroy the child
            child.destroy()

        # Clear the selection dictionary instance variable
        self.selection.clear()

    def _on_close_button_click(self) -> None:
        """
        Handles the 'close button' button click.

        This method will destroy the selection toplevel.

        Returns:
            None
        """

        # Destroy the toplevel widget
        self.toplevel.destroy()

    def _on_listbox_select(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """ """

        # Obtain the current selection from the listbox
        value_tuple: Tuple[int] = self.listbox.curselection()

        # Check,  if any values have been selected
        if len(value_tuple) == 0:
            # Return early
            return

        # Create a list from the string values obtained from the string variable instance variable
        string_values: List[str] = self.variable.get().split(",")

        # Check,  if any values have been selected
        if len(string_values) == 0:
            # Return early
            return

        # Initialize an empty list to store the selected values in
        value_list: List[str] = []

        # Iterate over the current selection of the listbox
        for index in value_tuple:
            # Append the value at the index to the empty values list
            value_list.append(string_values[index])

        # Check, if there is any previous selection
        if len(self.selection) > 0:
            # Iterate over the keys of the selection dictionary instance variable
            for key in self.selection.keys():
                # Obtain the OptionSelectFieldItem from the instance
                select_option_field_item: OptionSelectFieldItem = self.selection.pop(
                    key
                )

                # Destroy the OptionSelectFieldItem instance
                select_option_field_item.destroy()

        for (
            row,
            value,
        ) in enumerate(
            iterable=value_list, start=len(self.container_frame.winfo_children())
        ):
            # Check, if the current value already has been selected
            if value in self.selection.keys():
                # Skip the current iteration
                continue

            # Attempt to create a OptionSelectFieldItem instance
            select_option_field_item: Optional[OptionSelectFieldItem] = (
                OptionSelectFieldItemFactory.create_select_option_field_item(
                    dispatcher=self.dispatcher,
                    master=self.container,
                    namespace=self.internal_namespace,
                    value=value,
                )
            )

            # Check, if the creation of the OptionSelectFieldItem instance was successfull
            if not select_option_field_item:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create OptionSelectFieldItem instance in '{self.__class__.__name__}' class. This is likely due to something serious having gone wrong."
                )

                # Skip the current iteration
                continue

            # Place the OptionSelectFieldItem instace within the grid
            select_option_field_item.grid(
                column=0,
                padx=5,
                pady=5,
                row=row,
                sticky=NSEW,
            )

            # Add the select option field item to the selection dictionary instance variable
            self.selection[value] = select_option_field_item

        # Dispatch the SINGLE_OPTION_SELECT_FIELD_CHANGED event
        self.dispatcher.dispatch(
            event=Events.SINGLE_OPTION_SELECT_FIELD_CHANGED,
            label=self.display_name,
            namespace=self.namespace,
            value=self.selection.keys(),
        )

    def _on_request_option_select_field_item_destroy(
        self,
        id: int,
        uuid: str,
        value: str,
    ) -> None:
        """ """
        try:
            # Check, if the value is contained within the list of the selection dictionaries instance variable
            if value not in self.selection.keys():
                # Return early
                return

            # Obtain the OptionSelectFieldItem instance from the selection
            option_select_field_item: OptionSelectFieldItem = self.selection.pop(value)

            # Destroy the OptionSelectFieldItem instance
            option_select_field_item.destroy()

            # Dispatch the SINGLE_OPTION_SELECT_FIELD_CHANGED event
            self.dispatcher.dispatch(
                event=Events.SINGLE_OPTION_SELECT_FIELD_CHANGED,
                label=self.display_name,
                namespace=self.namespace,
                value=self.selection.keys(),
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run '_request_option_select_field_item_destroy' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def _on_select_button_click(self) -> None:
        """ """

        # Check, if the toplevel instance variable is not None
        if self.toplevel is not None:
            # Return early
            return

        # Create a toplevel widget and store it in the (optional) toplevel instance variable
        self.toplevel = tkinter.Toplevel(master=self)

        # Set the weight of the 0th column to 1
        # This means that the column will stretch when the window is resized
        self.toplevel.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Set the weight of the 0th row to 0
        # This means that the row will not stretch when the window is resized
        self.toplevel.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Set the weight of the 1st row to 1
        # This means that the row will not stretch when the window is resized
        self.toplevel.grid_rowconfigure(
            index=1,
            weight=0,
        )

        # Set the weight of the 2nd row to 1
        # This means that the row will stretch when the window is resized
        self.toplevel.grid_rowconfigure(
            index=2,
            weight=1,
        )

        # Set the weight of the 3rd row to 0
        # This means that the row will not stretch when the window is resized
        self.toplevel.grid_rowconfigure(
            index=3,
            weight=0,
        )

        # Configure the toplevel widget's title attribute
        self.toplevel.title("Please select a date")

        # Configure the toplevel widget's transient attribute
        self.toplevel.transient(self)

        # Route all events for this application to the toplevel widget
        self.toplevel.grab_set()

        # Bind the 'on_toplevel_destroy' to the toplevel widget via the 'WM_DESTROY' event
        self.toplevel.protocol(
            func=self._on_toplevel_destroy,
            sequence="WM_DESTROY",
        )

        # Create a label widget
        label: tkinter.Label = tkinter.Label(
            master=self.toplevel,
            text="Select on or more options",
        )

        # Place the label widget within the grid
        label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a frame widget
        frame: tkinter.Frame = tkinter.Frame(master=self.toplevel)

        # Place the frame widget within the grid
        frame.grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )

        # Create the 'search label' label widget
        search_label: tkinter.Label = tkinter.Label(
            master=frame,
            text="Search: ",
        )

        # Place the label widget within the grid
        search_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        def _on_entry_change(
            entry: tkinter.Entry,
            event: Optional[tkinter.Event] = None,
        ) -> None:
            """ """

            # Obtain the string value from the entry
            string_value: str = entry.get()

            # Check, if the value is an empty string
            if string_value == "":

                # Update the value of the tkinter.StringVar instance variable
                self.variable.set(value=dir(self.values))

                # Return early
                return

            # Initialize an empty list to store the values matching the string value obtained from the entry
            string_values: List[str] = []

            # Iterate over the list of values
            for string in self.values:
                # check, if the string value obtained from the entry is a part of the current string value from the values list
                if string_value.lower() not in string.lower():
                    continue

            # Append the matching string to the list of string values
            string_values.append(string)

            # Update the value of the tkinter.StringVar instance variable
            self.variable.set(value=dir(self.string_values))

        # Create a entry widget
        entry: tkinter.Entry = tkinter.Entry(master=frame)

        # Place the entry widget within the grid
        entry.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Bind the 'on_entry_change' method to the listbox widget via the '<KeyRelease>' event
        self.listbox.bind(
            func=lambda entry, event: _on_entry_change(
                entry=entry,
                event=event,
            ),
            sequence="<KeyRelease>",
        )

        # Update the value of the tkinter.StringVar instance variable
        self.variable(value=dir(self.values))

        # Create a listbox widget and store it in the (optional) listbox instance variable
        self.listbox = tkinter.Listbox(
            listvariable=self.variable,
            master=self.toplevel,
            selectmode="extended",
        )

        # Place the listbox widget within the grid
        self.listbox.grid(
            column=0,
            padx=5,
            pady=5,
            row=2,
            sticky=NSEW,
        )

        # Bind the 'on_listbox_select' method to the listbox widget via the '<<ListboxSelect>>' event
        self.listbox.bind(
            func=self._on_listbox_select,
            sequence="<<ListboxSelect>>",
        )

        # Create a button widget
        button: tkinter.Button = tkinter.Button(
            command=self._on_close_button_click,
            master=self.toplevel,
            text="Close",
        )

        # Place the label widget within the grid
        button.grid(
            column=0,
            padx=5,
            pady=5,
            row=3,
        )

    def _on_toplevel_destroy(self) -> None:
        """
        Cleans up internal references when the selection popup is closed.

        Returns:
            None
        """

        # Update the listbox instance variable to None
        self.listbox = None

        # Update the toplevel instance variable to None
        self.toplevel = None

    def add_value(
        self,
        values: Union[List[str], str],
    ) -> None:
        """ """

        # Check, if the passed values argument is not an instance of list
        if not isinstance(
            values,
            list,
        ):
            # Convert the passed values argument to a list
            values = [values]

        # Iterate over the list of values
        for value in values:
            # Check, if the current value is already in values the string list instance variable
            if value not in self.values:
                # Skip the current iteration
                continue

            # Append the value to the list of values
            self.values.append(value)

    @override
    def clear(
        self,
        dispatch: bool = False,
    ) -> None:
        """ """

        # Get a list of  childr widgets of the container frame
        children: List[tkinter.Misc] = self._container_frame.winfo_children()

        # Check,  if any child widgets exist
        if len(children) == 0:
            # Return early
            return

        # Iterate over the list of child widgets
        for child in children:
            # Destroy the child
            child.destroy()

        # Clear the selection dictionary instance variable
        self.selection.clear()

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the SINGLE_OPTION_SELECT_FIELD_CLEARED event
            self.dispatcher.dispatch(
                event=Events.SINGLE_OPTION_SELECT_FIELD_CLEARED,
                label=self.display_name,
                namespace=self.namespace,
                value=[],
            )

    @override
    def configure_grid(self) -> None:
        """ """

        # Set the weight of the 0th column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_columnconfigure(
            index=0,
            weight=0,
        )

        # Set the weight of the 1st column to 1
        # This means that the column will stretch when the window is resized
        self.grid_columnconfigure(
            index=1,
            weight=1,
        )

        # Set the weight of the 2nd column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_columnconfigure(
            index=2,
            weight=0,
        )

        # Set the weight of the 3rd column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_columnconfigure(
            index=3,
            weight=0,
        )

        # Set the weight of the 0th row to 0
        # This means that the row will not stretch when the window is resized
        self.grid_rowconfigure(
            index=0,
            weight=0,
        )

    def configure_option(
        self,
        option: str,
        attribute: Literal["button", "label"],
        **kwargs,
    ) -> None:
        """
        Attempts to configure the passed attribute of the passed option.

        This method attempts to configure the option select field widget based on the passed 'option' and 'attribute' keywords
        using the provided keyword arguments.

        Args:
            option (str): The name (label) of the option of which the attribute is to be configured.
            attribute (Literal["checkbutton", "label"]): The attribute of the option that is to be configured.
            **kwargs: The keyword arguments to be passed to the configure method
                of the corresponding option's attribute widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                label widget.
        """
        try:
            # Check, if the passed option is in the keys of selection dictionary instance variable
            if option not in self.selection.keys():
                # Log a warning message
                self.logger.warning(
                    message=f"Option with value '{option}' not found in 'selection' dictionary. This is likely due to a typo."
                )

                # Return early
                return

            # Store the looked up option in a variable
            option: OptionSelectFieldItem = self.selection[option]

            # Generate the corresponding method name
            method: str = f"configure_{attribute}"

            # Check if the option has the 'configure_{attribute}' method
            if not hasattr(
                option,
                method,
            ):
                # Log a warning message
                self.logger.warning(
                    message=f"Option with value '{option}' does not have any 'configure_{attribute}' attribute. This is likely due the method not being implemented."
                )

                # Return early
                return

            # Call the corresponding option's 'configure_{attribute}' and pass **kwargs to it
            getattr(
                option,
                method,
            )(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_option' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_option_select_field_items(self) -> None:
        try:
            pass
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_option_select_field_items' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @override
    def create_widgets(
        self,
        label: str,
        **kwargs,
    ) -> None:
        """ """

        # Create a label widget
        self._label: tkinter.Label = tkinter.Label(
            master=self, text=label, **kwargs.get("label", {})
        )

        # Place the label widget within the grid
        self._label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a 'container frame' frame widget
        self._container_frame: tkinter.Frame = tkinter.Frame(
            master=self, **kwargs.get("container_frame", {})
        )

        # Place the 'container frame' frame widget within the grid
        self._container_frame.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a 'clear button' button widget
        self._clear_button: tkinter.Button = tkinter.Button(
            command=self._on_clear_button_click,
            master=self,
            text="X",
            **kwargs.get(
                "clear_button",
                {},
            ),
        )

        # Place the 'clear button' button widget within the grid
        self._clear_button.grid(
            column=2,
            padx=5,
            pady=5,
            row=0,
        )

        # Create a 'select button' button widget
        self._select_button: tkinter.Button = tkinter.Button(
            command=self._on_select_button_click,
            master=self,
            text="Select",
            **kwargs.get(
                "select_button",
                {},
            ),
        )

        # Place the 'select button' button widget within the grid
        self._select_button.grid(
            column=3,
            padx=5,
            pady=5,
            row=0,
        )

    @override
    def get(
        self,
        dispatch: bool = False,
    ) -> Tuple[str, List[str]]:
        """ """

        # Obtain the label and values of this field
        (
            label,
            value,
        ) = (
            self.display_name,
            list(self.selection.keys()),
        )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the SINGLE_OPTION_SELECT_FIELD_GET event
            self.dispatcher.dispatch(
                event=Events.SINGLE_OPTION_SELECT_FIELD_GET,
                label=self.display_name,
                namespace=self.namespace,
                value=value,
            )

        # Return the label and the values of this field
        return (
            label,
            value,
        )

    @override
    def set(
        self,
        values: str,
        dispatch: bool = False,
    ) -> None:
        """ """

        # Check, if the passed values argument is not an instance of list
        if not isinstance(
            values,
            list,
        ):
            # Convert the passed values argument to a list
            values = [values]

        # Iterate over the list of values
        for value in values:
            # Check, if the current value is already in values the string list instance variable
            if value not in self.values:
                # Skip the current iteration
                continue

            # Append the value to the list of values
            self.values.append(value)

        # Check, if there is any previous selection
        if len(self.selection) > 0:
            # Iterate over the keys of the selection dictionary instance variable
            for key in self.selection.keys():
                # Obtain the OptionSelectFieldItem from the instance
                select_option_field_item: OptionSelectFieldItem = self.selection.pop(
                    key
                )

                # Destroy the OptionSelectFieldItem instance
                select_option_field_item.destroy()

        for (
            row,
            value,
        ) in enumerate(
            iterable=[values], start=len(self.container_frame.winfo_children())
        ):
            # Check, if the current value already has been selected
            if value in self.selection.keys():
                # Skip the current iteration
                continue

            # Attempt to create a OptionSelectFieldItem instance
            select_option_field_item: Optional[OptionSelectFieldItem] = (
                OptionSelectFieldItemFactory.create_select_option_field_item(
                    dispatcher=self.dispatcher,
                    master=self._container,
                    namespace=self.internal_namespace,
                    value=value,
                )
            )

            # Check, if the creation of the OptionSelectFieldItem instance was successfull
            if not select_option_field_item:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to create OptionSelectFieldItem instance in '{self.__class__.__name__}' class. This is likely due to something serious having gone wrong."
                )

                # Skip the current iteration
                continue

            # Place the OptionSelectFieldItem instace within the grid
            select_option_field_item.grid(
                column=0,
                padx=5,
                pady=5,
                row=row,
                sticky=NSEW,
            )

            # Add the select option field item to the selection dictionary instance variable
            self.selection[value] = select_option_field_item

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the SINGLE_OPTION_SELECT_FIELD_SET event
            self.dispatcher.dispatch(
                event=Events.SINGLE_OPTION_SELECT_FIELD_SET,
                label=self.display_name,
                namespace=self.namespace,
                value=value,
            )
