"""
Author: lodego
Date: 2025-04-13
"""

import copy
import tkinter

from tkinter.constants import *
from typing import *

from core.ui.frames.frames import ScrolledFrame, TabbedFrame
from core.ui.ui_builder import UIBuilder

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous


__all__: Final[List[str]] = ["BaseCreateForm"]


class BaseCreateForm(tkinter.Frame):
    """
    A base class for form based entity creation in the StudyFrog application.

    This class provides a reusable foundation for building UI forms consisting of labeled fields.
    It manages widget registration, value tracking, and validation logic. It also separates
    primary and secondary attribute sections and supports custom layout logic.

    Attributes:
        logger (Logger): This class' Logger instance.
        dispatcher (Dispatcher): The Dispatcher instance used for event communication.
        field_dict (dict): A dictionary in which fields are registered.
        namespace (str): The namespace to dispatch events with.
        value_dict(dict): A dictionary in which the form's value is being tracked.
    """

    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        namespace: str,
    ) -> None:
        """
        Initializes a new instance of the BaseCreateForm class.

        Args:
            dispatcher (Dispatcher): The Dispatcher instance used for event communication.
            master (tkinter.Misc): The parent widget for this frame.
            namespace (str): The namespace to dispatch events with.

        Returns:
            None
        """

        # Call the parent class constructor with the passed master widget
        super().__init__(master=master)

        # Store the passed Dispatcher instance in a constant instance variable
        self.dispatcher: Final[Dispatcher] = dispatcher

        # Initialize this class' Logger instance as a constant instance variable
        self.logger: Final[Logger] = Logger.get_logger(name=self.__class__.__name__)

        # Initialize the field dictionary instance variable as an empty dictionary
        self._field_dict: Dict[str, Dict[str, Union[bool, tkinter.Misc]]] = {}

        # Store the passed namespace string in a constant instance variable
        self.namespace: Final[str] = namespace

        # Initialize the list of subscription UUIDs as an empty list
        self.subscriptions: Final[List[str]] = []

        # Initialize the value dictionary instance variable as an empty dictionary
        self._value_dict: Dict[str, Dict[str, Optional[Any]]] = {}

        # Configure the grid layout
        self.configure_grid()

        # Create the widgets
        self.create_widgets()

        # Subscribe to events
        self.subscribe_to_events()

    @property
    def field_dict(self) -> Dict[str, Any]:
        """
        Returns a copy of the registered field dictionary.

        This property exposes a deep copy of the internal field registration dictionary `_field_dict`.
        Each entry maps a normalized label (snake_case) to a dictionary that contains the actual widget
        and a flag indicating whether the field is required.

        Returns:
            Dict[str, Any]: A dictionary of registered fields with their widget and required status.
        """

        # Return a copy of the field dictionary to the caller
        return copy.deepcopy(self._field_dict)

    @property
    def value_dict(self) -> Dict[str, Any]:
        """
        Returns a copy of the current value dictionary.

        This property exposes a deep copy of the `_value_dict`, which holds the current values of all
        registered fields. Each key corresponds to a normalized label and maps to a dictionary with a
        "value" key storing the current input.

        Returns:
            Dict[str, Any]: A dictionary mapping normalized labels to their current field values.
        """

        # Return a copy of the value dictionary to the caller
        return copy.deepcopy(self._value_dict)

    def _on_field_change(
        self,
        label: str,
        value: Any,
    ) -> None:
        """
        Handles updates to a field's value within the form.

        This method is triggered whenever a field's value changes. It normalizes the label
        (removes suffixes like ': ' and '*: ', converts it to snake_case) and stores the
        new value in the internal `value_dict`. Additionally, it dispatches a
        `CREATE_FORM_FIELD_CHANGED` event through the dispatcher for external observers.

        Args:
            label (str): The label of the changed field.
            value (Any): The new value of the field.

        Returns:
            None
        """

        # Check, if the passed label ends with ': '
        if label.endswith(": "):
            # Remove the ': ' suffix and update the passed label
            label = label.replace(": ", "")

        # Check, if the passed label ends with ': '
        elif label.endswith("*: "):
            # Remove the '*: ' suffix and update the passed label
            label = label.replace("*: ", "")

        # Convert the passed label string to snake case
        label = Miscellaneous.any_to_snake(string=label)

        # Check, if the passed label is not already contained in the value dictionary instance variable
        if label not in set(self._value_dict.keys()):
            # Add an empty dictionary to the value dictionary instance variable under the passed label
            self._value_dict[label] = {"value": None}

        # Add the passed value to the value dictionary instance variable under the passed label
        self._value_dict[label]["value"] = value

        # Log the update for debugging purposes
        self.logger.debug(
            message=f"Field changed - Label: '{label}' | Normalized Key: '{label}' | Value: {value}"
        )

        # Dispatch the CREATE_FORM_FIELD_CHANGED event
        self.dispatcher.dispatch(
            event=Events.CREATE_FORM_FIELD_CHANGED,
            label=label,
            namespace=self.namespace,
            value=value,
        )

    def _register_field(
        self,
        label: str,
        field: tkinter.Misc,
        required: bool = False,
    ) -> None:
        """
        Registers a new field widget.

        This method stores the field reference along with whether it is required. Labels are
        normalized to snake_case and stripped of trailing colons.

        Args:
            label (str): The label to identify the field (normalized to snake_case).
            field (tkinter.Misc): The field widget instance.
            required (bool): Whether the field is required for form validation.

        Returns:
            None
        """

        # Check, if the passed label contains ':'
        if ":" in label:
            # Remove the ':' and update the passed label
            label = label.replace(":", "")

        # Check, if the passed label contains '*'
        if "*" in label:
            # Remove the '*' and update the passed label
            label = label.replace("*", "")

        # Convert the passed label string to snake case
        label = Miscellaneous.any_to_snake(string=label.strip())

        # Check, if the passed label is already contained in the field dictionary instance variable
        if label in set(self._field_dict.keys()):
            # Log a warning message
            self.logger.warning(
                message=f"'{label}' '{field.__class__.__name__}' instance already registered in field dict. Aborting..."
            )

            # Return early
            return

        # Log the registration for debugging
        self.logger.debug(
            message=f"Registered field - Key: '{label}' | Field Type: {type(field).__name__}"
        )

        # Add the passed field widget and bool flag to the field dictionary instance variable under the passed label
        self._field_dict[label] = {
            "required": required,
            "widget": field,
        }

    def clear(self) -> None:
        """
        Clears all registered field values.

        This method resets all field widgets to their default state and clears the internal value dictionary.

        Args:
            None

        Returns:
            None
        """

        # Iterate over the registered field widgets
        for field in set(self._field_dict.values()):
            # Call the field widget's 'clear' function
            field["widget"].clear(dispatch=False)

        # Clear the value dictionary instance variable
        self._value_dict.clear()

    def collect_subscriptions(self) -> List[Dict[str, Any]]:
        """
        Collects and returns a list of subscriptions.

        This method creates an empty list of dictionaries containing event subscription configurations.
        This method should be implemented in any subclasses, that should handle events.

        Returns:
            List[Dict[str, Any]]: A list representing the subscriptions for events.
        """

        # Initialize the list of subscriptions as an empty list
        subscriptions: List[Dict[str, Any]] = []

        # Return the list to the caller
        return subscriptions

    def configure_grid(self) -> None:
        """
        Configures the grid layout for the form.

        This sets the resizing behavior of the outer frame to allow a top and center frame layout.

        Args:
            None

        Returns:
            None
        """

        # Configure the weight of the 0th column to 1
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the weight of the 0th row to 0
        self.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the weight of the 1st row to 1
        self.grid_rowconfigure(
            index=1,
            weight=1,
        )

    def create_center_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """
        Creates the main content area with a tabbed layout.

        This method sets up two scrollable tab views: one for primary and one for secondary attributes.
        It also delegates the creation of specific widgets to child class implementations.

        Args:
            master (tkinter.Frame): The container frame into which the tabbed content is placed.

        Returns:
            None
        """

        # Configure the weight of the 0th column to 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the weight of the 0th row to 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create a TabbedFrame widget and place it in the grid
        tabbed_frame: TabbedFrame = TabbedFrame(
            column=0,
            master=master,
            row=0,
        )

        # Style the TabbedFrame widget
        tabbed_frame.configure(background=Constants.BLUE_GREY["700"])

        # Style the TabbedFrame widget's 'container frame' tkinter.Frame widget
        tabbed_frame.configure_container_frame(background=Constants.BLUE_GREY["700"])

        # Style the TabbedFrame widget's 'top frame' tkinter.Frame widget
        tabbed_frame.configure_top_frame(background=Constants.BLUE_GREY["700"])

        # Create the 'primary attributes' ScrolledFrame widget
        primary_attributes_scrolled_frame: ScrolledFrame = ScrolledFrame(
            master=tabbed_frame
        )

        # Create the 'primary attributes' ScrolledFrame widget
        primary_attributes_scrolled_frame.configure(
            background=Constants.BLUE_GREY["700"]
        )

        # Style the 'primary attributes' ScrolledFrame widget's tkinter.Canvas widget
        primary_attributes_scrolled_frame.configure_canvas(
            background=Constants.BLUE_GREY["700"]
        )

        # Style the 'primary attributes' ScrolledFrame widget's 'container frame'
        primary_attributes_scrolled_frame.configure_container(
            background=Constants.BLUE_GREY["700"]
        )

        # Add the 'primary attributes' ScrolledFrame widget to the TabbedFrame widget
        tabbed_frame.add(
            label="Primary Attributes",
            widget=primary_attributes_scrolled_frame,
        )

        # Style the TabbedFrame widget's 'Primary Attributes' button
        tabbed_frame.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            name="Primary Attributes",
            relief=FLAT,
        )

        # Create the 'secondary attributes' ScrolledFrame widget
        secondary_attributes_scrolled_frame: ScrolledFrame = ScrolledFrame(
            master=tabbed_frame
        )

        # Style the 'secondary attributes' ScrolledFrame widget
        secondary_attributes_scrolled_frame.configure(
            background=Constants.BLUE_GREY["700"]
        )

        # Style the 'secondary attributes' ScrolledFrame widget's tkinter.Canvas widget
        secondary_attributes_scrolled_frame.configure_canvas(
            background=Constants.BLUE_GREY["700"]
        )

        # Style the 'secondary attributes' ScrolledFrame widget's 'container frame'
        secondary_attributes_scrolled_frame.configure_container(
            background=Constants.BLUE_GREY["700"]
        )

        # Add the 'secondary attributes' ScrolledFrame widget to the TabbedFrame widget
        tabbed_frame.add(
            label="Secondary Attributes",
            widget=secondary_attributes_scrolled_frame,
        )

        # Style the TabbedFrame widget's 'Secondary Attributes' button
        tabbed_frame.configure_button(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            name="Secondary Attributes",
            relief=FLAT,
        )

        # Create the 'primary attributes' widgets
        self.create_primary_attribute_widgets(
            master=primary_attributes_scrolled_frame.container
        )

        # Create the 'secondary attributes' widgets
        self.create_secondary_attribute_widgets(
            master=secondary_attributes_scrolled_frame.container
        )

    def create_primary_attribute_widgets(
        self,
        master: ScrolledFrame,
    ) -> None:
        """
        Abstract method to create widgets for primary attributes.

        This method must be implemented by subclasses to define which widgets appear in the 'Primary Attributes' tab.

        Args:
            master (ScrolledFrame): The container in which to create widgets.

        Returns:
            None

        Raises:
            NotImplementedError: Raises a NotImplementedError if the method is not implemented in the subclass.
        """

        # Raise a NotImplementedError as subclasses of the BaseCreateForm class must implement the 'create_primary_attribute_widgets' method
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement the 'create_primary_attribute_widgets' method."
        )

    def create_secondary_attribute_widgets(
        self,
        master: ScrolledFrame,
    ) -> None:
        """
        Abstract method to create widgets for secondary attributes.

        This method must be implemented by subclasses to define which widgets appear in the 'Secondary Attributes' tab.

        Args:
            master (ScrolledFrame): The container in which to create widgets.

        Returns:
            None

        Raises:
            NotImplementedError: Raises a NotImplementedError if the method is not implemented in the subclass.
        """

        # Raise a NotImplementedError as subclasses of the BaseCreateForm class must implement the 'create_secondary_attribute_widgets' method
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement the 'create_secondary_attribute_widgets' method."
        )

    def create_top_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """
        Creates a top instruction bar for the form.

        This typically contains a single label for static user instructions or context information.

        Args:
            master (tkinter.Frame): The top portion of the layout in which to place the label.

        Returns:
            None
        """

        # Configure the weight of the 0th column to 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the weight of the 0th row to 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create an instruction string to be passed to the instruction label
        instruction: str = (
            "Fields marked with an asterisk (*) are required and must be filled."
        )

        # Create the 'instruction label' tkinter.Label widget
        instruction_label: tkinter.Label = UIBuilder.get_label(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=master,
            text=instruction,
        )

        # Place the 'instruction label' tkinter.Label widget in the grid
        instruction_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

    def create_widgets(self) -> None:
        """
        Creates the top and center frames and populates them with their respective widgets.

        This is the main entry point for setting up the visual structure of the form.

        Args:
            None

        Returns:
            None
        """

        # Create the 'top frame' tkinter.Frame widget
        top_frame: tkinter.Frame = UIBuilder.get_frame(
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
        center_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        # Place the 'center frame' tkinter.Frame widget in the grid
        center_frame.grid(
            column=0,
            row=1,
            sticky=NSEW,
        )

        # Create the 'top frame' widgets
        self.create_top_frame_widgets(master=top_frame)

        # Create the 'center frame' widgets
        self.create_center_frame_widgets(master=center_frame)

    def destroy(self) -> None:
        """
        Cleans up resources and unsubscribes from events.

        This method attempts to unsubscribe from all events
        and calls the parent class's destroy method to clean
        up resources. Logs any exceptions that occur.

        Returns:
            None

        Raises:
            Exception: If an error occurs during the destroy process.
        """
        try:
            # Attempt to unsubscribe from all events
            self.unsubscribe_from_events()

            # Log an info message
            self.logger.info(
                message=f"Unsubscribed from all events. Destroying '{self.__class__.__name__}' instance..."
            )

            # Call the parent class's destroy method
            super().destroy()
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'destroy' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def get(self) -> Dict[str, Any]:
        """
        Returns the current values of the form.

        Args:
            None

        Returns:
            Dict[str, Any]: A dictionary containing all field values by normalized label.
        """

        # Return a copy of the value dictionary to the caller
        return {
            Miscellaneous.any_to_snake(string=key): self.field_dict[key]
            for key in sorted(self.field_dict.keys())
        }

    def set(
        self,
        label: str,
        value: Any,
    ) -> None:
        """
        Sets the value of a registered field.

        Args:
            label (str): The normalized label of the field.
            value (Any): The value to assign to the field.

        Returns:
            None
        """

        # Check, if the passed label is already contained in the field dictionary instance variable
        if label not in set(self._field_dict.keys()):
            # Log a warning message
            self.logger.warning(
                message=f"'{label}' field is not registered in field dict. Aborting..."
            )

            # Return early
            return

        # Update the field widget at the passed label with the passed value
        self._field_dict[label]["widget"].set(value=value)

        # Update the value at the passed label with the passed value
        self._value_dict[label]["value"] = value

    def subscribe_to_events(self) -> None:
        """
        Subscribes to all events in the subscriptions dictionary.

        This method iterates over the events and functions in the subscriptions
        dictionary and registers them with the dispatcher. It also stores the
        UUIDs of the subscriptions in the subscriptions list.

        Returns:
            None

        Raises:
            Exception: If an error occurs while subscribing to events.
        """
        try:
            # Create a dictionary of events and functions
            subscriptions: List[Dict[str, Any]] = self.collect_subscriptions()

            # Iterate over the events and functions in the subscriptions dictionary
            for subscription in subscriptions:
                # Store the UUID of the subscription in the subscriptions list
                self.subscriptions.append(
                    self.dispatcher.register(
                        event=subscription["event"],
                        function=subscription["function"],
                        namespace=subscription["namespace"],
                        persistent=subscription["persistent"],
                    )
                )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'subscribe_to_events' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def unsubscribe_from_events(self) -> None:
        """
        Unsubscribes from all events subscribed in the edit UI.

        This method iterates over the UUIDs in the subscriptions dictionary and
        unregisters the event handlers associated with each UUID.

        Returns:
            None

        Raises:
            Exception: If an error occurs while unsubscribing from events.
        """
        try:
            # Iterate over the UUIDs in the subscriptions dictionary
            for uuid in self.subscriptions:
                # Unregister the handler for the given UUID
                self.dispatcher.unregister(uuid=uuid)
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'unsubscribe_from_events' method from '{self.__class__.__name__}': {e}",
            )

            # Re-raise the exception to the caller
            raise e

    def validate_form(self) -> Dict[str, Any]:
        """
        Validates the form for required fields.

        Checks whether all fields marked as required have non-None values.

        Args:
            None

        Returns:
            Dict[str, Any]: A dictionary with validation results for each field and a "result" boolean.
        """

        # Initialize the result dictionary as an empty dictionary
        result: Dict[str, bool] = {"result": False}

        # Iterate over the field dictionary instance variable's items
        for (
            key,
            value,
        ) in self._field_dict.items():
            # Check, if the current value is not marked as required
            if not value["required"]:
                # Continue with the next iteration
                continue

            # Add True to the result dictionary if the required field is not empty otherwise False
            result[key] = True if self._value_dict[key]["value"] is not None else False

        # Update the 'result' key's value
        result["result"] = all(set(result.values()))

        # Check, if any required fields are missing
        if not result["result"]:
            # Log a warning message
            self.logger.warning(
                message=f"Required fields ({", ".join(set([key for key, value, in result.items() if not value]))}) are missing"
            )

        # Return the result dictionary
        return result
