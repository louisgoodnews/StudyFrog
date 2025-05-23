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

        # Configure the 0th column to weight 1
        self._container.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the 1st column to weight 1
        self._container.grid_columnconfigure(
            index=1,
            weight=1,
        )

        # Configure the 0th row to weight 0
        self._container.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the 1st row to weight 1
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

        # Place the label widget within the grid
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
                column=0,
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
        """
        Attempts to configure the button widget with the passed keyword arguments.

        Args:
                **kwargs: Additional keyword arguments passed to the button widget's configure method.

        Returns:
                None
        """
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
        """
        Attempts to configure the child widget with the passed keyword arguments.

        Args:
                **kwargs: Additional keyword arguments passed to the child widget's configure method.

        Returns:
                None
        """
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
        """
        Attempts to configure the container frame widget with the passed keyword arguments.

        Args:
                **kwargs: Additional keyword arguments passed to the container frame widget's configure method.

        Returns:
                None
        """
        try:
            # Attempt to configure the container frame widget
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
        """
        Attempts to configure the label widget with the passed keyword arguments.

        Args:
                **kwargs: Additional keyword arguments passed to the label widget's configure method.

        Returns:
                None
        """
        try:
            # Attempt to configure the label widget
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

    def configure_label(
        self,
        **kwargs,
    ) -> None:
        """
        Attempts to configure the label widget with the passed keyword arguments.

        Args:
                **kwargs: Additional keyword arguments passed to the label widget's configure method.

        Returns:
                None
        """
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

        # Return
        return


class ScrolledFrame(tkinter.Frame):
    """
    Represents a scrollable frame widget.

    This class provides a scrollable frame widget that can be used to embed
    other widgets within a scrollable area.
    """

    def __init__(
        self,
        master: tkinter.Frame,
        horizontal_scrollbar: bool = False,
        vertical_scrollbar: bool = True,
        **kwargs,
    ) -> None:
        """
        Initializes a new instance of the ScrolledFrame class.

        Args:
                master (tkinter.Frame): The parent widget to embed the ScrolledFrame into.
                horizontal_scrollbar (bool): Whether to enable the horizontal scrollbar. Default is False.
                vertical_scrollbar (bool): Whether to enable the vertical scrollbar. Default is True.
                **kwargs: Additional configuration options for the ScrolledFrame.

        Returns:
                None
        """

        # Initialize the parent class
        super().__init__(
            master=master,
            **kwargs,
        )

        # Configure the ScrolledFrame widget's 0th column to weight 1
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the ScrolledFrame widget's 1st column to weight 0
        self.grid_columnconfigure(
            index=1,
            weight=0,
        )

        # Configure the ScrolledFrame widget's 0th row to weight 1
        self.grid_rowconfigure(
            index=0,
            weight=1,
        )

        # Configure the ScrolledFrame widget's 1st row to weight 0
        self.grid_rowconfigure(
            index=1,
            weight=0,
        )

        # Create a tkinter.Canvas widget
        self.canvas: tkinter.Canvas = tkinter.Canvas(
            master=self,
            **kwargs,
        )

        # Place the tkinter.Canvas widget within the grid
        self.canvas.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Check, if the vertical scrollbar should be enabled
        if vertical_scrollbar:
            # Create a tkinter.Scrollbar widget
            self._vertical_scrollbar: tkinter.Scrollbar = tkinter.Scrollbar(
                command=self.canvas.yview,
                master=self,
                orient=VERTICAL,
            )

            # Place the tkinter.Scrollbar widget within the grid
            self._vertical_scrollbar.grid(
                column=1,
                row=0,
                sticky=NS,
            )

            # Configure the tkinter.Canvas widget to use the tkinter.Scrollbar widget
            self.canvas.configure(yscrollcommand=self._vertical_scrollbar.set)

        # Check, if the horizontal scrollbar should be enabled
        if horizontal_scrollbar:
            # Create a tkinter.Scrollbar widget
            self._horizontal_scrollbar: tkinter.Scrollbar = tkinter.Scrollbar(
                command=self.canvas.xview,
                master=self,
                orient=HORIZONTAL,
            )

            # Place the tkinter.Scrollbar widget within the grid
            self._horizontal_scrollbar.grid(
                column=0,
                row=1,
                sticky=EW,
            )

            # Configure the tkinter.Canvas widget to use the tkinter.Scrollbar widget
            self.canvas.configure(xscrollcommand=self._horizontal_scrollbar.set)

        # Create the 'container' tkinter.Frame widget
        self._container: tkinter.Frame = tkinter.Frame(
            master=self.canvas,
            **kwargs,
        )

        # Add the 'container' tkinter.Frame widget to the tkinter.Canvas widget
        self.canvas.create_window(
            (
                0,
                0,
            ),
            anchor=NW,
            window=self._container,
        )

        # Bind the tkinter.Canvas widget to the '_on_configure' method via the '<Configure>' event
        self.canvas.bind(
            func=self._on_configure,
            sequence="<Configure>",
        )

        # Bind the tkinter.Canvas widget to the '_on_mousewheel' method via the '<MouseWheel>' event
        self.canvas.bind(
            func=self._on_mousewheel,
            sequence="<MouseWheel>",
        )

    @property
    def container(self) -> tkinter.Frame:
        """
        Returns the 'container' tkinter.Frame widget.

        Returns:
                tkinter.Frame: The 'container' tkinter.Frame widget.
        """

        # Return the 'container' tkinter.Frame widget
        return self._container

    @property
    def horizontal_scrollbar(self) -> tkinter.Scrollbar:
        """
        Returns the horizontal tkinter.Scrollbar widget.

        Returns:
                tkinter.Scrollbar: The horizontal tkinter.Scrollbar widget.
        """

        # Return the horizontal tkinter.Scrollbar widget
        return self._horizontal_scrollbar

    @property
    def vertical_scrollbar(self) -> tkinter.Scrollbar:
        """
        Returns the vertical tkinter.Scrollbar widget.

        Returns:
                tkinter.Scrollbar: The vertical tkinter.Scrollbar widget.
        """

        # Return the vertical tkinter.Scrollbar widget
        return self._vertical_scrollbar

    def _on_configure(
        self,
        event: Optional[tkinter.Event] = None,
    ) -> None:
        """
        Updates the scroll region of the tkinter.Canvas widget based on the size of the 'container' tkinter.Frame widget.

        Args:
                event (Optional[tkinter.Event]): The event object, if any.

        Returns:
                None
        """

        # Update the scroll region of the tkinter.Canvas widget based on the size of the 'container' tkinter.Frame widget
        self.canvas.configure(scrollregion=self.canvas.bbox(ALL))

        # Update idletasks
        self.update_idletasks()

    def _on_mousewheel(
        self,
        event: tkinter.Event,
    ) -> None:
        """
        Handles mouse wheel events to scroll the tkinter.Canvas widget.

        Args:
            event (tkinter.Event): The mouse wheel event object.

        Returns:
            None
        """

        # Scroll the tkinter.Canvas widget
        self.canvas.yview_scroll(
            int(-1 * (event.delta / 120)),
            "units",
        )

    @override
    def configure(
        self,
        name: Optional[str] = None,
        **kwargs,
    ) -> None:
        """
        Configures the ScrolledFrame widget.

        Args:
            name (Optional[str]): The name of the ScrolledFrame widget.
            **kwargs: Additional keyword arguments to pass to the tkinter.Frame widget's configure method.

        Returns:
            None
        """

        # Check, if the name exists
        if not name:
            # Configure the ScrolledFrame widget directly
            super().configure(
                **kwargs,
            )

            # Return early
            return

        # Configure the widget corresponding to the name
        widget: Optional[tkinter.Misc] = getattr(
            self,
            name,
            None,
        )

        # Check, if the widget exists
        if not widget:
            # Return early
            return

        # Configure the widget
        widget.configure(
            **kwargs,
        )

    def configure_container(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the 'container' tkinter.Frame widget.

        Args:
            **kwargs: Additional keyword arguments to pass to the tkinter.Frame widget's configure method.

        Returns:
            None
        """

        # Configure the 'container' tkinter.Frame widget
        self.container.configure(**kwargs)

    def configure_horizontal_scrollbar(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the horizontal tkinter.Scrollbar widget.

        Args:
            **kwargs: Additional keyword arguments to pass to the tkinter.Scrollbar widget's configure method.

        Returns:
            None
        """

        # Configure the horizontal tkinter.Scrollbar widget
        self.horizontal_scrollbar.configure(**kwargs)

    def configure_vertical_scrollbar(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the vertical tkinter.Scrollbar widget.

        Args:
            **kwargs: Additional keyword arguments to pass to the tkinter.Scrollbar widget's configure method.

        Returns:
            None
        """

        # Configure the vertical tkinter.Scrollbar widget
        self.vertical_scrollbar.configure(**kwargs)


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

    Returns:
        None
    """

    def __init__(
        self,
        master: tkinter.Misc,
        **kwargs: Optional[Dict[str, Any]],
    ) -> None:
        """
        Initializes a new instance of the TabbedFrame class.

        This sets up the container and header area for the tabs but does not create any tabs themselves.
        Use the `add` method to register tab buttons and corresponding widgets.

        Args:
            master (tkinter.Misc): The parent widget to embed the TabbedFrame into.
            **kwargs: Additional configuration options for the container frame.

        Returns:
            None
        """

        # Call the parent constructor with the passed arguments to initialize the tkinter.Frame widget
        super().__init__(
            master=master,
            **kwargs,
        )

        # Initialize the current tab (optional) string instance variable as None
        self.current_tab: Optional[str] = None

        # Initialize the tabs dictionary instance variable as None
        self.tabs: Dict[str, tkinter.Misc] = {}

        # Configure the TabbedFrame widget's 0th column to weight 1
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the TabbedFrame widget's 0th row to weight 0
        self.grid_rowconfigure(
            index=0,
            weight=0,
        )

        # Configure the TabbedFrame widget's 1st row to weight 1
        self.grid_rowconfigure(
            index=1,
            weight=1,
        )

        # Create the 'top frame' tkinter.Frame widget
        self._top_frame: tkinter.Frame = tkinter.Frame(
            master=self,
            **kwargs,
        )

        # Configure the 'top frame' tkinter.Frame widget's 0th row to weight 1
        self._top_frame.grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Create the 'container frame' tkinter.Frame widget
        self._container: tkinter.Frame = tkinter.Frame(
            master=self,
            **kwargs,
        )

        # Place the 'container frame' tkinter.Frame widget within the grid
        self._container.grid(
            column=0,
            row=1,
            sticky=NSEW,
        )

        # Configure the 'container frame' tkinter.Frame widget's 0th column to weight 1
        self._container.grid_columnconfigure(
            index=0,
            weight=1,
        )

        # Configure the 'container frame' tkinter.Frame widget's 0th row to weight 1
        self._container.grid_rowconfigure(
            index=0,
            weight=1,
        )

    @property
    def container(self) -> tkinter.Frame:
        """
        Returns the 'container frame' tkinter.Frame widget.

        Returns:
            tkinter.Frame: The 'container frame' tkinter.Frame widget.
        """

        # Return the 'container frame' tkinter.Frame widget
        return self._container

    @property
    def top_frame(self) -> tkinter.Frame:
        """
        Returns the top frame widget.

        Returns:
            tkinter.Frame: The top frame widget.
        """

        # Return the 'top frame' tkinter.Frame widget
        return self._top_frame

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

        # Initialize the 'key' variable as None
        key: Optional[str] = Miscellaneous.any_to_snake(string=label)

        # Check, if a current tab is already active
        if self.current_tab is not None:
            # Disable the currently active button
            self.configure_button(
                name=self.current_tab,
                state=NORMAL,
            )

            # Hide the currently active widget
            self.tabs[Miscellaneous.any_to_snake(string=self.current_tab)][
                "widget"
            ].grid_forget()

        # Show the selected widget
        self.tabs[key]["widget"].grid(
            column=0,
            row=0,
            sticky=NSEW,
        )

        # Set the current tab
        self.current_tab = label

        # Disable the clicked button
        self.configure_button(
            name=label,
            state=DISABLED,
        )

    def add(
        self,
        label: str,
        widget: tkinter.Misc,
    ) -> None:
        """
        Adds a new tab with an associated widget to the tabbed interface.

        A button with the given label will be added to the top bar. When clicked, it will
        display the provided widget and hide others.

        Args:
            label (str): The label for the tab button.
            widget (tkinter.Misc): The widget to be shown when the tab is active.

        Returns:
            None
        """

        # Convert the passed label to snake case
        key: str = Miscellaneous.any_to_snake(string=label.strip())

        # Check, if the tab with the passed label already exists
        if key not in self.tabs:
            # Initialize the tab dictionary
            self.tabs[key] = {}

        # Store the passed widget in the tab dictionary
        self.tabs[key]["widget"] = widget

        # Create a button for the tab
        button: tkinter.Button = tkinter.Button(
            command=lambda: self._on_button_click(label=label),
            master=self._top_frame,
            text=label,
        )

        # Place the button within the grid
        button.grid(
            column=len(self.tabs),
            padx=5,
            pady=5,
            row=0,
        )

        # Store the button in the tab dictionary
        self.tabs[key]["button"] = button

        # Check, if this is the first tab
        if len(self.tabs) == 1:
            # Disable the button widget
            self.tabs[key]["button"].configure(state=DISABLED)

            # Check, if the widget has been mapped already
            if not widget.winfo_ismapped():
                # Show the passed widget
                widget.grid(
                    column=0,
                    row=0,
                    sticky=NSEW,
                )

            # Set the current tab
            self.current_tab = label
        else:
            # Hide the widegt from the grid
            widget.grid_forget()

    @override
    def configure(
        self,
        name: Optional[str] = None,
        **kwargs,
    ) -> None:
        """
        Configures the TabbedFrame widget.

        Args:
            name (Optional[str]): The name of the TabbedFrame widget.
            **kwargs: Additional keyword arguments to pass to the tkinter.Frame widget's configure method.

        Returns:
            None
        """

        # Check, if the name exists
        if not name:
            # Configure the TabbedFrame widget directly
            super().configure(
                **kwargs,
            )

            # Return early
            return

        # Configure the widget corresponding to the name
        widget: Optional[tkinter.Misc] = getattr(
            self,
            name,
            None,
        )

        # Check, if the widget exists
        if not widget:
            # Return early
            return

        # Configure the widget
        widget.configure(
            **kwargs,
        )

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
        """

        # Convert the passed name to snake case
        key = Miscellaneous.any_to_snake(string=name)

        # Check, if the passed name string is contained in the tabs dictionary instance variable
        if key not in self.tabs:
            # Return early
            return

        # Attempt to configure the button widget corresponding to the passed name
        self.tabs[key]["button"].configure(**kwargs)

    def configure_container(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the 'container frame' tkinter.Frame widget surrounding the canvas and scrollbars.

        This method allows external customization of the outer frame,
        such as padding, borders, or colors.

        Args:
            **kwargs: Keyword arguments to pass to the 'container frame' tkinter.Frame widget's configure method.

        Returns:
            None
        """

        # Configure the 'container frame' tkinter.Frame widget
        self._container.configure(**kwargs)

    def configure_top_frame(
        self,
        **kwargs,
    ) -> None:
        """
        Configures the top frame containing the tab buttons.

        This method allows external customization of the top frame,
        such as padding, borders, or colors.

        Args:
            **kwargs: Keyword arguments to pass to the top frame's configure method.

        Returns:
            None
        """

        # Configure the 'top frame' tkinter.Frame widget
        self._top_frame.configure(**kwargs)

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

        # Destroy the button widget
        self.tabs[label]["button"].destroy()

        # Destroy the widget
        self.tabs[label]["widget"].destroy()

        # Remove the tab from the dictionary
        self.tabs.pop(label)
