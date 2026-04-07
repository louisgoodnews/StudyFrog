# GUI Layer Documentation

## Overview

The GUI layer provides the user interface for StudyFrog using CustomTkinter. It follows a modular architecture with separate views, forms, logic, and widget components.

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Main GUI Management](#main-gui-management)
3. [View Components](#view-components)
4. [Form Components](#form-components)
5. [Logic Components](#logic-components)
6. [Custom Widgets](#custom-widgets)
7. [Event Handling](#event-handling)
8. [Navigation System](#navigation-system)

---

## Architecture Overview

### GUI Hierarchy

```
CustomTkinter Root Window
├── Top Frame (navigation, title)
├── Center Frame (main content area)
│   ├── Dashboard View
│   ├── Create View
│   ├── Edit View
│   ├── Rehearsal Views
│   └── Other Views
└── Bottom Frame (status, actions)
```

### Component Organization

```
gui/
├── gui.py              # Main GUI management
├── views/              # Main view components
│   ├── dashboard_view.py
│   ├── create_view.py
│   ├── edit_view.py
│   ├── rehearsal_run_view.py
│   └── ...
├── forms/              # Data entry forms
│   ├── flashcard_create_form.py
│   ├── stack_create_form.py
│   ├── question_create_form.py
│   └── ...
├── logic/              # Business logic
│   ├── create_view_logic.py
│   ├── edit_view_logic.py
│   ├── rehearsal_run_view_logic.py
│   └── ...
└── widgets.py          # Custom widgets
```

### Design Principles

1. **Separation of Concerns**: Views, forms, and logic are separate
2. **Event-Driven**: GUI components communicate through events
3. **Responsive**: Adapts to different screen sizes
4. **Consistent**: Uniform styling and behavior
5. **Accessible**: Keyboard navigation and screen reader support

---

## Main GUI Management

### gui.py - Main GUI Controller

#### Purpose

The main GUI module manages the overall GUI structure, frame access, and global GUI state.

#### Key Components

##### Frame Management

```python
def get_root() -> Optional[ctk.CTk]:
    """Get the main application window."""

def get_top_frame() -> Optional[ctk.CTkFrame]:
    """Get the top frame for navigation."""

def get_center_frame() -> Optional[ctk.CTkFrame]:
    """Get the center frame for main content."""

def get_bottom_frame() -> Optional[ctk.CTkFrame]:
    """Get the bottom frame for status and actions."""
```

##### Frame Configuration

```python
def configure_frames() -> None:
    """Configure the main frame structure and layout."""

def reset_frame_grids() -> None:
    """Reset all frame grids for new content."""

def clear_frames() -> None:
    """Clear all frames of their current content."""
```

##### Window Management

```python
def setup_main_window() -> None:
    """Set up the main application window."""

def configure_window_properties() -> None:
    """Configure window size, title, and properties."""

def center_window() -> None:
    """Center the window on the screen."""
```

#### Usage Example

```python
# Initialize GUI
setup_main_window()
configure_frames()

# Access frames
top_frame = get_top_frame()
center_frame = get_center_frame()
bottom_frame = get_bottom_frame()

# Clear and setup new content
clear_center_frame()
setup_new_view()
```

---

## View Components

### Dashboard View

#### Purpose

Main dashboard providing overview and navigation to all features.

#### Key Features

- **Summary Statistics**: Total flashcards, stacks, recent activity
- **Quick Actions**: Create new items, start rehearsal
- **Navigation**: Access to all major features
- **Recent Items**: Recently created or studied items

#### Implementation

```python
def get_dashboard_view() -> ctk.CTkFrame:
    """
    Create and return the dashboard view.
    
    Returns:
        ctk.CTkFrame: Dashboard view frame
    """
```

#### Components

```python
# Summary Section
def create_summary_section(parent: ctk.CTkFrame) -> ctk.CTkFrame:
    """Create summary statistics section."""

# Quick Actions
def create_quick_actions_section(parent: ctk.CTkFrame) -> ctk.CTkFrame:
    """Create quick action buttons."""

# Recent Items
def create_recent_items_section(parent: ctk.CTkFrame) -> ctk.CTkFrame:
    """Create recent items display."""
```

### Create View

#### Purpose

Unified interface for creating new content (flashcards, stacks, questions, notes).

#### Implementation

```python
def get_create_view() -> ctk.CTkFrame:
    """
    Create and return the create view with tabs for different content types.
    
    Returns:
        ctk.CTkFrame: Create view frame
    """
```

#### Tab Structure

```python
# Tab Management
def create_content_type_tabs(parent: ctk.CTkFrame) -> ctk.CTkTabview:
    """Create tabbed interface for different content types."""

# Tab Content
def setup_flashcard_tab(tab: ctk.CTkFrame) -> None:
    """Setup flashcard creation tab."""

def setup_stack_tab(tab: ctk.CTkFrame) -> None:
    """Setup stack creation tab."""

def setup_question_tab(tab: ctk.CTkFrame) -> None:
    """Setup question creation tab."""

def setup_note_tab(tab: ctk.CTkFrame) -> None:
    """Setup note creation tab."""
```

### Edit View

#### Purpose

Interface for editing existing content with search and selection capabilities.

#### Implementation

```python
def get_edit_view() -> ctk.CTkFrame:
    """
    Create and return the edit view.
    
    Returns:
        ctk.CTkFrame: Edit view frame
    """
```

#### Components

```python
# Search and Filter
def create_search_section(parent: ctk.CTkFrame) -> ctk.CTkFrame:
    """Create search and filter controls."""

# Item List
def create_item_list_section(parent: ctk.CTkFrame) -> ctk.CTkFrame:
    """Create list of editable items."""

# Edit Form
def create_edit_form_section(parent: ctk.CTkFrame) -> ctk.CTkFrame:
    """Create form for editing selected item."""
```

### Rehearsal Views

#### Rehearsal Run Setup View

Purpose: Configure rehearsal sessions before starting.

```python
def get_rehearsal_run_setup_view() -> ctk.CTkFrame:
    """Create rehearsal setup interface."""
```

**Features**:
- Select content type (flashcards, questions)
- Choose stacks or individual items
- Set session parameters (max items, time limit)
- Preview selected content

#### Rehearsal Run View

Purpose: Main rehearsal interface for presenting items and collecting responses.

```python
def get_rehearsal_run_view() -> ctk.CTkFrame:
    """Create main rehearsal interface."""
```

**Features**:
- Display current item
- Collect user response
- Show feedback
- Track progress
- Timer and scoring

#### Rehearsal Run Result View

Purpose: Display rehearsal session results and statistics.

```python
def get_rehearsal_run_result_view() -> ctk.CTkFrame:
    """Create results display interface."""
```

**Features**:
- Session summary
- Performance statistics
- Item-by-item results
- Export options

---

## Form Components

### Flashcard Create Form

#### Purpose

Form for creating new flashcards with validation and preview.

```python
def get_flashcard_create_form(parent: ctk.CTkFrame) -> ctk.CTkFrame:
    """
    Create flashcard creation form.
    
    Args:
        parent: Parent frame
        
    Returns:
        ctk.CTkFrame: Flashcard form frame
    """
```

#### Form Fields

```python
# Basic Fields
def create_basic_fields(parent: ctk.CTkFrame) -> dict[str, ctk.CTkEntry]:
    """Create front/back text fields."""

# Metadata Fields
def create_metadata_fields(parent: ctk.CTkFrame) -> dict[str, ctk.CTkComboBox]:
    """Create difficulty, priority, subject fields."""

# Custom Fields
def create_custom_fields_section(parent: ctk.CTkFrame) -> ctk.CTkFrame:
    """Create custom fields section."""
```

#### Validation

```python
def validate_flashcard_form(form_data: dict) -> tuple[bool, list[str]]:
    """
    Validate flashcard form data.
    
    Returns:
        tuple: (is_valid, error_messages)
    """
```

### Stack Create Form

#### Purpose

Form for creating new stacks with organization options.

```python
def get_stack_create_form(parent: ctk.CTkFrame) -> ctk.CTkFrame:
    """Create stack creation form."""
```

#### Features

- Stack name and description
- Parent/child relationships
- Subject and teacher assignment
- Initial item selection

### Question Create Form

#### Purpose

Form for creating questions with different answer types.

```python
def get_question_create_form(parent: ctk.CTkFrame) -> ctk.CTkFrame:
    """Create question creation form."""
```

#### Question Types

```python
# Open Ended
def get_open_ended_create_form(parent: ctk.CTkFrame) -> ctk.CTkFrame:
    """Create open-ended question form."""

# Multiple Choice
def get_multiple_choice_create_form(parent: ctk.CTkFrame) -> ctk.CTkFrame:
    """Create multiple choice question form."""

# True/False
def get_true_false_create_form(parent: ctk.CTkFrame) -> ctk.CTkFrame:
    """Create true/false question form."""
```

---

## Logic Components

### Create View Logic

#### Purpose

Business logic for creating new content items.

```python
# In create_view_logic.py

def handle_flashcard_creation(form_data: dict) -> bool:
    """
    Handle flashcard creation from form data.
    
    Args:
        form_data: Dictionary from form
        
    Returns:
        bool: True if successful
    """
```

#### Key Functions

```python
# Form Processing
def process_form_data(form_type: str, form_data: dict) -> Optional[Model]:
    """Process form data and create model instance."""

# Validation
def validate_form_data(form_type: str, form_data: dict) -> tuple[bool, list[str]]:
    """Validate form data for specific form type."""

# Storage
def save_new_model(model: Model) -> bool:
    """Save new model to storage."""

# Feedback
def show_creation_success(model: Model) -> None:
    """Show success feedback to user."""

def show_creation_errors(errors: list[str]) -> None:
    """Show error messages to user."""
```

### Edit View Logic

#### Purpose

Business logic for editing existing content.

```python
# In edit_view_logic.py

def handle_item_update(model_key: str, form_data: dict) -> bool:
    """
    Handle item update from form data.
    
    Args:
        model_key: Key of model to update
        form_data: Updated form data
        
    Returns:
        bool: True if successful
    """
```

#### Key Functions

```python
# Load and Display
def load_item_for_edit(model_key: str) -> Optional[Model]:
    """Load model for editing."""

def populate_edit_form(model: Model, form_fields: dict) -> None:
    """Populate form fields with model data."""

# Update Processing
def process_update(model: Model, form_data: dict) -> Model:
    """Process form data and update model."""

# Save Changes
def save_model_changes(model: Model) -> bool:
    """Save model changes to storage."""
```

### Rehearsal Run Logic

#### Purpose

Business logic for managing rehearsal sessions.

```python
# In rehearsal_run_view_logic.py

def start_rehearsal_session(config: dict) -> Optional[RehearsalRunModel]:
    """
    Start a new rehearsal session.
    
    Args:
        config: Session configuration
        
    Returns:
        RehearsalRunModel: Created session or None
    """
```

#### Key Functions

```python
# Session Management
def initialize_rehearsal_session(config: dict) -> RehearsalRunModel:
    """Initialize new rehearsal session."""

def get_next_item(session: RehearsalRunModel) -> Optional[Model]:
    """Get next item for rehearsal."""

def record_response(session: RehearsalRunModel, item_key: str, response: str) -> None:
    """Record user response for item."""

# Progress Tracking
def update_session_progress(session: RehearsalRunModel) -> None:
    """Update session progress statistics."""

def finalize_session(session: RehearsalRunModel) -> None:
    """Finalize session and calculate results."""
```

---

## Custom Widgets

### Toast Notifications

#### Purpose

Provide feedback to users through temporary notifications.

```python
# In widgets.py

def get_success_toast(message: str) -> ctk.CTkFrame:
    """Create success toast notification."""

def get_error_toast(message: str) -> ctk.CTkFrame:
    """Create error toast notification."""

def get_warning_toast(message: str) -> ctk.CTkFrame:
    """Create warning toast notification."""

def get_info_toast(message: str) -> ctk.CTkFrame:
    """Create info toast notification."""
```

#### Implementation

```python
class ToastNotification:
    def __init__(self, parent: ctk.CTk, message: str, toast_type: str):
        self.parent = parent
        self.message = message
        self.toast_type = toast_type
        self.frame = None
        self.auto_hide_timer = None
    
    def show(self) -> None:
        """Show the toast notification."""
        
    def hide(self) -> None:
        """Hide the toast notification."""
        
    def auto_hide(self, delay: int = 3000) -> None:
        """Automatically hide after delay."""
```

### Enhanced Entry Widgets

#### Purpose

Provide enhanced input widgets with validation and formatting.

```python
def get_validated_entry(parent: ctk.CTkFrame, validator: Callable) -> ctk.CTkEntry:
    """Create entry with built-in validation."""

def get_multiline_entry(parent: ctk.CTkFrame) -> ctk.CTkTextbox:
    """Create multiline text entry."""

def get_search_entry(parent: ctk.CTkFrame) -> ctk.CTkEntry:
    """Create search entry with clear button."""
```

### Data Display Widgets

#### Purpose

Widgets for displaying data in various formats.

```python
def get_item_list_widget(parent: ctk.CTkFrame, items: list[Model]) -> ctk.CTkScrollableFrame:
    """Create scrollable list of items."""

def get_statistics_widget(parent: ctk.CTkFrame, stats: dict) -> ctk.CTkFrame:
    """Create statistics display widget."""

def get_progress_widget(parent: ctk.CTkFrame, progress: float) -> ctk.CTkProgressBar:
    """Create progress bar widget."""
```

---

## Event Handling

### GUI Event Types

#### Navigation Events

```python
from studyfrog.constants.events import (
    GET_DASHBOARD_VIEW,
    GET_CREATE_VIEW,
    GET_EDIT_VIEW,
    GET_REHEARSAL_RUN_SETUP_VIEW,
    GET_REHEARSAL_RUN_VIEW,
    GET_REHEARSAL_RUN_RESULT_VIEW,
)
```

#### CRUD Events

```python
from studyfrog.constants.events import (
    FLASHCARD_CREATED,
    FLASHCARD_UPDATED,
    FLASHCARD_DELETED,
    STACK_CREATED,
    STACK_UPDATED,
    STACK_DELETED,
)
```

#### Rehearsal Events

```python
from studyfrog.constants.events import (
    REHEARSAL_RUN_STARTED,
    REHEARSAL_RUN_ITEM_PRESENTED,
    REHEARSAL_RUN_ITEM_ANSWERED,
    REHEARSAL_RUN_COMPLETED,
)
```

### Event Handlers

#### Navigation Handlers

```python
def handle_get_dashboard_view(event_data: dict) -> None:
    """Handle dashboard view request."""
    clear_center_frame()
    dashboard_view = get_dashboard_view()
    get_center_frame().pack(fill="both", expand=True)

def handle_get_create_view(event_data: dict) -> None:
    """Handle create view request."""
    content_type = event_data.get('content_type', 'flashcard')
    clear_center_frame()
    create_view = get_create_view(content_type=content_type)
    get_center_frame().pack(fill="both", expand=True)
```

#### CRUD Handlers

```python
def handle_flashcard_created(event_data: dict) -> None:
    """Handle flashcard creation event."""
    flashcard = event_data.get('flashcard')
    if flashcard:
        show_success_toast(f"Flashcard '{flashcard.front}' created successfully")
        refresh_dashboard()
        update_flashcard_list()

def handle_flashcard_updated(event_data: dict) -> None:
    """Handle flashcard update event."""
    flashcard = event_data.get('flashcard')
    if flashcard:
        show_success_toast(f"Flashcard '{flashcard.front}' updated successfully")
        refresh_current_view()
```

### Event Subscription

```python
# In bootstrap.py or view initialization

def subscribe_to_gui_events() -> None:
    """Subscribe to all GUI-related events."""
    
    # Navigation events
    subscribe(GET_DASHBOARD_VIEW, handle_get_dashboard_view)
    subscribe(GET_CREATE_VIEW, handle_get_create_view)
    subscribe(GET_EDIT_VIEW, handle_get_edit_view)
    
    # CRUD events
    subscribe(FLASHCARD_CREATED, handle_flashcard_created)
    subscribe(FLASHCARD_UPDATED, handle_flashcard_updated)
    subscribe(FLASHCARD_DELETED, handle_flashcard_deleted)
    
    # Rehearsal events
    subscribe(REHEARSAL_RUN_STARTED, handle_rehearsal_run_started)
    subscribe(REHEARSAL_RUN_COMPLETED, handle_rehearsal_run_completed)
```

---

## Navigation System

### Navigation Pattern

The GUI uses an event-driven navigation system:

```
User Action → Navigation Event → Event Handler → View Switch
```

### Navigation Events

```python
# View switching
dispatch(GET_DASHBOARD_VIEW, {})
dispatch(GET_CREATE_VIEW, {'content_type': 'flashcard'})
dispatch(GET_EDIT_VIEW, {'model_key': 'FLASHCARD_1'})
dispatch(GET_REHEARSAL_RUN_SETUP_VIEW, {})

# Modal dialogs
dispatch(SHOW_CONFIRMATION_DIALOG, {
    'title': 'Delete Item',
    'message': 'Are you sure you want to delete this item?',
    'callback': confirm_delete_callback
})
```

### View Management

```python
def switch_view(new_view: ctk.CTkFrame) -> None:
    """Switch to a new view in the center frame."""
    center_frame = get_center_frame()
    
    # Clear current content
    for widget in center_frame.winfo_children():
        widget.destroy()
    
    # Add new view
    new_view.pack(fill="both", expand=True)
    
    # Update navigation state
    update_navigation_state(new_view)
```

### State Management

```python
# Navigation state
navigation_state = {
    'current_view': None,
    'previous_view': None,
    'view_history': [],
    'view_parameters': {}
}

def update_navigation_state(view: ctk.CTkFrame) -> None:
    """Update navigation state when switching views."""
    current_view = navigation_state['current_view']
    
    if current_view:
        navigation_state['previous_view'] = current_view
        navigation_state['view_history'].append(current_view)
    
    navigation_state['current_view'] = view
```

---

## GUI Layer Best Practices

### 1. Use Event-Driven Communication

```python
# Good - use events
dispatch(FLASHCARD_CREATED, {'flashcard': flashcard})

# Avoid - direct method calls
other_view.update_flashcard_list(flashcard)  # Tightly coupled
```

### 2. Separate View and Logic

```python
# In view
def on_save_button_click() -> None:
    form_data = get_form_data()
    success, errors = create_view_logic.handle_flashcard_creation(form_data)
    
    if not success:
        show_validation_errors(errors)

# In logic
def handle_flashcard_creation(form_data: dict) -> tuple[bool, list[str]]:
    # Business logic only, no GUI code
    pass
```

### 3. Validate Input Early

```python
def validate_form_input(input_value: str, field_name: str) -> tuple[bool, str]:
    """Validate individual form field."""
    if not input_value.strip():
        return False, f"{field_name} cannot be empty"
    
    if len(input_value) > MAX_LENGTH:
        return False, f"{field_name} too long"
    
    return True, ""
```

### 4. Provide User Feedback

```python
def show_operation_result(success: bool, message: str) -> None:
    """Show appropriate feedback based on operation result."""
    if success:
        show_success_toast(message)
    else:
        show_error_toast(message)
```

### 5. Handle Errors Gracefully

```python
def handle_gui_error(error: Exception, context: str) -> None:
    """Handle GUI errors with user-friendly messages."""
    log_error(f"GUI Error in {context}: {error}")
    show_error_toast("An error occurred. Please try again.")
```

### 6. Use Consistent Styling

```python
# Define common styles
STYLE_CONFIG = {
    'button_color': '#1e90ff',
    'text_color': '#ffffff',
    'font_size': 12,
    'padding': 10
}

def apply_style(widget: ctk.CTkWidget, style_type: str) -> None:
    """Apply consistent styling to widgets."""
    config = STYLE_CONFIG.get(style_type, {})
    widget.configure(**config)
```

The GUI layer provides a comprehensive, user-friendly interface for StudyFrog while maintaining clean architecture and good separation of concerns.
