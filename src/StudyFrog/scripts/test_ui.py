"""
Author: lodego
Date: 2025-05-19
"""

import tkinter
import traceback

from typing import *
from tkinter.constants import *

from core.ui.fields.string_fields import MultiLineTextField
from core.ui.frames.frames import ScrolledFrame

from utils.constants import Constants
from utils.logger import Logger


__all__: Final[List[str]] = ["test_ui"]


def test_ui() -> None:
    """
    Tests the UI.

    Args:
        None

    Returns:
        None
    """

    # Get the logger
    logger: Logger = Logger.get_logger(name="test_ui")

    # Log a debug message
    logger.debug(message="Testing UI...")

    try:
        # Create the main window
        root: tkinter.Tk = tkinter.Tk()

        # Set the window title
        root.title("Test UI")

        # Set the window geometry
        root.geometry("400x300")

        # Configure the 0th column to weight 1
        root.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the 0th row to weight 1
        root.grid_rowconfigure(
            index=0,
            weight=1,
        )

        scrolled_frame: ScrolledFrame = ScrolledFrame(
            master=root,
            column=0,
            row=0,
        )

        scrolled_frame.configure(background=Constants.RED["700"])

        # Start the main event loop
        root.mainloop()
    except Exception as e:
        # Log an error message indicating an exception has occurred
        logger.error(
            message=f"Caught an exception while attempting to run 'test_ui' method from '{__name__}': {e}"
        )

        # Log the traceback
        logger.error(message=f"Traceback: {traceback.format_exc()}")

        # Re-raise the exception to the caller
        raise e

    # Log a debug message
    logger.debug(message="Testing UI completed.")


if __name__ == "__main__":
    test_ui()
