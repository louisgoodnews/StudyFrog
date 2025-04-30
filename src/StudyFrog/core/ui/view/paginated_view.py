"""
Author: lodego
Date: 2025-04-23
"""

import tkinter

from tkinter.constants import *
from typing import *

from core.answer import ImmutableAnswer
from core.flashcard import ImmutableFlashcard
from core.note import ImmutableNote
from core.question import ImmutableQuestion
from core.setting import SettingService

from core.ui.frames.frames import ScrolledFrame

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.logger import Logger


__all__: Final[List[str]] = ["PaginatedView"]


class PaginatedSortItem(tkinter.Frame):
    """ """

    pass


class PaginatedViewItem(tkinter.Frame):
    """ """

    def __init__(
        self,
        dispatcher: Dispatcher,
        entity: Union[
            ImmutableAnswer,
            ImmutableFlashcard,
            ImmutableNote,
            ImmutableQuestion,
        ],
        master: tkinter.Misc,
        **kwargs,
    ) -> None:
        """ """

        # Call the parent class constructor with the passed arguments
        super().__init__(
            master=master,
            name="paginated_view_item",
            **kwargs,
        )

        # Store the passed dispatcher
        self.dispatcher: Final[Dispatcher] = dispatcher

        # Store the passed entity
        self.entity: Final[
            Union[
                ImmutableAnswer,
                ImmutableFlashcard,
                ImmutableNote,
                ImmutableQuestion,
            ]
        ] = entity

        # Initialize this instance's Logger attribute
        self.logger: Final[Logger] = Logger.get_logger(name=self.__class__.__name__)

    def configure_grid(self) -> None:
        """ """

        pass

    def create_widgets(self) -> None:
        """ """

        pass


class PaginatedView(tkinter.Frame):
    """ """

    def __init__(
        self,
        dispatcher: Dispatcher,
        master: tkinter.Misc,
        namespace: str,
        setting_service: SettingService,
        items_per_page: int = 50,
        pagination_command: Optional[Callable[[], List[Any]]] = None,
        **kwargs,
    ) -> None:
        """ """

        # Call the parent class constructor with the passed arguments
        super().__init__(
            master=master,
            name="paginated_view",
            **kwargs,
        )

        # Store the tkinter.Frame widget that will contain the page buttons in an instance variable
        self.button_container: Optional[tkinter.Frame] = None

        # Store the ScrolledFrame widget's 'container frame' tkinter.Frame widget in an instance variable
        self.page_container: Optional[tkinter.Frame] = None

        # Store the passed Dispatcher instance
        self.dispatcher: Dispatcher = dispatcher

        # Store the filtered pages
        self.filtered_pages: Dict[str, List[Any]] = {}

        # Store the passed items per page
        self.items_per_page: int = items_per_page

        # Initialize this instance's Logger attribute
        self.logger: Logger = Logger.get_logger(name=self.__class__.__name__)

        # Store the passed namespace
        self.namespace: Final[str] = namespace

        # Store the pages
        self.pages: Dict[str, List[Any]] = {}

        # Store the passed pagination command
        self.pagination_command: Optional[Callable[[], List[Any]]] = pagination_command

        # Store the passed SettingService instance
        self.setting_service: SettingService = setting_service

        # Configure the grid
        self.configure_grid()

        # Create the widgets
        self.create_widgets()

    def _on_next_button_click(self) -> None:
        """ """

        pass

    def _on_previous_button_click(self) -> None:
        """ """

        pass

    def clear_filtered_pages(self) -> None:
        """
        Clears the filtered pages.

        This method clears the 'filtered_pages' attribute, removing all filtered pages.

        Args:
            None

        Returns:
            None
        """

        # Clear the filtered pages
        self.filtered_pages.clear()

    def configure_grid(self) -> None:
        """
        Configures the grid of the PaginatedView widget.

        This method configures the grid of the PaginatedView widget by setting the
        weights of the columns and rows.

        Args:
            None

        Returns:
            None
        """

        # Configure the PaginatedView widget's 0th column to weight 1.
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the PaginatedView widget's 0th row to weight 0.
        self.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the PaginatedView widget's 1st row to weight 1.
        self.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Configure the PaginatedView widget's 2nd row to weight 0.
        self.grid_rowconfigure(
            index=2,
            weight=0,
        )

    def create_bottom_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """ """

        # Configure the passed 'master' tkinter.Frame widget's 0th column to weight 0
        master.grid_columnconfigure(
            index=0,
            weight=0,
        )

        # Configure the passed 'master' tkinter.Frame widget's 1st column to weight 1
        master.grid_columnconfigure(
            index=1,
            weight=1,
        )

        # Configure the passed 'master' tkinter.Frame widget's 2nd column to weight 0
        master.grid_columnconfigure(
            index=2,
            weight=0,
        )

        # Configure the passed 'master' tkinter.Frame widget's 0th row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create the 'previous button' tkinter.Button widget
        previous_button: tkinter.Button = tkinter.Button(
            background=Constants.BLUE_GREY["700"],
            command=self._on_previous_button_click,
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=master,
            text="Previous",
            width=10,
        )

        # Place the 'previous button' tkinter.Button widget in the grid
        previous_button.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=EW,
        )

        # Create a tkinter.Frame widget
        frame: tkinter.Frame = tkinter.Frame(
            background=Constants.BLUE_GREY["700"],
            master=master,
        )

        # Place the tkinter.Frame widget in the grid
        frame.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=EW,
        )

        # Store the tkinter.Frame widget that will contain the page buttons in an instance variable
        self.button_container = frame

        # Create page buttons
        self.create_page_buttons(master=frame)

        # Create the 'next button' tkinter.Button widget
        next_button: tkinter.Button = tkinter.Button(
            background=Constants.BLUE_GREY["700"],
            command=self._on_next_button_click,
            font=(
                Constants.DEFAULT_FONT_FAMILY,
                Constants.DEFAULT_FONT_SIZE,
            ),
            foreground=Constants.WHITE,
            master=master,
            text="Next",
            width=10,
        )

        # Place the 'next button' tkinter.Button widget in the grid
        next_button.grid(
            column=2,
            padx=5,
            pady=5,
            row=0,
            sticky=EW,
        )

        # Update idletasks
        self.update_idletasks()

    def create_center_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """
        Creates and configures the main widgets of the center frame.

        This method creates and configures the main widgets of the center frame
        within the paginated view widget, setting their layout configuration.

        Args:
            master (tkinter.Frame): The parent widget.

        Returns:
            None
        """

        # Configure the passed 'master' tkinter.Frame widget's 0th column to weight 1
        master.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the passed 'master' tkinter.Frame widget's 0th row to weight 1
        master.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Create a ScrolledFrame widget
        scrolled_frame: ScrolledFrame = ScrolledFrame(master=master)

        # Configure the ScrolledFrame widget
        scrolled_frame.configure(background=Constants.BLUE_GREY["700"])

        # Configure the ScrolledFrame widget's tkinter.Canvas widget
        scrolled_frame.configure_canvas(background=Constants.BLUE_GREY["700"])

        # Configure the ScrolledFrame widget's 'container frame' tkinter.Frame widget
        scrolled_frame.configure_container_frame(background=Constants.BLUE_GREY["700"])

        # Place the ScrolledFrame widget in the grid
        scrolled_frame.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Store the ScrolledFrame widget's 'container frame' in an instance variable
        self.page_container = scrolled_frame.container

        # Update idletasks
        self.update_idletasks()

    def create_page_buttons(
        self,
        master: tkinter.Frame,
    ) -> None:
        """
        Creates and configures the page buttons of the paginated view widget.

        This method creates and configures the page buttons of the paginated view widget,
        setting their layout configuration and invoking methods to populate each frame
        with its respective widgets.

        Args:
            master (tkinter.Frame): The parent widget.

        Returns:
            None
        """

        pass

    def create_top_frame_widgets(
        self,
        master: tkinter.Frame,
    ) -> None:
        """ """

        # TODO:
        #   - implement PaginatedSortItem class widgets

        # Update idletasks
        self.update_idletasks()

    def create_widgets(self) -> None:
        """
        Creates and configures the main widgets of the paginated view widget.

        This method creates and configures the main widgets of the paginated view widget,
        setting their layout configuration and invoking methods to populate each frame
        with its respective widgets.

        Args:
            None

        Returns:
            None

        Raises:
            Exception: If an exception occurs during the creation or configuration of the widgets.
        """

        # Create the 'top frame' tkinter.Frame widget
        top_frame: tkinter.Frame = tkinter.Frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        # Place the 'top frame' tkinter.Frame widget in the grid
        top_frame.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create the 'top frame' widgets
        self.create_top_frame_widgets(master=top_frame)

        # Create the 'center frame' tkinter.Frame widget
        center_frame: tkinter.Frame = tkinter.Frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        # Place the 'center frame' tkinter.Frame widget in the grid
        center_frame.grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
            sticky=NSEW,
        )

        # Create the 'center frame' widgets
        self.create_center_frame_widgets(master=center_frame)

        # Create the 'bottom frame' tkinter.Frame widget
        bottom_frame: tkinter.Frame = tkinter.Frame(
            background=Constants.BLUE_GREY["700"],
            master=self,
        )

        # Place the 'bottom frame' tkinter.Frame widget in the grid
        bottom_frame.grid(
            column=0,
            padx=5,
            pady=5,
            row=2,
            sticky=NSEW,
        )

        # Create the 'bottom frame' widgets
        self.create_bottom_frame_widgets(master=bottom_frame)

        # Update idletasks
        self.update_idletasks()

    def has_filtered_pages(self) -> bool:
        """
        Determines if there are any filtered pages.

        This method checks if the 'filtered_pages' attribute contains any pages.
        It returns True if there are filtered pages, otherwise False.

        Returns:
            bool: True if there are filtered pages, False otherwise.
        """

        # Return True if there are filtered pages, False otherwise
        return bool(self.filtered_pages)
