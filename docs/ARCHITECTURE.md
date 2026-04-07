# StudyFrog Architecture Documentation

## Overview

StudyFrog is built with a layered, event-driven architecture that separates concerns and promotes modularity. The application follows a clear execution flow from entry point through initialization to user interaction.

## Architecture Diagram

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   main.py       │───▶│ core.application │───▶│ core.bootstrap  │
│  (Entry Point)  │    │  (Lifecycle)    │    │ (Init System)  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Event System  │◀───│      GUI        │───▶│   User Interface │
│  (Dispatcher)   │    │  (CustomTkinter)│    │   (Views/Forms) │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                                           │
         ▼                                           ▼
┌─────────────────┐                           ┌─────────────────┐
│   Models       │                           │   Storage       │
│  (Data Layer)  │                           │ (JSON Files)    │
└─────────────────┘                           └─────────────────┘
```

## Core Principles

### 1. Separation of Concerns

- **Core Layer**: Application lifecycle and bootstrap
- **GUI Layer**: User interface and interaction
- **Model Layer**: Data structures and business logic
- **Storage Layer**: Data persistence
- **Event System**: Decoupled communication

### 2. Event-Driven Architecture

The application uses an event-driven pattern where components communicate through events rather than direct method calls. This provides:

- **Loose Coupling**: Components don't depend on each other directly
- **Flexibility**: Easy to add new features or modify existing ones
- **Testability**: Components can be tested in isolation

### 3. Factory Pattern

Models are created using factory functions, providing:

- **Consistency**: Standardized model creation
- **Validation**: Built-in validation during creation
- **Flexibility**: Easy to extend with new model types

## Execution Flow

### 1. Application Startup

```
main.py
├── start_application()
│   ├── run_pre_start_tasks()
│   │   ├── ensure_directories()
│   │   ├── ensure_files()
│   │   ├── ensure_defaults()
│   │   └── subscribe_to_events()
│   ├── initialize_gui()
│   ├── run_post_start_tasks()
│   └── dispatch(APPLICATION_STARTED)
└── GUI Main Loop
```

### 2. Event Flow

```
User Action → GUI Component → Event Dispatch → Event Handler → Model Update → Storage Update
```

### 3. Data Flow

```
Storage JSON → Model Factory → GUI Display → User Input → Model Update → Storage Save
```

## Layer Responsibilities

### Core Layer (`core/`)

**Purpose**: Application lifecycle and system initialization

**Components**:
- `application.py`: Start/stop application, runtime management
- `bootstrap.py`: System setup, directory/file creation, event subscriptions
- `common.py`: Shared core utilities
- `core.py`: Core exports and initialization

**Key Responsibilities**:
- Initialize directory structure
- Create required database files
- Set up default data
- Initialize GUI components
- Manage application lifecycle
- Coordinate event subscriptions

### Model Layer (`models/`)

**Purpose**: Data structures and business logic

**Components**:
- `models.py`: Base Model class and specific model implementations
- `factory.py`: Factory functions for model creation
- `observables.py`: Observable data structures for reactive updates

**Key Responsibilities**:
- Define data structures
- Provide model validation
- Handle model relationships
- Support observable patterns
- Factory-based model creation

### GUI Layer (`gui/`)

**Purpose**: User interface and interaction handling

**Components**:
- `views/`: Main view components (dashboard, create, edit, rehearsal)
- `forms/`: Data entry forms for creating/editing content
- `logic/`: Business logic for GUI operations
- `widgets.py`: Custom GUI widgets
- `gui.py`: Main GUI management and frame access

**Key Responsibilities**:
- Display user interface
- Handle user input
- Manage view navigation
- Provide form validation
- Display feedback (toasts, dialogs)

### Storage Layer (`utils/storage.py`)

**Purpose**: Data persistence and file management

**Key Responsibilities**:
- Read/write JSON files
- Provide CRUD operations
- Handle file locking and safety
- Manage data integrity
- Support batch operations

### Event System (`utils/dispatcher.py`)

**Purpose**: Decoupled communication between components

**Key Responsibilities**:
- Event registration and subscription
- Event dispatching
- Event data management
- Subscription cleanup

## Data Architecture

### JSON-Based Storage

The application uses JSON files for data persistence, stored in `.local/data/`:

```
.local/data/
├── flashcards.json     # Flashcard data
├── stacks.json         # Stack organization
├── questions.json      # Question data
├── answers.json        # Answer data
├── notes.json         # Note data
├── rehearsal_runs.json # Rehearsal sessions
└── ...               # Other data files
```

### Model Hierarchy

```
Model (Base)
├── FlashcardModel
├── StackModel
├── QuestionModel
├── AnswerModel
├── NoteModel
├── RehearsalRunModel
├── RehearsalRunItemModel
└── ... (other models)
```

### Event Flow Patterns

#### 1. CRUD Operations

```
CREATE:
User fills form → Form validation → Model creation → Storage save → Event dispatch → GUI update

READ:
User requests data → Storage read → Model creation → GUI display

UPDATE:
User edits data → Form validation → Model update → Storage save → Event dispatch → GUI update

DELETE:
User deletes → Confirmation → Storage delete → Event dispatch → GUI update
```

#### 2. Rehearsal Flow

```
Setup Rehearsal → Select Content → Start Session → Present Items → Record Results → Save Results
```

## Key Design Patterns

### 1. Observer Pattern

Used in observable models to automatically update GUI when data changes:

```python
class ObservableModel(Model):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._observers = []
    
    def add_observer(self, observer):
        self._observers.append(observer)
    
    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)
```

### 2. Factory Pattern

Used for model creation to ensure consistency:

```python
def get_flashcard_model(**kwargs) -> Optional[FlashcardModel]:
    return get_model(type_='flashcard', **kwargs)
```

### 3. Event-Driven Architecture

Decouples components through event communication:

```python
# Event dispatch
dispatch(FLASHCARD_CREATED, {'flashcard': flashcard})

# Event subscription
subscribe(FLASHCARD_CREATED, on_flashcard_created)
```

### 4. Singleton Pattern

Used for global state management:

```python
# In constants/common.py
GLOBAL = {
    'root': None,
    'dispatcher': None,
    # ... other global state
}
```

## Configuration Management

### Constants Organization

```
constants/
├── common.py        # Global constants and state
├── defaults.py      # Default configuration values
├── directories.py   # Directory paths
├── events.py       # Event definitions
├── files.py        # File paths
└── ...            # Other constant groups
```

### Default Values

The application provides sensible defaults for:

- Difficulty levels (Easy, Medium, Hard)
- Priority levels (Low, Medium, High)
- User settings
- GUI preferences

## Error Handling Strategy

### Layered Error Handling

```
GUI Layer → Business Logic → Storage Layer → File System
     ↓             ↓              ↓             ↓
User Feedback   Logging       Error Codes   System Errors
```

### Error Categories

1. **User Input Errors**: Validation and feedback in GUI
2. **Business Logic Errors**: Handled in logic layer
3. **Storage Errors**: Logged and reported to user
4. **System Errors**: Logged and graceful degradation

## Performance Considerations

### 1. Lazy Loading

Models are loaded from storage only when needed to reduce startup time.

### 2. Event Debouncing

Rapid events are debounced to prevent excessive updates.

### 3. File I/O Optimization

JSON files are read/written efficiently with proper error handling.

### 4. Memory Management

GUI components are properly cleaned up to prevent memory leaks.

## Security Considerations

### 1. Input Validation

All user input is validated before processing or storage.

### 2. File Permissions

Application checks file permissions before attempting operations.

### 3. Data Integrity

JSON files are validated before and after operations.

## Testing Architecture

### Test Organization

```
tests/
├── test_models.py         # Model unit tests
├── test_storage.py        # Storage integration tests
├── test_dispatcher.py     # Event system tests
├── test_imports.py       # Import validation tests
└── conftest.py          # Test configuration
```

### Test Strategy

1. **Unit Tests**: Test individual components in isolation
2. **Integration Tests**: Test component interactions
3. **GUI Tests**: Test user interface behavior
4. **Storage Tests**: Test data persistence

## Future Architecture Considerations

### 1. Plugin System

The event-driven architecture supports future plugin additions.

### 2. Database Migration

JSON-based storage allows easy migration to other storage systems.

### 3. Multi-User Support

The model system can be extended for multi-user scenarios.

### 4. Web Interface

The separation of concerns allows for future web interface development.

This architecture provides a solid foundation for the current application while allowing for future growth and enhancement.
