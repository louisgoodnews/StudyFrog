"""
Author: lodego
Date: 2025-04-08
"""

import tkinter
import traceback

from tkinter.constants import *
from typing import *

from utils.base_field import BaseField
from utils.constants import Constants
from utils.events import Events


__all__: Final[List[str]] = [
    "CheckbuttonField",
    "RadiobuttonField",
    "ToggleButtonField",
]


class CheckbuttonField(BaseField):
    """
    A boolean field using a checkbutton widget.

    CheckbuttonField represents a binary user input field consisting of a label and a tkinter.Checkbutton.
    It stores its state in a tkinter.BooleanVar and provides event dispatching and callback support on change.

    The field layout consists of:
        [ Label | Checkbutton ]

    Attributes:
        variable (tkinter.BooleanVar): Holds the current boolean state of the checkbutton.
        label (tkinter.Label): The label widget describing the checkbutton.
        checkbutton (tkinter.Checkbutton): The interactive checkbox widget.

    Inherits from:
        BaseField
    """

    def __init__(
        self,
        display_name: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, bool], None]] = None,
        value: bool = False,
    ) -> None:
        """
        Initializes a new instance of the CheckbuttonField class.

        This constructor sets up the label and checkbutton widget, binds the necessary variable,
        and prepares the field for interaction and layout configuration.

        Args:
            display_name (str): The string to display for the field.
            master (tkinter.Misc): The parent container in which this widget is placed.
            namespace (str, optional): The namespace identifier for event dispatching. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[str, bool], None]], optional): Callback function called when the boolean value changes.
            value (bool, optional): The initial boolean state of the checkbutton. Defaults to False.

        Returns:
            None
        """

        # Call the parent class constructor with the passed arguments
        super().__init__(
            display_name=display_name,
            master=master,
            namespace=namespace,
            on_change_callback=on_change_callback,
        )

    @property
    def checkbutton(self) -> tkinter.Checkbutton:
        """
        Returns the checkbutton widget associated with this field.

        The checkbutton displays the name or description of the field.

        Returns:
            tkinter.Checkbutton: The checkbutton widget.
        """

        # Return the tkinter.Checkbutton checkbutton widget
        return self._checkbutton

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

    def _on_checkbutton_change(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        Handles changes in the checkbutton state.

        This method is triggered when the user toggles the checkbutton. It dispatches an event
        with the new boolean value and triggers an optional callback function.

        Args:
            event (Optional[tkinter.Event], optional): The event object. Defaults to None.

        Returns:
            None
        """

        # Dispatch the CHECKBUTTON_FIELD_CHANGED event
        self.dispatcher.dispatch(
            event=Events.CHECKBUTTON_FIELD_CHANGED,
            label=self.display_name,
            namespace=self.namespace,
            value=self.variable.get(),
        )

        # Update the text of the checkbutton widget
        self._checkbutton.configure(text=f"{self.variable.get()}")

        # Check, if the 'on_change_callback' function exists
        if self.on_change_callback:
            # Call the 'on_change_callback' function and pass the display name as well as the variable's value to it
            self.on_change_callback(
                self.display_name,
                self.variable.get(),
            )

    @override
    def clear(
        self,
        dispatch: bool = False,
    ) -> None:
        """
        Clears the state of the checkbutton, setting it to False.

        If `dispatch` is True, it also dispatches a clear event to notify any listeners.

        Args:
            dispatch (bool, optional): Whether to dispatch a clear event. Defaults to False.

        Returns:
            None
        """

        # Update the variable's value to False
        self.variable.set(value=False)

        # Update the text of the checkbutton widget
        self._checkbutton.configure(text=f"{self.variable.get()}")

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the CHECKBUTTON_FIELD_CLEARED event
            self.dispatcher.dispatch(
                event=Events.CHECKBUTTON_FIELD_CLEARED,
                label=self.display_name,
                namespace=self.namespace,
                value=self.variable.get(),
            )

    def configure_checkbutton(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the checkbutton widget in this field.

        This method configures the checkbutton widget in this field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the checkbutton widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                checkbutton widget.
        """
        try:
            # Attempt to configure the checkbutton widget
            self._checkbutton.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_checkbutton' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @override
    def configure_grid(self) -> None:
        """
        Configures the grid layout of the CheckbuttonField widget.

        This method sets the column and row weights for the internal layout of the CheckbuttonField.
        It ensures proper resizing behavior and alignment of label and checkbutton.

        Columns:
            - Column 0: Label (fixed width)
            - Column 1: Checkbutton field (fixed width)

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

        # Set the weight of the 1st column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_columnconfigure(
            index=1,
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
        display_name: str,
        **kwargs,
    ) -> None:
        """
        Creates and configures the widgets for the CheckbuttonField.

        This method initializes the label and the checkbutton widget, binds the internal BooleanVar,
        and places the widgets in the grid layout.

        Args:
            display_name (str): The string to display for the field.
            **kwargs: Additional keyword arguments passed to individual widget constructors.

        Returns:
            None
        """

        # Create a label widget
        self._label: tkinter.Label = tkinter.Label(
            master=self, text=display_name, **kwargs.get("label", {})
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
        self.variable: tkinter.BooleanVar = tkinter.BooleanVar(value=False)

        # Create a checkbutton widget
        self._checkbutton: tkinter.Checkbutton = tkinter.Checkbutton(
            command=self._on_checkbutton_change,
            master=self,
            text=f"{self.variable.get()}",
            variable=self.variable,
            **kwargs.get("checkbutton", {}),
        )

        # Place the checkbutton widget within the grid
        self._checkbutton.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

    @override
    def get(
        self,
        dispatch: bool = False,
    ) -> Tuple[str, bool]:
        """
        Retrieves the current state of the checkbutton.

        If `dispatch` is set to True, it also dispatches a GET event.

        Args:
            dispatch (bool, optional): Whether to dispatch a get event. Defaults to False.

        Returns:
            Tuple[str, bool]: A tuple containing the display label and the boolean value of the checkbutton.
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
            # Dispatch the CHECKBUTTON_FIELD_GET event
            self.dispatcher.dispatch(
                event=Events.CHECKBUTTON_FIELD_GET,
                label=self.display_name,
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
        value: bool,
        dispatch: bool = False,
    ) -> None:
        """
        Sets the state of the checkbutton to the given boolean value.

        If `dispatch` is set to True, a SET event is dispatched.

        Args:
            value (bool): The boolean value to set (True or False).
            dispatch (bool, optional): Whether to dispatch a set event. Defaults to False.

        Returns:
            None
        """

        # Update the variable with the passed value string
        self.variable.set(value=value)

        # Update the text of the checkbutton widget
        self._checkbutton.configure(text=f"{self.variable.get()}")

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the CHECKBUTTON_FIELD_SET event
            self.dispatcher.dispatch(
                event=Events.CHECKBUTTON_FIELD_SET,
                label=self.display_name,
                namespace=self.namespace,
                value=self.variable.get(),
            )


class RadiobuttonField(BaseField):
    """
    A boolean field using a radiobutton widget.

    RadiobuttonField represents a binary user input field consisting of a label and a tkinter.Radiobutton.
    It stores its state in a tkinter.BooleanVar and provides event dispatching and callback support on change.

    The field layout consists of:
        [ Label | Radiobutton ]

    Attributes:
        variable (tkinter.BooleanVar): Holds the current boolean state of the radiobutton.
        label (tkinter.Label): The label widget describing the radiobutton.
        radiobutton (tkinter.Radiobutton): The interactive radiobox widget.

    Inherits from:
        BaseField
    """

    def __init__(
        self,
        display_name: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, bool], None]] = None,
        value: bool = False,
    ) -> None:
        """
        Initializes a new instance of the RadiobuttonField class.

        This constructor sets up the label and radiobutton widget, binds the necessary variable,
        and prepares the field for interaction and layout configuration.

        Args:
            label (str): The label text displayed next to the radiobutton.
            master (tkinter.Misc): The parent container in which this widget is placed.
            namespace (str, optional): The namespace identifier for event dispatching. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[str, bool], None]], optional): Callback function called when the boolean value changes.
            value (bool, optional): The initial boolean state of the radiobutton. Defaults to False.

        Returns:
            None
        """

        # Call the parent class constructor with the passed arguments
        super().__init__(
            display_name=display_name,
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

    @property
    def radiobutton(self) -> tkinter.Radiobutton:
        """
        Returns the radiobutton widget associated with this field.

        The radiobutton displays the name or description of the field.

        Returns:
            tkinter.Radiobutton: The radiobutton widget.
        """

        # Return the tkinter.Radiobutton radiobutton widget
        return self._radiobutton

    def _on_radiobutton_change(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        Handles changes in the radiobutton state.

        This method is triggered when the user toggles the radiobutton. It dispatches an event
        with the new boolean value and triggers an optional callback function.

        Args:
            event (Optional[tkinter.Event], optional): The event object. Defaults to None.

        Returns:
            None
        """

        # Dispatch the RADIOBUTTON_FIELD_CLEARED event
        self.dispatcher.dispatch(
            event=Events.RADIOBUTTON_FIELD_CLEARED,
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

    @override
    def clear(
        self,
        dispatch: bool = False,
    ) -> None:
        """
        Clears the state of the radiobutton, setting it to False.

        If `dispatch` is True, it also dispatches a clear event to notify any listeners.

        Args:
            dispatch (bool, optional): Whether to dispatch a clear event. Defaults to False.

        Returns:
            None
        """

        # Update the variable's value to False
        self.variable.set(value=False)

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the RADIOBUTTON_FIELD_CLEARED event
            self.dispatcher.dispatch(
                event=Events.RADIOBUTTON_FIELD_CLEARED,
                label=self.display_name,
                namespace=self.namespace,
                value=self.variable.get(),
            )

    @override
    def configure_grid(self) -> None:
        """
        Configures the grid layout of the RadiobuttonField widget.

        This method sets the column and row weights for the internal layout of the RadiobuttonField.
        It ensures proper resizing behavior and alignment of label and radiobutton.

        Columns:
            - Column 0: Label (fixed width)
            - Column 1: Radiobutton field (fixed width)

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

        # Set the weight of the 1st column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_columnconfigure(
            index=1,
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

    def configure_radiobutton(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the radiobutton widget in this field.

        This method configures the radiobutton widget in this field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the radiobutton widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                radiobutton widget.
        """
        try:
            # Attempt to configure the radiobutton widget
            self._radiobutton.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_radiobutton' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @override
    def create_widgets(
        self,
        display_name: str,
        **kwargs,
    ) -> None:
        """
        Creates and configures the widgets for the RadiobuttonField.

        This method initializes the label and the radiobutton widget, binds the internal BooleanVar,
        and places the widgets in the grid layout.

        Args:
            display_name (str): The string to display for the field.
            **kwargs: Additional keyword arguments passed to individual widget constructors.

        Returns:
            None
        """

        # Create a label widget
        self._label: tkinter.Label = tkinter.Label(
            master=self,
            text=display_name,
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
        self.variable: tkinter.BooleanVar = tkinter.BooleanVar(value=False)

        # Create a radiobutton widget
        self._radiobutton: tkinter.Radiobutton = tkinter.Radiobutton(
            command=self._on_radiobutton_change,
            master=self,
            text=f"{self.variable.get()}",
            variable=self.variable,
            **kwargs.get("radiobutton", {}),
        )

        # Place the radiobutton widget within the grid
        self._radiobutton.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

    @override
    def get(
        self,
        dispatch: bool = False,
    ) -> Tuple[str, bool]:
        """
        Retrieves the current state of the radiobutton.

        If `dispatch` is set to True, it also dispatches a GET event.

        Args:
            dispatch (bool, optional): Whether to dispatch a get event. Defaults to False.

        Returns:
            Tuple[str, bool]: A tuple containing the display label and the boolean value of the radiobutton.
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
            # Dispatch the RADIOBUTTON_FIELD_GET event
            self.dispatcher.dispatch(
                event=Events.RADIOBUTTON_FIELD_GET,
                label=self.display_name,
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
        value: bool,
        dispatch: bool = False,
    ) -> None:
        """
        Sets the state of the radiobutton to the given boolean value.

        If `dispatch` is set to True, a SET event is dispatched.

        Args:
            value (bool): The boolean value to set (True or False).
            dispatch (bool, optional): Whether to dispatch a set event. Defaults to False.

        Returns:
            None
        """

        # Update the variable with the passed value string
        self.variable.set(value=value)

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the RADIOBUTTON_FIELD_SET event
            self.dispatcher.dispatch(
                event=Events.RADIOBUTTON_FIELD_SET,
                label=self.display_name,
                namespace=self.namespace,
                value=self.variable.get(),
            )


class ToggleButtonField(BaseField):
    """
    A custom boolean field represented as a toggle button.

    ToggleButtonField uses a tkinter.Button to represent a binary on/off value.
    When the button is clicked, it toggles between True and False, updates its display
    (e.g., 🔘 / 🟢), dispatches a change event, and optionally calls a user-defined callback.

    This widget is useful for compact binary choices with clear visual feedback.

    Layout:
        [ Label | Toggle Button ]

    Inherits from:
        BaseField
    """

    def __init__(
        self,
        display_name: str,
        master: tkinter.Misc,
        icons: Tuple[str, str] = ("🟢", "🔘"),
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[bool], None]] = None,
        value: Optional[bool] = False,
        **kwargs,
    ) -> None:
        """
        Initializes the ToggleButtonField.

        This method sets up the field context, including dispatcher, namespace,
        change callback, and optional configuration parameters (e.g. label, default value, icons).

        Args:
            master (Optional[tk.Misc]): The parent widget.
            dispatcher (Dispatcher): The event dispatcher for handling state changes.
            namespace (Optional[str], optional): Namespace for event dispatching. Defaults to None.
            on_change_callback (Optional[Callable], optional): A callback function that is triggered
                when the toggle value changes. Defaults to None.
            **kwargs: Additional field configuration parameters, including:
                - label (str): Display label.
                - default (bool): Initial toggle state.
                - icons (Tuple[str, str]): Icons for (off, on) states.

        Returns:
            None
        """

        # Store the passed icon tuple as an instance variable
        self.icons: Tuple[str, str,] = icons

        # Call the parent class constructor with the passed arguments
        super().__init__(
            display_name=display_name,
            master=master,
            namespace=namespace,
            on_change_callback=on_change_callback,
            value=value,
            **kwargs,
        )

    @property
    def button(self) -> tkinter.Button:
        """
        Returns the button widget associated with this field.

        The button displays the name or description of the field.

        Returns:
            tkinter.Button: The button widget.
        """

        # Return the tkinter.Button radiobutton widget
        return self._button

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

    def _on_button_change(self) -> None:
        """
        Toggles the field value and updates the UI.

        This method manually toggles the internal boolean state, updates the button label,
        dispatches a change event using the dispatcher, and calls the provided
        `on_change_callback` (if available).

        Args:
            None

        Returns:
            None
        """

        # Toggle the value manually
        self.variable.set(not self.variable.get())

        # Update button text based on new state
        self._button.configure(text=self.icons[0] if self.variable.get() else self.icons[1])

        # Dispatch the TOGGLE_BUTTON_FIELD_CLEARED event
        self.dispatcher.dispatch(
            event=Events.TOGGLE_BUTTON_FIELD_CLEARED,
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

    @override
    def clear(
        self,
        dispatch: bool = False,
    ) -> None:
        """
        Resets the toggle field to its default state (False).

        This method also updates the button display and dispatches a change event.

        Args:
            None

        Returns:
            None
        """

        # Update the variable's value to False
        self.variable.set(value=False)

        # Update button text based on new state
        self._button.configure(text=self.icons[0] if self.variable.get() else self.icons[1])

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the TOGGLE_BUTTON_FIELD_CLEARED event
            self.dispatcher.dispatch(
                event=Events.TOGGLE_BUTTON_FIELD_CLEARED,
                label=self.display_name,
                namespace=self.namespace,
                value=self.variable.get(),
            )

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
        """
        Configures the grid layout.

        Args:
            None

        Returns:
            None
        """

        # Set the weight of the 0th column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_columnconfigure(
            index=0,
            weight=0,
        )

        # Set the weight of the 1st column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_columnconfigure(
            index=1,
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
        display_name: str,
        **kwargs,
    ) -> None:
        """
        Creates and places the label and toggle button widgets.

        This method initializes the label and button, binds a `BooleanVar` to the field,
        and sets the initial button icon based on the current boolean value.
        All widgets are arranged in a grid layout.

        Args:
            display_name (str): The display label for the field.
            **kwargs: Optional keyword arguments for widget configuration:
                - 'label': config for the `tkinter.Label`
                - 'button': config for the `tkinter.Button`

        Returns:
            None
        """

        # Create a tkinter.Label widget
        self._label: tkinter.Label = tkinter.Label(
            master=self,
            text=display_name,
            **kwargs.get(
                "label",
                {},
            ),
        )

        # Place the tkinter.Label widget within the grid
        self._label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a string variable
        self.variable: tkinter.BooleanVar = tkinter.BooleanVar(value=False)

        # Create a tkinter.Button widget
        self._button: tkinter.Button = tkinter.Button(
            command=self._on_button_change,
            master=self,
            text=self.icons[0] if self.variable.get() else self.icons[1],
            **kwargs.get(
                "button",
                {},
            ),
        )

        # Place the tkinter.Button widget within the grid
        self._button.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
        )

    @override
    def get(
        self,
        dispatch: bool = False,
    ) -> Tuple[str, bool]:
        """
        Retrieves the current state of the toggle button.

        Optionally dispatches a GET event for external listeners.

        Args:
            dispatch (bool, optional): Whether to dispatch a get event. Defaults to False.

        Returns:
            Tuple[str, bool]: A tuple containing the field's label and current boolean value.
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
            # Dispatch the TOGGLE_BUTTON_FIELD_GET event
            self.dispatcher.dispatch(
                event=Events.TOGGLE_BUTTON_FIELD_GET,
                label=self.display_name,
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
        value: bool,
        dispatch: bool = False,
    ) -> None:
        """
        Sets the state of the toggle button to the given value.

        Updates the internal `BooleanVar`, adjusts the displayed icon,
        and optionally dispatches a SET event.

        Args:
            value (bool): The new boolean value for the toggle.
            dispatch (bool, optional): Whether to dispatch a set event. Defaults to False.

        Returns:
            None
        """

        # Update the variable with the passed value string
        self.variable.set(value=value)

        # Update button text based on new state
        self._button.configure(text=self.icons[0] if self.variable.get() else self.icons[1])

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the TOGGLE_BUTTON_FIELD_SET event
            self.dispatcher.dispatch(
                event=Events.TOGGLE_BUTTON_FIELD_SET,
                label=self.display_name,
                namespace=self.namespace,
                value=self.variable.get(),
            )
