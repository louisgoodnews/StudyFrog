"""
Author: lodego
Date: 2025-02-11
"""

import tkinter

from tkinter import ttk
from tkinter.constants import *

from typing import *

from core.answer import ImmutableAnswer
from core.flashcard import ImmutableFlashcard
from core.note import ImmutableNote
from core.question import ImmutableQuestion
from core.setting import SettingService
from core.stack import ImmutableStack

from core.ui.base_ui import BaseUI
from core.ui.ui_builder import UIBuilder

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous
from utils.navigation import NavigationHistoryItem, NavigationHistoryService
from utils.unified import UnifiedObjectManager


__all__: Final[List[str]] = ["SearchUI"]


class SearchUI(BaseUI):
    """
    A class representing the search user interface (UI) of the application.

    This class is responsible for initializing and configuring the layout of the
    search UI, including setting up the main frames and populating them with
    respective widgets. It extends the tkinter.Frame class and utilizes various
    utility classes for managing navigation, logging, and other functionalities.

    Attributes:
        dispatcher (Dispatcher): The dispatcher instance.
        logger (Logger): The logger instance.
        navigation_item (NavigationHistoryItem): The navigation history item instance.
        navigation_service (NavigationHistoryService): The navigation history service instance.
        setting_service (SettingService): The setting service instance.
        type (Optional[str]): The type of the search.
        unified_manager (UnifiedObjectManager): The unified manager instance.
    """

    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        navigation_item: NavigationHistoryItem,
        navigation_service: NavigationHistoryService,
        setting_service: SettingService,
        unified_manager: UnifiedObjectManager,
        type: Optional[str] = None,
    ) -> None:
        """
        Initializes a new instance of the SearchUI class.

        Args:
            dispatcher (Dispatcher): The dispatcher instance.
            master (tkinter.Misc): The parent widget.
            navigation_item (NavigationHistoryItem): The navigation history item instance.
            navigation_service (NavigationHistoryService): The navigation history service instance.
            setting_service (SettingService): The setting service instance.
            type (Optional[str]): The type of the search.
            unified_manager (UnifiedObjectManager): The unified manager instance.

        Returns:
            None
        """

        # Call the parent class constructor
        super().__init__(
            dispatcher=dispatcher,
            master=master,
            name="search_ui",
            navigation_item=navigation_item,
            navigation_service=navigation_service,
            setting_service=setting_service,
            unified_manager=unified_manager,
        )

        # Store the current page number in an instance variable
        self.page: int = 0

        # Store the type of the search in an instance variable
        self.type: Optional[str] = type

        # Load objects from the database
        self.load_contents()

    def clear(self) -> None:
        """
        Clears the content of the search widget.

        This method clears the content of the search widget by destroying all
        its children widgets.

        Returns:
            None
        """

        # Get a list of all children widgets in the content frame
        children: Optional[List[tkinter.Misc]] = self.content_frame.winfo_children()

        # Check if the content frame has any children
        if not children:
            # Return early if the content frame has no children
            return

        # Iterate over the children of the content frame
        for child in children:
            # Destroy each child widget
            child.destroy()

    def collect_subscriptions(self) -> List[Dict[str, Any]]:
        """
        Collects and returns a list of subscriptions.

        This method should be implemented by subclasses to provide
        a list containing event subscriptions. Each subscription
        is associated with specific events and their corresponding
        handlers.

        Returns:
            List[Dict[str, Any]]: A list representing the subscriptions for events.
        """

        subscriptions: List[Dict[str, Any]] = super().collect_subscriptions()

        return subscriptions

    @override
    def configure_grid(self) -> None:
        """
        Configures the grid of the search widget.

        This method configures the grid of the search widget by setting the
        weights of the columns and rows.

        Returns:
            None
        """

        # Configure the search widget's 1st column to weight 1.
        # This means that the 1st column will stretch when the window is resized.
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the search widget's 1st and 3rd row to weight 0.
        # This means that the 1st and 3rd row will not stretch when the window is resized.
        self.grid_rowconfigure(
            index=(
                0,
                2,
            ),
            weight=0,
        )

        # Configure the search widget's 2nd row to weight 1.
        # This means that the 2nd row will stretch when the window is resized.
        self.grid_rowconfigure(
            index=1,
            weight=1,
        )

    @override
    def create_widgets(self) -> None:
        """
        Creates and configures the main frames of the search UI.

        This method initializes the top, center, and bottom frames within the
        search UI, setting their layout configuration and invoking methods
        to populate each frame with its respective widgets.

        Args:
            None

        Returns:
            None
        """

        # Create the "Top Frame" frame widget
        top_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        # Configure the "Top Frame" frame widget's 0th column to weight 1
        top_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the "TOp Frame" frame widget's 0th row to weight 1
        top_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Place the "Top Frame" frame widget in the main window
        top_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create the "Center Frame" frame widget
        center_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        # Configure the "Center Frame" frame widget's 0th column to weight 1
        center_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the "Center Frame" frame widget's 0th row to weight 1
        center_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Place the "Center Frame" frame widget in the main window
        center_frame.grid(
            column=0,
            row=1,
            sticky=NSEW,
        )

        # Create the "Bottom Frame" frame widget
        bottom_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        # Configure the "Bottom Frame" frame widget's 0th column to weight 1
        bottom_frame.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the "Bottom Frame" frame widget's 0th row to weight 1
        bottom_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Place the "Bottom Frame" frame widget in the main window
        bottom_frame.grid(
            column=0,
            row=2,
            sticky=NSEW,
        )

        # Create the "Bottom Frame" frame widgets
        self.create_bottom_frame_widgets(master=bottom_frame)

        # Create the "Center Frame" frame widgets
        self.create_center_frame_widgets(master=center_frame)

        # Create the "Top Frame" frame widgets
        self.create_top_frame_widgets(master=top_frame)

    def create_bottom_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Creates and configures the main widgets of the bottom frame.

        This method initializes the main widgets of the bottom frame within the
        search UI, setting their layout configuration.

        Args:
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """

        # Configure the master frame's 0th column to weight 0
        master.grid_columnconfigure(
            index=0,
            weight=0,
        )

        # Configure the master frame's 1st column to weight 1
        master.grid_columnconfigure(
            index=1,
            weight=1,
        )

        # Configure the master frame's 2nd column to weight 0
        master.grid_columnconfigure(
            index=2,
            weight=0,
        )

        # Configure the master frame's 0th row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create the "Previous" button widget
        previous_button: tkinter.Button = UIBuilder.get_button(
            background=Constants.BLUE_GREY["700"],
            command=self.on_previous_button_click,
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=master,
            relief=FLAT,
            text="Previous",
        )

        # Place the "Previous" button widget within the top frame
        previous_button.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
        )

        # Create the "Next" button widget
        next_button: tkinter.Button = UIBuilder.get_button(
            background=Constants.BLUE_GREY["700"],
            command=self.on_next_button_click,
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=master,
            relief=FLAT,
            text="Next",
        )

        # Place the "Next" button widget within the top frame
        next_button.grid(
            column=2,
            padx=5,
            pady=5,
            row=0,
        )

    def create_center_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Creates and configures the main widgets of the center frame.

        This method initializes the main widgets of the center frame within the
        search UI, setting their layout configuration.

        Args:
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """

        # Configure the master frame's 0th column to weight 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the master frame's 0th row to weight 0
        master.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the master frame's 1st row to weight 1
        master.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Get the scrolled frame dictionary
        scrolled_frame: Optional[Dict[str, Any]] = UIBuilder.get_scrolled_frame(
            master=master
        )

        # Create the label frame
        label_frame: tkinter.Frame = UIBuilder.get_frame(
            background=Constants.BLUE_GREY["700"],
            master=master,
        )

        # Configure the label frame's 0th row to weight 1
        label_frame.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Place the label frame within the master frame
        label_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        for (
            index,
            string,
        ) in enumerate(
            iterable=[
                "icon",
                "name",
                "priority",
                "difficulty",
                "last viewed at",
                "status",
                "due by",
            ]
        ):
            # Configure the label frame's column at the current index to weight 1
            label_frame.grid_columnconfigure(
                index=index,
                weight=1,
            )

            # Create the label widget
            label: tkinter.Label = UIBuilder.get_label(
                background=Constants.BLUE_GREY["700"],
                font=(
                    Constants.DEFAULT_FONT_FAMILIY,
                    Constants.DEFAULT_FONT_SIZE,
                ),
                foreground=Constants.WHITE,
                master=label_frame,
                text=string.capitalize(),
            )

            # Place the label widget within the label frame
            label.grid(
                column=index,
                row=0,
                sticky=NSEW,
            )

        # Style the scrolled frame's canvas widget
        scrolled_frame["canvas"].configure(background=Constants.BLUE_GREY["700"])

        # Style the scrolled frame's frame widget
        scrolled_frame["frame"].configure(background=Constants.BLUE_GREY["700"])

        # Style the scrolled frame's root widget
        scrolled_frame["root"].configure(background=Constants.BLUE_GREY["700"])

        # Place the scrolled frame's root widget within the master frame
        scrolled_frame["root"].grid(
            column=0,
            row=1,
            sticky=NSEW,
        )

        # Initialize the content frame instance variable
        self.content_frame: tkinter.Frame = scrolled_frame["frame"]

    def create_content_item(
        self,
        columns: List[str],
        object: Union[
            ImmutableAnswer,
            ImmutableFlashcard,
            ImmutableNote,
            ImmutableQuestion,
            ImmutableStack,
        ],
    ) -> None:
        """
        Creates and configures the main widgets of the content item.

        This method initializes the main widgets of the content item within the
        search UI, setting their layout configuration.

        Args:
            columns (List[str]): The columns to display.
            object (Union[
                ImmutableAnswer,
                ImmutableFlashcard,
                ImmutableNote,
                ImmutableQuestion,
                ImmutableStack,
            ]): The object to create the content item for.

        Returns:
            None
        """

        try:
            # Create a tkinter.Frame widget
            frame: tkinter.Frame = UIBuilder.get_frame(
                background=Constants.BLUE_GREY["700"],
                master=self.content_frame,
            )

            # Configure the frame's 0th row to weight 1
            frame.grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Place the frame within the content frame
            frame.grid(
                column=0,
                padx=5,
                pady=5,
                row=len(self.content_frame.winfo_children()),
                sticky=NSEW,
            )

            # Iterate over each column
            for (
                index,
                column,
            ) in enumerate(iterable=columns):
                # Create a tkinter.Label widget
                label: tkinter.Label = UIBuilder.get_label(
                    background=Constants.BLUE_GREY["700"],
                    font=(
                        Constants.DEFAULT_FONT_FAMILIY,
                        Constants.DEFAULT_FONT_SIZE,
                    ),
                    foreground=Constants.WHITE,
                    master=frame,
                    text=object.get(name=column),
                )

                # Bind the label widget to the on_label_click method
                label.bind(
                    func=lambda event: self.on_label_click(object=object),
                    sequence="<ButtonRelease-1>",
                )

                # Place the label widget within the frame
                label.grid(
                    column=index,
                    padx=5,
                    pady=5,
                    row=0,
                    sticky=NSEW,
                )
        except Exception as e:
            # Log an error message indicating an exception occured
            self.logger.error(
                message=f"Caught an exception while attempting to run 'create_content_item' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def create_top_frame_widgets(
        self,
        master: tkinter.Misc,
    ) -> None:
        """
        Creates and configures the main widgets of the top frame.

        This method initializes the main widgets of the top frame within the
        search UI, setting their layout configuration.

        Args:
            master (tkinter.Misc): The parent widget.

        Returns:
            None
        """

        # Configure the master frame's 0th column to weight 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the master frame's 0th row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Configure the master frame's 1st row to weight 0
        master.grid_rowconfigure(
            index=1,
            weight=0,
        )

        # Get the searchbar dictionary
        self.searchbar: Optional[Dict[str, Any]] = UIBuilder.get_searchbar(
            command=self.searchbar_command,
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.MEDIUM_FONT_SIZE,
            ),
            master=master,
        )

        # Style the searchbar dictionary's "Button" button widget
        self.searchbar["button"].configure(
            background=Constants.BLUE_GREY["700"],
            font=(
                Constants.DEFAULT_FONT_FAMILIY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            relief=FLAT,
        )

        # Style the searchbar dictionary's "Root" frame widget
        self.searchbar["root"].configure(background=Constants.BLUE_GREY["700"])

        # Place the searchbar dictionary's "Root" frame widget within the master frame
        self.searchbar["root"].grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Get the separator widget
        separator: ttk.Separator = UIBuilder.get_separator(
            master=master,
            orient=HORIZONTAL,
        )

        # Place the separator widget within the master frame
        separator.grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )

    def load_contents(self) -> None:
        # Check, if the loaded_objects list already exists
        if not hasattr(
            self,
            "loaded_objects",
        ):
            # Load all objects from the database
            self.load_objects_from_database()

        for loaded_object in self.loaded_objects["0"]:
            self.create_content_item(
                columns=[
                    "icon",
                    "name",
                    "priority",
                    "difficulty",
                    "last_viewed_at",
                    "status",
                    "due_by",
                ],
                object=loaded_object,
            )

    def load_objects_from_database(self) -> None:
        """
        Loads all objects from the database and stores them as an instance variable.

        This method is used to load all objects from the database and store them in memory.
        It is used to populate the search results.

        Returns:
            None
        """
        try:
            # Initialize a dictionary to store loaded objects by page number
            self.loaded_objects: Dict[
                str,
                List[
                    Optional[
                        Union[
                            ImmutableAnswer,
                            ImmutableFlashcard,
                            ImmutableNote,
                            ImmutableQuestion,
                            ImmutableStack,
                        ]
                    ]
                ],
            ] = {}

            # Get all answers, flashcards, notes, questions, and stacks from the database
            objects: List[
                Optional[
                    Union[
                        ImmutableAnswer,
                        ImmutableFlashcard,
                        ImmutableNote,
                        ImmutableQuestion,
                        ImmutableStack,
                    ]
                ]
            ] = (
                self.unified_manager.get_all_answers()
                + self.unified_manager.get_all_flashcards()
                + self.unified_manager.get_all_notes()
                + self.unified_manager.get_all_questions()
                + self.unified_manager.get_all_stacks()
            )

            # Sort the objects by their 'created_at' attribute in descending order
            # This ensures the search results are shown in the order of their creation date
            objects.sort(
                key=lambda obj: obj["created_at"],
                reverse=True,
            )

            # Initialize page number for pagination
            page: int = 0

            # Iterate over the objects and paginate them
            for (
                index,
                loaded_object,
            ) in enumerate(iterable=objects):
                if index % 30 == 0:
                    page = int(index // 30)
                    # Initialize a new page in the dictionary
                    self.loaded_objects[str(page)] = []

                # Add the object to the current page
                self.loaded_objects[str(page)].append(loaded_object)
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'load_objects_from_database' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def on_label_click(
        self,
        object: Union[
            ImmutableAnswer,
            ImmutableFlashcard,
            ImmutableNote,
            ImmutableQuestion,
            ImmutableStack,
        ],
    ) -> None:
        """
        Handles the 'on_label_click' event and dispatches a navigation request.

        Args:
            object (Union[ImmutableAnswer, ImmutableFlashcard, ImmutableNote,
                          ImmutableQuestion, ImmutableStack]): The object associated
                          with the label that was clicked.

        Raises:
            Exception: If an exception occurs while dispatching the navigation request.
        """
        try:
            # Initialize the kwargs dictionary with navigation details
            kwargs: Dict[str, Any] = {
                "direction": "forward",
                "event": Events.REQUEST_VALIDATE_NAVIGATION,
                "namespace": Constants.GLOBAL_NAMESPACE,
                "source": "search_ui",
                "target": "edit_ui",
            }

            # Get the toplevel widget
            toplevel: tkinter.Toplevel = UIBuilder.get_toplevel()

            # Set the geometry of the toplevel widget
            toplevel.wm_geometry(newGeometry="1080x720")

            # Add the toplevel widget to kwargs
            kwargs["master"] = toplevel

            # Find the match from the object's key and add it to kwargs
            kwargs[
                Miscellaneous.find_match(
                    group=1,
                    string=object.key,
                    pattern=r"^([A-Za-z]+)\.",
                ).lower()
            ] = object

            # Dispatch the navigation request
            self.dispatcher.dispatch(**kwargs)
        except Exception as e:
            # Log an error message indicating an exception occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'on_label_click' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def on_next_button_click(self) -> None:
        """
        Handles the click event of the "Next" button.

        This method is used to navigate to the next page of search results.
        It first clears the content frame, then increments the current page,
        and finally loads the objects for the current page.

        Returns:
            None
        """

        # Check if the current page is the last page
        if self.page + 1 >= len(self.loaded_objects):
            # Log a warning message
            self.logger.warning(
                message=f"Cannot navigate to next page as the current page ({self.page}) is the last page."
            )

            # Return early
            return

        # Clear the content frame
        self.clear()

        # Increment the current page
        self.page += 1

        # Load the objects for the current page
        self.load_contents()

    def on_previous_button_click(self) -> None:
        """
        Handles the click event of the "Previous" button.

        This method is used to navigate to the previous page of search results.
        It first clears the content frame, then decrements the current page,
        and finally loads the objects for the current page.

        Returns:
            None
        """

        # Check if the current page is the first page
        if self.page - 1 <= 0:
            # Log a warning message
            self.logger.warning(
                message=f"Cannot navigate to previous page as the current page ({self.page}) is the first page."
            )

            # Return early
            return

        # Clear the content frame
        self.clear()

        # Decrement the current page
        self.page -= 1

        # Load the objects for the current page
        self.load_contents()

    def searchbar_command(
        self,
        string: str,
    ) -> None:
        try:
            pass
        except Exception as e:
            # Log an error message indicating an exception occured
            self.logger.error(
                message=f"Caught an exception while attempting to run 'searchbar_command' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e
