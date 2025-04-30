""" """

import asyncio
import traceback

from datetime import datetime
from typing import *

from utils.constants import Constants
from utils.file_service import FileService
from utils.level import Level
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous


__all__: Final[List[str]] = ["LogWriter"]


class LogWriter:
    """ """

    # The shared instance to facilitate the singleton pattern
    _shared_instance: Optional["LogWriter"] = None

    def __new__(cls) -> "LogWriter":
        """
        Creates a new instance of the LogWriter class.

        If the instance does not exist, it creates a new one by calling the parent
        class constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, it returns the existing instance.

        Args:
            None

        Returns:
            LogWriter: The created or existing instance of LogWriter class.
        """
        if not cls._shared_instance:
            cls._shared_instance = super(cls).__new__()
            cls._shared_instance.init()
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes a new instance of the LogWriter class.

        This method is called once the singleton instance is initialized and should not be
        called directly.

        Args:
            None

        Returns:
            None
        """

        # Initialize this instance's Logger
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Initialize the log queue list as an empty list
        self.log_queue: List[str] = []

        # Initialize the log queue size
        self._log_queue_size: int = 50

        # Initialize the datetime timestamp
        self.timestamp: datetime = Miscellaneous.get_current_datetime()

    @property
    def log_queue_size(self) -> int:
        """
        Gets the log queue size.

        Returns:
            int: The log queue size.
        """

        return self._log_queue_size

    @log_queue_size.setter
    def log_queue_size(
        self,
        value: int,
    ) -> None:
        """
        Sets the log queue size.

        Args:
            value (int): The new log queue size.

        Returns:
            None
        """

        self._log_queue_size = value

    def _flush_log_queue(self) -> None:
        """
        Internal method that flushes the log queue.

        Args:
            None

        Returns:
            None
        """

        # Check, if the log queue is empty
        if len(self.log_queue) == 0:
            # Return early
            return

        # Clear the log queue
        self.log_queue.clear()

        # Update the timestamp
        self.timestamp = Miscellaneous.get_current_datetime()

    def write(
        self,
        level: Level,
        message: str,
        queue: bool = True,
    ) -> None:
        """
        Writes a log message into a file corresponding to the passed Level Enum.

        Args:
            level (Level): The level of the log message.
            message (str): The log message.
            queue (bool, optional): Whether to add the log message to the queue. Defaults to True.

        Returns:
            None

        Raises:
            Exception: If an error occurs during log writing.
        """
        try:
            # Check, if the passed queue parameter is True
            if queue:
                # Append the level, log message and a new timestamp to the queue
                self.log_queue.append(
                    {
                        "level": level,
                        "message": message,
                        "timestamp": Miscellaneous.datetime_to_string(
                            datetime=Miscellaneous.get_current_datetime()
                        ),
                    }
                )

                # Return early
                return

            # Write the message to the log file directly

        except Exception as e:
            # Log an error message indicating thhat an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'write' method from {self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e
