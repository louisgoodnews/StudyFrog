"""
Author: lodego
Date: 2025-04-06
"""

import tkcalendar
import tkinter
import traceback

from datetime import datetime
from tkinter.constants import *
from typing import *

from utils.base_field import BaseField
from utils.constants import Constants
from utils.events import Events
from utils.miscellaneous import Miscellaneous


__all__: Final[List[str]] = ["DateSelectField"]


class DateSelectField(BaseField):
    """
    A date selection field with entry and calendar popup.

    This field allows users to either type in a date (with optional validation)
    or select one using a popup calendar. It supports custom date formats and
    integrates tightly with the event system and callback structure of StudyFrog.
    """

    def __init__(
        self,
        label: str,
        master: tkinter.Misc,
        date_format: str = Constants.DEFAULT_DATE_FORMAT,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, Optional[datetime]], None]] = None,
        readonly: bool = False,
        value: Optional[Union[datetime, string]] = None,
        **kwargs
    ) -> None:
        """
        Initializes a new instance of the DateSelectField class.

        Args:
            label (str): The label for the date select field.
            master (tkinter.Misc): The master widget.
            date_format (str): The format string used to parse and display dates.
            namespace (str): The namespace to dispatch events under.
            on_change_callback (Optional[Callable[[str, Optional[datetime]], None]]): 
                Callback function when the date value changes.
            readonly (bool): Whether the entry should be readonly.
            value (Optional[Union[datetime, string]]): The initial value for the field.
            **kwargs: Additional keyword arguments passed to widget configuration.

        Returns:
            None
        """

        # Call the parent class constructor with the passed arguments
        super().__init__(
            label=label,
            master=master,
            namespace=namespace,
            on_change_callback=on_change_callback,
            readonly=readonly,
            value=value,
            **kwargs,
        )

        # Initialize the (optional) calendar instance variable as None
        self.calendar: Optional[tkcalendar.Calendar] = None

        # Store the passed date format string
        self._date_format: str = date_format

        # Initialize the (optional) toplevel instance variable as None
        self.toplevel: Optional[tkinter.Toplevel] = None

        # Check, if the passed value is not None
        if value is not None:
            # Set the value of the field to the passed value
            self.set(value=value)

    @property
    def clear_button(self) -> tkinter.Button:
        """
        Returns the 'clear button' button widget used to empty the entry.

        Returns:
            tkinter.Button: The 'clear button' button instance.
        """

        # Return the 'clear button' button widget
        return self._clear_button

    @property
    def date_format(self) -> str:
        """
        Returns the currently used date format string.

        Returns:
            str: The active date format.
        """

        # Return the date format string
        return self._date_format

    @date_format.setter
    def date_format(
        self,
        value: str,
    ) -> None:
        """
        Updates the date format for parsing and formatting values.

        Args:
            value (str): The new date format string to apply.
        """

        # Check, if the passed value string has a valid format
        if not Miscellaneous.validate_date_format(date_format=value):
            # Return early
            return

        # Update the date format string with the passed value
        self._date_format = value

    @property
    def entry(self) -> tkinter.Entry:
        """
        Returns the entry widget displaying the date value.

        Returns:
            tkinter.Entry: The entry widget instance.
        """

        # Return the tkinter.Entry entry widget
        return self._entry

    @property
    def label(self) -> tkinter.Label:
        """
        Returns the label widget of the date field.

        Returns:
            tkinter.Label: The label widget.
        """

        # Return the tkinter.Label label widget
        return self._label

    @property
    def select_button(self) -> tkinter.Button:
        """
        Returns the 'select button' button widget used to open the calendar.

        Returns:
            tkinter.Button: The 'select button' button instance.
        """

        # Return the 'select button' button widget
        return self._select_button

    def _on_confirm_button_click(self) -> None:
        """
        Callback for the confirm button in the calendar popup.

        Transfers the selected calendar value into the entry and dispatches
        the value change, then closes the calendar popup.

        Returns:
            None
        """

        # Check, the calendar widget exists
        if self.calendar is not None:
            # Log a warning message
            self.logger.warning(
                message=f"Calendar not present. Cannot handle 'confirm button' button click. This is likely a serious issue."
            )

            # Destroy the toplevel widget, triggering the 'on_toplevel_destroy' method implicitly
            self.toplevel.destroy()

            # Return early
            return

        # Obtain the current value of the calendar widget
        value: Optional[str] = self.calendar.get_date()

        # Check, if the value is not None
        if value is None:
            # Log a warning message
            self.logger.warning(message=f"")
            
            # Return early
            return

        # Update the variable with the value obtained from the calendar widget
        self.variable.set(value=value)

        # Dispatch the DATE_SELECT_FIELD_CHANGED event in the passed namespace
        self.dispatcher.dispatch(
            event=Events.DATE_SELECT_FIELD_CHANGED,
            label=self.display_name,
            namespace=self.namespace,
            value=Miscellaneous.string_to_datetime(
                date_string=value,
                format=self.date_format,
            ),
        )

        # Destroy the toplevel widget, triggering the 'on_toplevel_destroy' method implicitly
        self.toplevel.destroy()

    def _on_entry_change(
        self,
        dispatch: bool = False,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        Handles manual entry changes and performs format validation.

        Args:
            dispatch (bool): Whether to dispatch change events.
            event (Optional[tkinter.Event]): The triggering key event, if any.

        Returns:
            None
        """

        # Obtain the current entry value of the string variable as string
        string_value: str = self.variable.get()

        # Attempt to find matches for the date_format within the current entry value
        match: Optional[str] = Miscellaneous.find_match(
            pattern=self.date_format,
            string=string_value,
        )

        # Check, if a match has been found
        if match is None:
            # Place the 'warning label' label widget within the grid
            self.warning_label.grid(
                column=1,
                padx=5,
                pady=5,
                row=1,
                sticky=NSEW,
            )
            
            # Return early
            return
        else:
            # Hide the'warning label' label widget
            self.warning_label.grid_forget()

        # Check, if the match string is not None and the dispatch flag is set to True
        if match is not None and dispatch:
            # Dispatch the DATE_SELECT_FIELD_CHANGED event in the passed namespace
            self.dispatcher.dispatch(
                event=Events.DATE_SELECT_FIELD_CHANGED,
                label=self.display_name,
                namespace=self.namespace,
                value=Miscellaneous.datetime_to_string(
                    date_string=match,
                    format=self.date_format,
                ),
            )

        # Check, if the 'on_change_callback' function exists and the match string is not None
        if match is not None and self.on_change_callback:
            # Call the 'on_change_callback' function and pass the display name as well as the variable's value to it
            self.on_change_callback(
                self.display_name,
                Miscellaneous.string_to_datetime(
                    date_string=match,
                    format=self.date_format,
                ),
            )

    def _on_select_button_click(self) -> None:
        """
        Opens the calendar popup for date selection.

        This method creates a Toplevel with a calendar and confirm button,
        and applies appropriate layout and focus handling.

        Returns:
            None
        """

        # Check, if the toplevel instance variable is not None
        if self.toplevel is not None:
            # Return early
            return

        # Create a toplevel widget
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
        # This means that the row will stretch when the window is resized
        self.toplevel.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Set the weight of the 2nd row to 0
        # This means that the row will not stretch when the window is resized
        self.toplevel.grid_rowconfigure(
            index=2,
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
            text="Please select a date."
        )

        # Place the label widget within the grid
        label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )        

        # Create a calendar widget
        self.calendar = tkcalendar.Calendar(
            date_pattern=self._date_format,
            master=self.toplevel,
        )

        # Place the calendar widget within the grid
        self.calendar.grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )

        # Create a button widget
        button: tkinter.Button = tkinter.Button(
            command=self._on_confirm_button_click,
            master=self.toplevel,
            text="Confirm",
        )

        # Place the button widget within the grid
        button.grid(
            column=0,
            padx=5,
            pady=5,
            row=2,
        )

    def _on_toplevel_destroy(self) -> None:
        """
        Cleans up internal references when the calendar popup is closed.

        Returns:
            None
        """

        # Update the calendar instance variable to None
        self.calendar = None

        # Update the toplevel instance variable to None
        self.toplevel = None

    def clear(
        self,
        dispatch: bool = False,
    ) -> None:
        """
        Clears the field's value.

        Args:
            dispatch (bool): Whether to dispatch a clear event.

        Returns:
            None
        """

        # Update the variable's value to an empty string
        self.variable.set(value="")

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the DATE_SELECT_FIELD_CLEARED event
            self.dispatcher.dispatch(
                event=Events.DATE_SELECT_FIELD_CLEARED,
                label=self.display_name,
                namespace=self.namespace,
                value=self.variable.get(),
            )

    def configure_clear_button(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the 'clear button' button widget in the date select field.

        This method configures the 'clear button' button widget in the date select field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the 'clear button' button widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                'clear button' button widget.
        """
        try:
            # Attempt to configure the 'clear button' button widget
            self._clear_button.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_clear_button' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_select_button(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the 'select button' button widget in the date select field.

        This method configures the 'select button' button widget in the date select field
        using the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments to be passed to the configure method
                of the 'select button' button widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to configure the
                'select button' button widget.
        """
        try:
            # Attempt to configure the 'select button' button widget
            self._select_button.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_select_button' method from '{self.__class__.__name__}' class: {e}"
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
        Configures the entry widget in the date select field.

        This method configures the entry widget in the date select field
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
            # Attempt to configure the entry widget
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
        Configures the grid layout of the DateSelectField widget.

        This method sets the column and row weights for the internal layout of the DateSelectField.
        It ensures proper resizing behavior and alignment of label, entry, and buttons.

        Columns:
            - Column 0: Label (fixed width)
            - Column 1: Entry field (expandable)
            - Column 2: Select button (fixed width)
            - Column 3: Clear button (fixed width)

        Rows:
            - Row 0: Main field layout (fixed height)
            - Row 1: Optional warning label (fixed height)

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

        # Set the weight of the 1st row to 0
        # This means that the row will not stretch when the window is resized
        self.grid_rowconfigure(
            index=1,
            weight=0,
        )

    def configure_label(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the label widget in the date select field.

        This method configures the label widget in the date select field
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

    def create_widgets(
        self,
        label: str,
        **kwargs,
    ) -> None:
        """
        Creates all internal widgets: label, entry, buttons, and warning label.

        Args:
            label (str): The label to be displayed.
            **kwargs: Optional widget-specific configuration (label, entry, buttons).

        Returns:
            None
        """

        # Create a label widget
        self._label: tkinter.Label = tkinter.Label(
            master=self,
            text=label,
            **kwargs.get(
                "label",
               {}
            )
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
        self.variable: tkinter.StringVar = tkinter.StringVar(
            value=Miscellaneous.datetime_to_string(
                datetime=Miscellaneous.get_current_datetime()
            )
        )

        # Create an entry widget
        self._entry: tkinter.Entry = tkinter.Entry(
            master=self,
            textvariable=self.variable,
            **kwargs.get(
                "entry",
               {}
            )
        )

       # Place the entry widget within the grid
        self._entry.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Bind the 'on_entry_change' method to the entry widget via the '<KeyRelease>' event
        self._entry.bind(
            func=self._on_entry_change,
            sequence="<KeyRelease>",
        )

        # Check, if the 'readonly' key is within kwargs and if so, True
        if kwargs.get("readonly", False):
            # Configure the tkinter.Entry entry widget's state to 'readonly'
            self._entry.configure(state="readonly")

        # Create the 'clear button' button widget
        self._clear_button: tkinter.Button = tkinter.Button(
            command=lambda: self.clear(dispatch=True),
            master=self,
            text="X",
            **kwargs.get(
                "clear_button",
               {}
            )
        )

       # Place the 'clear button' button widget within the grid
        self._clear_button.grid(
            column=2,
            padx=5,
            pady=5,
            row=0,
        )

        # Create the 'select button' button widget
        self._select_button: tkinter.Button = tkinter.Button(
            command=self._on_select_button_click,
            master=self,
            text="Select",
            **kwargs.get(
                "select_button",
               {}
            )
        )

       # Place the 'select button' button widget within the grid
        self._select_button.grid(
            column=3,
            padx=5,
            pady=5,
            row=0,
        )

        # Create the 'warning label' label widget
        self.warning_label: tkinter.Label = tkinter.Label(
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.RED["default"],
            master=self,
            text=f"Entry value '{self.variable.get()}' is not in a valid format. Expected: '{self.date_format}'.",
        )        

    def get(
        self,
        dispatch: bool = False,
    ) -> Tuple[str, Optional[datetime]]:
        """
        Returns the field's current value as a datetime object.

        Args:
            dispatch (bool): Whether to dispatch a get event.

        Returns:
            Tuple[str, Optional[datetime]]: The field's label and parsed datetime.
        """

        # Obtain the label and value strings from the widgets
        (
            label,
            value,
        ) = (
            self.display_name,
            Miscellaneous.string_to_datetime(
                date_string=self.variable.get(),
                format=self.date_format,
            ),
        )

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the DATE_SELECT_FIELD_GET event
            self.dispatcher.dispatch(
                event=Events.DATE_SELECT_FIELD_GET,
                label=label,
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
        value: Union[datetime, str],
        dispatch: bool = False,
    ) -> None:
        """
        Sets the value of the field either from string or datetime.

        Args:
            value (Union[datetime, str]): The value to set.
            dispatch (bool): Whether to dispatch a set event.

        Returns:
            None
        """

        # Check, if the passed value is a string
        if isinstance(
            value,
            str,
        ):
            # Update the variable with the passed value
            self.variable.set(value=value)
            
            # Attempt to convert the string to a datetime object
            value = Miscellaneous.string_to_datetime(
                date_string=value,
                format=self.date_format,
            )

        if value is None:
            # Log a warning message
            self.logger.warning(
                message=f"The passed value did not match expected format of '{self.date_format}'. This is likely a bug."
            )

            # Update the variable with an empty string
            self.variable.set(value="")

            # Return early
            return

        # Check, if the dispatch flag is set to True
        if dispatch:
            # Dispatch the DATE_SELECT_FIELD_SET event
            self.dispatcher.dispatch(
                event=Events.DATE_SELECT_FIELD_SET,
                label=self.display_name,
                namespace=self.namespace,
                value=self.variable.get(),
            )
