# Constants and Configuration Documentation

## Overview

The constants and configuration modules provide centralized management of all configuration values, file paths, event definitions, and default settings used throughout StudyFrog.

## Table of Contents

1. [Constants Organization](#constants-organization)
2. [Common Constants](#common-constants)
3. [Default Values](#default-values)
4. [Directory Paths](#directory-paths)
5. [File Paths](#file-paths)
6. [Event Definitions](#event-definitions)
7. [Configuration Management](#configuration-management)

---

## Constants Organization

### Directory Structure

```
constants/
├── __init__.py           # Package exports
├── common.py            # Global constants and shared state
├── defaults.py          # Default configuration values
├── directories.py       # Directory path constants
├── events.py           # Event name definitions
├── files.py            # File path constants
├── gui.py              # GUI-specific constants
└── validation.py       # Validation rules and limits
```

### Import Pattern

```python
# Import specific constants
from studyfrog.constants.common import GLOBAL, APPLICATION_NAME
from studyfrog.constants.defaults import DEFAULT_MEDIUM_DIFFICULTY
from studyfrog.constants.events import FLASHCARD_CREATED
from studyfrog.constants.files import FLASHCARDS_DB_JSON

# Or import entire module
from studyfrog.constants import defaults, events, files
```

---

## Common Constants

### Purpose

The common module contains global constants, shared state, and application-wide settings.

### Application Information

```python
# Application metadata
APPLICATION_NAME = "StudyFrog"
APPLICATION_VERSION = "1.0.0"
APPLICATION_AUTHOR = "Louis Goodnews"
APPLICATION_DESCRIPTION = "A comprehensive flashcard study application"

# Application identifiers
APP_ID = "com.studyfrog.app"
APP_NAME = "studyfrog"
```

### Global State

```python
# Global state dictionary
GLOBAL = {
    'root': None,              # Main application window
    'dispatcher': None,         # Event dispatcher instance
    'current_user': None,      # Current logged-in user
    'app_config': {},          # Application configuration
    'theme': 'dark',          # Current theme
    'language': 'en',         # Current language
    'debug_mode': False,       # Debug mode flag
}
```

### System Limits

```python
# File size limits
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
MAX_IMAGE_SIZE = 5 * 1024 * 1024   # 5MB

# Data limits
MAX_FLASHCARDS_PER_STACK = 1000
MAX_STACKS_PER_USER = 100
MAX_ITEMS_PER_REHEARSAL = 500

# Text limits
MAX_TEXT_LENGTH = 10000
MAX_TITLE_LENGTH = 200
MAX_DESCRIPTION_LENGTH = 1000
```

### Performance Constants

```python
# Timing constants
AUTO_SAVE_INTERVAL = 300  # 5 minutes
TOAST_DISPLAY_TIME = 3000  # 3 seconds
ANIMATION_DURATION = 200  # milliseconds

# Pagination
DEFAULT_PAGE_SIZE = 25
MAX_PAGE_SIZE = 100

# Cache sizes
MAX_CACHED_ENTRIES = 1000
CACHE_EXPIRY_TIME = 3600  # 1 hour
```

### Usage Examples

```python
from studyfrog.constants.common import GLOBAL, APPLICATION_NAME, MAX_FILE_SIZE

# Access global state
root_window = GLOBAL['root']
current_theme = GLOBAL['theme']

# Use application constants
print(f"Welcome to {APPLICATION_NAME}")
if file_size > MAX_FILE_SIZE:
    print("File too large")
```

---

## Default Values

### Purpose

The defaults module provides default configuration values for all application settings.

### Difficulty Levels

```python
# Difficulty definitions
DEFAULT_EASY_DIFFICULTY = "Easy"
DEFAULT_MEDIUM_DIFFICULTY = "Medium"
DEFAULT_HARD_DIFFICULTY = "Hard"

# Difficulty configuration
DIFFICULTY_LEVELS = [
    {
        'name': 'Easy',
        'color': '#00ff00',
        'weight': 1,
        'description': 'Simple content'
    },
    {
        'name': 'Medium',
        'color': '#ffff00',
        'weight': 2,
        'description': 'Moderately difficult content'
    },
    {
        'name': 'Hard',
        'color': '#ff0000',
        'weight': 3,
        'description': 'Challenging content'
    }
]
```

### Priority Levels

```python
# Priority definitions
DEFAULT_LOWEST_PRIORITY = "Lowest"
DEFAULT_LOW_PRIORITY = "Low"
DEFAULT_MEDIUM_PRIORITY = "Medium"
DEFAULT_HIGH_PRIORITY = "High"
DEFAULT_HIGHEST_PRIORITY = "Highest"

# Priority configuration
PRIORITY_LEVELS = [
    {'name': 'Lowest', 'weight': 1, 'color': '#e0e0e0'},
    {'name': 'Low', 'weight': 2, 'color': '#b0b0b0'},
    {'name': 'Medium', 'weight': 3, 'color': '#808080'},
    {'name': 'High', 'weight': 4, 'color': '#404040'},
    {'name': 'Highest', 'weight': 5, 'color': '#000000'}
]
```

### Default User Settings

```python
# Default user configuration
DEFAULT_USER = {
    'name': 'Default User',
    'email': '',
    'preferences': {
        'theme': 'dark',
        'language': 'en',
        'auto_save': True,
        'show_tips': True,
        'sound_enabled': True,
        'animation_enabled': True
    }
}

# Default study settings
DEFAULT_STUDY_SETTINGS = {
    'items_per_session': 20,
    'session_time_limit': 1800,  # 30 minutes
    'show_progress': True,
    'randomize_order': True,
    'repeat_incorrect': True,
    'auto_advance': False
}
```

### Default GUI Settings

```python
# Window defaults
DEFAULT_WINDOW_WIDTH = 1200
DEFAULT_WINDOW_HEIGHT = 800
DEFAULT_MIN_WIDTH = 800
DEFAULT_MIN_HEIGHT = 600

# GUI defaults
DEFAULT_FONT_SIZE = 12
DEFAULT_FONT_FAMILY = "Arial"
DEFAULT_BUTTON_HEIGHT = 40
DEFAULT_PADDING = 10

# Color scheme (dark theme)
DEFAULT_COLORS = {
    'background': '#2b2b2b',
    'surface': '#3c3c3c',
    'primary': '#1e90ff',
    'secondary': '#4169e1',
    'text': '#ffffff',
    'text_secondary': '#cccccc',
    'border': '#555555',
    'success': '#00ff00',
    'warning': '#ffff00',
    'error': '#ff0000'
}
```

### Default Content

```python
# Default stack if none exists
DEFAULT_STACK = {
    'name': 'My First Stack',
    'description': 'A stack for your first flashcards',
    'subject': 'General',
    'teacher': ''
}

# Default flashcard template
DEFAULT_FLASHCARD = {
    'front': 'What is...',
    'back': 'The answer is...',
    'difficulty': DEFAULT_MEDIUM_DIFFICULTY,
    'priority': DEFAULT_MEDIUM_PRIORITY,
    'subject': '',
    'teacher': '',
    'tags': []
}
```

### Usage Examples

```python
from studyfrog.constants.defaults import (
    DEFAULT_MEDIUM_DIFFICULTY,
    DEFAULT_STUDY_SETTINGS,
    DIFFICULTY_LEVELS
)

# Use default difficulty
flashcard.difficulty = DEFAULT_MEDIUM_DIFFICULTY

# Get default study settings
settings = DEFAULT_STUDY_SETTINGS.copy()
settings['items_per_session'] = 10

# Get difficulty configuration
for diff_config in DIFFICULTY_LEVELS:
    if diff_config['name'] == 'Easy':
        color = diff_config['color']
        break
```

---

## Directory Paths

### Purpose

The directories module defines all directory paths used by the application.

### Base Directories

```python
# Application directory structure
BASE_DIR = Path.cwd()
LOCAL_DIR = BASE_DIR / ".local"
DATA_DIR = LOCAL_DIR / "data"
LOGS_DIR = LOCAL_DIR / "logs"
TEMP_DIR = LOCAL_DIR / "temp"
ASSETS_DIR = LOCAL_DIR / "assets"
EXPORTS_DIR = LOCAL_DIR / "exports"
IMPORTS_DIR = LOCAL_DIR / "imports"
IMAGES_DIR = ASSETS_DIR / "images"
RESOURCES_DIR = ASSETS_DIR / "resources"
CONFIG_DIR = LOCAL_DIR / "config"
```

### User-Specific Directories

```python
# User directories (if multi-user support is added)
USERS_DIR = LOCAL_DIR / "users"
USER_DATA_DIR = USERS_DIR / "{user_id}" / "data"
USER_LOGS_DIR = USERS_DIR / "{user_id}" / "logs"
USER_CONFIG_DIR = USERS_DIR / "{user_id}" / "config"
```

### Backup Directories

```python
# Backup directories
BACKUP_DIR = LOCAL_DIR / "backups"
DAILY_BACKUP_DIR = BACKUP_DIR / "daily"
WEEKLY_BACKUP_DIR = BACKUP_DIR / "weekly"
MONTHLY_BACKUP_DIR = BACKUP_DIR / "monthly"
```

### Directory Creation

```python
def ensure_all_directories() -> None:
    """Ensure all required directories exist."""
    directories = [
        LOCAL_DIR, DATA_DIR, LOGS_DIR, TEMP_DIR,
        ASSETS_DIR, EXPORTS_DIR, IMPORTS_DIR,
        IMAGES_DIR, RESOURCES_DIR, CONFIG_DIR,
        BACKUP_DIR, DAILY_BACKUP_DIR, WEEKLY_BACKUP_DIR, MONTHLY_BACKUP_DIR
    ]
    
    for directory in directories:
        ensure_directory(directory)
```

### Usage Examples

```python
from studyfrog.constants.directories import DATA_DIR, LOGS_DIR, BACKUP_DIR

# Construct file paths
flashcards_file = DATA_DIR / "flashcards.json"
log_file = LOGS_DIR / "app.log"
backup_file = BACKUP_DIR / "backup_20260406.json"

# Ensure directories exist
ensure_directory(DATA_DIR)
ensure_directory(LOGS_DIR)
```

---

## File Paths

### Purpose

The files module defines all file paths used by the application.

### Database Files

```python
# Core data files
FLASHCARDS_DB_JSON = DATA_DIR / "flashcards.json"
STACKS_DB_JSON = DATA_DIR / "stacks.json"
QUESTIONS_DB_JSON = DATA_DIR / "questions.json"
ANSWERS_DB_JSON = DATA_DIR / "answers.json"
NOTES_DB_JSON = DATA_DIR / "notes.json"

# Rehearsal files
REHEARSAL_RUN_DB_JSON = DATA_DIR / "rehearsal_runs.json"
REHEARSAL_RUN_ITEM_DB_JSON = DATA_DIR / "rehearsal_run_items.json"

# Metadata files
DIFFICULTIES_DB_JSON = DATA_DIR / "difficulties.json"
PRIORITIES_DB_JSON = DATA_DIR / "priorities.json"
SUBJECTS_DB_JSON = DATA_DIR / "subjects.json"
TAGS_DB_JSON = DATA_DIR / "tags.json"
TEACHERS_DB_JSON = DATA_DIR / "teachers.json"
USERS_DB_JSON = DATA_DIR / "users.json"

# Configuration files
CONFIG_DB_JSON = DATA_DIR / "config.json"
CUSTOMFIELDS_DB_JSON = DATA_DIR / "customfields.json"
ASSOCIATIONS_DB_JSON = DATA_DIR / "associations.json"
IMAGES_DB_JSON = DATA_DIR / "images.json"
```

### Log Files

```python
# Application logs
APP_LOG_FILE = LOGS_DIR / "app.log"
ERROR_LOG_FILE = LOGS_DIR / "error.log"
DEBUG_LOG_FILE = LOGS_DIR / "debug.log"
PERFORMANCE_LOG_FILE = LOGS_DIR / "performance.log"

# GUI logs
GUI_LOG_FILE = LOGS_DIR / "gui.log"
USER_ACTION_LOG_FILE = LOGS_DIR / "user_actions.log"
```

### Configuration Files

```python
# Application configuration
MAIN_CONFIG_FILE = CONFIG_DIR / "config.json"
GUI_CONFIG_FILE = CONFIG_DIR / "gui.json"
STUDY_CONFIG_FILE = CONFIG_DIR / "study.json"
USER_CONFIG_FILE = CONFIG_DIR / "user.json"

# Theme files
THEME_CONFIG_FILE = CONFIG_DIR / "theme.json"
COLOR_SCHEME_FILE = CONFIG_DIR / "colors.json"
```

### Temporary Files

```python
# Temporary files
TEMP_EXPORT_FILE = TEMP_DIR / "temp_export.json"
TEMP_IMPORT_FILE = TEMP_DIR / "temp_import.json"
TEMP_BACKUP_FILE = TEMP_DIR / "temp_backup.json"
LOCK_FILE = TEMP_DIR / "app.lock"
```

### Asset Files

```python
# Image assets
APP_ICON_FILE = IMAGES_DIR / "icon.png"
LOGO_FILE = IMAGES_DIR / "logo.png"
DEFAULT_AVATAR_FILE = IMAGES_DIR / "default_avatar.png"

# Resource files
HELP_FILE = RESOURCES_DIR / "help.html"
LICENSE_FILE = RESOURCES_DIR / "license.txt"
CHANGELOG_FILE = RESOURCES_DIR / "changelog.txt"
```

### File Validation

```python
# Allowed file extensions
ALLOWED_IMAGE_EXTENSIONS = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
ALLOWED_IMPORT_EXTENSIONS = ['.json', '.csv', '.txt']
ALLOWED_EXPORT_EXTENSIONS = ['.json', '.csv', '.pdf']

# File size limits
MAX_IMAGE_FILE_SIZE = 5 * 1024 * 1024  # 5MB
MAX_IMPORT_FILE_SIZE = 50 * 1024 * 1024  # 50MB
```

### Usage Examples

```python
from studyfrog.constants.files import (
    FLASHCARDS_DB_JSON,
    APP_LOG_FILE,
    MAIN_CONFIG_FILE
)

# Use file paths
flashcards_data = load_json(FLASHCARDS_DB_JSON)
log_to_file(APP_LOG_FILE, "Application started")
config = load_config(MAIN_CONFIG_FILE)
```

---

## Event Definitions

### Purpose

The events module defines all event names used throughout the application for the event-driven architecture.

### Application Lifecycle Events

```python
# Application events
APPLICATION_STARTING = "APPLICATION_STARTING"
APPLICATION_STARTED = "APPLICATION_STARTED"
APPLICATION_STOPPING = "APPLICATION_STOPPING"
APPLICATION_STOPPED = "APPLICATION_STOPPED"

# Configuration events
CONFIG_LOADED = "CONFIG_LOADED"
CONFIG_CHANGED = "CONFIG_CHANGED"
CONFIG_SAVED = "CONFIG_SAVED"
```

### Navigation Events

```python
# View navigation
GET_DASHBOARD_VIEW = "GET_DASHBOARD_VIEW"
GET_CREATE_VIEW = "GET_CREATE_VIEW"
GET_EDIT_VIEW = "GET_EDIT_VIEW"
GET_DELETE_CONFIRMATION_VIEW = "GET_DELETE_CONFIRMATION_VIEW"

# Rehearsal navigation
GET_REHEARSAL_RUN_SETUP_VIEW = "GET_REHEARSAL_RUN_SETUP_VIEW"
GET_REHEARSAL_RUN_VIEW = "GET_REHEARSAL_RUN_VIEW"
GET_REHEARSAL_RUN_RESULT_VIEW = "GET_REHEARSAL_RUN_RESULT_VIEW"

# Modal events
SHOW_CONFIRMATION_DIALOG = "SHOW_CONFIRMATION_DIALOG"
SHOW_ERROR_DIALOG = "SHOW_ERROR_DIALOG"
SHOW_INFO_DIALOG = "SHOW_INFO_DIALOG"
HIDE_ALL_DIALOGS = "HIDE_ALL_DIALOGS"
```

### CRUD Events

```python
# Flashcard events
FLASHCARD_CREATED = "FLASHCARD_CREATED"
FLASHCARD_UPDATED = "FLASHCARD_UPDATED"
FLASHCARD_DELETED = "FLASHCARD_DELETED"
FLASHCARDS_BATCH_CREATED = "FLASHCARDS_BATCH_CREATED"
FLASHCARDS_BATCH_UPDATED = "FLASHCARDS_BATCH_UPDATED"
FLASHCARDS_BATCH_DELETED = "FLASHCARDS_BATCH_DELETED"

# Stack events
STACK_CREATED = "STACK_CREATED"
STACK_UPDATED = "STACK_UPDATED"
STACK_DELETED = "STACK_DELETED"
STACK_ITEM_ADDED = "STACK_ITEM_ADDED"
STACK_ITEM_REMOVED = "STACK_ITEM_REMOVED"

# Question events
QUESTION_CREATED = "QUESTION_CREATED"
QUESTION_UPDATED = "QUESTION_UPDATED"
QUESTION_DELETED = "QUESTION_DELETED"

# Answer events
ANSWER_CREATED = "ANSWER_CREATED"
ANSWER_UPDATED = "ANSWER_UPDATED"
ANSWER_DELETED = "ANSWER_DELETED"

# Note events
NOTE_CREATED = "NOTE_CREATED"
NOTE_UPDATED = "NOTE_UPDATED"
NOTE_DELETED = "NOTE_DELETED"
```

### Rehearsal Events

```python
# Session management
REHEARSAL_RUN_STARTED = "REHEARSAL_RUN_STARTED"
REHEARSAL_RUN_PAUSED = "REHEARSAL_RUN_PAUSED"
REHEARSAL_RUN_RESUMED = "REHEARSAL_RUN_RESUMED"
REHEARSAL_RUN_COMPLETED = "REHEARSAL_RUN_COMPLETED"
REHEARSAL_RUN_CANCELLED = "REHEARSAL_RUN_CANCELLED"

# Item presentation
REHEARSAL_RUN_ITEM_PRESENTED = "REHEARSAL_RUN_ITEM_PRESENTED"
REHEARSAL_RUN_ITEM_ANSWERED = "REHEARSAL_RUN_ITEM_ANSWERED"
REHEARSAL_RUN_ITEM_SKIPPED = "REHEARSAL_RUN_ITEM_SKIPPED"
REHEARSAL_RUN_ITEM_FLAGGED = "REHEARSAL_RUN_ITEM_FLAGGED"

# Progress events
REHEARSAL_RUN_PROGRESS_UPDATED = "REHEARSAL_RUN_PROGRESS_UPDATED"
REHEARSAL_RUN_TIME_UPDATED = "REHEARSAL_RUN_TIME_UPDATED"
REHEARSAL_RUN_SCORE_UPDATED = "REHEARSAL_RUN_SCORE_UPDATED"
```

### GUI Events

```python
# Window events
WINDOW_RESIZED = "WINDOW_RESIZED"
WINDOW_MOVED = "WINDOW_MOVED"
WINDOW_MINIMIZED = "WINDOW_MINIMIZED"
WINDOW_RESTORED = "WINDOW_RESTORED"

# Theme events
THEME_CHANGED = "THEME_CHANGED"
COLOR_SCHEME_CHANGED = "COLOR_SCHEME_CHANGED"
FONT_SIZE_CHANGED = "FONT_SIZE_CHANGED"

# Interaction events
BUTTON_CLICKED = "BUTTON_CLICKED"
MENU_ITEM_SELECTED = "MENU_ITEM_SELECTED"
TOOLBAR_ACTION = "TOOLBAR_ACTION"
CONTEXT_MENU_REQUESTED = "CONTEXT_MENU_REQUESTED"
```

### Data Events

```python
# Import/Export events
IMPORT_STARTED = "IMPORT_STARTED"
IMPORT_COMPLETED = "IMPORT_COMPLETED"
IMPORT_FAILED = "IMPORT_FAILED"
EXPORT_STARTED = "EXPORT_STARTED"
EXPORT_COMPLETED = "EXPORT_COMPLETED"
EXPORT_FAILED = "EXPORT_FAILED"

# Backup events
BACKUP_STARTED = "BACKUP_STARTED"
BACKUP_COMPLETED = "BACKUP_COMPLETED"
BACKUP_FAILED = "BACKUP_FAILED"
RESTORE_STARTED = "RESTORE_STARTED"
RESTORE_COMPLETED = "RESTORE_COMPLETED"
RESTORE_FAILED = "RESTORE_FAILED"

# Sync events
SYNC_STARTED = "SYNC_STARTED"
SYNC_COMPLETED = "SYNC_COMPLETED"
SYNC_FAILED = "SYNC_FAILED"
SYNC_CONFLICT = "SYNC_CONFLICT"
```

### Event Categories

```python
# Event categories for organization
EVENT_CATEGORIES = {
    'application': [
        APPLICATION_STARTING, APPLICATION_STARTED, APPLICATION_STOPPING, APPLICATION_STOPPED
    ],
    'navigation': [
        GET_DASHBOARD_VIEW, GET_CREATE_VIEW, GET_EDIT_VIEW, GET_DELETE_CONFIRMATION_VIEW
    ],
    'crud': [
        FLASHCARD_CREATED, FLASHCARD_UPDATED, FLASHCARD_DELETED,
        STACK_CREATED, STACK_UPDATED, STACK_DELETED
    ],
    'rehearsal': [
        REHEARSAL_RUN_STARTED, REHEARSAL_RUN_COMPLETED,
        REHEARSAL_RUN_ITEM_PRESENTED, REHEARSAL_RUN_ITEM_ANSWERED
    ],
    'gui': [
        WINDOW_RESIZED, THEME_CHANGED, BUTTON_CLICKED
    ],
    'data': [
        IMPORT_STARTED, IMPORT_COMPLETED, EXPORT_STARTED, EXPORT_COMPLETED
    ]
}
```

### Usage Examples

```python
from studyfrog.constants.events import (
    FLASHCARD_CREATED,
    GET_DASHBOARD_VIEW,
    REHEARSAL_RUN_STARTED
)

# Subscribe to events
subscribe(FLASHCARD_CREATED, handle_flashcard_created)
subscribe(GET_DASHBOARD_VIEW, handle_navigation)

# Dispatch events
dispatch(FLASHCARD_CREATED, {'flashcard': flashcard})
dispatch(GET_DASHBOARD_VIEW, {'source': 'menu'})
```

---

## Configuration Management

### Purpose

Configuration management provides centralized handling of application settings, user preferences, and runtime configuration.

### Configuration Structure

```python
# Main configuration structure
DEFAULT_CONFIG = {
    'application': {
        'name': APPLICATION_NAME,
        'version': APPLICATION_VERSION,
        'debug_mode': False,
        'auto_save': True,
        'backup_enabled': True
    },
    'gui': {
        'theme': 'dark',
        'language': 'en',
        'window_width': DEFAULT_WINDOW_WIDTH,
        'window_height': DEFAULT_WINDOW_HEIGHT,
        'font_size': DEFAULT_FONT_SIZE,
        'animations_enabled': True
    },
    'study': {
        'default_difficulty': DEFAULT_MEDIUM_DIFFICULTY,
        'default_priority': DEFAULT_MEDIUM_PRIORITY,
        'items_per_session': 20,
        'session_time_limit': 1800,
        'randomize_order': True,
        'show_progress': True
    },
    'storage': {
        'data_directory': str(DATA_DIR),
        'backup_directory': str(BACKUP_DIR),
        'auto_backup': True,
        'backup_interval': 86400,  # 24 hours
        'max_backups': 30
    },
    'performance': {
        'cache_enabled': True,
        'cache_size': MAX_CACHED_ENTRIES,
        'cache_expiry': CACHE_EXPIRY_TIME,
        'lazy_loading': True
    }
}
```

### Configuration Loading

```python
def load_config() -> dict:
    """
    Load configuration from file with fallback to defaults.
    
    Returns:
        dict: Loaded configuration
    """
    config = DEFAULT_CONFIG.copy()
    
    if MAIN_CONFIG_FILE.exists():
        try:
            file_config = safe_read_json(MAIN_CONFIG_FILE)
            config = deep_merge_dict(config, file_config)
        except Exception as e:
            log_error(f"Failed to load config: {e}")
    
    return config

def save_config(config: dict) -> bool:
    """
    Save configuration to file.
    
    Args:
        config: Configuration to save
        
    Returns:
        bool: True if successful
    """
    return safe_write_json(MAIN_CONFIG_FILE, config)
```

### Configuration Validation

```python
def validate_config(config: dict) -> tuple[bool, list[str]]:
    """
    Validate configuration structure and values.
    
    Args:
        config: Configuration to validate
        
    Returns:
        tuple: (is_valid, error_messages)
    """
    errors = []
    
    # Validate required sections
    required_sections = ['application', 'gui', 'study', 'storage']
    for section in required_sections:
        if section not in config:
            errors.append(f"Missing required section: {section}")
    
    # Validate specific values
    if 'gui' in config:
        gui_config = config['gui']
        if 'window_width' in gui_config:
            width = gui_config['window_width']
            if width < DEFAULT_MIN_WIDTH:
                errors.append(f"Window width too small: {width}")
    
    return len(errors) == 0, errors
```

### Runtime Configuration

```python
def get_config_value(key_path: str, default=None):
    """
    Get configuration value using dot notation.
    
    Args:
        key_path: Dot-separated path (e.g., 'gui.theme')
        default: Default value if not found
        
    Returns:
        Configuration value or default
    """
    keys = key_path.split('.')
    value = GLOBAL.get('app_config', {})
    
    for key in keys:
        if isinstance(value, dict) and key in value:
            value = value[key]
        else:
            return default
    
    return value

def set_config_value(key_path: str, value) -> None:
    """
    Set configuration value using dot notation.
    
    Args:
        key_path: Dot-separated path (e.g., 'gui.theme')
        value: Value to set
    """
    keys = key_path.split('.')
    config = GLOBAL.setdefault('app_config', {})
    
    for key in keys[:-1]:
        config = config.setdefault(key, {})
    
    config[keys[-1]] = value
    dispatch(CONFIG_CHANGED, {'key_path': key_path, 'value': value})
```

### Usage Examples

```python
from studyfrog.constants.common import GLOBAL
from studyfrog.constants.defaults import DEFAULT_CONFIG

# Load configuration
config = load_config()
GLOBAL['app_config'] = config

# Get configuration values
theme = get_config_value('gui.theme', 'dark')
window_width = get_config_value('gui.window_width', 1200)

# Set configuration values
set_config_value('gui.theme', 'light')
set_config_value('study.items_per_session', 25)

# Save configuration
save_config(GLOBAL['app_config'])
```

---

## Constants and Configuration Best Practices

### 1. Use Constants for Magic Values

```python
# Good - use constants
if file_size > MAX_FILE_SIZE:
    handle_large_file()

# Avoid - magic numbers
if file_size > 10485760:  # What is this number?
    handle_large_file()
```

### 2. Group Related Constants

```python
# Good - group related constants
GUI_CONSTANTS = {
    'DEFAULT_WIDTH': 1200,
    'DEFAULT_HEIGHT': 800,
    'MIN_WIDTH': 800,
    'MIN_HEIGHT': 600
}

# Avoid - scattered constants
DEFAULT_WIDTH = 1200
DEFAULT_HEIGHT = 800
MIN_WIDTH = 800
MIN_HEIGHT = 600
```

### 3. Use Descriptive Names

```python
# Good - descriptive names
AUTO_SAVE_INTERVAL_SECONDS = 300
MAX_FLASHCARDS_PER_STACK = 1000

# Avoid - unclear names
INTERVAL = 300
MAX_ITEMS = 1000
```

### 4. Document Constants

```python
# Good - documented constants
# Maximum file size for uploads (10MB)
MAX_UPLOAD_SIZE = 10 * 1024 * 1024

# Time in seconds between auto-saves (5 minutes)
AUTO_SAVE_INTERVAL = 300

# Avoid - undocumented constants
MAX_UPLOAD_SIZE = 10485760  # What is this for?
AUTO_SAVE_INTERVAL = 300
```

### 5. Use Configuration Management

```python
# Good - use configuration system
theme = get_config_value('gui.theme', 'dark')
set_config_value('gui.theme', 'light')

# Avoid - direct global access
GLOBAL['theme'] = 'light'  # No persistence, no validation
```

The constants and configuration system provides a solid foundation for maintaining consistent, configurable, and maintainable application behavior.
