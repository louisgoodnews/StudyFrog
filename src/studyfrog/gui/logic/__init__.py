from __future__ import annotations

# Import all exported functions from individual logic modules

# Create view logic functions
from studyfrog.gui.logic.create_view_logic import (
    on_cancel_button_click,
    on_create_button_click,
    on_stack_combobox_select,
    on_type_combobox_select,
)

# Dashboard view logic functions
from studyfrog.gui.logic.dashboard_view_logic import (
    on_create_button_click,
    on_delete_button_click,
    on_edit_button_click,
)

# Delete confirmation view logic functions
from studyfrog.gui.logic.delete_confirmation_view_logic import (
    on_cancel_button_click,
    on_okay_button_click,
)

# Edit view logic functions
from studyfrog.gui.logic.edit_view_logic import (
    on_cancel_button_click,
    on_delete_button_click,
    on_save_button_click,
)

# Rehearsal run result view logic functions (empty file, included for completeness)
from studyfrog.gui.logic.rehearsal_run_result_view_logic import *

# Rehearsal run setup view logic functions
from studyfrog.gui.logic.rehearsal_run_setup_view_logic import (
    on_cancel_button_click,
    on_start_button_click,
)

# Rehearsal run view logic functions
from studyfrog.gui.logic.rehearsal_run_view_logic import (
    end_rehearsal_run,
    on_cancel_button_click,
    on_easy_button_click,
    on_edit_button_click,
    on_end_button_click,
    on_hard_button_click,
    on_medium_button_click,
    on_next_button_click,
    on_previous_button_click,
    start_rehearsal_run,
)

# Note rehearsal view logic functions (empty file, included for completeness)
from studyfrog.gui.logic.note_rehearsal_view import *

# Export all logic functions
__all__: list[str] = [
    # Create view logic functions
    "on_cancel_button_click",  # create_view
    "on_create_button_click",  # create_view
    "on_stack_combobox_select",
    "on_type_combobox_select",
    # Dashboard view logic functions
    "on_create_button_click",  # dashboard_view
    "on_delete_button_click",  # dashboard_view
    "on_edit_button_click",  # dashboard_view
    # Delete confirmation view logic functions
    "on_cancel_button_click",  # delete_confirmation_view
    "on_okay_button_click",
    # Edit view logic functions
    "on_cancel_button_click",  # edit_view
    "on_delete_button_click",  # edit_view
    "on_save_button_click",
    # Rehearsal run setup view logic functions
    "on_cancel_button_click",  # rehearsal_run_setup_view
    "on_start_button_click",
    # Rehearsal run view logic functions
    "end_rehearsal_run",
    "on_cancel_button_click",  # rehearsal_run_view
    "on_easy_button_click",
    "on_edit_button_click",
    "on_end_button_click",
    "on_hard_button_click",
    "on_medium_button_click",
    "on_next_button_click",
    "on_previous_button_click",
    "start_rehearsal_run",
]
