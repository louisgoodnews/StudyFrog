"""
Author: lodego
Date: 2025-02-08
"""

import re
import tkinter

from datetime import timedelta
from typing import *
from tkinter import ttk
from tkinter.constants import *

from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherEvent
from utils.events import Events
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous


__all__: Final[List[str]] = ["UIBuilder"]


class UIBuilder:
    """
    A utility class for building (tkinter, ttk) user interface components.

    Attributes:
        logger (Logger): The logger instance used by the class.
        dispatcher (Dispatcher): The dispatcher instance used by the class.
    """

    # The logger instance used by the class
    logger: Final[Logger] = Logger.get_logger(name="UIBuilder")

    # The dispatcher instance used by the class
    dispatcher: Final[Dispatcher] = Dispatcher()

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
    def get_checkbutton_field(
        cls,
        label: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[bool], None]] = None,
        value: bool = False,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of tkinter.Checkbutton that is used as a field.

        This method creates a dictionary that holds all functions and widgets that facilitate the checkbox field.
        Contained keys are:
            - "clearer": A function that clears the checkbox field.
            - "getter": A function that retrieves the value of the checkbox field.
            - "setter": A function that sets the value of the checkbox field.
            - "variable": A tkinter.BooleanVar instance that holds the value of the checkbox field.
            - "root": A tkinter.Frame instance that holds the checkbox field.
            - "label": A tkinter.Label instance that holds the label for the checkbox field.
            - "checkbutton": A tkinter.Checkbutton instance that is used as a field.

        Args:
            label (str): The label for the checkbutton.
            master (tkinter.Misc): The master widget.
            namespace (str): The namespace for the checkbutton. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[bool], None]]): A callback function that is called when the value of the checkbox field changes. Defaults to None.
            value (bool): The initial value of the checkbox field. Defaults to False.
            **kwargs: Any additional keyword arguments to be passed to the various tkinter widgets.

        Returns:
            Optional[Dict[str, Any]]: The created tkinter.Checkbutton instance or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Checkbutton.
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def clear(dispatch: bool = True) -> None:
                """
                Clears the checkbutton field by setting its value to False.

                Args:
                    None

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to clear the checkbutton field.
                """
                try:
                    if dispatch:
                        # Dispatch the CHECKBUTTON_FIELD_CLEARED event
                        cls.dispatcher.dispatch(
                            event=Events.CHECKBUTTON_FIELD_CLEARED,
                            label=label,
                            namespace=namespace,
                            value=False,
                        )

                    # Set the value of the checkbutton field to False
                    result["variable"].set(value=False)

                    # Update the text of the checkbutton
                    result["checkbutton"].configure(text=str(result["variable"].get()))
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'clear' method from '{cls.__name__}': {e}"
                    )

            def get(dispatch: bool = True) -> bool:
                """
                Retrieves the value of the checkbutton field as a boolean.

                Args:
                    None

                Returns:
                    bool: The value of the checkbutton field as a boolean.

                Raises:
                    Exception: If an exception occurs while attempting to retrieve the value of the checkbutton field.
                """
                try:
                    if dispatch:
                        # Dispatch the CHECKBUTTON_FIELD_GET event
                        cls.dispatcher.dispatch(
                            event=Events.CHECKBUTTON_FIELD_GET,
                            label=label,
                            namespace=namespace,
                            value=result["variable"].get(),
                        )

                    # Return the value of the checkbutton field as a boolean
                    return result["variable"].get()
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'get' method from '{cls.__name__}': {e}"
                    )

                    # Return False
                    return False

            def on_check_box_changed(dispatch: bool = True) -> None:
                """
                Handles the CHECKBUTTON_FIELD_CHANGED event.

                This function is called when the value of the checkbutton field changes.

                Args:
                    None

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to dispatch the CHECKBUTTON_FIELD_CHANGED event.
                """
                try:
                    if dispatch:
                        # Dispatch the CHECKBUTTON_FIELD_CHANGED event
                        cls.dispatcher.dispatch(
                            event=Events.CHECKBUTTON_FIELD_CHANGED,
                            label=label,
                            namespace=namespace,
                            value=result["variable"].get(),
                        )

                    # Update the text of the checkbutton
                    result["checkbutton"].configure(text=str(result["variable"].get()))

                    # Check, if the on_change_callback is present
                    if on_change_callback:
                        # Call the on_change_callback function with the new value
                        on_change_callback(result["variable"].get())
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'on_check_box_changed' method from '{cls.__name__}': {e}"
                    )

            def set(
                dispatch: bool = True,
                value: bool = False,
            ) -> None:
                """
                Sets the value of the checkbutton field.

                Args:
                    dispatch (bool, optional): Whether to dispatch the CHECKBUTTON_FIELD_SET event. Defaults to True.
                    value (bool, optional): The value to set for the checkbutton field. Defaults to False.

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to set the value of the checkbutton field.
                """
                try:
                    if dispatch:
                        # Dispatch the CHECKBUTTON_FIELD_SET event
                        cls.dispatcher.dispatch(
                            event=Events.CHECKBUTTON_FIELD_SET,
                            label=label,
                            namespace=namespace,
                            value=value,
                        )

                    # Set the value of the checkbutton field
                    result["variable"].set(value=value)

                    # Update the text of the checkbutton
                    result["checkbutton"].configure(text=str(result["variable"].get()))
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'set' method from '{cls.__name__}': {e}"
                    )

            # Create the "Variable" boolean variable
            result["variable"] = cls.get_bool_variable(value=value)

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(
                master=master,
                **kwargs.get("frame", {}),
            )

            # Configure the "Root" frame widget's 0th column to weight 0
            result["root"].grid_columnconfigure(
                index=0,
                weight=0,
            )

            # Configure the "Root" frame widget's 1st column to weight 0
            result["root"].grid_columnconfigure(
                index=1,
                weight=0,
            )

            # Configure the "Root" frame widget's 0th row to weight 1
            result["root"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the "Label" label widget
            result["label"] = cls.get_label(
                master=result["root"],
                text=label,
                **kwargs.get("label", {}),
            )

            # Add the "Label" label widget to the "Root" frame widget
            result["label"].grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Create the "Checkbutton" checkbutton widget
            result["checkbutton"] = cls.get_checkbutton(
                command=on_check_box_changed,
                master=result["root"],
                text="False",
                variable=result["variable"],
                **kwargs.get("checkbutton", {}),
            )

            # Add the "Checkbutton" checkbutton widget to the "Root" frame widget
            result["checkbutton"].grid(
                column=1,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
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
                message=f"Caught an exception while attempting to run 'get_checkbutton_field' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_checkbutton_field_group(
        cls,
        labels: List[str],
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[bool], None]] = None,
        selection_mode: Literal["multiple", "single"] = "single",
        value: bool = False,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of a group of checkbutton fields.

        This method creates a frame widget and adds a checkbutton field to it for each label in the given list of labels.
        The checkbutton fields are configured to call the given on_change_callback when their value is changed.
        The method also adds a getter and setter function to the result dictionary, which can be used to get and set the value of the checkbutton fields.

        Args:
            labels (List[str]): A list of labels for the checkbutton fields.
            master (tkinter.Misc): The master widget.
            namespace (str, optional): The namespace to use for the checkbutton fields. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[bool], None]], optional): A callback function to call when the value of a checkbutton field is changed. Defaults to None.
            selection_mode (Literal["multiple", "single"], optional): The selection mode for the checkbutton fields. Defaults to "single".
            value (bool, optional): The initial value of the checkbutton fields. Defaults to False.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Checkbutton constructor.

        Returns:
            Optional[Dict[str, Any]]: A dictionary containing the created checkbutton fields, the getter and setter functions, and the clearer function.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Checkbutton.
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def clear() -> None:
                """
                Clears all the checkbutton fields.

                This method calls the "clearer" function on each checkbutton field in the "fields" dictionary.

                Returns:
                    None
                """

                # Iterate over the values in the "fields" dictionary
                for field in result["fields"].values():
                    # Call the "clearer" function on the current field
                    field["clearer"]()

            def enforce_selection_mode(
                label: str,
                value: bool,
            ) -> None:
                """
                Enforces the selection mode on the checkbutton fields.

                This method is called when the value of a checkbutton field is changed.
                It enforces the selection mode by calling the setter function on all
                other checkbutton fields with the opposite value of the one given.

                Args:
                    label (str): The label of the checkbutton field that was changed.
                    value (bool): The new value of the checkbutton field.
                """

                # Check, if the selection mode is "multiple"
                if selection_mode == "multiple":
                    # If the selection mode is "multiple", there is nothing to do
                    return

                # Iterate over the values in the "fields" dictionary
                for (
                    key,
                    field,
                ) in result["fields"].items():
                    # Check, if the current field is the one that was changed
                    if key == label:
                        # Skip the current field
                        continue

                    # Call the "setter" function on the current field
                    field["setter"](
                        dispatch=False,
                        value=not value,
                    )

                if on_change_callback:
                    # Call the on_change_callback
                    on_change_callback(value)

            def get(label: str) -> bool:
                """
                Gets the value of the checkbutton field with the given label.

                This method calls the "getter" function on the checkbutton field in the "fields" dictionary with the given label
                and returns its value.

                Args:
                    label (str): The label of the checkbutton field to get.

                Returns:
                    bool: The value of the checkbutton field with the given label.
                """

                # Check if the label is present in the "fields" dictionary
                if label not in result["fields"].keys():
                    # Return early
                    return False

                # Call the "getter" function on the current field
                return result["fields"][label]["getter"]()

            def set(
                label: str,
                value: bool = False,
            ) -> None:
                """
                Sets the value of the checkbutton field with the given label.

                This method calls the "setter" function on the checkbutton field in the "fields" dictionary with the given label
                and sets it to the given value.

                Args:
                    label (str): The label of the checkbutton field to set.
                    value (bool, optional): The value to set the checkbutton field to. Defaults to False.

                Returns:
                    None
                """

                # Check if the label is present in the "fields" dictionary
                if label not in result["fields"].keys():
                    # Return early
                    return

                # Call the "setter" function on the current field
                result["fields"][label]["setter"](value=value)

            # Initialize the "fields" dictionary as an empty dictionary
            result["fields"] = {}

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(master=master)

            # Configure the "Root" frame widget's 0th column to weight 1
            result["root"].grid_columnconfigure(
                index=0,
                weight=1,
            )

            for (
                index,
                label,
            ) in enumerate(iterable=labels):
                # Configure the "Root" frame widget's row at the current index to weight 0
                result["root"].grid_rowconfigure(
                    index=index,
                    weight=0,
                )

                # Create the check widget
                checkbutton_field: Optional[Dict[str, Any]] = cls.get_checkbutton_field(
                    label=label,
                    master=result["root"],
                    namespace=namespace,
                    on_change_callback=enforce_selection_mode,
                    value=value,
                    **kwargs.get(f"{label}_field", {}),
                )

                if not checkbutton_field:
                    # Log a warning message
                    cls.logger.warning(
                        message=f"Failed to create check widget in '{cls.__name__}'. This is likely a bug."
                    )

                    # Return early
                    return None

                # Add the check widget to the result dictionary
                result["fields"][label] = checkbutton_field

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
                message=f"Caught an exception while attempting to run 'get_checkbutton_field_group' method from '{cls.__name__}': {e}"
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
    def get_combobox_field(
        cls,
        label: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, str], None]] = None,
        values: List[str] = [],
        value: str = "",
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of tkinter.Combobox that is used as a field.

        This method creates a dictionary that holds all functions and widgets that facilitate the combobox field.
        Contained keys are:
            - "clearer": A function that clears the combobox field.
            - "getter": A function that retrieves the value of the combobox field.
            - "setter": A function that sets the value of the combobox field.
            - "variable": A tkinter.BooleanVar instance that holds the value of the combobox field.
            - "root": A tkinter.Frame instance that holds the combobox field.
            - "label": A tkinter.Label instance that holds the label for the combobox field.
            - "combobox": A tkinter.Combobox instance that is used as a field.

        Args:
            label (str): The label for the combobox.
            master (tkinter.Misc): The master widget.
            namespace (str): The namespace for the combobox. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[str, str], None]]): A callback function that is called when the value of the combobox field changes. Defaults to None.
            values (List[str]): The list of string values of the combobox field.
            **kwargs: Any additional keyword arguments to be passed to the various tkinter widgets.

        Returns:
            Optional[Dict[str, Any]]: The created tkinter.Combobox instance or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Combobox.
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def clear(dispatch: bool = True) -> None:
                """
                Clears the combobox field by setting its value to an empty string.

                Args:
                    None

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to clear the combobox field.
                """
                try:
                    # Set the value of the combobox field to an empty string
                    result["combobox"].set(value="")

                    if dispatch:
                        # Dispatch the COMBOBOX_FIELD_CLEARED event
                        cls.dispatcher.dispatch(
                            event=Events.COMBOBOX_FIELD_CLEARED,
                            label=label,
                            namespace=namespace,
                            value=result["combobox"].get(),
                        )
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'clear' method from '{cls.__name__}': {e}"
                    )

                    # Re-raise the exception to the caller
                    raise e

            def get(dispatch: bool = True) -> Optional[str]:
                """
                Retrieves the value of the combobox field as a string.

                Args:
                    None

                Returns:
                    Optional[str]: The value of the combobox field as a string. Or None if an exception occurs.

                Raises:
                    Exception: If an exception occurs while attempting to retrieve the value of the combobox field.
                """
                try:
                    if dispatch:
                        # Dispatch the COMBOBOX_FIELD_GET event
                        cls.dispatcher.dispatch(
                            event=Events.COMBOBOX_FIELD_GET,
                            label=label,
                            namespace=namespace,
                            value=result["combobox"].get(),
                        )

                    # Return the value of the combobox field as a string
                    return result["combobox"].get()
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'get' method from '{cls.__name__}': {e}"
                    )

                    # Return None indicating an exception occurred
                    return None

            def on_button_clicked() -> None:
                """
                Handles the button click.

                This function calls the clear function.

                Args:
                    None

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to clear the combobox field.
                """
                try:
                    # Clear the combobox field
                    clear(dispatch=True)
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'on_button_clicked' method from '{cls.__name__}': {e}"
                    )

                    # Re-raise the exception to the caller
                    raise e

            def on_combobox_changed(dispatch: bool = True) -> None:
                """
                Handles the COMBOBOX_FIELD_CHANGED event.

                This function is called when the value of the combobox field changes.

                Args:
                    None

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to dispatch the COMBOBOX_FIELD_CHANGED event.
                """
                try:
                    if dispatch:
                        # Dispatch the COMBOBOX_FIELD_CHANGED event
                        cls.dispatcher.dispatch(
                            event=Events.COMBOBOX_FIELD_CHANGED,
                            label=label,
                            namespace=namespace,
                            value=result["combobox"].get(),
                        )

                    # Check, if the on_change_callback is present
                    if on_change_callback:
                        # Call the on_change_callback function with the new value
                        on_change_callback(label, result["combobox"].get())
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'on_combobox_changed' method from '{cls.__name__}': {e}"
                    )

                    # Re-raise the exception to the caller
                    raise e

            def set(
                value: str,
                dispatch: bool = True,
            ) -> None:
                """
                Sets the value of the combobox field.

                Args:
                    dispatch (bool, optional): Whether to dispatch the COMBOBOX_FIELD_SET event. Defaults to True.
                    value (str): The value to set for the combobox field.

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to set the value of the combobox field.
                """
                try:
                    if dispatch:
                        # Dispatch the COMBOBOX_FIELD_SET event
                        cls.dispatcher.dispatch(
                            event=Events.COMBOBOX_FIELD_SET,
                            label=label,
                            namespace=namespace,
                            value=value,
                        )

                    if value not in result["values"]:
                        # Add the value to the values list
                        result["values"].append(value)

                    # Set the value of the combobox field
                    result["combobox"].set(value=value)
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'set' method from '{cls.__name__}': {e}"
                    )

                    # Re-raise the exception to the caller
                    raise e

            # Store the values in the result dictionary
            result["values"] = values

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(
                master=master,
                **kwargs.get("root", {}),
            )

            # Configure the "Root" frame widget's 0th column to weight 0
            result["root"].grid_columnconfigure(
                index=0,
                weight=0,
            )

            # Configure the "Root" frame widget's 1st column to weight 1
            result["root"].grid_columnconfigure(
                index=1,
                weight=1,
            )

            # Configure the "Root" frame widget's 2nd column to weight 0
            result["root"].grid_columnconfigure(
                index=2,
                weight=0,
            )

            # Configure the "Root" frame widget's 0th row to weight 1
            result["root"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the "Label" label widget
            result["label"] = cls.get_label(
                master=result["root"],
                text=label,
                **kwargs.get("label", {}),
            )

            # Add the "Label" label widget to the "Root" frame widget
            result["label"].grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Create the "Combobox" combobox widget
            result["combobox"] = cls.get_combobox(
                master=result["root"],
                state="readonly",
                text="False",
                values=result["values"],
                **kwargs.get("combobox", {}),
            )

            # Add the "Combobox" combobox widget to the "Root" frame widget
            result["combobox"].grid(
                column=1,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Bind the "Combobox" combobox widget to the "on_combobox_changed" function
            result["combobox"].bind(
                func=lambda event: on_combobox_changed(),
                sequence="<<ComboboxSelected>>",
            )

            # Create the "Button" button widget
            result["button"] = cls.get_button(
                command=on_button_clicked,
                master=result["root"],
                text="X",
                **kwargs.get("button", {}),
            )

            # Add the "Button" combobox widget to the "Root" frame widget
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

            if value:
                # Set the value of the combobox field
                result["setter"](
                    dispatch=False,
                    value=value,
                )

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_combobox_field' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured

            return None

    @classmethod
    def get_countdown(
        cls,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        namespace: str,
        time_limit: int = 60,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a countdown widget with associated labels and dispatcher notifications.

        The returned dictionary contains the following keys:
            - "root": The container frame for the widgets
            - "information_label": The information label widget
            - "countdown_label": The countdown label widget

        Args:
            dispatcher (Dispatcher): The dispatcher instance used for event notifications.
            master (tkinter.Misc): The master widget.
            namespace (str): The namespace for dispatching events.
            time_limit (int, optional): The time limit for the countdown in minutes. Defaults to 60.
            **kwargs: Additional keyword arguments. These will be passed to the tkinter.Label constructors.

        Returns:
            Optional[Dict[str, Any]]: A dictionary containing the countdown widget elements, or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create the countdown widget.
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def notify_countdown_start() -> None:
                # Check, if the notify_start variable is True
                if result["notify_start"]:
                    # Dispatch the NOTIFY_UI_COUNTDOWN_STARTED event
                    dispatcher.dispatch(
                        event=Events.NOTIFY_UI_COUNTDOWN_STARTED,
                        namespace=namespace,
                    )

                # Set the notify_start variable to False
                result["notify_start"] = False

            def notify_countdown_ended() -> None:
                # Check, if the notify_end variable is True
                if result["notify_end"]:
                    # Dispatch the NOTIFY_UI_COUNTDOWN_ENDED event
                    dispatcher.dispatch(
                        event=Events.NOTIFY_UI_COUNTDOWN_ENDED,
                        namespace=namespace,
                    )

                # Set the notify_end variable to False
                result["notify_end"] = False

            def update_countdown_label() -> None:
                # Decrement the seconds variable
                result["seconds"] -= 1

                # Check, if the seconds variable is less than 0
                if result["seconds"] < 0:
                    # Dispatch the NOTIFY_UI_COUNTDOWN_ENDED event
                    notify_countdown_ended()

                    # Return early
                    return

                # Update the countdown label
                result["countdown_label"].configure(
                    text=str(timedelta(seconds=result["seconds"])),
                )

                # Schedule the update_countdown_label function to be called after 1000 milliseconds
                after(
                    func=update_countdown_label,
                    ms=1000,
                )

            # Initialize the seconds variable
            result["seconds"] = 60 * time_limit

            # Initialize the flag to notify the end of the countdown
            result["notify_end"] = True

            # Initialize the flag to notify the start of the countdown
            result["notify_start"] = True

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(master=master)

            # Configure the "Root" frame widget's 0th column to weight 1
            result["root"].grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the "Root" frame widget's 1st column to weight 1
            result["root"].grid_columnconfigure(
                index=1,
                weight=1,
            )

            # Configure the "Root" frame widget's 0th row to weight 1
            result["root"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the "Information Label" label widget
            result["information_label"] = cls.get_label(
                master=result["root"],
                text="Time left: ",
                **kwargs,
            )

            # Grid the "Information Label" label widget in the "Root" frame widget
            result["information_label"].grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Create the "Countdown Label" label widget
            result["countdown_label"] = cls.get_label(
                master=result["root"],
                text="",
                **kwargs,
            )

            # Grid the "Countdown Label" label widget in the "Root" frame widget
            result["countdown_label"].grid(
                column=1,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Update the countdown label
            update_countdown_label()

            # Dispatch the NOTIFY_UI_COUNTDOWN_STARTED event
            notify_countdown_start()

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_countdown' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_countup(
        cls,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        namespace: str,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a countup widget with associated labels and dispatcher notifications.

        The returned dictionary contains the following keys:
            - "root": The container frame for the widgets
            - "information_label": The information label widget
            - "countup_label": The countup label widget

        Args:
            dispatcher (Dispatcher): The dispatcher instance used for event notifications.
            master (tkinter.Misc): The master widget.
            namespace (str): The namespace for dispatching events.
            **kwargs: Additional keyword arguments. These will be passed to the tkinter.Label constructors.

        Returns:
            Optional[Dict[str, Any]]: A dictionary containing the countup widget elements, or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create the countup widget.
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def notify_countup_start() -> None:
                # Check, if the notify_start variable is True
                if result["notify_start"]:
                    # Dispatch the NOTIFY_UI_COUNTUP_STARTED event
                    dispatcher.dispatch(
                        event=Events.NOTIFY_UI_COUNTUP_STARTED,
                        namespace=namespace,
                    )

                # Set the notify_start variable to False
                result["notify_start"] = False

            def update_countup_label() -> None:
                """
                Updates the label displaying the elapsed time of the countup.

                This function is scheduled to be called every 1000 milliseconds using the after method of the label widget.
                """

                # Update the text of the label
                result["countup_label"].config(
                    text=str(timedelta(seconds=result["seconds"])),
                )

                # Increment the seconds variable
                result["seconds"] += 1

                # Schedule the next call to update_countup_label
                result["countup_label"].after(
                    ms=1000,
                    func=update_countup_label,
                )

            # Initialize the flag to notify the start of the countup
            result["notify_start"] = True

            # Initialize the seconds variable
            result["seconds"] = 0

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(master=master)

            # Configure the "Root" frame widget's 0th column to weight 1
            result["root"].grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the "Root" frame widget's 1st column to weight 1
            result["root"].grid_columnconfigure(
                index=1,
                weight=1,
            )

            # Configure the "Root" frame widget's 0th row to weight 1
            result["root"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the "Information Label" label widget
            result["information_label"] = cls.get_label(
                master=result["root"],
                text="Time elapsed: ",
                **kwargs,
            )

            # Grid the "Information Label" label widget in the "Root" frame widget
            result["information_label"].grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Create the "Countdown Label" label widget
            result["countdown_label"] = cls.get_label(
                master=result["root"],
                text="",
                **kwargs,
            )

            # Grid the "Countdown Label" label widget in the "Root" frame widget
            result["countdown_label"].grid(
                column=1,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Update the countup label
            update_countup_label()

            # Dispatch the NOTIFY_UI_COUNTUP_STARTED event
            notify_countup_start()

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_countup' method from '{cls.__name__}': {e}"
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
    def get_float_scale_field(
        cls,
        label: str,
        master: tkinter.Misc,
        from_: float = 0,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str], None]] = None,
        resolution: float = 1,
        to: float = 100,
        value: float = 0,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of tkinter.Scale that is used as a field.

        This method creates a dictionary that holds all functions and widgets that facilitate the scale field.
        Contained keys are:
            - "clearer": A function that clears the scale field.
            - "getter": A function that retrieves the value of the scale field.
            - "setter": A function that sets the value of the scale field.
            - "variable": A tkinter.BooleanVar instance that holds the value of the scale field.
            - "root": A tkinter.Frame instance that holds the scale field.
            - "label": A tkinter.Label instance that holds the label for the scale field.
            - "scale": A tkinter.Scale instance that is used as a field.

        Args:
            from_ (float): The minimum of the scale.
            label (str): The label for the scale.
            master (tkinter.Misc): The master widget.
            namespace (str): The namespace for the scale. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[str], None]]): A callback function that is called when the value of the scale field changes. Defaults to None.
            resolution (float): The step size of the scale.
            to (float): The maximum of the scale.
            value (float): The float value of the scale field.
            **kwargs: Any additional keyword arguments to be passed to the various tkinter widgets.

        Returns:
            Optional[Dict[str, Any]]: The created tkinter.Scale instance or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Scale.
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def clear(dispatch: int = True) -> None:
                """
                Clears the scale field by setting its value to an empty float.

                Args:
                    None

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to clear the scale field.
                """
                try:
                    # Set the value of the scale field to an empty float
                    result["variable"].set(value="")

                    if dispatch:
                        # Dispatch the SCALE_FIELD_CLEARED event
                        cls.dispatcher.dispatch(
                            event=Events.SCALE_FIELD_CLEARED,
                            label=label,
                            namespace=namespace,
                            value=result["variable"].get(),
                        )
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'clear' method from '{cls.__name__}': {e}"
                    )

                    # Re-raise the exception to the caller
                    raise e

            def get(dispatch: int = True) -> Optional[float]:
                """
                Retrieves the value of the scale field as a float.

                Args:
                    None

                Returns:
                    Optional[float]: The value of the scale field as a float. Or None if an exception occurs.

                Raises:
                    Exception: If an exception occurs while attempting to retrieve the value of the scale field.
                """
                try:
                    if dispatch:
                        # Dispatch the SCALE_FIELD_GET event
                        cls.dispatcher.dispatch(
                            event=Events.SCALE_FIELD_GET,
                            label=label,
                            namespace=namespace,
                            value=result["variable"].get(),
                        )

                    # Return the value of the scale field as a float
                    return result["variable"].get()
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'get' method from '{cls.__name__}': {e}"
                    )

                    # Return None indicating an exception occurred
                    return None

            def on_button_clicked() -> None:
                """
                Handles the button click.

                This function calls the clear function.

                Args:
                    None

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to clear the scale field.
                """
                try:
                    # Clear the scale field
                    clear(dispatch=True)
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'on_button_clicked' method from '{cls.__name__}': {e}"
                    )

                    # Re-raise the exception to the caller
                    raise e

            def on_scale_changed(dispatch: int = True) -> None:
                """
                Handles the SCALE_FIELD_CHANGED event.

                This function is called when the value of the scale field changes.

                Args:
                    None

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to dispatch the SCALE_FIELD_CHANGED event.
                """
                try:
                    if dispatch:
                        # Dispatch the SCALE_FIELD_CHANGED event
                        cls.dispatcher.dispatch(
                            event=Events.SCALE_FIELD_CHANGED,
                            label=label,
                            namespace=namespace,
                            value=result["variable"].get(),
                        )

                    # Check, if the on_change_callback is present
                    if on_change_callback:
                        # Call the on_change_callback function with the new value
                        on_change_callback(result["variable"].get())
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'on_scale_changed' method from '{cls.__name__}': {e}"
                    )

                    # Re-raise the exception to the caller
                    raise e

            def set(
                value: float,
                dispatch: int = True,
            ) -> None:
                """
                Sets the value of the scale field.

                Args:
                    dispatch (int, optional): Whether to dispatch the SCALE_FIELD_SET event. Defaults to True.
                    value (float, optional): The value to set for the scale field.

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to set the value of the scale field.
                """
                try:
                    if dispatch:
                        # Dispatch the SCALE_FIELD_SET event
                        cls.dispatcher.dispatch(
                            event=Events.SCALE_FIELD_SET,
                            label=label,
                            namespace=namespace,
                            value=value,
                        )

                    if value not in result["values"]:
                        # Add the value to the values list
                        result["values"].append(value)

                    # Set the value of the scale field
                    result["variable"].set(value=value)
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'set' method from '{cls.__name__}': {e}"
                    )

                    # Re-raise the exception to the caller
                    raise e

            # Create the "Variable" float variable
            result["variable"] = cls.get_double_variable(value=value)

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(
                master=master,
                **kwargs.get("root", {}),
            )

            # Configure the "Root" frame widget's 0th column to weight 0
            result["root"].grid_columnconfigure(
                index=0,
                weight=0,
            )

            # Configure the "Root" frame widget's 1st column to weight 0
            result["root"].grid_columnconfigure(
                index=1,
                weight=0,
            )

            # Configure the "Root" frame widget's 2nd column to weight 0
            result["root"].grid_columnconfigure(
                index=2,
                weight=0,
            )

            # Configure the "Root" frame widget's 0th row to weight 1
            result["root"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the "Label" label widget
            result["label"] = cls.get_label(
                master=result["root"],
                text=label,
                **kwargs.get("label", {}),
            )

            # Add the "Label" label widget to the "Root" frame widget
            result["label"].grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Create the "Scale" scale widget
            result["scale"] = cls.get_scale(
                command=on_scale_changed,
                from_=from_,
                master=result["root"],
                resolution=resolution,
                to=to,
                value=value,
                variable=result["variable"],
                **kwargs.get("scale", {}),
            )

            # Add the "Scale" scale widget to the "Root" frame widget
            result["scale"].grid(
                column=1,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Create the "Button" button widget
            result["button"] = cls.get_button(
                command=on_button_clicked,
                master=result["root"],
                text="X",
                **kwargs.get("button", {}),
            )

            # Add the "Button" scale widget to the "Root" frame widget
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
                message=f"Caught an exception while attempting to run 'get_float_scale_field' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured

            return None

    @classmethod
    def get_float_spinbox_field(
        cls,
        label: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[float], None]] = None,
        setp_size: float = 1,
        value: float = 0,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of a tkinter widgets dictionary for an int spinbox field.

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
            namespace (str): The namespace for the widgets. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[float], None]]): A callback function to be called when the value of the variable changes. Defaults to None.
            setp_size (int): The step size for the integer spinbox. Defaults to 1.
            value (int): The initial value for the variable. Defaults to 0.
            **kwargs: Additional keyword arguments for the entry widget.

        Returns:
            Optional[Dict[str, Any]]: The created widgets dictionary or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.DoubleVar.
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def clear(dispatch: bool = True) -> None:
                """
                Clears the readonly field by setting its value to 0.

                Args:
                    None

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to clear the int spinbox field.
                """
                try:
                    # Clear the tkinter.DoubleVar widget
                    result["variable"].set(value=0)

                    if dispatch:
                        # Dispatch the FLOAT_SPINBOX_FIELD_CLEARED event
                        cls.dispatcher.dispatch(
                            event=Events.FLOAT_SPINBOX_FIELD_CLEARED,
                            label=label,
                            namespace=namespace,
                            value=result["variable"].get(),
                        )
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'clear' method from '{cls.__name__}': {e}"
                    )

                    # Re-raise the exception to the caller
                    raise e

            def get(dispatch: bool = True) -> Optional[float]:
                """
                Retrieves the value of the int spinbox field as an integer.

                Args:
                    None

                Returns:
                    Optional[float]: The value of the int spinbox field as an integer. Or None if an exception occurs.

                Raises:
                    Exception: If an exception occurs while attempting to retrieve the value of the int spinbox field.
                """
                try:
                    if dispatch:
                        # Dispatch the FLOAT_SPINBOX_FIELD_GET event
                        cls.dispatcher.dispatch(
                            event=Events.FLOAT_SPINBOX_FIELD_GET,
                            label=label,
                            namespace=namespace,
                            value=result["variable"].get(),
                        )

                    # Return the value of the readonly field as an int.
                    return result["variable"].get()
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'get' method from '{cls.__name__}': {e}"
                    )

                    # Return None indicating an exception occurred
                    return None

            def on_entry_changed(dispatch: bool = True) -> None:
                """
                Handles the SINGLE_LINE_FIELD_CHANGED event.

                This function is called when the value of the int spinbox field changes.

                Args:
                    None

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to dispatch the SINGLE_LINE_FIELD_CHANGED event.
                """
                try:
                    if dispatch:
                        # Dispatch the SINGLE_LINE_FIELD_CHANGED event
                        cls.dispatcher.dispatch(
                            event=Events.FLOAT_SPINBOX_FIELD_CHANGED,
                            label=label,
                            namespace=namespace,
                            value=result["variable"].get(),
                        )

                    # Check, if the on_change_callback is present
                    if on_change_callback:
                        # Call the on_change_callback function with the new value
                        on_change_callback(result["variable"].get())
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'on_entry_changed' method from '{cls.__name__}': {e}"
                    )

                    # Re-raise the exception to the caller
                    raise e

            def set(
                value: float,
                dispatch: bool = True,
            ) -> None:
                """
                Sets the value of the readonly field.

                Args:
                    dispatch (bool, optional): Whether to dispatch the SINGLE_LINE_FIELD_SET event. Defaults to True.
                    value (str, optional): The value to set for the readonly field. Defaults to an empty string.

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to set the value of the readonly field.
                """
                try:
                    if dispatch:
                        # Dispatch the FLOAT_SPINBOX_FIELD_SET event
                        cls.dispatcher.dispatch(
                            event=Events.FLOAT_SPINBOX_FIELD_SET,
                            label=label,
                            namespace=namespace,
                            value=value,
                        )

                    # Set the value of the readonly field
                    result["variable"].set(value=value)
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'set' method from '{cls.__name__}': {e}"
                    )

                    # Re-raise the exception to the caller
                    raise e

            # Create the "Variable" tkinter.DoubleVar variable
            result["variable"] = cls.get_double_variable(value=value)

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(
                master=master,
                **kwargs.get("root", {}),
            )

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
                **kwargs.get("label", {}),
            )

            # Create the "Decrement" button widget
            result["decrement_button"] = cls.get_button(
                command=lambda: (
                    result["variable"].set(value=result["variable"].get() - setp_size),
                    on_entry_changed(),
                ),
                master=result["root"],
                text="-",
                **kwargs.get("decrement_button", {}),
            )

            # Create the "Entry" entry widget
            result["entry"] = cls.get_entry(
                master=result["root"],
                state="readonly",
                textvariable=result["variable"],
                **kwargs.get("entry", {}),
            )

            # Create the "Increment" button widget
            result["increment_button"] = cls.get_button(
                command=lambda: (
                    result["variable"].set(value=result["variable"].get() + setp_size),
                    on_entry_changed(),
                ),
                master=result["root"],
                text="+",
                **kwargs.get("increment_button", {}),
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
    def get_int_scale_field(
        cls,
        label: str,
        master: tkinter.Misc,
        from_: int = 0,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str], None]] = None,
        resolution: int = 1,
        to: int = 100,
        value: int = 0,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of tkinter.Scale that is used as a field.

        This method creates a dictionary that holds all functions and widgets that facilitate the scale field.
        Contained keys are:
            - "clearer": A function that clears the scale field.
            - "getter": A function that retrieves the value of the scale field.
            - "setter": A function that sets the value of the scale field.
            - "variable": A tkinter.BooleanVar instance that holds the value of the scale field.
            - "root": A tkinter.Frame instance that holds the scale field.
            - "label": A tkinter.Label instance that holds the label for the scale field.
            - "scale": A tkinter.Scale instance that is used as a field.

        Args:
            from_ (int): The minimum value of the scale.
            label (str): The label for the scale.
            master (tkinter.Misc): The master widget.
            namespace (str): The namespace for the scale. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[str], None]]): A callback function that is called when the value of the scale field changes. Defaults to None.
            resolution (int): The resolution of the scale. Defaults to 1.
            to (int): The maximum value of the scale. Defaults to 100.
            value (int): The initial value of the scale. Defaults to 0.
            **kwargs: Any additional keyword arguments to be passed to the various tkinter widgets.

        Returns:
            Optional[Dict[str, Any]]: The created tkinter.Scale instance or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Scale.
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def clear(dispatch: int = True) -> None:
                """
                Clears the scale field by setting its value to an empty string.

                Args:
                    None

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to clear the scale field.
                """
                try:
                    # Set the value of the scale field to an empty string
                    result["variable"].set(value=value)

                    if dispatch:
                        # Dispatch the SCALE_FIELD_CLEARED event
                        cls.dispatcher.dispatch(
                            event=Events.SCALE_FIELD_CLEARED,
                            label=label,
                            namespace=namespace,
                            value=result["variable"].get(),
                        )
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'clear' method from '{cls.__name__}': {e}"
                    )

                    # Re-raise the exception to the caller
                    raise e

            def get(dispatch: int = True) -> Optional[str]:
                """
                Retrieves the value of the scale field as a string.

                Args:
                    None

                Returns:
                    Optional[str]: The value of the scale field as a string. Or None if an exception occurs.

                Raises:
                    Exception: If an exception occurs while attempting to retrieve the value of the scale field.
                """
                try:
                    if dispatch:
                        # Dispatch the SCALE_FIELD_GET event
                        cls.dispatcher.dispatch(
                            event=Events.SCALE_FIELD_GET,
                            label=label,
                            namespace=namespace,
                            value=result["variable"].get(),
                        )

                    # Return the value of the scale field as a string
                    return result["variable"].get()
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'get' method from '{cls.__name__}': {e}"
                    )

                    # Return None indicating an exception occurred
                    return None

            def on_button_clicked() -> None:
                """
                Handles the button click.

                This function calls the clear function.

                Args:
                    None

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to clear the scale field.
                """
                try:
                    # Clear the scale field
                    clear(dispatch=True)
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'on_button_clicked' method from '{cls.__name__}': {e}"
                    )

                    # Re-raise the exception to the caller
                    raise e

            def on_scale_changed(dispatch: int = True) -> None:
                """
                Handles the SCALE_FIELD_CHANGED event.

                This function is called when the value of the scale field changes.

                Args:
                    None

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to dispatch the SCALE_FIELD_CHANGED event.
                """
                try:
                    if dispatch:
                        # Dispatch the SCALE_FIELD_CHANGED event
                        cls.dispatcher.dispatch(
                            event=Events.SCALE_FIELD_CHANGED,
                            label=label,
                            namespace=namespace,
                            value=result["variable"].get(),
                        )

                    # Check, if the on_change_callback is present
                    if on_change_callback:
                        # Call the on_change_callback function with the new value
                        on_change_callback(result["variable"].get())
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'on_scale_changed' method from '{cls.__name__}': {e}"
                    )

                    # Re-raise the exception to the caller
                    raise e

            def set(
                value: int,
                dispatch: int = True,
            ) -> None:
                """
                Sets the value of the scale field.

                Args:
                    dispatch (int, optional): Whether to dispatch the SCALE_FIELD_SET event. Defaults to True.
                    value (int): The value to set for the scale field.

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to set the value of the scale field.
                """
                try:
                    if dispatch:
                        # Dispatch the SCALE_FIELD_SET event
                        cls.dispatcher.dispatch(
                            event=Events.SCALE_FIELD_SET,
                            label=label,
                            namespace=namespace,
                            value=value,
                        )

                    if value not in result["values"]:
                        # Add the value to the values list
                        result["values"].append(value)

                    # Set the value of the scale field
                    result["variable"].set(value=value)
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'set' method from '{cls.__name__}': {e}"
                    )

                    # Re-raise the exception to the caller
                    raise e

            # Create the "Variable" string variable
            result["variable"] = cls.get_int_variable(value=value)

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(
                master=master,
                **kwargs.get("root", {}),
            )

            # Configure the "Root" frame widget's 0th column to weight 0
            result["root"].grid_columnconfigure(
                index=0,
                weight=0,
            )

            # Configure the "Root" frame widget's 1st column to weight 0
            result["root"].grid_columnconfigure(
                index=1,
                weight=0,
            )

            # Configure the "Root" frame widget's 2nd column to weight 0
            result["root"].grid_columnconfigure(
                index=2,
                weight=0,
            )

            # Configure the "Root" frame widget's 0th row to weight 1
            result["root"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the "Label" label widget
            result["label"] = cls.get_label(
                master=result["root"],
                text=label,
                **kwargs.get("label", {}),
            )

            # Add the "Label" label widget to the "Root" frame widget
            result["label"].grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Create the "Scale" scale widget
            result["scale"] = cls.get_scale(
                command=on_scale_changed,
                from_=from_,
                master=result["root"],
                orient=HORIZONTAL,
                resolution=resolution,
                to=to,
                variable=result["variable"],
                **kwargs.get("scale", {}),
            )

            # Add the "Scale" scale widget to the "Root" frame widget
            result["scale"].grid(
                column=1,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Create the "Button" button widget
            result["button"] = cls.get_button(
                command=on_button_clicked,
                master=result["root"],
                text="X",
                **kwargs.get("button", {}),
            )

            # Add the "Button" scale widget to the "Root" frame widget
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
                message=f"Caught an exception while attempting to run 'get_int_scale_field' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured

            return None

    @classmethod
    def get_int_spinbox_field(
        cls,
        label: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[int], None]] = None,
        setp_size: int = 1,
        value: int = 0,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of a tkinter widgets dictionary for an int spinbox field.

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
            namespace (str): The namespace for the widgets. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[int], None]]): A callback function to be called when the value of the variable changes. Defaults to None.
            setp_size (int): The step size for the integer spinbox. Defaults to 1.
            value (int): The initial value for the variable. Defaults to 0.
            **kwargs: Additional keyword arguments for the entry widget.

        Returns:
            Optional[Dict[str, Any]]: The created widgets dictionary or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.DoubleVar.
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def clear(dispatch: bool = True) -> None:
                """
                Clears the readonly field by setting its value to 0.

                Args:
                    None

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to clear the int spinbox field.
                """
                try:
                    # Clear the tkinter.DoubleVar widget
                    result["variable"].set(value=0)

                    if dispatch:
                        # Dispatch the INT_SPINBOX_FIELD_CLEARED event
                        cls.dispatcher.dispatch(
                            event=Events.INT_SPINBOX_FIELD_CLEARED,
                            label=label,
                            namespace=namespace,
                            value=result["variable"].get(),
                        )
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'clear' method from '{cls.__name__}': {e}"
                    )

                    # Re-raise the exception to the caller
                    raise e

            def get(dispatch: bool = True) -> Optional[int]:
                """
                Retrieves the value of the int spinbox field as an integer.

                Args:
                    None

                Returns:
                    Optional[int]: The value of the int spinbox field as an integer. Or None if an exception occurs.

                Raises:
                    Exception: If an exception occurs while attempting to retrieve the value of the int spinbox field.
                """
                try:
                    if dispatch:
                        # Dispatch the INT_SPINBOX_FIELD_GET event
                        cls.dispatcher.dispatch(
                            event=Events.INT_SPINBOX_FIELD_GET,
                            label=label,
                            namespace=namespace,
                            value=result["variable"].get(),
                        )

                    # Return the value of the readonly field as an int.
                    return result["variable"].get()
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'get' method from '{cls.__name__}': {e}"
                    )

                    # Return None indicating an exception occurred
                    return None

            def on_entry_changed(dispatch: bool = True) -> None:
                """
                Handles the SINGLE_LINE_FIELD_CHANGED event.

                This function is called when the value of the int spinbox field changes.

                Args:
                    None

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to dispatch the SINGLE_LINE_FIELD_CHANGED event.
                """
                try:
                    if dispatch:
                        # Dispatch the SINGLE_LINE_FIELD_CHANGED event
                        cls.dispatcher.dispatch(
                            event=Events.INT_SPINBOX_FIELD_CHANGED,
                            label=label,
                            namespace=namespace,
                            value=result["variable"].get(),
                        )

                    # Check, if the on_change_callback is present
                    if on_change_callback:
                        # Call the on_change_callback function with the new value
                        on_change_callback(result["variable"].get())
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'on_entry_changed' method from '{cls.__name__}': {e}"
                    )

                    # Re-raise the exception to the caller
                    raise e

            def set(
                value: int,
                dispatch: bool = True,
            ) -> None:
                """
                Sets the value of the readonly field.

                Args:
                    dispatch (bool, optional): Whether to dispatch the SINGLE_LINE_FIELD_SET event. Defaults to True.
                    value (str, optional): The value to set for the readonly field. Defaults to an empty string.

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to set the value of the readonly field.
                """
                try:
                    if dispatch:
                        # Dispatch the INT_SPINBOX_FIELD_SET event
                        cls.dispatcher.dispatch(
                            event=Events.INT_SPINBOX_FIELD_SET,
                            label=label,
                            namespace=namespace,
                            value=value,
                        )

                    # Set the value of the readonly field
                    result["variable"].set(value=value)
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'set' method from '{cls.__name__}': {e}"
                    )

                    # Re-raise the exception to the caller
                    raise e

            # Create the "Variable" tkinter.IntVar variable
            result["variable"] = cls.get_int_variable(value=value)

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(
                master=master,
                **kwargs.get("root", {}),
            )

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
                **kwargs.get("label", {}),
            )

            # Place the "Label" label widget within the "Root" frame widget
            result["label"].grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Create the "Decrement" button widget
            result["decrement_button"] = cls.get_button(
                command=lambda: (
                    result["variable"].set(value=result["variable"].get() - setp_size),
                    on_entry_changed(),
                ),
                master=result["root"],
                text="-",
                **kwargs.get("decrement_button", {}),
            )

            # Place the "Decrement" button widget within the "Root" frame widget
            result["decrement_button"].grid(
                column=1,
                padx=5,
                pady=5,
                row=0,
            )

            # Create the "Entry" entry widget
            result["entry"] = cls.get_entry(
                master=result["root"],
                state="readonly",
                textvariable=result["variable"],
                **kwargs.get("entry", {}),
            )

            # Place the "Entry" entry widget within the "Root" frame widget
            result["entry"].grid(
                column=2,
                row=0,
                sticky=NSEW,
            )

            # Create the "Increment" button widget
            result["increment_button"] = cls.get_button(
                command=lambda: (
                    result["variable"].set(value=result["variable"].get() + setp_size),
                    on_entry_changed(),
                ),
                master=result["root"],
                text="+",
                **kwargs.get("increment_button", {}),
            )

            # Place the "Increment" button widget within the "Root" frame widget
            result["increment_button"].grid(
                column=3,
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
                message=f"Caught an exception while attempting to run 'get_int_spinbox_field' method from '{cls.__name__}': {e}"
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

            # Add the clearer function to the result dictionary
            result["clearer"] = clear

            # Add the getter function to the result dictionary
            result["getter"] = get

            # Add the setter function to the result dictionary
            result["setter"] = set

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
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
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str], None]] = None,
        value: str = "",
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of tkinter.Text that is used as a field.

        This method creates a dictionary that holds all functions and widgets that facilitate the multi line text field.
        Contained keys are:
            - "clearer": A function that clears the multi line text field.
            - "getter": A function that retrieves the value of the multi line text field.
            - "setter": A function that sets the value of the multi line textfield.
            - "variable": A tkinter.stringVar instance that holds the value of the multi line textfield.
            - "root": A tkinter.Frame instance that holds the multi line textfield.
            - "label": A tkinter.Label instance that holds the label for the multi line textfield.
            - "text": A tkinter.Entry instance that is used as a field.
            - "scrollbar": A tkinter.Scrollbar instance that is used to scroll the multi line textfield.
            - "button": A tkinter.Button that clears the multi line text field.

        Args:
            label (str): The label for the multi line text field.
            master (tkinter.Misc): The master widget.
            namespace (str): The namespace for the multi line text field. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[str], None]]): A callback function that is called when the value of the multi line text field changes. Defaults to None.
            value (bool): The initial value of the multi line text field. Defaults to an empty string.
            **kwargs: Any additional keyword arguments to be passed to the various tkinter widgets.

        Returns:
            Optional[Dict[str, Any]]: The created tkinter.Entry instance or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Entry.
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def clear(dispatch: bool = True) -> None:
                """
                Clears the multi line text field by setting its value to an empty string.

                Args:
                    None

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to clear the multi line text field.
                """
                try:
                    # Set the value of the multi line text field field to an empty string
                    result["text"].delete(
                        index1="1.0",
                        index2=END,
                    )

                    if dispatch:
                        # Dispatch the MULTI_LINE_FIELD_CLEARED event
                        cls.dispatcher.dispatch(
                            event=Events.MULTI_LINE_TEXT_FIELD_CLEARED,
                            label=label,
                            namespace=namespace,
                            value=result["text"].get(
                                index1="1.0",
                                index2=END,
                            ),
                        )
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'clear' method from '{cls.__name__}': {e}"
                    )

            def get(dispatch: bool = True) -> Optional[str]:
                """
                Retrieves the value of the multi line text field as a string.

                Args:
                    None

                Returns:
                    Optional[str]: The value of the multi line text field as a string. Or None if an exception occurs.

                Raises:
                    Exception: If an exception occurs while attempting to retrieve the value of the multi line text field.
                """
                try:
                    if dispatch:
                        # Dispatch the MULTI_LINE_FIELD_GET event
                        cls.dispatcher.dispatch(
                            event=Events.MULTI_LINE_TEXT_FIELD_GET,
                            label=label,
                            namespace=namespace,
                            value=result["text"].get(
                                index1="1.0",
                                index2=END,
                            ),
                        )

                    # Return the value of the multi line text field as a string
                    return result["text"].get(
                        index1="1.0",
                        index2=END,
                    )
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'get' method from '{cls.__name__}': {e}"
                    )

                    # Return None indicating an exception occurred
                    return None

            def on_button_clicked() -> None:
                """
                Handles the button click.

                This function calls the clear function.

                Args:
                    None

                Returns:
                    None
                """
                # Clear the multi line text field
                clear(dispatch=True)

            def on_text_changed(dispatch: bool = True) -> None:
                """
                Handles the MULTI_LINE_FIELD_CHANGED event.

                This function is called when the value of the multi line text field changes.

                Args:
                    None

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to dispatch the MULTI_LINE_FIELD_CHANGED event.
                """
                try:
                    if dispatch:
                        # Dispatch the MULTI_LINE_FIELD_CHANGED event
                        cls.dispatcher.dispatch(
                            event=Events.MULTI_LINE_TEXT_FIELD_CHANGED,
                            label=label,
                            namespace=namespace,
                            value=result["text"].get(
                                index1="1.0",
                                index2=END,
                            ),
                        )

                    # Check, if the on_change_callback is present
                    if on_change_callback:
                        # Call the on_change_callback function with the new value
                        on_change_callback(
                            result["text"].get(
                                index1="1.0",
                                index2=END,
                            )
                        )
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'on_text_changed' method from '{cls.__name__}': {e}"
                    )

            def set(
                dispatch: bool = True,
                value: str = "",
            ) -> None:
                """
                Sets the value of the multi line text field.

                Args:
                    dispatch (bool, optional): Whether to dispatch the MULTI_LINE_FIELD_SET event. Defaults to True.
                    value (str, optional): The value to set for the multi line text field. Defaults to an empty string.

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to set the value of the multi line text field.
                """
                try:
                    # Clear the text widget
                    result["text"].delete(
                        index1="1.0",
                        index2=END,
                    )

                    # Insert the passed string value into the text widget
                    result["text"].insert(
                        chars=value,
                        index="1.0",
                    )

                    if dispatch:
                        # Dispatch the MULTI_LINE_FIELD_SET event
                        cls.dispatcher.dispatch(
                            event=Events.MULTI_LINE_FIELD_SET,
                            label=label,
                            namespace=namespace,
                            value=value,
                        )
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'set' method from '{cls.__name__}': {e}"
                    )

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(
                master=master,
                **kwargs.get("root", {}),
            )

            # Configure the "Root" frame widget's 0th column to weight 0
            result["root"].grid_columnconfigure(
                index=0,
                weight=0,
            )

            # Configure the "Root" frame widget's 1st column to weight 1
            result["root"].grid_columnconfigure(
                index=1,
                weight=1,
            )

            # Configure the "Root" frame widget's 2nd column to weight 0
            result["root"].grid_columnconfigure(
                index=2,
                weight=0,
            )

            # Configure the "Root" frame widget's 0th row to weight 0
            result["root"].grid_rowconfigure(
                index=0,
                weight=0,
            )

            # Configure the "Root" frame widget's 1st row to weight 1
            result["root"].grid_rowconfigure(
                index=1,
                weight=1,
            )

            # Configure the "Root" frame widget's 2nd row to weight 0
            result["root"].grid_rowconfigure(
                index=2,
                weight=0,
            )

            # Create the "Label" label widget
            result["label"] = cls.get_label(
                master=result["root"],
                text=label,
                **kwargs.get("label", {}),
            )

            # Add the "Label" label widget to the "Root" frame widget
            result["label"].grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Create the "Text" text widget
            result["text"] = cls.get_text(
                master=result["root"],
                **kwargs.get("text", {}),
            )

            # Bind the "Text" text widget to the "on_text_changed" function
            result["text"].bind(
                func=lambda event: on_text_changed(),
                sequence="<KeyRelease>",
            )

            # Add the "Entry" text widget to the "Root" frame widget
            result["text"].grid(
                column=1,
                padx=5,
                pady=5,
                row=1,
                sticky=NSEW,
            )

            # Check if the value is present
            if value:
                # Set the value of the text widget
                result["text"].insert(
                    chars=value,
                    index="1.0",
                )

            # Create the "Scrollbar" scrollbar widget
            result["scrollbar"] = cls.get_scrollbar(
                command=result["text"].yview,
                master=result["root"],
                orient=VERTICAL,
            )

            # Add the "scrollbar" scrollbar widget to the "Root" frame widget
            result["scrollbar"].grid(
                column=2,
                padx=5,
                pady=5,
                row=1,
                sticky=NS,
            )

            # Configure the "Text" text widget's scrollbar
            result["text"].config(yscrollcommand=result["scrollbar"].set)

            # Create the "Button" button widget
            result["button"] = cls.get_button(
                command=on_button_clicked,
                master=result["root"],
                text="X",
                **kwargs.get("button", {}),
            )

            # Add the "Entry" text widget to the "Root" frame widget
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

            # Initialize the listbox widget as None
            result["listbox"] = None

            # Initialize the selection key as an empty list
            result["selection"] = []

            # Initialize the toplevel widget as None
            result["toplevel"] = None

            # Add the values to the result dictionary
            result["values"] = values

            def clear() -> None:
                """
                Clears the selected value from the single select field.

                Returns:
                    None
                """

                # Set the value associated with the "selection" key to None
                result["selection"] = []

                # Iterate over the children of the "Container" frame widget
                for child in result["container"].winfo_children():
                    # Destroy each child widget
                    child.destroy()

            def get() -> Optional[List[str]]:
                """
                Gets the selected value(s) from the single select field.

                Returns:
                    Optional[List[str]]: The selected value(s) or None if no value is selected.
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
                selection_indices: Optional[Tuple[int]] = tuple(
                    result["listbox"].curselection()
                )

                # Check, if selection indices are available
                if not selection_indices or len(selection_indices) == 0:
                    # Return early
                    return
                else:
                    # Appendselected value(s) to the  the value associated with the "selection" key with the selected value(s)
                    result["selection"].append(
                        result["listbox"].get(*selection_indices)
                    )

                # Iterate over the children of the "Container" frame widget
                for child in result["container"].winfo_children():
                    # Destroy each child widget
                    child.destroy()

                # Iterate over the selection
                for (
                    index,
                    value,
                ) in enumerate(iterable=result["selection"]):
                    # Configure the "Container" frame widget's index column to weight 1
                    result["container"].grid_columnconfigure(
                        index=index,
                        weight=1,
                    )

                    # Create the "Value frame" frame widget
                    result[f"value_frame_{index}"] = cls.get_frame(
                        master=result["container"]
                    )

                    # Configure the "Value frame" frame widget's 1st column to weight 1
                    result[f"value_frame_{index}"].grid_columnconfigure(
                        index=0,
                        weight=1,
                    )

                    # Configure the "Value frame" frame widget's 2nd column to weight 0
                    result[f"value_frame_{index}"].grid_columnconfigure(
                        index=1,
                        weight=0,
                    )

                    # Place the "Value frame" frame widget within the "Container" frame widget
                    result[f"value_frame_{index}"].grid(
                        column=index,
                        padx=5,
                        pady=5,
                        row=0,
                        sticky=NSEW,
                    )

                    # Create the "Value label" label widget
                    result[f"value_label_{index}"] = cls.get_label(
                        master=result[f"value_frame_{index}"],
                        text=value,
                        **kwargs,
                    )

                    # Place the "Value label" label widget within the "Value frame" frame widget
                    result[f"value_label_{index}"].grid(
                        column=0,
                        padx=5,
                        pady=5,
                        row=0,
                        sticky=NSEW,
                    )

                    # Create the "Value remove button" button widget
                    result[f"value_{index}_remove_button"] = cls.get_button(
                        command=lambda: on_value_remove_button_click(index=index),
                        master=result[f"value_frame_{index}"],
                        text="X",
                        width=3,
                        **kwargs,
                    )

                    # Place the "Value remove button" button widget within the "Value frame" frame widget
                    result[f"value_{index}_remove_button"].grid(
                        column=1,
                        padx=5,
                        pady=5,
                        row=0,
                    )

            def on_toplevel_destroy() -> None:
                """
                Called when the "Toplevel" toplevel widget is destroyed.

                Destroys the toplevel widget and the listbox widget associated with the result dictionary.

                Returns:
                    None
                """

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

            def on_value_remove_button_click(index: int) -> None:
                """
                Called when the "Value remove button" button widget is clicked.

                Destroys the value frame widget associated with the given index and removes the value at the given index from the selection list.

                Args:
                    index (int): The index of the value to be removed.

                Returns:
                    None
                """

                # Destroy the value frame widget associated with the given index
                result[f"value_frame_{index}"].destroy()

                # Remove the value at the given index from the selection list
                result["selection"].pop(index)

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

                    # Configure the "Toplevel" toplevel widget's 1st row to weight 1
                    result["toplevel"].grid_rowconfigure(
                        index=0,
                        weight=1,
                    )

                    # Add the WM_DELETE_WINDOW protocol to the toplevel widget
                    result["toplevel"].protocol(
                        name="WM_DELETE_WINDOW",
                        func=on_toplevel_destroy,
                    )

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
                    selectmode="extended",
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
                        index,
                        value,
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

            def set(value: str) -> None:
                """
                Sets the selected value in the single select field.

                Args:
                    value (str): The value to be set.

                Returns:
                    None
                """

                if value not in result["values"]:
                    # Add the value to the "values" list
                    result["values"].append(value)

                # Set the value associated with the "selection" key
                result["selection"] = [value]

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
                    text=result["selection"][0],
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
                    text="X",
                    width=3,
                    **kwargs,
                )

                # Place the "Value remove button" button widget within the "Value frame" frame widget
                result["value_remove_button"].grid(
                    column=1,
                    padx=5,
                    pady=5,
                    row=0,
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
                command=on_select_button_click,
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
        master: Optional[tkinter.Misc] = None,
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

            # Lift the "Root" toplevel widget above other windows
            result["root"].lift()

            # Ring the bell
            result["root"].bell()

            # Add the getter function to the result dictionary
            result["getter"] = get

            # Wait for the window to be closed
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
        master: Optional[tkinter.Misc] = None,
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

            def on_button_click(string: Literal["okay", "cancel"]) -> None:
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
                    if string.lower() == "cancel"
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

            # Lift the "Root" toplevel widget above other windows
            result["root"].lift()

            # Ring the bell
            result["root"].bell()

            # Add the getter function to the result dictionary
            result["getter"] = get

            # Wait for the window to be closed
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
        label: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[bool], None]] = None,
        value: bool = False,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of tkinter.Checkbutton that is used as a field.

        This method creates a dictionary that holds all functions and widgets that facilitate the checkbox field.
        Contained keys are:
            - "clearer": A function that clears the checkbox field.
            - "getter": A function that retrieves the value of the checkbox field.
            - "setter": A function that sets the value of the checkbox field.
            - "variable": A tkinter.BooleanVar instance that holds the value of the checkbox field.
            - "root": A tkinter.Frame instance that holds the checkbox field.
            - "label": A tkinter.Label instance that holds the label for the checkbox field.
            - "radiobutton": A tkinter.Checkbutton instance that is used as a field.

        Args:
            label (str): The label for the radiobutton.
            master (tkinter.Misc): The master widget.
            namespace (str): The namespace for the radiobutton. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[bool], None]]): A callback function that is called when the value of the checkbox field changes. Defaults to None.
            value (bool): The initial value of the checkbox field. Defaults to False.
            **kwargs: Any additional keyword arguments to be passed to the various tkinter widgets.

        Returns:
            Optional[Dict[str, Any]]: The created tkinter.Checkbutton instance or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Checkbutton.
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def clear(dispatch: bool = True) -> None:
                """
                Clears the radiobutton field by setting its value to False.

                Args:
                    None

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to clear the radiobutton field.
                """
                try:
                    if dispatch:
                        # Dispatch the RADIOBUTTON_FIELD_CLEARED event
                        cls.dispatcher.dispatch(
                            event=Events.RADIOBUTTON_FIELD_CLEARED,
                            label=label,
                            namespace=namespace,
                            value=False,
                        )

                    # Set the value of the radiobutton field to False
                    result["variable"].set(value=False)

                    # Update the text of the radiobutton
                    result["radiobutton"].configure(text=str(result["variable"].get()))
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'clear' method from '{cls.__name__}': {e}"
                    )

            def get(dispatch: bool = True) -> bool:
                """
                Retrieves the value of the radiobutton field as a boolean.

                Args:
                    None

                Returns:
                    bool: The value of the radiobutton field as a boolean.

                Raises:
                    Exception: If an exception occurs while attempting to retrieve the value of the radiobutton field.
                """
                try:
                    if dispatch:
                        # Dispatch the RADIOBUTTON_FIELD_GET event
                        cls.dispatcher.dispatch(
                            event=Events.RADIOBUTTON_FIELD_GET,
                            label=label,
                            namespace=namespace,
                            value=result["variable"].get(),
                        )

                    # Return the value of the radiobutton field as a boolean
                    return result["variable"].get()
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'get' method from '{cls.__name__}': {e}"
                    )

                    # Return False
                    return False

            def on_check_box_changed(dispatch: bool = True) -> None:
                """
                Handles the RADIOBUTTON_FIELD_CHANGED event.

                This function is called when the value of the radiobutton field changes.

                Args:
                    None

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to dispatch the RADIOBUTTON_FIELD_CHANGED event.
                """
                try:
                    if dispatch:
                        # Dispatch the RADIOBUTTON_FIELD_CHANGED event
                        cls.dispatcher.dispatch(
                            event=Events.RADIOBUTTON_FIELD_CHANGED,
                            label=label,
                            namespace=namespace,
                            value=result["variable"].get(),
                        )

                    # Update the text of the radiobutton
                    result["radiobutton"].configure(text=str(result["variable"].get()))

                    # Check, if the on_change_callback is present
                    if on_change_callback:
                        # Call the on_change_callback function with the new value
                        on_change_callback(result["variable"].get())
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'on_check_box_changed' method from '{cls.__name__}': {e}"
                    )

            def set(
                dispatch: bool = True,
                value: bool = False,
            ) -> None:
                """
                Sets the value of the radiobutton field.

                Args:
                    dispatch (bool, optional): Whether to dispatch the RADIOBUTTON_FIELD_SET event. Defaults to True.
                    value (bool, optional): The value to set for the radiobutton field. Defaults to False.

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to set the value of the radiobutton field.
                """
                try:
                    if dispatch:
                        # Dispatch the RADIOBUTTON_FIELD_SET event
                        cls.dispatcher.dispatch(
                            event=Events.RADIOBUTTON_FIELD_SET,
                            label=label,
                            namespace=namespace,
                            value=value,
                        )

                    # Set the value of the radiobutton field
                    result["variable"].set(value=value)

                    # Update the text of the radiobutton
                    result["radiobutton"].configure(text=str(result["variable"].get()))
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'set' method from '{cls.__name__}': {e}"
                    )

            # Create the "Variable" boolean variable
            result["variable"] = cls.get_bool_variable(value=value)

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(
                master=master,
                **kwargs.get("root", {}),
            )

            # Configure the "Root" frame widget's 0th column to weight 0
            result["root"].grid_columnconfigure(
                index=0,
                weight=0,
            )

            # Configure the "Root" frame widget's 1st column to weight 0
            result["root"].grid_columnconfigure(
                index=1,
                weight=0,
            )

            # Configure the "Root" frame widget's 0th row to weight 1
            result["root"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the "Label" label widget
            result["label"] = cls.get_label(
                master=result["root"],
                text=label,
                **kwargs.get("label", {}),
            )

            # Add the "Label" label widget to the "Root" frame widget
            result["label"].grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Create the "Checkbutton" radiobutton widget
            result["radiobutton"] = cls.get_radiobutton(
                command=on_check_box_changed,
                master=result["root"],
                text="False",
                variable=result["variable"],
                **kwargs.get("radiobutton", {}),
            )

            # Add the "Checkbutton" radiobutton widget to the "Root" frame widget
            result["radiobutton"].grid(
                column=1,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
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
                message=f"Caught an exception while attempting to run 'get_radiobutton_field' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_radiobutton_field_group(
        cls,
        labels: List[str],
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[bool], None]] = None,
        selection_mode: Literal["multiple", "single"] = "single",
        value: bool = False,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of a group of radiobutton fields.

        This method creates a frame widget and adds a radiobutton field to it for each label in the given list of labels.
        The radiobutton fields are configured to call the given on_change_callback when their value is changed.
        The method also adds a getter and setter function to the result dictionary, which can be used to get and set the value of the radiobutton fields.

        Args:
            labels (List[str]): A list of labels for the radiobutton fields.
            master (tkinter.Misc): The master widget.
            namespace (str, optional): The namespace to use for the radiobutton fields. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[bool], None]], optional): A callback function to call when the value of a radiobutton field is changed. Defaults to None.
            selection_mode (Literal["multiple", "single"], optional): The selection mode for the radiobutton fields. Defaults to "single".
            value (bool, optional): The initial value of the radiobutton fields. Defaults to False.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Checkbutton constructor.

        Returns:
            Optional[Dict[str, Any]]: A dictionary containing the created radiobutton fields, the getter and setter functions, and the clearer function.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Checkbutton.
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def clear() -> None:
                """
                Clears all the radiobutton fields.

                This method calls the "clearer" function on each radiobutton field in the "fields" dictionary.

                Returns:
                    None
                """

                # Iterate over the values in the "fields" dictionary
                for field in result["fields"].values():
                    # Call the "clearer" function on the current field
                    field["clearer"]()

            def enforce_selection_mode(
                label: str,
                value: bool,
            ) -> None:
                """
                Enforces the selection mode on the radiobutton fields.

                This method is called when the value of a radiobutton field is changed.
                It enforces the selection mode by calling the setter function on all
                other radiobutton fields with the opposite value of the one given.

                Args:
                    label (str): The label of the radiobutton field that was changed.
                    value (bool): The new value of the radiobutton field.
                """

                # Check, if the selection mode is "multiple"
                if selection_mode == "multiple":
                    # If the selection mode is "multiple", there is nothing to do
                    return

                # Iterate over the values in the "fields" dictionary
                for (
                    key,
                    field,
                ) in result["fields"].items():
                    # Check, if the current field is the one that was changed
                    if key == label:
                        # Skip the current field
                        continue

                    # Call the "setter" function on the current field
                    field["setter"](
                        dispatch=False,
                        value=not value,
                    )

                if on_change_callback:
                    # Call the on_change_callback
                    on_change_callback(value)

            def get(label: str) -> bool:
                """
                Gets the value of the radiobutton field with the given label.

                This method calls the "getter" function on the radiobutton field in the "fields" dictionary with the given label
                and returns its value.

                Args:
                    label (str): The label of the radiobutton field to get.

                Returns:
                    bool: The value of the radiobutton field with the given label.
                """

                # Check if the label is present in the "fields" dictionary
                if label not in result["fields"].keys():
                    # Return early
                    return False

                # Call the "getter" function on the current field
                return result["fields"][label]["getter"]()

            def set(
                label: str,
                value: bool = False,
            ) -> None:
                """
                Sets the value of the radiobutton field with the given label.

                This method calls the "setter" function on the radiobutton field in the "fields" dictionary with the given label
                and sets it to the given value.

                Args:
                    label (str): The label of the radiobutton field to set.
                    value (bool, optional): The value to set the radiobutton field to. Defaults to False.

                Returns:
                    None
                """

                # Check if the label is present in the "fields" dictionary
                if label not in result["fields"].keys():
                    # Return early
                    return

                # Call the "setter" function on the current field
                result["fields"][label]["setter"](value=value)

            # Initialize the "fields" dictionary as an empty dictionary
            result["fields"] = {}

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(master=master)

            # Configure the "Root" frame widget's 0th column to weight 1
            result["root"].grid_columnconfigure(
                index=0,
                weight=1,
            )

            for (
                index,
                label,
            ) in enumerate(iterable=labels):
                # Configure the "Root" frame widget's row at the current index to weight 0
                result["root"].grid_rowconfigure(
                    index=index,
                    weight=0,
                )

                # Create the check widget
                radiobutton_field: Optional[Dict[str, Any]] = cls.get_radiobutton_field(
                    label=label,
                    master=result["root"],
                    namespace=namespace,
                    on_change_callback=enforce_selection_mode,
                    value=value,
                    **kwargs.get(f"{label}_field", {}),
                )

                if not radiobutton_field:
                    # Log a warning message
                    cls.logger.warning(
                        message=f"Failed to create check widget in '{cls.__name__}'. This is likely a bug."
                    )

                    # Return early
                    return None

                # Add the check widget to the result dictionary
                result["fields"][label] = radiobutton_field

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
                message=f"Caught an exception while attempting to run 'get_radiobutton_field_group' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_readonly_field(
        cls,
        label: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str], None]] = None,
        value: str = "",
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of tkinter.Entry that is used as a field.

        This method creates a dictionary that holds all functions and widgets that facilitate the readonly field.
        Contained keys are:
            - "clearer": A function that clears the readonly field.
            - "getter": A function that retrieves the value of the readonly field.
            - "setter": A function that sets the value of the readonly field.
            - "variable": A tkinter.stringVar instance that holds the value of the readonly field.
            - "root": A tkinter.Frame instance that holds the readonly field.
            - "label": A tkinter.Label instance that holds the label for the readonly field.
            - "entry": A tkinter.Entry instance that is used as a field.

        Args:
            label (str): The label for the readonly field.
            master (tkinter.Misc): The master widget.
            namespace (str): The namespace for the readonly field. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[str], None]]): A callback function that is called when the value of the readonly field changes. Defaults to None.
            value (bool): The initial value of the readonly field. Defaults to an empty string.
            **kwargs: Any additional keyword arguments to be passed to the various tkinter widgets.

        Returns:
            Optional[Dict[str, Any]]: The created tkinter.Entry instance or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Entry.
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def clear(dispatch: bool = True) -> None:
                """
                Clears the readonly field by setting its value to an empty string.

                Args:
                    None

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to clear the readonly field.
                """
                try:
                    # Clear the tkinter.Entry widget
                    result["variable"].set(value="")

                    if dispatch:
                        # Dispatch the READONLY_FIELD_CLEARED event
                        cls.dispatcher.dispatch(
                            event=Events.READONLY_FIELD_CLEARED,
                            label=label,
                            namespace=namespace,
                            value=result["variable"].get(),
                        )
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'clear' method from '{cls.__name__}': {e}"
                    )

            def get(dispatch: bool = True) -> Optional[str]:
                """
                Retrieves the value of the readonly field as a string.

                Args:
                    None

                Returns:
                    Optional[str]: The value of the readonly field as a string. Or None if an exception occurs.

                Raises:
                    Exception: If an exception occurs while attempting to retrieve the value of the readonly field.
                """
                try:
                    if dispatch:
                        # Dispatch the READONLY_FIELD_GET event
                        cls.dispatcher.dispatch(
                            event=Events.READONLY_FIELD_GET,
                            label=label,
                            namespace=namespace,
                            value=result["variable"].get(),
                        )

                    # Return the value of the readonly field as a string
                    return result["variable"].get()
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'get' method from '{cls.__name__}': {e}"
                    )

                    # Return None indicating an exception occurred
                    return None

            def on_entry_changed(dispatch: bool = True) -> None:
                """
                Handles the SINGLE_LINE_FIELD_CHANGED event.

                This function is called when the value of the readonly field changes.

                Args:
                    None

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to dispatch the SINGLE_LINE_FIELD_CHANGED event.
                """
                try:
                    if dispatch:
                        # Dispatch the SINGLE_LINE_FIELD_CHANGED event
                        cls.dispatcher.dispatch(
                            event=Events.READONLY_FIELD_CHANGED,
                            label=label,
                            namespace=namespace,
                            value=result["variable"].get(),
                        )

                    # Check, if the on_change_callback is present
                    if on_change_callback:
                        # Call the on_change_callback function with the new value
                        on_change_callback(result["variable"].get())
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'on_entry_changed' method from '{cls.__name__}': {e}"
                    )

            def set(
                dispatch: bool = True,
                value: str = "",
            ) -> None:
                """
                Sets the value of the readonly field.

                Args:
                    dispatch (bool, optional): Whether to dispatch the SINGLE_LINE_FIELD_SET event. Defaults to True.
                    value (str, optional): The value to set for the readonly field. Defaults to an empty string.

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to set the value of the readonly field.
                """
                try:
                    if dispatch:
                        # Dispatch the SINGLE_LINE_FIELD_SET event
                        cls.dispatcher.dispatch(
                            event=Events.READONLY_FIELD_SET,
                            label=label,
                            namespace=namespace,
                            value=value,
                        )

                    # Set the value of the readonly field
                    result["variable"].set(value=value)
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'set' method from '{cls.__name__}': {e}"
                    )

            # Create the "Variable" StrVar object
            result["variable"] = cls.get_str_variable(value=value)

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(
                master=master,
                **kwargs.get("root", {}),
            )

            # Configure the "Root" frame widget's 0th column to weight 0
            result["root"].grid_columnconfigure(
                index=0,
                weight=0,
            )

            # Configure the "Root" frame widget's 1st column to weight 1
            result["root"].grid_columnconfigure(
                index=1,
                weight=1,
            )

            # Configure the "Root" frame widget's 0th row to weight 1
            result["root"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the "Label" label widget
            result["label"] = cls.get_label(
                master=result["root"],
                text=label,
                **kwargs.get("label", {}),
            )

            # Add the "Label" label widget to the "Root" frame widget
            result["label"].grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Create the "Entry" entry widget
            result["entry"] = cls.get_entry(
                master=result["root"],
                state="readonly",
                textvariable=result["variable"],
                **kwargs.get("entry", {}),
            )

            # Bind the "Entry" entry widget to the "on_entry_changed" function
            result["entry"].bind(
                func=lambda event: on_entry_changed(),
                sequence="<KeyRelease>",
            )

            # Add the "Entry" entry widget to the "Root" frame widget
            result["entry"].grid(
                column=1,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
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
                message=f"Caught an exception while attempting to run 'get_readonly_field' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_scale(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[tkinter.Scale]:
        """
        Creates and returns a new instance of tkinter.Scale.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Additional keyword arguments to be passed to the tkinter.Scale constructor.

        Returns:
            Optional[tkinter.Scale]: The created tkinter.Scale instance or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Scale.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Scale
            return tkinter.Scale(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_scale' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occurred
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

            def get() -> Optional[str]:
                """
                Gets the contents of the scrolled text widget.

                Returns:
                    str: The contents of the scrolled text widget.
                """

                # Return the contents of the text widget
                string: str = result["text"].get(
                    "1.0",
                    "end-1c",
                )

                # Check, if the text field's content is an empty string
                if string == "":
                    # Return None
                    return None

                # Return the string
                return string.strip()

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
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str], None]] = None,
        value: str = "",
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of tkinter.Entry that is used as a field.

        This method creates a dictionary that holds all functions and widgets that facilitate the single line text field.
        Contained keys are:
            - "clearer": A function that clears the single line text field.
            - "getter": A function that retrieves the value of the single line text field.
            - "setter": A function that sets the value of the single line textfield.
            - "variable": A tkinter.stringVar instance that holds the value of the single line textfield.
            - "root": A tkinter.Frame instance that holds the single line textfield.
            - "label": A tkinter.Label instance that holds the label for the single line textfield.
            - "entry": A tkinter.Entry instance that is used as a field.
            - "button": A tkinter.Button that clears the single line text field.

        Args:
            label (str): The label for the single line text field.
            master (tkinter.Misc): The master widget.
            namespace (str): The namespace for the single line text field. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[str], None]]): A callback function that is called when the value of the single line text field changes. Defaults to None.
            value (bool): The initial value of the single line text field. Defaults to an empty string.
            **kwargs: Any additional keyword arguments to be passed to the various tkinter widgets.

        Returns:
            Optional[Dict[str, Any]]: The created tkinter.Entry instance or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Entry.
        """
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def clear(dispatch: bool = True) -> None:
                """
                Clears the single line text field by setting its value to an empty string.

                Args:
                    None

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to clear the single line text field.
                """
                try:
                    # Clear the tkinter.Entry widget
                    result["entry"].delete(
                        first=0,
                        last=END,
                    )

                    if dispatch:
                        # Dispatch the SINGLE_LINE_TEXT_FIELD_CLEARED event
                        cls.dispatcher.dispatch(
                            event=Events.SINGLE_LINE_TEXT_FIELD_CLEARED,
                            label=label,
                            namespace=namespace,
                            value=result["entry"].get(),
                        )
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'clear' method from '{cls.__name__}': {e}"
                    )

            def get(dispatch: bool = True) -> Optional[str]:
                """
                Retrieves the value of the single line text field as a string.

                Args:
                    None

                Returns:
                    Optional[str]: The value of the single line text field as a string. Or None if an exception occurs.

                Raises:
                    Exception: If an exception occurs while attempting to retrieve the value of the single line text field.
                """
                try:
                    if dispatch:
                        # Dispatch the SINGLE_LINE_FIELD_GET event
                        cls.dispatcher.dispatch(
                            event=Events.SINGLE_LINE_TEXT_FIELD_GET,
                            label=label,
                            namespace=namespace,
                            value=result["entry"].get(),
                        )

                    # Return the value of the single line text field as a string
                    return result["entry"].get()
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'get' method from '{cls.__name__}': {e}"
                    )

                    # Return None indicating an exception occurred
                    return None

            def on_button_clicked() -> None:
                """
                Handles the button click.

                This function calls the clear function.

                Args:
                    None

                Returns:
                    None
                """
                try:
                    # Clear the single line text field
                    clear(dispatch=True)
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'on_button_clicked' method from '{cls.__name__}': {e}"
                    )

            def on_entry_changed(dispatch: bool = True) -> None:
                """
                Handles the SINGLE_LINE_FIELD_CHANGED event.

                This function is called when the value of the single line text field changes.

                Args:
                    None

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to dispatch the SINGLE_LINE_FIELD_CHANGED event.
                """
                try:
                    if dispatch:
                        # Dispatch the SINGLE_LINE_FIELD_CHANGED event
                        cls.dispatcher.dispatch(
                            event=Events.SINGLE_LINE_TEXT_FIELD_CHANGED,
                            label=label,
                            namespace=namespace,
                            value=result["entry"].get(),
                        )

                    # Check, if the on_change_callback is present
                    if on_change_callback:
                        # Call the on_change_callback function with the new value
                        on_change_callback(result["entry"].get())
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'on_entry_changed' method from '{cls.__name__}': {e}"
                    )

            def set(
                dispatch: bool = True,
                value: str = "",
            ) -> None:
                """
                Sets the value of the single line text field.

                Args:
                    dispatch (bool, optional): Whether to dispatch the SINGLE_LINE_FIELD_SET event. Defaults to True.
                    value (str, optional): The value to set for the single line text field. Defaults to an empty string.

                Returns:
                    None

                Raises:
                    Exception: If an exception occurs while attempting to set the value of the single line text field.
                """
                try:
                    if dispatch:
                        # Dispatch the SINGLE_LINE_FIELD_SET event
                        cls.dispatcher.dispatch(
                            event=Events.SINGLE_LINE_TEXT_FIELD_SET,
                            label=label,
                            namespace=namespace,
                            value=value,
                        )

                    # Clear the tkinter.Entry widget
                    result["entry"].delete(
                        first=0,
                        last=END,
                    )

                    # Set the value of the single line text field
                    result["entry"].insert(
                        0,
                        value,
                    )
                except Exception as e:
                    # Log an error message indicating an exception occurred
                    cls.logger.error(
                        message=f"Caught an exception while attempting to run 'set' method from '{cls.__name__}': {e}"
                    )

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(
                master=master,
                **kwargs.get("root", {}),
            )

            # Configure the "Root" frame widget's 0th column to weight 0
            result["root"].grid_columnconfigure(
                index=0,
                weight=0,
            )

            # Configure the "Root" frame widget's 1st column to weight 1
            result["root"].grid_columnconfigure(
                index=1,
                weight=1,
            )

            # Configure the "Root" frame widget's 2nd column to weight 0
            result["root"].grid_columnconfigure(
                index=2,
                weight=0,
            )

            # Configure the "Root" frame widget's 0th row to weight 1
            result["root"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the "Label" label widget
            result["label"] = cls.get_label(
                master=result["root"],
                text=label,
                **kwargs.get("label", {}),
            )

            # Add the "Label" label widget to the "Root" frame widget
            result["label"].grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Create the "Entry" entry widget
            result["entry"] = cls.get_entry(
                master=result["root"],
                **kwargs.get("entry", {}),
            )

            # Bind the "Entry" entry widget to the "on_entry_changed" function
            result["entry"].bind(
                func=lambda event: on_entry_changed(),
                sequence="<KeyRelease>",
            )

            # Add the "Entry" entry widget to the "Root" frame widget
            result["entry"].grid(
                column=1,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Create the "Button" button widget
            result["button"] = cls.get_button(
                command=on_button_clicked,
                master=result["root"],
                text="X",
                **kwargs.get("button", {}),
            )

            # Add the "Entry" entry widget to the "Root" frame widget
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
                message=f"Caught an exception while attempting to run 'get_checkbutton_field' method from '{cls.__name__}': {e}"
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

            def clear() -> None:
                """
                Clears the selected value from the single select field.

                Returns:
                    None
                """

                # Set the value associated with the "selection" key to None
                result["selection"] = None

                # Iterate over the children of the "Container" frame widget
                for child in result["container"].winfo_children():
                    # Destroy each child widget
                    child.destroy()

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
                        text="X",
                        width=3,
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

                    # Configure the "Toplevel" toplevel widget's 1st row to weight 1
                    result["toplevel"].grid_rowconfigure(
                        index=0,
                        weight=1,
                    )

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
                        index,
                        value,
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

            def set(value: str) -> None:
                """
                Sets the selected value in the single select field.

                Args:
                    value (str): The value to be set.

                Returns:
                    None
                """

                if value not in result["values"]:
                    # Add the value to the "values" list
                    result["values"].append(value)

                # Set the value associated with the "selection" key
                result["selection"] = value

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
                    text="X",
                    width=3,
                    **kwargs,
                )

                # Place the "Value remove button" button widget within the "Value frame" frame widget
                result["value_remove_button"].grid(
                    column=1,
                    padx=5,
                    pady=5,
                    row=0,
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
                padx=5,
                pady=5,
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
                column=2,
                row=0,
                sticky=NSEW,
            )

            # Add the clear function to the result dictionary
            result["clearer"] = clear

            # Add the getter function to the result dictionary
            result["getter"] = get

            # Add the set function to the result dictionary
            result["setter"] = set

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

                # Create the "{Miscellaneous.any_to_snake(string=label)}_button" button widget
                result[f"{Miscellaneous.any_to_snake(string=label)}_button"] = (
                    cls.get_button(
                        command=lambda string=label: on_button_click(string=string),
                        master=result["top_frame"],
                        text=label,
                    )
                )

                # Place the button widget within the "Top frame" frame widget
                result[f"{Miscellaneous.any_to_snake(string=label)}_button"].grid(
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
                    result[
                        f"{Miscellaneous.any_to_snake(string=label)}_button"
                    ].configure(state=DISABLED)
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
                    if f"{Miscellaneous.any_to_snake(string=string)}_button" != key:
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
            result["root"] = cls.get_frame(
                master=master,
                **kwargs,
            )

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
    def get_toast(
        cls,
        dispatcher: Dispatcher,
        message: str,
        title: str,
        master: Optional[tkinter.Misc] = None,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        try:
            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            def begin_fade(
                widget: tkinter.Misc,
                end: float = 1.0,
                interval: int = 50,
                start: float = 0.0,
                step: float = 0.05,
            ) -> None:
                if start > end:
                    start += step
                    widget.attributes(
                        "-alpha",
                        min(
                            start,
                            end,
                        ),
                    )
                    widget.after(
                        interval,
                        lambda: begin_fade(
                            end=end,
                            interval=interval,
                            step=step,
                            start=start,
                            widget=widget,
                        ),
                    )

            def end_fade(
                widget: tkinter.Misc,
                start: float = 0.0,
                end: float = 1.0,
                step: float = 0.05,
                interval: int = 50,
            ) -> None:
                if start <= end:
                    start += step
                    widget.attributes(
                        "-alpha",
                        min(
                            start,
                            end,
                        ),
                    )
                    widget.after(
                        interval,
                        lambda: end_fade(
                            end=end,
                            interval=interval,
                            start=start,
                            step=step,
                            widget=widget,
                        ),
                    )

            def show() -> None:
                """
                Makes the root widget visible by deiconifying it.

                Returns:
                    None
                """

                # Deiconify the root widget to make it visible
                result["root"].deiconify()

            def hide() -> None:
                """
                Hides the root widget by withdrawing it.

                Returns:
                    None
                """

                # Withdraw the root widget to hide it
                result["root"].withdraw()

            # Store the UUID of the toas in a variable
            result["uuid"] = Miscellaneous.get_uuid()

            # Create the "Root" toplevel widget
            result["root"] = cls.get_toplevel(master=master)

            result["root"].wm_geometry(newGeometry="100x100")

            # Configure the "Root" toplevel widget's 0th column to weight 1
            result["root"].grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the "Root" toplevel widget's 0th row to weight 0
            result["root"].grid_rowconfigure(
                index=0,
                weight=0,
            )

            # Configure the "Root" toplevel widget's 1st row to weight 1
            result["root"].grid_rowconfigure(
                index=1,
                weight=1,
            )

            # Create the "Title" label widget
            result["title"] = cls.get_label(
                master=result["root"],
                text=title,
                **kwargs,
            )

            # Bind the "<ButtonRelease-1>" (left mouse click) event to the "Title" label widget
            result["title"].bind(
                func=lambda event: dispatcher.dispatch(
                    event=Events.TOAST_CLICKED,
                    message=message,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    title=title,
                    uuid=result["uuid"],
                ),
                sequence="<ButtonRelease-1>",
            )

            # Place the "Title" label widget within the "Root" toplevel widget
            result["title"].grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the "Message" label widget
            result["message"] = cls.get_label(
                master=result["root"],
                text=message,
                **kwargs,
            )

            # Bind the "<ButtonRelease-1>" (left mouse click) event to the "Message" label widget
            result["message"].bind(
                func=lambda event: dispatcher.dispatch(
                    event=Events.TOAST_CLICKED,
                    message=message,
                    namespace=Constants.GLOBAL_NAMESPACE,
                    title=title,
                    uuid=result["uuid"],
                ),
                sequence="<ButtonRelease-1>",
            )

            # Place the "Message" label widget within the "Root" toplevel widget
            result["message"].grid(
                column=0,
                row=1,
                sticky=NSEW,
            )

            # Hide the "Root" toplevel widget
            hide()

            # Return the result dictonary
            return result
        except Exception as e:
            # Log an error message indicating an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_toast' method from '{cls.__class__.__name__}': {e}",
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
