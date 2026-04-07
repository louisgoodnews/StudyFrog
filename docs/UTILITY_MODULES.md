# Utility Modules Documentation

## Overview

The utility modules provide essential services that support the entire application, including data persistence, event handling, logging, and common helper functions.

## Table of Contents

1. [Storage Module](#storage-module)
2. [Event Dispatcher](#event-dispatcher)
3. [Logging System](#logging-system)
4. [Common Utilities](#common-utilities)
5. [File Management](#file-management)
6. [Directory Management](#directory-management)

---

## Storage Module

### Purpose

The storage module provides a unified interface for data persistence using JSON files, with support for CRUD operations, batch processing, and data integrity.

### Key Components

#### File Structure

```
.local/data/
├── flashcards.json      # Flashcard data
├── stacks.json          # Stack organization
├── questions.json       # Question data
├── answers.json         # Answer data
├── notes.json          # Note data
├── rehearsal_runs.json # Rehearsal sessions
├── rehearsal_run_items.json # Individual rehearsal items
├── difficulties.json    # Difficulty definitions
├── priorities.json     # Priority definitions
├── subjects.json      # Subject definitions
├── tags.json         # Tag definitions
├── teachers.json      # Teacher definitions
├── users.json        # User data
├── customfields.json  # Custom field definitions
├── associations.json  # Many-to-many relationships
└── config.json      # Application configuration
```

#### Database File Format

```json
{
    "created_at": "2026-01-01T10:00:00.000000",
    "created_on": "2026-01-01",
    "entries": {
        "entries": {
            "0": {
                "id": 0,
                "key": "FLASHCARD_0",
                "uuid": "550e8400-e29b-41d4-a716-446655440000",
                "type_": "FLASHCARD",
                "front": "What is the capital of France?",
                "back": "Paris",
                "difficulty": "Easy",
                "priority": "Medium",
                "subject": "Geography",
                "teacher": "",
                "customfields": [],
                "tags": [],
                "is_assigned_to_stack": false,
                "last_viewed_at": null,
                "last_viewed_on": null,
                "next_view_on": null,
                "author": "",
                "created_at": "2026-01-01T10:00:00.000000",
                "created_on": "2026-01-01",
                "updated_at": "2026-01-01T10:00:00.000000",
                "updated_on": "2026-01-01",
                "metadata": {
                    "author": "",
                    "created_at": "2026-01-01T10:00:00.000000",
                    "created_on": "2026-01-01",
                    "fields": {
                        "total": 22,
                        "values": ["self", "back", "front", ...]
                    },
                    "type": "FLASHCARD",
                    "updated_at": "2026-01-01T10:00:00.000000",
                    "updated_on": "2026-01-01"
                }
            }
        },
        "total": 1
    },
    "metadata": {
        "available_ids": [],
        "fields": {
            "fields": ["back", "customfields", "difficulty", ...],
            "total": 12
        },
        "next_id": 1,
        "schema": {}
    },
    "updated_at": "2026-01-01T10:00:00.000000",
    "updated_on": "2026-01-01",
    "uuid": "550e8400-e29b-41d4-a716-446655440001"
}
```

### Core Functions

#### Basic CRUD Operations

```python
def get_entry(file_path: Path, key: str) -> Optional[dict]:
    """
    Retrieve a specific entry from a storage file.
    
    Args:
        file_path: Path to the JSON file
        key: The key of the entry to retrieve
        
    Returns:
        dict: Entry data or None if not found
    """

def get_all_entries(file_path: Path) -> list[dict]:
    """
    Retrieve all entries from a storage file.
    
    Args:
        file_path: Path to the JSON file
        
    Returns:
        list: All entries in the file
    """

def get_entries(file_path: Path, keys: list[str]) -> list[dict]:
    """
    Retrieve specific entries by their keys.
    
    Args:
        file_path: Path to the JSON file
        keys: List of keys to retrieve
        
    Returns:
        list: List of entries (may be fewer than requested)
    """

def add_entry(file_path: Path, model: Model) -> bool:
    """
    Add a new entry to a storage file.
    
    Args:
        file_path: Path to the JSON file
        model: Model instance to add
        
    Returns:
        bool: True if successful
    """

def update_entry(file_path: Path, model: Model) -> bool:
    """
    Update an existing entry in a storage file.
    
    Args:
        file_path: Path to the JSON file
        model: Model instance with updated data
        
    Returns:
        bool: True if successful
    """

def delete_entry(file_path: Path, key: str) -> bool:
    """
    Delete an entry from a storage file.
    
    Args:
        file_path: Path to the JSON file
        key: The key of the entry to delete
        
    Returns:
        bool: True if successful
    """
```

#### Batch Operations

```python
def add_entries(file_path: Path, models: list[Model]) -> bool:
    """
    Add multiple entries to a storage file.
    
    Args:
        file_path: Path to the JSON file
        models: List of model instances to add
        
    Returns:
        bool: True if all successful
    """

def update_entries(file_path: Path, models: list[Model]) -> bool:
    """
    Update multiple entries in a storage file.
    
    Args:
        file_path: Path to the JSON file
        models: List of model instances with updated data
        
    Returns:
        bool: True if all successful
    """

def delete_entries(file_path: Path, keys: list[str]) -> bool:
    """
    Delete multiple entries from a storage file.
    
    Args:
        file_path: Path to the JSON file
        keys: List of keys to delete
        
    Returns:
        bool: True if all successful
    """

def delete_all_entries(file_path: Path) -> bool:
    """
    Delete all entries from a storage file.
    
    Args:
        file_path: Path to the JSON file
        
    Returns:
        bool: True if successful
    """
```

#### Conditional Operations

```python
def add_entry_if_not_exist(file_path: Path, model: Model) -> bool:
    """
    Add entry only if it doesn't already exist.
    
    Args:
        file_path: Path to the JSON file
        model: Model instance to add
        
    Returns:
        bool: True if added, False if already exists
    """

def add_entries_if_not_exist(file_path: Path, models: list[Model]) -> int:
    """
    Add entries only if they don't already exist.
    
    Args:
        file_path: Path to the JSON file
        models: List of model instances to add
        
    Returns:
        int: Number of entries actually added
    """
```

#### Search and Filter

```python
def filter_entries(file_path: Path, filter_func: Callable) -> list[dict]:
    """
    Filter entries using a custom function.
    
    Args:
        file_path: Path to the JSON file
        filter_func: Function that takes an entry and returns bool
        
    Returns:
        list: Filtered entries
    """

def search_entries(file_path: Path, search_term: str, fields: list[str]) -> list[dict]:
    """
    Search entries for a term in specific fields.
    
    Args:
        file_path: Path to the JSON file
        search_term: Term to search for
        fields: List of field names to search in
        
    Returns:
        list: Entries matching the search term
    """
```

#### Data Integrity

```python
def validate_storage_file(file_path: Path) -> tuple[bool, list[str]]:
    """
    Validate the structure and integrity of a storage file.
    
    Args:
        file_path: Path to the JSON file
        
    Returns:
        tuple: (is_valid, error_messages)
    """

def repair_storage_file(file_path: Path) -> bool:
    """
    Attempt to repair a corrupted storage file.
    
    Args:
        file_path: Path to the JSON file
        
    Returns:
        bool: True if repair was successful
    """

def backup_storage_file(file_path: Path) -> bool:
    """
    Create a backup of a storage file.
    
    Args:
        file_path: Path to the JSON file
        
    Returns:
        bool: True if backup was successful
    """
```

### Usage Examples

```python
from studyfrog.utils.storage import get_entry, add_entry, update_entry
from studyfrog.models.factory import get_flashcard_model
from studyfrog.constants.files import FLASHCARDS_DB_JSON

# Create a new flashcard
flashcard = get_flashcard_model(
    front="What is the capital of Germany?",
    back="Berlin"
)

# Save to storage
success = add_entry(FLASHCARDS_DB_JSON, flashcard)

# Retrieve existing flashcard
flashcard_data = get_entry(FLASHCARDS_DB_JSON, "FLASHCARD_1")

# Update flashcard
if flashcard_data:
    flashcard.front = "Updated question"
    success = update_entry(FLASHCARDS_DB_JSON, flashcard)
```

---

## Event Dispatcher

### Purpose

The event dispatcher provides a decoupled communication system using the publish-subscribe pattern, allowing components to communicate without direct dependencies.

### Architecture

```
Component A → Event → Dispatcher → Component B
                    ↘ Component C
                    ↘ Component D
```

### Core Functions

#### Event Subscription

```python
def subscribe(event_name: str, callback: Callable) -> str:
    """
    Subscribe to an event with a callback function.
    
    Args:
        event_name: Name of the event to subscribe to
        callback: Function to call when event is dispatched
        
    Returns:
        str: Subscription ID for unsubscribing later
    """

def unsubscribe(subscription_id: str) -> bool:
    """
    Unsubscribe from an event using subscription ID.
    
    Args:
        subscription_id: ID returned by subscribe()
        
    Returns:
        bool: True if successfully unsubscribed
    """

def unsubscribe_all(event_name: str) -> int:
    """
    Unsubscribe all callbacks for an event.
    
    Args:
        event_name: Name of the event
        
    Returns:
        int: Number of subscriptions removed
    """
```

#### Event Dispatching

```python
def dispatch(event_name: str, data: dict = None) -> int:
    """
    Dispatch an event to all subscribers.
    
    Args:
        event_name: Name of the event to dispatch
        data: Event data to pass to subscribers
        
    Returns:
        int: Number of subscribers notified
    """

def dispatch_async(event_name: str, data: dict = None) -> None:
    """
    Dispatch an event asynchronously.
    
    Args:
        event_name: Name of the event to dispatch
        data: Event data to pass to subscribers
    """

def dispatch_with_delay(event_name: str, data: dict = None, delay: float = 0.0) -> None:
    """
    Dispatch an event with a delay.
    
    Args:
        event_name: Name of the event to dispatch
        data: Event data to pass to subscribers
        delay: Delay in seconds before dispatching
    """
```

#### Event Management

```python
def get_subscribers(event_name: str) -> list[str]:
    """
    Get list of subscription IDs for an event.
    
    Args:
        event_name: Name of the event
        
    Returns:
        list: List of subscription IDs
    """

def get_all_events() -> list[str]:
    """
    Get list of all events with subscribers.
    
    Returns:
        list: List of event names
    """

def clear_all_subscriptions() -> None:
    """Clear all event subscriptions."""
```

### Event Data Structure

```python
# Standard event data format
event_data = {
    'source': 'component_name',      # Who dispatched the event
    'timestamp': datetime.now(),       # When the event was dispatched
    'data': {                        # Event-specific data
        'model': model_instance,
        'action': 'created',
        'old_value': old_value,
        'new_value': new_value
    }
}
```

### Usage Examples

```python
from studyfrog.utils.dispatcher import dispatch, subscribe, unsubscribe

# Define event handler
def on_flashcard_created(event_data: dict) -> None:
    """Handle flashcard creation events."""
    flashcard = event_data.get('data', {}).get('model')
    if flashcard:
        print(f"Flashcard created: {flashcard.front}")
        # Update GUI, refresh lists, etc.

# Subscribe to event
subscription_id = subscribe('FLASHCARD_CREATED', on_flashcard_created)

# Dispatch event
dispatch('FLASHCARD_CREATED', {
    'model': flashcard,
    'action': 'created'
})

# Unsubscribe when done
unsubscribe(subscription_id)
```

### Event Categories

#### Application Lifecycle Events

```python
APPLICATION_STARTING = "APPLICATION_STARTING"
APPLICATION_STARTED = "APPLICATION_STARTED"
APPLICATION_STOPPING = "APPLICATION_STOPPING"
APPLICATION_STOPPED = "APPLICATION_STOPPED"
```

#### Navigation Events

```python
GET_DASHBOARD_VIEW = "GET_DASHBOARD_VIEW"
GET_CREATE_VIEW = "GET_CREATE_VIEW"
GET_EDIT_VIEW = "GET_EDIT_VIEW"
GET_REHEARSAL_RUN_SETUP_VIEW = "GET_REHEARSAL_RUN_SETUP_VIEW"
GET_REHEARSAL_RUN_VIEW = "GET_REHEARSAL_RUN_VIEW"
GET_REHEARSAL_RUN_RESULT_VIEW = "GET_REHEARSAL_RUN_RESULT_VIEW"
```

#### CRUD Events

```python
FLASHCARD_CREATED = "FLASHCARD_CREATED"
FLASHCARD_UPDATED = "FLASHCARD_UPDATED"
FLASHCARD_DELETED = "FLASHCARD_DELETED"
STACK_CREATED = "STACK_CREATED"
STACK_UPDATED = "STACK_UPDATED"
STACK_DELETED = "STACK_DELETED"
```

#### Rehearsal Events

```python
REHEARSAL_RUN_STARTED = "REHEARSAL_RUN_STARTED"
REHEARSAL_RUN_ITEM_PRESENTED = "REHEARSAL_RUN_ITEM_PRESENTED"
REHEARSAL_RUN_ITEM_ANSWERED = "REHEARSAL_RUN_ITEM_ANSWERED"
REHEARSAL_RUN_COMPLETED = "REHEARSAL_RUN_COMPLETED"
```

---

## Logging System

### Purpose

The logging system provides structured logging with different levels, file output, and performance monitoring.

### Log Levels

```python
LOG_LEVELS = {
    'TRACE': 0,    # Detailed debugging information
    'DEBUG': 1,     # Debugging information
    'INFO': 2,      # General information
    'WARNING': 3,   # Warning messages
    'ERROR': 4,      # Error messages
    'CRITICAL': 5    # Critical errors
}
```

### Core Functions

#### Basic Logging

```python
def log_trace(message: str, name: str = None, **kwargs) -> None:
    """Log trace-level message."""

def log_debug(message: str, name: str = None, **kwargs) -> None:
    """Log debug-level message."""

def log_info(message: str, name: str = None, **kwargs) -> None:
    """Log info-level message."""

def log_warning(message: str, name: str = None, **kwargs) -> None:
    """Log warning-level message."""

def log_error(message: str, name: str = None, **kwargs) -> None:
    """Log error-level message."""

def log_critical(message: str, name: str = None, **kwargs) -> None:
    """Log critical-level message."""
```

#### Advanced Logging

```python
def log_with_level(level: str, message: str, name: str = None, **kwargs) -> None:
    """
    Log message at specific level.
    
    Args:
        level: Log level name
        message: Message to log
        name: Component name
        **kwargs: Additional context
    """

def log_exception(exception: Exception, message: str = None, name: str = None) -> None:
    """
    Log exception with traceback.
    
    Args:
        exception: Exception to log
        message: Additional message
        name: Component name
    """

def log_performance(operation: str, duration: float, name: str = None) -> None:
    """
    Log performance metrics.
    
    Args:
        operation: Operation name
        duration: Duration in seconds
        name: Component name
    """
```

#### Configuration

```python
def set_log_level(level: str) -> None:
    """Set the minimum log level."""

def set_log_file(file_path: Path) -> None:
    """Set the log file path."""

def enable_console_output(enabled: bool) -> None:
    """Enable or disable console output."""

def set_log_format(format_string: str) -> None:
    """Set the log message format."""
```

### Log Format

```python
# Default log format
LOG_FORMAT = "{timestamp} - [{level}] - [{name}] - {message}"

# Example output
2026-04-06T10:30:45.123456 - [INFO] - [STORAGE] - Flashcard saved successfully
2026-04-06T10:30:46.789012 - [ERROR] - [GUI] - Failed to create flashcard: Validation error
```

### Usage Examples

```python
from studyfrog.utils.logging import log_info, log_error, log_performance

# Basic logging
log_info("Application started", "MAIN")

# Error logging
try:
    # Some operation
    pass
except Exception as e:
    log_error(f"Operation failed: {e}", "STORAGE")

# Performance logging
import time
start_time = time.time()
# Perform operation
duration = time.time() - start_time
log_performance("Database query", duration, "STORAGE")
```

---

## Common Utilities

### Purpose

Common utilities provide frequently used helper functions across the application.

### String Utilities

```python
def pluralize_word(word: str, count: int) -> str:
    """
    Return plural form of word based on count.
    
    Args:
        word: Word to pluralize
        count: Number to determine pluralization
        
    Returns:
        str: Pluralized word
    """

def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate text to maximum length.
    
    Args:
        text: Text to truncate
        max_length: Maximum length
        suffix: Suffix to add if truncated
        
    Returns:
        str: Truncated text
    """

def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename for safe file system usage.
    
    Args:
        filename: Original filename
        
    Returns:
        str: Sanitized filename
    """
```

### Validation Utilities

```python
def is_valid_email(email: str) -> bool:
    """Validate email address format."""

def is_valid_uuid(uuid_string: str) -> bool:
    """Validate UUID string format."""

def is_valid_json(json_string: str) -> bool:
    """Validate JSON string format."""

def is_valid_date(date_string: str, format: str = "%Y-%m-%d") -> bool:
    """Validate date string format."""
```

### Conversion Utilities

```python
def string_to_bool(value: str) -> bool:
    """Convert string to boolean."""

def bytes_to_human_readable(bytes_value: int) -> str:
    """Convert bytes to human readable format."""

def seconds_to_human_readable(seconds: int) -> str:
    """Convert seconds to human readable time format."""
```

### Data Structure Utilities

```python
def deep_merge_dict(dict1: dict, dict2: dict) -> dict:
    """Deep merge two dictionaries."""

def flatten_dict(nested_dict: dict, separator: str = ".") -> dict:
    """Flatten nested dictionary."""

def remove_duplicates_preserve_order(sequence: list) -> list:
    """Remove duplicates while preserving order."""
```

### Usage Examples

```python
from studyfrog.utils.common import pluralize_word, truncate_text, is_valid_email

# String utilities
count = 5
text = f"{count} {pluralize_word('item', count)}"  # "5 items"
short_text = truncate_text("This is a very long text", 10)  # "This is..."

# Validation
if is_valid_email("user@example.com"):
    print("Valid email")
```

---

## File Management

### Purpose

File management utilities provide safe file operations with error handling and atomic writes.

### Core Functions

```python
def safe_read_file(file_path: Path) -> Optional[str]:
    """
    Safely read file contents.
    
    Args:
        file_path: Path to file
        
    Returns:
        str: File contents or None if error
    """

def safe_write_file(file_path: Path, content: str, backup: bool = True) -> bool:
    """
    Safely write file contents with atomic operation.
    
    Args:
        file_path: Path to file
        content: Content to write
        backup: Whether to create backup
        
    Returns:
        bool: True if successful
    """

def atomic_write_file(file_path: Path, content: str) -> bool:
    """
    Write file atomically to prevent corruption.
    
    Args:
        file_path: Path to file
        content: Content to write
        
    Returns:
        bool: True if successful
    """

def backup_file(file_path: Path, backup_dir: Path = None) -> bool:
    """
    Create backup of file.
    
    Args:
        file_path: Path to file to backup
        backup_dir: Directory for backup (default: same directory)
        
    Returns:
        bool: True if successful
    """

def get_file_info(file_path: Path) -> dict:
    """
    Get comprehensive file information.
    
    Args:
        file_path: Path to file
        
    Returns:
        dict: File information (size, modified, etc.)
    """
```

### JSON Operations

```python
def safe_read_json(file_path: Path) -> Optional[dict]:
    """
    Safely read JSON file.
    
    Args:
        file_path: Path to JSON file
        
    Returns:
        dict: Parsed JSON or None if error
    """

def safe_write_json(file_path: Path, data: dict, indent: int = 2) -> bool:
    """
    Safely write JSON file.
    
    Args:
        file_path: Path to JSON file
        data: Data to write
        indent: JSON indentation
        
    Returns:
        bool: True if successful
    """

def validate_json_structure(data: dict, required_keys: list) -> tuple[bool, list[str]]:
    """
    Validate JSON structure against required keys.
    
    Args:
        data: JSON data to validate
        required_keys: List of required keys
        
    Returns:
        tuple: (is_valid, missing_keys)
    """
```

### Usage Examples

```python
from studyfrog.utils.files import safe_read_json, safe_write_json, backup_file

# Read JSON safely
data = safe_read_json(Path("config.json"))
if data:
    print("Config loaded successfully")

# Write JSON safely
success = safe_write_json(Path("data.json"), {"key": "value"})

# Create backup
backup_file(Path("important_file.json"))
```

---

## Directory Management

### Purpose

Directory management utilities provide safe directory operations with proper error handling.

### Core Functions

```python
def ensure_directory(dir_path: Path) -> bool:
    """
    Ensure directory exists, creating if necessary.
    
    Args:
        dir_path: Path to directory
        
    Returns:
        bool: True if directory exists or was created
    """

def safe_delete_directory(dir_path: Path, recursive: bool = False) -> bool:
    """
    Safely delete directory.
    
    Args:
        dir_path: Path to directory
        recursive: Whether to delete recursively
        
    Returns:
        bool: True if successful
    """

def get_directory_size(dir_path: Path) -> int:
    """
    Get total size of directory in bytes.
    
    Args:
        dir_path: Path to directory
        
    Returns:
        int: Total size in bytes
    """

def list_directory_contents(dir_path: Path, pattern: str = "*") -> list[Path]:
    """
    List directory contents with optional pattern matching.
    
    Args:
        dir_path: Path to directory
        pattern: Glob pattern for matching
        
    Returns:
        list: List of file/directory paths
    """

def find_files(dir_path: Path, pattern: str, recursive: bool = True) -> list[Path]:
    """
    Find files matching pattern.
    
    Args:
        dir_path: Path to search
        pattern: Glob pattern
        recursive: Whether to search recursively
        
    Returns:
        list: List of matching file paths
    """
```

### Usage Examples

```python
from studyfrog.utils.directories import ensure_directory, find_files

# Ensure directory exists
ensure_directory(Path(".local/data"))

# Find all JSON files
json_files = find_files(Path(".local/data"), "*.json")

# Get directory size
size = get_directory_size(Path(".local"))
print(f"Directory size: {size} bytes")
```

---

## Utility Modules Best Practices

### 1. Use Safe Operations

```python
# Good - use safe operations
data = safe_read_json(file_path)
if data:
    process_data(data)

# Avoid - direct operations
with open(file_path, 'r') as f:  # No error handling
    data = json.load(f)
```

### 2. Validate Input

```python
def process_user_input(user_input: str) -> None:
    if not user_input or not user_input.strip():
        log_warning("Empty input received")
        return
    
    # Process valid input
    pass
```

### 3. Log Operations

```python
def perform_operation() -> bool:
    log_info("Starting operation", "MODULE_NAME")
    
    try:
        # Perform operation
        result = do_something()
        log_info("Operation completed successfully", "MODULE_NAME")
        return True
    except Exception as e:
        log_error(f"Operation failed: {e}", "MODULE_NAME")
        return False
```

### 4. Handle Resources Properly

```python
def process_files(file_paths: list[Path]) -> None:
    for file_path in file_paths:
        try:
            with open(file_path, 'r') as f:
                # Process file
                pass
        except Exception as e:
            log_error(f"Failed to process {file_path}: {e}")
            continue  # Continue with next file
```

### 5. Use Appropriate Abstractions

```python
# Good - use storage abstraction
success = add_entry(FLASHCARDS_DB_JSON, flashcard)

# Avoid - direct file manipulation
with open("flashcards.json", 'w') as f:
    json.dump(data, f)  # No validation, no error handling
```

The utility modules provide a solid foundation for data persistence, event handling, logging, and common operations throughout StudyFrog.
