"""
Author: lodego
Date: 2025-04-20
"""

import tkinter
import traceback

from tkinter.constants import *
from typing import *

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous


__all__: Final[List[str]] = [
    "ClockWidget",
    "CountdownButtonWidget",
    "CountdownClockWidget",
    "CountupClockWidget",
    "DateClockWidget",
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


class CountdownButtonWidget(tkinter.Button):
    """
    A countdown button widget that disables itself during a countdown and re-enables it once the countdown is complete.
    """

    def __init__(
        self,
        display_name: str,
        master: tkinter.Misc,
        namespace: str = Constants.GLOBAL_NAMESPACE,
        on_click_callback: Optional[Callable[[str], None]] = None,
        time_to_countdown: int = 10,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the CountdownButtonWidget class.

        Args:
            master (tkinter.Misc): The master widget.
            namespace (str): The namespace to use for event dispatching.
            on_click_callback (Optional[Callable[[str], None]]): The callback to execute when the button is clicked.
            time_to_countdown (int): The time in seconds to count down.
            **kwargs: Additional keyword arguments passed to the parent Button.

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

        # Initialize the Dispatcher instance
        self.dispatcher: Dispatcher = Dispatcher()

        # Store the passed display_name string in an instance variable
        self.display_name: str = display_name

        # Store the passed namespace string in an instance variable
        self.namespace: str = namespace

        # Store the passed on_click_callback callable in an instance variable
        self.on_click_callback: Optional[Callable[[str], None]] = on_click_callback

        # Store the passed time_to_countdown int in an instance variable
        self.time_to_countdown: int = time_to_countdown

        # Set the button's text
        self.configure(text=f"{self.time_to_countdown} seconds remaining")

        # Check, if the button has a callback
        if self.cget(key="command"):
            # Set the on_click_callback to the button's command
            self.on_click_callback = self.cget(key="command")

        # Set the button's command to the _on_button_click method
        self.configure(command=self._on_button_click)

        # Execute the countdown
        self._execute_countdown()

    def _execute_countdown(self) -> None:
        """
        Executes the countdown logic.

        This Method disables the button, then starts the countdown an re-enables the button once the countdown has reached 0.

        Args:
            None

        Returns:
            None

        Raises:
            Exception: If an exception occurs during the execution of the method.
        """
        try:
            # Disable the button
            self.configure(state=DISABLED)

            # Start the countdown
            for i in range(self.time_to_countdown, 0, -1):
                # Update the button's text
                self.configure(text=f"{i} seconds remaining")

                # Wait for 1 second
                self.after(1000)

            # Re-enable the button
            self.configure(state=NORMAL)

            # Update the button's text to the display name
            self.configure(text=self.display_name)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run '_execute_countdown' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the exceptions traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def _on_button_click(self) -> None:
        """
        Handles the logic for expanding/collapsing the frame.

        When the button is clicked, this method toggles the visibility
        of the internal container and updates the button label.

        Args:
            None

        Returns:
            None

        Raises:
            Exception: If an exception occurs during the execution of the method.
        """
        try:
            # Get the button's text
            text: str = self.cget(key="text")

            # Check, if the 'on_click_callback' callable is not None
            if self.on_click_callback:
                # Call the 'on_click_callback' callable with the passed namespace string
                self.on_click_callback(text)

            # Dispatch the COUNTDOWN_BUTTON_CLICKED event
            self.dispatcher.dispatch(
                event=Events.COUNTDOWN_BUTTON_CLICKED,
                namespace=self.namespace,
                text=text,
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run '_on_button_click' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the exceptions traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e


class CountdownClockWidget(tkinter.Frame):
    """
    A countdown clock widget that displays the remaining time in hours, minutes, and seconds.
    """

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
        """
        Initializes a new instance of the CountdownClockWidget class.

        Args:
            dispatcher (Dispatcher): The dispatcher to use for event dispatching.
            master (tkinter.Misc): The master widget.
            hours (int): The number of hours to count down.
            minutes (int): The number of minutes to count down.
            namespace (str): The namespace to use for event dispatching.
            seconds (int): The number of seconds to count down.
            **kwargs: Additional keyword arguments passed to the parent Frame.

        Returns:
            None
        """

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
        self._is_running: bool = True

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
        """
        Returns the internal label widget.

        Useful for configuring or styling the label externally.

        Returns:
            tkinter.Label: The label widget displaying the current time.
        """

        # Return the tkinter.Label widget
        return self._label

    @property
    def pause_button(self) -> tkinter.Button:
        """
        Returns the internal pause button widget.

        Useful for configuring or styling the button externally.

        Returns:
            tkinter.Button: The pause button widget.
        """

        # Return the 'pause button' tkinter.Button widget
        return self._pause_button

    @property
    def resume_button(self) -> tkinter.Button:
        """
        Returns the internal resume button widget.

        Useful for configuring or styling the button externally.

        Returns:
            tkinter.Button: The resume button widget.
        """

        # Return the 'resume button' tkinter.Button widget
        return self._resume_button

    def _on_pause_button_click(self) -> None:
        """
        Handles the logic for pausing the countdown.

        When the pause button is clicked, this method disables the pause button,
        enables the resume button, and updates the 'is running' flag.

        Args:
            None

        Returns:
            None
        """

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
        """
        Handles the logic for resuming the countdown.

        When the resume button is clicked, this method disables the resume button,
        enables the pause button, and updates the 'is running' flag.

        Args:
            None

        Returns:
            None
        """

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
        """
        Updates the clock display.

        This method decrements the seconds, minutes, and hours, and updates the label
        display accordingly. If the countdown reaches zero, it resets the values and
        disables the buttons.

        Args:
            None

        Returns:
            None
        """

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
        """
        Configures the grid layout for the widget.

        This method sets up the grid layout for the widget by configuring the weights
        of the columns and rows. The 0th column has a weight of 1, meaning it will
        stretch when the window is resized. The 1st and 2nd columns have a weight of 0,
        meaning they will not stretch. The 0th row also has a weight of 0.

        Args:
            None

        Returns:
            None
        """

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
        """
        Attempts to configure the label widget with the passed keyword arguments.

        Args:
            **kwargs: Additional keyword arguments passed to the label widget's configure method.

        Returns:
            None

        Raises:
            Exception: If an exception occurs during the execution of the method.
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

    def configure_pause_button(
        self,
        **kwargs,
    ) -> None:
        """
        Attempts to configure the pause button widget with the passed keyword arguments.

        Args:
            **kwargs: Additional keyword arguments passed to the pause button widget's configure method.

        Returns:
            None

        Raises:
            Exception: If an exception occurs during the execution of the method.
        """
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
        """
        Attempts to configure the resume button widget with the passed keyword arguments.

        Args:
            **kwargs: Additional keyword arguments passed to the resume button widget's configure method.

        Returns:
            None

        Raises:
            Exception: If an exception occurs during the execution of the method.
        """
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
        """
        Creates the internal widgets for the widget.

        This method creates the internal widgets for the widget, including the label,
        pause button, and resume button. It also places the widgets in the grid layout.

        Args:
            None

        Returns:
            None
        """

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
            state=DISABLED,
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
        """
        Returns the 'is running' boolean flag instance variable.

        Returns:
            bool: The 'is running' boolean flag instance variable.
        """

        # Return the 'is running' boolean flag instance variable
        return self._is_running


class CountupClockWidget(tkinter.Frame):
    """
    A countup clock widget that displays the elapsed time in hours, minutes, and seconds.
    """

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
        """
        Initializes a new instance of the CountupClockWidget class.

        Args:
            dispatcher (Dispatcher): The dispatcher to use for event dispatching.
            master (tkinter.Misc): The master widget.
            hours (int): The number of hours to count up.
            minutes (int): The number of minutes to count up.
            namespace (str): The namespace to use for event dispatching.
            seconds (int): The number of seconds to count up.
            **kwargs: Additional keyword arguments passed to the parent Frame.

        Returns:
            None
        """

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
        self._is_running: bool = True

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
        """
        Returns the internal label widget.

        Useful for configuring or styling the label externally.

        Returns:
            tkinter.Label: The label widget displaying the current time.
        """

        # Return the tkinter.Label widget
        return self._label

    @property
    def pause_button(self) -> tkinter.Button:
        """
        Returns the internal 'pause button' tkinter.Button widget.

        Useful for configuring or styling the 'pause button' externally.

        Returns:
            tkinter.Button: The 'pause button' tkinter.Button widget.
        """

        # Return the 'pause button' tkinter.Button widget
        return self._pause_button

    @property
    def resume_button(self) -> tkinter.Button:
        """
        Returns the internal 'resume button' tkinter.Button widget.

        Useful for configuring or styling the 'resume button' externally.

        Returns:
            tkinter.Button: The 'resume button' tkinter.Button widget.
        """

        # Return the 'resume button' tkinter.Button widget
        return self._resume_button

    def _on_pause_button_click(self) -> None:
        """
        Handles the logic for pausing the countup.

        When the 'pause button' tkinter.Button widget is clicked, this method updates the
        'is running' boolean flag instance variable and disables the 'pause button' tkinter.Button
        widget while enabling the 'resume button' tkinter.Button widget.

        Args:
            None

        Returns:
            None
        """

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
        """
        Handles the logic for resuming the countup.

        When the 'resume button' tkinter.Button widget is clicked, this method updates the
        'is running' boolean flag instance variable and disables the 'resume button' tkinter.Button
        widget while enabling the 'pause button' tkinter.Button widget.

        Args:
            None

        Returns:
            None
        """

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
        """
        Updates the countup clock.

        This method updates the countup clock by incrementing the seconds int and updating the tkinter.Label widget's text.

        Args:
            None

        Returns:
            None
        """

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
            1000,
            self._update_clock,
        )

    def configure_grid(self) -> None:
        """
        Configures the grid layout for the widget.

        This method configures the grid layout for the widget by setting the weights of the columns and rows.

        Args:
            None

        Returns:
            None
        """

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
        """
        Attempts to configure the label widget with the passed keyword arguments.

        Args:
            **kwargs: Additional keyword arguments passed to the label widget's configure method.

        Returns:
            None

        Raises:
            Exception: If an exception occurs during the execution of the method.
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

    def configure_pause_button(
        self,
        **kwargs,
    ) -> None:
        """
        Attempts to configure the pause button widget with the passed keyword arguments.

        Args:
            **kwargs: Additional keyword arguments passed to the pause button widget's configure method.

        Returns:
            None

        Raises:
            Exception: If an exception occurs during the execution of the method.
        """
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
        """
        Attempts to configure the resume button widget with the passed keyword arguments.

        Args:
            **kwargs: Additional keyword arguments passed to the resume button widget's configure method.

        Returns:
            None

        Raises:
            Exception: If an exception occurs during the execution of the method.
        """
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
        """
        Creates the internal widgets for the widget.

        This method creates the internal widgets for the widget, including the label and the buttons.

        Args:
            None

        Returns:
            None
        """

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
            state=DISABLED,
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
        """
        Returns the 'is running' boolean flag instance variable.

        Returns:
            bool: The 'is running' boolean flag instance variable.
        """

        # Return the 'is running' boolean flag instance variable
        return self._is_running


class DateClockWidget(tkinter.Frame):
    """
    The DateClockWidget class is a tkinter.Frame widget that displays the current date and time.

    This class consists of two tkinter.Label widgets, one for the time and one for the date.
    """

    def __init__(
        self,
        master: tkinter.Misc,
        date_format: str = "%a, %d.%m.%Y",
        time_format: str = "%H:%M:%S",
        **kwargs,
    ) -> None:
        """
        Initializes the DateClockWidget instance.

        Args:
            master (tkinter.Misc): The parent widget.
            date_format (str): The date format string. Defaults to "%a, %d.%m.%Y".
            time_format (str): The time format string. Defaults to "%H:%M:%S".
            **kwargs: Additional keyword arguments to pass to the parent constructor.

        Returns:
            None
        """

        # Call the parent constructor
        super().__init__(
            master=master,
            **kwargs,
        )

        # Initialize this class' Logger instance
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed time format string in an instance variable
        self.time_format: str = time_format

        # Store the passed date format string in an instance variable
        self.date_format: str = date_format

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
    def date_label(self) -> tkinter.Label:
        """
        Returns the internal tkinter.Label widget.

        Args:
            None

        Returns:
            tkinter.Label: The tkinter.Label widget.
        """

        # Return the tkinter.Label widget
        return self._date_label

    @property
    def time_label(self) -> tkinter.Label:
        """
        Returns the internal tkinter.Label widget.

        Args:
            None

        Returns:
            tkinter.Label: The tkinter.Label widget.
        """

        # Return the tkinter.Label widget
        return self._time_label

    def _update_clock(self) -> None:
        """
        Updates the clock every second.

        Args:
            None

        Returns:
            None
        """

        timestamp: datetime = Miscellaneous.get_current_datetime()

        # Update the time label
        self.time_label.configure(
            text=Miscellaneous.datetime_to_string(
                datetime=timestamp,
                format=self.time_format,
            ),
        )

        # Update the date label
        self.date_label.configure(
            text=Miscellaneous.datetime_to_string(
                datetime=timestamp,
                format=self.date_format,
            ),
        )

        # Schedule the next update
        self.after(
            1000,
            self._update_clock,
        )

    def configure_date_label(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the date label widget.

        Args:
            **kwargs: Additional keyword arguments to pass to the tkinter.Label widget's configure method.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while configuring the date label widget.
        """
        try:
            # Attempt to configre the date label widget with the passed keyword argument
            self._date_label.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_date_label' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_grid(self) -> None:
        """
        Configures the grid layout of the DateClockWidget instance.

        Args:
            None

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

        # Set the weight of the 1st row to 0
        # This means that the row will not stretch when the window is resized
        self.grid_rowconfigure(
            index=1,
            weight=0,
        )

    def configure_time_label(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the time label widget.

        Args:
            **kwargs: Additional keyword arguments to pass to the tkinter.Label widget's configure method.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while configuring the time label widget.
        """
        try:
            # Attempt to configre the time label widget with the passed keyword argument
            self._time_label.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_time_label' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def create_widgets(self) -> None:
        """
        Creates and places the internal tkinter.Label widgets.

        The labels are initialized with empty strings and added to the widget's grid.

        Args:
            None

        Returns:
            None
        """

        # Create a tkinter.Label widget
        self._time_label: tkinter.Label = tkinter.Label(
            master=self,
            text="",
        )

        # Place the tkinter.Label widget in the grid
        self._time_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a tkinter.Label widget
        self._date_label: tkinter.Label = tkinter.Label(
            master=self,
            text="",
        )

        # Place the tkinter.Label widget in the grid
        self._date_label.grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )
