"""
Author: lodego
Date: 2025-03-15
"""

import traceback

from typing import *

from core.answer import AnswerFactory, AnswerManager
from core.association import AssociationFactory, AssociationManager
from core.change_history import (
    ChangeHistoryFactory,
    ChangeHistoryManager,
    ChangeHistoryItemFactory,
    ChangeHistoryItemManager,
)
from core.comment import CommentFactory, CommentManager
from core.custom_field import CustomFieldFactory, CustomFieldManager
from core.default import DefaultFactory, DefaultManager
from core.difficulty import DifficultyFactory, DifficultyManager
from core.flashcard import FlashcardFactory, FlashcardManager
from core.note import NoteFactory, NoteManager
from core.priority import PriorityFactory, PriorityManager
from core.question import QuestionFactory, QuestionManager
from core.setting import SettingFactory, SettingManager
from core.stack import StackFactory, StackManager
from core.status import StatusFactory, StatusManager
from core.subject import SubjectFactory, SubjectManager
from core.tag import TagFactory, TagManager
from core.teacher import TeacherFactory, TeacherManager
from core.user import UserFactory, UserManager

from utils.dispatcher import Dispatcher
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous
from utils.unified import UnifiedObjectFactory, UnifiedObjectManager


__all__: Final[List[str]] = ["ComponentAccessor"]


class ComponentAccessor:
    """
    This class provides methods to access manager instances for various components in the StudyFrog application.

    Attributes:
        logger (Logger): The logger instance associated with the ComponentAccessor class.
        answer_manager (AnswerManager): The answer manager instance.
        association_manager (AssociationManager): The association manager instance.
        change_history_manager (ChangeHistoryManager): The change history manager instance.
        change_history_item_manager (ChangeHistoryItemManager): The change history item manager instance.
        comment_manager (CommentManager): The comment manager instance.
        custom_field_manager (CustomFieldManager): The custom field manager instance.
        default_manager (DefaultManager): The default manager instance.
        difficulty_manager (DifficultyManager): The difficulty manager instance.
        flashcard_manager (FlashcardManager): The flashcard manager instance.
        note_manager (NoteManager): The note manager instance.
        priority_manager (PriorityManager): The priority manager instance.
        question_manager (QuestionManager): The question manager instance.
        setting_manager (SettingManager): The setting manager instance.
        stack_manager (StackManager): The stack manager instance.
        status_manager (StatusManager): The status manager instance.
        subject_manager (SubjectManager): The subject manager instance.
        tag_manager (TagManager): The tag manager instance.
        teacher_manager (TeacherManager): The teacher manager instance.
        unified_manager (UnifiedObjectManager): The unified manager instance.
        user_manager (UserManager): The user manager instance.
        dispatcher (Dispatcher): The dispatcher instance.

    Methods:
        get_answer_manager(): Returns the answer manager instance.
        get_association_manager(): Returns the association manager instance.
        get_change_history_manager(): Returns the change history manager instance.
        get_change_history_item_manager(): Returns the change history item manager instance.
        get_comment_manager(): Returns the comment manager instance.
        get_component(component_name: str): Returns the component manager instance for the specified component name.
        get_custom_field_manager(): Returns the custom field manager instance.
        get_default_manager(): Returns the default manager instance.
        get_difficulty_manager(): Returns the difficulty manager instance.
        get_dispatcher(): Returns the dispatcher instance.
        get_flashcard_manager(): Returns the flashcard manager instance.
        get_logger(name: str): Returns a logger instance for the specified name.
        get_note_manager(): Returns the note manager instance.
        get_priority_manager(): Returns the priority manager instance.
        get_question_manager(): Returns the question manager instance.
        get_setting_manager(): Returns the setting manager instance.
        get_stack_manager(): Returns the stack manager instance.
        get_status_manager(): Returns the status manager instance.
        get_subject_manager(): Returns the subject manager instance.
        get_tag_manager(): Returns the tag manager instance.
        get_teacher_manager(): Returns the teacher manager instance.
        get_unified_factory(): Returns the unified factory instance.
        get_unified_manager(): Returns the unified manager instance.
        get_user_manager(): Returns the user manager instance.
    """

    logger: Final[Logger] = Logger.get_logger(name="ComponentAccessor")

    answer_manager: AnswerManager = AnswerManager()
    association_manager: AssociationManager = AssociationManager()
    change_history_manager: ChangeHistoryManager = ChangeHistoryManager()
    change_history_item_manager: ChangeHistoryItemManager = ChangeHistoryItemManager()
    comment_manager: CommentManager = CommentManager()
    custom_field_manager: CustomFieldManager = CustomFieldManager()
    default_manager: DefaultManager = DefaultManager()
    difficulty_manager: DifficultyManager = DifficultyManager()
    dispatcher: Dispatcher = Dispatcher()
    flashcard_manager: FlashcardManager = FlashcardManager()
    note_manager: NoteManager = NoteManager()
    priority_manager: PriorityManager = PriorityManager()
    question_manager: QuestionManager = QuestionManager()
    setting_manager: SettingManager = SettingManager()
    stack_manager: StackManager = StackManager()
    status_manager: StatusManager = StatusManager()
    subject_manager: SubjectManager = SubjectManager()
    tag_manager: TagManager = TagManager()
    teacher_manager: TeacherManager = TeacherManager()
    unified_factory: UnifiedObjectFactory = UnifiedObjectFactory()
    unified_manager: UnifiedObjectManager = UnifiedObjectManager()
    user_manager: UserManager = UserManager()

    @classmethod
    def get_answer_manager(cls) -> AnswerManager:
        """
        Returns the answer manager instance.

        Returns:
            AnswerManager: The answer manager instance.
        """
        return AnswerManager()

    @classmethod
    def get_association_manager(cls) -> AssociationManager:
        """
        Returns the association manager instance.

        Returns:
            AssociationManager: The association manager instance.
        """
        return AssociationManager()

    @classmethod
    def get_change_history_manager(cls) -> ChangeHistoryManager:
        """
        Returns the change history manager instance.

        Returns:
            ChangeHistoryManager: The change history manager instance.
        """
        return ChangeHistoryManager()

    @classmethod
    def get_change_history_item_manager(cls) -> ChangeHistoryItemManager:
        """
        Returns the change history item manager instance.

        Returns:
            ChangeHistoryItemManager: The change history item manager instance.
        """
        return ChangeHistoryItemManager()

    @classmethod
    def get_comment_manager(cls) -> CommentManager:
        """
        Returns the comment manager instance.

        Returns:
            CommentManager: The comment manager instance.
        """
        return CommentManager()

    @classmethod
    def get_component(
        cls,
        component_name: str,
    ) -> Any:
        """
        Returns the component manager instance.

        Args:
            component_name (str): The name of the component manager.

        Returns:
            Any: The component manager instance.
        """
        try:
            if hasattr(
                cls,
                f"get_{component_name}_manager",
            ):
                return getattr(
                    cls,
                    f"get_{component_name}_manager",
                )()
            else:
                raise ValueError(f"Invalid component name: {component_name}")
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_component' method from '{cls.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    @classmethod
    def get_custom_field_manager(cls) -> CustomFieldManager:
        """
        Returns the custom field manager instance.

        Returns:
            CustomFieldManager: The custom field manager instance.
        """
        return CustomFieldManager()

    @classmethod
    def get_default_manager(cls) -> DefaultManager:
        """
        Returns the default manager instance.

        Returns:
            DefaultManager: The default manager instance.
        """
        return DefaultManager()

    @classmethod
    def get_difficulty_manager(cls) -> DifficultyManager:
        """
        Returns the difficulty manager instance.

        Returns:
            DifficultyManager: The difficulty manager instance.
        """
        return DifficultyManager()

    @classmethod
    def get_dispatcher(cls) -> Dispatcher:
        """
        Returns the Dispatcher instance.

        Returns:
            Dispatcher: The Dispatcher instance.
        """
        return Dispatcher()

    @classmethod
    def get_flashcard_manager(cls) -> FlashcardManager:
        """
        Returns the flashcard manager instance.

        Returns:
            FlashcardManager: The flashcard manager instance.
        """
        return FlashcardManager()

    @classmethod
    def get_logger(
        cls,
        name: str,
    ) -> Logger:
        """
        Returns a logger instance for the specified name.

        Args:
            name (str): The name of the logger.

        Returns:
            Logger: The logger instance.
        """
        try:
            return Logger.get_logger(name=name)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_logger' method from '{cls.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    @classmethod
    def get_note_manager(cls) -> NoteManager:
        """
        Returns the note manager instance.

        Returns:
            NoteManager: The note manager instance.
        """
        return NoteManager()

    @classmethod
    def get_priority_manager(cls) -> PriorityManager:
        """
        Returns the priority manager instance.

        Returns:
            PriorityManager: The priority manager instance.
        """
        return PriorityManager()

    @classmethod
    def get_question_manager(cls) -> QuestionManager:
        """
        Returns the question manager instance.

        Returns:
            QuestionManager: The question manager instance.
        """
        return QuestionManager()

    @classmethod
    def get_setting_manager(cls) -> SettingManager:
        """
        Returns the setting manager instance.

        Returns:
            SettingManager: The setting manager instance.
        """
        return SettingManager()

    @classmethod
    def get_stack_manager(cls) -> StackManager:
        """
        Returns the stack manager instance.

        Returns:
            StackManager: The stack manager instance.
        """
        return StackManager()

    @classmethod
    def get_status_manager(cls) -> StatusManager:
        """
        Returns the status manager instance.

        Returns:
            StatusManager: The status manager instance.
        """
        return StatusManager()

    @classmethod
    def get_subject_manager(cls) -> SubjectManager:
        """
        Returns the subject manager instance.

        Returns:
            SubjectManager: The subject manager instance.
        """
        return SubjectManager()

    @classmethod
    def get_tag_manager(cls) -> TagManager:
        """
        Returns the tag manager instance.

        Returns:
            TagManager: The tag manager instance.
        """
        return TagManager()

    @classmethod
    def get_teacher_manager(cls) -> TeacherManager:
        """
        Returns the teacher manager instance.

        Returns:
            TeacherManager: The teacher manager instance.
        """
        return TeacherManager()

    @classmethod
    def get_unified_factory(cls) -> UnifiedObjectFactory:
        """
        Returns the unified factory instance.

        Returns:
            UnifiedObjectFactory: The unified factory instance.
        """
        try:
            # Create the factory instance
            result: UnifiedObjectFactory = UnifiedObjectFactory()

            factories: List[Type] = [
                AnswerFactory,
                AssociationFactory,
                ChangeHistoryFactory,
                ChangeHistoryItemFactory,
                CommentFactory,
                CustomFieldFactory,
                DefaultFactory,
                DifficultyFactory,
                FlashcardFactory,
                NoteFactory,
                PriorityFactory,
                QuestionFactory,
                SettingFactory,
                StackFactory,
                StatusFactory,
                SubjectFactory,
                TagFactory,
                TeacherFactory,
                UserFactory,
            ]

            # Iterate over the list of factory classes
            for factory in factories:
                # Register the factory
                result.register_factory(
                    name=Miscellaneous.camel_to_snake(string=factory.__name__),
                    factory=factory,
                )

            # Return the factory instance
            return result
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_unified_factory' method from '{cls.__class__.__name__}': {e}"
            )

            # Log the traceback
            cls.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    @classmethod
    def get_unified_manager(cls) -> UnifiedObjectManager:
        """
        Returns the unified manager instance.

        Returns:
            UnifiedObjectManager: The unified manager instance.
        """
        try:
            # Create the manager instance
            result: UnifiedObjectManager = UnifiedObjectManager()

            # Initialize the list of manager classes
            managers: List[Type] = [
                AnswerManager,
                AssociationManager,
                ChangeHistoryManager,
                ChangeHistoryItemManager,
                CommentManager,
                CustomFieldManager,
                DefaultManager,
                DifficultyManager,
                FlashcardManager,
                NoteManager,
                PriorityManager,
                QuestionManager,
                SettingManager,
                StackManager,
                StatusManager,
                SubjectManager,
                TagManager,
                TeacherManager,
                UserManager,
            ]

            # Iterate over the list of manager classes
            for manager in managers:
                # Register the manager
                result.register_manager(
                    name=Miscellaneous.camel_to_snake(string=manager.__name__),
                    manager=manager,
                )

            # Return the manager instance
            return result
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_unified_manager' method from '{cls.__class__.__name__}': {e}"
            )

            # Log the traceback
            cls.logger.error(message=traceback.format_exc())

            # Re-raise the exception to the caller
            raise e

    @classmethod
    def get_user_manager(cls) -> UserManager:
        """
        Returns the user manager instance.

        Returns:
            UserManager: The user manager instance.
        """
        return UserManager()
