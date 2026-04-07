# Model Layer Documentation

## Overview

The model layer forms the data foundation of StudyFrog, providing structured data representations for all entities in the system. It follows object-oriented principles with inheritance, factory patterns, and observable behaviors.

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Base Model Class](#base-model-class)
3. [Specific Model Types](#specific-model-types)
4. [Model Factory](#model-factory)
5. [Observable Models](#observable-models)
6. [Data Validation](#data-validation)
7. [Model Relationships](#model-relationships)

---

## Architecture Overview

### Model Hierarchy

```
Model (Base Class)
├── FlashcardModel
├── StackModel
├── QuestionModel
├── AnswerModel
├── NoteModel
├── RehearsalRunModel
├── RehearsalRunItemModel
├── DifficultyModel
├── PriorityModel
├── SubjectModel
├── TagModel
├── TeacherModel
├── UserModel
├── CustomFieldModel
└── AssociationModel
```

### Design Principles

1. **Inheritance**: All models inherit from base `Model` class
2. **Encapsulation**: Data is accessed through properties and methods
3. **Validation**: Models validate their own data
4. **Serialization**: Models can be serialized to/from JSON
5. **Observability**: Models can notify observers of changes

---

## Base Model Class

### Purpose

The `Model` class provides common functionality for all data entities in StudyFrog.

### Core Properties

```python
class Model:
    def __init__(self, **kwargs):
        # Identification
        self.id: Optional[int] = kwargs.get('id')
        self.key: Optional[str] = kwargs.get('key')
        self.uuid: Optional[str] = kwargs.get('uuid')
        
        # Metadata
        self.author: str = kwargs.get('author', '')
        self.created_at: Optional[datetime] = kwargs.get('created_at')
        self.created_on: Optional[date] = kwargs.get('created_on')
        self.updated_at: Optional[datetime] = kwargs.get('updated_at')
        self.updated_on: Optional[date] = kwargs.get('updated_on')
        
        # Type information
        self.type_: str = kwargs.get('type_', 'MODEL')
        
        # Custom fields
        self.customfields: list = kwargs.get('customfields', [])
        self.tags: list = kwargs.get('tags', [])
```

### Key Methods

#### Serialization

```python
def to_dict(self) -> dict[str, Any]:
    """
    Converts the model to a dictionary representation.
    
    Returns:
        dict: Dictionary representation of the model
    """

@classmethod
def from_dict(cls, data: dict[str, Any]) -> 'Model':
    """
    Creates a model instance from a dictionary.
    
    Args:
        data: Dictionary containing model data
        
    Returns:
        Model: Model instance
    """
```

#### Identification

```python
def get_identifier(self) -> str:
    """
    Gets the primary identifier for the model.
    
    Returns:
        str: The model's key or uuid
    """

def is_identifiable(self) -> bool:
    """
    Checks if the model has valid identification.
    
    Returns:
        bool: True if model has id/key/uuid
    """
```

#### Timestamp Management

```python
def update_timestamps(self) -> None:
    """
    Updates the updated_at and updated_on timestamps.
    """

def set_creation_timestamps(self) -> None:
    """
    Sets the created_at and created_on timestamps.
    """
```

#### Validation

```python
def is_valid(self) -> bool:
    """
    Validates the model's data.
    
    Returns:
        bool: True if model data is valid
    """

def get_validation_errors(self) -> list[str]:
    """
    Gets a list of validation errors.
    
    Returns:
        list: List of validation error messages
    """
```

### Metadata Structure

All models include a metadata dictionary:

```python
self.metadata = {
    'author': self.author,
    'created_at': self.created_at,
    'created_on': self.created_on,
    'fields': {
        'total': 22,  # Number of fields
        'values': ['field1', 'field2', ...]  # Field names
    },
    'type': self.type_,
    'updated_at': self.updated_at,
    'updated_on': self.updated_on
}
```

---

## Specific Model Types

### FlashcardModel

Represents a flashcard with front/back content.

```python
class FlashcardModel(Model):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type_ = 'FLASHCARD'
        
        # Core content
        self.front: str = kwargs.get('front', '')
        self.back: str = kwargs.get('back', '')
        
        # Study properties
        self.difficulty: str = kwargs.get('difficulty', 'Medium')
        self.priority: str = kwargs.get('priority', 'Medium')
        self.subject: str = kwargs.get('subject', '')
        self.teacher: str = kwargs.get('teacher', '')
        
        # Tracking
        self.is_assigned_to_stack: bool = kwargs.get('is_assigned_to_stack', False)
        self.last_viewed_at: Optional[datetime] = kwargs.get('last_viewed_at')
        self.last_viewed_on: Optional[date] = kwargs.get('last_viewed_on')
        self.next_view_on: Optional[date] = kwargs.get('next_view_on')
```

**Key Features**:
- Front/back question format
- Difficulty and priority levels
- Study scheduling support
- Stack assignment tracking

### StackModel

Represents a collection/stack of flashcards.

```python
class StackModel(Model):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type_ = 'STACK'
        
        # Basic properties
        self.name: str = kwargs.get('name', '')
        self.description: str = kwargs.get('description', '')
        
        # Organization
        self.parent: Optional[str] = kwargs.get('parent')
        self.children: list = kwargs.get('children', [])
        self.items: list = kwargs.get('items', [])  # Flashcard keys
        
        # Categorization
        self.subject: str = kwargs.get('subject', '')
        self.teacher: str = kwargs.get('teacher', '')
```

**Key Features**:
- Hierarchical organization (parent/child)
- Item collection management
- Subject and teacher categorization

### QuestionModel

Represents a question that can have multiple answers.

```python
class QuestionModel(Model):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type_ = 'QUESTION'
        
        # Question content
        self.question_text: str = kwargs.get('question_text', '')
        self.question_type: str = kwargs.get('question_type', 'OPEN_ENDED')
        
        # Options for multiple choice
        self.options: list = kwargs.get('options', [])
        self.correct_answer: str = kwargs.get('correct_answer', '')
        
        # Categorization
        self.difficulty: str = kwargs.get('difficulty', 'Medium')
        self.subject: str = kwargs.get('subject', '')
        self.teacher: str = kwargs.get('teacher', '')
```

**Question Types**:
- `OPEN_ENDED`: Free text response
- `MULTIPLE_CHOICE`: Select from options
- `TRUE_FALSE`: True/False selection

### AnswerModel

Represents an answer to a question.

```python
class AnswerModel(Model):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type_ = 'ANSWER'
        
        # Answer content
        self.answer_text: str = kwargs.get('answer_text', '')
        self.answer_type: str = kwargs.get('answer_type', 'OPEN_ENDED')
        
        # Scoring
        self.is_correct: bool = kwargs.get('is_correct', False)
        self.points: int = kwargs.get('points', 0)
        
        # Association
        self.question_key: Optional[str] = kwargs.get('question_key')
```

### NoteModel

Represents a study note or text content.

```python
class NoteModel(Model):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type_ = 'NOTE'
        
        # Content
        self.title: str = kwargs.get('title', '')
        self.content: str = kwargs.get('content', '')
        
        # Organization
        self.subject: str = kwargs.get('subject', '')
        self.teacher: str = kwargs.get('teacher', '')
        self.tags: list = kwargs.get('tags', [])
```

### RehearsalRunModel

Represents a rehearsal/study session.

```python
class RehearsalRunModel(Model):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type_ = 'REHEARSAL_RUN'
        
        # Session info
        self.session_name: str = kwargs.get('session_name', '')
        self.start_time: Optional[datetime] = kwargs.get('start_time')
        self.end_time: Optional[datetime] = kwargs.get('end_time')
        
        # Configuration
        self.item_type: str = kwargs.get('item_type', 'FLASHCARD')
        self.stack_keys: list = kwargs.get('stack_keys', [])
        self.max_items: int = kwargs.get('max_items', 0)
        
        # Results
        self.total_items: int = kwargs.get('total_items', 0)
        self.correct_answers: int = kwargs.get('correct_answers', 0)
        self.incorrect_answers: int = kwargs.get('incorrect_answers', 0)
```

### RehearsalRunItemModel

Represents an individual item within a rehearsal session.

```python
class RehearsalRunItemModel(Model):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type_ = 'REHEARSAL_RUN_ITEM'
        
        # Association
        self.rehearsal_run_key: Optional[str] = kwargs.get('rehearsal_run_key')
        self.item_key: Optional[str] = kwargs.get('item_key')
        
        # Performance
        self.is_correct: bool = kwargs.get('is_correct', False)
        self.response_time: float = kwargs.get('response_time', 0.0)
        self.attempts: int = kwargs.get('attempts', 1)
        
        # Timing
        self.presented_at: Optional[datetime] = kwargs.get('presented_at')
        self.answered_at: Optional[datetime] = kwargs.get('answered_at')
```

---

## Model Factory

### Purpose

The model factory provides a standardized way to create model instances with proper validation and type conversion.

### Key Functions

#### Generic Model Creation

```python
def get_model(type_: str, **kwargs) -> Optional[Model]:
    """
    Creates a model instance based on type.
    
    Args:
        type_: The model type ('flashcard', 'stack', etc.)
        **kwargs: Model parameters
        
    Returns:
        Model: Model instance or None if type not found
    """
```

**Supported Types**:
- `'flashcard'` → `FlashcardModel`
- `'stack'` → `StackModel`
- `'question'` → `QuestionModel`
- `'answer'` → `AnswerModel`
- `'note'` → `NoteModel`
- `'rehearsal_run'` → `RehearsalRunModel`
- `'rehearsal_run_item'` → `RehearsalRunItemModel`

#### Specific Factory Functions

```python
def get_flashcard_model(**kwargs) -> Optional[FlashcardModel]:
    """Creates a flashcard model instance."""

def get_stack_model(**kwargs) -> Optional[StackModel]:
    """Creates a stack model instance."""

def get_question_model(**kwargs) -> Optional[QuestionModel]:
    """Creates a question model instance."""

def get_answer_model(**kwargs) -> Optional[AnswerModel]:
    """Creates an answer model instance."""

def get_note_model(**kwargs) -> Optional[NoteModel]:
    """Creates a note model instance."""

def get_rehearsal_run_model(**kwargs) -> Optional[RehearsalRunModel]:
    """Creates a rehearsal run model instance."""

def get_rehearsal_run_item_model(**kwargs) -> Optional[RehearsalRunItemModel]:
    """Creates a rehearsal run item model instance."""
```

### Parameter Conversion

The factory automatically converts certain parameter types:

```python
def _convert_parameters(type_: str, **kwargs) -> dict[str, Any]:
    """
    Converts parameters to appropriate types for the model.
    
    Conversions performed:
    - String dates to datetime objects
    - String UUIDs to UUID objects
    - Numeric strings to numbers
    """
```

**Conversion Examples**:
```python
# Date strings
"2026-01-01T10:00:00" → datetime(2026, 1, 1, 10, 0, 0)
"2026-01-01" → date(2026, 1, 1)

# UUID strings
"550e8400-e29b-41d4-a716-446655440000" → UUID object

# Numeric strings
"123" → 123 (int)
"123.45" → 123.45 (float)
```

### Validation

Factory functions include validation:

```python
def _validate_parameters(type_: str, **kwargs) -> bool:
    """
    Validates parameters for the specified model type.
    
    Returns:
        bool: True if parameters are valid
    """
```

### Usage Examples

```python
# Create a flashcard
flashcard = get_flashcard_model(
    front="What is the capital of France?",
    back="Paris",
    difficulty="Easy",
    priority="High"
)

# Create a stack
stack = get_stack_model(
    name="Geography",
    description="World capitals and countries"
)

# Create from dictionary
data = {
    'front': 'Question',
    'back': 'Answer',
    'difficulty': 'Medium'
}
flashcard = get_model(type_='flashcard', **data)
```

---

## Observable Models

### Purpose

Observable models provide reactive behavior, automatically notifying observers when data changes.

### Implementation

```python
class ObservableModel(Model):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._observers: list[Callable] = []
        self._changed_fields: set = set()
    
    def add_observer(self, observer: Callable) -> None:
        """Add an observer to be notified of changes."""
        if observer not in self._observers:
            self._observers.append(observer)
    
    def remove_observer(self, observer: Callable) -> None:
        """Remove an observer."""
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify_observers(self) -> None:
        """Notify all observers of changes."""
        for observer in self._observers:
            observer(self)
    
    def _set_field(self, field_name: str, value: Any) -> None:
        """Set a field value and mark as changed."""
        if hasattr(self, field_name):
            old_value = getattr(self, field_name)
            if old_value != value:
                setattr(self, field_name, value)
                self._changed_fields.add(field_name)
                self.notify_observers()
```

### Observer Interface

```python
def model_changed_observer(model: ObservableModel) -> None:
    """
    Observer function called when model changes.
    
    Args:
        model: The model that changed
    """
    changed_fields = model.get_changed_fields()
    print(f"Model changed: {changed_fields}")
```

### Usage Example

```python
# Create observable model
flashcard = get_flashcard_model(front="Question", back="Answer")

# Add observer
flashcard.add_observer(model_changed_observer)

# Change model (triggers notification)
flashcard.front = "Updated question"
```

---

## Data Validation

### Validation Levels

1. **Field-level validation**: Individual field validation
2. **Model-level validation**: Cross-field validation
3. **Business rule validation**: Application-specific rules

### Validation Methods

```python
def validate_field(self, field_name: str, value: Any) -> bool:
    """
    Validates a single field value.
    
    Args:
        field_name: Name of the field to validate
        value: Value to validate
        
    Returns:
        bool: True if valid
    """

def validate_model(self) -> list[str]:
    """
    Validates the entire model.
    
    Returns:
        list: List of validation error messages
    """
```

### Common Validation Rules

#### Required Fields
```python
def validate_required_fields(self) -> list[str]:
    """Validates that all required fields are present."""
    errors = []
    required_fields = self.get_required_fields()
    
    for field in required_fields:
        if not hasattr(self, field) or getattr(self, field) in [None, '']:
            errors.append(f"{field} is required")
    
    return errors
```

#### Field Types
```python
def validate_field_types(self) -> list[str]:
    """Validates field types."""
    errors = []
    field_types = self.get_field_types()
    
    for field, expected_type in field_types.items():
        if hasattr(self, field):
            value = getattr(self, field)
            if value is not None and not isinstance(value, expected_type):
                errors.append(f"{field} must be {expected_type.__name__}")
    
    return errors
```

#### String Length
```python
def validate_string_lengths(self) -> list[str]:
    """Validates string field lengths."""
    errors = []
    length_limits = self.get_length_limits()
    
    for field, max_length in length_limits.items():
        if hasattr(self, field):
            value = getattr(self, field)
            if isinstance(value, str) and len(value) > max_length:
                errors.append(f"{field} exceeds maximum length of {max_length}")
    
    return errors
```

### Model-Specific Validation

#### Flashcard Validation
```python
class FlashcardModel(Model):
    def validate_model(self) -> list[str]:
        errors = super().validate_model()
        
        # Validate front/back content
        if not self.front.strip():
            errors.append("Front content cannot be empty")
        if not self.back.strip():
            errors.append("Back content cannot be empty")
        
        # Validate difficulty
        valid_difficulties = ['Easy', 'Medium', 'Hard']
        if self.difficulty not in valid_difficulties:
            errors.append(f"Invalid difficulty: {self.difficulty}")
        
        return errors
```

#### Stack Validation
```python
class StackModel(Model):
    def validate_model(self) -> list[str]:
        errors = super().validate_model()
        
        # Validate name
        if not self.name.strip():
            errors.append("Stack name cannot be empty")
        
        # Validate items
        if not isinstance(self.items, list):
            errors.append("Items must be a list")
        
        return errors
```

---

## Model Relationships

### Association Patterns

#### One-to-Many
```python
# Stack has many flashcards
class StackModel(Model):
    def get_flashcards(self) -> list[FlashcardModel]:
        """Get all flashcards in this stack."""
        from studyfrog.utils.storage import get_entries
        return get_entries(FLASHCARDS_DB_JSON, self.items)
```

#### Many-to-Many
```python
# Flashcards can be in multiple stacks (via associations)
class AssociationModel(Model):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.flashcard_key: str = kwargs.get('flashcard_key')
        self.stack_key: str = kwargs.get('stack_key')
```

### Referential Integrity

```python
def validate_references(self) -> list[str]:
    """Validates that references point to existing entities."""
    errors = []
    
    # Validate stack references
    if hasattr(self, 'stack_key') and self.stack_key:
        if not get_entry(STACKS_DB_JSON, self.stack_key):
            errors.append(f"Stack {self.stack_key} does not exist")
    
    return errors
```

### Cascade Operations

```python
def delete_stack_cascade(stack_key: str) -> None:
    """Delete a stack and update associated flashcards."""
    # Delete the stack
    delete_entry(STACKS_DB_JSON, stack_key)
    
    # Update flashcards to remove stack reference
    flashcards = get_all_entries(FLASHCARDS_DB_JSON)
    for flashcard in flashcards:
        if stack_key in flashcard.stack_keys:
            flashcard.stack_keys.remove(stack_key)
            update_entry(FLASHCARDS_DB_JSON, flashcard)
```

---

## Model Layer Best Practices

### 1. Always Use Factory Functions

```python
# Good
flashcard = get_flashcard_model(front="Q", back="A")

# Avoid
flashcard = FlashcardModel(front="Q", back="A")  # No validation
```

### 2. Validate Before Saving

```python
flashcard = get_flashcard_model(**data)
if flashcard.is_valid():
    add_entry(FLASHCARDS_DB_JSON, flashcard)
else:
    show_errors(flashcard.get_validation_errors())
```

### 3. Use Observers for GUI Updates

```python
# In GUI component
def on_model_changed(model: ObservableModel) -> None:
    refresh_display()

# In model setup
model.add_observer(on_model_changed)
```

### 4. Handle Serialization Properly

```python
# Save model
data = model.to_dict()
with open(file_path, 'w') as f:
    json.dump(data, f, indent=2, default=str)

# Load model
with open(file_path, 'r') as f:
    data = json.load(f)
model = Model.from_dict(data)
```

### 5. Maintain Timestamps

```python
# On creation
model.set_creation_timestamps()

# On update
model.update_timestamps()
```

The model layer provides a robust foundation for data management in StudyFrog, ensuring data integrity, validation, and proper relationships between entities.
