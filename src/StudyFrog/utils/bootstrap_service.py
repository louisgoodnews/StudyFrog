"""
Author: lodego
Date: 2025-02-09
"""

import tkinter
from typing import *

from core.answer import AnswerManager
from core.association import AssociationManager
from core.change_history import ChangeHistoryManager, ChangeHistoryItemManager
from core.custom_field import CustomFieldManager
from core.default import DefaultManager
from core.difficulty import DifficultyManager
from core.flashcard import FlashcardManager
from core.note import NoteManager
from core.option import OptionManager
from core.priority import PriorityManager
from core.question import QuestionManager
from core.setting import SettingManager, SettingService
from core.stack import StackManager
from core.tag import TagManager
from core.user import UserManager

from core.ui.dashboard_ui import DashboardUI
from core.ui.setting_ui import SettingUI
from core.ui.ui_registry import UIRegistry

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.logger import Logger
from utils.navigation import NavigationService
from utils.unified_manager import UnifiedManager


__all__: List[str] = ["BootstrapService"]


class BootstrapService:
    """
    A singleton class responsible for bootstrapping and initializing core services.

    This class provides a shared instance that initializes and manages essential services
    such as logging, event dispatching, navigation, and settings. It ensures that these
    services are set up and accessible throughout the application.

    Attributes:
        _shared_instance (Optional[BootstrapService]): The shared instance of the service.
        logger (Logger): The logger instance for logging information and errors.
        dispatcher (Dispatcher): The dispatcher instance for managing events.
        navigation_service (NavigationService): The service for handling navigation.
        setting_service (SettingService): The service for managing settings.
    """

    _shared_instance: Optional["BootstrapService"] = None

    def __new__(cls) -> "BootstrapService":
        """
        Creates and returns a new instance of the BootstrapService class.

        If the instance does not exist, creates a new one by calling the parent class constructor
        and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Returns:
            BootstrapService: The created or existing instance of BootstrapService class.
        """
        if cls._shared_instance is None:
            cls._shared_instance = super().__new__(cls)
            cls._shared_instance.init()
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes the shared instance of the BootstrapService.

        This method is called when the shared instance is created, and it initializes
        the logger, dispatcher, navigation service, and setting service.

        Returns:
            None
        """

        # Initialize a logger instance
        self.logger = Logger.get_logger(name=self.__class__.__name__)

        # Initialize the dispatcher instance
        self.dispatcher: Dispatcher = Dispatcher()

        # Initialize the navigation service instance
        self.navigation_service: NavigationService = NavigationService(
            dispatcher=self.dispatcher
        )

        # Initialize the setting service instance
        self.setting_service: SettingService = SettingService()

        # Initialize the unified manager instance
        self.unified_manager: UnifiedManager = UnifiedManager()

    def register_handlers(self) -> None:
        """
        Registers functions to be called when certain events are dispatched.

        This method registers functions with the Dispatcher to be called when
        certain events are dispatched. The functions are registered with the
        Dispatcher and provide a way to handle events in a centralized manner.

        The events and their associated functions are as follows:
        - REQUEST_BACKWARD_NAVIGATION: `on_request_backward_navigation`
        - REQUEST_FORWARD_NAVIGATION: `on_request_forward_navigation`

        Returns:
            None
        """
        try:
            # Register a function to be called when the REQUEST_BACKWARD_NAVIGATION event is dispatched
            self.dispatcher.register(
                event=Events.REQUEST_BACKWARD_NAVIGATION,
                function=self.navigation_service.on_request_backward_navigation,
                namespace=Constants.GLOBAL_NAMESPACE,
                persistent=True,
            )

            # Register a function to be called when the REQUEST_FORWARD_NAVIGATION event is dispatched
            self.dispatcher.register(
                event=Events.REQUEST_FORWARD_NAVIGATION,
                function=self.navigation_service.on_request_forward_navigation,
                namespace=Constants.GLOBAL_NAMESPACE,
                persistent=True,
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'register_handlers' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def register_menus(self) -> None:
        """
        Registers the UI classes for the main menu with the UIRegistry.

        This method registers the DashboardUI, SettingUI and various other classes with the UIRegistry,
        which allows them to be instantiated and used elsewhere in the application.

        Returns:
            None
        """
        try:
            # Store the menus in a dictionary
            menus: Dict[str, Type[tkinter.Misc]] = {
                "dashboard": DashboardUI,
                "settings": SettingUI,
            }

            # Iterate over the menus and register each one with the UIRegistry
            for (
                name,
                widget,
            ) in menus.items():
                # Register the type with the UIRegistry
                UIRegistry.register(
                    name=name,
                    widget=widget,
                )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'run_startup_tasks' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def register_managers(self) -> None:
        """
        Registers the managers with the UnifiedManager.

        This method registers all manager classes with the UnifiedManager,
        which allows them to be accessed and used elsewhere in the application.

        Returns:
            None
        """
        try:
            # Store the manager classes in a dictionary
            managers: Dict[str, Type[Any]] = {
                "answer_manager": AnswerManager,
                "association_manager": AssociationManager,
                "change_history_manager": ChangeHistoryManager,
                "change_history_item_manager": ChangeHistoryItemManager,
                "custom_field_manager": CustomFieldManager,
                "default_manager": DefaultManager,
                "difficulty_manager": DifficultyManager,
                "flashcard_manager": FlashcardManager,
                "note_manager": NoteManager,
                "option_manager": OptionManager,
                "priority_manager": PriorityManager,
                "question_manager": QuestionManager,
                "setting_manager": SettingManager,
                "stack_manager": StackManager,
                "tag_manager": TagManager,
                "user_manager": UserManager,
            }

            # Iterate over the managers and register each one with the UnifiedManager
            for (
                name,
                manager,
            ) in managers.items():
                # Register the manager with the UnifiedManager
                self.unified_manager.register_manager(
                    name=name,
                    manager=manager,
                )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'register_managers' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def run_startup_tasks(
        self,
    ) -> Tuple[
        Optional[Dispatcher],
        Optional[NavigationService],
        Optional[SettingService],
        Optional[UnifiedManager],
    ]:
        """
        Executes startup tasks for the application.

        This method registers UI menus and returns initialized instances of
        dispatcher, navigation service, and setting service.

        Returns:
            Tuple[Optional[Dispatcher], Optional[NavigationService], Optional[SettingService], Optional[UnifiedManager]]:
            A tuple containing the dispatcher, navigation service, and setting service
            instances, or None values if an exception occurs.

        Raises:
            Exception: If an exception occurs while running the startup tasks.
        """
        try:
            # Register the event handlers
            self.register_handlers()

            # Register the managers with the UnifiedManager
            self.register_managers()

            # Register the menus with the UIRegistry
            self.register_menus()

            # Return the dispatcher, navigation service, setting service, and unified manager instances
            return (
                self.dispatcher,
                self.navigation_service,
                self.setting_service,
                self.unified_manager,
            )
        except Exception as e:
            # Log an error message to indicate an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'run_startup_tasks' method from '{self.__class__.__name__}': {e}"
            )

            # Return None to indicate an exception has occurred
            return None, None, None
