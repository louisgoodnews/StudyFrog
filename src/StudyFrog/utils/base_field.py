"""
Author: lodego
Date: 2025-04-05
"""

import tkinter

from tkinter.constants import *
from typing import *

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.logger import Logger


__all__: Final[List[str]] = ["BaseField"]


class BaseField(tkinter.Frame):
    """
    A base class for all field widgets.

    BaseField is a tkinter.Frame subclass that provides a common interface for all
    field widgets. It is responsible for creating and laying out the widgets, as well
    as handling events and providing a callback function for when the value of the
    field changes.

    Attributes:
        label (str): The label for the field.
        master (tkinter.Misc): The master widget.
        namespace (str): The namespace for the field. Defaults to Constants.GLOBAL_NAMESPACE.
        on_change_callback (Optional[Callable[[str, Any], None]]): The callback function to be called when the value of the field changes. Defaults to None.
        value (Optional[Any]): The initial value of the field. Defaults to None.
        **kwargs: Additional keyword arguments for the widgets.

    Methods:
        _on_change (event: Optional[tkinter.Event] = None): Raises NotImplementedError.
        clear (dispatch: bool = False): Raises NotImplementedError.
        configure_grid (): Raises NotImplementedError.
        create_widgets (label: str): Raises NotImplementedError.
        get (dispatch: bool = False): -> Tuple[str, Any]: Raises NotImplementedError.
        set (value: Any, dispatch: bool = False): Raises NotImplementedError.

    """

    def __init__(
        self,
        label: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_change_callback: Optional[Callable[[str, Any], None]] = None,
        value: Optional[Any] = None,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the BaseField class.

        Args:
            label (str): The label for the field.
            master (tkinter.Misc): The master widget.
            namespace (str, optional): The namespace for the field. Defaults to Constants.GLOBAL_NAMESPACE.
            on_change_callback (Optional[Callable[[str, Any], None]], optional): The callback function to be called when the value of the field changes. Defaults to None.
            value (Optional[Any], optional): The initial value of the field. Defaults to None.
            **kwargs: Additional keyword arguments for the widgets.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            master=master,
            **kwargs,
        )

        # Create an instance of the Logger class
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Get the singleton instance of the Dispatcher class
        self.dispatcher: Dispatcher = Dispatcher()

        # Store the display name
        self.display_name: str = label

        # Store the namespace
        self.namespace: str = namespace

        # Store the on_change_callback
        self.on_change_callback: Optional[Callable[[str, Any], None]] = (
            on_change_callback
        )

        # Configure the grid
        self.configure_grid()

        # Create the widgets
        self.create_widgets(label=label)

        # Check, if the passed value is not None
        if value is not None:
            # Set the widget's value to the passed value
            self.set(
                dispatch=False,
                value=value,
            )

    def clear(
        self,
        dispatch: bool = False,
    ) -> None:
        """
        Clears the field widget.

        This method clears the field widget by deleting its value. If the dispatch
        flag is set to True, it will also dispatch the CLEAR event.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            None
        """
        raise NotImplementedError(
            f"Subclasses of 'BaseField' must implement the 'clear' method."
        )

    def configure_grid(self) -> None:
        """
        Configures the grid of the field widget.

        This method configures the grid of the field widget by setting the
        weights of the columns and rows. It is called by the constructor of the
        BaseField class.

        Returns:
            None
        """

        raise NotImplementedError(
            f"Subclasses of 'BaseField' must implement the 'configure_grid' method."
        )

    def create_widgets(
        self,
        label: str,
        **kwargs,
    ) -> None:
        """
        Creates and configures the widgets for the field.

        This method creates and configures the widgets for the field, such as
        the label and the entry widget. It is called by the constructor of the
        BaseField class.

        Args:
            label (str): The label for the field.
            **kwargs: Additional keyword arguments for the widgets.

        Returns:
            None
        """

        raise NotImplementedError(
            f"Subclasses of 'BaseField' must implement the 'create_widgets' method."
        )

    def get(
        self,
        dispatch: bool = False,
    ) -> Tuple[str, Any]:
        """
        Retrieves the value of the field.

        This method retrieves the value of the field and returns it as a tuple
        containing the label and the value of the field. If the dispatch flag is
        set to True, it will also dispatch the corresponding event.

        Args:
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Returns:
            Tuple[str, Any]: A tuple containing the label and the value of the field.
        """
        raise NotImplementedError(
            f"Subclasses of 'BaseField' must implement the 'get' method."
        )

    def set(
        self,
        value: Any,
        dispatch: bool = False,
    ) -> None:
        """
        Sets the value of the field.

        This method sets the value of the field to the passed value. If the dispatch
        flag is set to True, it will also dispatch the SET event.

        Args:
            value (Any): The value to set for the field.
            dispatch (bool, optional): Whether to dispatch an event. Defaults to False.

        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        raise NotImplementedError(
            f"Subclasses of 'BaseField' must implement the 'set' method."
        )
