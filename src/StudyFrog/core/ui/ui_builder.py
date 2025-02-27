"""
Author: lodego
Date: 2025-02-08
"""

import re

import tkinter

from typing import *

from tkinter import ttk

from tkinter.constants import *

from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherEvent
from utils.events import Events
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous


__all__: List[str] = ["UIBuilder"]


class UIBuilder:
    """
    A utility class for building user interface components.

    Attributes:
        logger (Logger): The logger instance used by the class.
    """

    logger: Logger = Logger.get_logger(name="UIBuilder")

    @classmethod
    def get_bool_variable(
        cls,
        master: Optional[tkinter.Misc] = None,
        name: Optional[str] = None,
        value: Optional[Any] = False,
    ) -> Optional[tkinter.BooleanVar]:
        """
        Creates and returns a new instance of tkinter.BooleanVar.

        Args:
            name (str): The name of the variable.

        Returns:
            tkinter.BooleanVar: The created tkinter.BooleanVar instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.BooleanVar.
        """
        try:
            # Attempt to create and return a new instance of tkinter.BooleanVar
            return tkinter.BooleanVar(
                master=master,
                name=name,
                value=value,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_bool_variable' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_button(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[tkinter.Button]:
        """
        Creates and returns a new instance of tkinter.Button.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Button constructor.

        Returns:
            Optional[ttk.Button]: The created tkinter.Button instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Button.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Button
            return tkinter.Button(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_button' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_canvas(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[tkinter.Canvas]:
        """
        Creates and returns a new instance of tkinter.Canvas.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Canvas constructor.

        Returns:
            Optional[ttk.Canvas]: The created tkinter.Canvas instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Canvas.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Canvas
            return tkinter.Canvas(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_canvas' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_checkbutton(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[tkinter.Checkbutton]:
        """
        Creates and returns a new instance of tkinter.Checkbutton.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Checkbutton constructor.

        Returns:
            Optional[ttk.Checkbutton]: The created tkinter.Checkbutton instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Checkbutton.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Checkbutton
            return tkinter.Checkbutton(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_checkbutton' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_clock(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of tkinter.Label that displays the current datetime.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Label constructor.

        Returns:
            Optional[Dict[str, Any]]: The created tkinter.Label instance or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Label.
        """
        try:

            def update_clock() -> None:
                """
                Updates the text of the label to the current datetime.

                This function is scheduled to be called every 1000 milliseconds using the after method of the label widget.

                Returns:
                    None
                """
                # Set the text of the label to the current datetime
                result["label"]["text"] = Miscellaneous.datetime_to_string(
                    datetime=Miscellaneous.get_current_datetime(),
                    format="%H:%M:%S",
                )

                # Schedule the next call to update the clock
                result["label"].after(
                    ms=1000,
                    func=update_clock,
                )

            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(master=master)

            # Configure the "Root" frame widget's 1st column to weight 1
            result["root"].grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the "Root" frame widget's 1st row to weight 1
            result["root"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the "Label" label widget
            result["label"] = cls.get_label(
                master=result["root"],
                text=Miscellaneous.datetime_to_string(
                    datetime=Miscellaneous.get_current_datetime(),
                    format="%H:%M:%S",
                ),
                **kwargs,
            )

            # Grid the "Label" label widget in the "Root" frame widget
            result["label"].grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Start the clock
            update_clock()

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_clock' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_combobox(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[ttk.Combobox]:
        """
        Creates and returns a new instance of ttk.Combobox.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the ttk.Combobox constructor.

        Returns:
            Optional[ttk.Combobox]: The created ttk.Combobox instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Combobox.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Combobox
            return ttk.Combobox(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_combobox' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_combobox_select_field(
        cls,
        label: str,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a combobox widget with associated label and button.

        The returned dictionary contains the following keys:
            - "root": The container frame for the widgets
            - "label": The label widget
            - "combobox": The combobox widget
            - "button": The button widget

        Args:
            label (str): The text for the label widget.
            master (tkinter.Misc): The master widget for placing the container frame.
            **kwargs: Additional keyword arguments for the combobox widget.

        Returns:
            Optional[Dict[str, Any]]: The created combobox widget dictionary.

        Raises:
            Exception: If an exception occurs while attempting to create the combobox widget.
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def clear() -> None:
                """
                Clears the content of the combobox widget.

                Returns:
                    None
                """

                # Set the content of the combobox widget to an empty string
                result["combobox"].set("")

            def get() -> Optional[str]:
                """
                Retrieves the content of the combobox widget.

                Returns:
                    Optional[str]: The content of the combobox widget.
                """

                # Attempt to obtain the current value of the combobox widget
                string: Optional[str] = result["combobox"].get()

                # Check, if the content of the combobox widget is an empty string
                if string == "" or string is None:
                    # Return early
                    return None

                # Return the content of the combobox widget
                return string

            def set(value: str) -> None:
                """
                Sets the content of the combobox widget.

                Args:
                    value (str): The value to set the combobox widget to.

                Returns:
                    None
                """

                # Set the content of the combobox widget to the given value
                result["combobox"].set(value)

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(master=master)

            # Configure the "Root" frame widget's 1st and 3rd column to weight 0
            result["root"].grid_columnconfigure(
                index=(
                    0,
                    2,
                ),
                weight=0,
            )

            # Configure the "Root" frame widget's 2nd column to weight 1
            result["root"].grid_columnconfigure(
                index=1,
                weight=1,
            )

            # Configure the "Root" frame widget's 1st row to weight 1
            result["root"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the "Label" label widget
            result["label"] = cls.get_label(
                master=result["root"],
                text=label,
            )

            # Grid the "Label" label widget in the "Root" frame widget
            result["label"].grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the "Combobox" combobox widget
            result["combobox"] = cls.get_combobox(
                master=result["root"],
                **kwargs,
            )

            # Grid the "Combobox" combobox widget in the "Root" frame widget
            result["combobox"].grid(
                column=1,
                row=0,
                sticky=NSEW,
            )

            # Create the "Button" button widget
            result["button"] = cls.get_button(
                command=clear,
                master=result["root"],
                text="Clear",
            )

            # Grid the "Button" button widget in the "Root" frame widget
            result["button"].grid(
                column=2,
                padx=5,
                pady=5,
                row=0,
            )

            # Add the clearer function to the result dictionary
            result["clearer"] = clear

            # Add the getter function to the result dictionary
            result["getter"] = get

            # Add the setter function to the result dictionary
            result["setter"] = set

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_combobox_select_field' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_date_entry(
        cls,
        label: str,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a date entry widget with associated label and button.

        The returned dictionary contains the following keys:
            - "root": The container frame for the widgets
            - "label": The label widget
            - "entry": The entry widget with validation
            - "button": The button widget for clearing the entry
            - "clearer": A function to clear the entry content
            - "getter": A function to retrieve the entry content
            - "setter": A function to set the entry content
            - "validator": A function to validate the entry content

        Args:
            label (str): The text for the label widget.
            master (tkinter.Misc): The master widget for placing the container frame.
            **kwargs: Additional keyword arguments for the entry widget.

        Returns:
            Optional[Dict[str, Any]]: The created widgets dictionary or None if an exception occurs.
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def clear() -> None:
                """
                Clears the content of the entry widget.

                Returns:
                    None
                """

                # Delete the content of the entry widget
                result["entry"].delete(
                    0,
                    END,
                )

            def get() -> Optional[str]:
                """
                Retrieves the content of the entry widget.

                Returns:
                    Optional[str]: The content of the entry widget.
                """

                # Attempt to obtain the current value of the entry widget
                string: Optional[str] = result["entry"].get()

                # Check, if the content of the entry widget is an empty string
                if string == "" or string is None:
                    # Return early
                    return None

                # Return the content of the entry widget
                return string

            def on_key_release() -> None:
                """
                Validates the date format (YYYY-MM-DD) and checks if it's a valid calendar date.

                Called when a key is released in the entry widget.

                Returns:
                    None
                """

                # Attempt to validate the date format and check if it's a valid calendar date
                if validate(value=get()):
                    # If the date is valid, set the entry background to white and the warning text to empty
                    result["entry"].configure(
                        background=Constants.WHITE,
                    )

                    # Configure the "Warner" label widget to display no text
                    result["warner"].configure(
                        foreground=Constants.RED["200"],
                        text="",
                    )

                    # Hide the "Warner" label widget
                    result["warner"].grid_forget()
                else:
                    # If the date is invalid, set the entry background to red and display a warning message
                    result["entry"].configure(
                        background=Constants.RED["200"],
                    )

                    # Display a warning message
                    result["warner"].configure(
                        foreground=Constants.RED["200"],
                        text="Invalid date format! Use YYYY-MM-DD",
                    )

                    # Place the "Warner" label widget within the "Root" frame widget
                    result["warner"].grid(
                        column=1,
                        padx=5,
                        pady=5,
                        row=1,
                    )

            def set(value: str) -> None:
                """
                Sets the content of the entry widget.

                Args:
                    value (str): The content to set in the entry widget.

                Returns:
                    None
                """

                # Delete the content of the entry widget
                result["entry"].delete(
                    0,
                    END,
                )

                # Insert the new content into the entry widget
                result["entry"].insert(
                    0,
                    value,
                )

            def validate(value: str) -> bool:
                """
                Validates a date string against the default date format and checks if it's a valid date.

                Args:
                    value (str): The date string to validate.

                Returns:
                    bool: True if the date string is valid, False otherwise.
                """

                # Check if the value matches the default date format pattern
                if not re.match(
                    pattern=Constants.DEFAULT_DATE_FORMAT,
                    string=value,
                ):
                    return False

                try:
                    # Attempt to convert the string to a datetime object
                    Miscellaneous.string_to_datetime(
                        date_string=value,
                        format="%Y-%m-%d",
                    )
                    return True
                except ValueError:
                    # Return False if conversion raises a ValueError
                    return False

            # Create a container frame to hold the label, entry, and button widgets
            result["root"] = cls.get_frame(master=master)

            # Configure the "Root" frame widget's 1st and 2nd column to weight 0
            result["root"].grid_columnconfigure(
                index=(
                    0,
                    2,
                ),
                weight=0,
            )

            # Configure the "Root" frame widget's 2nd column to weight 1
            result["root"].grid_columnconfigure(
                index=1,
                weight=1,
            )

            # Configure the "Root" frame widget's 1st row to weight 1
            result["root"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the "Label" widget
            result["label"] = cls.get_label(
                master=result["root"],
                text=label,
            )

            # Place the "Label" widget within the "Root" frame
            result["label"].grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the "Entry" widget
            result["entry"] = cls.get_entry(
                master=result["root"],
                **kwargs,
            )

            # Configure the "Entry" widget with validation
            result["entry"].bind(
                func=lambda event: on_key_release,
                sequence="<KeyRelease>",
            )

            # Place the "Entry" widget within the "Root" frame
            result["entry"].grid(
                column=1,
                row=0,
                sticky=NSEW,
            )

            # Create the "Button" widget
            result["button"] = cls.get_button(
                command=clear,
                master=result["root"],
                text="Clear",
            )

            # Place the "Button" widget within the "Root" frame widget
            result["button"].grid(
                column=2,
                padx=5,
                pady=5,
                row=0,
            )

            # Create the "Warner" label
            result["warner"] = cls.get_label(
                foreground=Constants.RED["200"],
                master=result["root"],
                text="",
            )

            # Place the "Warner" label within the "Root" frame
            result["warner"].grid_forget()

            # Assign the clearer function to the result dictionary
            result["clearer"] = clear

            # Assign the getter function to the result dictionary
            result["getter"] = get

            # Assign the setter function to the result dictionary
            result["setter"] = set

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_date_entry' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occurred
            return None

    @classmethod
    def get_entry(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[tkinter.Entry]:
        """
        Creates and returns a new instance of tkinter.Entry.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Entry constructor.

        Returns:
            Optional[ttk.Entry]: The created tkinter.Entry instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Entry.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Entry
            return tkinter.Entry(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_entry' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_float_spinbox_field(
        cls,
        label: str,
        master: tkinter.Misc,
        step_size: float = 1.0,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of a tkinter widgets dictionary for a float spinbox field.

        The returned dictionary contains the following keys:
            - "root": The container frame for the widgets
            - "label": The label widget
            - "variable": The tkinter.DoubleVar variable
            - "decrement_button": The decrement button widget
            - "entry": The entry widget
            - "increment_button": The increment button widget
            - "clearer": A function to clear the value of the variable
            - "getter": A function to retrieve the value of the variable
            - "setter": A function to set the value of the variable

        Args:
            label (str): The text for the label widget.
            master (tkinter.Misc): The master widget for placing the container frame.
            step_size (float): The step size for the float spinbox. Defaults to 1.0.
            **kwargs: Additional keyword arguments for the entry widget.

        Returns:
            Optional[Dict[str, Any]]: The created widgets dictionary or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create the tkinter widgets dictionary.
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def clear() -> None:
                """
                Clears the value of the variable.

                Returns:
                    None
                """

                # Set the value of the variable to 0
                result["variable"].set(value=0.0)

            def decrement() -> None:
                """
                Decrements the value of the variable by the step size.

                Returns:
                    None
                """

                # Decrement the value of the variable
                result["variable"].set(result["variable"].get() - step_size)

            def get() -> float:
                """
                Returns the current value of the variable.

                Returns:
                    float: The current value of the variable.
                """

                # Return the value of the variable
                return result["variable"].get()

            def increment() -> None:
                """
                Increments the value of the variable by the step size.

                Returns:
                    None
                """

                # Increment the value of the variable
                result["variable"].set(result["variable"].get() + step_size)

            def set(value: float) -> None:
                """
                Sets the value of the variable.

                Args:
                    value (float): The value to set the variable to.

                Returns:
                    None
                """

                # Set the value of the variable
                result["variable"].set(value=value)

            # Create the "Variable" tkinter.DoubleVar variable
            result["variable"] = cls.get_double_variable(value=0.0)

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(master=master)

            # Configure the "Root" frame widget's 0th column to weight 1
            result["root"].grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the "Root" frame widget's 1st column to weight 0
            result["root"].grid_columnconfigure(
                index=1,
                weight=0,
            )

            # Configure the "Root" frame widget's 2nd column to weight 1
            result["root"].grid_columnconfigure(
                index=2,
                weight=1,
            )

            # Configure the "Root" frame widget's 3rd column to weight 0
            result["root"].grid_columnconfigure(
                index=3,
                weight=0,
            )

            # Configure the "Root" frame widget's 1st row to weight 1
            result["root"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the "Label" label widget
            result["label"] = cls.get_label(
                master=result["root"],
                text=label,
            )

            # Create the "Decrement" button widget
            result["decrement_button"] = cls.get_button(
                command=decrement,
                master=result["root"],
                text="-",
            )

            # Create the "Entry" entry widget
            result["entry"] = cls.get_entry(
                master=result["root"],
                state="readonly",
                textvariable=result["variable"],
                **kwargs,
            )

            # Create the "Increment" button widget
            result["increment_button"] = cls.get_button(
                command=increment,
                master=result["root"],
                text="+",
            )

            # Add the clear function to the result dictionary
            result["clearer"] = clear

            # Add the getter function to the result dictionary
            result["getter"] = get

            # Add the setter function to the result dictionary
            result["setter"] = set

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_float_spinbox_field' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_float_variable(
        cls,
        master: Optional[tkinter.Misc] = None,
        name: Optional[str] = None,
        value: Optional[float] = 0.0,
    ) -> Optional[tkinter.DoubleVar]:
        """
        Creates and returns a new instance of tkinter.DoubleVar.

        Args:
            master (Optional[Any]): The master widget.
            name (Optional[str]): The name of the variable.
            value (Optional[float]): The initial value of the variable.

        Returns:
            Optional[tkinter.DoubleVar]: The created tkinter.DoubleVar instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.DoubleVar.
        """
        try:
            # Attempt to create and return a new instance of tkinter.DoubleVar
            return tkinter.DoubleVar(
                master=master,
                name=name,
                value=value,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_float_variable' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_frame(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[tkinter.Frame]:
        """
        Creates and returns a new instance of tkinter.Frame.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Frame constructor.

        Returns:
            Optional[ttk.Frame]: The created tkinter.Frame instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Frame.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Frame
            return tkinter.Frame(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_frame' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_int_variable(
        cls,
        master: Optional[tkinter.Misc] = None,
        name: Optional[str] = None,
        value: Optional[int] = 0,
    ) -> Optional[tkinter.IntVar]:
        """
        Creates and returns a new instance of tkinter.IntVar.

        Args:
            master (Optional[Any]): The master widget.
            name (Optional[str]): The name of the variable.
            value (Optional[int]): The initial value of the variable.

        Returns:
            Optional[tkinter.IntVar]: The created tkinter.IntVar instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.IntVar.
        """
        try:
            # Attempt to create and return a new instance of tkinter.IntVar
            return tkinter.IntVar(
                master=master,
                name=name,
                value=value,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_int_variable' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_integer_spinbox_field(
        cls,
        label: str,
        master: tkinter.Misc,
        setp_size: int = 1,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of a tkinter widgets dictionary for an integer spinbox field.

        The returned dictionary contains the following keys:
            - "root": The container frame for the widgets
            - "label": The label widget
            - "variable": The tkinter.IntVar variable
            - "decrement_button": The decrement button widget
            - "entry": The entry widget
            - "increment_button": The increment button widget
            - "clearer": A function to clear the value of the variable
            - "getter": A function to retrieve the value of the variable
            - "setter": A function to set the value of the variable

        Args:
            label (str): The text for the label widget.
            master (tkinter.Misc): The master widget for placing the container frame.
            setp_size (int): The step size for the integer spinbox. Defaults to 1.
            **kwargs: Additional keyword arguments for the entry widget.

        Returns:
            Optional[Dict[str, Any]]: The created widgets dictionary or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.IntVar.
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def clear() -> None:
                """
                Clears the value of the variable.

                Returns:
                    None
                """

                # Set the value of the variable to 0
                result["variable"].set(value=0)

            def decrement() -> None:
                """
                Decrements the value of the variable by the step size.

                Returns:
                    None
                """

                # Decrement the value of the variable
                result["variable"].set(result["variable"].get() - setp_size)

            def get() -> int:
                """
                Returns the current value of the variable.

                Returns:
                    int: The current value of the variable.
                """

                # Return the value of the variable
                return result["variable"].get()

            def increment() -> None:
                """
                Increments the value of the variable by the step size.

                Returns:
                    None
                """

                # Increment the value of the variable
                result["variable"].set(result["variable"].get() + setp_size)

            def set(value: int) -> None:
                """
                Sets the value of the variable.

                Args:
                    value (int): The value to set the variable to.

                Returns:
                    None
                """

                # Set the value of the variable
                result["variable"].set(value=value)

            # Create the "Variable" tkinter.IntVar variable
            result["variable"] = cls.get_int_variable(value=0)

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(master=master)

            # Configure the "Root" frame widget's 0th column to weight 1
            result["root"].grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the "Root" frame widget's 1st column to weight 0
            result["root"].grid_columnconfigure(
                index=1,
                weight=0,
            )

            # Configure the "Root" frame widget's 2nd column to weight 1
            result["root"].grid_columnconfigure(
                index=2,
                weight=1,
            )

            # Configure the "Root" frame widget's 3rd column to weight 0
            result["root"].grid_columnconfigure(
                index=3,
                weight=0,
            )

            # Configure the "Root" frame widget's 1st row to weight 1
            result["root"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the "Label" label widget
            result["label"] = cls.get_label(
                master=result["root"],
                text=label,
            )

            # Create the "Decrement" button widget
            result["decrement_button"] = cls.get_button(
                command=decrement,
                master=result["root"],
                text="-",
            )

            # Create the "Entry" entry widget
            result["entry"] = cls.get_entry(
                master=result["root"],
                state="readonly",
                textvariable=result["variable"],
                **kwargs,
            )

            # Create the "Increment" button widget
            result["increment_button"] = cls.get_button(
                command=increment,
                master=result["root"],
                text="+",
            )

            # Add the clearer function to the result dictionary
            result["clearer"] = clear

            # Add the getter function to the result dictionary
            result["getter"] = get

            # Add the setter function to the result dictionary
            result["setter"] = set

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_integer_spinbox_field' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_label(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[tkinter.Label]:
        """
        Creates and returns a new instance of tkinter.Label.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Label constructor.

        Returns:
            Optional[tkinter.Label]: The created tkinter.Label instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Label.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Label
            return tkinter.Label(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_label' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_listbox(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[tkinter.Listbox]:
        """
        Creates and returns a new instance of tkinter.Listbox.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Listbox constructor.

        Returns:
            Optional[tkinter.Listbox]: The created tkinter.Listbox instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Listbox.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Listbox
            return tkinter.Listbox(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_listbox' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_menu(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[tkinter.Menu]:
        """
        Creates and returns a new instance of tkinter.Menu.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Menu constructor.

        Returns:
            Optional[tkinter.Menu]: The created tkinter.Menu instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Menu.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Menu
            return tkinter.Menu(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_menu' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_menubutton(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[tkinter.Menubutton]:
        """
        Creates and returns a new instance of tkinter.Menubutton.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Menubutton constructor.

        Returns:
            Optional[tkinter.Menubutton]: The created tkinter.Menubutton instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Menubutton.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Menubutton
            return tkinter.Menubutton(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_menubutton' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_multiple_choice_answer_field(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def clear() -> None:
                """
                Clears the value of the multiple choice answer field.

                Returns:
                    None
                """

                # Delete the current content of the entry widget
                result["entry"].delete(
                    0,
                    END,
                )

            def get() -> Optional[Dict[str, Any]]:
                """
                Retrieves the value of the multiple choice answer field.

                The value is stored in a dictionary with the following keys:
                    - "value": The value of the multiple choice answer field.
                    - "is_correct": A boolean indicating whether the answer is correct or not.

                If the value is an empty string or the is_correct variable is None, the value is set to None.

                Returns:
                    Optional[Dict[str, Any]]: The dictionary containing the value of the multiple choice answer field or None if an exception occurs.
                """

                # Initialize the dictionary as an empty dictionary
                dictionary: Dict[str, Any] = {}

                # Get the value of the is_correct variable
                dictionary["is_correct"] = result["is_correct"].get()

                # Get the value of the entry widget
                dictionary["value"] = result["entry"].get()

                if dictionary["value"] == "" or dictionary["is_correct"] is None:
                    # If the value is empty or the is_correct variable is None, set the value to None
                    dictionary["value"] = None

                # Return the dictionary
                return dictionary

            def set(value: str) -> None:
                """
                Sets the value of the multiple choice answer field.

                Args:
                    value (str): The value to set.

                Returns:
                    None
                """

                # Delete the current content of the entry widget
                result["entry"].delete(
                    0,
                    END,
                )

                # Insert the new value into the entry widget
                result["entry"].insert(
                    0,
                    value,
                )

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(master=master)

            # Configure the "Root" frame widget's 1st column to weight 0
            result["root"].grid_columnconfigure(
                index=0,
                weight=0,
            )

            # Configure the "Root" frame widget's 2nd column to weight 1
            result["root"].grid_columnconfigure(
                index=1,
                weight=1,
            )

            # Configure the "Root" frame widget's 1st row to weight 0
            result["root"].grid_rowconfigure(
                index=0,
                weight=0,
            )

            # Create the "Is correct" boolean variable
            result["is_correct"] = cls.get_bool_variable(value=False)

            # Create the "Check button" checkbutton widget
            result["checkbutton"] = cls.get_checkbutton(
                master=result["root"],
                text="Is correct? ",
                variable=result["is_correct"],
            )

            # Place the "Check button" checkbutton widget in the "Root" frame widget
            result["checkbutton"].grid(
                row=0,
                column=0,
                sticky=NSEW,
            )

            # Create the "Entry" entry widget
            result["entry"] = cls.get_entry(
                master=result["root"],
                **kwargs,
            )

            # Place the "Entry" entry widget in the "Root" frame widget
            result["entry"].grid(
                row=0,
                column=1,
                sticky=NSEW,
            )

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_multiple_choice_answer_field' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_multi_line_text_field(
        cls,
        label: str,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns various widgets required to create a multi-line text field.

        The created widgets are stored in a dictionary and returned to the caller.

        The dictionary contains the following keys:
            - "root": The master widget (Call your geometry manager (.place, .grid, .pack, etc.) on this widget)
            - "label": The label widget
            - "text": The text widget
            - "button": The button widget
            - "clear": A function to clear all content from the text widget
            - "get": A function to get the content of the text widget
            - "set": A function to set the content of the text widget

        Returns:
            Optional[Dict[str, Any]]: The created widgets dictionary or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create the widgets
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def clear() -> None:
                """
                Clears the content of the text widget.

                Returns:
                    None
                """

                # Delete all content from the text widget
                result["text"].delete(
                    "1.0",
                    END,
                )

            def get() -> Optional[str]:
                """
                Retrieves the content of the text widget.

                Returns:
                    Optional[str]: The content of the text widget.
                """

                # Attempt to obtain the current value of the text widget
                string: Optional[str] = result["text"].get(
                    "1.0",
                    END,
                )

                # Check, if the content of the text widget is an empty string
                if string == "":
                    # Return early
                    return None

                # Return the content of the text widget
                return string

            def set(value: str) -> None:
                """
                Sets the content of the text widget to the given value.

                Args:
                    value (str): The value to set the content of the text widget to.

                Returns:
                    None
                """

                # Delete all content from the text widget
                result["text"].delete(
                    "1.0",
                    END,
                )

                # Insert the given value into the text widget
                result["text"].insert(
                    "1.0",
                    value,
                )

            # Create the "Root Frame" frame widget
            result["root"] = cls.get_frame(master=master)

            # Configure the "Root Frame" frame widget's 1st and 3rd column to weight 0
            result["root"].grid_columnconfigure(
                index=(
                    0,
                    2,
                ),
                weight=0,
            )

            # Configure the "Root Frame" frame widget's 2nd column to weight 1
            result["root"].grid_columnconfigure(
                index=1,
                weight=1,
            )

            # Configure the "Root Frame" frame widget's 1st and 3rd column to weight 0
            result["root"].grid_rowconfigure(
                index=(
                    0,
                    2,
                ),
                weight=0,
            )

            # Configure the "Root Frame" frame widget's 1st row to weight 1
            result["root"].grid_rowconfigure(
                index=1,
                weight=1,
            )

            # Create the "Label" label widget
            result["label"] = cls.get_label(
                master=result["root"],
                text=label,
            )

            # Configure the "Label" label widget's grid properties
            result["label"].grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the "Text" text widget
            result["text"] = cls.get_text(
                master=result["root"],
                **kwargs,
            )

            # Configure the "Text" text widget's grid properties
            result["text"].grid(
                column=1,
                row=1,
                sticky=NSEW,
            )

            # Create the "Clear" button widget
            result["button"] = cls.get_button(
                command=clear,
                master=result["root"],
                text="Clear",
            )

            # Grid the button widget
            result["button"].grid(
                column=2,
                padx=5,
                pady=5,
                row=2,
            )

            # Add the "clearer" function to the result dictionary
            result["clearer"] = clear

            # Add the "getter" function to the result dictionary
            result["getter"] = get

            # Add the "setter" function to the result dictionary
            result["setter"] = set

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_multi_line_text_field' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_multi_select_field(
        cls,
        label: str,
        master: tkinter.Misc,
        values: List[str],
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            # Initialize the "Listbox" key as None
            result["listbox"] = None

            # Initialize the "Toplevel" key as None
            result["toplevel"] = None

            # Initialize the "Selection" key as an empty list
            result["selection"] = []

            def clear() -> None:
                pass

            def get() -> Optional[List[str]]:
                pass

            def on_listbox_select(event: Optional[tkinter.Event] = None) -> None:
                pass

            def on_select_button_click() -> None:
                # Check, if the "Toplevel" key is associated with a value
                if not result.get(
                    "toplevel",
                    None,
                ):
                    # Create the "Toplevel" toplevel widget
                    result["toplevel"] = cls.get_toplevel()

            def set(value: List[str]) -> None:
                pass

            def update_selection_display() -> None:
                pass

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(master=master)

            # Configure the "Root" frame widget's 1st column to weight 0
            result["root"].grid_columnconfigure(
                index=0,
                weight=0,
            )

            # Configure the "Root" frame widget's 2nd column to weight 1
            result["root"].grid_columnconfigure(
                index=1,
                weight=1,
            )

            # Configure the "Root" frame widget's 3rd column to weight 0
            result["root"].grid_columnconfigure(
                index=2,
                weight=0,
            )

            # Create the "Label" widget
            result["label"] = cls.get_label(
                master=result["root"],
                text=label,
            )

            # Place the "Label" label widget in the "Root" frame widget
            result["label"].grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the "Container" frame widget
            result["container"] = cls.get_frame(master=result["root"])

            # Place the "Container" frame widget in the "Root" frame widget
            result["container"].grid(
                column=1,
                row=0,
                sticky=NSEW,
            )

            # Create the "Select button" button widget
            result["select_button"] = cls.get_button(
                master=result["root"],
                text="Select",
            )

            # Place the "Select button" button widget in the "Root" frame widget
            result["select_button"].grid(
                column=2,
                row=0,
                sticky=NSEW,
            )

            # Add the clearer function to the result dictionary
            result["clearer"] = clear

            # Add the getter function to the result dictionary
            result["getter"] = get

            # Add the setter function to the result dictionary
            result["setter"] = set

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_multi_select_field' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_notebook(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[ttk.Notebook]:
        """
        Creates and returns a new instance of ttk.Notebook.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the ttk.Notebook constructor.

        Returns:
            Optional[ttk.Notebook]: The created ttk.Notebook instance or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of ttk.Notebook.
        """
        try:
            # Attempt to create and return a new instance of ttk.Notebook
            return ttk.Notebook(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_notebook' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_okay(
        cls,
        dispatcher: Dispatcher,
        message: str,
        title: str,
        master: Optional[tkinter.Misc],
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of a dialog with an "Okay" button.

        Args:
            dispatcher (Dispatcher): The dispatcher to use for dispatching events.
            message (str): The message to display in the dialog.
            title (str): The title of the dialog.
            master (Optional[tkinter.Misc]): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the get_toplevel method.

        Returns:
            Optional[Dict[str, Any]]: The created dialog instance or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of the dialog.
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def on_okay_click() -> None:
                """
                Called when the "Okay" button is clicked.

                Dispatches an event to the global namespace with the target "okay".

                Returns:
                    None
                """
                dispatcher.dispatch(
                    event=Events.OKAY_BUTTON_CLICKED,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    source="ui:dialog:okay",
                    target="okay",
                )

                # Set the result to "okay"
                result["result"] = "okay"

                # Destroy the "Root" toplevel widget
                result["root"].destroy()

            def get() -> Optional[str]:
                """
                Gets the value at key "result" in dictionary "result" and returns it.

                Returns:
                    Optional[str]: The value at key "result" in dictionary "result" or None if the key is not found.
                """
                # Return the value at key "result" in dictionary "result"
                return result.get(
                    "result",
                    None,
                )

            # Create the "Root" toplevel widget
            result["root"] = cls.get_toplevel(
                master=master,
                **kwargs,
            )

            # Configure the "Root" toplevel widget's 1st column to weight 1
            result["root"].grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the "Root" toplevel widget's 1st and 3rd row to weight 0
            result["root"].grid_rowconfigure(
                index=(
                    0,
                    2,
                ),
                weight=0,
            )

            # Configure the "Root" toplevel widget's 2nd row to weight 1
            result["root"].grid_rowconfigure(
                index=1,
                weight=1,
            )

            # Create the "Title" label widget
            result["title_label"] = cls.get_label(
                master=result["root"],
                text=title,
            )

            # Place the "Title" label widget within the "Root" toplevel widget
            result["title_label"].grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Create the "Message" label widget
            result["message_label"] = cls.get_label(
                master=result["root"],
                text=message,
            )

            # Place the "Message" label widget within the "Root" toplevel widget
            result["message_label"].grid(
                column=0,
                padx=5,
                pady=5,
                row=1,
                sticky=NSEW,
            )

            # Create the "Button" button widget
            result["button"] = cls.get_button(
                command=on_okay_click,
                master=result["root"],
                text="Okay",
            )

            # Place the "Button" button widget within the "Root" toplevel widget
            result["button"].grid(
                column=0,
                padx=5,
                pady=5,
                row=2,
            )

            # Configure the "Root" toplevel widget to be initially minimized
            result["root"].iconify()

            # Set the "Root" toplevel widget to have grab set
            result["root"].grab_set()

            # Set the "Root" toplevel widget to have focus
            result["root"].focus_set()

            # Ring the bell
            result["root"].bell()

            # Wait for the "Root" toplevel widget to be closed
            result["root"].wait_window()

            # Return the result
            return result
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_okay' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_okay_cancel(
        cls,
        dispatcher: Dispatcher,
        message: str,
        title: str,
        master: Optional[tkinter.Misc],
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of a dialog with "Okay" and "Cancel" buttons.

        Args:
            dispatcher (Dispatcher): The dispatcher to use for dispatching events.
            message (str): The message to display in the dialog.
            title (str): The title of the dialog.
            master (Optional[tkinter.Misc]): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the get_toplevel method.

        Returns:
            Optional[Dict[str, Any]]: The created dialog instance or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of the dialog.
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def on_button_click(string: str) -> None:
                """
                Called when any of the "Okay" or "Cancel" buttons is clicked.

                Dispatches an event to the global namespace with the target from the button.
                Sets the result to the target and destroys the "Root" toplevel widget.

                Args:
                    string (str): The string passed from the button. Can be either of "Okay" or "Cancel".

                Returns:
                    None
                """

                # Obtain an event based on the passed string
                event: DispatcherEvent = (
                    Events.CANCEL_BUTTON_CLICKED
                    if string == "Cancel"
                    else Events.OKAY_BUTTON_CLICKED
                )

                # Dispatch the event to the global namespace with the target from the button
                dispatcher.dispatch(
                    event=event,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    source=f"ui:dialog:{string}",
                    target=string,
                )

                # Set the result to the target
                result["result"] = string

                # Destroy the "Root" toplevel widget
                result["root"].destroy()

            def get() -> Optional[str]:
                """
                Gets the value at key "result" in dictionary "result" and returns it.

                Returns:
                    Optional[str]: The value at key "result" in dictionary "result" or None if the key is not found.
                """
                # Return the value at key "result" in dictionary "result"
                return result.get(
                    "result",
                    None,
                )

            # Create the "Root" toplevel widget
            result["root"] = cls.get_toplevel(
                master=master,
                **kwargs,
            )

            # Configure the "Root" toplevel widget's 1st column to weight 1
            result["root"].grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the "Root" toplevel widget's 1st and 3rd row to weight 0
            result["root"].grid_rowconfigure(
                index=(
                    0,
                    2,
                ),
                weight=0,
            )

            # Configure the "Root" toplevel widget's 2nd row to weight 1
            result["root"].grid_rowconfigure(
                index=1,
                weight=1,
            )

            # Create the "Title" label widget
            result["title_label"] = cls.get_label(
                master=result["root"],
                text=title,
            )

            # Place the "Title" label widget within the "Root" toplevel widget
            result["title_label"].grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Create the "Message" label widget
            result["message_label"] = cls.get_label(
                master=result["root"],
                text=message,
            )

            # Place the "Message" label widget within the "Root" toplevel widget
            result["message_label"].grid(
                column=0,
                padx=5,
                pady=5,
                row=1,
                sticky=NSEW,
            )

            # Create the "Button Frame" frame widget
            result["button_frame"] = cls.get_frame(
                master=result["root"],
            )

            # Configure the "Button Frame" frame widget's 1st and 2nd column to weight 1
            result["button_frame"].grid_columnconfigure(
                index=(
                    0,
                    1,
                ),
                weight=1,
            )

            # Place the "Button Frame" frame widget within the "Root" toplevel widget
            result["button_frame"].grid(
                column=0,
                padx=5,
                pady=5,
                row=2,
                sticky=NSEW,
            )

            # Create the "Cancel" button widget
            result["cancel_button"] = cls.get_button(
                command=lambda string="cancel": on_button_click(string=string),
                master=result["button_frame"],
                text="Cancel",
            )

            # Place the "Cancel" button widget within the "Button Frame" frame widget
            result["cancel_button"].grid(
                column=0,
                padx=5,
                pady=5,
                row=2,
            )

            # Create the "Okay" button widget
            result["okay_button"] = cls.get_button(
                command=lambda string="okay": on_button_click(string=string),
                master=result["button_frame"],
                text="Okay",
            )

            # Place the "Okay" button widget within the "Button Frame" frame widget
            result["okay_button"].grid(
                column=1,
                padx=5,
                pady=5,
                row=2,
            )

            # Configure the "Root" toplevel widget to be initially minimized
            result["root"].iconify()

            # Set the "Root" toplevel widget to have grab set
            result["root"].grab_set()

            # Set the "Root" toplevel widget to have focus
            result["root"].focus_set()

            # Ring the bell
            result["root"].bell()

            # Wait for the "Root" toplevel widget to be closed
            result["root"].wait_window()

            # Return the result
            return result
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_okay' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_open_answer_field(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a dictionary containing widgets to facilitate a open answer field.

        The widgets contained are:
            - "root" (tkinter.Frame): The root widget of the open answer field.
            - "label" (tkinter.Label): The label widget of the open answer field.
            - "container" (tkinter.Frame): The container widget of the text and scrollbar widgets.
            - "text" (tkinter.Text): The text widget of the open answer field.
            - "h_scrollbar" (tkinter.Scrollbar): The horizontal scrollbar of the text widget.
            - "v_scrollbar" (tkinter.Scrollbar): The vertical scrollbar of the text widget.
            - "button" (tkinter.Button): The clear button of the open answer field.

        Returns:
            Optional[Dict[str, Any]]: The created widgets dictionary or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create the widgets
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def clear() -> None:
                """
                Clears the value in the "text" Text widget.
                """

                # Delete the value in the "text" Text widget
                result["text"].delete(
                    "1.0",
                    END,
                )

            def get() -> Optional[str]:
                """
                Gets the value in the "text" Text widget and returns it.

                If the value is empty, None is returned.

                Returns:
                    Optional[str]: The value in the "text" Text widget or None if the value is empty.
                """

                # Get the value in the "text" Text widget
                string: str = result["text"].get(
                    "1.0",
                    END,
                )

                # If the string is empty, return None
                if string == "":
                    return None

                # Otherwise return the string
                return string

            def set(value: str) -> None:
                """
                Sets the value in the "text" Text widget.

                Args:
                    value (str): The value to set in the "text" Text widget.

                Returns:
                    None
                """

                # Delete the value in the "text" Text widget
                result["text"].delete(
                    "1.0",
                    END,
                )

                # Set the value in the "text" Text widget
                result["text"].insert(
                    "1.0",
                    value,
                )

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(master=master)

            # Configure the "Root" frame widget's 1st column to weight 0
            result["root"].grid_columnconfigure(
                index=0,
                weight=0,
            )

            # Configure the "Root" frame widget's 2nd column to weight 1
            result["root"].grid_columnconfigure(
                index=1,
                weight=1,
            )

            # Configure the "Root" frame widget's 3rd column to weight 0
            result["root"].grid_columnconfigure(
                index=2,
                weight=0,
            )

            # Configure the "Root" frame widget's 1st row to weight 0
            result["root"].grid_rowconfigure(
                index=0,
                weight=0,
            )

            # Configure the "Root" frame widget's 2nd row to weight 1
            result["root"].grid_rowconfigure(
                index=1,
                weight=1,
            )

            # Configure the "Root" frame widget's 3rd row to weight 0
            result["root"].grid_rowconfigure(
                index=2,
                weight=0,
            )

            # Create the "Label" label widget
            result["label"] = cls.get_label(
                master=result["root"],
                text="Enter here: ",
            )

            # Place the "Label" label widget within the "root" frame widget
            result["label"].grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Create the "Container" frame widget
            result["container"] = cls.get_frame(master=result["root"])

            # Configure the "Container" frame widget's 1st column to weight 1
            result["container"].grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the "Container" frame widget's 2nd column to weight 0
            result["container"].grid_columnconfigure(
                index=1,
                weight=0,
            )

            # Configure the "Container" frame widget's 1st row to weight 0
            result["container"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Configure the "Container" frame widget's 2nd row to weight 0
            result["container"].grid_rowconfigure(
                index=1,
                weight=0,
            )

            # Place the "container" frame widget within the "root" frame widget
            result["container"].grid(
                column=1,
                row=1,
                sticky=NSEW,
            )

            # Create the "text" Text widget
            result["text"] = cls.get_text(
                master=result["container"],
                **kwargs,
            )

            # Place the "text" Text widget within the "container" frame widget
            result["text"].grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the "v_scrollbar" Scrollbar widget
            result["v_scrollbar"] = cls.get_scrollbar(
                command=result["text"].yview,
                master=result["container"],
                orient=VERTICAL,
            )

            # Place the "v_scrollbar" Scrollbar widget within the "container" frame widget
            result["v_scrollbar"].grid(
                column=1,
                row=0,
                sticky=NS,
            )

            # Create the "h_scrollbar" Scrollbar widget
            result["h_scrollbar"] = cls.get_scrollbar(
                command=result["text"].xview,
                master=result["container"],
                orient=HORIZONTAL,
            )

            # Place the "h_scrollbar" Scrollbar widget within the "container" frame widget
            result["h_scrollbar"].grid(
                column=0,
                row=1,
                sticky=EW,
            )

            # Configure the "text" Text widget's xscrollcommand to result["h_scrollbar"].set
            result["text"].configure(
                xscrollcommand=result["h_scrollbar"].set,
                yscrollcommand=result["v_scrollbar"].set,
            )

            # Create the "button" Button widget
            result["button"] = cls.get_button(
                command=clear,
                master=result["root"],
                text="Clear",
            )

            # Place the "button" Button widget within the "root" frame widget
            result["button"].grid(
                column=2,
                padx=5,
                pady=5,
                row=2,
            )

            # Add the clearer function to the result dictionary
            result["clearer"] = clear

            # Add the getter function to the result dictionary
            result["getter"] = get

            # Add the setter function to the result dictionary
            result["setter"] = set

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_open_answer_field' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_progressbar(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[ttk.Progressbar]:
        """
        Creates and returns a new instance of ttk.Progressbar.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the ttk.Progressbar constructor.

        Returns:
            Optional[ttk.Progressbar]: The created ttk.Progressbar instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of ttk.Progressbar.
        """
        try:
            # Attempt to create and return a new instance of ttk.Progressbar
            return ttk.Progressbar(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_progressbar' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_radiobutton(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[tkinter.Radiobutton]:
        """
        Creates and returns a new instance of tkinter.Radiobutton.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Radiobutton constructor.

        Returns:
            Optional[tkinter.Radiobutton]: The created tkinter.Radiobutton instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Radiobutton.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Radiobutton
            return tkinter.Radiobutton(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_radiobutton' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_radiobutton_field(
        cls,
        labels: Iterable[str],
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of a radiobutton field.

        The created radiobutton field contains a frame widget as its root widget,
        and a checkbutton widget for each label passed as argument.

        The value of each checkbutton is stored in a tkinter.BooleanVar instance,
        which is stored in a dictionary under the key "variable_{index}".

        The checkbutton widgets are stored in a dictionary under the key "checkbuttons".
        The keys of the dictionary are the keys of the "checkbuttons" dictionary,
        and the values are the checkbutton widgets.

        The method returns a dictionary containing the created radiobutton field widgets and functions.

        Args:
            labels (Iterable[str]): The labels of the checkbuttons.
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Checkbutton constructor.

        Returns:
            Optional[Dict[str, Any]]: The created radiobutton field widgets and functions.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Checkbutton.
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def clear() -> None:
                """
                Deselects all radiobuttons.

                Returns:
                    None
                """

                # Iterate over all radiobuttons in the "Radiobuttons" dictionary
                for value in result["radiobuttons"].values():
                    # Deselect the radiobutton
                    value.deselect()

            def get() -> Optional[Dict[str, Any]]:
                """
                Retrieves the values of the radiobuttons and returns them in a dictionary.

                The keys of the dictionary are the keys of the "radiobuttons" dictionary,
                and the values are the values of the radiobuttons.

                Returns:
                    Optional[Dict[str, Any]]: The dictionary containing the values of the radiobuttons.
                """

                # Initialize the dictionary as an empty dictionary
                dictionary: Dict[str, Any] = {}

                # Iterate over the radiobuttons in the "Radiobuttons" dictionary
                for (
                    key,
                    value,
                ) in result["radiobuttons"].items():
                    # Get the value of the radiobutton
                    dictionary[key] = value.get()

                # Return the dictionary
                return dictionary

            def on_radiobutton_click(string: str) -> None:
                """
                Handles the click event of a radiobutton.

                Deselects all radiobuttons except the one that was clicked.

                Args:
                    string (str): The key of the radiobutton that was clicked.

                Returns:
                    None
                """

                # Iterate over all radiobuttons in the "Radiobuttons" dictionary
                for (
                    key,
                    value,
                ) in result["radiobuttons"].items():
                    # Check if the key is not the one that was clicked
                    if key != string:
                        # Deselect the radiobutton
                        value.deselect()

            def set(
                key: str,
                value: bool,
            ) -> None:
                """
                Sets the value of the radiobutton with the given key to the given value.

                Args:
                    key (str): The key of the radiobutton to be set.
                    value (bool): The value to which the radiobutton should be set.

                Returns:
                    None
                """

                # Check if the key is present in the "Radiobuttons" dictionary
                if key in result["radiobuttons"].keys():
                    # Set the value of the radiobutton with the given key to the given value
                    result["radiobuttons"][key].set(value=value)

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(master=master)

            # Configure the "Root" frame widget's 1st column to weight 1
            result["root"].grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Initialize the "Radiobuttons" dictionary as an empty dictionary
            result["radiobuttons"] = {}

            # Iterate over the passed labels
            for (
                index,
                label,
            ) in enumerate(iterable=labels):
                # Create a "Variable_{index}" tkinter.BooleanVar
                result[f"variable_{index}"] = cls.get_bool_variable(
                    master=result["root"],
                    value=False,
                )

                # Create a "Frame_{index}" frame widget
                result[f"frame_{index}"] = cls.get_frame(master=result["root"])

                # Configure the "Frame_{index}" frame widget's 1st column to weight 1
                result[f"frame_{index}"].grid_columnconfigure(
                    index=0,
                    weight=1,
                )

                # Create a "Radiobutton_{index}" radiobutton widget
                result[f"radiobutton_{index}"] = cls.get_radiobutton(
                    command=lambda string=f"radiobutton_{index}": on_radiobutton_click(
                        string=string
                    ),
                    master=result[f"frame_{index}"],
                    text=label,
                    variable=result[f"variable_{index}"],
                    **kwargs,
                )

                # Place the "Radiobutton_{index}" radiobutton widget in the "Frame_{index}" frame widget
                result[f"radiobutton_{index}"].grid(
                    column=0,
                    padx=5,
                    pady=5,
                    row=index,
                    sticky=NSEW,
                )

                # Append the "Radiobutton_{index}" radiobutton widget to the "Checkbuttons" dictionary
                result["radiouttons"][f"radiobutton_{index}"] = result[
                    f"radiobutton_{index}"
                ]

            # Add the clearer function to the result dictionary
            result["clearer"] = clear

            # Add the getter function to the result dictionary
            result["getter"] = get

            # Add the setter function to the result dictionary
            result["setter"] = set

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_radiobutton_field' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_scrollbar(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[tkinter.Scrollbar]:
        """
        Creates and returns a new instance of tkinter.Scrollbar.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Scrollbar constructor.

        Returns:
            Optional[tkinter.Scrollbar]: The created tkinter.Scrollbar instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Scrollbar.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Scrollbar
            return tkinter.Scrollbar(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_scrollbar' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_scrolled_frame(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of a scrolled frame.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Frame constructor.

        Returns:
            Optional[Dict[str, Any]]: The created scrolled frame.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of a scrolled frame.
        """
        try:
            # Initialise the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(
                master=master,
            )

            # Configure the "Root" frame widget's 1st column to weight 1
            result["root"].grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the "Root" frame widget's 2nd column to weight 0
            result["root"].grid_columnconfigure(
                index=1,
                weight=0,
            )

            # Configure the "Root" frame widget's 1st row to weight 1
            result["root"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the "Scrollbar" scrollbar widget
            result["scrollbar"] = cls.get_scrollbar(
                master=result["root"],
                orient=VERTICAL,
            )

            # Grid the "Scrollbar" scrollbar widget in the "Root" frame widget
            result["scrollbar"].grid(
                column=1,
                row=0,
                sticky=NS,
            )

            # Create the "Canvas" canvas widget
            result["canvas"] = cls.get_canvas(
                master=result["root"],
            )

            # Create the "Frame" frame widget
            result["frame"] = cls.get_frame(
                master=result["canvas"],
                **kwargs,
            )

            # Configure the "Frame" frame widget's 1st column to weight 1
            result["frame"].grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the "Frame" frame widget's 1st row to weight 1
            result["frame"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Configure the "Scrollbar" scrollbar widget to the canvas
            result["scrollbar"].configure(
                command=result["canvas"].yview,
            )

            # Add the "Frame" frame widget to the "Canvas" canvas widget
            result["window_id"] = result["canvas"].create_window(
                (
                    0,
                    0,
                ),
                anchor=NW,
                window=result["frame"],
            )

            # Configure the "Canvas" canvas widget to use the "Scrollbar" scrollbar widget
            result["canvas"].configure(yscrollcommand=result["scrollbar"].set)

            # Bind the "Frame" frame widget to the "Configure" event
            result["frame"].bind(
                func=lambda event: (
                    result["canvas"].configure(scrollregion=result["canvas"].bbox(ALL)),
                    result["canvas"].itemconfig(
                        result["window_id"], width=result["canvas"].winfo_width()
                    ),
                ),
                sequence="<Configure>",
            )

            # Configure the "Frame" widget in the "Canvas" widget
            result["canvas"].itemconfig(
                result["window_id"], width=result["canvas"].winfo_width()
            )

            # Grid the "Canvas" canvas widget in the "Root" frame widget
            result["canvas"].grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_scrolled_frame' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_scrolled_text(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of a scrolled text widget.

        This function creates a new instance of a scrolled text widget, which
        consists of a text widget and an associated vertical scrollbar. The
        text widget can be used to display or edit multi-line text content.

        The dictionary contains:
            - "root": The "Root" frame widget.
            - "text": The text widget.
            - "scrollbar": The scrollbar widget.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the
                text widget's constructor.

        Returns:
            Optional[Dict[str, Any]]: The created scrolled text widget
            instance.

        Raises:
            Exception: If an exception occurs while attempting to create a
                new instance of the scrolled text widget.
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def clear() -> None:
                """
                Clears the contents of the scrolled text widget.

                This function is called when the "Clear" button is pressed.

                Returns:
                    None
                """

                # Delete the contents of the text widget
                result["text"].delete(
                    "1.0",
                    END,
                )

            def get() -> str:
                """
                Gets the contents of the scrolled text widget.

                Returns:
                    str: The contents of the scrolled text widget.
                """

                # Return the contents of the text widget
                return result["text"].get(
                    "1.0",
                    END,
                )

            def set(value: str) -> None:
                """
                Sets the contents of the scrolled text widget.

                Args:
                    value (str): The new contents for the scrolled text widget.
                """

                # Delete the current content of the text widget
                result["text"].delete(
                    "1.0",
                    END,
                )

                # Insert the new contents into the text widget
                result["text"].insert(
                    "1.0",
                    value,
                )

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(master=master)

            # Configure the "Root" frame widget's 1st column to weight 1 (expandable)
            result["root"].grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the "Root" frame widget's 2nd column to weight 0 (fixed size)
            result["root"].grid_columnconfigure(
                index=1,
                weight=0,
            )

            # Configure the "Root" frame widget's 1st row to weight 1 (expandable)
            result["root"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the "Text" text widget
            result["text"] = cls.get_text(
                master=result["root"],
                **kwargs,
            )

            # Place the "Text" text widget in the "Root" frame widget with sticky positioning
            result["text"].grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the "Scrollbar" scrollbar widget
            result["scrollbar"] = cls.get_scrollbar(
                master=result["root"],
                orient=VERTICAL,
            )

            # Place the "Scrollbar" scrollbar widget in the "Root" frame widget
            result["scrollbar"].grid(
                column=1,
                row=0,
                sticky=NS,
            )

            # Configure the "Text" text widget to use the "Scrollbar" for vertical scrolling
            result["text"].configure(yscrollcommand=result["scrollbar"].set)

            # Configure the "Scrollbar" to control the "Text" text widget's vertical view
            result["scrollbar"].configure(command=result["text"].yview)

            # Add the "clearer" function to the result dictionary
            result["clearer"] = clear

            # Add the "getter" function to the result dictionary
            result["getter"] = get

            # Add the "setter" function to the result dictionary
            result["setter"] = set

            # Return the result dictionary containing the scrolled text widget components
            return result
        except Exception as e:
            # Log an error message indicating an exception occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_scrolled_text' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occurred
            return None

    @classmethod
    def get_scrolled_text_field(
        cls,
        label: str,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of a scrolled text field widget.

        A scrolled text field widget is a frame that contains a label widget,
        a scrolled text widget, and a button widget. The label widget is used
        to label the scrolled text widget. The scrolled text widget is used to
        input a text query and the button widget is used to execute the text
        query.

        The dictionary contains:
            - "root": The root frame widget of the scrolled text field
                widget.
            - "label": The label widget of the scrolled text field
                widget.
            - "scrolled_text_field": The scrolled text widget of the
                scrolled text field widget.
            - "button": The button widget of the scrolled text field
                widget.
            - "clearer": A function to clear the scrolled text widget.
            - "getter": A function to get the value of the scrolled text
                widget.
            - "setter": A function to set the value of the scrolled text
                widget.


        Args:
            label: The label of the scrolled text widget.
            master: The master widget of the scrolled text widget.
            **kwargs: Any additional keyword arguments to be passed to the
                scrolled text widget.

        Returns:
            Optional[Dict[str, Any]]: A dictionary containing the widgets.

        Raises:
            Exception: If an exception occurs while attempting to run the
                method.
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(master=master)

            # Configure the "Root" frame widget's 1st column to weight 0 (fixed size)
            result["root"].grid_columnconfigure(
                index=0,
                weight=0,
            )

            # Configure the "Root" frame widget's 2nd column to weight 1 (flexible size)
            result["root"].grid_columnconfigure(
                index=1,
                weight=1,
            )

            # Configure the "Root" frame widget's 3rd column to weight 0 (fixed size)
            result["root"].grid_columnconfigure(
                index=2,
                weight=0,
            )

            # Configure the "Root" frame widget's 1st row to weight 0 (fixed size)
            result["root"].grid_rowconfigure(
                index=0,
                weight=0,
            )

            # Configure the "Root" frame widget's 2nd row to weight 1 (flexible size)
            result["root"].grid_rowconfigure(
                index=1,
                weight=1,
            )

            # Configure the "Root" frame widget's 3rd row to weight 0 (fixed size)
            result["root"].grid_rowconfigure(
                index=2,
                weight=0,
            )

            # Create the "Label" label widget
            result["label"] = cls.get_label(
                master=result["root"],
                text=label,
            )

            # Place the "Label" label widget in the "Root" frame widget
            result["label"].grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the "ScrolledText" scrolled text widget
            result["scrolled_text_field"] = cls.get_scrolled_text(
                master=result["root"],
                **kwargs,
            )

            # Place the "ScrolledText" scrolled text widget in the "Root" frame widget
            result["scrolled_text_field"]["root"].grid(
                column=1,
                row=1,
                sticky=NSEW,
            )

            # Create the "Button" button widget
            result["button"] = cls.get_button(
                command=result["scrolled_text_field"]["clearer"],
                master=result["root"],
                text="Clear",
            )

            # Place the "Button" button widget in the "Root" frame widget
            result["button"].grid(
                column=2,
                padx=5,
                pady=5,
                row=2,
            )

            # Add the "clearer" function to the result dictionary
            result["clearer"] = result["scrolled_text_field"]["clearer"]

            # Add the "getter" function to the result dictionary
            result["getter"] = result["scrolled_text_field"]["getter"]

            # Add the "setter" function to the result dictionary
            result["setter"] = result["scrolled_text_field"]["setter"]

            # Return the result dictionary containing the scrolled text widget components
            return result
        except Exception as e:
            # Log an error message indicating an exception occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_scrolled_text_field' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occurred
            return None

    @classmethod
    def get_searchbar(
        cls,
        master: tkinter.Misc,
        command: Callable[[str], None],
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of a search bar widget.

        This function creates a new instance of a search bar widget. The
        search bar widget is a frame that contains an entry widget and a
        button widget. The entry widget is used to input a search query and
        the button widget is used to execute the search query. When the
        button widget is clicked, the command function is called with the
        current value of the entry widget as an argument.

        Args:
            master (tkinter.Misc): The master widget.
            command (Callable[[str], None]): The command function to execute
                when the button widget is clicked.
            **kwargs: Any additional keyword arguments to be passed to the
                frame widget's constructor.

        Returns:
            Optional[Dict[str, Any]]: The created search bar widget instance.

        Raises:
            Exception: If an exception occurs while attempting to create a
                new instance of the search bar widget.
        """
        try:

            def clear() -> None:
                """
                Clears the current value of the entry widget.

                This function clears the current content of the entry widget.

                Returns:
                    None
                """
                result["entry"].delete(
                    0,
                    END,
                )

            def get() -> Optional[str]:
                """
                Retrieves the content of the entry widget.

                Returns:
                    Optional[str]: The content of the entry widget.
                """

                # Attempt to obtain the current value of the entry widget
                string: Optional[str] = result["entry"].get()

                # Check, if the content of the entry widget is an empty string
                if string == "":
                    # Return early
                    return None

                # Return the content of the entry widget
                return string

            def set(value: str) -> None:
                """
                Sets the value of the entry widget.

                This function clears the current content of the entry widget
                and inserts the provided value.

                Args:
                    value (str): The string value to set in the entry widget.

                Returns:
                    None
                """
                clear()
                result["entry"].insert(
                    0,
                    value,
                )

            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(master=master)

            # Configure the "Root" frame widget's 1st column to weight 1
            result["root"].grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the "Root" frame widget's 2nd column to weight 0
            result["root"].grid_columnconfigure(
                index=1,
                weight=0,
            )

            # Configure the "Root" frame widget's 1st row to weight 1
            result["root"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the "Entry" entry widget
            result["entry"] = cls.get_entry(master=result["root"])

            # Grid the "Entry" entry widget in the "Root" frame widget
            result["entry"].grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the "Clear" button widget
            result["button"] = cls.get_button(
                command=lambda: command(get()),
                master=result["root"],
                text="Search",
            )

            # Grid the "Button" button widget in the "Root" frame widget
            result["button"].grid(
                column=1,
                padx=5,
                pady=5,
                row=0,
            )

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_searchbar' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_separator(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[ttk.Separator]:
        """
        Creates and returns a new instance of ttk.Separator.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the ttk.Separator constructor.

        Returns:
            Optional[ttk.Separator]: The created ttk.Separator instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of ttk.Separator.
        """
        try:
            # Attempt to create and return a new instance of ttk.Separator
            return ttk.Separator(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_separator' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_single_line_text_field(
        cls,
        label: str,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of a single-line text field widget.

        The returned dictionary contains the following keys:
            - "root": The master widget (Call your geometry manager (.place, .grid, .pack, etc.) on this widget)
            - "label": The label widget
            - "entry": The entry widget
            - "button": The button widget
            - "clear": A function to clear all content from the entry widget
            - "get": A function to get the content of the entry widget
            - "set": A function to set the content of the entry widget

        Returns:
            Optional[Dict[str, Any]]: The created widgets dictionary or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create the widgets
        """
        try:
            # Initialize the result dictionary as an empty
            result: Dict[str, Any] = {}

            # Create a method to clear the content of the entry widget
            def clear() -> None:
                """
                Clears the content of the entry widget.

                Returns:
                    None
                """

                # Delete all content from the entry widget
                result["entry"].delete(
                    0,
                    END,
                )

            # Create a method to get the content of the entry widget
            def get() -> Optional[str]:
                """
                Retrieves the content of the entry widget.

                Returns:
                    Optional[str]: The content of the entry widget.
                """

                # Attempt to obtain the current value of the entry widget
                string: Optional[str] = result["entry"].get()

                # Check, if the content of the entry widget is an empty string
                if string == "" or string is None:
                    # Return early
                    return None

                # Return the content of the entry widget
                return string

            # Create a method to set the content of the entry widget
            def set(value: str) -> None:
                """
                Sets the content of the entry widget to the given value.

                Args:
                    value (str): The value to set in the entry widget.

                Returns:
                    None
                """

                # Clear the content of the entry widget
                result["entry"].delete(
                    0,
                    END,
                )

                # Insert the given value into the entry widget
                result["entry"].insert(
                    0,
                    value,
                )

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(master=master)

            # Configure the "Root" frame widget's 1st column to weight 0
            result["root"].grid_columnconfigure(
                index=(
                    0,
                    2,
                ),
                weight=0,
            )

            # Configure the "Root" frame widget's 2nd column to weight 1
            result["root"].grid_columnconfigure(
                index=1,
                weight=1,
            )

            # Configure the "Root" frame widget's 1st row to weight 1
            result["root"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the label widget
            result["label"] = cls.get_label(
                master=result["root"],
                text=label,
            )

            # Grid the label widget
            result["label"].grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the entry widget
            result["entry"] = cls.get_entry(
                master=result["root"],
                **kwargs,
            )

            # Grid the entry widget
            result["entry"].grid(
                column=1,
                row=0,
                sticky=NSEW,
            )

            # Create the button widget
            result["button"] = cls.get_button(
                command=clear,
                master=result["root"],
                text="Clear",
            )

            # Grid the button widget
            result["button"].grid(
                column=2,
                padx=5,
                pady=5,
                row=0,
            )

            # Add the "clearer" function to the result dictionary
            result["clearer"] = clear

            # Add the "getter" function to the result dictionary
            result["getter"] = get

            # Add the "setter" function to the result dictionary
            result["setter"] = set

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_single_line_text_field' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_single_select_field(
        cls,
        label: str,
        master: tkinter.Misc,
        values: List[str],
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a single select field widget with associated label and button.

        The returned dictionary contains the following keys:
            - "root": The container frame for the widgets
            - "label": The label widget
            - "container": The container for the selected value
            - "button": The button widget to open the selection
            - "listbox": The listbox widget for selection (created on demand)
            - "selection": The currently selected value
            - "toplevel": The toplevel widget for listbox (created on demand)
            - "values": The list of values to select from
            - "getter": A function to retrieve the selected value

        Args:
            label (str): The text for the label widget.
            master (tkinter.Misc): The master widget for placing the container frame.
            values (List[str]): The list of values to select from.
            **kwargs: Additional keyword arguments for the widgets.

        Returns:
            Optional[Dict[str, Any]]: The created widgets dictionary or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create the widgets.
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            # Initialize the listbox widget as None
            result["listbox"] = None

            # Initialize the selection key as None
            result["selection"] = None

            # Initialize the toplevel widget as None
            result["toplevel"] = None

            # Add the values to the result dictionary
            result["values"] = values

            def get() -> Optional[str]:
                """
                Gets the selected value from the single select field.

                Returns:
                    Optional[str]: The selected value or None if no value is selected.
                """

                # Check, if a value is associated with the "selection" key
                if not result.get(
                    "selection",
                    None,
                ):
                    # Return early
                    return None

                # Return the value associated with the "selection" key
                return result["selection"]

            def on_listbox_select(event: Optional[tkinter.Event] = None) -> None:
                """
                Called when an item is selected from the listbox widget.

                Gets the selected value from the listbox widget and sets it to the "selection" key of the result dictionary.

                If no selection is made, sets the value associated with the "selection" key to None.

                Args:
                    event (Optional[tkinter.Event]): The event object.

                Returns:
                    None
                """

                # Get the selection indices of the listbox widget
                selection_indices: Optional[Tuple[int]] = result[
                    "listbox"
                ].curselection()

                # Check, if selection indices are available
                if not selection_indices:
                    # Set the value associated with the "selection" key to None
                    result["selection"] = None
                else:
                    # Set the value associated with the "selection" key to the value at the 0th index of the selection indices tuple
                    result["selection"] = result["listbox"].get(selection_indices[0])

                    # Iterate over the children of the "Container" frame widget
                    for child in result["container"].winfo_children():
                        # Destroy each child widget
                        child.destroy()

                    # Create the "Value frame" frame widget
                    result["value_frame"] = cls.get_frame(master=result["container"])

                    # Configure the "Value frame" frame widget's 1st column to weight 1
                    result["value_frame"].grid_columnconfigure(
                        index=0,
                        weight=1,
                    )

                    # Configure the "Value frame" frame widget's 2nd column to weight 0
                    result["value_frame"].grid_columnconfigure(
                        index=1,
                        weight=0,
                    )

                    # Place the "Value frame" frame widget within the "Container" frame widget
                    result["value_frame"].grid(
                        column=0,
                        padx=5,
                        pady=5,
                        row=0,
                        sticky=NSEW,
                    )

                    # Create the "Value label" label widget
                    result["value_label"] = cls.get_label(
                        master=result["value_frame"],
                        text=result["selection"],
                        **kwargs,
                    )

                    # Place the "Value label" label widget within the "Value frame" frame widget
                    result["value_label"].grid(
                        column=0,
                        padx=5,
                        pady=5,
                        row=0,
                        sticky=NSEW,
                    )

                    # Create the "Value remove button" button widget
                    result["value_remove_button"] = cls.get_button(
                        command=on_value_remove_button_click,
                        master=result["value_frame"],
                        **kwargs,
                    )

                    # Place the "Value remove button" button widget within the "Value frame" frame widget
                    result["value_remove_button"].grid(
                        column=1,
                        padx=5,
                        pady=5,
                        row=0,
                    )

                    # Check, if a value is associated with the "toplevel" key
                    if result.get(
                        "toplevel",
                        None,
                    ):
                        # Destroy the toplevel widget
                        result["toplevel"].destroy()

                        # Set the value associated with the "toplevel" key to None
                        result["toplevel"] = None

                        # Set the value associated with the "listbox" key to None
                        result["listbox"] = None

            def on_value_remove_button_click() -> None:
                """
                Called when the "Value remove button" button widget is clicked.

                Clears the content of the "Container" frame widget and sets the value associated with the "selection" key to None.

                Returns:
                    None
                """

                # Iterate over the children of the "Container" frame widget
                for child in result["container"].winfo_children():
                    # Destroy each child widget
                    child.destroy()

                # Set the value associated with the "selection" key to None
                result["selection"] = None

            def on_select_button_click() -> None:
                """
                Called when the "Select" button is clicked.

                Creates and displays a toplevel widget with a listbox widget containing the values to be selected from.

                Returns:
                    None
                """

                # Check, if a value is associated with the "toplevel" key
                if not result.get(
                    "toplevel",
                    None,
                ):
                    # Create the "Toplevel" toplevel widget
                    result["toplevel"] = cls.get_toplevel()

                # Configure the "Toplevel" toplevel widget's 1st column to weight 1
                result["toplevel"].grid_columnconfigure(
                    index=0,
                    weight=1,
                )

                # Configure the "Toplevel" toplevel widget's 2nd column to weight 0
                result["toplevel"].grid_columnconfigure(
                    index=1,
                    weight=0,
                )

                # Create the "Listbox" listbox widget
                result["listbox"] = cls.get_listbox(
                    activestyle="underline",
                    master=result["toplevel"],
                    selectmode="single",
                    **kwargs,
                )

                # Place the "listbox" listbox widget in the "Toplevel" toplevel widget
                result["listbox"].grid(
                    column=0,
                    row=0,
                    sticky=NSEW,
                )

                # Add the values to the "Listbox" listbox widget
                [
                    result["listbox"].insert(
                        index=index,
                        value=value,
                    )
                    for (
                        index,
                        value,
                    ) in enumerate(iterable=result["values"])
                ]

                # Bind the "<<ListboxSelect>>" event to the "on_listbox_select" function
                result["listbox"].bind(
                    func=on_listbox_select,
                    sequence="<<ListboxSelect>>",
                )

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(master=master)

            # Configure the "Root" frame widget's 1st column to weight 0
            result["root"].grid_columnconfigure(
                index=0,
                weight=0,
            )

            # Configure the "Root" frame widget's 2nd column to weight 1
            result["root"].grid_columnconfigure(
                index=1,
                weight=1,
            )

            # Configure the "Root" frame widget's 3rd column to weight 0
            result["root"].grid_columnconfigure(
                index=2,
                weight=0,
            )

            # Configure the "Root" frame widget's 1st row to weight 0
            result["root"].grid_rowconfigure(
                index=0,
                weight=0,
            )

            # Create the "Label" label widget
            result["label"] = cls.get_label(
                master=result["root"],
                text=label,
                **kwargs,
            )

            # Place the "Label" widget within the "Root" frame widget
            result["label"].grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the "Container" frame widget
            result["container"] = cls.get_frame(master=result["root"])

            # Configure the "Container" frame widget's 1st column to weight 1
            result["container"].grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the "Container" frame widget's 1st row to weight 1
            result["container"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Place the "Container" frame widget within the "Root" frame widget
            result["container"].grid(
                column=1,
                row=0,
                sticky=NSEW,
            )

            # Create the "Button" button widget
            result["button"] = cls.get_button(
                command=on_select_button_click,
                master=result["root"],
                text="Select",
            )

            # Place the "Button" button widget within the "Root" frame widget
            result["button"].grid(
                column=0,
                row=1,
                sticky=NSEW,
            )

            # Add the getter function to the result dictionary
            result["getter"] = get

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_single_select_field' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_spinbox(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[ttk.Spinbox]:
        """
        Creates and returns a new instance of ttk.Spinbox.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the ttk.Spinbox constructor.

        Returns:
            Optional[ttk.Spinbox]: The created ttk.Spinbox instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of ttk.Spinbox.
        """
        try:
            # Attempt to create and return a new instance of ttk.Spinbox
            return ttk.Spinbox(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_spinbox' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_str_variable(
        cls,
        master: Optional[tkinter.Misc] = None,
        name: Optional[str] = None,
        value: Optional[str] = "",
    ) -> Optional[tkinter.StringVar]:
        """
        Creates and returns a new instance of tkinter.StringVar.

        Args:
            master (Optional[Any]): The master widget.
            name (Optional[str]): The name of the variable.
            value (Optional[str]): The initial value of the variable.

        Returns:
            Optional[tkinter.StringVar]: The created tkinter.StringVar instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.StringVar.
        """
        try:
            # Attempt to create and return a new instance of tkinter.StringVar
            return tkinter.StringVar(
                master=master,
                name=name,
                value=value,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_str_variable' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_style(
        cls,
        master: Optional[tkinter.Misc] = None,
    ) -> Optional[ttk.Style]:
        """
        Creates and returns a new instance of ttk.Style.

        Args:
            master (Optional[tkinter.Misc]): The master widget.

        Returns:
            Optional[ttk.Style]: The created ttk.Style instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of ttk.Style.
        """
        try:
            # Attempt to create and return a new instance of ttk.Style
            return ttk.Style(master=master)
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_style' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_tabbed_view(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of a tabbed view widget.

        A tabbed view widget is a frame that contains a top frame widget and a center frame widget.
        The top frame widget contains a series of buttons and the center frame widget contains a series
        of widgets. Each button in the top frame widget is associated with a widget in the center frame
        widget. When a button is clicked, all widgets in the center frame widget are hidden and the
        associated widget is shown.

        The dictionary contains:
            - "root": The root frame widget of the tabbed view widget.
            - "children": A dictionary of the widgets in the center frame widget.
            - "top_frame": The top frame widget of the tabbed view widget.
            - "{label.lower()}_button": A button widget in the top frame widget.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Frame constructor.

        Returns:
            Optional[Dict[str, Any]]: The created tabbed view widget.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of a tabbed view
                widget.
        """

        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            # Initialize the children dictionary as an empty dictionary
            result["children"] = {}

            def add(
                label: str,
                widget: Type[tkinter.Misc],
                state: Literal[NORMAL, DISABLED, HIDDEN] = NORMAL,
                sticky: str = NSEW,
            ) -> None:
                """
                Adds a widget to the 'children' dictionary and configures its placement.

                Args:
                    label (str): The label for the widget.
                    widget (Type[tkinter.Misc]): The widget instance to be added.
                    state (Literal[NORMAL, DISABLED, HIDDEN], optional): The state of the widget. Defaults to NORMAL.
                    sticky (str, optional): The sticky configuration for the widget. Defaults to NSEW.

                Returns:
                    None
                """

                # Add the widget to the "children" dictionary under the key "label"
                result["children"][label] = {
                    "state": state,
                    "sticky": sticky,
                    "widget": widget,
                }

                # Get the number of children in the "children" dictionary
                num_children: int = len(result["children"])

                # Create the "{label.lower()}_button" button widget
                result[f"{label.lower()}_button"] = cls.get_button(
                    command=lambda string=label: on_button_click(string=string),
                    master=result["top_frame"],
                    text=label,
                )

                # Place the button widget within the "Top frame" frame widget
                result[f"{label.lower()}_button"].grid(
                    column=num_children - 1,
                    row=0,
                    sticky=sticky,
                )

                # Check if the widget is the only one added to the "children" dictionary
                if num_children == 1:
                    # Place the widget within the "Center frame" frame widget
                    widget.grid(
                        column=0,
                        row=0,
                        sticky=sticky,
                    )

                    # Disable the button
                    result[f"{label.lower()}_button"].configure(state=DISABLED)
                else:
                    # Hide the widget
                    widget.grid_forget()

            def on_button_click(string: str) -> None:
                """
                Called when any of the buttons in the "children" dictionary is clicked.

                Hides all widgets in the "children" dictionary and shows the widget with the key
                "string".

                Args:
                    string (str): The key of the widget to be shown.

                Returns:
                    None
                """

                # Check if the string could be found in the "children" dictionary
                if string not in set([label for label in result["children"].keys()]):
                    # Log a warning message, that the string could not be found
                    cls.logger.warning(
                        message=f"'{string}' could not be found in the 'children' dictionary. This is likely a bug.",
                    )

                    # Return early
                    return

                # Hide all widgets in the "children" dictionary
                for child in set(
                    [value["widget"] for value in result["children"].values()]
                ):
                    child.grid_forget()

                # Iterate over the items in the result dictionary
                for (
                    key,
                    value,
                ) in [
                    (
                        key,
                        value,
                    )
                    for (
                        key,
                        value,
                    ) in result.items()
                    if "_button" in key
                ]:
                    # Check, if the key and the string are identical
                    if string.lower() not in key:
                        # Enable the widget if it is not the one that was clicked
                        value.configure(state=NORMAL)
                    else:
                        # Disable the widget if it is the one that was clicked
                        value.configure(state=DISABLED)

                # Show the widget in the "children" dictionary with the key "string"
                result["children"][string]["widget"].grid(
                    column=0,
                    row=0,
                    sticky=result["children"][string]["sticky"],
                )

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(master=master)

            # Configure the "Root" frame widget's 1st column to weight 1
            result["root"].grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the "Root" frame widget's 1st row to weight 0
            result["root"].grid_rowconfigure(
                index=0,
                weight=0,
            )

            # Configure the "Root" frame widget's 2nd row to weight 1
            result["root"].grid_rowconfigure(
                index=1,
                weight=1,
            )

            # Create the "Top frame" frame widget
            result["top_frame"] = cls.get_frame(master=result["root"])

            # Place the "Top frame" widget within the "Root" frame widget
            result["top_frame"].grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the "Center frame" frame widget
            result["center_frame"] = cls.get_frame(master=result["root"])

            # Configure the "Center frame" frame widget's 1st column to weight 1
            result["center_frame"].grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the "Center frame" frame widget's 1st row to weight 1
            result["center_frame"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Place the "Center frame" widget within the "Root" frame widget
            result["center_frame"].grid(
                column=0,
                row=1,
                sticky=NSEW,
            )

            # Add the adder function to the result dictionary
            result["adder"] = add

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_tabbed_view' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_text(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[tkinter.Text]:
        """
        Creates and returns a new instance of tkinter.Text.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Text constructor.

        Returns:
            Optional[tkinter.Text]: The created tkinter.Text instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Text.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Text
            return tkinter.Text(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_text' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_tk(
        cls,
        base_name: Optional[str] = None,
        class_name: Optional[str] = "Tk",
        screen_name: Optional[str] = None,
        sync: Optional[bool] = False,
        use: Optional[str] = None,
        use_tk: Optional[bool] = True,
    ) -> Optional[tkinter.Tk]:
        """
        Creates and returns a new instance of tkinter.Tk.

        Args:
            base_name (Optional[str]): The base name of the root window.
            class_name (Optional[str]): The class name of the root window. Defaults to "Tk".
            screen_name (Optional[str]): The name of the screen where the root window should appear.
            sync (Optional[bool]): Whether to use synchronous mode or not. Defaults to False.
            use (Optional[str]): The use argument to be passed to the tkinter.Tk constructor.
            use_tk (Optional[bool]): Whether to use Tk or not. Defaults to True.

        Returns:
            Optional[tkinter.Tk]: The created tkinter.Tk instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Tk.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Tk
            return tkinter.Tk(
                baseName=base_name,
                className=class_name,
                screenName=screen_name,
                sync=sync,
                use=use,
                useTk=use_tk,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_tk' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_toplevel(
        cls,
        master: Optional[tkinter.Misc] = None,
        **kwargs,
    ) -> Optional[tkinter.Toplevel]:
        """
        Creates and returns a new instance of tkinter.Toplevel.

        Args:
            master (Optional[Any]): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Toplevel constructor.

        Returns:
            Optional[tkinter.Toplevel]: The created tkinter.Toplevel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Toplevel.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Toplevel
            return tkinter.Toplevel(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_toplevel' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_treeview(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[ttk.Treeview]:
        """
        Creates and returns a new instance of ttk.Treeview.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the ttk.Treeview constructor.

        Returns:
            Optional[ttk.Treeview]: The created ttk.Treeview instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of ttk.Treeview.
        """
        try:
            # Attempt to create and return a new instance of ttk.Treeview
            return ttk.Treeview(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_treeview' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_true_false_answer_field(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a dictionary containing widgets to facilitate a true false answer field.

        The widgets contained in the dictionary are:
            - "root" (tkinter.Frame): The root widget of the true false answer field.
            - "label" (tkinter.Label): The label widget of the true false answer field.
            - "container" (tkinter.Frame): The container widget of the true false answer field.
            - "true_var" (tkinter.IntVar): The variable for the true radio button.
            - "false_var" (tkinter.IntVar): The variable for the false radio button.
            - "true_radiobutton" (tkinter.Radiobutton): The true radio button.
            - "false_radiobutton" (tkinter.Radiobutton): The false radio button.

        Returns:
            Optional[Dict[str, Any]]: The created widgets dictionary or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create the widgets.
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            # Initialize the "value" key to False
            result["value"] = False

            def clear() -> None:
                """
                Clears the result dictionary by setting the "value" key to False and the "true_var" and "false_var" keys to their default values.

                Returns:
                    None
                """
                # Set the "value" key to False
                result["value"] = False

                # Set the "true_var" key to False
                result["true_var"].set(value=False)

                # Set the "false_var" key to True
                result["false_var"].set(value=True)

            def get() -> bool:
                """
                Retrieves the value of the result dictionary.

                Returns:
                    bool: The value of the result dictionary.
                """
                # Return the value of the "value" key
                return result["value"]

            def set(value: Union[bool, int]) -> None:
                """
                Sets the value of the result dictionary to the value of the "value" argument.

                Args:
                    value (Union[bool,int]): The value to set the result dictionary to.

                Returns:
                    None
                """
                # Set the "value" key to the value of the "value" argument
                result["value"] = bool(value)

                # Set the "true_var" key to the value of the "value" argument
                result["true_var"].set(value=value)

                # Set the "false_var" key to the inverse of the value of the "value" argument
                result["false_var"].set(value=not value)

            def on_true_radiobutton_click() -> None:
                """
                Called when the true radio button is clicked.

                Sets the "value" key to True and the "true_var" key to True.
                Sets the "false_var" key to False.

                Returns:
                    None
                """
                # Set the "value" key to True
                result["value"] = True

                # Set the "true_var" key to True
                result["true_var"].set(value=True)

                # Set the "false_var" key to False
                result["false_var"].set(value=False)

            def on_false_radiobutton_click() -> None:
                """
                Called when the false radio button is clicked.

                Sets the "value" key to False and the "true_var" key to False.
                Sets the "false_var" key to True.

                Returns:
                    None
                """
                # Set the "value" key to False
                result["value"] = False

                # Set the "true_var" key to False
                result["true_var"].set(value=False)

                # Set the "false_var" key to True
                result["false_var"].set(value=True)

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(master=master)

            # Configure the "Root" frame widget's 1st column to weight 0
            result["root"].grid_columnconfigure(
                index=0,
                weight=0,
            )

            # Configure the "Root" frame widget's 2nd column to weight 1
            result["root"].grid_columnconfigure(
                index=1,
                weight=1,
            )

            # Configure the "Root" frame widget's 3rd column to weight 0
            result["root"].grid_columnconfigure(
                index=2,
                weight=0,
            )

            # Configure the "Root" frame widget's 1st row to weight 0
            result["root"].grid_rowconfigure(
                index=0,
                weight=0,
            )

            # Configure the "Root" frame widget's 2nd row to weight 0
            result["root"].grid_rowconfigure(
                index=1,
                weight=0,
            )

            # Create the "Label" label widget
            result["label"] = cls.get_label(
                master=result["root"],
                text="Select one of: ",
                **kwargs,
            )

            # Place the "Label" label widget within the "Root" frame widget
            result["label"].grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Create the "Container" frame widget
            result["container"] = cls.get_frame(master=result["root"])

            # Configure the "Container" frame widget's 0th and 1st column to weight 0
            result["container"].grid_columnconfigure(
                index=(
                    0,
                    1,
                ),
                weight=0,
            )

            # Configure the "Container" frame widget's 0th row to weight 0
            result["container"].grid_rowconfigure(
                index=0,
                weight=0,
            )

            # Place the "Container" frame widget within the "Root" frame widget
            result["container"].grid(
                column=1,
                row=1,
                sticky=NSEW,
            )

            # Create the "True" boolean variable
            result["true_var"] = cls.get_bool_variable(
                master=result["root"],
                value=True,
            )

            # Create the "False" boolean variable
            result["false_var"] = cls.get_bool_variable(
                master=result["root"],
                value=False,
            )

            # Create the "true_radiobutton" radiobutton widget
            result["true_radiobutton"] = cls.get_radiobutton(
                command=on_true_radiobutton_click,
                master=result["container"],
                text="True",
                variable=result["true_var"],
            )

            # Place the "True" radiobutton widget within the "Container" frame widget
            result["true_radiobutton"].grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Create the "false_radiobutton" radiobutton widget
            result["false_radiobutton"] = cls.get_radiobutton(
                command=on_false_radiobutton_click,
                master=result["container"],
                text="False",
                variable=result["false_var"],
            )

            # Place the "False" radiobutton widget within the "Container" frame widget
            result["false_radiobutton"].grid(
                column=1,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Add the clearer function to the result dictionary
            result["clearer"] = clear

            # Add the getter function to the result dictionary
            result["getter"] = get

            # Add the setter function to the result dictionary
            result["setter"] = set

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_true_false_answer_field' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None
