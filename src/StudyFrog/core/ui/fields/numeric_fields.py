"""
Author: lodego
Date: 2025-04-06
"""

import tkinter
import traceback

from tkinter.constants import *
from typing import *

from utils.base_field import BaseField
from utils.constants import Constants
from utils.events import Events
from utils.miscellaneous import Miscellaneous


__all__: Final[List[str]] = [
    "FloatSpinboxField",
    "IntegerSpinboxField",
]


class FloatSpinboxField(BaseField):
    """
    A float spinbox field widget.

    This class represents a spinbox field with a label, decrement button, entry, increment button, and reset button.
    It provides methods to configure and interact with the widgets, as well as a callback
    for handling changes in the entry's value.
    """

    def __init__(
        self,
        label: str,
        master: tkinter.Misc,
        maximum: float = 100.0,
        minimum: float = -100.0,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[float, str], None]] = None,
        step_size: float = 0.1,
        value: float = 0.0,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the FloatSpinboxField class.

        Args:
            label (str): The label to be displayed for the field.
            master (tkinter.Misc): The parent widget.
            maximum (float): The maximum value for the field. Defaults to 100.0.
            minimum (float): The minimum value for the field. Defaults to -100.0.
            namespace (str): The namespace for the field. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[float, str], None]]): The callback function to be called when the value of the field changes. Defaults to None.
            step_size (float): The step size for the field. Defaults to 0.1.
            value (float): The initial value for the field. Defaults to 0.0.
            kwargs: Additional keyword arguments for the widgets.
        """

        # Call the parent class constructor with the passed arguments
        super().__init__(
            label=label,
            master=master,
            namespace=namespace,
            on_change_callback=on_change_callback,
            value=value,
            **kwargs,
        )

        # Store the passed maximum value
        self._maximum: float = maximum

        # Store the passed minimum value
        self._minimum: float = minimum

        # Store the passed step size value
        self._stepsize: float = step_size

    @property
    def decrement_button(self) -> tkinter.Button:
        """
        Returns the 'decrement button' button widget.

        Returns:
            tkinter.Button: The 'decrement button' button widget.
        """

        # Return the 'decrement button' button widget
        return self._decrement_button

    @property
    def entry(self) -> tkinter.Entry:
        """
        Returns the entry widget.

        Returns:
            tkinter.Entry: The entry widget.
        """

        # Return the entry widget
        return self._entry

    @property
    def increment_button(self) -> tkinter.Button:
        """
        Returns the 'increment button' button widget.

        Returns:
            tkinter.Button: The 'increment button' button widget.
        """

        # Return the 'increment button' button widget
        return self._increment_button

    @property
    def label(self) -> tkinter.Label:
        """
        Returns the label widget.

        Returns:
            tkinter.Label: The label widget.
        """

        # Return the label widget
        return self._label

    @property
    def maximum(self) -> float:
        """
        Returns the maximum float value for the FloatSpinboxField.

        Returns:
            float: The maximum float value for the FloatSpinboxField.
        """

        # Return the 'maximum' instance variable
        return self._maximum

    @maximum.setter
    def maximum(
        self,
        value: float = 100.0,
    ) -> None:
        """
        Sets the maximum value for the FloatSpinboxField.

        Args:
            value (float): The the maximum value to set. Defaults to 100.0.

        Returns:
            None
        """

        # Update the 'maximum' instance variable
        self._maximum = value

    @property
    def minimum(self) -> float:
        """
        Returns the minimum float value for the FloatSpinboxField.

        Returns:
            float: The minimum float value for the FloatSpinboxField.
        """

        # Return the 'minimum' instance variable
        return self._minimum

    @minimum.setter
    def minimum(
        self,
        value: float = -100.0,
    ) -> None:
        """
        Sets the minimum value for the FloatSpinboxField.

        Args:
            value (float): The the minimum value to set. Defaults to -100.0.

        Returns:
            None
        """

        # Update the 'minimum' instance variable
        self._minimum = value

    @property
    def reset_button(self) -> tkinter.Button:
        """
        Returns the 'reset button' button widget.

        Returns:
            tkinter.Button: The 'reset button' button widget.
        """

        # Return the 'reset button' button widget
        return self._reset_button

    @property
    def step_size(self) -> float:
        """
        Returns the step size for the FloatSpinboxField.

        Returns:
            float: The step size for the FloatSpinboxField.
        """

        # Return the 'step size' instance variable
        return self._step_size

    @step_size.setter
    def step_size(
        self,
        value: float = 0.1,
    ) -> None:
        """
        Sets the step size for the FloatSpinboxField.

        Args:
            value (float): The step size to set. Defaults to 0.1.

        Returns:
            None
        """

        # Update the 'step size' instance variable
        self._step_size = value

    def _on_decrement_button_click(self) -> None:
        """
        Handles the click event for the decrement button.

        This method is called when the decrement button is clicked.
        It decrements the value of the entry field by the step size and
        dispatches the FLOAT_SPINBOX_FIELD_CHANGED event in the specified
        namespace.

        Returns:
            None
        """

        # Obtain the current value of the tkinter.StringVar variable
        string_value: str = self.variable.get()

        # Convert the current value (str) to float
        float_value: float = float(string_value)

        # Check, if the decremented float value is less than the maximum value
        if (float_value - self.step_size) < self._maximum:
            # Update the value of the tkinter.StringVar variable to the decremented float value converted to str
            self.variable.set(value=f"{float_value - self.step_size}")
        else:
            # Return early
            return

        # Dispatch the FLOAT_SPINBOX_FIELD_CHANGED event in the passed namespace
        self.dispatcher.dispatch(
            event=Events.FLOAT_SPINBOX_FIELD_CHANGED,
            label=self.display_name,
            namespace=self.namespace,
            value=float_value,
        )

        # Check, if the 'on_change_callback' function exists
        if self.on_change_callback:
            # Call the 'on_change_callback' function and pass the display name as well as the variable's value to it
            self.on_change_callback(self.display_name, self.variable.get())

    def _on_entry_change(
        self,
        dispatch: bool = False,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        Handles the change event for the entry field.

        This method is called when the value of the entry field changes.
        It verifies if the current value is a valid float. If valid, it hides
        the warning label; otherwise, it shows the warning label. If the value
        is valid and the dispatch flag is set to True, it dispatches the
        FLOAT_SPINBOX_FIELD_CHANGED event in the specified namespace.

        Args:
            dispatch (bool): Whether to dispatch the event. Defaults to False.
            event (Optional[tkinter.Event]): The event instance. Defaults to None.

        Returns:
            None
        """
        # Obtain the current value of the tkinter.StringVar variable
        string_value: str = self.variable.get()

        # float value placeholder
        float_value: Optional[float] = None

        # Check, if the str value is an float number
        if Miscellaneous.is_float_number(string=string_value):
            # Convert the current value (str) to float
            float_value = float(string_value)

            # Hide the'warning label' label widget
            self._warning_label.grid_forget()
        else:
            # Show the'warning label' label widget
            self._warning_label.grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

        # Check, if the float value is not None and the dispatch flag is set to True
        if float_value is not None and dispatch:
            # Dispatch the FLOAT_SPINBOX_FIELD_CHANGED event in the passed namespace
            self.dispatcher.dispatch(
                event=Events.FLOAT_SPINBOX_FIELD_CHANGED,
                label=self.display_name,
                namespace=self.namespace,
                value=float_value,
            )

        # Check, if the 'on_change_callback' function exists and the float value is not None
        if float_value is not None and self.on_change_callback:
            # Call the 'on_change_callback' function and pass the display name as well as the variable's value to it
            self.on_change_callback(self.display_name, float_value)

    def _on_increment_button_click(self) -> None:
        """
        Handles the event when the 'Increment' button is clicked.

        This method increments the float spinbox field by the step size.
        If the incremented value is less than the maximum value, it updates the value of the tkinter.StringVar variable to the incremented float value converted to str.
        It also dispatches the FLOAT_SPINBOX_FIELD_CHANGED event in the passed namespace.

        Returns:
            None
        """

        # Obtain the current value of the tkinter.StringVar variable
        string_value: str = self.variable.get()

        # Convert the current value (str) to float
        float_value: float = float(string_value)

        # Check, if the incremented float value is less than the maximum value
        if (float_value + self.step_size) < self._maximum:
            # Update the value of the tkinter.StringVar variable to the incremented float value converted to str
            self.variable.set(value=f"{float_value + self.step_size}")
        else:
            # Return early
            return

        # Check, if the float value is not None and the dispatch flag is set to True
        if float_value is not None and dispatch:
            # Dispatch the FLOAT_SPINBOX_FIELD_CHANGED event in the passed namespace
            self.dispatcher.dispatch(
                event=Events.FLOAT_SPINBOX_FIELD_CHANGED,
                label=self.display_name,
                namespace=self.namespace,
                value=float(self.variable.get()),
            )

        # Check, if the 'on_change_callback' function exists and the float value is not None
        if self.on_change_callback:
            # Call the 'on_change_callback' function and pass the display name as well as the variable's value to it
            self.on_change_callback(self.display_name, self.variable.get())

    def _on_reset_button_click(self) -> None:
        """
        Handles the event when the 'Reset' button is clicked.

        This method updates the value of the tkinter.StringVar variable to "0.0".

        Returns:
            None
        """

        # Update the value of the tkinter.StringVar variable to "0.0"
        self.variable.set(value="0.0")

        # Check, if the 'on_change_callback' function exists
        if self.on_change_callback:
            # Call the 'on_change_callback' function and pass the display name as well as the variable's value to it
            self.on_change_callback(self.display_name, self.variable.get())

    def clear(
        self,
        dispatch: bool = False,
    ) -> None:
        """
        Clears the float spinbox field.

        This method clears the float spinbox field by setting its value to "0.0".
        If the dispatch flag is set to True, it will also dispatch the
        FLOAT_SPINBOX_FIELD_CLEARED event in the passed namespace.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            None
        """
        # Update the value of the tkinter.StringVar variable to "0.0"
        self.variable.set(value="0.0")

        # Check, if the 'dispatch' flag has been set to True
        if dispatch:
            # Dispatch the FLOAT_SPINBOX_FIELD_CLEARED event in the passed namespace
            self.dispatcher.dispatch(
                event=Events.FLOAT_SPINBOX_FIELD_CLEARED,
                label=self.display_name,
                namespace=self.namespace,
                value=float(self.variable.get()),
            )

    def configure_decrement_button(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the 'decrement button' button widget in the float spinbox field.

        This method configures the 'decrement button' button widget in the float spinbox field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the 'decrement button' button widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                'decrement button' button widget.
        """
        try:
            # Attempt to configure the 'decrement button' button widget
            self._decrement_button.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_decrement_button' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_entry(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the entry widget in the float spinbox field.

        This method configures the entry widget in the float spinbox field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the entry widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                entry widget.
        """
        try:
            # Attempt to configure the entry widget with the provided arguments
            self._entry.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_entry' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_grid(self) -> None:
        """
        Configures the grid of the FloatSpinboxField widget.

        This method configures the grid of the FloatSpinboxField widget by setting
        the weights of the columns and rows.

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

        # Set the weight of the 4th column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_columnconfigure(
            index=4,
            weight=0,
        )

        # Set the weight of the 0th row to 1
        # This means that the row will stretch when the window is resized
        self.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Set the weight of the 2nd row to 0
        # This means that the row will not stretch when the window is resized
        self.grid_rowconfigure(
            index=1,
            weight=0,
        )

    def configure_increment_button(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the 'increment button' button widget in the float spinbox field.

        This method configures the 'increment button' button widget in the float spinbox field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the 'increment button' button widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                'increment button' button widget.
        """
        try:
            # Attempt to configure the 'increment button' button widget
            self._increment_button.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_increment_button' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_label(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the label widget in the float spinbox field.

        This method configures the label widget in the float spinbox field
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
            # Attempt to configure the label widget with the provided arguments
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

    def configure_reset_button(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the 'reset button' button widget in the float spinbox field.

        This method configures the 'reset button' button widget in the float spinbox field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the 'reset button' button widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                'reset button' button widget.
        """
        try:
            # Attempt to configure the 'reset button' button widget
            self._reset_button.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_reset_button' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def create_widgets(
        self,
        label: str,
        **kwargs,
    ) -> None:
        """
        Creates and configures the widgets for a numeric field.

        This method initializes label, entry, and button widgets for a numeric
        input field, setting their layout configuration and binding necessary
        events. It includes decrement, increment, reset buttons, and a warning
        label to provide feedback.

        Args:
            label (str): The text for the label widget.
            **kwargs: Optional keyword arguments for configuring the widgets.
        """

        # Create a label widget
        self._label: tkinter.Label = tkinter.Label(
            master=self, text=label, **kwargs.get("label", {})
        )

        # Place the label widget in the grid
        self._label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a StringVar to hold the entry value
        self.variable: tkinter.StringVar = tkinter.StringVar(value="0.0")

        # Create a 'decrement button' button widget
        self._decrement_button: tkinter.Button = tkinter.Button(
            command=self._on_decrement_button_click,
            master=self,
            text="-",
            **kwargs.get("decrement_button", {}),
        )

        # Place the 'decrement button' button widget in the grid
        self._decrement_button.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
        )

        # Create an entry widget
        self._entry: tkinter.Entry = tkinter.Entry(
            master=self, textvariable=self.variable, **kwargs.get("entry", {})
        )

        # Place the entry widget in the grid
        self._entry.grid(
            column=2,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Bind the entry widget to 'on_entry_change' method via the '<KeyRelease>' event
        self._entry.bind(
            func=self._on_entry_change,
            sequence="<KeyRelease>",
        )

        # Create an 'increment button' button widget
        self._increment_button: tkinter.Button = tkinter.Button(
            command=self._on_increment_button_click,
            master=self,
            text="+",
            **kwargs.get("increment_button", {}),
        )

        # Place the 'increment button' button widget in the grid
        self._increment_button.grid(
            column=3,
            padx=5,
            pady=5,
            row=0,
        )

        # Create a 'reset button' button widget
        self._reset_button: tkinter.Button = tkinter.Button(
            command=self._on_reset_button_click,
            master=self,
            text="X",
            **kwargs.get("reset_button", {}),
        )

        # Place the 'reset button' button widget in the grid
        self._reset_button.grid(
            column=4,
            padx=5,
            pady=5,
            row=0,
        )

        # Create a 'warning label' label widget
        self._warning_label: tkinter.Label = tkinter.Label(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.RED["default"],
            master=self,
            text=f"{self.variable.get()}",
            **kwargs.get("warning_label", {}),
        )

    def get(
        self,
        dispatch: bool = False,
    ) -> Tuple[str, float]:
        """
        Retrieves the text of the label and the value of the float spinbox field.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            Tuple[str, float]: A tuple containing the text of the label and the value of the float spinbox field.
        """
        # Obtain the 'label' (str) and 'value' (int) from the display name and the tkinter.StringVar variable
        (
            label,
            value,
        ) = (
            self.display_name,
            float(self.variable.get()),
        )

        # Check, if the 'dispatch' flag has been set to True
        if dispatch:
            # Dispatch the FLOAT_SPINBOX_FIELD_GET event in the passed namespace
            self.dispatcher.dispatch(
                event=Events.FLOAT_SPINBOX_FIELD_GET,
                label=label,
                namespace=self.namespace,
                value=value,
            )

        # Return the 'label' (str) and the 'value' (int)
        return (
            label,
            value,
        )

    def set(
        self,
        value: float,
        dispatch: bool = False,
    ) -> None:
        """
        Sets the value of the float spinbox field.

        This method sets the value of the float spinbox field to the passed value. If the dispatch
        flag is set to True, it will also dispatch the SET event.

        Args:
            value (float): The value to set for the float spinbox field.
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            None
        """

        # Check if the passed value is within the bounds of minimum and maximum
        if self._minimum <= value <= self._maximum:
            # Update the value of the tkinter.StringVar variable
            self.variable.set(value=str(value))
        else:
            # Log a warning message indicating that the value is out of bounds
            self.logger.warning(
                message=f"Value '{value}' is out of bounds ({self._minimum} - {self._maximum})."
            )

            # Return early
            return

        # Check, if the 'dispatch' flag has been set to True
        if dispatch:
            # Dispatch the FLOAT_SPINBOX_FIELD_SET event in the passed namespace
            self.dispatcher.dispatch(
                event=Events.FLOAT_SPINBOX_FIELD_SET,
                label=self.display_name,
                namespace=self.namespace,
                value=value,
            )


class IntegerSpinboxField(BaseField):
    """
    A int spinbox field widget.

    This class represents a spinbox field with a label, decrement button, entry, increment button, and reset button.
    It provides methods to configure and interact with the widgets, as well as a callback
    for handling changes in the entry's value.
    """

    def __init__(
        self,
        label: str,
        master: tkinter.Misc,
        maximum: int = 100,
        minimum: int = -100,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[int, str], None]] = None,
        step_size: int = 1,
        value: int = 0,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the IntegerSpinboxField class.

        Args:
            label (str): The label to be displayed for the field.
            master (tkinter.Misc): The parent widget.
            maximum (int): The maximum value for the field. Defaults to 100.
            minimum (int): The minimum value for the field. Defaults to -100.
            namespace (str): The namespace for the field. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[int, str], None]]): The callback function to be called when the value of the field changes. Defaults to None.
            step_size (int): The step size for the field. Defaults to 1.
            value (int): The initial value for the field. Defaults to 0.
            kwargs: Additional keyword arguments for the widgets.
        """

        # Call the parent class constructor with the passed arguments
        super().__init__(
            label=label,
            master=master,
            namespace=namespace,
            on_change_callback=on_change_callback,
            value=value,
            **kwargs,
        )

        # Store the passed maximum value
        self._maximum: int = maximum

        # Store the passed minimum value
        self._minimum: int = minimum

        # Store the passed step size value
        self._stepsize: int = step_size

    @property
    def decrement_button(self) -> tkinter.Button:
        """
        Returns the 'decrement button' button widget.

        Returns:
            tkinter.Button: The 'decrement button' button widget.
        """

        # Return the 'decrement button' button widget
        return self._decrement_button

    @property
    def entry(self) -> tkinter.Entry:
        """
        Returns the entry widget.

        Returns:
            tkinter.Entry: The entry widget.
        """

        # Return the entry widget
        return self._entry

    @property
    def increment_button(self) -> tkinter.Button:
        """
        Returns the 'increment button' button widget.

        Returns:
            tkinter.Button: The 'increment button' button widget.
        """

        # Return the 'increment button' button widget
        return self._increment_button

    @property
    def label(self) -> tkinter.Label:
        """
        Returns the label widget.

        Returns:
            tkinter.Label: The label widget.
        """

        # Return the label widget
        return self._label

    @property
    def maximum(self) -> int:
        """
        Returns the maximum int value for the IntegerSpinboxField.

        Returns:
            int: The maximum int value for the IntegerSpinboxField.
        """

        # Return the 'maximum' instance variable
        return self._maximum

    @maximum.setter
    def maximum(
        self,
        value: int = 100,
    ) -> None:
        """
        Sets the maximum value for the IntegerSpinboxField.

        Args:
            value (int): The the maximum value to set. Defaults to 100.

        Returns:
            None
        """

        # Update the 'maximum' instance variable
        self._maximum = value

    @property
    def minimum(self) -> int:
        """
        Returns the minimum int value for the IntegerSpinboxField.

        Returns:
            int: The minimum int value for the IntegerSpinboxField.
        """

        # Return the 'minimum' instance variable
        return self._minimum

    @minimum.setter
    def minimum(
        self,
        value: int = -100,
    ) -> None:
        """
        Sets the minimum value for the IntegerSpinboxField.

        Args:
            value (int): The the minimum value to set. Defaults to -100.

        Returns:
            None
        """

        # Update the 'minimum' instance variable
        self._minimum = value

    @property
    def reset_button(self) -> tkinter.Button:
        """
        Returns the 'reset button' button widget.

        Returns:
            tkinter.Button: The 'reset button' button widget.
        """

        # Return the 'reset button' button widget
        return self._reset_button

    @property
    def step_size(self) -> int:
        """
        Returns the step size for the IntegerSpinboxField.

        Returns:
            int: The step size for the IntegerSpinboxField.
        """

        # Return the 'step size' instance variable
        return self._step_size

    @step_size.setter
    def step_size(
        self,
        value: int = 1,
    ) -> None:
        """
        Sets the step size for the IntegerSpinboxField.

        Args:
            value (int): The step size to set. Defaults to 1.

        Returns:
            None
        """

        # Update the 'step size' instance variable
        self._step_size = value

    def _on_decrement_button_click(self) -> None:
        """
        Handles the click event for the decrement button.

        This method is called when the decrement button is clicked.
        It decrements the value of the entry field by the step size and
        dispatches the INT_SPINBOX_FIELD_CHANGED event in the specified
        namespace.

        Returns:
            None
        """

        # Obtain the current value of the tkinter.StringVar variable
        string_value: str = self.variable.get()

        # Convert the current value (str) to int
        int_value: int = int(string_value)

        # Check, if the decremented int value is less than the maximum value
        if (int_value - self.step_size) < self._maximum:
            # Update the value of the tkinter.StringVar variable to the decremented int value converted to str
            self.variable.set(value=f"{int_value - self.step_size}")
        else:
            # Return early
            return

        # Dispatch the INT_SPINBOX_FIELD_CHANGED event in the passed namespace
        self.dispatcher.dispatch(
            event=Events.INT_SPINBOX_FIELD_CHANGED,
            label=self.display_name,
            namespace=self.namespace,
            value=int_value,
        )

        # Check, if the 'on_change_callback' function exists
        if self.on_change_callback:
            # Call the 'on_change_callback' function and pass the display name as well as the variable's value to it
            self.on_change_callback(self.display_name, self.variable.get())

    def _on_entry_change(
        self,
        dispatch: bool = False,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        Handles the change event for the entry field.

        This method is called when the value of the entry field changes.
        It verifies if the current value is a valid int. If valid, it hides
        the warning label; otherwise, it shows the warning label. If the value
        is valid and the dispatch flag is set to True, it dispatches the
        INT_SPINBOX_FIELD_CHANGED event in the specified namespace.

        Args:
            dispatch (bool): Whether to dispatch the event. Defaults to False.
            event (Optional[tkinter.Event]): The event instance. Defaults to None.

        Returns:
            None
        """
        # Obtain the current value of the tkinter.StringVar variable
        string_value: str = self.variable.get()

        # int value placeholder
        int_value: Optional[int] = None

        # Check, if the str value is an int number
        if Miscellaneous.is_int_number(string=string_value):
            # Convert the current value (str) to int
            int_value = int(string_value)

            # Hide the'warning label' label widget
            self._warning_label.grid_forget()
        else:
            # Show the'warning label' label widget
            self._warning_label.grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

        # Check, if the int value is not None and the dispatch flag is set to True
        if int_value is not None and dispatch:
            # Dispatch the INT_SPINBOX_FIELD_CHANGED event in the passed namespace
            self.dispatcher.dispatch(
                event=Events.INT_SPINBOX_FIELD_CHANGED,
                label=self.display_name,
                namespace=self.namespace,
                value=int_value,
            )

        # Check, if the 'on_change_callback' function exists and the int value is not None
        if int_value is not None and self.on_change_callback:
            # Call the 'on_change_callback' function and pass the display name as well as the variable's value to it
            self.on_change_callback(self.display_name, int_value)

    def _on_increment_button_click(self) -> None:
        """
        Handles the event when the 'Increment' button is clicked.

        This method increments the int spinbox field by the step size.
        If the incremented value is less than the maximum value, it updates the value of the tkinter.StringVar variable to the incremented int value converted to str.
        It also dispatches the INT_SPINBOX_FIELD_CHANGED event in the passed namespace.

        Returns:
            None
        """

        # Obtain the current value of the tkinter.StringVar variable
        string_value: str = self.variable.get()

        # Convert the current value (str) to int
        int_value: int = int(string_value)

        # Check, if the incremented int value is less than the maximum value
        if (int_value + self.step_size) < self._maximum:
            # Update the value of the tkinter.StringVar variable to the incremented int value converted to str
            self.variable.set(value=f"{int_value + self.step_size}")
        else:
            # Return early
            return

        # Check, if the int value is not None and the dispatch flag is set to True
        if int_value is not None and dispatch:
            # Dispatch the INT_SPINBOX_FIELD_CHANGED event in the passed namespace
            self.dispatcher.dispatch(
                event=Events.INT_SPINBOX_FIELD_CHANGED,
                label=self.display_name,
                namespace=self.namespace,
                value=int(self.variable.get()),
            )

        # Check, if the 'on_change_callback' function exists and the int value is not None
        if self.on_change_callback:
            # Call the 'on_change_callback' function and pass the display name as well as the variable's value to it
            self.on_change_callback(self.display_name, self.variable.get())

    def _on_reset_button_click(self) -> None:
        """
        Handles the event when the 'Reset' button is clicked.

        This method updates the value of the tkinter.StringVar variable to "0".

        Returns:
            None
        """

        # Update the value of the tkinter.StringVar variable to "0"
        self.variable.set(value="0")

        # Check, if the 'on_change_callback' function exists
        if self.on_change_callback:
            # Call the 'on_change_callback' function and pass the display name as well as the variable's value to it
            self.on_change_callback(self.display_name, self.variable.get())

    def clear(
        self,
        dispatch: bool = False,
    ) -> None:
        """
        Clears the int spinbox field.

        This method clears the int spinbox field by setting its value to "0".
        If the dispatch flag is set to True, it will also dispatch the
        INT_SPINBOX_FIELD_CLEARED event in the passed namespace.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            None
        """
        # Update the value of the tkinter.StringVar variable to "0"
        self.variable.set(value="0")

        # Check, if the 'dispatch' flag has been set to True
        if dispatch:
            # Dispatch the INT_SPINBOX_FIELD_CLEARED event in the passed namespace
            self.dispatcher.dispatch(
                event=Events.INT_SPINBOX_FIELD_CLEARED,
                label=self.display_name,
                namespace=self.namespace,
                value=int(self.variable.get()),
            )

    def configure_decrement_button(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the 'decrement button' button widget in the int spinbox field.

        This method configures the 'decrement button' button widget in the int spinbox field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the 'decrement button' button widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                'decrement button' button widget.
        """
        try:
            # Attempt to configure the 'decrement button' button widget
            self._decrement_button.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_decrement_button' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_entry(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the entry widget in the int spinbox field.

        This method configures the entry widget in the int spinbox field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the entry widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                entry widget.
        """
        try:
            # Attempt to configure the entry widget with the provided arguments
            self._entry.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_entry' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_grid(self) -> None:
        """
        Configures the grid of the IntegerSpinboxField widget.

        This method configures the grid of the IntegerSpinboxField widget by setting
        the weights of the columns and rows.

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

        # Set the weight of the 4th column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_columnconfigure(
            index=4,
            weight=0,
        )

        # Set the weight of the 0th row to 1
        # This means that the row will stretch when the window is resized
        self.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Set the weight of the 2nd row to 0
        # This means that the row will not stretch when the window is resized
        self.grid_rowconfigure(
            index=1,
            weight=0,
        )

    def configure_increment_button(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the 'increment button' button widget in the int spinbox field.

        This method configures the 'increment button' button widget in the int spinbox field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the 'increment button' button widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                'increment button' button widget.
        """
        try:
            # Attempt to configure the 'increment button' button widget
            self._increment_button.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_increment_button' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_label(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the label widget in the int spinbox field.

        This method configures the label widget in the int spinbox field
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
            # Attempt to configure the label widget with the provided arguments
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

    def configure_reset_button(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the 'reset button' button widget in the int spinbox field.

        This method configures the 'reset button' button widget in the int spinbox field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the 'reset button' button widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                'reset button' button widget.
        """
        try:
            # Attempt to configure the 'reset button' button widget
            self._reset_button.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_reset_button' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def create_widgets(
        self,
        label: str,
        **kwargs,
    ) -> None:
        """
        Creates and configures the widgets for a numeric field.

        This method initializes label, entry, and button widgets for a numeric
        input field, setting their layout configuration and binding necessary
        events. It includes decrement, increment, reset buttons, and a warning
        label to provide feedback.

        Args:
            label (str): The text for the label widget.
            **kwargs: Optional keyword arguments for configuring the widgets.
        """

        # Create a label widget
        self._label: tkinter.Label = tkinter.Label(
            master=self, text=label, **kwargs.get("label", {})
        )

        # Place the label widget in the grid
        self._label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a StringVar to hold the entry value
        self.variable: tkinter.StringVar = tkinter.StringVar(value="0")

        # Create a 'decrement button' button widget
        self._decrement_button: tkinter.Button = tkinter.Button(
            command=self._on_decrement_button_click,
            master=self,
            text="-",
            **kwargs.get("decrement_button", {}),
        )

        # Place the 'decrement button' button widget in the grid
        self._decrement_button.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
        )

        # Create an entry widget
        self._entry: tkinter.Entry = tkinter.Entry(
            master=self, textvariable=self.variable, **kwargs.get("entry", {})
        )

        # Place the entry widget in the grid
        self._entry.grid(
            column=2,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Bind the entry widget to 'on_entry_change' method via the '<KeyRelease>' event
        self._entry.bind(
            func=self._on_entry_change,
            sequence="<KeyRelease>",
        )

        # Create an 'increment button' button widget
        self._increment_button: tkinter.Button = tkinter.Button(
            command=self._on_increment_button_click,
            master=self,
            text="+",
            **kwargs.get("increment_button", {}),
        )

        # Place the 'increment button' button widget in the grid
        self._increment_button.grid(
            column=3,
            padx=5,
            pady=5,
            row=0,
        )

        # Create a 'reset button' button widget
        self._reset_button: tkinter.Button = tkinter.Button(
            command=self._on_reset_button_click,
            master=self,
            text="X",
            **kwargs.get("reset_button", {}),
        )

        # Place the 'reset button' button widget in the grid
        self._reset_button.grid(
            column=4,
            padx=5,
            pady=5,
            row=0,
        )

        # Create a 'warning label' label widget
        self._warning_label: tkinter.Label = tkinter.Label(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.RED["default"],
            master=self,
            text=f"{self.variable.get()}",
            **kwargs.get("warning_label", {}),
        )

    def get(
        self,
        dispatch: bool = False,
    ) -> Tuple[str, int]:
        """
        Retrieves the text of the label and the value of the int spinbox field.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            Tuple[str, int]: A tuple containing the text of the label and the value of the int spinbox field.
        """
        # Obtain the 'label' (str) and 'value' (int) from the display name and the tkinter.StringVar variable
        (
            label,
            value,
        ) = (
            self.display_name,
            int(self.variable.get()),
        )

        # Check, if the 'dispatch' flag has been set to True
        if dispatch:
            # Dispatch the INT_SPINBOX_FIELD_GET event in the passed namespace
            self.dispatcher.dispatch(
                event=Events.INT_SPINBOX_FIELD_GET,
                label=label,
                namespace=self.namespace,
                value=value,
            )

        # Return the 'label' (str) and the 'value' (int)
        return (
            label,
            value,
        )

    def set(
        self,
        value: int,
        dispatch: bool = False,
    ) -> None:
        """
        Sets the value of the int spinbox field.

        This method sets the value of the int spinbox field to the passed value. If the dispatch
        flag is set to True, it will also dispatch the SET event.

        Args:
            value (int): The value to set for the int spinbox field.
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            None
        """

        # Check if the passed value is within the bounds of minimum and maximum
        if self._minimum <= value <= self._maximum:
            # Update the value of the tkinter.StringVar variable
            self.variable.set(value=str(value))
        else:
            # Log a warning message indicating that the value is out of bounds
            self.logger.warning(
                message=f"Value '{value}' is out of bounds ({self._minimum} - {self._maximum})."
            )

            # Return early
            return

        # Check, if the 'dispatch' flag has been set to True
        if dispatch:
            # Dispatch the INT_SPINBOX_FIELD_SET event in the passed namespace
            self.dispatcher.dispatch(
                event=Events.INT_SPINBOX_FIELD_SET,
                label=self.display_name,
                namespace=self.namespace,
                value=value,
            )
