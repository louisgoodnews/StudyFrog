"""
Author: lodego
Date: 2025-02-09
"""

import asyncio
import tkinter

from datetime import datetime
from typing import *

from core.learning.learning_session import (
    LearningSessionManager,
    LearningSessionModel,
    LearningSessionActionManager,
    LearningSessionActionModel,
    LearningSessionItemManager,
    LearningSessionItemModel,
)

from core.answer import AnswerFactory, AnswerManager, AnswerModel
from core.association import AssociationFactory, AssociationManager, AssociationModel
from core.change_history import (
    ChangeHistoryFactory,
    ChangeHistoryManager,
    ChangeHistoryModel,
    ChangeHistoryItemFactory,
    ChangeHistoryItemManager,
    ChangeHistoryItemModel,
)
from core.comment import CommentFactory, CommentManager, CommentModel
from core.custom_field import CustomFieldFactory, CustomFieldManager, CustomFieldModel
from core.default import DefaultFactory, DefaultManager, DefaultModel
from core.difficulty import DifficultyFactory, DifficultyManager, DifficultyModel
from core.flashcard import FlashcardFactory, FlashcardManager, FlashcardModel
from core.note import NoteFactory, NoteManager, NoteModel
from core.option import OptionFactory, OptionManager, OptionModel
from core.priority import PriorityFactory, PriorityManager, PriorityModel
from core.question import QuestionFactory, QuestionManager, QuestionModel
from core.setting import SettingFactory, SettingManager, SettingModel, SettingService
from core.stack import StackFactory, StackManager, StackModel
from core.status import StatusFactory, StatusManager, StatusModel
from core.tag import TagFactory, TagManager, TagModel
from core.user import UserFactory, UserManager, UserModel

from core.ui.calendar_ui import CalendarUI
from core.ui.create_ui import CreateUI
from core.ui.dashboard_ui import DashboardUI
from core.ui.edit_ui import EditUI
from core.ui.flashcards_view_ui import FlashcardsViewUI
from core.ui.help_ui import HelpUI
from core.ui.learning_dashboard_ui import LearningDashboardUI
from core.ui.learning_session_ui import LearningSessionUI
from core.ui.learning_session_result_ui import LearningSessionResultUI
from core.ui.menu_ui import MenuUI
from core.ui.notes_view_ui import NotesViewUI
from core.ui.notification_ui import NotificationUI
from core.ui.questions_view_ui import QuestionsViewUI
from core.ui.report_ui import ReportUI
from core.ui.search_ui import SearchUI
from core.ui.setting_ui import SettingUI
from core.ui.learning_stack_selection_ui import LearningStackSelectionUI
from core.ui.stacks_view_ui import StacksViewUI
from core.ui.statistics_view_ui import StatisticsViewUI
from core.ui.ui_registry import UIRegistry
from core.ui.user_ui import UserUI


from utils.constants import Constants
from utils.database_service import DatabaseService
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.miscellaneous import Miscellaneous
from utils.navigation import NavigationHistoryService
from utils.notification_service import NotificationService
from utils.object import ImmutableBaseObject
from utils.unified import (
    UnifiedObjectFactory,
    UnifiedObjectManager,
    UnifiedObjectService,
)


__all__: Final[List[str]] = ["BootstrapService"]


class BootstrapService(ImmutableBaseObject):
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
            cls._shared_instance = super(BootstrapService, cls).__new__(cls)
            cls._shared_instance.init()
        return cls._shared_instance

    def init(self) -> None:
        """
        Initializes the shared instance of the BootstrapService.

        This method is called when the shared instance is created, and it initializes
        the dispatcher, navigation service, setting service, unified object manager, and unified object service.

        Returns:
            None
        """

        # Initialize the dispatcher instance
        self.dispatcher: Dispatcher = Dispatcher()

        # Initialize the navigation service instance
        self.navigation_history_service: NavigationHistoryService = (
            NavigationHistoryService(dispatcher=self.dispatcher)
        )

        # Initialize the setting service instance
        self.setting_service: SettingService = SettingService()

        # Initialize the list of subscriptions
        self.subscriptions: List[str] = []

        # Initialize the notification service instance
        self.notification_service: NotificationService = NotificationService(
            dispatcher=self.dispatcher
        )

        # Initialize the unified object factory instance
        self.unified_object_factory: UnifiedObjectFactory = UnifiedObjectFactory()

        # Initialize the unified object manager instance
        self.unified_object_manager: UnifiedObjectManager = UnifiedObjectManager()

        # Initialize the unified object service instance
        self.unified_object_service: UnifiedObjectService = UnifiedObjectService(
            unified_manager=self.unified_object_manager
        )

    def create_default_answers(self) -> None:
        """
        Creates default answer entries in the database if they do not exist.

        This method checks for the existence of default answers in the database,
        and creates them if they are not found. It uses the unified object manager
        to retrieve and create default answers.
        """
        try:
            # Define a list of answer names
            answers: List[str] = [
                Constants.TRUE,
                Constants.FALSE,
            ]

            # Iterate over the answer names
            for answer in answers:
                # Check if the default answer exists in the database
                if not self.unified_object_manager.get_default_by(
                    field="name",
                    value=f"answer:{answer}",
                ):
                    # Create the default answer if it does not exist
                    self.unified_object_manager.create_default(
                        default=DefaultFactory.create_default(
                            name=f"answer:{answer}",
                            type="answer",
                            value=answer.capitalize(),
                        )
                    )

            # Retrieve the default answers from the database
            self.unified_object_manager.get_default_answers()
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_default_answers' method from '{self.__class__.__name__}': {e}"
            )

            # Raise the exception to the caller
            raise e

    def create_default_difficulties(self) -> None:
        """
        Creates default difficulty entries in the database if they do not exist.

        This method checks for the existence of default difficulties in the database,
        and creates them if they are not found. It uses the unified object manager
        to retrieve and create default difficulties.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while creating default difficulties.
        """
        try:
            # Define a list of difficulty names
            difficulties: List[str] = [
                Constants.HARD,
                Constants.MEDIUM,
                Constants.EASY,
            ]

            # Iterate over the difficulty names
            for difficulty in difficulties:
                # Check if the default difficulty exists in the database
                if not self.unified_object_manager.get_default_by(
                    field="name",
                    value=f"difficulty:{difficulty}",
                ):
                    # Create the default difficulty if it does not exist
                    self.unified_object_manager.create_default(
                        default=DefaultFactory.create_default(
                            name=f"difficulty:{difficulty}",
                            type="difficulty",
                            value=difficulty.capitalize(),
                        )
                    )

            # Retrieve the default difficulties from the database
            self.unified_object_manager.get_default_difficulties()
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_default_difficulties' method from '{self.__class__.__name__}': {e}"
            )

            # Raise the exception to the caller
            raise e

    def create_default_priorities(self) -> None:
        """
        Creates default priority entries in the database if they do not exist.

        This method checks for the existence of default priorities in the database,
        and creates them if they are not found. It uses the unified object manager
        to retrieve and create default priorities.

        Returns:
            None

        Raises:
            Exception: If an exception occurs while creating default priorities.
        """
        try:
            # Define a list of priority names
            priorities: List[str] = [
                Constants.HIGHEST,
                Constants.HIGH,
                Constants.MEDIUM,
                Constants.LOW,
                Constants.LOWEST,
            ]

            # Iterate over the priority names
            for priority in priorities:
                # Check if the default priority exists in the database
                if not self.unified_object_manager.get_default_by(
                    field="name",
                    value=f"priority:{priority}",
                ):
                    # Create the default priority if it does not exist
                    self.unified_object_manager.create_default(
                        default=DefaultFactory.create_default(
                            name=f"priority:{priority}",
                            type="priority",
                            value=priority.capitalize(),
                        )
                    )

            # Retrieve the default priorities from the database
            self.unified_object_manager.get_default_priorities()
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_default_priorities' method from '{self.__class__.__name__}': {e}"
            )

            # Raise the exception to the caller
            raise e

    def create_default_statuses(self) -> None:
        """
        Creates default status entries in the database if they do not exist.

        This method checks for the existence of default statuses in the database,
        and creates them if they are not found. It uses the unified object manager
        to retrieve and create default statuses.

        Raises:
            Exception: If an exception occurs while creating default statuses.
        """
        try:
            # Define a list of default status names
            statuses: List[str] = [
                Constants.NEW,
                Constants.LEARNING,
                Constants.REVIEW,
                Constants.COMPLETED,
            ]

            # Iterate over the status names
            for status in statuses:
                # Check if the default status exists in the database
                if not self.unified_object_manager.get_default_by(
                    field="name",
                    value=f"status:{status}",
                ):
                    # Create the default status if it does not exist
                    self.unified_object_manager.create_default(
                        default=DefaultFactory.create_default(
                            name=f"status:{status}",
                            type="status",
                            value=status.capitalize(),
                        )
                    )

            # Retrieve the default statuses from the database
            self.unified_object_manager.get_default_statuses()
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_default_statuses' method from '{self.__class__.__name__}': {e}"
            )

            # Raise the exception to the caller
            raise e

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
                CommentModel,
                DefaultModel,
                DifficultyModel,
                FlashcardModel,
                LearningSessionModel,
                LearningSessionActionModel,
                LearningSessionItemModel,
                NoteModel,
                OptionModel,
                PriorityModel,
                QuestionModel,
                SettingModel,
                StackModel,
                StatusModel,
                TagModel,
                UserModel,
            ]:
                # Log an info message indicating that the table is being created
                self.logger.info(
                    message=f"Attempting to create '{model_class.table}' table."
                )

                # Create the table
                asyncio.run(model_class.create_table(database=Constants.DATABASE_PATH))
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to create tables: {e}"
            )

            # Reraise the exception to the caller
            raise e

    def initialize_database_service(self) -> None:
        """
        Initializes the database service.

        This method is called when the shared instance of the BootstrapService is created,
        and it initializes the database service by calling the `DatabaseService` class.

        Returns:
            None
        """
        try:
            # Initialize the database service
            DatabaseService()
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to initialize database service: {e}"
            )

            # Reraise the exception to the caller
            raise e

    def register_factories(self) -> None:
        """ """
        try:
            factories: Dict[str, Type[Any]] = {
                "answer_factory": AnswerFactory,
                "association_factory": AssociationFactory,
                "change_history_factory": ChangeHistoryFactory,
                "change_history_item_factory": ChangeHistoryItemFactory,
                "comment_factory": CommentFactory,
                "custom_field_factory": CustomFieldFactory,
                "default_factory": DefaultFactory,
                "difficulty_factory": DifficultyFactory,
                "flashcard_factory": FlashcardFactory,
                "note_factory": NoteFactory,
                "option_factory": OptionFactory,
                "priority_factory": PriorityFactory,
                "question_factory": QuestionFactory,
                "setting_factory": SettingFactory,
                "stack_factory": StackFactory,
                "status_factory": StatusFactory,
                "tag_factory": TagFactory,
                "user_factory": UserFactory,
            }

            for (
                name,
                factory,
            ) in factories.items():
                self.unified_object_factory.register_factory(
                    factory=factory,
                    name=name,
                )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to register factories: {e}"
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
            # Store the subscription parameters in a list
            subscriptions: List[Dict[str, Any]] = [
                {
                    "event": Events.REQUEST_BACKWARD_NAVIGATION,
                    "function": self.navigation_history_service.on_request_backward_navigation,
                },
                {
                    "event": Events.REQUEST_FORWARD_NAVIGATION,
                    "function": self.navigation_history_service.on_request_forward_navigation,
                },
                {
                    "event": Events.REQUEST_ANSWER_CREATE,
                    "function": self.unified_object_service.on_request_answer_create,
                },
                {
                    "event": Events.REQUEST_ANSWER_DELETE,
                    "function": self.unified_object_service.on_request_answer_delete,
                },
                {
                    "event": Events.REQUEST_ANSWER_LOAD,
                    "function": self.unified_object_service.on_request_answer_load,
                },
                {
                    "event": Events.REQUEST_ANSWER_LOOKUP,
                    "function": self.unified_object_service.on_request_answer_lookup,
                },
                {
                    "event": Events.REQUEST_ANSWER_UPDATE,
                    "function": self.unified_object_service.on_request_answer_update,
                },
                {
                    "event": Events.REQUEST_ASSOCIATION_CREATE,
                    "function": self.unified_object_service.on_request_association_create,
                },
                {
                    "event": Events.REQUEST_ASSOCIATION_DELETE,
                    "function": self.unified_object_service.on_request_association_delete,
                },
                {
                    "event": Events.REQUEST_ASSOCIATION_LOAD,
                    "function": self.unified_object_service.on_request_association_load,
                },
                {
                    "event": Events.REQUEST_ASSOCIATION_LOOKUP,
                    "function": self.unified_object_service.on_request_association_lookup,
                },
                {
                    "event": Events.REQUEST_ASSOCIATION_UPDATE,
                    "function": self.unified_object_service.on_request_association_update,
                },
                {
                    "event": Events.REQUEST_CHANGE_HISTORY_CREATE,
                    "function": self.unified_object_service.on_request_change_history_create,
                },
                {
                    "event": Events.REQUEST_CHANGE_HISTORY_DELETE,
                    "function": self.unified_object_service.on_request_change_history_delete,
                },
                {
                    "event": Events.REQUEST_CHANGE_HISTORY_LOAD,
                    "function": self.unified_object_service.on_request_change_history_load,
                },
                {
                    "event": Events.REQUEST_CHANGE_HISTORY_LOOKUP,
                    "function": self.unified_object_service.on_request_change_history_lookup,
                },
                {
                    "event": Events.REQUEST_CHANGE_HISTORY_UPDATE,
                    "function": self.unified_object_service.on_request_change_history_update,
                },
                {
                    "event": Events.REQUEST_CHANGE_HISTORY_ITEM_CREATE,
                    "function": self.unified_object_service.on_request_change_history_item_create,
                },
                {
                    "event": Events.REQUEST_CHANGE_HISTORY_ITEM_DELETE,
                    "function": self.unified_object_service.on_request_change_history_item_delete,
                },
                {
                    "event": Events.REQUEST_CHANGE_HISTORY_ITEM_LOAD,
                    "function": self.unified_object_service.on_request_change_history_item_load,
                },
                {
                    "event": Events.REQUEST_CHANGE_HISTORY_ITEM_LOOKUP,
                    "function": self.unified_object_service.on_request_change_history_item_lookup,
                },
                {
                    "event": Events.REQUEST_CHANGE_HISTORY_ITEM_UPDATE,
                    "function": self.unified_object_service.on_request_change_history_item_update,
                },
                {
                    "event": Events.REQUEST_CUSTOM_FIELD_CREATE,
                    "function": self.unified_object_service.on_request_custom_field_create,
                },
                {
                    "event": Events.REQUEST_CUSTOM_FIELD_DELETE,
                    "function": self.unified_object_service.on_request_custom_field_delete,
                },
                {
                    "event": Events.REQUEST_CUSTOM_FIELD_LOAD,
                    "function": self.unified_object_service.on_request_custom_field_load,
                },
                {
                    "event": Events.REQUEST_CUSTOM_FIELD_LOOKUP,
                    "function": self.unified_object_service.on_request_custom_field_lookup,
                },
                {
                    "event": Events.REQUEST_CUSTOM_FIELD_UPDATE,
                    "function": self.unified_object_service.on_request_custom_field_update,
                },
                {
                    "event": Events.REQUEST_DIFFICULTY_CREATE,
                    "function": self.unified_object_service.on_request_difficulty_create,
                },
                {
                    "event": Events.REQUEST_DIFFICULTY_DELETE,
                    "function": self.unified_object_service.on_request_difficulty_delete,
                },
                {
                    "event": Events.REQUEST_DIFFICULTY_LOAD,
                    "function": self.unified_object_service.on_request_difficulty_load,
                },
                {
                    "event": Events.REQUEST_DIFFICULTY_LOOKUP,
                    "function": self.unified_object_service.on_request_difficulty_lookup,
                },
                {
                    "event": Events.REQUEST_DIFFICULTY_UPDATE,
                    "function": self.unified_object_service.on_request_difficulty_update,
                },
                {
                    "event": Events.REQUEST_FLASHCARD_CREATE,
                    "function": self.unified_object_service.on_request_flashcard_create,
                },
                {
                    "event": Events.REQUEST_FLASHCARD_DELETE,
                    "function": self.unified_object_service.on_request_flashcard_delete,
                },
                {
                    "event": Events.REQUEST_FLASHCARD_LOAD,
                    "function": self.unified_object_service.on_request_flashcard_load,
                },
                {
                    "event": Events.REQUEST_FLASHCARD_LOOKUP,
                    "function": self.unified_object_service.on_request_flashcard_lookup,
                },
                {
                    "event": Events.REQUEST_FLASHCARD_UPDATE,
                    "function": self.unified_object_service.on_request_flashcard_update,
                },
                {
                    "event": Events.REQUEST_GET_ALL_ANSWERS,
                    "function": self.unified_object_service.on_request_get_all_answers,
                },
                {
                    "event": Events.REQUEST_GET_ALL_ASSOCIATIONS,
                    "function": self.unified_object_service.on_request_get_all_associations,
                },
                {
                    "event": Events.REQUEST_GET_ALL_CUSTOM_FIELDS,
                    "function": self.unified_object_service.on_request_get_all_custom_fields,
                },
                {
                    "event": Events.REQUEST_GET_ALL_DEFAULTS,
                    "function": self.unified_object_service.on_request_get_all_defaults,
                },
                {
                    "event": Events.REQUEST_GET_ALL_DIFFICULTIES,
                    "function": self.unified_object_service.on_request_get_all_difficulties,
                },
                {
                    "event": Events.REQUEST_GET_ALL_FLASHCARDS,
                    "function": self.unified_object_service.on_request_get_all_flashcards,
                },
                {
                    "event": Events.REQUEST_GET_ALL_NOTES,
                    "function": self.unified_object_service.on_request_get_all_notes,
                },
                {
                    "event": Events.REQUEST_GET_ALL_OPTIONS,
                    "function": self.unified_object_service.on_request_get_all_options,
                },
                {
                    "event": Events.REQUEST_GET_ALL_PRIORITIES,
                    "function": self.unified_object_service.on_request_get_all_priorities,
                },
                {
                    "event": Events.REQUEST_GET_ALL_QUESTIONS,
                    "function": self.unified_object_service.on_request_get_all_questions,
                },
                {
                    "event": Events.REQUEST_GET_ALL_SETTINGS,
                    "function": self.unified_object_service.on_request_get_all_settings,
                },
                {
                    "event": Events.REQUEST_GET_ALL_STACKS,
                    "function": self.unified_object_service.on_request_get_all_stacks,
                },
                {
                    "event": Events.REQUEST_GET_ALL_STATUSES,
                    "function": self.unified_object_service.on_request_get_all_statuses,
                },
                {
                    "event": Events.REQUEST_GET_ALL_USERS,
                    "function": self.unified_object_service.on_request_get_all_users,
                },
                {
                    "event": Events.REQUEST_GET_BY_KEY,
                    "function": self.unified_object_service.on_request_get_by_key,
                },
                {
                    "event": Events.REQUEST_GET_BY_KEYS,
                    "function": self.unified_object_service.on_request_get_by_keys,
                },
                {
                    "event": Events.REQUEST_LEARNING_SESSION_CREATE,
                    "function": self.unified_object_service.on_request_learning_session_create,
                },
                {
                    "event": Events.REQUEST_LEARNING_SESSION_DELETE,
                    "function": self.unified_object_service.on_request_learning_session_delete,
                },
                {
                    "event": Events.REQUEST_LEARNING_SESSION_LOAD,
                    "function": self.unified_object_service.on_request_learning_session_load,
                },
                {
                    "event": Events.REQUEST_LEARNING_SESSION_LOOKUP,
                    "function": self.unified_object_service.on_request_learning_session_lookup,
                },
                {
                    "event": Events.REQUEST_LEARNING_SESSION_UPDATE,
                    "function": self.unified_object_service.on_request_learning_session_update,
                },
                {
                    "event": Events.REQUEST_LEARNING_SESSION_ACTION_CREATE,
                    "function": self.unified_object_service.on_request_learning_session_action_create,
                },
                {
                    "event": Events.REQUEST_LEARNING_SESSION_ACTION_DELETE,
                    "function": self.unified_object_service.on_request_learning_session_action_delete,
                },
                {
                    "event": Events.REQUEST_LEARNING_SESSION_ACTION_LOAD,
                    "function": self.unified_object_service.on_request_learning_session_action_load,
                },
                {
                    "event": Events.REQUEST_LEARNING_SESSION_ACTION_LOOKUP,
                    "function": self.unified_object_service.on_request_learning_session_action_lookup,
                },
                {
                    "event": Events.REQUEST_LEARNING_SESSION_ACTION_UPDATE,
                    "function": self.unified_object_service.on_request_learning_session_action_update,
                },
                {
                    "event": Events.REQUEST_LEARNING_SESSION_ITEM_CREATE,
                    "function": self.unified_object_service.on_request_learning_session_item_create,
                },
                {
                    "event": Events.REQUEST_LEARNING_SESSION_ITEM_DELETE,
                    "function": self.unified_object_service.on_request_learning_session_item_delete,
                },
                {
                    "event": Events.REQUEST_LEARNING_SESSION_ITEM_LOAD,
                    "function": self.unified_object_service.on_request_learning_session_item_load,
                },
                {
                    "event": Events.REQUEST_LEARNING_SESSION_ITEM_LOOKUP,
                    "function": self.unified_object_service.on_request_learning_session_item_lookup,
                },
                {
                    "event": Events.REQUEST_LEARNING_SESSION_ITEM_UPDATE,
                    "function": self.unified_object_service.on_request_learning_session_item_update,
                },
                {
                    "event": Events.REQUEST_NOTE_CREATE,
                    "function": self.unified_object_service.on_request_note_create,
                },
                {
                    "event": Events.REQUEST_NOTE_DELETE,
                    "function": self.unified_object_service.on_request_note_delete,
                },
                {
                    "event": Events.REQUEST_NOTE_LOAD,
                    "function": self.unified_object_service.on_request_note_load,
                },
                {
                    "event": Events.REQUEST_NOTE_LOOKUP,
                    "function": self.unified_object_service.on_request_note_lookup,
                },
                {
                    "event": Events.REQUEST_NOTE_UPDATE,
                    "function": self.unified_object_service.on_request_note_update,
                },
                {
                    "event": Events.REQUEST_OPTION_CREATE,
                    "function": self.unified_object_service.on_request_option_create,
                },
                {
                    "event": Events.REQUEST_OPTION_DELETE,
                    "function": self.unified_object_service.on_request_option_delete,
                },
                {
                    "event": Events.REQUEST_OPTION_LOAD,
                    "function": self.unified_object_service.on_request_option_load,
                },
                {
                    "event": Events.REQUEST_OPTION_LOOKUP,
                    "function": self.unified_object_service.on_request_option_lookup,
                },
                {
                    "event": Events.REQUEST_OPTION_UPDATE,
                    "function": self.unified_object_service.on_request_option_update,
                },
                {
                    "event": Events.REQUEST_PRIORITY_CREATE,
                    "function": self.unified_object_service.on_request_priority_create,
                },
                {
                    "event": Events.REQUEST_PRIORITY_DELETE,
                    "function": self.unified_object_service.on_request_priority_delete,
                },
                {
                    "event": Events.REQUEST_PRIORITY_LOAD,
                    "function": self.unified_object_service.on_request_priority_load,
                },
                {
                    "event": Events.REQUEST_PRIORITY_LOOKUP,
                    "function": self.unified_object_service.on_request_priority_lookup,
                },
                {
                    "event": Events.REQUEST_PRIORITY_UPDATE,
                    "function": self.unified_object_service.on_request_priority_update,
                },
                {
                    "event": Events.REQUEST_QUESTION_CREATE,
                    "function": self.unified_object_service.on_request_question_create,
                },
                {
                    "event": Events.REQUEST_QUESTION_DELETE,
                    "function": self.unified_object_service.on_request_question_delete,
                },
                {
                    "event": Events.REQUEST_QUESTION_LOAD,
                    "function": self.unified_object_service.on_request_question_load,
                },
                {
                    "event": Events.REQUEST_QUESTION_LOOKUP,
                    "function": self.unified_object_service.on_request_question_lookup,
                },
                {
                    "event": Events.REQUEST_QUESTION_UPDATE,
                    "function": self.unified_object_service.on_request_question_update,
                },
                {
                    "event": Events.REQUEST_SETTING_CREATE,
                    "function": self.unified_object_service.on_request_setting_create,
                },
                {
                    "event": Events.REQUEST_SETTING_DELETE,
                    "function": self.unified_object_service.on_request_setting_delete,
                },
                {
                    "event": Events.REQUEST_SETTING_LOAD,
                    "function": self.unified_object_service.on_request_setting_load,
                },
                {
                    "event": Events.REQUEST_SETTING_LOOKUP,
                    "function": self.unified_object_service.on_request_setting_lookup,
                },
                {
                    "event": Events.REQUEST_SETTING_UPDATE,
                    "function": self.unified_object_service.on_request_setting_update,
                },
                {
                    "event": Events.REQUEST_STACK_CREATE,
                    "function": self.unified_object_service.on_request_stack_create,
                },
                {
                    "event": Events.REQUEST_STACK_DELETE,
                    "function": self.unified_object_service.on_request_stack_delete,
                },
                {
                    "event": Events.REQUEST_STACK_LOAD,
                    "function": self.unified_object_service.on_request_stack_load,
                },
                {
                    "event": Events.REQUEST_STACK_LOOKUP,
                    "function": self.unified_object_service.on_request_stack_lookup,
                },
                {
                    "event": Events.REQUEST_STACK_UPDATE,
                    "function": self.unified_object_service.on_request_stack_update,
                },
                {
                    "event": Events.REQUEST_STATUS_CREATE,
                    "function": self.unified_object_service.on_request_status_create,
                },
                {
                    "event": Events.REQUEST_STATUS_DELETE,
                    "function": self.unified_object_service.on_request_status_delete,
                },
                {
                    "event": Events.REQUEST_STATUS_LOAD,
                    "function": self.unified_object_service.on_request_status_load,
                },
                {
                    "event": Events.REQUEST_STATUS_LOOKUP,
                    "function": self.unified_object_service.on_request_status_lookup,
                },
                {
                    "event": Events.REQUEST_STATUS_UPDATE,
                    "function": self.unified_object_service.on_request_status_update,
                },
                {
                    "event": Events.REQUEST_TAG_CREATE,
                    "function": self.unified_object_service.on_request_tag_create,
                },
                {
                    "event": Events.REQUEST_TAG_DELETE,
                    "function": self.unified_object_service.on_request_tag_delete,
                },
                {
                    "event": Events.REQUEST_TAG_LOAD,
                    "function": self.unified_object_service.on_request_tag_load,
                },
                {
                    "event": Events.REQUEST_TAG_LOOKUP,
                    "function": self.unified_object_service.on_request_tag_lookup,
                },
                {
                    "event": Events.REQUEST_TAG_UPDATE,
                    "function": self.unified_object_service.on_request_tag_update,
                },
                {
                    "event": Events.REQUEST_UPDATE,
                    "function": self.unified_object_service.on_request_update,
                },
                {
                    "event": Events.REQUEST_UPDATE_IN_BULK,
                    "function": self.unified_object_service.on_request_update_in_bulk,
                },
                {
                    "event": Events.REQUEST_USER_CREATE,
                    "function": self.unified_object_service.on_request_user_create,
                },
                {
                    "event": Events.REQUEST_USER_DELETE,
                    "function": self.unified_object_service.on_request_user_delete,
                },
                {
                    "event": Events.REQUEST_USER_LOAD,
                    "function": self.unified_object_service.on_request_user_load,
                },
                {
                    "event": Events.REQUEST_USER_LOOKUP,
                    "function": self.unified_object_service.on_request_user_lookup,
                },
                {
                    "event": Events.REQUEST_USER_UPDATE,
                    "function": self.unified_object_service.on_request_user_update,
                },
            ]

            # Iterate over the list
            for subscription in subscriptions:
                # Register the subscription and append the UUID code to the subscriptions list
                self.subscriptions.append(
                    # Register the function
                    self.dispatcher.register(
                        event=subscription["event"],
                        function=subscription["function"],
                        namespace=Constants.GLOBAL_NAMESPACE,
                        persistent=True,
                    )
                )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'register_handlers' method from '{self.__class__.__name__}': {e}"
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
                "comment_manager": CommentManager,
                "custom_field_manager": CustomFieldManager,
                "default_manager": DefaultManager,
                "difficulty_manager": DifficultyManager,
                "flashcard_manager": FlashcardManager,
                "learning_session_manager": LearningSessionManager,
                "learning_session_action_manager": LearningSessionActionManager,
                "learning_session_item_manager": LearningSessionItemManager,
                "note_manager": NoteManager,
                "option_manager": OptionManager,
                "priority_manager": PriorityManager,
                "question_manager": QuestionManager,
                "setting_manager": SettingManager,
                "stack_manager": StackManager,
                "status_manager": StatusManager,
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
                "flashcards_view_ui": FlashcardsViewUI,
                "help_ui": HelpUI,
                "learning_dashboard_ui": LearningDashboardUI,
                "learning_session_ui": LearningSessionUI,
                "learning_session_result_ui": LearningSessionResultUI,
                "menu_ui": MenuUI,
                "notes_view_ui": NotesViewUI,
                "notification_ui": NotificationUI,
                "questions_view_ui": QuestionsViewUI,
                "report_ui": ReportUI,
                "search_ui": SearchUI,
                "setting_ui": SettingUI,
                "learning_stack_selection_ui": LearningStackSelectionUI,
                "stacks_view_ui": StacksViewUI,
                "statistics_view_ui": StatisticsViewUI,
                "user_ui": UserUI,
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

    def run_shutdown_tasks(self) -> None:
        """
        Runs shutdown tasks.

        This method performs any necessary cleanup tasks after the application has
        finished running. It typically includes closing databases or other resources.

        Returns:
            None
        """
        try:
            # Get the current datetime
            start: datetime = Miscellaneous.get_current_datetime()

            # Log an info message about running shutdown tasks
            self.logger.info(message="Running shutdown tasks....")

            # Unregister all event handlers from the dispatcher
            self.unregister_handlers()

            # Get the current datetime
            end: datetime = Miscellaneous.get_current_datetime()

            # Calculate the duration
            duration: float = (end - start).total_seconds()

            # Log an info message about completing shutdown tasks
            self.logger.info(
                message=f"Shutdown tasks completed in {duration:.2f} seconds."
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'run_shutdown_tasks' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def run_startup_tasks(
        self,
    ) -> Tuple[
        Optional[Dispatcher],
        Optional[NavigationHistoryService],
        Optional[NotificationService],
        Optional[SettingService],
        Optional[UnifiedObjectFactory],
        Optional[UnifiedObjectManager],
        Optional[UnifiedObjectService],
    ]:
        """
        Executes startup tasks for the application.

        This method registers UI menus and returns initialized instances of
        dispatcher, navigation service, notification service, setting service,
        unified object manager, and unified object service.

        Returns:
            Tuple[Optional[Dispatcher], Optional[NavigationHistoryService], Optional[NotificationService], Optional[SettingService], Optional[UnifiedObjectFactory], Optional[UnifiedObjectManager], Optional[UnifiedObjectService]]:
            A tuple containing the dispatcher, navigation service, setting service,
            unified object factory, unified object manager, and unified object service instances, or None
            values if an exception occurs.

        Raises:
            Exception: If an exception occurs while running the startup tasks.
        """
        try:
            # Get the current datetime
            start: datetime = Miscellaneous.get_current_datetime()

            # Log an info message about running startup tasks
            self.logger.info(message="Running startup tasks....")

            # Initialize the database service
            self.initialize_database_service()

            # Create the database tables
            self.create_tables()

            # Register the factories with the UnifiedObjectFactory
            self.register_factories()

            # Register the managers with the UnifiedObjectManager
            self.register_managers()

            # Register the event handlers
            self.register_handlers()

            # Register the menus with the UIRegistry
            self.register_menus()

            # Create the default answers
            self.create_default_answers()

            # Create the default difficulties
            self.create_default_difficulties()

            # Create the default priorities
            self.create_default_priorities()

            # Create the default statuses
            self.create_default_statuses()

            # Get the current datetime
            end: datetime = Miscellaneous.get_current_datetime()

            # Calculate the duration
            duration: float = (end - start).total_seconds()

            # Log an info message about completing startup tasks
            self.logger.info(
                message=f"Startup tasks completed in {duration:.2f} seconds."
            )

            # Return the dispatcher, navigation service, notification service, setting service, and unified object manager instances
            return (
                self.dispatcher,
                self.navigation_history_service,
                self.notification_service,
                self.setting_service,
                self.unified_object_factory,
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

    def unregister_handlers(self) -> None:
        """
        Unregisters all event handlers from the dispatcher.

        This method iterates over all subscriptions and unregisters each one
        by calling the dispatcher's `unregister` method with the UUID.

        Returns:
            None

        Raises:
            Exception: If an exception occurs during the unregistration process.
        """
        try:
            # Iterate over each subscription's UUID
            for uuid in self.subscriptions:
                # Unregister the handler for the given UUID
                self.dispatcher.unregister(uuid=uuid)
        except Exception as e:
            # Log an error message to indicate an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'unregister_handlers' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e
