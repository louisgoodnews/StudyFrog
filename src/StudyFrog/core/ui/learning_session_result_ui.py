"""
Author: lodego
Date: 2025-03-15
"""

import tkinter
import traceback

from tkinter.constants import *
from typing import *

from core.difficulty import ImmutableDifficulty
from core.flashcard import ImmutableFlashcard
from core.note import ImmutableNote
from core.priority import ImmutablePriority
from core.question import ImmutableQuestion
from core.setting import SettingService
from core.status import ImmutableStatus

from core.learning.learning_session import (
    ImmutableLearningSession,
    ImmutableLearningSessionAction,
    ImmutableLearningSessionItem,
)

from core.ui.frames.frames import ScrolledFrame, TabbedFrame

from utils.base_ui import BaseUI
from utils.constants import Constants
from utils.dispatcher import Dispatcher, DispatcherEvent, DispatcherNotification
from utils.events import Events
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous
from utils.navigation import NavigationHistoryItem, NavigationHistoryService
from utils.unified import UnifiedObjectFactory, UnifiedObjectManager
from utils.utils import DateUtil


__all__: Final[List[str]] = ["LearningSessionResultUI"]


class LearningSessionResultItem(tkinter.Frame):
    """
    A tkinter.Frame widget that represents a learning session item.

    This class extends the tkinter.Frame class and provides a user interface
    for displaying a learning session item.

    Attributes:
        dispatcher (Dispatcher): The dispatcher instance.
        learning_session_item (ImmutableLearningSessionItem): The learning session item.
        master (tkinter.Misc): The master widget.
        **kwargs: Additional keyword arguments.
    """

    def __init__(
        self,
        dispatcher: Dispatcher,
        learning_session_item: ImmutableLearningSessionItem,
        master: tkinter.Misc,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the LearningSessionResultItem class.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.
            learning_session_item (ImmutableLearningSessionItem): The learning session item.
            master (tkinter.Misc): The master widget.
            **kwargs: Additional keyword arguments.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            master=master,
            **kwargs,
        )

        # Store the passed Dispatcher instance
        self.dispatcher: Dispatcher = dispatcher

        # Store the passed ImmutableLearningSessionItem instance
        self.learning_session_item: Final[ImmutableLearningSessionItem] = (
            learning_session_item
        )

        # Initialize this instance's Logger attribute
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Obtain the entity associated with the ImmutableLearningSessionItem instance's reference
        self.entity: Optional[
            Union[
                ImmutableFlashcard,
                ImmutableNote,
                ImmutableQuestion,
            ]
        ] = self._get_entity_by_key(key=self.learning_session_item.reference)

        # Configure the grid
        self.configure_grid()

        # Create the widgets
        self.create_widgets()

    def _get_entity_by_key(
        self,
        key: str,
    ) -> Optional[
        Union[
            ImmutableFlashcard,
            ImmutableLearningSessionAction,
            ImmutableNote,
            ImmutableQuestion,
        ]
    ]:
        """
        Requests the entity associated with the passed key.

        This method dispatches the REQUEST_GET_BY_KEY event in the 'global'
        namespace and returns the one and only result (assuming the object
        associated with the passed key) to the caller.

        Args:
            key (str): The key of the entity to be requested.

        Returns:
            Optional[Union[ImmutableFlashcard ImmutableLearningSessionAction, ImmutableNote, ImmutableQuestion]]: The requested entity if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to run this method.
        """
        try:
            # Dispatch the REQUEST_GET_BY_KEY event in the 'global' namespace
            notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
                event=Events.REQUEST_GET_BY_KEY,
                key=key,
                namespace=Constants.GLOBAL_NAMESPACE,
            )

            # Check, if the notification exists or has errors
            if not notification or notification.has_errors():
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to dispatch 'REQUEST_GET_BY_KEY' in 'global' namespace in '{self.__class__.__name__}' class: {notification.get_errors() if notification else None}"
                )

                # Return early
                return

            # Return the one and only result (assuming the object associated with the passed key) to the caller
            return notification.get_one_and_only_result()
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run '_get_entity_by_key' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def _suggest_future_difficulty(
        self,
        key: str,
    ) -> Optional[ImmutableDifficulty]:
        """ """

        pass

    def _suggest_future_priority(
        self,
        key: str,
    ) -> Optional[ImmutablePriority]:
        """ """

        pass

    def configure_grid(self) -> None:
        """ """

        pass

    def create_widgets(self) -> None:
        """ """

        # Update idletasks
        self.update_idletasks()


class LearningSessionResultUI(BaseUI):
    """
    A class representing the learning session result user interface (UI) of the application.

    This class is responsible for initializing and configuring the layout of the
    learning session UI, including setting up the main frames and populating them with
    respective widgets. It extends the tkinter.Frame class and utilizes various
    utility classes for managing navigation, logging, and other functionalities.

    Attributes:
        dispatcher (Dispatcher): The dispatcher instance.
        learning_session (ImmutableLearningSession): The learning session instance.
        logger (Logger): The logger instance.
        navigation_item (NavigationHistoryItem): The navigation history item instance.
        navigation_service (NavigationHistoryService): The navigation history service instance.
        setting_service (SettingService): The setting service instance.
        unified_factory (UnifiedObjectFactory): The unified factory instance.
        unified_manager (UnifiedObjectManager): The unified manager instance.
    """

    def __init__(
        self,
        dispatcher: Dispatcher,
        learning_session: ImmutableLearningSession,
        master: tkinter.Misc,
        navigation_item: NavigationHistoryItem,
        navigation_service: NavigationHistoryService,
        setting_service: SettingService,
        unified_factory: UnifiedObjectFactory,
        unified_manager: UnifiedObjectManager,
    ) -> None:
        """
        Initializes a new instance of the LearningSessionResultUI class.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.
            learning_session (ImmutableLearningSession): The learning session instance.
            master (tkinter.Misc): The parent widget.
            navigation_item (NavigationHistoryItem): The navigation history item instance.
            navigation_service (NavigationHistoryService): The navigation history service instance.
            setting_service (SettingService): The setting service instance.
            unified_factory (UnifiedObjectFactory): The unified factory instance.
            unified_manager (UnifiedObjectManager): The unified manager instance.

        Returns:
            None
        """

        # Store the passed ImmutableLearningSession object in an instance variable
        self.learning_session: ImmutableLearningSession = learning_session

        # Call the parent class constructor
        super().__init__(
            dispatcher=dispatcher,
            master=master,
            name="learning_session_result_ui",
            navigation_item=navigation_item,
            navigation_service=navigation_service,
            setting_service=setting_service,
            unified_factory=unified_factory,
            unified_manager=unified_manager,
        )

        # Load the learning session items
        self._load_learning_session_items()

    def _get_entity_by_key(
        self,
        key: str,
    ) -> Optional[
        Union[
            ImmutableFlashcard,
            ImmutableNote,
            ImmutableQuestion,
        ]
    ]:
        """
        Retrieves an entity by its key.

        This method dispatches a request to get an entity associated with the given key
        in the 'global' namespace. It returns the entity if found, otherwise None.

        Args:
            key (str): The key of the entity to be retrieved.

        Returns:
            Optional[Union[ImmutableFlashcard, ImmutableNote, ImmutableQuestion]]:
                The entity associated with the key, or None if not found or an error occurs.

        Raises:
            Exception: If an exception occurs while attempting to retrieve the entity.
        """
        try:
            # Dispatch the REQUEST_GET_BY_KEY event in the 'global' namespace
            notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
                event=Events.REQUEST_GET_BY_KEY,
                key=key,
                namespace=Constants.GLOBAL_NAMESPACE,
            )

            # Check if the notification exists or has errors
            if not notification or notification.has_errors():
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to dispatch 'REQUEST_GET_BY_KEY' in global namespace for '{key}' key: {notification.get_errors() if notification else "This is likely a bug."}"
                )

                # Return early
                return

            # Return the one and only result of the notification
            return notification.get_one_and_only_result()
        except Exception as e:
            # Log an error message if an exception occurs
            self.logger.error(
                message=f"Caught an exception while attempting to run '_get_entity_by_key' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def _get_entities_by_keys(
        self,
        keys: List[str],
    ) -> Optional[
        List[
            Union[
                ImmutableFlashcard,
                ImmutableNote,
                ImmutableQuestion,
            ]
        ]
    ]:
        """
        Retrieves a list of entities by their keys.

        This method dispatches a request to get entities associated with the given keys
        in the 'global' namespace. It returns the entities in a list if found, otherwise None.

        Args:
            keys (List[str]): The keys of the entities to be retrieved.

        Returns:
            Optional[List[Union[ImmutableFlashcard, ImmutableNote, ImmutableQuestion]]]:
                The entities associated with the keys, or None if not found or an error occurs.

        Raises:
            Exception: If an exception occurs while attempting to retrieve the entity.
        """
        try:
            # Dispatch the REQUEST_GET_BY_KEYS event in the 'global' namespace
            notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
                event=Events.REQUEST_GET_BY_KEYS,
                keys=keys,
                namespace=Constants.GLOBAL_NAMESPACE,
            )

            # Check if the notification exists or has errors
            if not notification or notification.has_errors():
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to dispatch 'REQUEST_GET_BY_KEYS' in global namespace for '{', '.join(keys)}' keys: {notification.get_errors() if notification else "This is likely a bug."}"
                )

                # Return early
                return

            # Return the one and only result of the notification
            return notification.get_one_and_only_result()
        except Exception as e:
            # Log an error message if an exception occurs
            self.logger.error(
                message=f"Caught an exception while attempting to run '_get_entities_by_keys' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def _load_learning_session_items(self) -> None:
        """
        Loads the learning session items.

        This method loads the learning session items from the unified manager.

        Args:
            None

        Returns:
            None
        """
        try:
            # Obtain the entities associated to the learning session
            entities: Optional[
                List[
                    Union[
                        ImmutableFlashcard,
                        ImmutableNote,
                        ImmutableQuestion,
                    ]
                ]
            ] = self._get_entities_by_keys(keys=self.learning_session.children)

            # Check, if the entities exist
            if not entities:
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to fetch learning session items. Aborting..."
                )

                # Return early
                return

            # Iterate over the entities
            for (
                index,
                entity,
            ) in enumerate(iterable=entities):
                # Configure the row at the current index to weight 1
                self.details_scrolled_frame.grid_rowconfigure(
                    index=index,
                    weight=1,
                )

                # Create a new LearningSessionResultItem instance
                result_item: LearningSessionResultItem = LearningSessionResultItem(
                    dispatcher=self.dispatcher,
                    learning_session_item=entity,
                    master=self.details_scrolled_frame,
                )

                # Place the LearningSessionResultItem instance in the grid
                result_item.grid(
                    column=0,
                    row=index,
                    sticky=NSEW,
                )
        except Exception as e:
            # Log an error message if an exception occurs
            self.logger.error(
                message=f"Caught an exception while attempting to run 'load_learning_session_items' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def _on_continue_button_click(self) -> None:
        """
        Handles the click event of the 'Continue' button.

        This method dispatches the REQUEST_VALIDATE_NAVIGATION event in the 'global' namespace
        to request that the navigation service validate the navigation to the 'learning_dashboard_ui'
        target.

        Args:
            None

        Returns:
            None

        Raises:
            Exception: If an error occurs during dispatch or internal processing.
        """
        try:
            # Dispatch the REQUEST_VALIDATE_NAVIGATION event in the 'global' namespace
            notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
                direction=Constants.FORWARD_DIRECTION,
                event=Events.REQUEST_VALIDATE_NAVIGATION,
                namespace=Constants.GLOBAL_NAMESPACE,
                source="learning_session_result_ui",
                target="learning_dashboard_ui",
            )

            # Check, if the notification exists or has errors
            if not notification or notification.has_errors():
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to dispatch 'REQUEST_VALIDATE_NAVIGATION' event in 'global' namespace in '{self.__class__.__name__}' class. Errors: {notification.get_errors() if notification else None}"
                )

                # Return early
                return
        except Exception as e:
            # Log an error message
            self.logger.error(
                message=f"Caught an exception while attempting to run '_on_continue_button_click' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def _on_retry_button_click(self) -> None:
        """
        Handles the click event of the 'Retry' button.

        Dispatches the REQUEST_VALIDATE_NAVIGATION event in the 'global' namespace
        to request that the navigation service validate the navigation to the
        'learning_session_stack_selection_ui' target.

        Args:
            None

        Returns:
            None

        Raises:
            Exception: If an error occurs during dispatch or internal processing.
        """
        try:
            # Dispatch the REQUEST_VALIDATE_NAVIGATION event in the 'global' namespace
            notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
                direction=Constants.FORWARD_DIRECTION,
                event=Events.REQUEST_VALIDATE_NAVIGATION,
                namespace=Constants.GLOBAL_NAMESPACE,
                source="learning_session_result_ui",
                target="learning_stack_selection_ui",
            )

            # Check, if the notification exists or has errors
            if not notification or notification.has_errors():
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to dispatch 'REQUEST_VALIDATE_NAVIGATION' event in 'global' namespace in '{self.__class__.__name__}' class. Errors: {notification.get_errors() if notification else None}"
                )

                # Return early
                return
        except Exception as e:
            # Log an error message
            self.logger.error(
                message=f"Caught an exception while attempting to run '_on_retry_button_click' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def _request_entity(
        self,
        event: DispatcherEvent,
        **kwargs,
    ) -> Optional[
        Union[
            ImmutableDifficulty,
            ImmutableFlashcard,
            ImmutableLearningSession,
            ImmutableLearningSessionAction,
            ImmutableLearningSessionItem,
            ImmutableNote,
            ImmutablePriority,
            ImmutableQuestion,
            ImmutableStatus,
        ]
    ]:
        """
        Dispatches the given event in the 'global' namespace and returns the one and only result of the notification.

        This method dispatches the given event in the 'global' namespace and returns the one and only result of the notification
        if the notification exists and does not have errors. Otherwise, it logs a warning message and returns None.

        Args:
            event (DispatcherEvent): The event to be dispatched in the 'global' namespace.
            **kwargs: Additional keyword arguments to be passed to the dispatcher.

        Returns:
            Optional[Union[ImmutableDifficulty, ImmutableFlashcard, ImmutableLearningSession, ImmutableLearningSessionAction, ImmutableLearningSessionItem, ImmutableNote, ImmutablePriority, ImmutableQuestion, ImmutableStatus]]:
                The one and only result of the notification if the notification exists and does not have errors.
                Otherwise, None.

        Raises:
            Exception: If an error occurs during dispatch or internal processing.
        """
        try:
            # Dispatch the REQUEST_GET_BY_KEYS event in the 'global' namespace
            notification: Optional[DispatcherNotification] = self.dispatcher.dispatch(
                event=event,
                namespace=Constants.GLOBAL_NAMESPACE,
                **kwargs,
            )

            # Check if the notification exists or has errors
            if not notification or notification.has_errors():
                # Log a warning message
                self.logger.warning(
                    message=f"Failed to dispatch '{event}' event in 'global' namespace: {notification.get_errors() if notification else "This is likely a bug."}"
                )

                # Return early
                return

            # Return the one and only result of the notification
            return notification.get_one_and_only_result()
        except Exception as e:
            # Log an error message
            self.logger.error(
                message=f"Caught an exception while attempting to run '_request_entity' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def collect_subscriptions(self) -> List[Dict[str, Any]]:
        """
        Collects and returns a list of subscriptions.

        This method should be implemented by subclasses to provide
        a list containing event subscriptions. Each subscription
        is associated with specific events and their corresponding
        handlers.

        Args:
            None

        Returns:
            List[Dict[str, Any]]: A list representing the subscriptions for events.
        """

        # Call the parent class 'collect_subscriptions' method
        subscriptions: List[Dict[str, Any]] = super().collect_subscriptions()

        # Return the list of subscriptions to the caller
        return subscriptions

    @override
    def configure_grid(self) -> None:
        """
        Configures the grid of the learning session result user interface.

        This method configures the grid of the learning session result user interface by setting the
        weights of the columns and rows.

        Returns:
            None
        """

        # Configure the weight of the LearningSessionUI widget's 0th column to 1.
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the weight of the LearningSessionUI widget's 0th row to 0.
        self.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the weight of the LearningSessionUI widget's 1st row to 1.
        self.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Configure the weight of the LearningSessionUI widget's 2nd row to 0.
        self.grid_rowconfigure(
            index=2,
            weight=0,
        )

    def create_bottom_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """
        Creates and configures the main widgets of the bottom frame.

        This method initializes the main widgets of the bottom frame within the
        learning session result UI, setting their layout configuration and
        adding functionalities to the 'retry' and 'continue' buttons.

        Args:
            master (tkinter.Frame): The parent widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs during the execution of the method.
        """
        try:
            # Configure the weight of the 0th column of the passed master tkinter.Frame widget to 1.
            master.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 1st column of the passed master tkinter.Frame widget to 0.
            master.grid_columnconfigure(
                index=1,
                weight=0,
            )

            # Configure the weight of the 2nd column of the passed master tkinter.Frame widget to 0.
            master.grid_columnconfigure(
                index=2,
                weight=0,
            )

            # Configure the weight of the 0th row of the passed master tkinter.Frame widget to 1.
            master.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the 'retry button' tkinter.Button widget
            retry_button: tkinter.Button = tkinter.Button(
                background=Constants.BLUE_GREY["700"],
                command=self._on_retry_button_click,
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=master,
                relief=FLAT,
                text="Retry",
            )

            # Place the 'retry button' tkinter.Button widget in the grid
            retry_button.grid(
                column=1,
                padx=5,
                pady=5,
                row=0,
                sticky=E,
            )

            # Create the 'continue button' tkinter.Button widget
            continue_button: tkinter.Button = tkinter.Button(
                background=Constants.BLUE_GREY["700"],
                command=self._on_continue_button_click,
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=master,
                relief=FLAT,
                text="Continue",
            )

            # Place the 'continue button' tkinter.Button widget in the grid
            continue_button.grid(
                column=2,
                padx=5,
                pady=5,
                row=0,
                sticky=E,
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_bottom_frame_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def create_center_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """
        Creates and configures the main widgets of the center frame.

        This method initializes the main widgets of the center frame within the
        learning session result user interface, setting their layout configuration.

        Args:
            master (tkinter.Frame): The parent widget.

        Returns:
            None

        Raises:
            Exception: If an exception occurs during the creation of the TabbedFrame widget.
        """
        try:
            # Configure the weight of the 0th column of the passed master tkinter.Frame widget to 1.
            master.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 0th row of the passed master tkinter.Frame widget to 1.
            master.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create a TabbedFrame widget
            tabbed_frame: TabbedFrame = TabbedFrame(master=master)

            # Place the TabbedFrame widget in the grid
            tabbed_frame.grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Configure the TabbedFrame widget
            tabbed_frame.configure(background=Constants.BLUE_GREY["700"])

            # Configure the TabbedFrame widget's 'container frame' tkinter.Frame widget
            tabbed_frame.configure_container(
                background=Constants.BLUE_GREY["700"]
            )

            # Configure the TabbedFrame widget's 'top frame' tkinter.Frame widget
            tabbed_frame.configure_top_frame(background=Constants.BLUE_GREY["700"])

            # Create and add the overview widgets to the TabbedFrame widget
            tabbed_frame.add(
                label="Overview",
                widget=self.create_overview_widgets(master=tabbed_frame),
            )

            # Configure the TabbedFrame widget's 'overview button' widget
            tabbed_frame.configure_button(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                name="overview",
                relief=FLAT,
            )

            # Create and add the details widgets to the TabbedFrame widget
            tabbed_frame.add(
                label="Details", widget=self.create_details_widgets(master=tabbed_frame)
            )

            # Configure the TabbedFrame widget's 'details button' widget
            tabbed_frame.configure_button(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                name="details",
                relief=FLAT,
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_center_frame_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def create_details_widgets(
        self,
        master: tkinter.Frame,
    ) -> ScrolledFrame:
        """
        Creates and configures the main widgets of the details frame.

        This method initializes the main widgets of the details frame within the
        learning session result user interface, setting their layout configuration.

        Args:
            master (tkinter.Frame): The parent widget.

        Returns:
            ScrolledFrame: The ScrolledFrame widget.

        Raises:
            Exception: If an exception occurs during the creation of the ScrolledFrame widget.
        """
        try:
            # Configure the weight of the 0th column of the passed master tkinter.Frame widget to 1.
            master.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 0th row of the passed master tkinter.Frame widget to 1.
            master.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the ScrolledFrame widget
            self.details_scrolled_frame: ScrolledFrame = ScrolledFrame(master=master)

            # Place the ScrolledFrame in the grid
            self.details_scrolled_frame.grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Configure the ScrolledFrame widget's 'container frame' tkinter.Frame widget
            self.details_scrolled_frame.configure_container(
                background=Constants.BLUE_GREY["700"]
            )

            # Apply default layout configuration to the ScrolledFrame widget
            self._apply_default_frame_layout_configuration(
                frame=self.details_scrolled_frame
            )

            # Return the ScrolledFrame widget to the caller
            return self.details_scrolled_frame
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_details_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def create_overview_widgets(
        self,
        master: tkinter.Frame,
    ) -> ScrolledFrame:
        """
        Creates and configures the main widgets of the overview frame.

        This method initializes the main widgets of the overview frame within the
        learning session result user interface, setting their layout configuration.

        Args:
            master (tkinter.Frame): The parent widget.

        Returns:
            ScrolledFrame: The ScrolledFrame widget.

        Raises:
            Exception: If an exception occurs during the creation of the ScrolledFrame widget.
        """
        try:
            # Configure the weight of the 0th column of the passed master tkinter.Frame widget to 1.
            master.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 0th row of the passed master tkinter.Frame widget to 1.
            master.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the ScrolledFrame widget
            scrolled_frame: ScrolledFrame = ScrolledFrame(master=master)

            # Place the ScrolledFrame in the grid
            scrolled_frame.grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Configure the weight of the 0th column of the ScrolledFrame widget to 1.
            scrolled_frame.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the ScrolledFrame widget's 'container frame' tkinter.Frame widget
            scrolled_frame.configure_container(background=Constants.BLUE_GREY["700"])

            # Create the 'time stats label' tkinter.Label widget
            time_stats_label: tkinter.Label = tkinter.Label(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.LARGE_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=scrolled_frame.container,
                text="Time Stats",
            )

            # Place the 'time stats label' tkinter.Label widget in the grid
            time_stats_label.grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Create the 'duration label' tkinter.Label widget
            duration_label: tkinter.Label = tkinter.Label(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.LARGE_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=scrolled_frame.container,
                text=f"Duration: {self.learning_session.duration // 60} minutes.",
            )

            # Place the 'duration label' tkinter.Label widget in the grid
            duration_label.grid(
                column=0,
                padx=5,
                pady=5,
                row=1,
                sticky=NSEW,
            )

            # Create the 'number of contents label' tkinter.Label widget
            number_of_contents_label: tkinter.Label = tkinter.Label(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.LARGE_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=scrolled_frame.container,
                text=f"Number of contents: {len(self.learning_session.contents)}",
            )

            # Place the 'number of contents label' tkinter.Label widget in the grid
            number_of_contents_label.grid(
                column=0,
                padx=5,
                pady=5,
                row=2,
                sticky=NSEW,
            )

            # Create the 'average on content label' tkinter.Label widget
            average_on_content_label: tkinter.Label = tkinter.Label(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.LARGE_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=scrolled_frame.container,
                text=f"Average on content: {self.learning_session.duration // len(self.learning_session.contents)} seconds",
            )

            # Place the 'average on content label' tkinter.Label widget in the grid
            average_on_content_label.grid(
                column=0,
                padx=5,
                pady=5,
                row=3,
                sticky=NSEW,
            )

            # Create the 'number of stacks label' tkinter.Label widget
            number_of_stacks_label: tkinter.Label = tkinter.Label(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.LARGE_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=scrolled_frame.container,
                text=f"Number of stacks: {len(self.learning_session.stacks)} ({', '.join(self.learning_session.stacks)})",
            )

            # Place the 'number of stacks label' tkinter.Label widget in the grid
            number_of_stacks_label.grid(
                column=0,
                padx=5,
                pady=5,
                row=4,
                sticky=NSEW,
            )

            # Apply default layout configuration to the ScrolledFrame widget
            self._apply_default_frame_layout_configuration(frame=scrolled_frame)

            # Return the ScrolledFrame widget to the caller
            return scrolled_frame
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_overview_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def create_top_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """
        Creates and configures the main widgets of the top frame.

        This method initializes the main widgets of the top frame within the
        learning session result user interface, setting their layout configuration.

        Args:
            master (tkinter.Frame): The parent widget.

        Returns:
            None
        """
        try:
            # Configure the weight of the 0th column of the passed master tkinter.Frame widget to 1.
            master.grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the weight of the 0th row of the passed master tkinter.Frame widget to 1.
            master.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create a tkinter.Label widget
            label: tkinter.Label = tkinter.Label(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILY,
                    Constants.LARGE_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=master,
                text="Congrats! You've completed this learning session run.",
            )

            # Place the tkinter.Label widget in the grid
            label.grid(
                column=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_top_frame_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @override
    def create_widgets(self) -> None:
        """
        Creates and configures the main widgets of the learning session result user interface.

        This method creates and configures the main widgets of the learning session result user
        interface, setting their layout configuration and invoking methods to populate
        each frame with its respective widgets.

        Args:
            None

        Returns:
            None

        Raises:
            Exception: If an exception occurs during the creation or configuration of the widgets.
        """
        try:
            # Create the bottom frame widget
            bottom_frame: tkinter.Frame = tkinter.Frame(
                background=Constants.BLUE_GREY["700"],
                height=25,
                master=self,
            )

            # Place the bottom frame widget in the main window
            bottom_frame.grid(
                column=0,
                row=2,
                sticky=NSEW,
            )

            # Create and configure the bottom frame widgets
            self.create_bottom_frame_widgets(master=bottom_frame)

            # Create the center frame widget
            center_frame: tkinter.Frame = tkinter.Frame(
                background=Constants.BLUE_GREY["700"],
                master=self,
            )

            # Place the center frame widget in the main window
            center_frame.grid(
                column=0,
                row=1,
                sticky=NSEW,
            )

            # Create and configure the center frame widgets
            self.create_center_frame_widgets(master=center_frame)

            # Create the top frame widget
            top_frame: tkinter.Frame = tkinter.Frame(
                background=Constants.BLUE_GREY["700"],
                height=25,
                master=self,
            )

            # Place the top frame widget in the main window
            top_frame.grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create and configure the top frame widgets
            self.create_top_frame_widgets(master=top_frame)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_widgets' method from '{self.__class__.__name__}': {e}"
            )

            # Log the traceback
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e
