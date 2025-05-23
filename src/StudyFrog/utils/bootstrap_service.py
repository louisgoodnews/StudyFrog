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
from core.subject import SubjectFactory, SubjectManager, SubjectModel
from core.tag import TagFactory, TagManager, TagModel
from core.teacher import TeacherFactory, TeacherManager, TeacherModel
from core.user import UserFactory, UserManager, UserModel

from core.ui.calendar_ui import CalendarUI
from core.ui.create_ui import CreateUI
from core.ui.dashboard_ui import DashboardUI
from core.ui.edit_ui import EditUI
from core.ui.flashcards_view_ui import FlashcardsViewUI
from core.ui.help_ui import HelpUI
from core.ui.learning_dashboard_ui import LearningDashboardUI
from core.ui.learning_session_ui import LearningSessionUI
from core.ui.learning_session_recall_ui import LearningSessionRecallUI
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
            dispatcher=self.dispatcher,
            unified_manager=self.unified_object_manager,
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
                Constants.CORRECT,
                Constants.INCORRECT,
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
                SubjectModel,
                TagModel,
                TeacherModel,
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
                "subject_factory": SubjectFactory,
                "tag_factory": TagFactory,
                "teacher_factory": TeacherFactory,
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
                "subject_manager": SubjectManager,
                "tag_manager": TagManager,
                "teacher_manager": TeacherManager,
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
                "learning_session_recall_ui": LearningSessionRecallUI,
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
