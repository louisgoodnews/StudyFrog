"""
Author: lodego
Date: 2025-04-10
"""

import platform
import tkinter
import traceback

from tkinter.constants import *
from typing import *

from utils.logger import Logger
from utils.miscellaneous import Miscellaneous


__all__: Final[List[str]] = [
    "CollapsibleFrame",
    "ScrolledFrame",
    "TabbedFrame",
]


class CollapsibleFrame(tkinter.Frame):
    """
    A collapsible frame widget with a label and a toggle button.

    This class represents a tkinter.Frame that can show or hide its content dynamically.
    It provides a label and a button at the top; the button toggles the visibility of
    the internal container where additional widgets can be inserted. This is useful for
    managing UI complexity by hiding or showing advanced or optional options.

    Attributes:
        is_collapsed (bool): Whether the frame is currently collapsed (i.e., content hidden).
        logger (Logger): Logger instance for debugging/logging.
        _child (Optional[tkinter.Misc]): The actual widget/content placed inside the collapsible area.
    """

    def __init__(
        self,
        label: str,
        master: tkinter.Misc,
        column: int = 0,
        row: int = 0,
        **kwargs: Optional[Dict[str, Any]],
    ) -> None:
        """
        Initializes a new instance of the CollapsibleFrame class.

        Args:
            label (str): The text to display in the label.
            master (tkinter.Misc): The master widget.
            **kwargs: Additional keyword arguments passed to the parent Frame.

        Returns:
            None
        """

        # Initialize this class' logger instance in an instance variable
        self.logger: Final[Logger] = Logger.get_logger(name=self.__class__.__name__)

        # Initialize the child (optional) tkinter.Misc instance variable as None
        self._child: Optional[tkinter.Misc] = None

        # Initializue the flag to determine, if the widget is collapsed or not as false
        self.is_collapsed: bool = True

        # Create the 'container' frame widget
        self._container: tkinter.Frame = tkinter.Frame(
            master=master,
            **kwargs,
        )

        #
        self._container.grid_columnconfigure(
            index=0,
            weight=1,
        )

        #
        self._container.grid_columnconfigure(
            index=1,
            weight=1,
        )

        #
        self._container.grid_rowconfigure(
            index=0,
            weight=0,
        )

        #
        self._container.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Place the 'container' frame widget within the grid
        self._container.grid(
            column=column,
            row=row,
            sticky=NSEW,
        )

        # Create a label widget
        self._label: tkinter.Label = tkinter.Label(
            master=self,
            text=label,
        )

        # Place the button widget within the grid
        self._label.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Create a button widget
        self._button: tkinter.Button = tkinter.Button(
            command=self._on_button_click,
            master=self,
            text="Click here to expand",
        )

        # Place the button widget within the grid
        self._button.grid(
            column=1,
            padx=5,
            pady=5,
            row=0,
            sticky=E,
        )

        # Call the parent class constructor with the passed attributes
        super().__init__(
            master=self._container,
            **kwargs,
        )

    @property
    def button(self) -> tkinter.Button:
        """
        Returns the toggle button widget that expands/collapses the frame.

        Returns;
            tkinter.Button: the toggle button widget that expands/collapses the frame.
        """

        # Return the tkinter.Button button
        return self._button

    @property
    def child(self) -> Optional[tkinter.Misc]:
        """
        Returns the child widget currently assigned to the collapsible frame.

        Returns:
            Optional[tkinter.Misc]: The child widget currently assigned to the collapsible frame, if it exists. Otherwise None
        """

        # Return the tkinter.Misc (optional) child
        return self._child

    @child.setter
    def child(
        self,
        value: tkinter.Misc,
    ) -> None:
        """
        Sets the child widget for the collapsible content area.

        Args:
            value (tkinter.Misc): The widget to be inserted inside the collapsible frame.

        Returns:
            None
        """

        # Update the child to the passed value
        self._child = value

    @property
    def container(self) -> tkinter.Frame:
        """
        Returns the internal container frame for the child content.

        Returns:
            tkinter.Frame: The internal container frame for the child content.
        """

        # Return the 'container' frame
        return self._container

    @property
    def label(self) -> tkinter.Label:
        """
        Returns the label widget associated with the collapsible frame.

        Returns:
            tkinter.Label: The label widget associated with the collapsible frame.
        """

        # Return the tkinter.Label label
        return self._label

    def _on_button_click(self) -> None:
        """
        Handles the logic for expanding/collapsing the frame.

        When the button is clicked, this method toggles the visibility
        of the internal container and updates the button label.

        Returns:
            None
        """

        # Check, if this widget currently has a child
        if not self._child:
            # Return early
            return

        # Check, if the 'is collapsed' flag is set to True
        if self.is_collapsed:
            # Place the container widget in the grid
            self.grid(
                colum=0,
                padx=5,
                pady=5,
                row=0,
                sticky=NSEW,
            )

            # Update the button widget's text
            self._button.configure(text="Click here to collapse")
        else:
            # Hide the container widget in the grid
            self.grid_forget()

            # Update the button widget's text
            self._button.configure(text="Click here to expand")

        # Update the 'is collapsed' flag to the opposite value
        self.is_collapsed = not self.is_collapsed

    def configure_button(
        self,
        **kwargs,
    ) -> None:
        """ """
        try:
            # Attempt to configure the button widget
            self._button.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_button' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_child(
        self,
        **kwargs,
    ) -> None:
        """ """
        try:
            # Check, if the child widget exists:
            if not self._child:
                # Return early
                return

            # Attempt to configure the child widget
            self._child.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_child' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_container(
        self,
        **kwargs,
    ) -> None:
        """ """
        try:
            # Attempt to configure the container widget
            self._container.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_container' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_label(
        self,
        **kwargs,
    ) -> None:
        """ """
        try:
            # Attempt to configure the buttlabelon widget
            self._label.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_label' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def remove(self) -> None:
        """
        Removes and destroys the currently assigned child widget, if any.

        This is useful when re-assigning content or resetting the frame.

        Returns:
            None
        """

        # Check, fi this widget currently has a child
        if self._child is not None:
            # Destroy the child widget
            self._child.destroy()

            # Set the child attribute to None
            self._child = None

        # Return
        return

    def set(
        self,
        child: tkinter.Misc,
    ) -> None:
        """
        Assigns a child widget to the collapsible container.

        The provided widget will be embedded in the collapsible frame.

        Args:
            child (tkinter.Misc): The widget to be placed inside the collapsible content area.

        Returns:
            None
        """

        # Check, if the child's master is identical to this frame
        if child.master != self:
            # Update the child widget#s master attribute to the 'container frame' frame widget
            child["master"] = self

        # Upate the child attribute
        self.child = child


class ScrolledFrame(tkinter.Frame):
    """
    A scrollable frame widget that adds horizontal and vertical scrollbars.

    This class represents a tkinter.Frame embedded in a scrollable Canvas, surrounded
    by scrollbars. It is useful for placing widgets in a scrollable area when content
    might exceed the visible bounds of the application window.

    Attributes:
        logger (Logger): Logger instance for debugging/logging.
        container (tkinter.Frame): The outer container holding the Canvas and scrollbars.
        canvas (tkinter.Canvas): The canvas on which this frame is drawn.
        horizontal_scrollbar (tkinter.Scrollbar): Scrollbar for horizontal scrolling.
        vertical_scrollbar (tkinter.Scrollbar): Scrollbar for vertical scrolling.
    """

    def __init__(
        self,
        master: tkinter.Misc,
        column: int = 0,
        row: int = 0,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the ScrolledFrame class.

        This method creates a container frame that embeds a canvas and two scrollbars,
        and adds this frame into the canvas to make it scrollable.

        Args:
            master (tkinter.Misc): The parent widget in which to place the scrolled frame.
            column (int): The grid column in which to place the container. Defaults to 0.
            row (int): The grid row in which to place the container. Defaults to 0.
            **kwargs: Additional keyword arguments passed to the container frame.

        Returns:
            None
        """

        # Initialize this class' logger instance in an instance variable
        self.logger: Final[Logger] = Logger.get_logger(name=self.__class__.__name__)

        # Create the 'container' frame widget
        self._container: tkinter.Frame = tkinter.Frame(
            master=master,
            **kwargs,
        )

        #
        self._container.grid_columnconfigure(
            index=0,
            weight=1,
        )

        #
        self._container.grid_columnconfigure(
            index=1,
            weight=0,
        )

        #
        self._container.grid_rowconfigure(
            index=0,
            weight=1,
        )

        #
        self._container.grid_rowconfigure(
            index=1,
            weight=0,
        )

        # Place the container widget within the grid
        self._container.grid(
            column=column,
            row=row,
            sticky=NSEW,
        )

        # Create a canvas widget
        self._canvas: tkinter.Canvas = tkinter.Canvas(master=self._container)

        # Place the canvas widget within the frame
        self._canvas.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Call the parent class constructor
        super().__init__(master=self._container)

        # Bind the 'on_canvas_configure' method to this widget via the '<Configure>' event
        self.bind(
            func=self._on_container_configure,
            sequence="<Configure>",
        )

        # Bind the 'on_canvas_configure' method to the canvas widget via the '<Configure>' event
        self._canvas.bind(
            func=self._on_container_configure,
            sequence="<Configure>",
        )

        # Get the name of the OS
        system: str = platform.system()

        # Check, if the OS is 'Windows"
        if system.lower() == "windows":
            #
            self._canvas.bind_all(
                func=self._on_mousewheel,
                sequence="<MouseWheel>",
            )
        elif system.lower() == "darwin":
            #
            self._canvas.bind_all(
                func=self._on_mousewheel,
                sequence="<MouseWheel>",
            )
        else:
            #
            self._canvas.bind_all(
                func=self._on_mousewheel,
                sequence="<Button-4>",
            )

            #
            self._canvas.bind_all(
                sunc=self._on_mousewheel,
                sequence="<Button-5>",
            )

        # Add this frame to the canvas widget
        self._canvas.create_window(
            anchor=NW,
            window=self,
            x=0,
            y=0,
        )

        # Create the 'vertical scrollbar' scrollbar widget
        self._vertical_scrollbar: tkinter.Scrollbar = tkinter.Scrollbar(
            command=self._canvas.yview,
            master=self._container,
            orient=VERTICAL,
        )

        # Place the 'vertical scrollbar' scrollbar widget within the frame
        self._vertical_scrollbar.grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
            sticky=EW,
        )

        # Create the 'horizontal scrollbar' scrollbar widget
        self._horizontal_scrollbar: tkinter.Scrollbar = tkinter.Scrollbar(
            command=self._canvas.xview,
            master=self._container,
            orient=HORIZONTAL,
        )

        # Place the 'horizontal scrollbar' scrollbar widget within the frame
        self._horizontal_scrollbar.grid(
            column=0,
            padx=5,
            pady=5,
            row=1,
            sticky=EW,
        )

        # Configure the canvas widget
        self._canvas.configure(
            xscrollcommand=self._horizontal_scrollbar.set,
            yscrollcommand=self._vertical_scrollbar.set,
        )

    @property
    def canvas(self) -> tkinter.Canvas:
        """
        Returns the canvas widget on which this frame is drawn.

        Returns:
            tkinter.Canvas: The canvas widget.
        """

        # Return the tkinter.Canvas canvas
        return self._container

    @property
    def container(self) -> tkinter.Frame:
        """
        Returns the outer container frame holding the canvas and scrollbars.

        Returns:
            tkinter.Frame: The outer container frame.
        """

        # Return the 'container' frame
        return self._container

    @property
    def horizontal_scrollbar(self) -> tkinter.Scrollbar:
        """
        Returns the horizontal scrollbar widget.

        Returns:
            tkinter.Scrollbar: The horizontal scrollbar.
        """

        # Return the 'horizontal scrollbar' scrollbar
        return self._horizontal_scrollbar

    @property
    def vertical_scrollbar(self) -> tkinter.Scrollbar:
        """
        Returns the vertical scrollbar widget.

        Returns:
            tkinter.Scrollbar: The vertical scrollbar.
        """

        # Return the 'vertical scrollbar' scrollbar
        return self._vertical_scrollbar

    def _on_container_configure(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        Handles container resizing and updates the scroll region.

        This method should be bound to the <Configure> event of the canvas
        to dynamically update the scroll region when content is added or resized.

        Args:
            event (Optional[tkinter.Event]): The event object. Defaults to None.

        Returns:
            None
        """
        try:
            # Update scrollregion to encompass the entire embedded frame
            self._canvas.configure(scrollregion=self._canvas.bbox(ALL))
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run '_on_container_configure' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def _on_mousewheel(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        Handles mouse wheel events to scroll the canvas content.

        This method can be bound to mouse wheel events to allow vertical
        scrolling via the user's mouse wheel or trackpad.

        Args:
            event (Optional[tkinter.Event]): The mouse wheel event. Defaults to None.

        Returns:
            None
        """
        try:
            # Check, if the event is None
            if not event:
                # Return early
                return

            # Ontain the OS' sname
            system: str = platform.system()

            # Initialise the amount int to 0
            amount: int = 0

            # Check, if teh OS is either Windows or Darwin (MacOS)
            if system.lower() in [
                "darwin",
                "windows",
            ]:
                amount = -1 if event.delta > 0 else 1
            else:
                amount = -1 if event.num == 4 else 1

            # Control key pressed → horizontal scroll
            if event.state & 0x0004:
                self._canvas.xview_scroll(
                    number=amount,
                    what=UNITS,
                )
            else:
                self._canvas.yview_scroll(
                    number=amount,
                    what=UNITS,
                )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run '_on_mousewheel' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_canvas(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the canvas widget inside the ScrolledFrame.

        This method allows external customization of the canvas widget,
        such as changing background color, scroll behavior, or other properties.

        Args:
            **kwargs: Keyword arguments to pass to the canvas' configure method.

        Returns:
            None

        Raises:
            Exception: Raises an exception if any errors occur while attempting configuration.
        """
        try:
            # Attempt to configure the canvas widget
            self._canvas.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_canvas' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_container(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the container frame surrounding the canvas and scrollbars.

        This method allows external customization of the outer frame,
        such as padding, borders, or colors.

        Args:
            **kwargs: Keyword arguments to pass to the container's configure method.

        Returns:
            None

        Raises:
            Exception: Raises an exception if any errors occur while attempting configuration.
        """
        try:
            # Attempt to configure the 'container' frame widget
            self._container.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_contaier' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_horizontal_scrollbar(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the horizontal scrollbar widget.

        This method allows customization of the horizontal scrollbar,
        including style, appearance, or orientation.

        Args:
            **kwargs: Keyword arguments to pass to the scrollbar's configure method.

        Returns:
            None

        Raises:
            Exception: Raises an exception if any errors occur while attempting configuration.
        """
        try:
            # Attempt to configure the 'horizontal scrollbar' scrolblar widget
            self.button.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_horizontal_scrollbar' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_vertical_scrollbar(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the vertical scrollbar widget.

        This method allows customization of the vertical scrollbar,
        including style, appearance, or orientation.

        Args:
            **kwargs: Keyword arguments to pass to the scrollbar's configure method.

        Returns:
            None

        Raises:
            Exception: Raises an exception if any errors occur while attempting configuration.
        """
        try:
            # Attempt to configure the 'vertical scrollbar' scrollbar widget
            self._vertical_scrollbar.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_vertical_scrollbar' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    @override
    def destroy(self) -> None:
        """
        Cleans up and destroys the ScrolledFrame widget.

        This method unbinds all mousewheel-related events to prevent memory leaks
        or dangling event handlers, and then destroys the underlying Frame.

        Returns:
            None
        """

        # Obtain the OS' name
        system: str = platform.system()

        # Check, if the OS is 'Windows'
        if system.lower() == "windows":
            self._canvas.unbind_all(sequence="<MouseWheel>")

        # Check, if the OS is 'Darwin' (MacOS)
        elif system.lower() == "darwin":
            self._canvas.unbind_all(sequence="<MouseWheel>")

        # If the OS is neither Windows nor MacOS, assume it's Linux based
        else:
            self._canvas.unbind_all(sequence="<Button-4>")
            self._canvas.unbind_all(sequence="<Button-5>")

        # Call the parent class' 'destroy' method
        super().destroy()


class TabbedFrame(tkinter.Frame):
    """
    A tabbed frame widget that allows switching between multiple embedded widgets.

    This widget creates a horizontal row of buttons as tabs. Each button corresponds to a widget (e.g., a Frame)
    that will be shown when the button is clicked. Only one tab is visible at a time, and selecting a new tab will
    automatically hide the previously active one.

    Attributes:
        current_tab (Optional[str]): The label of the currently active tab.
        tabs (Dict[str, Dict[str, tkinter.Misc]]): A dictionary of tab labels mapped to their associated widgets and buttons.
        container (tkinter.Frame): The container that holds the tab headers and content.
        top_frame (tkinter.Frame): The top frame used for holding tab buttons.
    """

    def __init__(
        self,
        master: tkinter.Misc,
        column: int = 0,
        row: int = 0,
        **kwargs: Optional[Dict[str, Any]],
    ) -> None:
        """
        Initializes a new instance of the TabbedFrame class.

        This sets up the container and header area for the tabs but does not create any tabs themselves.
        Use the `add` method to register tab buttons and corresponding widgets.

        Args:
            master (tkinter.Misc): The parent widget to embed the TabbedFrame into.
            column (int): The column position to grid the container in. Default is 0.
            row (int): The row position to grid the container in. Default is 0.
            **kwargs: Additional configuration options for the container frame.
        """

        # Initialize this class' logger instance in an instance variable
        self.logger: Final[Logger] = Logger.get_logger(name=self.__class__.__name__)

        # Initialize the current tab (optional) string instance variable as None
        self.current_tab: Optional[str] = None

        # Initialize the tabs dictionary instance variable as None
        self.tabs: Dict[str, tkinter.Misc] = {}

        # Create the 'container' frame widget
        self._container: tkinter.Frame = tkinter.Frame(
            master=master,
            **kwargs,
        )

        # Place the 'container' frame widget within the grid
        self._container.grid(
            column=column,
            row=row,
            sticky=NSEW,
        )

        # Create the 'top frame' frame widget
        self._top_frame: tkinter.Frame = tkinter.Frame(master=self._container)

        # Place the 'top frame' frame widget within the grid
        self._top_frame.grid(
            column=0,
            padx=5,
            pady=5,
            row=0,
            sticky=NSEW,
        )

        # Place this frame within the grid
        self.grid(
            column=0,
            row=1,
            sticky=NSEW,
        )

    def _on_button_click(
        self,
        label: str,
    ) -> None:
        """
        Handles the tab switching logic when a tab button is clicked.

        Hides the currently displayed tab widget (if any), shows the selected one,
        and updates the button states accordingly.

        Args:
            label (str): The label of the tab to be activated.

        Returns:
            None
        """

        #
        if self.current_tab:
            #
            self.configure_button(
                label=self.current_tab,
                state=NORMAL,
            )

            #
            self.tabs[Miscellaneous.any_to_snake(string=self.current_tab)][
                "widget"
            ].grid_forget()

        #
        self.tabs[Miscellaneous.any_to_snake(string=label)]["widget"].grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        #
        self.current_tab = label

        #
        self.configure_button(
            label=label,
            state=DISABLED,
        )

    def add(
        self,
        label: str,
        widget: tkinter.Misc,
    ) -> str:
        """
        Adds a new tab with an associated widget to the tabbed interface.

        A button with the given label will be added to the top bar. When clicked, it will
        display the provided widget and hide others.

        Args:
            label (str): The label for the tab button.
            widget (tkinter.Misc): The widget to be shown when the tab is active.

        Returns:
            str: The snake_case version of the label, which is used as an internal key.
        """

        #
        self.tabs[Miscellaneous.any_to_snake(string=label)]["widget"] = widget

        #
        button: tkinter.Button = tkinter.Button(
            command=lambda: self._on_button_click(label=label),
            master=self._top_frame,
            text=label,
        )

        #
        button.grid(
            column=len(self.tabs),
            padx=5,
            pady=5,
            row=0,
        )

        #
        self.tabs[Miscellaneous.any_to_snake(string=label)]["button"] = button

        #
        if len(self.tabs) == 1:
            #
            widget.grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

        # Return a snake case representation of the passed label
        return Miscellaneous.any_to_snake(string=label)

    def configure_button(
        self,
        name: str,
        **kwargs,
    ) -> None:
        """
        Configures the button associated with a specific tab.

        This method allows customization of the tab button corresponding to the
        specified name. Common options include changing text, state, background, etc.

        Args:
            name (str): The label of the tab whose button should be configured.
            **kwargs: Additional keyword arguments passed to the `configure` method of the button widget.

        Returns:
            None

        Raises:
            Exception: If an error occurs during configuration, it will be logged and re-raised.
        """
        try:
            # Convert the passed name to snake case
            name = Miscellaneous.any_to_snake(string=name)

            # Check, if the passed name string is contained in the tabs dictionary instance variable
            if name not in self.tabs:
                # Return early
                return

            # Attempt to configure the button widget corresponding to the passed name
            self.tabs[name]["button"].configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_button' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def configure_container(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the container frame surrounding the canvas and scrollbars.

        This method allows external customization of the outer frame,
        such as padding, borders, or colors.

        Args:
            **kwargs: Keyword arguments to pass to the container's configure method.

        Returns:
            None

        Raises:
            Exception: Raises an exception if any errors occur while attempting configuration.
        """
        try:
            # Attempt to configure the 'container' frame widget
            self._container.configure(**kwargs)
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'configure_contaier' method from '{self.__class__.__name__}' class: {e}"
            )

            # Log the traceback as error message
            self.logger.error(message=f"Traceback: {traceback.format_exc()}")

            # Re-raise the exception to the caller
            raise e

    def remove(
        self,
        label: str,
    ) -> None:
        """
        Removes a tab and its associated widget and button.

        Args:
            label (str): The label of the tab to be removed.

        Returns:
            None
        """

        #
        self.tabs[label]["button"].destroy()

        #
        self.tabs[label]["widget"].destroy()

        #
        self.tabs.pop(label)
