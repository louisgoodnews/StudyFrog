"""
Author: lodego
Date: 2025-02-06
"""

from typing import *

from utils.logger import Logger


__all__: List[str] = ["Application"]


class Application:
    _shared_instance: Optional["Application"] = None

    def __new__(cls) -> "Application":
        if cls._shared_instance is None:
            cls._shared_instance = super().__new__(cls)
            cls._shared_instance.init()
        return cls._shared_instance

    def init(self) -> None:
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

    def start(self) -> None:
        try:
            pass
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'start' method from '{self.__class__.__name__}': {e}"
            )

            # Exit the application with a non-zero exit code indicating an exception occurred
            exit(1)

    def stop(self) -> None:
        try:
            # Exit the application with a zero exit code indicating no exception occurred
            exit(0)
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'stop' method from '{self.__class__.__name__}': {e}"
            )

            # Exit the application with a non-zero exit code indicating an exception occurred
            exit(1)
