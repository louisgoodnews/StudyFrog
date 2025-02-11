"""
Author: lodego
Date: 2025-02-09
"""

import asyncio

import tkinter

from typing import *

from core.answer import AnswerManager, AnswerModel
from core.association import AssociationManager, AssociationModel
from core.change_history import (
    ChangeHistoryManager,
    ChangeHistoryModel,
    ChangeHistoryItemManager,
    ChangeHistoryItemModel,
)
from core.custom_field import CustomFieldManager, CustomFieldModel
from core.default import DefaultManager, DefaultModel
from core.difficulty import DifficultyManager, DifficultyModel
from core.flashcard import FlashcardManager, FlashcardModel
from core.note import NoteManager, NoteModel
from core.option import OptionManager, OptionModel
from core.priority import PriorityManager, PriorityModel
from core.question import QuestionManager, QuestionModel
from core.setting import SettingManager, SettingModel, SettingService
from core.stack import StackManager, StackModel
from core.tag import TagManager, TagModel
from core.user import UserManager, UserModel

from core.ui.calendar_ui import CalendarUI
from core.ui.create_ui import CreateUI
from core.ui.dashboard_ui import DashboardUI
from core.ui.edit_ui import EditUI
from core.ui.report_ui import ReportUI
from core.ui.search_ui import SearchUI
from core.ui.setting_ui import SettingUI
from core.ui.ui_registry import UIRegistry

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.logger import Logger
from utils.navigation import NavigationHistoryService
from utils.unified import UnifiedObjectManager, UnifiedObjectService


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
        navigation_service (NavigationHistoryService): The service for handling navigation.
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
        the logger, dispatcher, navigation service, setting service, unified object manager, and unified object service.

        Returns:
            None
        """

        # Initialize a logger instance
        self.logger = Logger.get_logger(name=self.__class__.__name__)

        # Initialize the dispatcher instance
        self.dispatcher: Dispatcher = Dispatcher()

        # Initialize the navigation service instance
        self.navigation_history_service: NavigationHistoryService = (
            NavigationHistoryService(dispatcher=self.dispatcher)
        )

        # Initialize the setting service instance
        self.setting_service: SettingService = SettingService()

        # Initialize the unified object manager instance
        self.unified_object_manager: UnifiedObjectManager = UnifiedObjectManager()

        # Initialize the unified object service instance
        self.unified_object_service: UnifiedObjectService = UnifiedObjectService(
            unifiec_manager=self.unified_object_manager
        )

    def create_tables(self) -> None:
        """
        Creates the tables for the models in the database if they do not exist.

        This method is used to create the tables for the models in the database
        if they do not exist. It iterates over the defined models and then creates the table.

        If an exception occurs while running the method, it logs an error message
        indicating the exception and then reraises the exception to the caller.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while running the method.
        """
        try:
            # Iterate over the defined models and create the tables
            for model_class in [
                AnswerModel,
                AssociationModel,
                ChangeHistoryItemModel,
                ChangeHistoryModel,
                CustomFieldModel,
                DefaultModel,
                DifficultyModel,
                FlashcardModel,
                NoteModel,
                OptionModel,
                PriorityModel,
                QuestionModel,
                SettingModel,
                StackModel,
                TagModel,
                UserModel,
            ]:
                # Create the table
                asyncio.run(model_class.create_table(database=Constants.DATABASE_PATH))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to create tables: {e}"
            )

            # Reraise the exception to the caller
            raise e

    def register_handlers(self) -> None:
        """
        Registers functions to be called when certain events are dispatched.

        This method registers functions with the Dispatcher to be called when
        certain events are dispatched. The functions are registered with the
        Dispatcher and provide a way to handle events in a centralized manner.

        Returns:
            None
        """
        try:
            # Store the subscription parameters in a nested list
            subscriptions: List[List[Any]] = [
                [
                    Events.REQUEST_BACKWARD_NAVIGATION,
                    self.navigation_history_service.on_request_backward_navigation,
                ],
                [
                    Events.REQUEST_FORWARD_NAVIGATION,
                    self.navigation_history_service.on_request_forward_navigation,
                ],
                [
                    Events.REQUEST_ANSWER_CREATE,
                    self.unified_object_service.on_request_answer_create,
                ],
                [
                    Events.REQUEST_ANSWER_DELETE,
                    self.unified_object_service.on_request_answer_delete,
                ],
                [
                    Events.REQUEST_ANSWER_LOAD,
                    self.unified_object_service.on_request_answer_load,
                ],
                [
                    Events.REQUEST_ANSWER_UPDATE,
                    self.unified_object_service.on_request_answer_update,
                ],
                [
                    Events.REQUEST_ASSOCIATION_CREATE,
                    self.unified_object_service.on_request_association_create,
                ],
                [
                    Events.REQUEST_ASSOCIATION_DELETE,
                    self.unified_object_service.on_request_association_delete,
                ],
                [
                    Events.REQUEST_ASSOCIATION_LOAD,
                    self.unified_object_service.on_request_association_load,
                ],
                [
                    Events.REQUEST_ASSOCIATION_UPDATE,
                    self.unified_object_service.on_request_association_update,
                ],
                [
                    Events.REQUEST_CHANGE_HISTORY_CREATE,
                    self.unified_object_service.on_request_change_history_create,
                ],
                [
                    Events.REQUEST_CHANGE_HISTORY_DELETE,
                    self.unified_object_service.on_request_change_history_delete,
                ],
                [
                    Events.REQUEST_CHANGE_HISTORY_LOAD,
                    self.unified_object_service.on_request_change_history_load,
                ],
                [
                    Events.REQUEST_CHANGE_HISTORY_UPDATE,
                    self.unified_object_service.on_request_change_history_update,
                ],
                [
                    Events.REQUEST_CHANGE_HISTORY_ITEM_CREATE,
                    self.unified_object_service.on_request_change_history_item_create,
                ],
                [
                    Events.REQUEST_CHANGE_HISTORY_ITEM_DELETE,
                    self.unified_object_service.on_request_change_history_item_delete,
                ],
                [
                    Events.REQUEST_CHANGE_HISTORY_ITEM_LOAD,
                    self.unified_object_service.on_request_change_history_item_load,
                ],
                [
                    Events.REQUEST_CHANGE_HISTORY_ITEM_UPDATE,
                    self.unified_object_service.on_request_change_history_item_update,
                ],
                [
                    Events.REQUEST_CUSTOM_FIELD_CREATE,
                    self.unified_object_service.on_request_custom_field_create,
                ],
                [
                    Events.REQUEST_CUSTOM_FIELD_DELETE,
                    self.unified_object_service.on_request_custom_field_delete,
                ],
                [
                    Events.REQUEST_CUSTOM_FIELD_LOAD,
                    self.unified_object_service.on_request_custom_field_load,
                ],
                [
                    Events.REQUEST_CUSTOM_FIELD_UPDATE,
                    self.unified_object_service.on_request_custom_field_update,
                ],
                [
                    Events.REQUEST_DIFFICULTY_CREATE,
                    self.unified_object_service.on_request_difficulty_create,
                ],
                [
                    Events.REQUEST_DIFFICULTY_DELETE,
                    self.unified_object_service.on_request_difficulty_delete,
                ],
                [
                    Events.REQUEST_DIFFICULTY_LOAD,
                    self.unified_object_service.on_request_difficulty_load,
                ],
                [
                    Events.REQUEST_DIFFICULTY_UPDATE,
                    self.unified_object_service.on_request_difficulty_update,
                ],
                [
                    Events.REQUEST_FLASHCARD_CREATE,
                    self.unified_object_service.on_request_flashcard_create,
                ],
                [
                    Events.REQUEST_FLASHCARD_DELETE,
                    self.unified_object_service.on_request_flashcard_delete,
                ],
                [
                    Events.REQUEST_FLASHCARD_LOAD,
                    self.unified_object_service.on_request_flashcard_load,
                ],
                [
                    Events.REQUEST_FLASHCARD_UPDATE,
                    self.unified_object_service.on_request_flashcard_update,
                ],
                [
                    Events.REQUEST_NOTE_CREATE,
                    self.unified_object_service.on_request_note_create,
                ],
                [
                    Events.REQUEST_NOTE_DELETE,
                    self.unified_object_service.on_request_note_delete,
                ],
                [
                    Events.REQUEST_NOTE_LOAD,
                    self.unified_object_service.on_request_note_load,
                ],
                [
                    Events.REQUEST_NOTE_UPDATE,
                    self.unified_object_service.on_request_note_update,
                ],
                [
                    Events.REQUEST_OPTION_CREATE,
                    self.unified_object_service.on_request_option_create,
                ],
                [
                    Events.REQUEST_OPTION_DELETE,
                    self.unified_object_service.on_request_option_delete,
                ],
                [
                    Events.REQUEST_OPTION_LOAD,
                    self.unified_object_service.on_request_option_load,
                ],
                [
                    Events.REQUEST_OPTION_UPDATE,
                    self.unified_object_service.on_request_option_update,
                ],
                [
                    Events.REQUEST_PRIORITY_CREATE,
                    self.unified_object_service.on_request_priority_create,
                ],
                [
                    Events.REQUEST_PRIORITY_DELETE,
                    self.unified_object_service.on_request_priority_delete,
                ],
                [
                    Events.REQUEST_PRIORITY_LOAD,
                    self.unified_object_service.on_request_priority_load,
                ],
                [
                    Events.REQUEST_PRIORITY_UPDATE,
                    self.unified_object_service.on_request_priority_update,
                ],
                [
                    Events.REQUEST_QUESTION_CREATE,
                    self.unified_object_service.on_request_question_create,
                ],
                [
                    Events.REQUEST_QUESTION_DELETE,
                    self.unified_object_service.on_request_question_delete,
                ],
                [
                    Events.REQUEST_QUESTION_LOAD,
                    self.unified_object_service.on_request_question_load,
                ],
                [
                    Events.REQUEST_QUESTION_UPDATE,
                    self.unified_object_service.on_request_question_update,
                ],
                [
                    Events.REQUEST_SETTING_CREATE,
                    self.setting_service.on_request_setting_create,
                ],
                [
                    Events.REQUEST_SETTING_DELETE,
                    self.setting_service.on_request_setting_delete,
                ],
                [
                    Events.REQUEST_SETTING_LOAD,
                    self.setting_service.on_request_setting_load,
                ],
                [
                    Events.REQUEST_SETTING_UPDATE,
                    self.setting_service.on_request_setting_update,
                ],
                [
                    Events.REQUEST_STACK_CREATE,
                    self.unified_object_service.on_request_stack_create,
                ],
                [
                    Events.REQUEST_STACK_DELETE,
                    self.unified_object_service.on_request_stack_delete,
                ],
                [
                    Events.REQUEST_STACK_LOAD,
                    self.unified_object_service.on_request_stack_load,
                ],
                [
                    Events.REQUEST_STACK_UPDATE,
                    self.unified_object_service.on_request_stack_update,
                ],
                [
                    Events.REQUEST_TAG_CREATE,
                    self.unified_object_service.on_request_tag_create,
                ],
                [
                    Events.REQUEST_TAG_DELETE,
                    self.unified_object_service.on_request_tag_delete,
                ],
                [
                    Events.REQUEST_TAG_LOAD,
                    self.unified_object_service.on_request_tag_load,
                ],
                [
                    Events.REQUEST_TAG_UPDATE,
                    self.unified_object_service.on_request_tag_update,
                ],
                [
                    Events.REQUEST_USER_CREATE,
                    self.unified_object_service.on_request_user_create,
                ],
                [
                    Events.REQUEST_USER_DELETE,
                    self.unified_object_service.on_request_user_delete,
                ],
                [
                    Events.REQUEST_USER_LOAD,
                    self.unified_object_service.on_request_user_load,
                ],
                [
                    Events.REQUEST_USER_UPDATE,
                    self.unified_object_service.on_request_user_update,
                ],
            ]

            # Iterate over the list
            for subscription in subscriptions:
                # Register the function
                self.dispatcher.register(
                    event=subscription[0],
                    function=subscription[1],
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
                "calendar_ui": CalendarUI,
                "create_ui": CreateUI,
                "dashboard_ui": DashboardUI,
                "edit_ui": EditUI,
                "report_ui": ReportUI,
                "search_ui": SearchUI,
                "setting_ui": SettingUI,
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
        Registers the managers with the UnifiedObjectManager.

        This method registers all manager classes with the UnifiedObjectManager,
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

            # Iterate over the managers and register each one with the UnifiedObjectManager
            for (
                name,
                manager,
            ) in managers.items():
                # Register the manager with the UnifiedObjectManager
                self.unified_object_manager.register_manager(
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
        Optional[NavigationHistoryService],
        Optional[SettingService],
        Optional[UnifiedObjectManager],
        Optional[UnifiedObjectService],
    ]:
        """
        Executes startup tasks for the application.

        This method registers UI menus and returns initialized instances of
        dispatcher, navigation service, and setting service.

        Returns:
            Tuple[Optional[Dispatcher], Optional[NavigationHistoryService], Optional[SettingService], Optional[UnifiedObjectManager], Optional[UnifiedObjectService]]:
            A tuple containing the dispatcher, navigation service, setting service,
            unified object manager, and unified object service instances, or None
            values if an exception occurs.

        Raises:
            Exception: If an exception occurs while running the startup tasks.
        """
        try:
            # Create the database tables
            self.create_tables()

            # Register the managers with the UnifiedObjectManager
            self.register_managers()

            # Register the event handlers
            self.register_handlers()

            # Register the menus with the UIRegistry
            self.register_menus()

            # Return the dispatcher, navigation service, setting service, and unified object manager instances
            return (
                self.dispatcher,
                self.navigation_history_service,
                self.setting_service,
                self.unified_object_manager,
                self.unified_object_service,
            )
        except Exception as e:
            # Log an error message to indicate an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'run_startup_tasks' method from '{self.__class__.__name__}': {e}"
            )

            # Return None to indicate an exception has occurred
            return None, None, None, None, None
