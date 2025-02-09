"""
Author: lodego
Date: 2025-02-08
"""

import tkinter

from typing import *

from tkinter import ttk

from tkinter.constants import *

from utils.logger import Logger
from utils.miscellaneous import Miscellaneous


__all__: List[str] = ["UIBuilder"]


class UIBuilder:
    """
    A utility class for building user interface components.

    Attributes:
        logger (Logger): The logger instance used by the class.
    """

    logger: Logger = Logger.get_logger(name="UIBuilder")

    @classmethod
    def get_bool_variable(
        cls,
        master: Optional[tkinter.Misc] = None,
        name: Optional[str] = None,
        value: Optional[Any] = False,
    ) -> Optional[tkinter.BooleanVar]:
        """
        Creates and returns a new instance of tkinter.BooleanVar.

        Args:
            name (str): The name of the variable.

        Returns:
            tkinter.BooleanVar: The created tkinter.BooleanVar instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.BooleanVar.
        """
        try:
            # Attempt to create and return a new instance of tkinter.BooleanVar
            return tkinter.BooleanVar(
                master=master,
                name=name,
                value=value,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_bool_variable' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_button(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[tkinter.Button]:
        """
        Creates and returns a new instance of tkinter.Button.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Button constructor.

        Returns:
            Optional[ttk.Button]: The created tkinter.Button instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Button.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Button
            return tkinter.Button(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_button' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_canvas(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[tkinter.Canvas]:
        """
        Creates and returns a new instance of tkinter.Canvas.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Canvas constructor.

        Returns:
            Optional[ttk.Canvas]: The created tkinter.Canvas instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Canvas.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Canvas
            return tkinter.Canvas(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_canvas' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_checkbutton(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[tkinter.Checkbutton]:
        """
        Creates and returns a new instance of tkinter.Checkbutton.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Checkbutton constructor.

        Returns:
            Optional[ttk.Checkbutton]: The created tkinter.Checkbutton instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Checkbutton.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Checkbutton
            return tkinter.Checkbutton(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_checkbutton' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_clock(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of tkinter.Label that displays the current datetime.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Label constructor.

        Returns:
            Optional[Dict[str, Any]]: The created tkinter.Label instance or None if an exception occurs.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Label.
        """
        try:

            def update_clock() -> None:
                """
                Updates the text of the label to the current datetime.

                This function is scheduled to be called every 1000 milliseconds using the after method of the label widget.

                Returns:
                    None
                """
                # Set the text of the label to the current datetime
                result["label"]["text"] = Miscellaneous.datetime_to_string(
                    datetime=Miscellaneous.get_current_datetime()
                )

                # Schedule the next call to update the clock
                result["label"].after(
                    ms=1000,
                    func=update_clock,
                )

            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(master=master)

            # Configure the "Root" frame widget's 1st column to weight 1
            result["root"].grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the "Root" frame widget's 1st row to weight 1
            result["root"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the "Label" label widget
            result["label"] = cls.get_label(
                master=result["root"],
                text=Miscellaneous.datetime_to_string(
                    datetime=Miscellaneous.get_current_datetime()
                ),
                **kwargs,
            )

            # Grid the "Label" label widget in the "Root" frame widget
            result["label"].grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Start the clock
            update_clock()

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_clock' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_combobox(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[ttk.Combobox]:
        """
        Creates and returns a new instance of tkinter.Combobox.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Combobox constructor.

        Returns:
            Optional[ttk.Combobox]: The created tkinter.Combobox instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Combobox.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Combobox
            return ttk.Combobox(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_combobox' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_entry(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[tkinter.Entry]:
        """
        Creates and returns a new instance of tkinter.Entry.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Entry constructor.

        Returns:
            Optional[ttk.Entry]: The created tkinter.Entry instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Entry.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Entry
            return tkinter.Entry(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_entry' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_float_variable(
        cls,
        master: Optional[tkinter.Misc] = None,
        name: Optional[str] = None,
        value: Optional[float] = 0.0,
    ) -> Optional[tkinter.DoubleVar]:
        """
        Creates and returns a new instance of tkinter.DoubleVar.

        Args:
            master (Optional[Any]): The master widget.
            name (Optional[str]): The name of the variable.
            value (Optional[float]): The initial value of the variable.

        Returns:
            Optional[tkinter.DoubleVar]: The created tkinter.DoubleVar instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.DoubleVar.
        """
        try:
            # Attempt to create and return a new instance of tkinter.DoubleVar
            return tkinter.DoubleVar(
                master=master,
                name=name,
                value=value,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_float_variable' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_frame(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[tkinter.Frame]:
        """
        Creates and returns a new instance of tkinter.Frame.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Frame constructor.

        Returns:
            Optional[ttk.Frame]: The created tkinter.Frame instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Frame.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Frame
            return tkinter.Frame(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_frame' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_int_variable(
        cls,
        master: Optional[tkinter.Misc] = None,
        name: Optional[str] = None,
        value: Optional[int] = 0,
    ) -> Optional[tkinter.IntVar]:
        """
        Creates and returns a new instance of tkinter.IntVar.

        Args:
            master (Optional[Any]): The master widget.
            name (Optional[str]): The name of the variable.
            value (Optional[int]): The initial value of the variable.

        Returns:
            Optional[tkinter.IntVar]: The created tkinter.IntVar instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.IntVar.
        """
        try:
            # Attempt to create and return a new instance of tkinter.IntVar
            return tkinter.IntVar(
                master=master,
                name=name,
                value=value,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_int_variable' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_label(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[tkinter.Label]:
        """
        Creates and returns a new instance of tkinter.Label.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Label constructor.

        Returns:
            Optional[tkinter.Label]: The created tkinter.Label instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Label.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Label
            return tkinter.Label(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_label' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_menu(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[tkinter.Menu]:
        """
        Creates and returns a new instance of tkinter.Menu.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Menu constructor.

        Returns:
            Optional[tkinter.Menu]: The created tkinter.Menu instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Menu.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Menu
            return tkinter.Menu(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_menu' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_menubutton(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[tkinter.Menubutton]:
        """
        Creates and returns a new instance of tkinter.Menubutton.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Menubutton constructor.

        Returns:
            Optional[tkinter.Menubutton]: The created tkinter.Menubutton instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Menubutton.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Menubutton
            return tkinter.Menubutton(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_menubutton' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_progressbar(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[ttk.Progressbar]:
        """
        Creates and returns a new instance of ttk.Progressbar.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the ttk.Progressbar constructor.

        Returns:
            Optional[ttk.Progressbar]: The created ttk.Progressbar instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of ttk.Progressbar.
        """
        try:
            # Attempt to create and return a new instance of ttk.Progressbar
            return ttk.Progressbar(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_progressbar' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_radiobutton(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[tkinter.Radiobutton]:
        """
        Creates and returns a new instance of tkinter.Radiobutton.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Radiobutton constructor.

        Returns:
            Optional[tkinter.Radiobutton]: The created tkinter.Radiobutton instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Radiobutton.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Radiobutton
            return tkinter.Radiobutton(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_radiobutton' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_scrollbar(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[tkinter.Scrollbar]:
        """
        Creates and returns a new instance of tkinter.Scrollbar.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Scrollbar constructor.

        Returns:
            Optional[tkinter.Scrollbar]: The created tkinter.Scrollbar instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Scrollbar.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Scrollbar
            return tkinter.Scrollbar(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_scrollbar' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_scrolled_frame(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of a scrolled frame.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Frame constructor.

        Returns:
            Optional[Dict[str, Any]]: The created scrolled frame.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of a scrolled frame.
        """
        try:

            def on_frame_configure(event: tkinter.Event) -> None:
                """
                Resizes the canvas whenever the containing frame is resized.

                This method is called whenever the containing frame is resized. It resizes the
                canvas to fit the new size of the frame.

                Args:
                    event (tkinter.Event): The event that triggered this method call.

                Returns:
                    None
                """
                result["canvas"].configure(scrollregion=result["canvas"].bbox("all"))
                result["canvas"].itemconfig(
                    id,
                    anchor="nw",
                    width=result["canvas"].winfo_width(),
                )

            # Initialise the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(
                master=master,
            )

            # Configure the "Root" frame widget's 1st column to weight 1
            result["root"].grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the "Root" frame widget's 2nd column to weight 0
            result["root"].grid_columnconfigure(
                index=1,
                weight=0,
            )

            # Configure the "Root" frame widget's 1st row to weight 1
            result["root"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the "Scrollbar" scrollbar widget
            result["scrollbar"] = cls.get_scrollbar(
                master=master,
            )

            # Grid the "Scrollbar" scrollbar widget in the "Root" frame widget
            result["scrollbar"].grid(
                column=1,
                row=0,
                sticky=NS,
            )

            # Create the "Canvas" canvas widget
            result["canvas"] = cls.get_canvas(
                master=master,
                yscrollcommand=result["scrollbar"].set,
            )

            # Grid the "Canvas" canvas widget in the "Root" frame widget
            result["canvas"].grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the "Frame" frame widget
            result["frame"] = cls.get_frame(
                master=result["canvas"],
                **kwargs,
            )

            # Configure the "Scrollbar" scrollbar widget to the canvas
            result["scrollbar"].config(
                command=result["canvas"].yview,
            )

            # Add the "Frame" frame widget to the "Canvas" canvas widget
            id: int = result["canvas"].create_window(
                (
                    0,
                    0,
                ),
                anchor=NW,
                window=result["frame"],
            )

            # Bind the "Frame" frame widget to the "Configure" event
            result["frame"].bind(
                func=on_frame_configure,
                sequence="<Configure>",
            )

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_scrolled_frame' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_searchbar(
        cls,
        master: tkinter.Misc,
        command: Callable[[str], None],
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Creates and returns a new instance of a search bar widget.

        This function creates a new instance of a search bar widget. The
        search bar widget is a frame that contains an entry widget and a
        button widget. The entry widget is used to input a search query and
        the button widget is used to execute the search query. When the
        button widget is clicked, the command function is called with the
        current value of the entry widget as an argument.

        Args:
            master (tkinter.Misc): The master widget.
            command (Callable[[str], None]): The command function to execute
                when the button widget is clicked.
            **kwargs: Any additional keyword arguments to be passed to the
                frame widget's constructor.

        Returns:
            Optional[Dict[str, Any]]: The created search bar widget instance.

        Raises:
            Exception: If an exception occurs while attempting to create a
                new instance of the search bar widget.
        """
        try:

            def clear() -> None:
                """
                Clears the current value of the entry widget.

                This function clears the current content of the entry widget.

                Returns:
                    None
                """
                result["entry"].delete(
                    0,
                    END,
                )

            def get() -> str:
                """
                Returns the current value of the entry widget.

                Returns the current value of the entry widget. This is the
                string that is currently displayed in the entry widget.

                Returns:
                    str: The current value of the entry widget.
                """
                return result["entry"].get()

            def set(value: str) -> None:
                """
                Sets the value of the entry widget.

                This function clears the current content of the entry widget
                and inserts the provided value.

                Args:
                    value (str): The string value to set in the entry widget.

                Returns:
                    None
                """
                clear()
                result["entry"].insert(
                    0,
                    value,
                )

            # Initialize the result dictionary as an empty dictionary
            result: Dict[str, Any] = {}

            # Create the "Root" frame widget
            result["root"] = cls.get_frame(master=master)

            # Configure the "Root" frame widget's 1st column to weight 1
            result["root"].grid_columnconfigure(
                index=0,
                weight=1,
            )

            # Configure the "Root" frame widget's 2nd column to weight 0
            result["root"].grid_columnconfigure(
                index=1,
                weight=0,
            )

            # Configure the "Root" frame widget's 1st row to weight 1
            result["root"].grid_rowconfigure(
                index=0,
                weight=1,
            )

            # Create the "Entry" entry widget
            result["entry"] = cls.get_entry(master=result["root"])

            # Grid the "Entry" entry widget in the "Root" frame widget
            result["entry"].grid(
                column=0,
                row=0,
                sticky=NSEW,
            )

            # Create the "Clear" button widget
            result["button"] = cls.get_button(
                command=lambda: command(get()),
                master=result["root"],
                text="Search",
            )

            # Grid the "Button" button widget in the "Root" frame widget
            result["button"].grid(
                column=1,
                padx=5,
                pady=5,
                row=0,
            )

            # Return the result dictionary
            return result
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_searchbar' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_separator(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[ttk.Separator]:
        """
        Creates and returns a new instance of ttk.Separator.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the ttk.Separator constructor.

        Returns:
            Optional[ttk.Separator]: The created ttk.Separator instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of ttk.Separator.
        """
        try:
            # Attempt to create and return a new instance of ttk.Separator
            return ttk.Separator(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_separator' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_spinbox(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[ttk.Spinbox]:
        """
        Creates and returns a new instance of ttk.Spinbox.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the ttk.Spinbox constructor.

        Returns:
            Optional[ttk.Spinbox]: The created ttk.Spinbox instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of ttk.Spinbox.
        """
        try:
            # Attempt to create and return a new instance of ttk.Spinbox
            return ttk.Spinbox(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_spinbox' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_str_variable(
        cls,
        master: Optional[tkinter.Misc] = None,
        name: Optional[str] = None,
        value: Optional[str] = "",
    ) -> Optional[tkinter.StringVar]:
        """
        Creates and returns a new instance of tkinter.StringVar.

        Args:
            master (Optional[Any]): The master widget.
            name (Optional[str]): The name of the variable.
            value (Optional[str]): The initial value of the variable.

        Returns:
            Optional[tkinter.StringVar]: The created tkinter.StringVar instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.StringVar.
        """
        try:
            # Attempt to create and return a new instance of tkinter.StringVar
            return tkinter.StringVar(
                master=master,
                name=name,
                value=value,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_str_variable' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_text(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[tkinter.Text]:
        """
        Creates and returns a new instance of tkinter.Text.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Text constructor.

        Returns:
            Optional[tkinter.Text]: The created tkinter.Text instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Text.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Text
            return tkinter.Text(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_text' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_tk(
        cls,
        base_name: Optional[str] = None,
        class_name: Optional[str] = None,
        screen_name: Optional[str] = None,
        sync: Optional[bool] = False,
        use_tk: Optional[bool] = False,
    ) -> Optional[tkinter.Tk]:
        """
        Creates and returns a new instance of tkinter.Tk.

        Args:
            base_name (Optional[str]): The base name of the root window.
            class_name (Optional[str]): The class name of the root window.
            screen_name (Optional[str]): The name of the screen where the root window should appear.
            sync (Optional[bool]): Whether to use synchronous mode or not.
            use_tk (Optional[bool]): Whether to use Tk or not.

        Returns:
            Optional[tkinter.Tk]: The created tkinter.Tk instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Tk.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Tk
            return tkinter.Tk(
                baseName=base_name,
                className=class_name,
                screenName=screen_name,
                sync=sync,
                useTk=use_tk,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_tk' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_toplevel(
        cls,
        master: Optional[tkinter.Misc] = None,
        **kwargs,
    ) -> Optional[tkinter.Toplevel]:
        """
        Creates and returns a new instance of tkinter.Toplevel.

        Args:
            master (Optional[Any]): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the tkinter.Toplevel constructor.

        Returns:
            Optional[tkinter.Toplevel]: The created tkinter.Toplevel instance if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of tkinter.Toplevel.
        """
        try:
            # Attempt to create and return a new instance of tkinter.Toplevel
            return tkinter.Toplevel(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_toplevel' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None

    @classmethod
    def get_treeview(
        cls,
        master: tkinter.Misc,
        **kwargs,
    ) -> Optional[ttk.Treeview]:
        """
        Creates and returns a new instance of ttk.Treeview.

        Args:
            master (tkinter.Misc): The master widget.
            **kwargs: Any additional keyword arguments to be passed to the ttk.Treeview constructor.

        Returns:
            Optional[ttk.Treeview]: The created ttk.Treeview instance.

        Raises:
            Exception: If an exception occurs while attempting to create a new instance of ttk.Treeview.
        """
        try:
            # Attempt to create and return a new instance of ttk.Treeview
            return ttk.Treeview(
                master=master,
                **kwargs,
            )
        except Exception as e:
            # Log an error message indicating an exception occured
            cls.logger.error(
                message=f"Caught an exception while attempting to run 'get_treeview' method from '{cls.__name__}': {e}"
            )

            # Return None indicating an exception occured
            return None
