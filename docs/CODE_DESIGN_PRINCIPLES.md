# StudyFrog Code Design Principles

## Overview

This document outlines the core design principles that guide StudyFrog development. These principles ensure maintainable, testable, and efficient code that follows functional programming concepts while maintaining clarity of purpose.

## Table of Contents

1. [Core Philosophy](#core-philosophy)
2. [Function-Oriented Design](#function-oriented-design)
3. [Minimal Nesting](#minimal-nesting)
4. [Single Purpose Methods](#single-purpose-methods)
5. [Pure Data Storage](#pure-data-storage)
6. [Additional Principles](#additional-principles)
7. [Practical Examples](#practical-examples)
8. [Anti-Patterns](#anti-patterns)
9. [Implementation Guidelines](#implementation-guidelines)

---

## Core Philosophy

StudyFrog follows a **functional-first design philosophy** that prioritizes:

- **Clarity of Intent**: Every function has a clear, single purpose
- **Predictable Behavior**: Functions do exactly what they say, no side effects
- **Testability**: Pure functions are easy to test in isolation
- **Maintainability**: Simple, focused code is easier to understand and modify
- **Performance**: Minimal overhead through focused, efficient operations

---

## Function-Oriented Design

### Principle

Functions are the primary building blocks of StudyFrog. Each function should be:

- **Pure**: Same inputs always produce same outputs
- **Focused**: Handle one specific task or transformation
- **Composable**: Can be combined to create complex behaviors
- **Stateless**: Don't maintain internal state between calls

### Implementation Guidelines

```python
# Good - Function-oriented approach
def calculate_flashcard_score(flashcard: FlashcardModel, difficulty_weights: dict) -> float:
    """
    Calculate a flashcard's score based on difficulty.
    
    Args:
        flashcard: The flashcard to score
        difficulty_weights: Mapping of difficulty to score multiplier
        
    Returns:
        float: The calculated score
    """
    weight = difficulty_weights.get(flashcard.difficulty, 1.0)
    return weight * flashcard.priority_value

# Avoid - Object-oriented with unnecessary state
class FlashcardScorer:
    def __init__(self, difficulty_weights: dict):
        self.weights = difficulty_weights
        self.last_score = 0
    
    def calculate(self, flashcard: FlashcardModel) -> float:
        # Maintains state unnecessarily
        weight = self.weights.get(flashcard.difficulty, 1.0)
        self.last_score = weight * flashcard.priority_value
        return self.last_score
```

### Function Composition

```python
# Compose simple functions into complex operations
def validate_flashcard_text(text: str) -> bool:
    """Validate flashcard text content."""
    return bool(text and text.strip())

def sanitize_flashcard_text(text: str) -> str:
    """Sanitize flashcard text for storage."""
    return text.strip().replace('\n', ' ').replace('\r', ' ')

def prepare_flashcard_content(raw_text: str) -> Optional[str]:
    """Prepare flashcard content for storage."""
    if not validate_flashcard_text(raw_text):
        return None
    return sanitize_flashcard_text(raw_text)

# Usage combines multiple functions
def process_flashcard_input(user_input: str) -> Optional[str]:
    """Process user input for flashcard creation."""
    return prepare_flashcard_content(user_input)
```

---

## Minimal Nesting

### Principle

Avoid deep nesting of functions and classes. Flat structures are easier to:

- **Test**: Each function can be tested independently
- **Debug**: Simpler call stacks and error traces
- **Understand**: Linear flow is easier to follow
- **Maintain**: Changes don't affect deeply nested logic

### Implementation Guidelines

```python
# Good - Flat structure with clear flow
def create_flashcard(front: str, back: str) -> Optional[FlashcardModel]:
    """Create a new flashcard with validation."""
    if not validate_flashcard_content(front):
        log_error("Invalid front content")
        return None
    
    if not validate_flashcard_content(back):
        log_error("Invalid back content")
        return None
    
    return get_flashcard_model(front=front, back=back)

def save_flashcard(flashcard: FlashcardModel) -> bool:
    """Save flashcard to storage."""
    return add_entry(FLASHCARDS_DB_JSON, flashcard)

# Usage - clear, linear flow
def handle_flashcard_creation(front: str, back: str) -> bool:
    flashcard = create_flashcard(front, back)
    if flashcard:
        return save_flashcard(flashcard)
    return False

# Avoid - Deep nesting
class FlashcardCreator:
    def __init__(self):
        self.validator = FlashcardValidator()
        self.storage = FlashcardStorage()
        self.logger = FlashcardLogger()
    
    def create(self, front: str, back: str):
        def validate_and_create():
            if self.validator.validate(front):
                if self.validator.validate(back):
                    return self.storage.save(self.model_factory.create(front, back))
        return validate_and_create()
        
        # Nested function makes testing and debugging difficult
        return validate_and_create()
```

### Nesting Limits

- **Maximum Depth**: No more than 2-3 levels of function nesting
- **Early Returns**: Validate inputs early, return on first error
- **Guard Clauses**: Use guard clauses instead of nested if statements
- **Extract Functions**: Pull nested logic into separate functions

---

## Single Purpose Methods

### Principle

Each method or function should have **one specific purpose and outcome**:

- **Clear Name**: Function name describes exactly what it does
- **Single Responsibility**: One function, one job
- **Predictable Output**: Consistent return types and behavior
- **No Side Effects**: Don't modify external state unexpectedly

### Implementation Guidelines

```python
# Good - Single purpose functions
def validate_flashcard_front(text: str) -> bool:
    """Validate flashcard front text."""
    return len(text.strip()) > 0 and len(text.strip()) <= MAX_FRONT_LENGTH

def validate_flashcard_back(text: str) -> bool:
    """Validate flashcard back text."""
    return len(text.strip()) > 0 and len(text.strip()) <= MAX_BACK_LENGTH

def calculate_rehearsal_score(correct: int, total: int) -> float:
    """Calculate rehearsal score as percentage."""
    if total == 0:
        return 0.0
    return (correct / total) * 100

# Usage - each function has clear purpose
def create_flashcard_with_validation(front: str, back: str) -> Optional[FlashcardModel]:
    """Create flashcard with full validation."""
    if not validate_flashcard_front(front):
        show_error("Front text is invalid")
        return None
    
    if not validate_flashcard_back(back):
        show_error("Back text is invalid")
        return None
    
    return get_flashcard_model(front=front, back=back)

# Avoid - Multi-purpose functions
def process_flashcard_data(front: str, back: str, operation: str) -> dict:
    """Does too many things - unclear purpose."""
    # What does this function actually do?
    if operation == "validate":
        # Validate logic
    elif operation == "create":
        # Create logic
    elif operation == "save":
        # Save logic
    # Unclear responsibility and outcome
```

### Function Naming

```python
# Good - Clear, purpose-driven names
def is_valid_flashcard_text(text: str) -> bool:
    """Check if text is valid for flashcard."""
    pass

def get_flashcard_count_by_stack(stack_key: str) -> int:
    """Get total number of flashcards in a stack."""
    pass

def format_flashcard_for_display(flashcard: FlashcardModel) -> str:
    """Format flashcard for GUI display."""
    pass

# Avoid - unclear names
def process_data(data: dict) -> dict:
    """What does this process?"""
    pass

def handle_item(item: dict) -> bool:
    """Handle what kind of item?"""
    pass
```

---

## Pure Data Storage

### Principle

Data storage should be **pure and transparent**:

- **No Business Logic**: Storage functions only handle data persistence
- **No Hidden State**: Don't embed business rules in storage layer
- **Direct Mapping**: JSON fields map directly to data structures
- **Immutable Operations**: Storage operations don't modify input data

### Implementation Guidelines

```python
# Good - Pure storage functions
def save_flashcard(flashcard: FlashcardModel) -> bool:
    """
    Save flashcard to JSON storage.
    
    Args:
        flashcard: The flashcard model to save
        
    Returns:
        bool: True if saved successfully
    """
    try:
        flashcard_dict = flashcard.to_dict()
        return add_entry(FLASHCARDS_DB_JSON, flashcard_dict)
    except Exception as e:
        log_error(f"Failed to save flashcard: {e}")
        return False

def load_flashcard(key: str) -> Optional[dict]:
    """
    Load flashcard from JSON storage.
    
    Args:
        key: The flashcard key to load
        
    Returns:
        dict: Flashcard data or None if not found
    """
    try:
        return get_entry(FLASHCARDS_DB_JSON, key)
    except Exception as e:
        log_error(f"Failed to load flashcard: {e}")
        return None

# Usage - clear separation of concerns
def flashcard_business_logic(front: str, back: str) -> Optional[FlashcardModel]:
    """Business logic for flashcard creation."""
    # Validation, defaults, business rules
    if not is_valid_flashcard_content(front):
        return None
    
    return get_flashcard_model(front=front, back=back)

def handle_flashcard_creation(front: str, back: str) -> bool:
    """Handle the complete flashcard creation process."""
    # Business logic
    flashcard = flashcard_business_logic(front, back)
    if not flashcard:
        return False
    
    # Pure storage operation
    return save_flashcard(flashcard)

# Avoid - mixing concerns
def create_and_save_flashcard(front: str, back: str) -> bool:
    """Mixes business logic and storage - bad practice."""
    # Validation mixed with storage
    if not is_valid_flashcard_content(front):
        return False  # Early return, but storage logic mixed
    
    flashcard = get_flashcard_model(front=front, back=back)
    flashcard.created_at = datetime.now()
    
    # Storage with embedded business logic
    try:
        if flashcard.difficulty == "Easy":
            flashcard.priority = 1  # Business rule in storage layer
        return add_entry(FLASHCARDS_DB_JSON, flashcard.to_dict())
    except Exception as e:
        return False
```

### Data Structure Mapping

```python
# Good - Direct mapping between JSON and models
def flashcard_from_dict(data: dict) -> FlashcardModel:
    """Convert JSON data to flashcard model."""
    return get_flashcard_model(**data)

def flashcard_to_dict(flashcard: FlashcardModel) -> dict:
    """Convert flashcard model to JSON data."""
    return flashcard.to_dict()

# JSON structure matches model structure exactly
{
    "front": "What is capital of France?",
    "back": "Paris",
    "difficulty": "Easy",
    "created_at": "2026-01-01T10:00:00"
}
```

---

## Additional Principles

### 1. Immutability

Treat data as immutable wherever possible:

```python
# Good - Return new instances instead of modifying
def update_flashcard_text(flashcard: FlashcardModel, new_front: str) -> FlashcardModel:
    """Create new flashcard with updated text."""
    return get_flashcard_model(
        front=new_front,
        back=flashcard.back,
        difficulty=flashcard.difficulty,
        # ... copy all other fields
    )

# Avoid - modifying inputs
def update_flashcard_text_bad(flashcard: FlashcardModel, new_front: str) -> None:
    """Modifies the input flashcard - side effect."""
    flashcard.front = new_front  # Modifies original
    flashcard.updated_at = datetime.now()
    return None
```

### 2. Explicit Dependencies

Make dependencies clear and explicit:

```python
# Good - Explicit dependencies
def calculate_session_score(responses: list[bool], time_limit: int) -> float:
    """Calculate session score with explicit parameters."""
    correct_count = sum(responses)
    total_questions = len(responses)
    return (correct_count / total_questions) * 100 if total_questions > 0 else 0

# Avoid - Hidden dependencies
def calculate_session_score_bad() -> float:
    """Relies on global state - unclear dependencies."""
    global _current_session_responses, _current_session_time_limit
    correct_count = sum(_current_session_responses)
    total_questions = len(_current_session_responses)
    return (correct_count / total_questions) * 100
```

### 3. Error Handling

Handle errors explicitly and predictably:

```python
# Good - Explicit error handling
def load_flashcard_safe(key: str) -> tuple[Optional[FlashcardModel], Optional[str]]:
    """
    Load flashcard with explicit error handling.
    
    Returns:
        tuple: (flashcard, error_message)
    """
    try:
        data = get_entry(FLASHCARDS_DB_JSON, key)
        if not data:
            return None, f"Flashcard {key} not found"
        
        flashcard = flashcard_from_dict(data)
        if not flashcard.is_valid():
            return None, f"Flashcard {key} has invalid data"
        
        return flashcard, None
        
    except FileNotFoundError:
        return None, f"Storage file not found"
    except json.JSONDecodeError as e:
        return None, f"Invalid JSON format: {e}"
    except Exception as e:
        return None, f"Unexpected error: {e}"

# Usage - clear error handling
flashcard, error = load_flashcard_safe("FLASHCARD_1")
if error:
    show_error(error)
else:
    display_flashcard(flashcard)
```

### 4. Type Safety

Use type hints and validate types:

```python
# Good - Type-safe functions
def process_flashcard_list(flashcards: list[FlashcardModel]) -> list[str]:
    """
    Process flashcard list with type safety.
    
    Args:
        flashcards: List of flashcard models
        
    Returns:
        list[str]: List of flashcard fronts
    """
    return [flashcard.front for flashcard in flashcards if isinstance(flashcard, FlashcardModel)]

# Avoid - Type confusion
def process_flashcard_list_bad(flashcards) -> list:
    """Unclear about input types."""
    # What type is flashcards? How to handle different types?
    return [item.front for item in flashcards]  # May fail if not FlashcardModel
```

---

## Practical Examples

### Complete Example: Flashcard Creation

```python
# Following all principles in a complete workflow

# 1. Pure validation functions
def is_valid_flashcard_length(text: str, max_length: int) -> bool:
    """Check if text length is within limits."""
    return 0 < len(text.strip()) <= max_length

def has_valid_flashcard_content(front: str, back: str) -> bool:
    """Check if both front and back have valid content."""
    return (is_valid_flashcard_length(front, MAX_FRONT_LENGTH) and 
            is_valid_flashcard_length(back, MAX_BACK_LENGTH))

# 2. Pure data transformation
def create_flashcard_data(front: str, back: str) -> dict:
    """Create flashcard data dictionary."""
    return {
        "front": front.strip(),
        "back": back.strip(),
        "difficulty": DEFAULT_MEDIUM_DIFFICULTY,
        "priority": DEFAULT_MEDIUM_PRIORITY,
        "created_at": get_now().isoformat()
    }

# 3. Pure storage operation
def save_flashcard_pure(data: dict) -> bool:
    """Save flashcard data to storage."""
    try:
        return add_entry(FLASHCARDS_DB_JSON, data)
    except Exception as e:
        log_error(f"Storage error: {e}")
        return False

# 4. Orchestrating function (single purpose)
def create_new_flashcard(front: str, back: str) -> tuple[bool, str]:
    """
    Create a new flashcard following all design principles.
    
    Returns:
        tuple: (success, message)
    """
    # Validate inputs
    if not has_valid_flashcard_content(front, back):
        return False, "Invalid flashcard content"
    
    # Transform data
    flashcard_data = create_flashcard_data(front, back)
    
    # Save to storage
    if not save_flashcard_pure(flashcard_data):
        return False, "Failed to save flashcard"
    
    # Success
    return True, "Flashcard created successfully"

# 5. Usage - clear, testable flow
def handle_user_flashcard_request(user_front: str, user_back: str) -> None:
    """Handle user's flashcard creation request."""
    success, message = create_new_flashcard(user_front, user_back)
    
    if success:
        show_success(message)
        dispatch(FLASHCARD_CREATED, {"source": "user_request"})
    else:
        show_error(message)
```

### Example: Rehearsal Session

```python
# Function-oriented rehearsal session management

# 1. Pure calculation functions
def calculate_session_statistics(responses: list[dict]) -> dict:
    """Calculate session statistics from responses."""
    correct = sum(1 for r in responses if r.get("is_correct", False))
    total = len(responses)
    average_time = sum(r.get("response_time", 0) for r in responses) / total
    
    return {
        "correct": correct,
        "total": total,
        "accuracy": (correct / total * 100) if total > 0 else 0,
        "average_response_time": average_time
    }

def is_session_complete(session_config: dict, current_item_count: int) -> bool:
    """Check if session should end."""
    max_items = session_config.get("max_items", 0)
    time_limit = session_config.get("time_limit", 0)
    elapsed_time = session_config.get("elapsed_time", 0)
    
    return (max_items > 0 and current_item_count >= max_items) or \
           (time_limit > 0 and elapsed_time >= time_limit)

# 2. State management (minimal, explicit)
def start_rehearsal_session(config: dict) -> dict:
    """Start a new rehearsal session."""
    return {
        "config": config,
        "start_time": get_now(),
        "current_item_index": 0,
        "responses": [],
        "is_active": True
    }

def add_session_response(session: dict, response: dict) -> dict:
    """Add response to session."""
    new_responses = session["responses"] + [response]
    updated_session = session.copy()
    updated_session["responses"] = new_responses
    return updated_session

# 3. Single purpose operations
def present_next_item(session: dict) -> tuple[dict, Optional[dict]]:
    """Get next item to present in session."""
    if not session["is_active"]:
        return session, None
    
    # Get next item logic would go here
    next_item = get_next_rehearsal_item(session)
    return session, next_item

def record_response(session: dict, item_key: str, response_data: dict) -> dict:
    """Record user response for current item."""
    response = {
        "item_key": item_key,
        "timestamp": get_now(),
        **response_data
    }
    
    return add_session_response(session, response)

# 4. Orchestrated workflow
def run_rehearsal_session(config: dict) -> dict:
    """Run complete rehearsal session."""
    session = start_rehearsal_session(config)
    
    while session["is_active"]:
        # Present item
        session, item = present_next_item(session)
        if item is None:
            break
        
        # Collect response (this would be handled by GUI)
        # response = collect_user_response(item)
        # session = record_response(session, response)
        
        # Check if session should continue
        session["elapsed_time"] = (get_now() - session["start_time"]).total_seconds()
        if is_session_complete(session["config"], session["current_item_index"]):
            session["is_active"] = False
    
    # Calculate final statistics
    statistics = calculate_session_statistics(session["responses"])
    final_session = session.copy()
    final_session["statistics"] = statistics
    final_session["end_time"] = get_now()
    
    return final_session
```

---

## Anti-Patterns

### 1. God Functions

**Avoid**: Functions that do too many things

```python
# Bad - God function
def process_flashcard_operation(operation: str, data: dict) -> dict:
    """Handles create, update, delete, validate, export, import..."""
    if operation == "create":
        # 50 lines of creation logic
    elif operation == "update":
        # 50 lines of update logic
    elif operation == "delete":
        # 50 lines of deletion logic
    # ... hundreds of lines
    
# Good - Single purpose functions
def create_flashcard(data: dict) -> FlashcardModel:
    """Only creates flashcards."""
    pass

def update_flashcard(key: str, data: dict) -> bool:
    """Only updates flashcards."""
    pass

def delete_flashcard(key: str) -> bool:
    """Only deletes flashcards."""
    pass
```

### 2. Deep Nesting

**Avoid**: Functions nested more than 2-3 levels deep

```python
# Bad - Excessive nesting
def complex_operation(data: dict):
    def inner_function_1(x):
        def inner_function_2(y):
            def inner_function_3(z):
                # Deep nesting makes code hard to follow
                return x + y + z
            return inner_function_3(5)
        return inner_function_2(10)
    return inner_function_1(20)

# Good - Flat structure
def add_three_numbers(a: int, b: int, c: int) -> int:
    """Clear, single purpose."""
    return a + b + c

def complex_operation_flat(data: dict):
    """Flat, readable structure."""
    result = add_three_numbers(10, 20, 30)
    return process_result(result)
```

### 3. Hidden Side Effects

**Avoid**: Functions that modify external state unexpectedly

```python
# Bad - Hidden side effects
global_counter = 0

def increment_counter_and_process(data: dict) -> dict:
    """Modifies global state as side effect."""
    global global_counter
    global_counter += 1  # Hidden side effect
    return process_data(data)

# Good - Pure functions
def process_data_pure(data: dict) -> dict:
    """Pure function - no side effects."""
    return process_data(data)

# State management is explicit
def increment_counter_explicit(counter: int) -> int:
    """Explicit state modification."""
    return counter + 1

current_counter = 0
current_counter = increment_counter_explicit(current_counter)
```

### 4. Mixed Concerns

**Avoid**: Functions that mix business logic, storage, and GUI

```python
# Bad - Mixed concerns
def create_and_display_flashcard(front: str, back: str):
    """Mixes creation, storage, and display."""
    flashcard = get_flashcard_model(front, back)
    
    # Storage logic mixed with display logic
    try:
        add_entry(FLASHCARDS_DB_JSON, flashcard)
        show_success("Flashcard saved!")
        update_display_list()  # GUI logic in storage function
    except Exception as e:
        show_error(f"Save failed: {e}")  # GUI logic in storage function

# Good - Separated concerns
def create_flashcard_pure(front: str, back: str) -> bool:
    """Only handles creation and storage."""
    flashcard = get_flashcard_model(front, back)
    return add_entry(FLASHCARDS_DB_JSON, flashcard)

def handle_flashcard_creation_result(success: bool, message: str) -> None:
    """Only handles display logic."""
    if success:
        show_success(message)
        update_display_list()
    else:
        show_error(message)
```

---

## Implementation Guidelines

### 1. Function Design Checklist

For every function, ask:

- [ ] **Single Purpose**: Does this function do exactly one thing?
- [ ] **Clear Name**: Does the name clearly describe what it does?
- [ ] **Pure Inputs**: Does it avoid modifying input parameters?
- [ ] **Predictable Output**: Does it always return the same type for the same inputs?
- [ ] **No Side Effects**: Does it avoid modifying external state?
- [ ] **Testable**: Can it be easily tested in isolation?
- [ ] **Documented**: Is the purpose and behavior clearly documented?

### 2. Code Review Checklist

When reviewing code, check for:

- [ ] **Function Length**: Is the function reasonably short (under 50 lines)?
- [ ] **Nesting Depth**: Is nesting limited to 2-3 levels maximum?
- [ ] **Parameter Count**: Does the function have 3-5 parameters maximum?
- [ ] **Dependencies**: Are all dependencies explicit and minimal?
- [ ] **Error Handling**: Are errors handled explicitly and appropriately?
- [ ] **Type Safety**: Are type hints used and validated?

### 3. Testing Strategy

```python
# Test each function independently
def test_is_valid_flashcard_length():
    """Test flashcard length validation."""
    # Test valid cases
    assert is_valid_flashcard_length("Hello", 50) == True
    assert is_valid_flashcard_length("", 50) == False
    
    # Test edge cases
    assert is_valid_flashcard_length("A" * 50, 50) == False
    assert is_valid_flashcard_length("Hello", 5) == False

# Test function composition
def test_create_flashcard_data():
    """Test flashcard data creation."""
    front = "What is capital of France?"
    back = "Paris"
    
    data = create_flashcard_data(front, back)
    
    assert data["front"] == front.strip()
    assert data["back"] == back.strip()
    assert "difficulty" in data
    assert "created_at" in data
```

### 4. Refactoring Guidelines

When refactoring code:

1. **Extract Functions**: Pull repeated logic into separate functions
2. **Reduce Nesting**: Flatten deeply nested structures
3. **Single Purpose**: Split multi-purpose functions
4. **Remove Duplication**: Create reusable pure functions
5. **Improve Names**: Make function names more descriptive
6. **Add Types**: Include type hints for better safety

---

## Summary

StudyFrog's code design principles ensure:

### 🎯 **Function-Oriented Architecture**
- Pure functions with single responsibilities
- Composable building blocks for complex behavior
- Testable units with predictable behavior

### 📦 **Minimal Complexity**
- Flat structures with limited nesting
- Clear, linear execution flows
- Easy to understand and maintain

### 🎪 **Single Purpose Methods**
- Each function has one specific outcome
- Clear names that describe exact behavior
- No hidden side effects or state modification

### 💾 **Pure Data Storage**
- Storage functions only handle data persistence
- No business logic embedded in storage layer
- Direct mapping between data structures and storage format

### 🛡️ **Robust Error Handling**
- Explicit error types and handling
- Predictable error responses
- Graceful degradation without side effects

These principles create a **maintainable, testable, and efficient** codebase where every function has a clear purpose and predictable behavior.
