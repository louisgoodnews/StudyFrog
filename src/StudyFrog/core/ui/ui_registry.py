"""
Author: lodego
Date: 2025-02-09
"""

import tkinter

from typing import *

from utils.constants import Constants
from utils.logger import Logger


__all__: List[str] = ["UIRegistry"]


class UIRegistry:
    """
    A class for managing a registry of user interface (UI) widgets.

    Attributes:
        registry (Dict[str, Type[tkinter.Misc]]): A dictionary mapping widget names to widget classes.
        logger (Logger): The logger instance associated with the object.
    """

    registry: Dict[str, Type[tkinter.Misc]] = {}

    logger: Logger = Logger.get_logger(name="UIRegistry")

    @classmethod
    def get(
        cls,
        name: str,
    ) -> Optional[Type[tkinter.Misc]]:
        """
        Returns the widget class registered under the given name.

        Args:
            name (str): The name of the widget.

        Returns:
            Optional[Type[tkinter.Misc]]: The widget class registered under the given name, or None if no such widget is registered.
        """

        # Attempt to return the widget class registered under the given name
        result: Optional[Type[tkinter.Misc]] = cls.registry.get(name)

        if not result:
            # Log a warning message indicating that no such widget is registered
            cls.logger.warning(message=f"No UI class registered under name '{name}'.")

            # Return None indicating that no such widget is registered
            return None

        # Return the widget class
        return result

    @classmethod
    def register(
        cls,
        name: str,
        widget: Type[tkinter.Misc],
    ) -> None:
        """
        Registers a new widget class with the UIRegistry.

        Args:
            name (str): The name of the widget.
            widget (Type[tkinter.Misc]): The widget class to register.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to register the widget.
        """
        try:
            # Check if a widget with the given name is already registered
            if name in cls.registry:
                # Log a warning message indicating that the widget will be overwritten
                cls.logger.warning(
                    message=f"Overwriting widget '{name}' with class '{type(widget).__name__}'."
                )

            # Check if the provided widget is a subclass of tkinter.Misc.
            if not issubclass(
                widget,
                tkinter.Misc,
            ):
                # Log an error message indicating that the provided widget is not a valid tkinter UI class.
                cls.logger.error(
                    message=f"Cannot register '{name}': Provided widget is not a valid tkinter UI class."
                )

                # Raise a type error indicating that the provided widget is not a valid tkinter UI class.
                raise TypeError(
                    f"Provided widget '{name}' is not a subclass of tkinter.Misc."
                )

            # Register the widget class under the given name
            cls.registry[name] = widget

            # Log an info message indicating that the widget has been registered
            cls.logger.info(
                message=f"Registered widget '{name}' with class '{type(widget).__name__}',"
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'register' method from '{cls.__name__}': {e}"
            )

            # Reraise the exception to propagate it up the call stack
            raise e

    @classmethod
    def unregister(
        cls,
        name: str,
    ) -> None:
        """
        Unregisters a widget class from the UIRegistry.

        Args:
            name (str): The name of the widget to unregister.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while attempting to unregister the widget.
        """
        try:
            # Check if the widget class is registered
            if name in cls.registry:
                # Remove the widget class from the registry
                del cls.registry[name]

                # Log an info message indicating that the widget has been unregistered
                cls.logger.info(message=f"Unregistered UI class '{name}'.")
            else:
                # Log a warning message indicating that no such widget is registered
                cls.logger.warning(
                    message=f"Cannot unregister '{name}': No such UI class registered."
                )
        except Exception as e:
            # Log an error message indicating that no such widget is registered
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'unregister' method from '{cls.__name__}': {e}"
            )

            # Reraise the exception to propagate it up the call stack
            raise e
