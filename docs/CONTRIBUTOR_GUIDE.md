# StudyFrog Contributor Guide

Welcome to the StudyFrog contributor guide! This document provides comprehensive documentation for developers who want to contribute to the StudyFrog flashcard application.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Architecture](#architecture)
3. [Getting Started](#getting-started)
4. [Code Structure](#code-structure)
5. [Module Documentation](#module-documentation)
6. [Development Workflow](#development-workflow)
7. [Testing](#testing)
8. [Coding Standards](#coding-standards)

## Project Overview

StudyFrog is a Python-based flashcard application built with CustomTkinter for the GUI. It provides a comprehensive study system with:

- **Flashcard Management**: Create, edit, and organize flashcards
- **Stack Organization**: Group flashcards into thematic stacks
- **Rehearsal System**: Practice sessions with different question types
- **Data Persistence**: JSON-based storage for all study materials
- **Event-Driven Architecture**: Modular design using event dispatching

## Architecture

### Application Flow

The application follows this execution flow:

```
main.py → core.application → core.bootstrap → GUI → Event System
```

1. **Entry Point**: `main.py` initializes the application
2. **Core Layer**: Handles application lifecycle and bootstrap
3. **Bootstrap**: Sets up directories, files, and default data
4. **GUI Layer**: CustomTkinter-based user interface
5. **Event System**: Decoupled communication between components

### Key Components

- **Models**: Data structures for flashcards, stacks, questions, etc.
- **Views**: GUI components for different user interactions
- **Logic**: Business logic for user operations
- **Utils**: Helper functions for storage, logging, etc.
- **Constants**: Configuration values and event definitions

## Getting Started

### Prerequisites

- Python 3.11+
- pip (Python package manager)
- Git

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd StudyFrog
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python -m studyfrog.main
   ```

### Development Setup

For development with additional tools:

```bash
pip install -r requirements-dev.txt  # If available
pre-commit install  # Set up pre-commit hooks
```

## Code Structure

```
src/studyfrog/
├── main.py              # Application entry point
├── core/                # Core application logic
│   ├── application.py    # Application lifecycle management
│   ├── bootstrap.py     # System initialization
│   ├── common.py        # Shared core utilities
│   └── core.py         # Core exports
├── models/              # Data models and factories
│   ├── factory.py       # Model creation utilities
│   ├── models.py        # Base and specific model classes
│   └── observables.py   # Observable data structures
├── gui/                 # User interface components
│   ├── views/           # Main view components
│   ├── forms/           # Data entry forms
│   ├── logic/           # GUI business logic
│   ├── widgets.py        # Custom GUI widgets
│   └── gui.py          # Main GUI management
├── utils/               # Utility modules
│   ├── storage.py       # Data persistence
│   ├── dispatcher.py    # Event system
│   ├── logging.py       # Logging utilities
│   └── ...
├── constants/           # Configuration constants
│   ├── events.py        # Event definitions
│   ├── defaults.py      # Default values
│   └── ...
└── common/             # Shared utilities
```

## Module Documentation

### Core Modules

#### `main.py`
**Purpose**: Application entry point and lifecycle management.

**Key Functions**:
- `main()`: Primary entry point that starts and stops the application

**Usage**:
```python
if __name__ == "__main__":
    raise SystemExit(main())
```

#### `core.application`
**Purpose**: Manages application startup, shutdown, and runtime.

**Key Functions**:
- `start_application()`: Initializes and starts the application
- `stop_application()`: Cleanly shuts down the application
- `run_pre_start_tasks()`: Tasks to run before GUI initialization
- `run_post_start_tasks()`: Tasks to run after GUI initialization

**Events**:
- `APPLICATION_STARTING`: Fired before application starts
- `APPLICATION_STARTED`: Fired after application starts
- `APPLICATION_STOPPING`: Fired before application stops
- `APPLICATION_STOPPED`: Fired after application stops

#### `core.bootstrap`
**Purpose**: System initialization including directories, files, and default data.

**Key Functions**:
- `ensure_directories()`: Creates required directory structure
- `ensure_files()`: Creates required database files
- `ensure_defaults()`: Sets up default data if needed
- `initialize_gui()`: Sets up the GUI components
- `subscribe_to_events()`: Sets up event subscriptions

### Data Models

#### `models.models`
**Purpose**: Defines all data structures used in the application.

**Key Classes**:
- `Model`: Base class for all data models
- `FlashcardModel`: Flashcard data structure
- `StackModel`: Stack/organization data structure
- `QuestionModel`, `AnswerModel`: Q&A data structures
- `RehearsalRunModel`: Rehearsal session data

**Common Fields**:
- `id`: Unique identifier
- `key`: String key for references
- `uuid`: UUID for unique identification
- `created_at`, `updated_at`: Timestamps
- `metadata`: Additional model information

#### `models.factory`
**Purpose**: Factory functions for creating model instances.

**Key Functions**:
- `get_flashcard_model()`: Creates flashcard instances
- `get_stack_model()`: Creates stack instances
- `get_model()`: Generic model creation from type

### GUI Components

#### `gui.views`
**Purpose**: Main view components for different user interactions.

**Key Views**:
- `dashboard_view`: Main dashboard and navigation
- `create_view`: Form for creating new items
- `edit_view`: Form for editing existing items
- `rehearsal_run_view`: Main rehearsal interface
- `rehearsal_run_setup_view`: Configure rehearsal sessions

#### `gui.forms`
**Purpose**: Data entry forms for creating and editing content.

**Key Forms**:
- `flashcard_create_form`: Create new flashcards
- `stack_create_form`: Create new stacks
- `question_create_form`: Create questions
- `answer_create_form`: Create answers

#### `gui.logic`
**Purpose**: Business logic for GUI operations.

**Key Modules**:
- `rehearsal_run_view_logic`: Rehearsal session management
- `create_view_logic`: Content creation logic
- `edit_view_logic`: Content editing logic

### Utility Modules

#### `utils.storage`
**Purpose**: Data persistence and JSON file management.

**Key Functions**:
- `get_all_entries()`: Retrieve all entries from a store
- `get_entry()`: Retrieve specific entry
- `add_entry()`: Add new entry
- `update_entry()`: Update existing entry
- `delete_entry()`: Remove entry

#### `utils.dispatcher`
**Purpose**: Event-driven communication system.

**Key Functions**:
- `dispatch()`: Send events to subscribers
- `subscribe()`: Listen for specific events
- `unsubscribe()`: Stop listening for events

#### `utils.logging`
**Purpose**: Application logging system.

**Key Functions**:
- `log_info()`: Information messages
- `log_warning()`: Warning messages
- `log_error()`: Error messages
- `log_trace()`: Debug messages

### Constants

#### `constants.events`
**Purpose**: All event definitions used throughout the application.

**Event Categories**:
- Application lifecycle events
- Navigation events
- CRUD operation events
- GUI interaction events

#### `constants.defaults`
**Purpose**: Default configuration values.

**Includes**:
- Default difficulty levels
- Default priority levels
- Default user settings

## Development Workflow

### 1. Creating New Features

1. **Plan the Feature**:
   - Define the user story
   - Identify affected modules
   - Plan the data model changes (if any)

2. **Implement the Backend**:
   - Add/update models in `models/`
   - Implement storage operations in `utils/storage.py`
   - Add event definitions in `constants/events.py`

3. **Implement the GUI**:
   - Create views in `gui/views/`
   - Create forms in `gui/forms/`
   - Implement logic in `gui/logic/`

4. **Wire Everything Together**:
   - Add event subscriptions in `core/bootstrap.py`
   - Update navigation if needed

### 2. Adding New Models

1. **Define the Model**:
   ```python
   class NewModel(Model):
       def __init__(self, **kwargs):
           super().__init__(**kwargs)
           self.field1 = kwargs.get('field1')
           self.field2 = kwargs.get('field2')
   ```

2. **Add Factory Function**:
   ```python
   def get_new_model(**kwargs) -> Optional[NewModel]:
       return get_model(type_='new_model', **kwargs)
   ```

3. **Update Storage**:
   - Add database file constant in `constants/files.py`
   - Add file creation in `core/bootstrap.py`

### 3. Adding New Views

1. **Create View Module**:
   ```python
   # gui/views/new_view.py
   def get_new_view() -> ctk.CTkFrame:
       # View implementation
       pass
   ```

2. **Add Navigation**:
   - Add navigation event in `constants/events.py`
   - Add event handler in `core/bootstrap.py`

3. **Update Main GUI**:
   - Import the view in `core/bootstrap.py`
   - Add to navigation system

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_models.py

# Run with coverage
pytest --cov=studyfrog
```

### Test Structure

```
tests/
├── test_imports.py        # Import validation
├── test_models.py         # Model tests
├── test_storage.py        # Storage tests
├── test_dispatcher.py     # Event system tests
└── conftest.py          # Test configuration
```

### Writing Tests

1. **Model Tests**:
   ```python
   def test_flashcard_creation():
       flashcard = get_flashcard_model(front="Question", back="Answer")
       assert flashcard.front == "Question"
       assert flashcard.back == "Answer"
   ```

2. **Storage Tests**:
   ```python
   def test_add_flashcard():
       flashcard = get_flashcard_model(front="Q", back="A")
       add_entry(FLASHCARDS_DB_JSON, flashcard)
       retrieved = get_entry(FLASHCARDS_DB_JSON, flashcard.key)
       assert retrieved is not None
   ```

## Coding Standards

### Code Style

- **Python Version**: 3.11+
- **Line Length**: 100 characters
- **Imports**: Group imports (stdlib, third-party, local)
- **Docstrings**: Google-style docstrings
- **Type Hints**: Use type hints where possible

### Naming Conventions

- **Files**: `snake_case.py`
- **Classes**: `PascalCase`
- **Functions/Variables**: `snake_case`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private**: `_leading_underscore`

### Documentation

- **Module Docstrings**: Explain purpose and usage
- **Function Docstrings**: Args, returns, and examples
- **Class Docstrings**: Purpose and key methods
- **Inline Comments**: Complex logic only

### Error Handling

- **Use Specific Exceptions**: Avoid bare `except:`
- **Log Errors**: Use the logging system
- **Graceful Degradation**: Handle errors gracefully
- **User Feedback**: Show user-friendly error messages

## Contributing Guidelines

### Before Contributing

1. **Read the Code**: Understand the existing architecture
2. **Check Issues**: Look for related issues or feature requests
3. **Create Issue**: For new features, create an issue first

### Submitting Changes

1. **Fork the Repository**
2. **Create Feature Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make Changes**: Follow the coding standards
4. **Add Tests**: Ensure test coverage
5. **Run Tests**: Make sure all tests pass
6. **Update Documentation**: Update relevant docs
7. **Submit Pull Request**: With clear description

### Pull Request Guidelines

- **Clear Title**: Describe the change
- **Detailed Description**: Explain what and why
- **Test Coverage**: Include tests for new features
- **Documentation**: Update relevant documentation
- **No Breaking Changes**: Maintain backward compatibility

## Common Patterns

### Event-Driven Updates

```python
# In bootstrap.py
subscribe_to_events()

# In event handler
def on_flashcard_created(event_data):
    # Handle flashcard creation
    pass

subscribe(FLASHCARD_CREATED, on_flashcard_created)
```

### Model Creation

```python
# Using factory
flashcard = get_flashcard_model(
    front="What is 2+2?",
    back="4",
    difficulty="Easy"
)

# Manual creation
flashcard = FlashcardModel(
    front="What is 2+2?",
    back="4",
    difficulty="Easy"
)
```

### Storage Operations

```python
# Add entry
add_entry(FLASHCARDS_DB_JSON, flashcard)

# Get entry
flashcard = get_entry(FLASHCARDS_DB_JSON, "FLASHCARD_1")

# Update entry
flashcard.front = "Updated question"
update_entry(FLASHCARDS_DB_JSON, flashcard)

# Delete entry
delete_entry(FLASHCARDS_DB_JSON, "FLASHCARD_1")
```

## Troubleshooting

### Common Issues

1. **Import Errors**: Check PYTHONPATH includes `src/`
2. **GUI Not Showing**: Ensure CustomTkinter is installed
3. **Data Not Saving**: Check file permissions in `.local/data/`
4. **Events Not Working**: Check event subscriptions in bootstrap

### Debug Mode

Enable debug logging:

```python
from studyfrog.utils.logging import set_debug_mode
set_debug_mode(True)
```

### Getting Help

- **Check Issues**: Look for similar problems
- **Create Issue**: Provide detailed error information
- **Join Discussion**: Ask questions in discussions
- **Review Code**: Look at similar implementations

Thank you for contributing to StudyFrog! Your contributions help make this project better for everyone.
