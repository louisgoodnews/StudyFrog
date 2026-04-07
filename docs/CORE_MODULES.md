# Core Modules Documentation

This document provides detailed documentation for the core modules that form the foundation of StudyFrog.

## Table of Contents

1. [main.py - Application Entry Point](#mainpy---application-entry-point)
2. [core.application - Application Lifecycle](#coreapplication---application-lifecycle)
3. [core.bootstrap - System Initialization](#corebootstrap---system-initialization)
4. [core.common - Shared Core Utilities](#corecommon---shared-core-utilities)

---

## main.py - Application Entry Point

### Purpose

The main module serves as the primary entry point for the StudyFrog application. It handles application initialization, execution, and graceful shutdown.

### Key Components

#### `main()` Function

```python
def main() -> int:
    """
    Primary entry point for the application.
    
    Returns:
        int: Exit code (0 for success, 1 for failure)
    """
```

**Responsibilities**:
- Initialize the application through `start_application()`
- Handle any exceptions during execution
- Perform cleanup through `stop_application()`
- Return appropriate exit codes

**Execution Flow**:
1. Call `start_application()` to initialize and run the app
2. Call `stop_application()` for cleanup
3. Return 0 on success, 1 on failure
4. Log any exceptions that occur

#### Usage

```python
# Direct execution
python -m studyfrog.main

# Programmatic usage
from studyfrog.main import main
exit_code = main()
```

### Error Handling

The main function includes comprehensive error handling:

```python
try:
    start_application()
    stop_application()
    return 0
except Exception as e:
    log_error(message=f"Caught an exception: {e}", name=__NAME__)
    return 1
```

### Constants

- `__NAME__`: Module identifier for logging purposes

---

## core.application - Application Lifecycle

### Purpose

The application module manages the complete lifecycle of the StudyFrog application, from startup through shutdown, including runtime tracking and event coordination.

### Key Components

#### Application Lifecycle Functions

##### `start_application()`

```python
def start_application() -> None:
    """
    Starts the application by running pre-start tasks, initializing GUI,
    running post-start tasks, and starting the main loop.
    """
```

**Execution Steps**:
1. Run pre-start tasks (directory setup, file creation, etc.)
2. Initialize the GUI system
3. Run post-start tasks (event subscriptions, etc.)
4. Dispatch `APPLICATION_STARTED` event
5. Start the GUI main loop

##### `stop_application()`

```python
def stop_application() -> None:
    """
    Stops the application by running pre-stop tasks, stopping the GUI,
    running post-stop tasks, and dispatching stop events.
    """
```

**Execution Steps**:
1. Dispatch `APPLICATION_STOPPING` event
2. Run pre-stop tasks
3. Stop the GUI main loop
4. Run post-stop tasks
5. Dispatch `APPLICATION_STOPPED` event

#### Runtime Management

##### `run_pre_start_tasks()`

```python
def run_pre_start_tasks() -> None:
    """
    Executes tasks that need to run before the GUI is initialized.
    """
```

**Tasks Performed**:
- Ensure required directories exist
- Create necessary database files
- Set up default data if needed
- Initialize storage systems

##### `run_post_start_tasks()`

```python
def run_post_start_tasks() -> None:
    """
    Executes tasks that need to run after the GUI is initialized.
    """
```

**Tasks Performed**:
- Subscribe to application events
- Set up GUI event handlers
- Initialize dashboard view
- Perform any post-initialization setup

#### Runtime Tracking

The module tracks application runtime for analytics and debugging:

```python
def _get_runtime_duration() -> Optional[int]:
    """
    Returns the application runtime duration in seconds.
    """
```

**Runtime Variables**:
- `START`: Application start timestamp
- `STOP`: Application stop timestamp

### Event Integration

The application module integrates with the event system:

```python
from studyfrog.constants.events import (
    APPLICATION_STARTED,
    APPLICATION_STARTING,
    APPLICATION_STOPPED,
    APPLICATION_STOPPING,
    GET_DASHBOARD_VIEW,
)
```

**Events Dispatched**:
- `APPLICATION_STARTING`: Before initialization begins
- `APPLICATION_STARTED`: After initialization completes
- `APPLICATION_STOPPING`: Before shutdown begins
- `APPLICATION_STOPPED`: After shutdown completes

### Dependencies

```python
from studyfrog.core.bootstrap import (
    ensure_directories,
    ensure_files,
    ensure_defaults,
    initialize_gui,
    subscribe_to_events,
    unsubscribe_from_events,
)
from studyfrog.gui.gui import get_root
from studyfrog.utils.dispatcher import dispatch
from studyfrog.utils.logging import log_error, log_info, log_trace
```

### Usage Example

```python
# Starting the application
from studyfrog.core.application import start_application

try:
    start_application()
except KeyboardInterrupt:
    print("Application interrupted by user")
except Exception as e:
    print(f"Application error: {e}")
```

---

## core.bootstrap - System Initialization

### Purpose

The bootstrap module is responsible for initializing all system components required for the application to run. This includes directory structure, database files, default data, GUI components, and event subscriptions.

### Key Components

#### System Initialization Functions

##### `ensure_directories()`

```python
def ensure_directories() -> None:
    """
    Ensures all required directories exist in the application directory structure.
    """
```

**Directories Created**:
- `.local/` - Main local directory
- `.local/data/` - Database files
- `.local/logs/` - Application logs
- `.local/assets/` - Static assets
- `.local/temp/` - Temporary files
- And other required directories

**Implementation**:
```python
from studyfrog.constants.directories import (
    ASSETS_DIR, CONFIG_DIR, DATA_DIR, EXPORTS_DIR,
    IMAGES_DIR, IMPORTS_DIR, LOGS_DIR, RESOURCES_DIR, TEMP_DIR
)

for directory in [DATA_DIR, LOGS_DIR, ASSETS_DIR, ...]:
    ensure_directory(directory)
```

##### `ensure_files()`

```python
def ensure_files() -> None:
    """
    Ensures all required database files exist and are properly initialized.
    """
```

**Files Created**:
- `flashcards.json` - Flashcard data
- `stacks.json` - Stack organization
- `questions.json` - Question data
- `answers.json` - Answer data
- `notes.json` - Note data
- `rehearsal_runs.json` - Rehearsal sessions
- And other database files

**File Structure**:
```json
{
    "created_at": "timestamp",
    "created_on": "date",
    "entries": {
        "entries": {},
        "total": 0
    },
    "metadata": {
        "available_ids": [],
        "fields": {...},
        "next_id": 1,
        "schema": {}
    },
    "updated_at": "timestamp",
    "updated_on": "date",
    "uuid": "unique-identifier"
}
```

##### `ensure_defaults()`

```python
def ensure_defaults() -> None:
    """
    Ensures default data exists in the system.
    """
```

**Default Data Created**:
- Default difficulty levels (Easy, Medium, Hard)
- Default priority levels (Low, Medium, High)
- Default user settings
- Default stack if none exists

#### GUI Initialization

##### `initialize_gui()`

```python
def initialize_gui() -> None:
    """
    Initializes the GUI system and creates the main application window.
    """
```

**GUI Components Initialized**:
- Main application window
- Top, center, and bottom frames
- Dashboard view
- Navigation system
- Toast notification system

**Implementation Steps**:
1. Create main CustomTkinter window
2. Set up frame structure
3. Initialize dashboard view
4. Set up navigation handlers
5. Configure window properties

#### Event System Setup

##### `subscribe_to_events()`

```python
def subscribe_to_events() -> None:
    """
    Sets up event subscriptions for the application.
    """
```

**Event Subscriptions**:
- Navigation events (view switching)
- CRUD operations (create, update, delete)
- Rehearsal events (start, stop, complete)
- GUI events (button clicks, form submissions)

**Example Subscription**:
```python
def on_flashcard_created(event_data: dict[str, Any]) -> None:
    """Handle flashcard creation events."""
    flashcard = event_data.get('flashcard')
    if flashcard:
        # Update GUI, refresh views, etc.
        pass

subscribe(FLASHCARD_CREATED, on_flashcard_created)
```

##### `unsubscribe_from_events()`

```python
def unsubscribe_from_events() -> None:
    """
    Cleans up event subscriptions during application shutdown.
    """
```

### Default Data Management

#### Default Values

The bootstrap uses default values from `constants.defaults`:

```python
from studyfrog.constants.defaults import (
    DEFAULT_EASY_DIFFICULTY,
    DEFAULT_MEDIUM_DIFFICULTY,
    DEFAULT_HARD_DIFFICULTY,
    DEFAULT_LOW_PRIORITY,
    DEFAULT_MEDIUM_PRIORITY,
    DEFAULT_HIGH_PRIORITY,
    DEFAULT_USER,
)
```

#### Model Factory Integration

The bootstrap integrates with the model factory to create default instances:

```python
from studyfrog.models.factory import (
    get_answer_model,
    get_flashcard_model,
    get_note_model,
    get_question_model,
    get_rehearsal_run_model,
    get_stack_model,
)
```

### Error Handling

The bootstrap module includes comprehensive error handling:

```python
def ensure_directory(directory: Path) -> None:
    """Ensure a directory exists, creating it if necessary."""
    try:
        directory.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        log_error(f"Failed to create directory {directory}: {e}")

def ensure_file(file_path: Path, default_content: dict) -> None:
    """Ensure a file exists with default content."""
    try:
        if not file_path.exists():
            with open(file_path, 'w') as f:
                json.dump(default_content, f, indent=2)
    except Exception as e:
        log_error(f"Failed to create file {file_path}: {e}")
```

### Configuration Dependencies

The bootstrap module imports numerous constants and configurations:

```python
# Directory constants
from studyfrog.constants.directories import (
    DATA_DIR, LOGS_DIR, ASSETS_DIR, TEMP_DIR, ...
)

# File constants
from studyfrog.constants.files import (
    FLASHCARDS_DB_JSON, STACKS_DB_JSON, QUESTIONS_DB_JSON, ...
)

# Event constants
from studyfrog.constants.events import *

# Default values
from studyfrog.constants.defaults import (
    DEFAULT_EASY_DIFFICULTY, DEFAULT_USER, ...
)
```

### Usage Example

```python
# Manual bootstrap (normally called by application.py)
from studyfrog.core.bootstrap import (
    ensure_directories, ensure_files, ensure_defaults,
    initialize_gui, subscribe_to_events
)

# Initialize system
ensure_directories()
ensure_files()
ensure_defaults()
initialize_gui()
subscribe_to_events()
```

---

## core.common - Shared Core Utilities

### Purpose

The common module provides shared utilities and constants used throughout the core system.

### Key Components

#### Common Constants

```python
# Application identifiers
APPLICATION_NAME = "StudyFrog"
APPLICATION_VERSION = "1.0.0"

# Common file extensions
JSON_EXTENSION = ".json"
LOG_EXTENSION = ".log"

# Common delimiters
KEY_VALUE_DELIMITER = ":"
LIST_DELIMITER = ","
```

#### Utility Functions

##### String Utilities

```python
def pluralize_word(word: str, count: int) -> str:
    """
    Returns the plural form of a word based on count.
    
    Args:
        word: The word to pluralize
        count: The count to determine pluralization
        
    Returns:
        str: Pluralized word
    """
```

**Examples**:
```python
pluralize_word("flashcard", 1)  # "flashcard"
pluralize_word("flashcard", 5)  # "flashcards"
```

##### Validation Utilities

```python
def is_valid_identifier(identifier: str) -> bool:
    """
    Checks if a string is a valid identifier.
    
    Args:
        identifier: The identifier to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
```

##### Path Utilities

```python
def get_relative_path(path: Path, base: Path) -> Path:
    """
    Gets the relative path from a base path.
    
    Args:
        path: The target path
        base: The base path
        
    Returns:
        Path: Relative path
    """
```

### Error Handling

The common module provides standardized error handling:

```python
def handle_core_error(error: Exception, context: str) -> None:
    """
    Handles core-level errors with consistent logging.
    
    Args:
        error: The exception that occurred
        context: The context where the error occurred
    """
```

### Integration Points

The common module integrates with:

- `utils.logging` for error reporting
- `constants.common` for shared constants
- `utils.common` for additional utilities

### Usage Example

```python
from studyfrog.core.common import pluralize_word, is_valid_identifier

# Pluralization
count = 5
word = f"{count} {pluralize_word('item', count)}"  # "5 items"

# Validation
if is_valid_identifier(username):
    # Process valid username
    pass
```

## Core Module Interactions

### Module Dependencies

```
main.py
├── core.application
│   ├── core.bootstrap
│   │   ├── constants.* (all constant modules)
│   │   ├── models.factory
│   │   ├── gui.* (GUI components)
│   │   ├── utils.dispatcher
│   │   ├── utils.storage
│   │   └── utils.logging
│   ├── utils.dispatcher (for events)
│   ├── utils.logging
│   └── gui.gui (for root access)
└── utils.logging
```

### Execution Flow Summary

1. **main.py** calls `start_application()`
2. **core.application** runs pre-start tasks via **core.bootstrap**
3. **core.bootstrap** initializes:
   - Directory structure
   - Database files
   - Default data
   - GUI components
   - Event subscriptions
4. **core.application** starts GUI main loop
5. **main.py** handles cleanup on exit

### Error Propagation

```
GUI Layer → core.application → main.py → System Exit
     ↓              ↓              ↓
   Events        Logging        Exit Code
```

This core architecture provides a solid foundation for the StudyFrog application, ensuring proper initialization, error handling, and component coordination.
