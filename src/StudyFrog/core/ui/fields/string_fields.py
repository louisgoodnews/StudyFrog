"""
Author: lodego
Date: 2025-04-05
"""

import platform
import tkinter
import traceback

from tkinter.constants import *
from typing import *

from utils.base_field import BaseField
from utils.constants import Constants
from utils.events import Events
from utils.miscellaneous import Miscellaneous


__all__: Final[List[str]] = [
    "MultiLineTextField",
    "SingleLineTextField",
]


class MultiLineTextField(BaseField):
    """
    A multi line text field widget.

    This class represents a multi line text field with a label, text, scrollbar, and clear button.
    It provides methods to configure and interact with the widgets, as well as a callback
    for handling changes in the text field's value.
    """

    def __init__(
        self,
        label: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, str], None]] = None,
        value: Optional[str] = None,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the SingleLineTextField class.

        Args:
            label (str): The label for the multi line text field.
            master (tkinter.Misc): The master widget.
            namespace (str, optional): The namespace for the multi line text field. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[str, str], None]], optional): The callback function to be called when the value of the multi line text field changes. Defaults to None.
            value (Optional[str], optional): The initial value of the multi line text field. Defaults to None.
            kwargs: Additional keyword arguments
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

    def _on_text_change(self) -> None:
        """
        This method is called when the value of the multi line text field changes.

        It dispatches the MULTI_LINE_TEXT_FIELD_CHANGED event and calls the on_change_callback function with the new label and value.

        Returns:
            None
        """

        # Get the label and value of the multi line text field
        (
            label,
            value,
        ) = (
            self.label.cget(key="text"),
            self.text.get(
                index1="1.0",
                index2=END,
            ).strip(),
        )

        # Dispatch the MULTI_LINE_TEXT_FIELD_CHANGED event
        self.dispatcher.dispatch(
            event=Events.MULTI_LINE_TEXT_FIELD_CHANGED,
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
            index2=END,
        )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the MULTI_LINE_TEXT_FIELD_CLEARED event
            self.dispatcher.dispatch(
                event=Events.MULTI_LINE_TEXT_FIELD_CLEARED,
                label=self.label.cget(key="text"),
                namespace=self.namespace,
                value=self.text.get(
                    index1="1.0",
                    index2=END,
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
        self.grid_column_configure(
            index=0,
            weight=0,
        )

        # Set the weight of the 1st column to 1
        # This means that the column will stretch when the window is resized
        self.grid_column_configure(
            index=1,
            weight=1,
        )

        # Set the weight of the 2nd column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_column_configure(
            index=2,
            weight=0,
        )

        # Set the weight of the 0th row to 0
        # This means that the row will not stretch when the window is resized
        self.grid_row_configure(
            index=0,
            weight=0,
        )

        # Set the weight of the 1st row to 1
        # This means that the row will stretch when the window is resized
        self.grid_row_configure(
            index=1,
            weight=1,
        )

        # Set the weight of the 2nd row to 0
        # This means that the row will not stretch when the window is resized
        self.grid_row_configure(
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
        label: str,
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
            text=label,
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
            column=2,
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
            self.label.cget(key="text"),
            self.text.get(
                index1="1.0",
                index2=END,
            ).strip(),
        )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the MULTI_LINE_TEXT_FIELD_GET
            self.dispatcher.dispatch(
                event=Events.MULTI_LINE_TEXT_FIELD_GET,
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
            index2=END,
        )

        # Insert the passed value string into the tkinter.Text widget
        self.text.insert(
            chars=value,
            index1="1.0",
        )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the MULTI_LINE_TEXT_FIELD_SET
            self.dispatcher.dispatch(
                event=Events.MULTI_LINE_TEXT_FIELD_SET,
                label=self.label.cget(key="text"),
                namespace=self.namespace,
                value=self.text.get(
                    index1="1.0",
                    index2=END,
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
        label: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, str], None]] = None,
        value: Optional[str] = None,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the ReadOnlyMultiLineTextField class.

        Args:
        label (str): The label for the read-only multi line text field.
        master (tkinter.Misc): The master widget.
            namespace (str, optional): The namespace for the text field. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[str, str], None]], optional): The callback function to be called when the value of the text field changes. Defaults to None.
            value (Optional[str], optional): The initial value of the text field. Defaults to None.
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
            self.label.cget(key="text"),
            self.variable.get(),
        )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the READONLY_FIELD_GET event
            self.dispatcher.dispatch(
                event=Events.READONLY_MULTI_LINE_TEXT_FIELD_GET,
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


class SingleLineTextField(BaseField):
    """
    A single line text field widget.

    This class represents a single line text field with a label, entry, and clear button.
    It provides methods to configure and interact with the widgets, as well as a callback
    for handling changes in the text field's value.
    """

    def __init__(
        self,
        label: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, str], None]] = None,
        value: Optional[str] = None,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the SingleLineTextField class.

        Args:
            label (str): The label for the single line text field.
            master (tkinter.Misc): The master widget.
            namespace (str, optional): The namespace for the single line text field. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[str, str], None]], optional): The callback function to be called when the value of the single line text field changes. Defaults to None.
            value (Optional[str], optional): The initial value of the single line text field. Defaults to None.
            kwargs: Additional keyword arguments.
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
            self.label.cget(key="text"),
            self.variable.get(),
        )

        # Dispatch the SINGLE_LINE_TEXT_FIELD_CHANGED event
        self.dispatcher.dispatch(
            event=Events.SINGLE_LINE_TEXT_FIELD_CHANGED,
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
                label=self.label.cget(key="text"),
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
        self.grid_column_configure(
            index=0,
            weight=0,
        )

        # Set the weight of the 1st column to 1
        # This means that the column will stretch when the window is resized
        self.grid_column_configure(
            index=1,
            weight=1,
        )

        # Set the weight of the 2nd column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_column_configure(
            index=2,
            weight=0,
        )

        # Set the weight of the 0th row to 1
        # This means that the row will stretch when the window is resized
        self.grid_row_configure(
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
        label: str,
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
            text=label,
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
            self.label.cget(key="text"),
            self.variable.get(),
        )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the SINGLE_LINE_TEXT_FIELD_GET
            self.dispatcher.dispatch(
                event=Events.SINGLE_LINE_TEXT_FIELD_GET,
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
                label=self.label.cget(key="text"),
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
        label: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, str], None]] = None,
        value: Optional[str] = None,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the PasswordTextField class.

        Args:
        label (str): The label for the password text field.
        master (tkinter.Misc): The master widget.
        namespace (str, optional): The namespace for the password text field. Defaults to Constants.GLOBAL_NAMESPACE.
        on_change_callback (Optional[Callable[[str, str], None]], optional): The callback function to be called when the value of the password text field changes. Defaults to None.
        value (Optional[str], optional): The initial value of the password text field. Defaults to None.
        kwargs: Additional keyword arguments.
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
                label=self.label.cget(key="text"),
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
            self.label.cget(key="text"),
            self.variable.get(),
        )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the PASSWORD_TEXT_FIELD_GET event
            self.dispatcher.dispatch(
                event=Events.PASSWORD_TEXT_FIELD_GET,
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
                label=self.label.cget(key="text"),
                namespace=self.namespace,
                value=self.variable.get(),
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
        label: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, str], None]] = None,
        value: Optional[str] = None,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the ReadOnlySingleLineTextField class.

        Args:
        label (str): The label for the read-only single line text field.
        master (tkinter.Misc): The master widget.
            namespace (str, optional): The namespace for the text field. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[str, str], None]], optional): The callback function to be called when the value of the text field changes. Defaults to None.
            value (Optional[str], optional): The initial value of the text field. Defaults to None.
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

        # Configure the entry widget to be read-only
        self._entry.configure(state=DISABLED)

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
            self.label.cget(key="text"),
            self.variable.get(),
        )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the READONLY_FIELD_GET event
            self.dispatcher.dispatch(
                event=Events.READONLY_SINGLE_LINE_TEXT_FIELD_GET,
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
