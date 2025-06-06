"""
Author: lodego
Date: 2025-04-13
"""

import tkinter

from tkinter.constants import *
from typing import *

from core.ui.frames.frames import ScrolledFrame, TabbedFrame


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

        # Initialize the field dictionary instance variable as an empty dictionary
        self._field_dict: Dict[str, Dict[str, Union[bool, tkinter.Misc]]] = {}

        # Initialize the 'is saved' bool instance variable as False
        self._is_saved: bool = False

        # Initialize this class' Logger instance as a constant instance variable
        self.logger: Final[Logger] = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed namespace string in a constant instance variable
        self.namespace: Final[str] = namespace

        # Initialize the list of subscription UUIDs as an empty list
        self.subscriptions: Final[List[str]] = []

        # Initialize the value dictionary instance variable as an empty dictionary
        self._value_dict: Dict[str, Dict[str, Optional[Any]]] = {
            "type": {
                "value": self.__class__.__name__.replace(
                    "CreateForm",
                    "",
                )
            }
        }

        # Configure the grid layout
        self.configure_grid()

        # Create the widgets
        self.create_widgets()

        # Update idletasks
        self.update_idletasks()

        # Subscribe to events
        self.subscribe_to_events()

    @property
    def field_dict(self) -> Dict[str, Any]:
        """
        Returns a the registered field dictionary.

        This property exposes a deep the internal field registration dictionary `_field_dict`.
        Each entry maps a normalized label (snake_case) to a dictionary that contains the actual widget
        and a flag indicating whether the field is required.

        Returns:
            Dict[str, Any]: A dictionary of registered fields with their widget and required status.
        """

        # Return a the field dictionary to the caller
        return self._field_dict

    @property
    def is_saved(self) -> bool:
        """
        Returns the 'is saved' bool instance variable.

        Returns:
            bool: The 'is saved' bool instance variable.
        """

        # Return the 'is saved' bool instance variable to the caller
        return self._is_saved

    @is_saved.setter
    def is_saved(
        self,
        value: bool,
    ) -> None:
        """
        Sets the 'is saved' bool instance variable.

        Args:
            value (bool): The new value for the 'is saved' bool instance variable.

        Returns:
            None
        """

        # Set the 'is saved' bool instance variable to the passed value
        self._is_saved = value

    @property
    def value_dict(self) -> Dict[str, Any]:
        """
        Returns a the current value dictionary.

        This property exposes a deep the `_value_dict`, which holds the current values of all
        registered fields. Each key corresponds to a normalized label and maps to a dictionary with a
        "value" key storing the current input.

        Returns:
            Dict[str, Any]: A dictionary mapping normalized labels to their current field values.
        """

        # Return a the value dictionary to the caller
        return self._value_dict

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

        # Check, if the passed label contains ':'
        if ":" in label:
            # Remove the ':' and update the passed label
            label = label.replace(":", "")

        # Check, if the passed label contains '*'
        if "*" in label:
            # Remove the '*' and update the passed label
            label = label.replace("*", "")

        # Convert the passed label string to snake case
        label = Miscellaneous.any_to_snake(string=label)

        # Check, if the passed label is not already contained in the value dictionary instance variable
        if label not in self._value_dict.keys():
            # Add an empty dictionary to the value dictionary instance variable under the passed label
            self._value_dict[label] = {"value": None}

        # Add the passed value to the value dictionary instance variable under the passed label
        self._value_dict[label]["value"] = (
            value if not isinstance(value, (list, set, tuple)) else value[0]
        )

        # Update the 'is saved' bool instance variable
        self._is_saved = False

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
        if label in self._field_dict.keys():
            # Log a warning message
            self.logger.warning(
                message=f"'{label}' '{field.__class__.__name__}' instance already registered in field dict. Aborting..."
            )

            # Return early
            return

        # Add the passed field widget and bool flag to the field dictionary instance variable under the passed label
        self._field_dict[label] = {
            "required": required,
            "widget": field,
        }

    def check_save(self) -> bool:
        """
        Checks if the form has already been saved.

        Args:
            None

        Returns:
            bool: True if the form has already been saved, False otherwise.
        """

        # Return the 'is saved' bool instance variable to the caller
        return self._is_saved

    def clear(
        self,
        exclude: Optional[List[str]] = None,
    ) -> None:
        """
        Clears all registered field values.

        This method resets all field widgets to their default state and clears the internal value dictionary.

        Args:
            exclude (list, optional): An optional list of fields to exclude. Defaults to None

        Returns:
            None
        """

        # Iterate over the registered labels and field widgets
        for (
            label,
            field,
        ) in self._field_dict.items():
            # Check, if the current label is contained within the exclude list (if it exists)
            if exclude and label in exclude:
                # Skip the current iterartion
                continue

            # Call the field widget's 'clear' function
            field["widget"].clear(dispatch=False)

        # Iterate over the keys in the value dictionary instance variable
        for key in self._value_dict.keys():
            # Check, if the current key is contained within the exclude list (if it exists)
            if exclude and key in exclude:
                # Skip the current iterartion
                continue

            # Set the value associated to the current key from the value dictionary instance variable to None
            self._value_dict[key] = {"value": None}

        # Update the 'is saved' bool instance variable
        self._is_saved = True

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
            background=Constants.BLUE_GREY["700"],
            master=master,
        )

        # Configure the weight of the 0th column of the TabbedFrame widget's container to 1
        tabbed_frame.container.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the weight of the 0th row of the TabbedFrame widget's container to 1
        tabbed_frame.container.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Place the TabbedFrame widget in the grid
        tabbed_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create the 'primary attributes' ScrolledFrame widget
        primary_attributes_scrolled_frame: ScrolledFrame = ScrolledFrame(
            background=Constants.BLUE_GREY["700"],
            master=tabbed_frame.container,
        )

        # Create the 'primary attributes' widgets
        self.create_primary_attribute_widgets(
            master=primary_attributes_scrolled_frame.container
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
            background=Constants.BLUE_GREY["700"],
            master=tabbed_frame.container,
        )

        # Create the 'secondary attributes' widgets
        self.create_secondary_attribute_widgets(
            master=secondary_attributes_scrolled_frame.container
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

    def create_primary_attribute_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """
        Abstract method to create widgets for primary attributes.

        This method must be implemented by subclasses to define which widgets appear in the 'Primary Attributes' tab.

        Args:
            master (tkinter.Frame): The container in which to create widgets.

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
        master: tkinter.Frame,
    ) -> None:
        """
        Abstract method to create widgets for secondary attributes.

        This method must be implemented by subclasses to define which widgets appear in the 'Secondary Attributes' tab.

        Args:
            master (tkinter.Frame): The container in which to create widgets.

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
        instruction_label: tkinter.Label = tkinter.Label(
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
        top_frame: tkinter.Frame = tkinter.Frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        # Place the 'top frame' tkinter.Frame widget in the grid
        top_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create the 'top frame' widgets
        self.create_top_frame_widgets(master=top_frame)

        # Create the 'center frame' tkinter.Frame widget
        center_frame: tkinter.Frame = tkinter.Frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        # Place the 'center frame' tkinter.Frame widget in the grid
        center_frame.grid(
            column=0,
            row=1,
            sticky=NSEW,
        )

        # Create the 'center frame' widgets
        self.create_center_frame_widgets(master=center_frame)

    @override
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

        # Update the value dictionary instance variable
        for (
            key,
            value,
        ) in self.field_dict.items():
            self.value_dict[key.replace(":", "").replace("*", "")] = {
                "type": type(value["widget"].get()[1]),
                "value": value["widget"].get()[1],
            }

        # Return a the value dictionary to the caller
        return self._value_dict

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
        if label not in self._field_dict.keys():
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

    def update_save(
        self,
        value: bool,
    ) -> None:
        """
        Updates the 'is saved' bool instance variable.

        Args:
            value (bool): The new value for the 'is saved' bool instance variable.

        Returns:
            None
        """

        # Set the 'is saved' bool instance variable to the passed value
        self.is_saved = value

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
        result: Dict[str, bool] = {
            "fields": {},
            "result": False,
        }

        # Iterate over the field dictionary instance variable's items
        for (
            key,
            value,
        ) in self._field_dict.items():
            # Check, if the current value is not marked as required
            if not value["required"]:
                # Continue with the next iteration
                continue

            # Check, if the key is contained within the value dictionary instance variable
            if key not in self._value_dict:
                # Add a dictionary value: None to the value dictionary instance variable
                self._value_dict[key] = {"value": None}

            # Add True to the result dictionary if the required field is not empty otherwise False
            result["fields"][key] = (
                True if self._value_dict[key]["value"] is not None else False
            )

        # Update the 'result' key's value
        result["result"] = all(result["fields"].values())

        # Check, if any required fields are missing
        if not result["result"]:
            # Log a warning message
            self.logger.warning(
                message=f"Required fields ({", ".join([key for key, value, in result["fields"].items() if not value])}) are missing"
            )

        # Return the result dictionary
        return result
