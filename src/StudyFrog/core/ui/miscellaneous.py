"""
Author: lodego
Date: 2025-04-20
"""

import tkinter

from datetime import datetime
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
    """ """

    def __init__(
        self,
        master: tkinter.Misc,
        time_format: str = Constants.DEFAULT_TIME_FORMAT,
        **kwargs,
    ) -> None:
        """ """

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
        """ """

        # Return the tkinter.Label widget
        return self._label

    def _update_clock(self) -> None:
        """ """

        pass

    def configure_grid(self) -> None:
        """ """

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

    def create_widgets(self) -> None:
        """ """

        pass

    def create_widgets(self) -> None:
        """ """

        pass


class CountdownWidget(tkinter.Frame):
    """ """

    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        time_in_minutes: int,
        time_format: str = Constants.DEFAULT_TIME_FORMAT,
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

        # Initialize the 'is running' boolean flag as an instance variable
        self._is_running: bool = False

        # Initialize this class' Logger instance
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed time format string in an instance variable
        self.time_format: str = time_format

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
            100,
            self._update_clock,
        )

    def _update_clock(self) -> None:
        """ """

        pass

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

    def create_widgets(self) -> None:
        """ """

        pass

    def is_running(self) -> bool:
        """
        """

        # Return the 'is running' boolean flag instance variable
        return self._is_running


class CountupWidget(tkinter.Frame):
    """ """

    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        time_in_minutes: int,
        time_format: str = Constants.DEFAULT_TIME_FORMAT,
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

        # Initialize the 'is running' boolean flag as an instance variable
        self._is_running: bool = False

        # Initialize this class' Logger instance
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed time format string in an instance variable
        self.time_format: str = time_format

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
            100,
            self._update_clock,
        )

    def _update_clock(self) -> None:
        """ """

        pass

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

    def create_widgets(self) -> None:
        """ """

        pass

    def is_running(self) -> bool:
        """
        """

        # Return the 'is running' boolean flag instance variable
        return self._is_running
