"""
Author: lodego
Date: 2025-04-05
"""

import platform
import tkinter
import traceback

from PIL import Image
from PIL import ImageGrab
from PIL import ImageTk
from tkinter.constants import *
from tkinter import font
from tkinter import ttk
from typing import *

from utils.base_field import BaseField
from utils.constants import Constants
from utils.events import Events
from utils.object import MutableBaseObject


__all__: Final[List[str]] = [
    "MultiSelectAnswerField",
    "MultipleSelectResponseField",
    "MultiLineTextField",
    "PasswordTextField",
    "ReadOnlyMultiLineTextField",
    "ReadOnlySingleLineTextField",
    "SearchbarField",
    "SingleLineTextField",
    "TextEditorField",
]


class MultiSelectAnswerField(BaseField):
    """
    A custom compound field widget designed for multiple-select answer input.

    This widget consists of a label, a checkbutton with a boolean flag,
    an optional label describing the checkbutton, an entry field, and a clear button.

    It is intended to be used for constructing answers to multiple-select questions,
    where both a text input and a 'correctness' flag are required.
    """

    def __init__(
        self,
        display_name: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, Tuple[str, bool]], None]] = None,
        value: Optional[str] = None,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the MultiSelectAnswerField class.

        Args:
            display_name (str): The string to display for the field.label (str): The label text associated with the field.
            master (tkinter.Misc): The parent tkinter widget.
            namespace (str): The namespace for event dispatching. Defaults to global.
            on_change_callback (Optional[Callable]): A callback to trigger when the field value changes.
            value (Optional[str]): The initial value of the entry field.
            **kwargs: Additional keyword arguments passed to widget constructors.

        Returns:
            None
        """

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
        Returns the clear button widget.

        Returns:
            tkinter.Button: The button widget used to clear the entry and reset the checkbox.
        """

        # Return the tkinter.Button widget
        return self._button

    @property
    def checkbutton(self) -> tkinter.Checkbutton:
        """
        Returns the checkbutton widget.

        Returns:
            tkinter.Checkbutton: The checkbutton indicating whether the entry is a correct answer.
        """

        # Return the tkinter.Checkbutton widget
        return self._checkbutton

    @property
    def checkbutton_label(self) -> tkinter.Label:
        """
        Returns the label describing the checkbutton.

        Returns:
            tkinter.Label: The label widget showing e.g., "Is correct?".
        """

        # Return the tkinter.Label widget
        return self._checkbutton_label

    @property
    def entry(self) -> tkinter.Entry:
        """
        Returns the entry widget for the answer text.

        Returns:
            tkinter.Entry: The entry widget where the user types the answer.
        """

        # Return the tkinter.Entry widget
        return self._entry

    @property
    def label(self) -> tkinter.Label:
        """
        Returns the main label widget for the field.

        Returns:
            tkinter.Label: The label widget describing this answer field.
        """

        # Return the tkinter.Label widget
        return self._label

    def _on_variable_change(self) -> None:
        """
        Handles internal variable change events.

        This method is called when either the entry's text or the checkbox's value changes.
        It dispatches an event and optionally calls the user-defined on_change_callback.

        Returns:
            None
        """

        # Get the label and value of the multi select answer field
        (
            label,
            value,
        ) = (
            self.display_name,
            (
                self.string_variable.get(),
                self.boolean_variable.get(),
            ),
        )

        # Dispatch the MULTI_SELECT_ANSWER_FIELD_CHANGED event
        self.dispatcher.dispatch(
            event=Events.MULTI_SELECT_ANSWER_FIELD_CHANGED,
            label=self.display_name,
            namespace=self.namespace,
            value=value,
        )

        # Check, if the on_change_callback is present
        if self.on_change_callback:
            # Call the on_change_callback function with the new value
            self.on_change_callback(
                label,
                value,
            )

    def clear(
        self,
        dispatch: bool = False,
    ) -> None:
        """
        Clears the field by resetting the entry and checkbutton to default values.

        This method sets the entry text to an empty string and the checkbox to False.
        If dispatch is True, a MULTI_SELECT_ANSWER_FIELD_CLEARED event is dispatched.

        Args:
            dispatch (bool): Whether to dispatch an event after clearing the field.

        Returns:
            None
        """

        # Set the value of the string variable to an empty string
        self.string_variable.set(value="")

        # Set the value of the boolean variable to False
        self.boolean_variable.set(value=False)

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the MULTI_SELECT_ANSWER_FIELD_CLEARED event
            self.dispatcher.dispatch(
                event=Events.MULTI_SELECT_ANSWER_FIELD_CLEARED,
                label=self.display_name,
                namespace=self.namespace,
                value=(
                    self.string_variable.get(),
                    self.boolean_variable.get(),
                ),
            )

    def configure_button(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the button widget in the multi select answer field.

        This method configures the button widget in the multi select answer field
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
            # Attempt to configure the button widget with the provided arguments
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

    def configure_checkbutton(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the checkbutton widget in the multi select answer field.

        This method configures the checkbutton widget in the multi select answer field
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
            # Attempt to configure the checkbutton widget with the provided arguments
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

    def configure_checkbutton_label(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the 'checkbutton label' label widget in the multi select answer field.

        This method configures the 'checkbutton label' label widget in the multi select answer field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the 'checkbutton label' label widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                'checkbutton label' label widget.
        """
        try:
            # Attempt to configure the 'checkbutton label' label widget with the provided arguments
            self._checkbutton_label.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_checkbutton_label' method from '{self.__class__.__name__}' class: {e}"
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
        Configures the entry widget in the multi select answer field.

        This method configures the entry widget in the multi select answer field
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
        Configures the grid layout for the internal widgets.

        This method sets the weight of each grid column and row to ensure
        proper resizing behavior of the MultiSelectAnswerField. The entry field
        is given a higher weight to expand horizontally, while other widgets
        remain fixed in size.

        Returns:
            None
        """

        # Configure the weight of the 0th column to 0
        self.grid_columnconfigure(
            index=0,
            weight=0,
        )

        # Configure the weight of the 1st column to 0
        self.grid_columnconfigure(
            index=1,
            weight=0,
        )

        # Configure the weight of the 2nd column to 0
        self.grid_columnconfigure(
            index=2,
            weight=0,
        )

        # Configure the weight of the 3rd column to 1
        self.grid_columnconfigure(
            index=3,
            weight=1,
        )

        # Configure the weight of the 4th column to 0
        self.grid_columnconfigure(
            index=4,
            weight=0,
        )

        # Configure the weight of the 0th row to 0
        self.grid_rowconfigure(
            index=0,
            weight=0,
        )

    def configure_label(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the label widget in the multi select answer field.

        This method configures the label widget in the multi select answer field
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

    def create_widgets(
        self,
        display_name: str,
        **kwargs,
    ) -> None:
        """
        Creates and places all internal widgets used in the field.

        This includes a label, checkbutton with label, entry field, and a clear button.
        It also binds the variables and sets up the internal state of the widget.

        Args:
            label (str): The text to display for the label.
            **kwargs: Optional configuration for individual widgets.

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

        # Place the tkinter.Label widget in the grid
        self._label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a 'checkbutton label' tkinter.Label widget
        self._checkbutton_label: tkinter.Label = tkinter.Label(
            master=self,
            text="Is correct? ",
            **kwargs.get(
                "checkbutton_label",
                {},
            ),
        )

        # Place the tkinter.Label widget in the grid
        self._checkbutton_label.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a BooleanVar to hold the entry value
        self.boolean_variable: tkinter.BooleanVar = tkinter.BooleanVar(value=False)

        # Create a tkinter.Checkbutton widget
        self._checkbutton: tkinter.Checkbutton = tkinter.Checkbutton(
            master=self,
            text=f"{self.boolean_variable.get()}",
            variable=self.boolean_variable,
            **kwargs.get(
                "checkbutton",
                {},
            ),
        )

        # Place the tkinter.Checkbutton widget in the grid
        self._checkbutton.grid(
            column=2,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a StringVar to hold the entry value
        self.string_variable: tkinter.StringVar = tkinter.StringVar(value="")

        # Add a trace to the variable
        self.string_variable.trace_add(
            callback=lambda *args: self._on_variable_change(),
            mode="write",
        )

        # Create a tkinter.Entry widget
        self._entry: tkinter.Entry = tkinter.Entry(
            master=self,
            textvariable=self.string_variable,
            **kwargs.get(
                "entry",
                {},
            ),
        )

        # Place the tkinter.Entry widget in the grid
        self._entry.grid(
            column=3,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a tkinter.Button widget
        self._button: tkinter.Button = tkinter.Button(
            command=lambda: self.clear(dispatch=True),
            master=self,
            text="X",
            **kwargs.get(
                "button",
                {},
            ),
        )

        # Place the tkinter.Button widget in the grid
        self._button.grid(
            column=4,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

    def get(
        self,
        dispatch: bool = False,
    ) -> Tuple[str, Any]:
        """
        Retrieves the current state of the field.

        Args:
            dispatch (bool): If True, an event is dispatched after reading the value.

        Returns:
            Tuple[str, Tuple[str, bool]]: The label and a tuple of (entry text, checkbox value).
        """

        # Get the label and value of the multi select answer field
        (
            label,
            value,
        ) = (
            self.display_name,
            (
                self.string_variable.get(),
                self.boolean_variable.get(),
            ),
        )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the MULTI_SELECT_ANSWER_FIELD_GET
            self.dispatcher.dispatch(
                event=Events.MULTI_SELECT_ANSWER_FIELD_GET,
                label=self.display_name,
                namespace=self.namespace,
                value=value,
            )

        # Return the text of the label and the value of the text field
        return (
            label,
            value,
        )

    def set(
        self,
        value: Tuple[str, Optional[bool]],
        dispatch: bool = False,
    ) -> None:
        """
        Sets the current state of the field.

        Args:
            value (Tuple[str, Optional[bool]]): A tuple of entry text and checkbox state.
            dispatch (bool): If True, an event is dispatched after setting the value.

        Returns:
            None
        """

        # Set the string value of the multi select answer field
        self.string_variable.set(value=value[0])

        # Check, if the value has a second (the optional bool) value
        if len(value) == 2:
            # Set the boolean value of the multi select answer field
            self.boolean_variable.set(value=value[1])

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the MULTI_SELECT_ANSWER_FIELD_SET
            self.dispatcher.dispatch(
                event=Events.MULTI_SELECT_ANSWER_FIELD_SET,
                label=self.display_name,
                namespace=self.namespace,
                value=(
                    self.string_variable.get(),
                    self.boolean_variable.get(),
                ),
            )


class MultipleSelectResponseField(BaseField):
    """ """

    pass


class MultiLineTextField(BaseField):
    """
    A multi line text field widget.

    This class represents a multi line text field with a label, text, scrollbar, and clear button.
    It provides methods to configure and interact with the widgets, as well as a callback
    for handling changes in the text field's value.
    """

    def __init__(
        self,
        display_name: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, str], None]] = None,
        value: Optional[str] = None,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the SingleLineTextField class.

        Args:
            display_name (str): The string to display for the field.
            master (tkinter.Misc): The master widget.
            namespace (str, optional): The namespace for the multi line text field. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[str, str], None]], optional): The callback function to be called when the value of the multi line text field changes. Defaults to None.
            value (Optional[str], optional): The initial value of the multi line text field. Defaults to None.
            kwargs: Additional keyword arguments
        """

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
        Returns the button widget.

        This property provides access to the button widget associated with the multi line text field.

        Returns:
            tkinter.Button: The button widget.
        """
        return self._button

    @property
    def horizontal_scrollbar(self) -> tkinter.Scrollbar:
        """
        Returns the (horizontal) scrollbar widget.

        This property provides access to the (horizontal) scrollbar widget associated with the multi line text field.

        Returns:
            tkinter.Scrollbar: The (horizontal) scrollbar widget.
        """
        return self._horizontal_scrollbar

    @property
    def label(self) -> tkinter.Label:
        """
        Returns the label widget.

        This property provides access to the label widget associated with the multi line text field.

        Returns:
            tkinter.Label: The label widget.
        """
        return self._label

    @property
    def text(self) -> tkinter.Text:
        """
        Returns the text widget.

        This property provides access to the text widget associated with the multi line text field.

        Returns:
            tkinter.Text: The text widget.
        """
        return self._text

    @property
    def vertical_scrollbar(self) -> tkinter.Scrollbar:
        """
        Returns the (vertical) scrollbar widget.

        This property provides access to the (vertical) scrollbar widget associated with the multi line text field.

        Returns:
            tkinter.Scrollbar: The (vertical) scrollbar widget.
        """
        return self._vertical_scrollbar

    def _on_mousewheel(
        self,
        event: tkinter.Event,
    ) -> None:
        """
        Handles mouse wheel scrolling for the text widget.
        This method scrolls the text widget vertically.

        Args:
            event (tkinter.Event): The mouse wheel event.
        """

        # Windows + Linux
        if event.num == 4 or event.delta > 0:
            self.text.yview_scroll(
                number=-1,
                what="units",
            )
        elif event.num == 5 or event.delta < 0:
            self.text.yview_scroll(
                number=1,
                what="units",
            )

    def _bind_mousewheel(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        Binds the mouse wheel event to the text widget.

        This method binds the mouse wheel event to the text widget, allowing scrolling with the mouse wheel.

        Args:
            event (Optional[tkinter.Event], optional): The mouse wheel event. Defaults to None.
        """

        # Check, if the current plattform is one of "winddows", "MacOS" or "Linux"
        if platform.system() == "Windows":
            # Bind the mouse wheel event for Windows
            self.text.bind(
                sequence="<MouseWheel>",
                func=self._on_mousewheel,
            )
        elif platform.system() == "Darwin":  # macOS
            # Bind the mouse wheel event for macOS
            self.text.bind(
                sequence="<MouseWheel>",
                func=self._on_mousewheel,
            )
        else:  # Linux (X11)
            # Bind the mouse wheel event for Linux (X11)
            self.text.bind(
                sequence="<Button-4>",
                func=self._on_mousewheel,
            )
            self.text.bind(
                sequence="<Button-5>",
                func=self._on_mousewheel,
            )

    def _unbind_mousewheel(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        Unbinds the mouse wheel event from the text widget.

        This method unbinds the mouse wheel event from the text widget.

        Args:
            event (Optional[tkinter.Event], optional): The mouse wheel event. Defaults to None.
        """

        # Unbind the mouse wheel event from the text widget
        if platform.system() == "Windows":
            self.text.unbind(sequence="<MouseWheel>")  # Windows
        elif platform.system() == "Darwin":  # macOS
            self.text.unbind(sequence="<MouseWheel>")  # macOS
        else:  # Linux (X11)
            self.text.unbind(sequence="<Button-4>")  # Linux (X11)
            self.text.unbind(sequence="<Button-5>")  # Linux (X11)

    def _on_text_change(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        This method is called when the value of the multi line text field changes.

        It dispatches the MULTI_LINE_TEXT_FIELD_CHANGED event and calls the on_change_callback function with the new label and value.

        Args:
            event (tkinter.Event, optional): The event passed to this method.

        Returns:
            None
        """

        # Get the label and value of the multi line text field
        (
            label,
            value,
        ) = (
            self.display_name,
            self.text.get(
                index1="1.0",
                index2="end-1c",
            ).strip(),
        )

        # Dispatch the MULTI_LINE_TEXT_FIELD_CHANGED event
        self.dispatcher.dispatch(
            event=Events.MULTI_LINE_TEXT_FIELD_CHANGED,
            label=self.display_name,
            namespace=self.namespace,
            value=value,
        )

        # Check, if the on_change_callback is present
        if self.on_change_callback:
            # Call the on_change_callback function with the new value
            self.on_change_callback(
                label,
                value,
            )

    @override
    def clear(
        self,
        dispatch: bool = False,
    ) -> None:
        """
        Clears the multi line text field.

        This method clears the multi line text field by deleting its value..

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            None
        """

        # Delete the contents of the tkinter.Text widget
        self.text.delete(
            index1="1.0",
            index2="end-1c",
        )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the MULTI_LINE_TEXT_FIELD_CLEARED event
            self.dispatcher.dispatch(
                event=Events.MULTI_LINE_TEXT_FIELD_CLEARED,
                label=self.display_name,
                namespace=self.namespace,
                value=self.text.get(
                    index1="1.0",
                    index2="end-1c",
                ).strip(),
            )

    def configure_button(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the button widget in the multi line text field.

        This method configures the button widget in the multi line text field
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

    @override
    def configure_grid(self) -> None:
        """
        Configures the grid of the multi line text field widget.

        This method configures the grid of the multi line text field widget
        by setting the weights of the columns and rows.

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

        # Set the weight of the 1st row to 1
        # This means that the row will stretch when the window is resized
        self.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Set the weight of the 2nd row to 0
        # This means that the row will not stretch when the window is resized
        self.grid_rowconfigure(
            index=2,
            weight=0,
        )

    def configure_label(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the label widget in the multi line text field.

        This method configures the label widget in the multi line text field
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

    def configure_scrollbar(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the scrollbar widget in the multi line text field.

        This method configures the scrollbar widget in the multi line text field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the scrollbar widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                scrollbar widget.
        """
        try:
            # Attempt to configure the scrollbar widget with the provided arguments
            self.scrollbar.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_scrollbar' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_text(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the text widget in the multi line text field.

        This method configures the text widget in the multi line text field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the text widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                text widget.
        """
        try:
            # Attempt to configure the text widget with the provided arguments
            self.text.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_text' method from '{self.__class__.__name__}' class: {e}"
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
        Creates and configures the widgets for the multi line text field.

        This method initializes the label, text, scrollbar, and button widgets for the
        multi line text field, setting their layout configuration.

        Args:
            label (str): The text for the label widget.
            **kwargs: Additional keyword arguments for the widgets.

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

        # Place the label widget in the grid
        self._label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a text widget
        self._text: tkinter.Text = tkinter.Text(
            master=self,
            **kwargs.get(
                "text",
                {},
            ),
        )

        # Bind mouse wheel-scrolling (Windows / Linux / MacOS)
        self._text.bind(
            func=self._bind_mousewheel,
            sequence="<Enter>",
        )
        self._text.bind(
            func=self._unbind_mousewheel,
            sequence="<Leave>",
        )

        # Bind the 'on_text_change' method the tkinter.Text widget via the '<KeyRelease>' event
        self._text.bind(
            func=self._on_text_change,
            sequence="<KeyRelease>",
        )

        # Place the text widget in the grid
        self._text.grid(
            column=1,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )

        # Create a (vertical) scrollbar widget
        self._vertical_scrollbar: tkinter.Scrollbar = tkinter.Scrollbar(
            master=self,
            orient=VERTICAL,
            **kwargs.get(
                "scrollbar",
                {},
            ),
        )

        # Configure the tkinter.Scrollbar widget's yscrollcommand attribute
        self._text.config(yscrollcommand=self._vertical_scrollbar.set)

        # Configure the tkinter.Scrollbar widget's command attribute
        self._vertical_scrollbar.config(command=self._text.yview)

        # Place the (vertical) scrollbar widget in the grid
        self._vertical_scrollbar.grid(
            column=2,
            padx=5,
            pady=5,
            row=1,
            sticky=NS,
        )

        # Create a (horizontal) scrollbar widget
        self._horizontal_scrollbar: tkinter.Scrollbar = tkinter.Scrollbar(
            master=self,
            orient=HORIZONTAL,
            **kwargs.get(
                "scrollbar",
                {},
            ),
        )

        # Configure the tkinter.Scrollbar widget's xscrollcommand attribute
        self._text.config(xscrollcommand=self._horizontal_scrollbar.set)

        # Configure the tkinter.Scrollbar widget's command attribute
        self._horizontal_scrollbar.config(command=self._text.xview)

        # Place the (horizontal) scrollbar widget in the grid
        self._horizontal_scrollbar.grid(
            column=1,
            padx=5,
            pady=5,
            row=2,
            sticky=EW,
        )

        # Create a button widget
        self._button: tkinter.Button = tkinter.Button(
            command=lambda: self.clear(dispatch=True),
            master=self,
            text="X",
            **kwargs.get(
                "button",
                {},
            ),
        )

        # Place the button widget in the grid
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
    ) -> Tuple[str, str]:
        """
        Retrieves the text of the label and the value of the text field.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            Tuple[str, str]: A tuple containing the text of the label and the value of the text field.
        """

        # Obtain the label and value strings from the widgets
        (
            label,
            value,
        ) = (
            self.display_name,
            self.text.get(
                index1="1.0",
                index2="end-1c",
            ).strip(),
        )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the MULTI_LINE_TEXT_FIELD_GET
            self.dispatcher.dispatch(
                event=Events.MULTI_LINE_TEXT_FIELD_GET,
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
        value: str,
        dispatch: bool = False,
    ) -> None:
        """
        Sets the value of the text field.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.
            value (str): The value to set for the text field.

        Returns:
            None
        """

        # Delete the contents of the tkinter.Text widget
        self.text.delete(
            index1="1.0",
            index2="end-1c",
        )

        # Insert the passed value string into the tkinter.Text widget
        self.text.insert(
            chars=value,
            index="1.0",
        )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the MULTI_LINE_TEXT_FIELD_SET
            self.dispatcher.dispatch(
                event=Events.MULTI_LINE_TEXT_FIELD_SET,
                label=self.display_name,
                namespace=self.namespace,
                value=self.text.get(
                    index1="1.0",
                    index2="end-1c",
                ).strip(),
            )


class ReadOnlyMultiLineTextField(MultiLineTextField):
    """
    A read-only multi line text field widget.

    This class represents a multi line text field that cannot be edited by the user.
    It provides methods to configure and interact with the widgets, as well as a callback
    for handling changes in the text field's value.
    """

    def __init__(
        self,
        display_name: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, str], None]] = None,
        value: Optional[str] = None,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the ReadOnlyMultiLineTextField class.

        Args:
            display_name (str): The string to display for the field.
            master (tkinter.Misc): The master widget.
            namespace (str, optional): The namespace for the text field. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[str, str], None]], optional): The callback function to be called when the value of the text field changes. Defaults to None.
            value (Optional[str], optional): The initial value of the text field. Defaults to None.
            kwargs: Additional keyword arguments for the widgets.
        """

        # Call the parent class constructor with the passed arguments
        super().__init__(
            display_name=display_name,
            master=master,
            namespace=namespace,
            on_change_callback=on_change_callback,
            value=value,
            **kwargs,
        )

        # Configure the text widget to be read-only
        self._text.configure(state=DISABLED)

    @override
    def clear(
        self,
        dispatch: bool = False,
    ) -> None:
        """
        Prevents clearing of the text field.

        This method raises an error because the ReadOnlyField cannot be cleared
        after initialization.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Raises:
            ValueError: If the ReadOnlyField is attempted to be cleared.
        """

        # Raise an error to indicate that the field cannot be cleared
        raise ValueError(
            f"{self.__class__.__name__} cannot be modified after initialization."
        )

    @override
    def get(
        self,
        dispatch: bool = False,
    ) -> Tuple[str, str]:
        """
        Retrieves the text of the label and the value of the text field.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            Tuple[str, str]: A tuple containing the text of the label and the value of the text field.
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
            # Dispatch the READONLY_FIELD_GET event
            self.dispatcher.dispatch(
                event=Events.READONLY_MULTI_LINE_TEXT_FIELD_GET,
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
        value: str,
        dispatch: bool = False,
    ) -> None:
        """
        Raises an error because the ReadOnlyField cannot be modified after initialization.

        Args:
            value (str): The value to be set for the text field.
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Raises:
            ValueError: If the ReadOnlyField is modified after initialization.
        """

        # Raise an error to indicate that the field cannot be modified
        raise ValueError(
            f"{self.__class__.__name__} cannot be modified after initialization."
        )


class SearchbarField(BaseField):
    """ """

    def __init__(
        self,
        display_name: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, str], None]] = None,
        value: Optional[str] = None,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the SearchbarField class.

        Args:
            display_name (str): The string to display for the field.
            master (tkinter.Misc): The master widget.
            namespace (str, optional): The namespace for the search bar field. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[str, str], None]], optional): The callback function to be called when the value of the search bar field changes. Defaults to None.
            value (Optional[str], optional): The initial value of the search bar field. Defaults to None.
            kwargs: Additional keyword arguments.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            display_name,
            master,
            namespace,
            on_change_callback,
            value,
            **kwargs,
        )

    @property
    def button(self) -> tkinter.Button:
        """
        Returns the button widget.

        Args:
            None

        Returns:
            tkinter.Button: The button widget.
        """

        # Return the button widget
        return self._button

    @property
    def entry(self) -> tkinter.Entry:
        """
        Returns the entry widget.

        Args:
            None

        Returns:
            tkinter.Entry: The entry widget.
        """

        # Return the entry widget
        return self._entry

    @property
    def label(self) -> tkinter.Label:
        """
        Returns the label widget.

        Args:
            None

        Returns:
            tkinter.Label: The label widget.
        """

        # Return the label widget
        return self._label

    def _on_button_click(self) -> None:
        """
        This method is called when the button is clicked.

        It dispatches the SEARCH_BAR_FIELD_CLICKED event.

        Args:
            None

        Returns:
            None
        """

        # Get the label and value of the single line text field
        (
            label,
            value,
        ) = (
            self.display_name,
            self.variable.get(),
        )

        # Dispatch the SEARCH_BAR_FIELD_CLICKED event
        self.dispatcher.dispatch(
            event=Events.SEARCH_BAR_FIELD_CLICKED,
            label=label,
            namespace=self.namespace,
            value=value,
        )

    def _on_variable_change(self) -> None:
        """
        This method is called when the value of the search bar field changes.

        It dispatches the SEARCH_BAR_FIELD_CHANGED event and calls the on_change_callback function with the new label and value.

        Args:
            None

        Returns:
            None
        """

        # Get the label and value of the single line text field
        (
            label,
            value,
        ) = (
            self.display_name,
            self.variable.get(),
        )

        # Dispatch the SEARCH_BAR_FIELD_CHANGED event
        self.dispatcher.dispatch(
            event=Events.SEARCH_BAR_FIELD_CHANGED,
            label=label,
            namespace=self.namespace,
            value=value,
        )

        # Check, if the on_change_callback is present
        if self.on_change_callback:
            # Call the on_change_callback function with the new value
            self.on_change_callback(
                label,
                value,
            )

    @override
    def clear(
        self,
        dispatch: bool = False,
    ) -> None:
        """
        Clears the search bar field.

        This method clears the search bar field by setting its value to an empty string.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            None
        """

        # Set the value of the variable to an empty string
        self.variable.set(value="")

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the SEARCH_BAR_FIELD_CLEARED event
            self.dispatcher.dispatch(
                event=Events.SEARCH_BAR_FIELD_CLEARED,
                label=self.display_name,
                namespace=self.namespace,
                value=self.variable.get(),
            )

    def configure_button(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the button widget in the search bar field.

        This method configures the button widget in the search bar field
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

    def configure_entry(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the entry widget in the search bar field.

        This method configures the entry widget in the search bar field
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
            self.entry.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_entry' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @override
    def configure_grid(self) -> None:
        """
        Configures the grid for the search bar field.

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

    def configure_label(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the label widget in the search bar field.

        This method configures the label widget in the search bar field
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

    @override
    def create_widgets(
        self,
        display_name: str,
        **kwargs,
    ) -> None:
        """
        Creates the widgets for the search bar field.

        Args:
            display_name (str): The string to display for the field.
            **kwargs: Additional keyword arguments.

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

        # Place the tkinter.Label widget in the grid
        self._label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a StringVar to hold the entry value
        self.variable: tkinter.StringVar = tkinter.StringVar(value="")

        # Add a trace to the variable
        self.variable.trace_add(
            callback=lambda *args: self._on_variable_change(),
            mode="write",
        )

        # Create a tkinter.Entry widget
        self._entry: tkinter.Entry = tkinter.Entry(
            master=self,
            textvariable=self.variable,
            **kwargs.get(
                "entry",
                {},
            ),
        )

        # Place the tkinter.Entry widget in the grid
        self._entry.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a tkinter.Button widget
        self._button: tkinter.Button = tkinter.Button(
            master=self,
            text="Search",
            **kwargs.get("button", {}),
        )

        # Place the tkinter.Button widget in the grid
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
    ) -> Tuple[str, str]:
        """
        Retrieves the text of the label and the value of the search bar field.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            Tuple[str, str]: A tuple containing the text of the label and the value of the text field.
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
            # Dispatch the SEARCH_BAR_FIELD_GET event
            self.dispatcher.dispatch(
                event=Events.SEARCH_BAR_FIELD_GET,
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
        value: str,
        dispatch: bool = False,
    ) -> None:
        """
        Sets the value of the search bar field.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.
            value (str): The value to set for the search bar field.

        Returns:
            None
        """

        # Set the value of the search bar field
        self.variable.set(value=value)

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the SEARCH_BAR_FIELD_SET event
            self.dispatcher.dispatch(
                event=Events.SEARCH_BAR_FIELD_SET,
                label=self.display_name,
                namespace=self.namespace,
                value=self.variable.get(),
            )


class SingleLineTextField(BaseField):
    """
    A single line text field widget.

    This class represents a single line text field with a label, entry, and clear button.
    It provides methods to configure and interact with the widgets, as well as a callback
    for handling changes in the text field's value.
    """

    def __init__(
        self,
        display_name: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, str], None]] = None,
        value: Optional[str] = None,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the SingleLineTextField class.

        Args:
            display_name (str): The string to display for the field.
            master (tkinter.Misc): The master widget.
            namespace (str, optional): The namespace for the single line text field. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[str, str], None]], optional): The callback function to be called when the value of the single line text field changes. Defaults to None.
            value (Optional[str], optional): The initial value of the single line text field. Defaults to None.
            kwargs: Additional keyword arguments.
        """

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
        Returns the button widget.

        This property provides access to the button widget associated with the single line text field.

        Returns:
            tkinter.Button: The button widget.
        """
        return self._button

    @property
    def entry(self) -> tkinter.Entry:
        """
        Returns the entry widget.

        This property provides access to the entry widget associated with the single line text field.

        Returns:
            tkinter.Entry: The entry widget.
        """
        return self._entry

    @property
    def label(self) -> tkinter.Label:
        """
        Returns the label widget.

        This property provides access to the label widget associated with the single line text field.

        Returns:
            tkinter.Label: The label widget.
        """
        return self._label

    def _on_variable_change(self) -> None:
        """
        This method is called when the value of the single line text field changes.

        It dispatches the SINGLE_LINE_TEXT_FIELD_CHANGED event and calls the on_change_callback function with the new label and value.

        Returns:
            None
        """

        # Get the label and value of the single line text field
        (
            label,
            value,
        ) = (
            self.display_name,
            self.variable.get(),
        )

        # Dispatch the SINGLE_LINE_TEXT_FIELD_CHANGED event
        self.dispatcher.dispatch(
            event=Events.SINGLE_LINE_TEXT_FIELD_CHANGED,
            label=self.display_name,
            namespace=self.namespace,
            value=value,
        )

        # Check, if the on_change_callback is present
        if self.on_change_callback:
            # Call the on_change_callback function with the new value
            self.on_change_callback(
                label,
                value,
            )

    @override
    def clear(
        self,
        dispatch: bool = False,
    ) -> None:
        """
        Clears the single line text field.

        This method clears the single line text field by setting its value to an empty string.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            None
        """

        # Set the value of the variable to an empty string
        self.variable.set(value="")

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the SINGLE_LINE_TEXT_FIELD_CLEARED event
            self.dispatcher.dispatch(
                event=Events.SINGLE_LINE_TEXT_FIELD_CLEARED,
                label=self.display_name,
                namespace=self.namespace,
                value=self.variable.get(),
            )

    def configure_button(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the button widget in the single line text field.

        This method configures the button widget in the single line text field
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

    def configure_entry(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the entry widget in the single line text field.

        This method configures the entry widget in the single line text field
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
            self.entry.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_entry' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @override
    def configure_grid(self) -> None:
        """
        Configures the grid of the single line text field widget.

        This method configures the grid of the single line text field widget
        by setting the weights of the columns and rows.

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

        # Set the weight of the 0th row to 1
        # This means that the row will stretch when the window is resized
        self.grid_rowconfigure(
            index=0,
            weight=1,
        )

    def configure_label(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the label widget in the single line text field.

        This method configures the label widget in the single line text field
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

    @override
    def create_widgets(
        self,
        display_name: str,
        **kwargs,
    ) -> None:
        """
        Creates and configures the widgets for the single line text field.

        This method initializes the label, entry, and button widgets for the
        single line text field, setting their layout configuration.

        Args:
            label (str): The text for the label widget.
            **kwargs: Additional keyword arguments for the widgets.

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

        # Place the label widget in the grid
        self._label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a StringVar to hold the entry value
        self.variable: tkinter.StringVar = tkinter.StringVar(value="")

        # Add a trace to the variable
        self.variable.trace_add(
            callback=lambda *args: self._on_variable_change(),
            mode="write",
        )

        # Create an entry widget
        self._entry: tkinter.Entry = tkinter.Entry(
            master=self,
            textvariable=self.variable,
            **kwargs.get(
                "entry",
                {},
            ),
        )

        # Place the entry widget in the grid
        self._entry.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a button widget
        self._button: tkinter.Button = tkinter.Button(
            command=lambda: self.clear(dispatch=True),
            master=self,
            text="X",
            **kwargs.get(
                "button",
                {},
            ),
        )

        # Place the button widget in the grid
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
    ) -> Tuple[str, str]:
        """
        Retrieves the text of the label and the value of the text field.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            Tuple[str, str]: A tuple containing the text of the label and the value of the text field.
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
            # Dispatch the SINGLE_LINE_TEXT_FIELD_GET
            self.dispatcher.dispatch(
                event=Events.SINGLE_LINE_TEXT_FIELD_GET,
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
        value: str,
        dispatch: bool = False,
    ) -> None:
        """
        Sets the value of the text field.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.
            value (str): The value to set for the text field.

        Returns:
            None
        """

        # Set the value of the text field
        self.variable.set(value=value)

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the SINGLE_LINE_TEXT_FIELD_SET
            self.dispatcher.dispatch(
                event=Events.SINGLE_LINE_TEXT_FIELD_SET,
                label=self.display_name,
                namespace=self.namespace,
                value=self.variable.get(),
            )


class PasswordTextField(SingleLineTextField):
    """
    A password text field widget.

    The PasswordTextField class is a widget that shows a label and a text
    field for entering a password. It is a subclass of the SingleLineTextField
    class and inherits all of its methods and properties.

    The PasswordTextField class is configured to show asterisks (\*) instead
    of the actual characters entered, in order to hide the password from the
    user.
    """

    def __init__(
        self,
        display_name: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, str], None]] = None,
        value: Optional[str] = None,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the PasswordTextField class.

        Args:
        display_name (str): The string to display for the field.
        master (tkinter.Misc): The master widget.
        namespace (str, optional): The namespace for the password text field. Defaults to Constants.GLOBAL_NAMESPACE.
        on_change_callback (Optional[Callable[[str, str], None]], optional): The callback function to be called when the value of the password text field changes. Defaults to None.
        value (Optional[str], optional): The initial value of the password text field. Defaults to None.
        kwargs: Additional keyword arguments.
        """

        # Call the parent class constructor with the passed arguments
        super().__init__(
            display_name=display_name,
            master=master,
            namespace=namespace,
            on_change_callback=on_change_callback,
            value=value,
            **kwargs,
        )

        # Configure the entry widget to hide input with asterisks
        self._entry.configure(show="*")

    @override
    def clear(
        self,
        dispatch: bool = False,
    ) -> None:
        """
        Clears the single line text field.

        This method clears the single line text field by setting its value to an empty string.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            None
        """

        # Set the value of the variable to an empty string
        self.variable.set(value="")

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the PASSWORD_TEXT_FIELD_CHANGED event
            self.dispatcher.dispatch(
                event=Events.PASSWORD_TEXT_FIELD_CHANGED,
                label=self.display_name,
                namespace=self.namespace,
                value=self.variable.get(),
            )

    @override
    def get(
        self,
        dispatch: bool = False,
    ) -> Tuple[str, str]:
        """
        Retrieves the text of the label and the value of the text field.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            Tuple[str, str]: A tuple containing the text of the label and the value of the text field.
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
            # Dispatch the PASSWORD_TEXT_FIELD_GET event
            self.dispatcher.dispatch(
                event=Events.PASSWORD_TEXT_FIELD_GET,
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
        value: str,
        dispatch: bool = False,
    ) -> None:
        """
        Sets the value of the text field.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.
            value (str): The value to set for the text field.

        Returns:
            None
        """

        # Set the value of the text field
        self.variable.set(value=value)

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the PASSWORD_TEXT_FIELD_SET event
            self.dispatcher.dispatch(
                event=Events.PASSWORD_TEXT_FIELD_SET,
                label=self.display_name,
                namespace=self.namespace,
                value=self.variable.get(),
            )


class ReadOnlyMultiLineTextField(MultiLineTextField):
    """
    A read-only multi line text field widget.

    This class represents a multi line text field that cannot be edited by the user.
    It provides methods to configure and interact with the widgets, as well as a callback
    for handling changes in the text field's value.
    """

    def __init__(
        self,
        display_name: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, str], None]] = None,
        value: Optional[str] = None,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the ReadOnlyMultiLineTextField class.

        Args:
            display_name (str): The string to display for the field.
            master (tkinter.Misc): The master widget.
            namespace (str, optional): The namespace for the text field. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[str, str], None]], optional): The callback function to be called when the value of the text field changes. Defaults to None.
            value (Optional[str], optional): The initial value of the text field. Defaults to None.
            kwargs: Additional keyword arguments for the widgets.
        """

        # Call the parent class constructor with the passed arguments
        super().__init__(
            display_name=display_name,
            master=master,
            namespace=namespace,
            on_change_callback=on_change_callback,
            value=value,
            **kwargs,
        )

        # Configure the entry widget to be read-only
        self._entry.configure(state="readonly")

    @override
    def clear(
        self,
        dispatch: bool = False,
    ) -> None:
        """
        Prevents clearing of the text field.

        This method raises an error because the ReadOnlyField cannot be cleared
        after initialization.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Raises:
            ValueError: If the ReadOnlyField is attempted to be cleared.
        """

        # Raise an error to indicate that the field cannot be cleared
        raise ValueError(
            f"{self.__class__.__name__} cannot be modified after initialization."
        )

    @override
    def get(
        self,
        dispatch: bool = False,
    ) -> Tuple[str, str]:
        """
        Retrieves the text of the label and the value of the text field.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            Tuple[str, str]: A tuple containing the text of the label and the value of the text field.
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
            # Dispatch the READONLY_FIELD_GET event
            self.dispatcher.dispatch(
                event=Events.READONLY_MULTI_LINE_TEXT_FIELD_GET,
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
        value: str,
        dispatch: bool = False,
    ) -> None:
        """
        Raises an error because the ReadOnlyField cannot be modified after initialization.

        Args:
            value (str): The value to be set for the text field.
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Raises:
            ValueError: If the ReadOnlyField is modified after initialization.
        """

        # Check, if the tkinter.StringVar instance is empty
        if not self.text.get():
            # Set the value of the tkinter.StringVar instance
            self.text.insert(
                chars=value,
                index="1.0",
            )

            # Return early
            return

        # Raise an error to indicate that the field cannot be modified
        raise ValueError(
            f"{self.__class__.__name__} cannot be modified after initialization."
        )


class ReadOnlySingleLineTextField(SingleLineTextField):
    """
    A read-only single line text field widget.

    This class represents a single line text field that cannot be edited by the user.
    It provides methods to configure and interact with the widgets, as well as a callback
    for handling changes in the text field's value.
    """

    def __init__(
        self,
        display_name: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, str], None]] = None,
        value: Optional[str] = None,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the ReadOnlySingleLineTextField class.

        Args:
            display_name (str): The string to display for the field.
            master (tkinter.Misc): The master widget.
            namespace (str, optional): The namespace for the text field. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[str, str], None]], optional): The callback function to be called when the value of the text field changes. Defaults to None.
            value (Optional[str], optional): The initial value of the text field. Defaults to None.
            kwargs: Additional keyword arguments for the widgets.
        """

        # Call the parent class constructor with the passed arguments
        super().__init__(
            display_name=display_name,
            master=master,
            namespace=namespace,
            on_change_callback=on_change_callback,
            value=value,
            **kwargs,
        )

        # Configure the entry widget to be read-only
        self._entry.configure(state="readonly")

    @override
    def clear(
        self,
        dispatch: bool = False,
    ) -> None:
        """
        Prevents clearing of the text field.

        This method raises an error because the ReadOnlyField cannot be cleared
        after initialization.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Raises:
            ValueError: If the ReadOnlyField is attempted to be cleared.
        """

        # Raise an error to indicate that the field cannot be cleared
        raise ValueError(
            f"{self.__class__.__name__} cannot be modified after initialization."
        )

    @override
    def get(
        self,
        dispatch: bool = False,
    ) -> Tuple[str, str]:
        """
        Retrieves the text of the label and the value of the text field.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            Tuple[str, str]: A tuple containing the text of the label and the value of the text field.
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
            # Dispatch the READONLY_FIELD_GET event
            self.dispatcher.dispatch(
                event=Events.READONLY_SINGLE_LINE_TEXT_FIELD_GET,
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
        value: str,
        dispatch: bool = False,
    ) -> None:
        """
        Raises an error because the ReadOnlyField cannot be modified after initialization.

        Args:
            value (str): The value to be set for the text field.
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Raises:
            ValueError: If the ReadOnlyField is modified after initialization.
        """

        # Check, if the tkinter.StringVar instance is empty
        if not self.variable.get():
            # Set the value of the tkinter.StringVar instance
            self.variable.set(value=value)

            # Return early
            return

        # Raise an error to indicate that the field cannot be modified
        raise ValueError(
            f"{self.__class__.__name__} cannot be modified after initialization."
        )


class TextEditorFieldImageItem(MutableBaseObject):
    """
    Represents an image item within a text editor field.

    This class is responsible for handling an image and its position within the
    text editor field, allowing for the integration of image elements into the
    text content.

    Attributes:
        image (ImageTk.PhotoImage): The image to be displayed in the text editor.
        name (str): The name of the image.
        position (str): The position of the image within the text field.
    """

    def __init__(
        self,
        image: ImageTk.PhotoImage,
        name: str,
        position: str,
    ) -> None:
        """
        Initializes a new instance of the TextEditorFieldImageItem class with an image and its position.

        Args:
            image (ImageTk.PhotoImage): The image to be displayed.
                position (str): The position of the image within the field.

        Returns:
            None
        """

        # Call the parent class constructor with the passed arguments
        super().__init__(
            _image=image,
            _name=name,
            _position=position,
        )

    @property
    def image(self) -> ImageTk.PhotoImage:
        """
        Gets the image associated with the image item.

        Returns:
            ImageTk.PhotoImage: The image associated with the image item.
        """

        # Return the 'image' ImageTk.PhotoImage instance variable
        return self._image

    @image.setter
    def image(
        self,
        value: ImageTk.PhotoImage,
    ) -> None:
        """
        Raises an error because the TextEditorFieldImageItem cannot be modified after initialization.

        Args:
            value (ImageTk.PhotoImage): The new image to be displayed.

        Returns:
            None
        """

        raise ValueError(
            f"The 'image' instance variable of the {self.__class__.__name__} class cannot be modified after initialization."
        )

    @property
    def name(self) -> str:
        """
        Gets the name of the image.

        Returns:
            str: The name of the image.
        """

        # Return the 'name' string instance variable
        return self._name

    @name.setter
    def name(
        self,
        value: str,
    ) -> None:
        """
        Raises an error because the TextEditorFieldImageItem cannot be modified after initialization.

        Args:
            value (str): The new name of the image.

        Returns:
            None
        """

        raise ValueError(
            f"The 'name' instance variable of the {self.__class__.__name__} class cannot be modified after initialization."
        )

    @property
    def position(self) -> str:
        """
        Gets the position of the image within the text field.

        Returns:
            str: The position of the image within the text field.
        """

        # Return the 'position' string instance variable
        return self._position

    @position.setter
    def position(
        self,
        value: str,
    ) -> None:
        """
        Sets the position of the image within the text field.

        Args:
            value (str): The new position of the image within the text field.

        Returns:
            None
        """

        # Set the 'position' string instance variable
        self._position = value

    @override
    def __eq__(
        self,
        other: "TextEditorFieldImageItem",
    ) -> bool:
        """
        Checks if the current TextEditorFieldImageItem is equal to another.

        Args:
            other (TextEditorFieldImageItem): The other image item to compare against.

        Returns:
            bool: True if both image items have the same position, False otherwise.
        """

        # Check, if the 'other' argument is an instance of the TextEditorFieldImageItem class
        if not isinstance(
            other,
            TextEditorFieldImageItem,
        ):
            # Return NotImplemented indicating that the comparison is not supported
            return NotImplemented

        # Return True if the 'name' or 'position' string instance variables are equal, False otherwise
        return self.name == other.name or self.position == other.position


class TextEditorFieldTagItem(MutableBaseObject):
    """
    Represents a tag item within a text editor field.

    This class is responsible for handling a tag and its associated font
    configuration within the text editor field, allowing for the integration
    of styled text elements into the text content.

    Attributes:
        end (str): The end position of the tag within the text field.
        font_configuration (Dict[str, Any]): The font configuration associated with the tag.
        start (str): The start position of the tag within the text field.
        tag_name (str): The name of the tag.
    """

    def __init__(
        self,
        end: str,
        font_configuration: Dict[str, Any],
        start: str,
        tag_name: str,
    ) -> None:
        """
        Initializes a new instance of the TextEditorFieldTagItem class with an end position,
        font configuration, start position, and tag name.

        Args:
            end (str): The end position of the tag within the text field.
            font_configuration (Dict[str, Any]): The font configuration associated with the tag.
            start (str): The start position of the tag within the text field.
            tag_name (str): The name of the tag.

        Returns:
            None
        """

        # Call the parent class constructor with the passed arguments
        super().__init__(
            _end=end,
            _font_configuration=font_configuration,
            _start=start,
            _tag_name=tag_name,
        )

    @property
    def end(self) -> str:
        """
        Gets the end position of the tag within the text field.

        Returns:
            str: The end position of the tag within the text field.
        """

        # Return the 'end' string instance variable
        return self._end

    @end.setter
    def end(
        self,
        value: str,
    ) -> None:
        """
        Sets the end position of the tag within the text field.

        Args:
            value (str): The new end position of the tag within the text field.

        Returns:
            None
        """

        # Update the 'end' string instance variable
        self._end = value

    @property
    def font_configuration(self) -> Dict[str, Any]:
        """
        Gets the font configuration associated with the tag.

        Returns:
            Dict[str, Any]: The font configuration associated with the tag.
        """

        # Return the 'font_configuration' dictionary instance variable
        return self._font_configuration

    @font_configuration.setter
    def font_configuration(
        self,
        value: Dict[str, Any],
    ) -> None:
        """
        Raises an error because the TextEditorFieldTagItem cannot be modified after initialization.

        Args:
            value (Dict[str, Any]): The new font configuration.

        Returns:
            None
        """

        raise ValueError(
            f"The 'font_configuration' instance variable of the {self.__class__.__name__} class cannot be modified after initialization."
        )

    @property
    def start(self) -> str:
        """
        Gets the start position of the tag within the text field.

        Returns:
            str: The start position of the tag within the text field.
        """

        # Return the 'start' string instance variable
        return self._start

    @start.setter
    def start(
        self,
        value: str,
    ) -> None:
        """
        Sets the start position of the tag within the text field.

        Args:
            value (str): The new start position of the tag within the text field.

        Returns:
            None
        """

        # Update the 'start' string instance variable
        self._start = value

    @property
    def tag_name(self) -> str:
        """
        Gets the name of the tag.

        Returns:
            str: The name of the tag.
        """

        # Return the 'tag_name' string instance variable
        return self._tag_name

    @tag_name.setter
    def tag_name(
        self,
        value: str,
    ) -> None:
        """
        Raises an error because the TextEditorFieldTagItem cannot be modified after initialization.

        Args:
            value (str): The new tag name.

        Returns:
            None
        """

        raise ValueError(
            f"The 'tag_name' instance variable of the {self.__class__.__name__} class cannot be modified after initialization."
        )


class TextEditorField(BaseField):
    """
    A text editor field.

    This class represents a text editor field that allows users to edit and format text.
    It provides methods to configure and interact with the widgets, as well as a callback
    for handling changes in the text field's value.

    Attributes:
        clear_button (tkinter.Button): The clear button widget.
        text (tkinter.Text): The text widget.
        config_cache (Dict[str, Any]): The configuration cache dictionary.
        content_cache (Dict[str, Union[Set[Union[TextEditorFieldImageItem, TextEditorFieldTagItem]], str]]): The content cache dictionary.
        current_font (Optional[font.Font]): The current font.
        dispatcher (Dispatcher): The dispatcher object.
        display_name (str): The display name of the field.
        font_cache (Dict[str, font.Font]): The font cache dictionary.
        images (Dict[str, ImageTk.PhotoImage]): The images dictionary.
        namespace (str): The namespace for the field.
        on_change_callback (Optional[Callable[[str, str], None]]): The callback function to be called when the field value changes.
        value (Optional[str]): The value of the field.
    """

    def __init__(
        self,
        display_name: str,
        master: tkinter.Misc,
        config: Optional[Dict[str, Any]] = None,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, str], None]] = None,
        value: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the TextEditorField class.

        Args:
            config (Optional[Dict[str, Any]], optional): The configuration for the text editor field. Defaults to None.
            display_name (str): The display name of the field.
            master (tkinter.Misc): The parent widget.
            namespace (str, optional): The namespace for the field. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[str, str], None]], optional): The callback function to be called when the field value changes. Defaults to None.
            value (Optional[str], optional): The initial value of the field. Defaults to None.

        Returns:
            None
        """

        # Initialize the config cache dictionary instance variable as an empty dictionary
        self.config_cache: Dict[str, Any] = {
            "family": "default",
            "justify": "left",
            "overstrike": False,
            "size": 10,
            "slant": "roman",
            "underline": False,
            "weight": "normal",
        }

        # Check, if config is not empty
        if config:
            # Update the config cache
            self.config_cache.update(config)

        # Initialize the 'content cache' dictionary instance variable as an empty dictionary
        self._content_cache: Dict[
            str,
            Union[Set[Union[TextEditorFieldImageItem, TextEditorFieldTagItem]], str],
        ] = {
            "images": set(),
            "tags": set(),
            "text": "",
        }

        # Initialize the 'current font' (optional) Font object as a Font object
        self.current_font: Optional[font.Font] = font.Font(
            family=self.config_cache["family"],
            size=self.config_cache["size"],
            slant=self.config_cache["slant"],
            overstrike=self.config_cache["overstrike"],
            underline=self.config_cache["underline"],
            weight=self.config_cache["weight"],
        )

        # Initialize the font cache as an empty dictionary
        self.font_cache: Dict[str, font.Font] = {}

        # Initialize the images dictionary instance variable as an empty dictionary
        self.images: Dict[str, ImageTk.PhotoImage] = {}

        # Call the parent class constructor
        super().__init__(
            display_name=display_name,
            master=master,
            namespace=namespace,
            on_change_callback=on_change_callback,
            value=value,
        )

    @property
    def clear_button(self) -> tkinter.Button:
        """
        Gets the tkinter.Button widget associated with the text editor field.

        Returns:
            tkinter.Button: The tkinter.Button widget associated with the text editor field.
        """

        # Return the tkinter.Button widget to the caller
        return self._clear_button

    @property
    def content_cache(self) -> Dict[str, Any]:
        """
        Gets the content cache dictionary instance variable.

        Returns:
            Dict[str, Any]: The content cache dictionary instance variable.
        """

        # Return the content cache dictionary instance variable to the caller
        return {
            "images": [
                {
                    key.replace(
                        "_",
                        "",
                        1,
                    ): value
                    for (
                        key,
                        value,
                    ) in image.to_dict(exclude=["_logger"]).items()
                }
                for image in self._content_cache["images"]
            ],
            "tags": [
                {
                    key.replace(
                        "_",
                        "",
                        1,
                    ): value
                    for (
                        key,
                        value,
                    ) in tag.to_dict(exclude=["_logger"]).items()
                }
                for tag in self._content_cache["tags"]
            ],
            "text": self._content_cache["text"],
        }

    @property
    def horizontal_scrollbar(self) -> tkinter.Scrollbar:
        """
        Gets the tkinter.Scrollbar widget associated with the text editor field.

        Returns:
            tkinter.Scrollbar: The tkinter.Scrollbar widget associated with the text editor field.
        """

        # Return the tkinter.Scrollbar widget to the caller
        return self._horizontal_scrollbar

    @property
    def label(self) -> tkinter.Label:
        """
        Gets the tkinter.Label widget associated with the text editor field.

        Returns:
            tkinter.Label: The tkinter.Label widget associated with the text editor field.
        """

        # Return the tkinter.Label widget to the caller
        return self._label

    @property
    def text(self) -> tkinter.Text:
        """
        Gets the tkinter.Text widget associated with the text editor field.

        Returns:
            tkinter.Text: The tkinter.Text widget associated with the text editor field.
        """

        # Return the tkinter.Text widget to the caller
        return self._text

    @property
    def vertical_scrollbar(self) -> tkinter.Scrollbar:
        """
        Gets the tkinter.Scrollbar widget associated with the text editor field.

        Returns:
            tkinter.Scrollbar: The tkinter.Scrollbar widget associated with the text editor field.
        """

        # Return the tkinter.Scrollbar widget to the caller
        return self._vertical_scrollbar

    def _add_to_content_cache(
        self,
        image: Optional[TextEditorFieldImageItem] = None,
        tag: Optional[TextEditorFieldTagItem] = None,
        text: Optional[str] = None,
    ) -> None:
        """
        Adds the passed arguments to the content cache dictionary instance variable.

        Args:
            image (Optional[TextEditorFieldImageItem], optional): The image to be added to the content cache dictionary instance variable. Defaults to None.
            tag (Optional[TextEditorFieldTagItem], optional): The tag to be added to the content cache dictionary instance variable. Defaults to None.
            text (Optional[str], optional): The text to be added to the content cache dictionary instance variable. Defaults to None.

        Returns:
            None
        """

        # Check, if the 'image' argument has been passed
        if image:
            # Append the passed 'image' dictionary argument to the 'images' list in the content cache dictionary instance variable
            self._content_cache["images"].add(image)

        # Check, if the 'tag' argument has been passed
        if tag:
            # Append the passed 'tag' dictionary argument to the 'tags' list in the content cache dictionary instance variable
            self._content_cache["tags"].add(tag)

        # Check, if the 'text' argument has been passed and is not equal to the cached text
        if text and text != self._content_cache["text"]:
            # Set the passed 'text' string argument to the 'text' string in the content cache dictionary instance variable
            self._content_cache["text"] = text

    def _apply_font(self) -> None:
        """
        Applies the font configuration to the text widget.

        This method generates a tag name from the keyword arguments stored in
        the config cache and applies the font configuration associated with the
        tag name to the text widget.

        Args:
            None

        Returns:
            None
        """

        # Get or create the font
        font_to_apply: font.Font = self._get_font(**self.config_cache)

        # Generate the tag name
        tag_name: str = self._generate_tag_name(**self.config_cache)

        # If the tag doesn't exist yet, configure it
        if not tag_name in self.text.tag_names():
            self.text.tag_configure(
                tag_name,
                font=font_to_apply,
                justify=self.config_cache["justify"],
                overstrike=self.config_cache["overstrike"],
                underline=self.config_cache["underline"],
            )

        # Apply tag to selection or insert position
        if self._has_selection():
            # Apply tag to selection
            self.text.tag_add(tag_name, *self._get_selection_position())
        else:
            # Apply tag to the insert position for future typing
            self.text.tag_add(tag_name, self._get_insert_position())

        # Update the 'content cache' dictionary instance variable
        self._update_content_cache()

    def _get_font(
        self,
        **kwargs,
    ) -> font.Font:
        """
        Gets a font.Font object from the given keyword arguments.

        This method takes in keyword arguments and returns a font.Font object
        associated with the given keyword arguments. If the tag name is already
        in the font cache, it returns the font from the cache to the caller.
        Otherwise, it creates a new font.Font object, adds it to the cache and
        returns it to the caller.

        Args:
            **kwargs: Keyword arguments to be passed to the font.Font constructor.

        Returns:
            font.Font: The font.Font object associated with the given keyword arguments.
        """

        # Generate the tag name from the keyword arguments
        tag_name: str = self._generate_tag_name(**kwargs)

        # Check, if the tag name is already in the font cache
        if tag_name in self.font_cache:

            # Return the font from the cache to the caller
            return self.font_cache[tag_name]

        # Create the font and add it to the cache
        self.font_cache[tag_name] = font.Font(
            family=kwargs.get(
                "family",
                "default",
            ),
            overstrike=kwargs.get(
                "overstrike",
                False,
            ),
            size=kwargs.get(
                "size",
                10,
            ),
            slant=kwargs.get(
                "slant",
                "roman",
            ),
            underline=kwargs.get(
                "underline",
                False,
            ),
            weight=kwargs.get(
                "weight",
                "normal",
            ),
        )

        # Update the config cache
        self.config_cache.update(**kwargs)

        # Update the 'current font' Font instance variable
        self.current_font = self.font_cache[tag_name]

        # Return the font to the caller
        return self.font_cache[tag_name]

    def _generate_tag_name(
        self,
        **kwargs,
    ) -> str:
        """
        Generates a tag name from the given keyword arguments.

        This method takes in keyword arguments and returns a string tag name
        that can be used with the tkinter.Text widget.

        Args:
            **kwargs: The keyword arguments to generate the tag name from.

        Returns:
            str: The generated tag name.
        """

        # Initialize the strings list
        strings: List[str] = [
            kwargs.get(
                "family",
                "default",
            ).lower(),
            str(
                kwargs.get(
                    "size",
                    "10",
                )
            ),
            kwargs.get(
                "weight",
                "normal",
            ).lower(),
            kwargs.get(
                "slant",
                "roman",
            ).lower(),
            (
                "underline"
                if kwargs.get(
                    "underline",
                    False,
                )
                else "nounderline"
            ),
            (
                "overstrike"
                if kwargs.get(
                    "overstrike",
                    False,
                )
                else "nooverstrike"
            ),
            kwargs.get(
                "justify",
                "left",
            ).lower(),
        ]

        # Return the tag name to the caller
        return "_".join(strings)

    def _get_insert_position(self) -> Optional[str]:
        """
        Gets the current insert position in the tkinter.Text widget associated with the text editor field.

        Args:
            None

        Returns:
            Optional[str]: The current insert position in the tkinter.Text widget associated with the text editor field.
        """

        # Return the insert position to the caller
        return self._text.index(index=INSERT) if self._text else None

    def _get_selection_position(self) -> Optional[Tuple[str, str]]:
        """
        Gets the current selection position in the tkinter.Text widget associated with the text editor field.

        Args:
            None

        Returns:
            Optional[Tuple[str, str]]: The current selection position in the tkinter.Text widget associated with the text editor field.
        """

        # Return the selection position to the caller
        return (
            (
                self._text.index(index="sel.first"),
                self._text.index(index="sel.last"),
            )
            if self._text
            else None
        )

    def _has_selection(self) -> bool:
        """
        Checks if there is a selection in the tkinter.Text widget associated with the text editor field.

        Args:
            None

        Returns:
            bool: True if there is a selection, False otherwise.
        """

        # Return the selection position to the caller
        return "selection" in self._text.tag_names()

    def _on_bold_button_click(self) -> None:
        """
        Dispatches the TEXT_EDITOR_FIELD_BOLD_BUTTON_CLICKED event in the namespace string instance variable.

        Args:
            None

        Returns:
            None
        """

        # Update the value associated with the 'weight' key in the 'config cache' dictionary instance variable
        self.config_cache["weight"] = (
            "bold" if self.config_cache["weight"] == "normal" else "normal"
        )

        # Apply the font
        self._apply_font()

        # Dispatch the TEXT_EDITOR_FIELD_BOLD_BUTTON_CLICKED event in the namespace string instance variable
        self.dispatcher.dispatch(
            event=Events.TEXT_EDITOR_FIELD_BOLD_BUTTON_CLICKED,
            insert=self._get_insert_position(),
            namespace="text_editor_field_internal",
            selection=self._get_selection_position() if self._has_selection() else None,
        )

    def _on_center_align_button_click(self) -> None:
        """
        Dispatches the TEXT_EDITOR_FIELD_ALIGN_CENTER_BUTTON_CLICKED event in the namespace string instance variable.

        Args:
            None

        Returns:
            None
        """

        # Update the value associated with the 'justify' key in the 'config cache' dictionary instance variable
        self.config_cache["justify"] = "center"

        # Apply the font
        self._apply_font()

        # Dispatch the TEXT_EDITOR_FIELD_ALIGN_CENTER_BUTTON_CLICKED event in the namespace string instance variable
        self.dispatcher.dispatch(
            event=Events.TEXT_EDITOR_FIELD_ALIGN_CENTER_BUTTON_CLICKED,
            insert=self._get_insert_position(),
            namespace="text_editor_field_internal",
            selection=self._get_selection_position() if self._has_selection() else None,
        )

    def _on_clear_button_click(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        Clears the tkinter.Text widget associated with the text editor field.

        Args:
            event (Optional[tkinter.Event], optional): The event that triggered the clear action. Defaults to None.

        Returns:
            None
        """

        # Clear the tkinter.Text widget
        self._text.delete(
            index1="1.0",
            index2="end-1c",
        )

        # Obtain the label and the value
        (
            label,
            value,
        ) = (
            self.display_name,
            self._text.get(
                index1="1.0",
                index2="end-1c",
            ).strip(),
        )

        # Dispatch the TEXT_EDITOR_FIELD_CHANGED event in the namespace string instance variable
        self.dispatcher.dispatch(
            event=Events.TEXT_EDITOR_FIELD_CHANGED,
            label=label,
            namespace=self.namespace,
            value=value,
        )

        # Check, if an 'on_change_callback' exists
        if self.on_change_callback:
            # Call the 'on_change_callback' funtion with the label and the value
            self.on_change_callback(
                (
                    label,
                    value,
                )
            )

    def _on_ctrl_v(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        Pastes content from the clipboard into the tkinter.Text widget associated with the text editor field.

        If the clipboard contains an image, it will be inserted into the tkinter.Text widget at the position of the
        text insertion cursor. If the clipboard does not contain an image, this method will generate a paste event
        to allow the default paste behavior to occur.

        Args:
            event (Optional[tkinter.Event], optional): The event that triggered the paste action. Defaults to None.

        Returns:
            None
        """

        # Attempt to get an image from the clipboard
        clipboard_image: Optional[Image.Image] = ImageGrab.grabclipboard()

        # Check, if the clipboard contains an image
        if not clipboard_image:
            # Generate a paste event
            self._text.event_generate(sequence="<<Paste>>")

            # Return early
            return

        # Convert the image to a PhotoImage
        photo_image: ImageTk.PhotoImage = ImageTk.PhotoImage(image=clipboard_image)

        # Add the PhotoImage object the 'images' dictionary instance variable
        self.images[str(photo_image)] = photo_image

        # Insert the image into the tkinter.Text widget
        self._text.image_create(
            index=INSERT,
            image=photo_image,
            name=str(photo_image),
        )

        # Update the 'content cache' dictionary instance variable
        self._update_content_cache()

        # Update the tkinter.Text widget
        self._text.update()

    def _on_font_family_combobox_select(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        Dispatches the TEXT_EDITOR_FIELD_FONT_FAMILY_COMBOX_SELECT event in the namespace string instance variable.

        Args:
            event (Optional[tkinter.Event], optional): The event that triggered the font family combobox selection. Defaults to None.

        Returns:
            None
        """

        # Update the value associated with the 'family' key in the 'config cache' dictionary instance variable
        self.config_cache["family"] = self._font_family_combobox.get() or "default"

        # Apply the font
        self._apply_font()

        # Dispatch the TEXT_EDITOR_FIELD_FONT_FAMILY_COMBOX_SELECT event in the namespace string instance variable
        self.dispatcher.dispatch(
            event=Events.TEXT_EDITOR_FIELD_FONT_FAMILY_COMBOX_SELECT,
            font_family=self._font_family_combobox.get(),
            insert=self._get_insert_position(),
            namespace="text_editor_field_internal",
            selection=self._get_selection_position() if self._has_selection() else None,
        )

    def _on_font_size_combobox_select(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        Dispatches the TEXT_EDITOR_FIELD_FONT_SIZE_COMBOX_SELECT event in the namespace string instance variable.

        Args:
            event (Optional[tkinter.Event], optional): The event that triggered the font size combobox selection. Defaults to None.

        Returns:
            None
        """

        # Update the value associated with the 'size' key in the 'config cache' dictionary instance variable
        self.config_cache["size"] = int(self._font_size_combobox.get()) or 12

        # Apply the font
        self._apply_font()

        # Dispatch the TEXT_EDITOR_FIELD_FONT_SIZE_COMBOX_SELECT event in the namespace string instance variable
        self.dispatcher.dispatch(
            event=Events.TEXT_EDITOR_FIELD_FONT_SIZE_COMBOX_SELECT,
            font_size=self._font_size_combobox.get(),
            insert=self._get_insert_position(),
            namespace="text_editor_field_internal",
            selection=self._get_selection_position() if self._has_selection() else None,
        )

    def _on_italic_button_click(self) -> None:
        """
        Dispatches the TEXT_EDITOR_FIELD_ITALIC_BUTTON_CLICKED event in the namespace string instance variable.

        Args:
            None

        Returns:
            None
        """

        # Update the value associated with the 'slant' key in the 'config cache' dictionary instance variable
        self.config_cache["slant"] = (
            "italic" if self.config_cache["slant"] == "roman" else "roman"
        )

        # Apply the font
        self._apply_font()

        # Dispatch the TEXT_EDITOR_FIELD_ITALIC_BUTTON_CLICKED event in the namespace string instance variable
        self.dispatcher.dispatch(
            event=Events.TEXT_EDITOR_FIELD_ITALIC_BUTTON_CLICKED,
            insert=self._get_insert_position(),
            namespace="text_editor_field_internal",
            selection=self._get_selection_position() if self._has_selection() else None,
        )

    def _on_key_release(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        Called when a key is released in the text widget.

        This method applies the font configuration to the text widget.

        Args:
            event (Optional[tkinter.Event], optional): The event that triggered the key release. Defaults to None.

        Returns:
            None
        """

        # Apply the font
        self._apply_font()

    def _on_left_align_button_click(self) -> None:
        """
        Dispatches the TEXT_EDITOR_FIELD_ALIGN_LEFT_BUTTON_CLICKED event in the namespace string instance variable.

        Args:
            None

        Returns:
            None
        """

        # Update the value associated with the 'justify' key in the 'config cache' dictionary instance variable
        self.config_cache["justify"] = "left"

        # Apply the font
        self._apply_font()

        # Dispatch the TEXT_EDITOR_FIELD_ALIGN_LEFT_BUTTON_CLICKED event in the namespace string instance variable
        self.dispatcher.dispatch(
            event=Events.TEXT_EDITOR_FIELD_ALIGN_LEFT_BUTTON_CLICKED,
            insert=self._get_insert_position(),
            namespace="text_editor_field_internal",
            selection=self._get_selection_position() if self._has_selection() else None,
        )

    def _on_overstrike_button_click(self) -> None:
        """
        Dispatches the TEXT_EDITOR_FIELD_OVERSTRIKE_BUTTON_CLICKED event in the namespace string instance variable.

        Args:
            None

        Returns:
            None
        """

        # Update the value associated with the 'overstrike' key in the 'config cache' dictionary instance variable
        self.config_cache["overstrike"] = not self.config_cache["overstrike"]

        # Apply the font
        self._apply_font()

        # Dispatch the TEXT_EDITOR_FIELD_OVERSTRIKE_BUTTON_CLICKED event in the namespace string instance variable
        self.dispatcher.dispatch(
            event=Events.TEXT_EDITOR_FIELD_OVERSTRIKE_BUTTON_CLICKED,
            insert=self._get_insert_position(),
            namespace="text_editor_field_internal",
            selection=self._get_selection_position() if self._has_selection() else None,
        )

    def _on_right_align_button_click(self) -> None:
        """
        Dispatches the TEXT_EDITOR_FIELD_ALIGN_RIGHT_BUTTON_CLICKED event in the namespace string instance variable.

        Args:
            None

        Returns:
            None
        """

        # Update the value associated with the 'justify' key in the 'config cache' dictionary instance variable
        self.config_cache["justify"] = "right"

        # Apply the font
        self._apply_font()

        # Dispatch the TEXT_EDITOR_FIELD_ALIGN_RIGHT_BUTTON_CLICKED event in the namespace string instance variable
        self.dispatcher.dispatch(
            event=Events.TEXT_EDITOR_FIELD_ALIGN_RIGHT_BUTTON_CLICKED,
            insert=self._get_insert_position(),
            namespace="text_editor_field_internal",
            selection=self._get_selection_position() if self._has_selection() else None,
        )

    def _on_text_change(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        Handles the text change event.

        This method is called when the text in the tkinter.Text widget changes.

        Args:
            event (tkinter.Event, optional): The event object associated with the text change event.

        Returns:
            None
        """

        # Obtain the label and the value
        (
            label,
            value,
        ) = (
            self.display_name,
            self._text.get(
                index1="1.0",
                index2="end-1c",
            ).strip(),
        )

        # Dispatch the TEXT_EDITOR_FIELD_CHANGED event in the namespace string instance variable
        self.dispatcher.dispatch(
            event=Events.TEXT_EDITOR_FIELD_CHANGED,
            label=label,
            namespace=self.namespace,
            value=value,
        )

        # Check, if an 'on_change_callback' exists
        if self.on_change_callback:
            # Call the 'on_change_callback' funtion with the label and the value
            self.on_change_callback(
                (
                    label,
                    value,
                )
            )

    def _on_underline_button_click(self) -> None:
        """
        Dispatches the TEXT_EDITOR_FIELD_UNDERLINE_BUTTON_CLICKED event in the namespace string instance variable.

        Args:
            None

        Returns:
            None
        """

        # Update the value associated with the 'underline' key in the 'config cache' dictionary instance variable
        self.config_cache["underline"] = not self.config_cache["underline"]

        # Apply the font
        self._apply_font()

        # Dispatch the TEXT_EDITOR_FIELD_UNDERLINE_BUTTON_CLICKED event in the namespace string instance variable
        self.dispatcher.dispatch(
            event=Events.TEXT_EDITOR_FIELD_UNDERLINE_BUTTON_CLICKED,
            insert=self._get_insert_position(),
            namespace="text_editor_field_internal",
            selection=self._get_selection_position() if self._has_selection() else None,
        )

    def _update_content_cache(self) -> None:
        """
        Updates the content cache based on the current content of the text widget.

        Args:
            None

        Returns:
            None
        """

        # Update plain text
        self._content_cache["text"] = self.text.get(
            index1="1.0",
            index2="end-1c",
        )

        # Clear existing images
        self._content_cache["images"].clear()

        # Clear existing tags
        self._content_cache["tags"].clear()

        # Get the dump of the text widget
        dump: List[Tuple[str, str, str]] = self._text.dump(
            all=True,
            index1="1.0",
            index2="end-1c",
        )

        # Filter the dump for 'image' 'tagoff' 'tagon'
        filtered_dump: List[Tuple[str, str, Any]] = list(
            filter(
                lambda x: x[0]
                in (
                    "image",
                    "tagoff",
                    "tagon",
                ),
                dump,
            )
        )

        # Initialize a dictionary to keep track of active tags
        active_tags: Dict[str, str] = {}

        for (
            item_type,
            position,
            value,
        ) in filtered_dump:
            # Check, if the item type is 'image'
            if item_type == "image":
                # Attempt to get the image from the 'images' dictionary instance variable
                image: Optional[ImageTk.PhotoImage] = self.images.get(
                    str(value),
                    None,
                )

                # Check, if the image exists
                if not image:
                    # Skip the current iteration
                    continue

                # Add the image to the content cache
                self._add_to_content_cache(
                    image=TextEditorFieldImageItem(
                        image=image,
                        name=str(value),
                        position=position,
                    )
                )

            # Check, if the item type is 'tagoff'
            elif item_type == "tagoff":
                # Attempt to get the start position from the 'active tags' dictionary
                start_position: Optional[str] = active_tags.pop(
                    value,
                    None,
                )

                # Check, if the start position exists
                if not start_position:
                    # Skip the current iteration
                    continue

                # Add the tag to the content cache
                self._add_to_content_cache(
                    tag=TextEditorFieldTagItem(
                        end=position,
                        font_configuration=self.font_cache[value],
                        start=start_position,
                        tag_name=value,
                    )
                )

            # Check, if the item type is 'tagon'
            elif item_type == "tagon":
                # Add the tag to the 'active tags' dictionary
                active_tags[value] = position

    @override
    def clear(
        self,
        dispatch: bool = False,
    ) -> None:
        """
        Clears the tkinter.Text widget.

        This method clears the tkinter.Text widget and dispatches a TEXT_EDITOR_FIELD_CLEARED event if the dispatch flag is set to True.

        Args:
            dispatch (bool, optional): Whether to dispatch a clear event. Defaults to False.

        Returns:
            None
        """

        # Clear the tkinter.Text widget
        self._text.delete(
            index1="1.0",
            index2="end-1c",
        )

        # Obtain the label and the value
        (
            label,
            value,
        ) = (
            self.display_name,
            self._text.get(
                index1="1.0",
                index2="end-1c",
            ).strip(),
        )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the TEXT_EDITOR_FIELD_CLEARED event in the namespace string instance variable
            self.dispatcher.dispatch(
                event=Events.TEXT_EDITOR_FIELD_CLEARED,
                label=label,
                namespace=self.namespace,
                value=value,
            )

    def configure_clear_button(
        self,
        **kwargs,
    ) -> None:
        """ """
        try:
            # Attempt to configure the 'clear button' tkinter.Button widget
            self._clear_button.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_clear_button' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @override
    def configure_grid(self) -> None:
        """
        Configures the grid for the TextEditorField widget.

        This method configures the grid for the TextEditorField widget by setting the weight of the columns.

        Args:
            None

        Returns:
            None
        """

        # Configure the TextEditorField widget's 0th column to weight 0
        self.grid_columnconfigure(
            index=0,
            weight=0,
        )

        # Configure the TextEditorField widget's 1st column to weight 1
        self.grid_columnconfigure(
            index=1,
            weight=1,
        )

        # Configure the TextEditorField widget's 2nd column to weight 0
        self.grid_columnconfigure(
            index=2,
            weight=0,
        )

        # Configure the TextEditorField widget's 0th row to weight 0
        self.grid_columnconfigure(
            index=0,
            weight=0,
        )

        # Configure the TextEditorField widget's 1st row to weight 0
        self.grid_columnconfigure(
            index=1,
            weight=0,
        )

        # Configure the TextEditorField widget's 2nd row to weight 1
        self.grid_columnconfigure(
            index=2,
            weight=1,
        )

        # Configure the TextEditorField widget's 3rd row to weight 0
        self.grid_columnconfigure(
            index=3,
            weight=0,
        )

    def configure_horizontal_scrollbar(
        self,
        **kwargs,
    ) -> None:
        """ """
        try:
            # Attempt to configure the 'horizontal scrollbar' tkinter.Scrollbar widget
            self._horizontal_scrollbar.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_horizontal_scrollbar' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_label(
        self,
        **kwargs,
    ) -> None:
        """ """
        try:
            # Attempt to configure the tkinter.Label widget
            self._label.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_label' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_text(
        self,
        **kwargs,
    ) -> None:
        """ """
        try:
            # Attempt to configure the tkinter.Text widget
            self._text.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_text' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_tools_frame(
        self,
        **kwargs,
    ) -> None:
        """ """
        try:
            # Attempt to configure the 'tools frame' tkinter.Frame widget
            self._tools_frame.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_tools_frame' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_vertical_scrollbar(
        self,
        **kwargs,
    ) -> None:
        """ """
        try:
            # Attempt to configure the 'vertical scrollbar' tkinter.Scrollbar widget
            self._vertical_scrollbar.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_vertical_scrollbar' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @override
    def create_widgets(
        self,
        display_name: str,
        **kwargs,
    ) -> None:
        """ """

        # Create a tkinter.Label widget
        self._label: tkinter.Label = tkinter.Label(
            master=self,
            text=display_name,
            **kwargs.get(
                "label",
                {},
            ),
        )

        # Place the tkinter.Label widget in the grid
        self._label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create the 'tools frame' tkinter.Frame widget
        self._tools_frame: tkinter.Frame = tkinter.Frame(
            master=self,
            **kwargs.get(
                "tools_frame",
                {},
            ),
        )

        # Place the 'tools frame' tkinter.Frame widget in the grid
        self._tools_frame.grid(
            column=1,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )

        # Create the 'bold button' tkinter.Button' widget
        self._bold_button: tkinter.Button = tkinter.Button(
            command=self._on_bold_button_click,
            master=self._tools_frame,
            text="Bold",
            **kwargs.get(
                "bold_button",
                {},
            ),
        )

        # Place the 'bold button' tkinter.Button' widget in the grid
        self._bold_button.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
        )

        # Create the 'italic button' tkinter.Button' widget
        self._italic_button: tkinter.Button = tkinter.Button(
            command=self._on_italic_button_click,
            master=self._tools_frame,
            text="Italic",
            **kwargs.get(
                "italic_button",
                {},
            ),
        )

        # Place the 'italic button' tkinter.Button' widget in the grid
        self._italic_button.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
        )

        # Create the 'left align button' tkinter.Button' widget
        self._left_align_button: tkinter.Button = tkinter.Button(
            command=self._on_left_align_button_click,
            master=self._tools_frame,
            text="Left",
            **kwargs.get(
                "left_align_button",
                {},
            ),
        )

        # Place the 'left align button' tkinter.Button' widget in the grid
        self._left_align_button.grid(
            column=2,
            padx=5,
            pady=5,
            row=0,
        )

        # Create the 'center align button' tkinter.Button' widget
        self._center_align_button: tkinter.Button = tkinter.Button(
            command=self._on_center_align_button_click,
            master=self._tools_frame,
            text="Center",
            **kwargs.get(
                "center_align_button",
                {},
            ),
        )

        # Place the 'center align button' tkinter.Button' widget in the grid
        self._center_align_button.grid(
            column=3,
            padx=5,
            pady=5,
            row=0,
        )

        # Create the 'right align button' tkinter.Button' widget
        self._right_align_button: tkinter.Button = tkinter.Button(
            command=self._on_right_align_button_click,
            master=self._tools_frame,
            text="Right",
            **kwargs.get(
                "right_align_button",
                {},
            ),
        )

        # Place the 'right align button' tkinter.Button' widget in the grid
        self._right_align_button.grid(
            column=4,
            padx=5,
            pady=5,
            row=0,
        )

        # Create the 'underline button' tkinter.Button' widget
        self._underline_button: tkinter.Button = tkinter.Button(
            command=self._on_underline_button_click,
            master=self._tools_frame,
            text="Underline",
            **kwargs.get(
                "underline_button",
                {},
            ),
        )

        # Place the 'underline button' tkinter.Button' widget in the grid
        self._underline_button.grid(
            column=5,
            padx=5,
            pady=5,
            row=0,
        )

        # Create the 'overstrike button' tkinter.Button' widget
        self._overstrike_button: tkinter.Button = tkinter.Button(
            command=self._on_overstrike_button_click,
            master=self._tools_frame,
            text="Strikethrough",
            **kwargs.get(
                "overstrike_button",
                {},
            ),
        )

        # Place the 'overstrike button' tkinter.Button' widget in the grid
        self._overstrike_button.grid(
            column=6,
            padx=5,
            pady=5,
            row=0,
        )

        # Create the 'font family' ttk.Combobox widget
        self._font_family_combobox: ttk.Combobox = ttk.Combobox(
            master=self._tools_frame,
            **kwargs.get(
                "font_family_combobox",
                {},
            ),
        )

        # Place the 'font family' ttk.Combobox widget in the grid
        self._font_family_combobox.grid(
            column=7,
            padx=5,
            pady=5,
            row=0,
        )

        # Create the 'font size' ttk.Combobox widget
        self._font_size_combobox: ttk.Combobox = ttk.Combobox(
            master=self._tools_frame,
            values=list(range(0, 100)),
            **kwargs.get(
                "font_size_combobox",
                {},
            ),
        )

        # Place the 'font size' ttk.Combobox widget in the grid
        self._font_size_combobox.grid(
            column=8,
            padx=5,
            pady=5,
            row=0,
        )

        # Create a tkinter.Text widget
        self._text: tkinter.Text = tkinter.Text(
            master=self,
            **kwargs.get(
                "text",
                {},
            ),
        )

        # Place the tkinter.Text widget in the grid
        self._text.grid(
            column=1,
            padx=5,
            pady=5,
            row=2,
            sticky=NSEW,
        )

        # Bind the '_on_ctrl_v' method to the tkinter.Text widget via the 'Control-v' event
        self._text.bind(
            add="+",
            func=self._on_ctrl_v,
            sequence="<Control-v>",
        )

        # Bind the '_on_key_release' method to the tkinter.Text widget via the 'KeyRelease' event
        self._text.bind(
            add="+",
            func=self._on_key_release,
            sequence="<KeyRelease>",
        )

        # Bind the '_on_text_change' method to the tkinter.Text widget via the 'KeyRelease' event
        self._text.bind(
            add="+",
            func=self._on_text_change,
            sequence="<KeyRelease>",
        )

        # Create the 'vertical scrollbar' tkinter.Scrollbar widget
        self._vertical_scrollbar: tkinter.Scrollbar = tkinter.Scrollbar(
            master=self,
            orient=VERTICAL,
            **kwargs.get(
                "vertical_scrollbar",
                {},
            ),
        )

        # Place the 'vertical scrollbar' tkinter.Scrollbar widget in the grid
        self._vertical_scrollbar.grid(
            column=2,
            row=2,
            sticky=NS,
        )

        # Create the 'horizontal scrollbar' tkinter.Scrollbar widget
        self._horizontal_scrollbar: tkinter.Scrollbar = tkinter.Scrollbar(
            master=self,
            orient=HORIZONTAL,
            **kwargs.get(
                "horizontal_scrollbar",
                {},
            ),
        )

        # Place the 'horizontal scrollbar' tkinter.Scrollbar widget in the grid
        self._horizontal_scrollbar.grid(
            column=1,
            row=3,
            sticky=EW,
        )

        # Create the 'clear button' tkinter.Button widget
        self._clear_button: tkinter.Button = tkinter.Button(
            command=self._on_clear_button_click,
            master=self,
            text="X",
            **kwargs.get(
                "clear_button",
                {},
            ),
        )

        # Place the 'clear button' tkinter.Button widget in the grid
        self._clear_button.grid(
            column=2,
            padx=5,
            pady=5,
            row=3,
        )

    @override
    def get(
        self,
        dispatch: bool = False,
    ) -> Tuple[str, str]:
        """
        Gets the value of the text editor field.

        This method returns the display name and the current value of the text editor field.

        If the dispatch flag is set to True, a GET event is dispatched.

        Args:
            dispatch (bool, optional): Whether to dispatch a get event. Defaults to False.

        Returns:
            Tuple[str, str]: A tuple containing the display name and the current value of the text editor field.
        """

        # Obtain the label and the value
        (
            label,
            value,
        ) = (
            self.display_name,
            self._text.get(
                index1="1.0",
                index2="end-1c",
            ).strip(),
        )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the TEXT_EDITOR_FIELD_GET event in the namespace string instance variable
            self.dispatcher.dispatch(
                event=Events.TEXT_EDITOR_FIELD_GET,
                label=label,
                namespace=self.namespace,
                value=value,
            )

        # Return the label and the value to the caller
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
        Sets the value of the text editor field.

        This method clears the tkinter.Text widget and inserts the passed string value.

        If the dispatch flag is set to True, a SET event is dispatched.

        Args:
            value (str): The string value to set for the text editor field.
            dispatch (bool, optional): Whether to dispatch a set event. Defaults to False.

        Returns:
            None
        """

        # Clear the tkinter.Text widget
        self._text.delete(
            index1="1.0",
            index2="end-1c",
        )

        # Insert the passed string value
        self._text.insert(
            chars=value,
            index="1.0",
        )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the TEXT_EDITOR_FIELD_SET event in the namespace string instance variable
            self.dispatcher.dispatch(
                event=Events.TEXT_EDITOR_FIELD_SET,
                label=self.display_name,
                namespace=self.namespace,
                value=value,
            )
