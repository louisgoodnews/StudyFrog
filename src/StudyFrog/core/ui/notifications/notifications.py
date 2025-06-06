"""
Author: lodego
Date 2025-04-11
"""

import tkinter
import traceback

from enum import Enum
from tkinter.constants import *
from typing import *

from utils.logger import Logger


__all__: Final[List[str]] = [
    "ToplevelPositions",
    "ToplevelNotification",
    "ToplevelToastNotification",
]


class ToplevelPositions(Enum):
    """ """

    BOTTOM_LEFT: Literal["bottom_left"] = "bottom_left"
    BOTTOM_RIGHT: Literal["bottom_right"] = "bottom_right"
    CENTER: Literal["center"] = "center"
    TOP_LEFT: Literal["top_left"] = "top_left"
    TOP_RIGHT: Literal["top_right"] = "top_right"


class ToplevelNotification:
    """ """

    # Initialize this class' logger instance in a class variable
    logger: Final[Logger] = Logger.get_logger(name="ToplevelNotification")

    @classmethod
    def cancel(
        cls,
        message: str,
        title: str,
        on_click_callback: Optional[Callable[[str], None]] = None,
        **kwargs,
    ) -> Optional[str]:
        """
        Creates a toplevel widget with a cancel button.

        This method creates a toplevel widget with a cancel button and a message label.
        It also sets up the geometry of the widget and places the widgets within the grid.

        Args:
            message (str): The message to display in the message label
            title (str): The title of the toplevel widget
            on_click_callback (Optional[Callable[[str], None]]): The callback to execute when the cancel button is clicked
            **kwargs: Any
                Additional keyword arguments to pass to the tkinter.Toplevel constructor

        Returns:
            Optional[str]: The result of the callback function
        """
        try:
            # Initialize the result variable as 'cancel'
            result: str = "cancel"

            # Create a toplevel widget
            toplevel: tkinter.Toplevel = tkinter.Toplevel(
                **kwargs.get(
                    "toplevel",
                    {},
                )
            )

            # Set the window title
            toplevel.wm_title(string=title)

            # Set the weight of the 0th column to 1
            # This means that the column will stretch when the window is resized
            toplevel.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Set the weight of the 0th row to 0
            # This means that the row will not stretch when the window is resized
            toplevel.grid_rowconfigure(
                index=0,
                weight=0,
            )

            # Set the weight of the 1st row to 1
            # This means that the row will stretch when the window is resized
            toplevel.grid_rowconfigure(
                index=1,
                weight=1,
            )

            # Set the weight of the 2nd row to 0
            # This means that the row will not stretch when the window is resized
            toplevel.grid_rowconfigure(
                index=2,
                weight=0,
            )

            # Create the 'title label' label widget
            title_label: tkinter.Label = tkinter.Label(
                master=toplevel,
                text=title,
                **kwargs.get(
                    "title_label",
                    {},
                ),
            )

            # Place the label widget within the grid
            title_label.grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the 'message label' label widget
            message_label: tkinter.Label = tkinter.Label(
                master=toplevel,
                text=message,
                **kwargs.get(
                    "message_label",
                    {},
                ),
            )

            # Place the label widget within the grid
            message_label.grid(
                column=0,
                row=1,
                sticky=NSEW,
            )

            def _on_button_click(string: str) -> None:
                """
                Handles the button click event.

                This method is called when the button is clicked. It sets the result variable to the passed string and calls the on_click_callback callable if it is not None.
                Finally, it destroys the toplevel widget.

                Args:
                    string (str): The string to set the result variable to

                Returns:
                    None
                """

                # Declare a nonlocal variable
                nonlocal result

                # Set the result variable to 'cancel'
                result = string

                # Check, if the on_click_callback callable has been passed
                if on_click_callback:
                    # Call the on_click_callback callable
                    on_click_callback("cancel")

                # Destroy the toplevel widget
                toplevel.destroy()

            # Create a button widget
            button: tkinter.Button = tkinter.Button(
                command=lambda: _on_button_click(string="cancel"),
                master=toplevel,
                text="Cancel",
                **kwargs.get(
                    "cancel_button",
                    {},
                ),
            )

            # Place the button widget within the grid
            button.grid(
                column=0,
                padx=5,
                pady=5,
                row=2,
            )

            # Wait until the toplevel widget is destroyed
            toplevel.wait_window()

            # Return the result string
            return result
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'cancel' method from '{cls.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            cls.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    @classmethod
    def okay(
        cls,
        title: str,
        message: str,
        on_click_callback: Optional[Callable[[str], None]] = None,
        **kwargs,
    ) -> Optional[str]:
        """
        Creates a toplevel widget with an okay button.

        This method creates a toplevel widget with an okay button and a message label.
        It also sets up the geometry of the widget and places the widgets within the grid.

        Args:
            title (str): The title of the toplevel widget
            message (str): The message to display in the message label
            on_click_callback (Optional[Callable[[str], None]]): The callback to execute when the okay button is clicked
            **kwargs: Any
                Additional keyword arguments to pass to the tkinter.Toplevel constructor

        Returns:
            Optional[str]: The result of the callback function
        """
        try:
            # Initialize the result variable as 'okay'
            result: str = "okay"

            # Create a toplevel widget
            toplevel: tkinter.Toplevel = tkinter.Toplevel(
                **kwargs.get(
                    "toplevel",
                    {},
                )
            )

            # Set the window title
            toplevel.wm_title(string=title)

            # Set the weight of the 0th column to 1
            # This means that the column will stretch when the window is resized
            toplevel.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Set the weight of the 0th row to 0
            # This means that the row will not stretch when the window is resized
            toplevel.grid_rowconfigure(
                index=0,
                weight=0,
            )

            # Set the weight of the 1st row to 1
            # This means that the row will stretch when the window is resized
            toplevel.grid_rowconfigure(
                index=1,
                weight=1,
            )

            # Set the weight of the 2nd row to 0
            # This means that the row will not stretch when the window is resized
            toplevel.grid_rowconfigure(
                index=2,
                weight=0,
            )

            # Create the 'title label' label widget
            title_label: tkinter.Label = tkinter.Label(
                master=toplevel,
                text=title,
                **kwargs.get(
                    "title_label",
                    {},
                ),
            )

            # Place the label widget within the grid
            title_label.grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the 'message label' label widget
            message_label: tkinter.Label = tkinter.Label(
                master=toplevel,
                text=message,
                **kwargs.get(
                    "message_label",
                    {},
                ),
            )

            # Place the label widget within the grid
            message_label.grid(
                column=0,
                row=1,
                sticky=NSEW,
            )

            def _on_button_click(string: str) -> None:
                """
                Handles the button click event.

                This method is called when the button is clicked. It sets the result variable to the passed string and calls the on_click_callback callable if it is not None.
                Finally, it destroys the toplevel widget.

                Args:
                    string (str): The string to set the result variable to

                Returns:
                    None
                """

                # Declare a non-local variable
                nonlocal result

                # Update the result variable with the passed string argument
                result = string

                # Check, if the on_click_callback callable has been passed
                if on_click_callback:
                    # Call the on_click_callback callable
                    on_click_callback("okay")

                # Destroy the toplevel widget
                toplevel.destroy()

            # Create a button widget
            button: tkinter.Button = tkinter.Button(
                command=lambda: _on_button_click(string="okay"),
                master=toplevel,
                text="Okay",
                **kwargs.get(
                    "okay_button",
                    {},
                ),
            )

            # Place the button widget within the grid
            button.grid(
                column=0,
                padx=5,
                pady=5,
                row=2,
            )

            # Wait until the toplevel widget is destroyed
            toplevel.wait_window()

            # Return the result string
            return result
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'okay' method from '{cls.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            cls.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    @classmethod
    def okay_cancel(
        cls,
        title: str,
        message: str,
        on_click_callback: Optional[Callable[[str], None]] = None,
        **kwargs,
    ) -> Optional[str]:
        """
        Creates a toplevel widget with an okay and cancel button.

        This method creates a toplevel widget with an okay and cancel button and a message label.
        It also sets up the geometry of the widget and places the widgets within the grid.

        Args:
            title (str): The title of the toplevel widget
            message (str): The message to display in the message label
            on_click_callback (Optional[Callable[[str], None]]): The callback to execute when the okay or cancel button is clicked
            **kwargs: Any
                Additional keyword arguments to pass to the tkinter.Toplevel constructor

        Returns:
            Optional[str]: The result of the callback function
        """
        try:
            # Initialize the result variable as 'cancel'
            result: str = "cancel"

            # Create a toplevel widget
            toplevel: tkinter.Toplevel = tkinter.Toplevel(
                **kwargs.get(
                    "toplevel",
                    {},
                )
            )

            # Set the window title
            toplevel.wm_title(string=title)

            # Set the weight of the 0th column to 1
            # This means that the column will stretch when the window is resized
            toplevel.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Set the weight of the 0th row to 0
            # This means that the row will not stretch when the window is resized
            toplevel.grid_rowconfigure(
                index=0,
                weight=0,
            )

            # Set the weight of the 1st row to 1
            # This means that the row will stretch when the window is resized
            toplevel.grid_rowconfigure(
                index=1,
                weight=1,
            )

            # Set the weight of the 2nd row to 0
            # This means that the row will not stretch when the window is resized
            toplevel.grid_rowconfigure(
                index=2,
                weight=0,
            )

            # Create the 'title label' label widget
            title_label: tkinter.Label = tkinter.Label(
                master=toplevel,
                text=title,
                **kwargs.get(
                    "title_label",
                    {},
                ),
            )

            # Place the label widget within the grid
            title_label.grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the 'message label' label widget
            message_label: tkinter.Label = tkinter.Label(
                master=toplevel,
                text=message,
                **kwargs.get(
                    "message_label",
                    {},
                ),
            )

            # Place the 'message label' label widget within the grid
            message_label.grid(
                column=0,
                row=1,
                sticky=NSEW,
            )

            def _on_button_click(string: str) -> None:
                """
                Handles the button click event.

                This method is called when the button is clicked. It sets the result variable to the passed string and calls the on_click_callback callable if it is not None.
                Finally, it destroys the toplevel widget.

                Args:
                    string (str): The string to set the result variable to

                Returns:
                    None
                """

                # Declare a nonlocal variable
                nonlocal result

                # Update the result variable with the passed string argument
                result = string

                # Check, if the on_click_callback callable has been passed
                if on_click_callback:
                    # Call the on_click_callback callable
                    on_click_callback(string)

                # Destroy the toplevel widget
                toplevel.destroy()

            # Create a frame widget
            frame: tkinter.Frame = tkinter.Frame(
                master=toplevel,
                **kwargs.get(
                    "frame",
                    {},
                ),
            )

            # Set the weight of the 0th column to 1
            # This means that the column will stretch when the window is resized
            frame.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Set the weight of the 1st column to 1
            # This means that the column will stretch when the window is resized
            frame.grid_columnconfigure(
                index=1,
                weight=1,
            )

            # Place the frame widget within the grid
            frame.grid(
                column=0,
                row=2,
                sticky=NSEW,
            )

            # Create the 'okay button' button widget
            okay_button: tkinter.Button = tkinter.Button(
                command=lambda: _on_button_click(string="okay"),
                master=frame,
                text="Okay",
                **kwargs.get(
                    "okay_button",
                    {},
                ),
            )

            # Place the 'okay button' button widget within the grid
            okay_button.grid(
                column=0,
                padx=5,
                pady=5,
                row=2,
            )

            # Create the 'cancel button' button widget
            cancel_button: tkinter.Button = tkinter.Button(
                command=lambda: _on_button_click(string="cancel"),
                master=frame,
                text="Cancel",
                **kwargs.get(
                    "cancel_button",
                    {},
                ),
            )

            # Place the button widget within the grid
            cancel_button.grid(
                column=1,
                padx=5,
                pady=5,
                row=2,
            )

            # Wait until the toplevel widget is destroyed
            toplevel.wait_window()

            # Return the result
            return result
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'okay_cancel' method from '{cls.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            cls.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    @classmethod
    def retry(
        cls,
        title: str,
        message: str,
        on_click_callback: Optional[Callable[[str], None]] = None,
        **kwargs,
    ) -> Optional[str]:
        """
        Creates a toplevel widget with a retry button.

        This method creates a toplevel widget with a retry button and a message label.
        It also sets up the geometry of the widget and places the widgets within the grid.

        Args:
            title (str): The title of the toplevel widget
            message (str): The message to display in the message label
            on_click_callback (Optional[Callable[[str], None]]): The callback to execute when the retry button is clicked
            **kwargs: Any
                Additional keyword arguments to pass to the tkinter.Toplevel constructor

        Returns:
            Optional[str]: The result of the callback function
        """
        try:
            # Initialize the result variable as 'retry'
            result: str = "retry"

            # Create a toplevel widget
            toplevel: tkinter.Toplevel = tkinter.Toplevel(
                **kwargs.get(
                    "toplevel",
                    {},
                )
            )

            # Set the window title
            toplevel.wm_title(string=title)

            # Set the weight of the 0th column to 1
            # This means that the column will stretch when the window is resized
            toplevel.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Set the weight of the 0th row to 0
            # This means that the row will not stretch when the window is resized
            toplevel.grid_rowconfigure(
                index=0,
                weight=0,
            )

            # Set the weight of the 1st row to 1
            # This means that the row will stretch when the window is resized
            toplevel.grid_rowconfigure(
                index=1,
                weight=1,
            )

            # Set the weight of the 2nd row to 0
            # This means that the row will not stretch when the window is resized
            toplevel.grid_rowconfigure(
                index=2,
                weight=0,
            )

            # Create the 'title label' label widget
            title_label: tkinter.Label = tkinter.Label(
                master=toplevel,
                text=title,
                **kwargs.get(
                    "title_label",
                    {},
                ),
            )

            # Place the label widget within the grid
            title_label.grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the 'message label' label widget
            message_label: tkinter.Label = tkinter.Label(
                master=toplevel,
                text=message,
                **kwargs.get(
                    "message_label",
                    {},
                ),
            )

            # Place the label widget within the grid
            message_label.grid(
                column=0,
                row=1,
                sticky=NSEW,
            )

            def _on_button_click(string: str) -> None:
                """
                Handles the button click event.

                This method is called when the button is clicked. It sets the result variable to the passed string and calls the on_click_callback callable if it is not None.
                Finally, it destroys the toplevel widget.

                Args:
                    string (str): The string to set the result variable to

                Returns:
                    None
                """

                # Declare a non-local variable
                nonlocal result

                # Update the result variable with the passed string argument
                result = string

                # Check, if the on_click_callback callable has been passed
                if on_click_callback:
                    # Call the on_click_callback callable
                    on_click_callback("retry")

                # Destroy the toplevel widget
                toplevel.destroy()

            # Create a button widget
            button: tkinter.Button = tkinter.Button(
                command=lambda: _on_button_click(string="retry"),
                master=toplevel,
                text="retry",
                **kwargs.get(
                    "retry_button",
                    {},
                ),
            )

            # Place the button widget within the grid
            button.grid(
                column=0,
                padx=5,
                pady=5,
                row=2,
            )

            # Wait until the toplevel widget is destroyed
            toplevel.wait_window()

            # Return the result string
            return result
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'retry' method from '{cls.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            cls.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    @classmethod
    def retry_cancel(
        cls,
        title: str,
        message: str,
        on_click_callback: Optional[Callable[[str], None]] = None,
        **kwargs,
    ) -> Optional[str]:
        """
        Creates a toplevel widget with a retry and cancel button.

        This method creates a toplevel widget with a retry and cancel button and a message label.
        It also sets up the geometry of the widget and places the widgets within the grid.

        Args:
            title (str): The title of the toplevel widget
            message (str): The message to display in the message label
            on_click_callback (Optional[Callable[[str], None]]): The callback to execute when the retry or cancel button is clicked
            **kwargs: Any
                Additional keyword arguments to pass to the tkinter.Toplevel constructor

        Returns:
            Optional[str]: The result of the callback function
        """

        try:
            # Initialize the result variable as 'cancel'
            result: str = "cancel"

            # Create a toplevel widget
            toplevel: tkinter.Toplevel = tkinter.Toplevel(
                **kwargs.get(
                    "toplevel",
                    {},
                )
            )

            # Set the window title
            toplevel.wm_title(string=title)

            # Set the weight of the 0th column to 1
            # This means that the column will stretch when the window is resized
            toplevel.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Set the weight of the 0th row to 0
            # This means that the row will not stretch when the window is resized
            toplevel.grid_rowconfigure(
                index=0,
                weight=0,
            )

            # Set the weight of the 1st row to 1
            # This means that the row will stretch when the window is resized
            toplevel.grid_rowconfigure(
                index=1,
                weight=1,
            )

            # Set the weight of the 2nd row to 0
            # This means that the row will not stretch when the window is resized
            toplevel.grid_rowconfigure(
                index=2,
                weight=0,
            )

            # Create the 'title label' label widget
            title_label: tkinter.Label = tkinter.Label(
                master=toplevel,
                text=title,
                **kwargs.get(
                    "title_label",
                    {},
                ),
            )

            # Place the label widget within the grid
            title_label.grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the 'message label' label widget
            message_label: tkinter.Label = tkinter.Label(
                master=toplevel,
                text=message,
                **kwargs.get(
                    "message_label",
                    {},
                ),
            )

            # Place the 'message label' label widget within the grid
            message_label.grid(
                column=0,
                row=1,
                sticky=NSEW,
            )

            def _on_button_click(string: str) -> None:
                """
                Handles the button click event.

                This method is called when the button is clicked. It sets the result variable to the passed string and calls the on_click_callback callable if it is not None.
                Finally, it destroys the toplevel widget.

                Args:
                    string (str): The string to set the result variable to

                Returns:
                    None
                """

                # Declare a nonlocal variable
                nonlocal result

                # Update the result variable with the passed string argument
                result = string

                # Check, if the on_click_callback callable has been passed
                if on_click_callback:
                    # Call the on_click_callback callable
                    on_click_callback(string)

                # Destroy the toplevel widget
                toplevel.destroy()

            # Create a frame widget
            frame: tkinter.Frame = tkinter.Frame(
                master=toplevel,
                **kwargs.get(
                    "frame",
                    {},
                ),
            )

            # Set the weight of the 0th column to 1
            # This means that the column will stretch when the window is resized
            frame.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Set the weight of the 1st column to 1
            # This means that the column will stretch when the window is resized
            frame.grid_columnconfigure(
                index=1,
                weight=1,
            )

            # Place the frame widget within the grid
            frame.grid(
                column=0,
                row=2,
                sticky=NSEW,
            )

            # Create the 'retry button' button widget
            retry_button: tkinter.Button = tkinter.Button(
                command=lambda: _on_button_click(string="retry"),
                master=frame,
                text="retry",
                **kwargs.get(
                    "retry_button",
                    {},
                ),
            )

            # Place the 'retry button' button widget within the grid
            retry_button.grid(
                column=0,
                padx=5,
                pady=5,
                row=2,
            )

            # Create the 'cancel button' button widget
            cancel_button: tkinter.Button = tkinter.Button(
                command=lambda: _on_button_click(string="cancel"),
                master=frame,
                text="Cancel",
                **kwargs.get(
                    "cancel_button",
                    {},
                ),
            )

            # Place the button widget within the grid
            cancel_button.grid(
                column=1,
                padx=5,
                pady=5,
                row=2,
            )

            # Wait until the toplevel widget is destroyed
            toplevel.wait_window()

            # Return the result
            return result
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'retry_cancel' method from '{cls.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            cls.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    @classmethod
    def yes_no(
        cls,
        title: str,
        message: str,
        on_click_callback: Optional[Callable[[str], None]] = None,
        **kwargs,
    ) -> Optional[str]:
        """
        Creates a toplevel widget with a yes and no button.

        This method creates a toplevel widget with a yes and no button and a message label.
        It also sets up the geometry of the widget and places the widgets within the grid.

        Args:
            title (str): The title of the toplevel widget
            message (str): The message to display in the message label
            on_click_callback (Optional[Callable[[str], None]]): The callback to execute when the yes or no button is clicked
            **kwargs: Any
                Additional keyword arguments to pass to the tkinter.Toplevel constructor

        Returns:
            Optional[str]: The result of the callback function
        """

        try:
            # Initialize the result variable as 'no'
            result: str = "no"

            # Create a toplevel widget
            toplevel: tkinter.Toplevel = tkinter.Toplevel(
                **kwargs.get(
                    "toplevel",
                    {},
                )
            )

            # Set the window title
            toplevel.wm_title(string=title)

            # Set the weight of the 0th column to 1
            # This means that the column will stretch when the window is resized
            toplevel.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Set the weight of the 0th row to 0
            # This means that the row will not stretch when the window is resized
            toplevel.grid_rowconfigure(
                index=0,
                weight=0,
            )

            # Set the weight of the 1st row to 1
            # This means that the row will stretch when the window is resized
            toplevel.grid_rowconfigure(
                index=1,
                weight=1,
            )

            # Set the weight of the 2nd row to 0
            # This means that the row will not stretch when the window is resized
            toplevel.grid_rowconfigure(
                index=2,
                weight=0,
            )

            # Create the 'title label' label widget
            title_label: tkinter.Label = tkinter.Label(
                master=toplevel,
                text=title,
                **kwargs.get(
                    "title_label",
                    {},
                ),
            )

            # Place the label widget within the grid
            title_label.grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the 'message label' label widget
            message_label: tkinter.Label = tkinter.Label(
                master=toplevel,
                text=message,
                **kwargs.get(
                    "message_label",
                    {},
                ),
            )

            # Place the 'message label' label widget within the grid
            message_label.grid(
                column=0,
                row=1,
                sticky=NSEW,
            )

            def _on_button_click(string: str) -> None:
                """
                Handles the button click event.

                This method is called when the button is clicked. It sets the result variable to the passed string and calls the on_click_callback callable if it is not None.
                Finally, it destroys the toplevel widget.

                Args:
                    string (str): The string to set the result variable to

                Returns:
                    None
                """

                # Declare a nonlocal variable
                nonlocal result

                # Update the result variable with the passed string argument
                result = string

                # Check, if the on_click_callback callable has been passed
                if on_click_callback:
                    # Call the on_click_callback callable
                    on_click_callback(string)

                # Destroy the toplevel widget
                toplevel.destroy()

            # Create a frame widget
            frame: tkinter.Frame = tkinter.Frame(
                master=toplevel,
                **kwargs.get(
                    "frame",
                    {},
                ),
            )

            # Set the weight of the 0th column to 1
            # This means that the column will stretch when the window is resized
            frame.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Set the weight of the 1st column to 1
            # This means that the column will stretch when the window is resized
            frame.grid_columnconfigure(
                index=1,
                weight=1,
            )

            # Place the frame widget within the grid
            frame.grid(
                column=0,
                row=2,
                sticky=NSEW,
            )

            # Create the 'yes button' button widget
            yes_button: tkinter.Button = tkinter.Button(
                command=lambda: _on_button_click(string="yes"),
                master=frame,
                text="yes",
                **kwargs.get(
                    "yes_button",
                    {},
                ),
            )

            # Place the 'yes button' button widget within the grid
            yes_button.grid(
                column=0,
                padx=5,
                pady=5,
                row=2,
            )

            # Create the 'no button' button widget
            no_button: tkinter.Button = tkinter.Button(
                command=lambda: _on_button_click(string="no"),
                master=frame,
                text="no",
                **kwargs.get(
                    "no_button",
                    {},
                ),
            )

            # Place the button widget within the grid
            no_button.grid(
                column=1,
                padx=5,
                pady=5,
                row=2,
            )

            # Wait until the toplevel widget is destroyed
            toplevel.wait_window()

            # Return the result
            return result
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'yes_no' method from '{cls.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            cls.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    @classmethod
    def yes_no_cancel(
        cls,
        title: str,
        message: str,
        on_click_callback: Optional[Callable[[str], None]] = None,
        **kwargs,
    ) -> Optional[str]:
        """
        Creates a toplevel widget with a yes, no and cancel button.

        This method creates a toplevel widget with a yes, no and cancel button and a message label.
        It also sets up the geometry of the widget and places the widgets within the grid.

        Args:
            title (str): The title of the toplevel widget
            message (str): The message to display in the message label
            on_click_callback (Optional[Callable[[str], None]]): The callback to execute when the yes, no or cancel button is clicked
            **kwargs: Any
                Additional keyword arguments to pass to the tkinter.Toplevel constructor

        Returns:
            Optional[str]: The result of the callback function
        """

        try:
            # Initialize the result variable as 'no'
            result: str = "no"

            # Create a toplevel widget
            toplevel: tkinter.Toplevel = tkinter.Toplevel(
                **kwargs.get(
                    "toplevel",
                    {},
                )
            )

            # Set the window title
            toplevel.wm_title(string=title)

            # Set the weight of the 0th column to 1
            # This means that the column will stretch when the window is resized
            toplevel.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Set the weight of the 0th row to 0
            # This means that the row will not stretch when the window is resized
            toplevel.grid_rowconfigure(
                index=0,
                weight=0,
            )

            # Set the weight of the 1st row to 1
            # This means that the row will stretch when the window is resized
            toplevel.grid_rowconfigure(
                index=1,
                weight=1,
            )

            # Set the weight of the 2nd row to 0
            # This means that the row will not stretch when the window is resized
            toplevel.grid_rowconfigure(
                index=2,
                weight=0,
            )

            # Create the 'title label' label widget
            title_label: tkinter.Label = tkinter.Label(
                master=toplevel,
                text=title,
                **kwargs.get(
                    "title_label",
                    {},
                ),
            )

            # Place the label widget within the grid
            title_label.grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the 'message label' label widget
            message_label: tkinter.Label = tkinter.Label(
                master=toplevel,
                text=message,
                **kwargs.get(
                    "message_label",
                    {},
                ),
            )

            # Place the 'message label' label widget within the grid
            message_label.grid(
                column=0,
                row=1,
                sticky=NSEW,
            )

            def _on_button_click(string: str) -> None:
                """
                Handles the button click event.

                This method is called when the button is clicked. It sets the result variable to the passed string and calls the on_click_callback callable if it is not None.
                Finally, it destroys the toplevel widget.

                Args:
                    string (str): The string to set the result variable to

                Returns:
                    None
                """

                # Create a nonlocal variable
                nonlocal result

                # Update the result variable with the passed string argument
                result = string

                # Check, if the on_click_callback callable has been passed
                if on_click_callback:
                    # Call the on_click_callback callable
                    on_click_callback(string)

                # Destroy the toplevel widget
                toplevel.destroy()

            # Create a frame widget
            frame: tkinter.Frame = tkinter.Frame(
                master=toplevel,
                **kwargs.get(
                    "frame",
                    {},
                ),
            )

            # Set the weight of the 0th column to 1
            # This means that the column will stretch when the window is resized
            frame.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Set the weight of the 1st column to 1
            # This means that the column will stretch when the window is resized
            frame.grid_columnconfigure(
                index=1,
                weight=1,
            )

            # Set the weight of the 2nd column to 1
            # This means that the column will stretch when the window is resized
            frame.grid_columnconfigure(
                index=2,
                weight=1,
            )

            # Place the frame widget within the grid
            frame.grid(
                column=0,
                row=2,
                sticky=NSEW,
            )

            # Create the 'yes button' button widget
            yes_button: tkinter.Button = tkinter.Button(
                command=lambda: _on_button_click(string="yes"),
                master=frame,
                text="yes",
                **kwargs.get(
                    "yes_button",
                    {},
                ),
            )

            # Place the 'yes button' button widget within the grid
            yes_button.grid(
                column=0,
                padx=5,
                pady=5,
                row=2,
            )

            # Create the 'no button' button widget
            no_button: tkinter.Button = tkinter.Button(
                command=lambda: _on_button_click(string="no"),
                master=frame,
                text="no",
                **kwargs.get(
                    "no_button",
                    {},
                ),
            )

            # Place the button widget within the grid
            no_button.grid(
                column=1,
                padx=5,
                pady=5,
                row=2,
            )

            # Create the 'cancel button' button widget
            cancel_button: tkinter.Button = tkinter.Button(
                command=lambda: _on_button_click(string="cancel"),
                master=frame,
                text="cancel",
                **kwargs.get(
                    "cancel_button",
                    {},
                ),
            )

            # Place the button widget within the grid
            cancel_button.grid(
                column=2,
                padx=5,
                pady=5,
                row=2,
            )

            # Wait until the toplevel widget is destroyed
            toplevel.wait_window()

            # Return the result
            return result
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'yes_no_cancel' method from '{cls.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            cls.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e


class ToplevelToastNotification(tkinter.Toplevel):
    """
    A class representing a toast notification.

    This class extends the tkinter.Toplevel class and provides a toast notification with a fade-in and fade-out animation.

    Attributes:
        fade_after: int
            The duration of the fade animation in milliseconds
        fade_after_id: Optional[str]
            The ID of the fade animation
        fade_duration: int
            The duration of the fade animation in milliseconds
        on_click_callback: Optional[Callable[[], None]]
            The callback to execute when the notification is clicked
        position: Union[ToplevelPositions, str]
            The position of the notification on the screen
    """

    def __init__(
        self,
        message: str,
        title: str,
        fade_duration: int = 500,
        on_click_callback: Optional[Callable[[], None]] = None,
        position: Union[ToplevelPositions, str] = ToplevelPositions.TOP_RIGHT,
        master: Optional[tkinter.Misc] = None,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the ToplevelToastNotification class.

        Args:
            message: str
                The message to display in the notification
            title: str
                The title of the notification
            fade_duration: int
                The duration of the fade animation in milliseconds
            on_click_callback: Optional[Callable[[], None]]
                The callback to execute when the notification is clicked
            position: Union[ToplevelPositions, str]
                The position of the notification on the screen
            master: Optional[tkinter.Misc]
                The parent widget
            **kwargs: Any
                Additional keyword arguments to pass to the tkinter.Toplevel constructor

        Returns:
            None
        """

        # Initialize this class' logger instance in an instance variable
        self.logger: Final[Logger] = Logger.get_logger(name=self.__class__.__name__)

        # Initialize the fade after int instance variable as 2000
        # Notice: This is the amount of time that needs to pass until fade out sets in
        self.fade_after: int = 2000

        # Initialize the fade after id (optional) string instance variable as None
        self.fade_after_id: Optional[str] = None

        # Store the passed fade duration int in an instance variable
        # Notice: This is the total amount of time it takes to fade out
        self.fade_duration: int = fade_duration

        # Store the passed 'on click callback' callable in an instance variable
        self.on_click_callback: Optional[Callable[[], None]] = on_click_callback

        # Store the passed position (union) string, ToplevelPositions in an instance variable
        self.position: Union[ToplevelPositions, str] = position

        # Call the parent class constructor with the provided arguments
        super().__init__(
            master=master,
            **kwargs.get(
                "toast",
                {},
            ),
        )

        # Set the focus on the window
        self.grab_set()

        # Override the default behavior of the window
        self.overrideredirect(boolean=True)

        # Make the window non-transparent
        self.attributes(
            "-alpha",
            1.0,
        )

        # Raise the window to the top
        self.attributes(
            "-topmost",
            True,
        )

        # Make the window non-resizable
        self.resizable(
            height=False,
            width=False,
        )

        # Set the geometry of the window
        self.wm_geometry(newGeometry="400x100")

        # Set the title of the window
        self.wm_title(string=title)

        # Set the weight of the 0th column to 1
        # This means that the column will stretch when the window is resized
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Set the weight of the 0th row to 0
        # This means that the row will not stretch when the window is resized
        self.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Set the weight of the 1st row to 1
        # This means that the row will not stretch when the window is resized
        self.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Create the 'title label' label widget
        self._title_label: tkinter.Label = tkinter.Label(
            master=self,
            text=title,
            **kwargs.get(
                "title_label",
                {},
            ),
        )

        # Place the 'title label' label widget within the grid
        self._title_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Bind the 'on_click' method to the 'title label' label widget via the '<ButtonRelease-1>' event
        self._title_label.bind(
            func=self._on_click,
            sequence="<ButtonRelease-1>",
        )

        # Create the 'message label' label widget
        self._message_label: tkinter.Label = tkinter.Label(
            master=self,
            text=message,
            **kwargs.get(
                "message_label",
                {},
            ),
        )

        # Place the 'message label' label widget within the grid
        self._message_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )

        # Bind the 'on_click' method to the 'message label' label widget via the '<ButtonRelease-1>' event
        self._message_label.bind(
            func=self._on_click,
            sequence="<ButtonRelease-1>",
        )

        # Bind the 'on_leave' method to the window via the '<Leave>' event
        self.bind(
            func=self._on_leave,
            sequence="<Leave>",
        )

        # Bind the 'on_enter' method to the window via the '<Enter>' event
        self.bind(
            func=self._on_enter,
            sequence="<Enter>",
        )

        # Ring the bell
        self.bell()

        # Show the window
        self.show()

    @property
    def message_label(self) -> tkinter.Label:
        """
        Returns the 'message label' label widget.

        Returns:
            tkinter.Label: The 'message label' label widget
        """

        # Return the 'message label' label widget
        return self._message_label

    @property
    def title_label(self) -> tkinter.Label:
        """
        Returns the 'title label' label widget.

        Returns:
            tkinter.Label: The 'title label' label widget
        """

        # Return the 'title label' label widget
        return self._title_label

    def _fade_in(
        self,
        alpha: float,
    ) -> None:
        """
        Fades in the window.

        This method is called when the window needs to be faded in. It sets the opacity of the window to the passed alpha and schedules the next fade step.

        Parameters:
            alpha: float
                The alpha value to set for the window

        Returns:
            None
        """

        # Check, if the passed alpha is greater than or equal to 1.0
        if alpha >= 1.0:
            # Cancel the scheduled fade after call
            self.after_cancel(self.fade_after_id)

            # Reset the fade after id to None
            self.fade_after_id = None

            # Schedule the fade out
            self.fade_after_id = self.after(
                self.fade_after,
                self._fade_out,
                1.0,
            )

            # Return early
            return

        # Set the opacity of the window
        self.attributes(
            "-alpha",
            alpha,
        )

        # Schedule the next fade step
        self.after(
            50,
            self._fade_in,
            alpha + 0.05,
        )

    def _fade_out(
        self,
        alpha: float,
    ) -> None:
        """
        Fades out the window.

        This method is called when the window needs to be faded out. It sets the opacity of the window to the passed alpha and schedules the next fade step.

        Parameters:
            alpha: float
                The alpha value to set for the window

        Returns:
            None
        """

        # Check, if the passed alpha is less than or equal to 0
        if alpha <= 0:
            # Destroy the window
            self.destroy()

            # Return early
            return

        # Set the opacity of the window
        self.attributes(
            "-alpha",
            alpha,
        )

        # Schedule the next fade step
        self.after(
            50,
            self._fade_out,
            alpha - 0.05,
        )

    def _on_click(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        Handles the click event of the window.

        This method is called when the window is clicked. It calls the passed on_click_callback callable if it is not None.
        If an exception occurs while executing the on_click_callback callable, it is logged and the exception is re-raised.
        Finally, the ToplevelToastNotification is destroyed.

        Args:
            event (Optional[tkinter.Event]): The event object.

        Returns:
            None
        """

        # Check, if an on_click_callback callable has been passed
        if self.on_click_callback:
            try:
                # Call the on_click_callback callable
                self.on_click_callback()
            except Exception as e:
                # Log an error message indicating that an exception has occurred
                self.logger.error(
                    message=f"Caught an exception while attempting to execute 'on_click_callback' in '_on_click' method from '{self.__class__.__name__}': {e}"
                )

                # Log the traceback
                self.logger.error(message=traceback.format_exc())

                # Re-raise the exception to the caller
                raise e

        # Destroy the ToplevelToastNotification
        self.destroy()

    def _on_enter(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        Handles the enter event of the window.

        This method is called when the mouse enters the window. It cancels the fade out animation and schedules the fade in animation.

        Args:
            event (Optional[tkinter.Event]): The event object.

        Returns:
            None
        """

        # Check, if a fade after id has been scheduled
        if self.fade_after_id:
            # Cancel the scheduled fade after call
            self.after_cancel(self.fade_after_id)

            # Reset the fade after id to None
            self.fade_after_id = None

        # Set the opacity of the window to 100%
        self.attributes(
            "-alpha",
            1.0,
        )

        # Schedule the fade out
        self.fade_after_id = self.after(
            self.fade_after,
            self._fade_out,
            1.0,
        )

    def _on_leave(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        Handles the leave event of the window.

        This method is called when the mouse leaves the window. It schedules the fade out animation.

        Args:
            event (Optional[tkinter.Event]): The event object.

        Returns:
            None
        """

        # Schedule the fade out
        self.fade_after_id = self.after(
            25,
            self._fade_out,
            0.0,
        )

    def _place_toast(
        self,
        position: Union[ToplevelPositions, str],
    ) -> None:
        """
        Places the toast notification on the screen.

        This method is called when the toast notification needs to be placed on the screen. It updates the window's idletasks and calculates the position of the toast notification based on the passed position.

        Args:
            position (Union[ToplevelPositions, str]): The position of the toast notification on the screen

        Returns:
            None
        """
        try:
            # Update the window's idletasks
            self.update_idletasks()

            # Get the width of the screen
            screen_width: int = self.winfo_screenwidth()

            # Get the height of the screen
            screen_height: int = self.winfo_screenheight()

            # Get the width of the window
            window_width: int = self.winfo_width()

            # Get the height of the window
            window_height: int = self.winfo_height()

            # Initialize the x-coordinate to 0
            x: int = 0

            # Initialize the y-coordinate to 0
            y: int = 0

            if position == ToplevelPositions.TOP_LEFT:
                # Set the x-coordinate to 10
                x = 10

                # Set the y-coordinate to 10
                y = 10

            elif position == ToplevelPositions.TOP_RIGHT:
                # Set the x-coordinate to the width of the screen
                x = screen_width - window_width - 10

                # Set the y-coordinate to 10
                y = 10

            elif position == ToplevelPositions.CENTER:
                # Set the x-coordinate to the width of the screen
                x = screen_width / 2 - window_width / 2

                # Set the y-coordinate to the height of the screen
                y = screen_height / 2 - window_height / 2

            elif position == ToplevelPositions.BOTTOM_LEFT:
                # Set the x-coordinate to 10
                x = 10

                # Set the y-coordinate to height of the screen
                y = screen_height - window_height - 50

            elif position == ToplevelPositions.BOTTOM_RIGHT:
                # Set the x-coordinate to the width of the screen
                x = screen_width - window_width - 10

                # Set the y-coordinate to 10
                y = 10

            # Set the geometry of the window
            self.geometry(newGeometry=f"{window_width}x{window_height}+{x}+{y}")
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run '_place_toast' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @override
    def configure(
        self,
        name: Optional[str] = None,
        **kwargs,
    ) -> None:
        """
        Configures the widget in question by the passed name.

        This method is called when the widget in question needs to be configured. It configures the widget in question with the passed keyword arguments.

        Args:
            name (Optional[str]): The name of the widget in question
            **kwargs: Any
                Additional keyword arguments to pass to the tkinter.Misc constructor

        Returns:
            None
        """
        try:
            # Check, if the 'name' argument is None
            if name is None:
                # Call the super class' 'configure' method with the passed keyword arguments
                super().configure(**kwargs)

                # Return early
                return

            # Get the widget in question by the passed name
            widget: Optional[tkinter.Misc] = getattr(
                self,
                name,
                None,
            )

            # Check, if the 'widget' is None
            if widget is None:
                # Log an error message indicating that the widget is not found
                self.logger.error(
                    message=f"Widget '{name}' not found in '{self.__class__.__name__}' class"
                )

                # Return early
                return

            # Configure the widget
            widget.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_message_label(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the 'message label' label widget.

        This method is called when the 'message label' label widget needs to be configured. It configures the 'message label' label widget with the passed keyword arguments.

        Args:
            **kwargs: Any
                Additional keyword arguments to pass to the tkinter.Label constructor

        Returns:
            None
        """
        try:
            # Configure the 'message label' label widget
            self._message_label.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_message_label' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_title_label(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the 'title label' label widget.

        This method is called when the 'title label' label widget needs to be configured. It configures the 'title label' label widget with the passed keyword arguments.

        Args:
            **kwargs: Any
                Additional keyword arguments to pass to the tkinter.Label constructor

        Returns:
            None
        """
        try:
            # Configure the 'title label' label widget
            self._title_label.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_title_label' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def show(self) -> None:
        """
        Shows the toplevel widget.

        This method is called when the toplevel widget needs to be shown. It shows the toplevel widget with a fade-in animation.

        Args:
            None

        Returns:
            None
        """

        # Place the toplevel widget
        self._place_toast(position=self.position)

        # Schedule the fade in
        self.fade_after_id = self.after(
            25,
            self._fade_in,
            0.0,
        )
