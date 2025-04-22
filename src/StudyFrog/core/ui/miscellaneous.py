"""
Author: lodego
Date: 2025-04-20
"""

import tkinter
import traceback

from datetime import timedelta
from tkinter.constants import *
from typing import *

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous


__all__: Final[List[str]] = [
    "ClockWidget",
    "CountdownWidget",
    "CountupWidget",
]


class ClockWidget(tkinter.Frame):
    """
    A live-updating clock widget displaying the current system time.

    The ClockWidget updates automatically every 100 milliseconds and supports
    configurable time formats. It can be embedded in any Tkinter-based UI and is
    designed for use in dashboards, toolbars, or standalone time displays.
    """

    def __init__(
        self,
        master: tkinter.Misc,
        time_format: str = Constants.DEFAULT_TIME_FORMAT,
        **kwargs,
    ) -> None:
        """
        Initializes the ClockWidget and starts the live time update loop.

        Args:
            master (tkinter.Misc): The parent Tkinter widget.
            time_format (str, optional): Format string for displaying the current time.
                Follows `datetime.strftime` syntax. Defaults to Constants.DEFAULT_TIME_FORMAT.
            **kwargs: Additional keyword arguments forwarded to the tkinter.Frame constructor.

        Returns:
            None
        """

        # Call the parent class constructor with the passed arguments
        super().__init__(
            master=master,
            **kwargs,
        )

        # Initialize this class' Logger instance
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed time format string in an instance variable
        self.time_format: str = time_format

        # Configure the grid
        self.configure_grid()

        # Create the widgets
        self.create_widgets()

        # Update the clock after 100 miliseconds
        self.after(
            100,
            self._update_clock,
        )

    @property
    def label(self) -> tkinter.Label:
        """
        Returns the internal time label widget.

        Useful for configuring or styling the label externally.

        Returns:
            tkinter.Label: The label widget displaying the current time.
        """

        # Return the tkinter.Label widget
        return self._label

    def _update_clock(self) -> None:
        """
        Refreshes the displayed time and schedules the next update.

        Uses the current system time and the widget's configured time format to update
        the label text every 100 milliseconds.

        Returns:
            None
        """

        # Update the tkinter.Label's text
        self._label.configure(
            text=Miscellaneous.datetime_to_string(
                datetime=Miscellaneous.get_current_datetime(),
                format=self.time_format,
            ),
        )

        # Update the clock after 100 miliseconds
        self.after(
            100,
            self._update_clock,
        )

    def configure_grid(self) -> None:
        """
        Configures the internal grid layout of the ClockWidget.

        The single column stretches with the window, while the row remains fixed.
        This ensures proper alignment and scaling in different layouts.

        Returns:
            None
        """

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

    def configure_label(
        self,
        **kwargs,
    ) -> None:
        """
        Dynamically configures the internal label widget using given keyword arguments.

        This allows runtime customization of label appearance (e.g. font, background, padding).

        Args:
            **kwargs: Keyword arguments accepted by `tkinter.Label.configure()`.

        Returns:
            None

        Raises:
            Exception: If the configuration fails, the exception is logged and re-raised.
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

    def create_widgets(self) -> None:
        """
        Creates and places the internal label widget.

        The label is initialized with the current time and added to the widget's grid.

        Returns:
            None
        """

        # Create a tkinter.Label widget
        self._label: tkinter.Label = tkinter.Label(
            master=self,
            text=Miscellaneous.datetime_to_string(
                datetime=Miscellaneous.get_current_datetime(),
                format=self.time_format,
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


class CountdownWidget(tkinter.Frame):
    """ """

    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        hours: int = 1,
        minutes: int = 30,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        seconds: int = 0,
        **kwargs,
    ) -> None:
        """ """

        # Call the parent class constructor with the passed arguments
        super().__init__(
            master=master,
            **kwargs,
        )

        # Store the passed Dispatcher instance in an instance variable
        self.dispatcher: Dispatcher = dispatcher

        # Store the passed hours int as an instance variable
        self.hours: int = hours

        # Initialize the 'is running' boolean flag as an instance variable
        self._is_running: bool = False

        # Initialize this class' Logger instance
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed minutes int as an instance variable
        self.minutes: int = minutes

        # Store the passed namespace string as an instance variable
        self.namespace: str = namespace

        # Store the passed hours int as an instance variable
        self.seconds: int = seconds

        # Configure the grid
        self.configure_grid()

        # Create the widgets
        self.create_widgets()

        # Update the clock after 100 miliseconds
        self.update_call: str = self.after(
            100,
            self._update_clock,
        )

    @property
    def label(self) -> tkinter.Label:
        """ """

        # Return the tkinter.Label widget
        return self._label

    @property
    def pause_button(self) -> tkinter.Button:
        """ """

        # Return the 'pause button' tkinter.Button widget
        return self._pause_button

    @property
    def resume_button(self) -> tkinter.Button:
        """ """

        # Return the 'resume button' tkinter.Button widget
        return self._resume_button

    def _on_pause_button_click(self) -> None:
        """ """

        # Check, if the countdown is not running
        if not self._is_running:
            # Return early
            return

        # Disable the 'pause button' tkinter.Button widget
        self._pause_button.configure(state=DISABLED)

        # Enable the 'resume button' tkinter.Button widget
        self._resume_button.configure(state=NORMAL)

        # Update the 'is running' boolean flag instance variable
        self._is_running = not self._is_running

        # Cancel the update call
        self.after_cancel(id=self.update_call)

    def _on_resume_button_click(self) -> None:
        """ """

        # Check, if the countdown is running
        if self._is_running:
            # Return early
            return

        # Disable the 'resume button' tkinter.Button widget
        self._resume_button.configure(state=DISABLED)

        # Enable the 'pause button' tkinter.Button widget
        self._pause_button.configure(state=NORMAL)

        # Update the 'is running' boolean flag instance variable
        self._is_running = not self._is_running

        # Update the clock after 100 miliseconds
        self.update_call: str = self.after(
            1000,
            self._update_clock,
        )

    def _update_clock(self) -> None:
        """ """

        # Check, if the countdown is running
        if not self._is_running:
            # Return early
            return

        # decrement the seconds int
        self.seconds -= 1

        # Check, if the seconds are less than or equal to 0
        if self.seconds <= 0:

            # Reset the seconds int to 59
            self.seconds = 59

            # decrement the minutes int
            self.minutes -= 1

            # Check, if the minutes are less than or equal to 0
            if self.minutes <= 0:

                # Reset the minutes int to 59
                self.minutes = 59

                # decrement the hours int
                self.hours -= 1

        # Update the tkinter.Label widget's text
        self._label.configure(text=f"{self.hours} : {self.minutes} : {self.seconds}")

        # Schedule the next call
        self.after(
            1000,
            self._update_clock,
        )

    def configure_grid(self) -> None:
        """ """

        # Set the weight of the 0th column to 1
        # This means that the column will stretch when the window is resized
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Set the weight of the 1st column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_columnconfigure(
            index=1,
            weight=0,
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

    def configure_label(
        self,
        **kwargs,
    ) -> None:
        """ """
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

    def configure_pause_button(
        self,
        **kwargs,
    ) -> None:
        """ """
        try:
            # Attempt to configure the label widget
            self._pause_button.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_pause_button' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_resume_button(
        self,
        **kwargs,
    ) -> None:
        """ """
        try:
            # Attempt to configure the 'resume button' tkinter.Button widget
            self._resume_button.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_resume_button' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def create_widgets(self) -> None:
        """ """

        # Create a tkinter.Label widget
        self._label: tkinter.Label = tkinter.Label(
            master=self,
            text=f"{self.hours} : {self.minutes} : {self.seconds}",
        )

        # Place the tkinter.Label widget in the grid
        self._label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create the 'pause button' tkinter.Button widget
        self._pause_button: tkinter.Button = tkinter.Button(
            command=self._on_pause_button_click,
            master=self,
            text="⏸️",
        )

        # Place the 'pause button' tkinter.Button widget in the grid
        self._pause_button.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
        )

        # Create the 'resume button' tkinter.Button widget
        self._resume_button: tkinter.Button = tkinter.Button(
            command=self._on_resume_button_click,
            master=self,
            text="▶️",
        )

        # Place the 'resume button' tkinter.Button widget in the grid
        self._resume_button.grid(
            column=2,
            padx=5,
            pady=5,
            row=0,
        )

    def is_running(self) -> bool:
        """ """

        # Return the 'is running' boolean flag instance variable
        return self._is_running


class CountupWidget(tkinter.Frame):
    """ """

    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        hours: int = 0,
        minutes: int = 0,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        seconds: int = 0,
        **kwargs,
    ) -> None:
        """ """

        # Call the parent class constructor with the passed arguments
        super().__init__(
            master=master,
            **kwargs,
        )

        # Store the passed Dispatcher instance in an instance variable
        self.dispatcher: Dispatcher = dispatcher

        # Store the passed hours int as an instance variable
        self.hours: int = hours

        # Initialize the 'is running' boolean flag as an instance variable
        self._is_running: bool = False

        # Initialize this class' Logger instance
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed minutes int as an instance variable
        self.minutes: int = minutes

        # Store the passed namespace string as an instance variable
        self.namespace: str = namespace

        # Store the passed hours int as an instance variable
        self.seconds: int = seconds

        # Configure the grid
        self.configure_grid()

        # Create the widgets
        self.create_widgets()

        # Update the clock after 100 miliseconds
        self.update_call: str = self.after(
            1000,
            self._update_clock,
        )

    @property
    def label(self) -> tkinter.Label:
        """ """

        # Return the tkinter.Label widget
        return self._label

    @property
    def pause_button(self) -> tkinter.Button:
        """ """

        # Return the 'pause button' tkinter.Button widget
        return self._pause_button

    @property
    def resume_button(self) -> tkinter.Button:
        """ """

        # Return the 'resume button' tkinter.Button widget
        return self._resume_button

    def _on_pause_button_click(self) -> None:
        """ """

        # Check, if the countup is not running
        if not self._is_running:
            # Return early
            return

        # Disable the 'pause button' tkinter.Button widget
        self._pause_button.configure(state=DISABLED)

        # Enable the 'resume button' tkinter.Button widget
        self._resume_button.configure(state=NORMAL)

        # Update the 'is running' boolean flag instance variable
        self._is_running = not self._is_running

        # Cancel the update call
        self.after_cancel(id=self.update_call)

    def _on_resume_button_click(self) -> None:
        """ """

        # Check, if the countup is not running
        if self._is_running:
            # Return early
            return

        # Disable the 'resume button' tkinter.Button widget
        self._resume_button.configure(state=DISABLED)

        # Enable the 'pause button' tkinter.Button widget
        self._pause_button.configure(state=NORMAL)

        # Update the 'is running' boolean flag instance variable
        self._is_running = not self._is_running

        # Update the clock after 100 miliseconds
        self.update_call: str = self.after(
            1000,
            self._update_clock,
        )

    def _update_clock(self) -> None:
        """ """

        # Check, if the countup is not running
        if not self._is_running:
            # Return early
            return

        # Increment the seconds int
        self.seconds += 1

        # Check, if the seconds are more than or equal to 60
        if self.seconds >= 60:

            # Reset the seconds int to 0
            self.seconds = 0

            # Increment the minutes int
            self.minutes += 1

            # Check, if the minutes are more than or equal to 60
            if self.minutes == 60:

                # Reset the minutes int to 0
                self.minutes = 0

                # Increment the hours int
                self.hours += 1

        # Update the tkinter.Label widget's text
        self._label.configure(text=f"{self.hours} : {self.minutes} : {self.seconds}")

        # Schedule the next call
        self.after(
            100,
            self._update_clock,
        )

    def configure_grid(self) -> None:
        """ """

        # Set the weight of the 0th column to 1
        # This means that the column will stretch when the window is resized
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Set the weight of the 1st column to 0
        # This means that the column will not stretch when the window is resized
        self.grid_columnconfigure(
            index=1,
            weight=0,
        )

        # Set the weight of the 0th row to 0
        # This means that the row will not stretch when the window is resized
        self.grid_rowconfigure(
            index=0,
            weight=0,
        )

    def configure_label(
        self,
        **kwargs,
    ) -> None:
        """ """
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

    def configure_pause_button(
        self,
        **kwargs,
    ) -> None:
        """ """
        try:
            # Attempt to configure the label widget
            self._pause_button.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_pause_button' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_resume_button(
        self,
        **kwargs,
    ) -> None:
        """ """
        try:
            # Attempt to configure the 'resume button' tkinter.Button widget
            self._resume_button.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_resume_button' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def create_widgets(self) -> None:
        """ """

        # Create a tkinter.Label widget
        self._label: tkinter.Label = tkinter.Label(
            master=self,
            text=f"{self.hours} : {self.minutes} : {self.seconds}",
        )

        # Place the tkinter.Label widget in the grid
        self._label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create the 'pause button' tkinter.Button widget
        self._pause_button: tkinter.Button = tkinter.Button(
            command=self._on_pause_button_click,
            master=self,
            text="⏸️",
        )

        # Place the 'pause button' tkinter.Button widget in the grid
        self._pause_button.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
        )

        # Create the 'resume button' tkinter.Button widget
        self._resume_button: tkinter.Button = tkinter.Button(
            command=self._on_resume_button_click,
            master=self,
            text="▶️",
        )

        # Place the 'resume button' tkinter.Button widget in the grid
        self._resume_button.grid(
            column=2,
            padx=5,
            pady=5,
            row=0,
        )

    def is_running(self) -> bool:
        """ """

        # Return the 'is running' boolean flag instance variable
        return self._is_running
