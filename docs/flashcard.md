# StudyFrog Flashcard Module Documentation 🧠📇

Welcome to the documentation for the `flashcard` module in the StudyFrog API. This module defines how **flashcards** are represented, manipulated, persisted, and retrieved within the StudyFrog learning system.

---

## 📘 Overview
Flashcards are central elements of the StudyFrog system, allowing users to practice and review content through spaced repetition and tagging systems. This module includes:

- Immutable and mutable flashcard classes
- Factory and builder patterns for creation
- Converter for DB mapping
- Manager for persistence and access
- ORM model for database integration

---

## 📦 ImmutableFlashcard

### Description
A read-only version of a flashcard. Suitable for presentation and access-only operations.

### Key Attributes
- `front_text`, `back_text`: Main text content
- `front_word_count`, `back_word_count`, `total_word_count`
- `difficulty`, `priority`, `status`: Linked by ID
- `familiarity`: Float value for SR tracking
- `tags`: List of string keys
- `uuid`, `key`, `icon`
- `created_at`, `updated_at`, `last_viewed_at`
- `custom_field_values`: Optional list of additional metadata

### Methods
- `get_custom_field_value(id) → Optional[Any]`
- `to_mutable() → MutableFlashcard`

---

## ✍️ MutableFlashcard

### Description
An editable version of a flashcard with methods to manipulate internal state.

### Extra Methods
- `set_custom_field_value(id, value)`
- `set_difficulty(difficulty_obj)`
- `set_priority(priority_obj)`
- `to_immutable() → ImmutableFlashcard`

---

## 🔁 FlashcardConverter

### Description
Utility class for transforming between `FlashcardModel` and `ImmutableFlashcard` objects.

### Methods
- `model_to_object(model: FlashcardModel) → ImmutableFlashcard`
- `object_to_model(object: ImmutableFlashcard) → FlashcardModel`

Includes robust error logging.

---

## 🏭 FlashcardFactory

### Description
Creates `ImmutableFlashcard` instances with sane defaults and logging.

### Method
- `create_flashcard(...) → ImmutableFlashcard`

Handles icon defaulting, UUID generation, etc.

---

## 🧱 FlashcardBuilder

### Description
Builder class for fluent, chainable creation of flashcard objects.

### Example
```python
flashcard = (
    FlashcardBuilder()
    .front_text("What is the capital of France?")
    .back_text("Paris")
    .familiarity(0.2)
    .build()
)
```

### Method
- `build(as_mutable=False) → ImmutableFlashcard | MutableFlashcard`

All field setters mirror the flashcard attributes and return `self` for chaining.

---

## 🧠 FlashcardManager

### Description
Provides full database management for flashcards. Caches objects to minimize DB load.

### Key Methods
- `get_all_flashcards()`
- `create_flashcard(flashcard)`
- `update_flashcard(flashcard)`
- `delete_flashcard(flashcard)`
- `get_flashcard_by(field, value)` / `get_flashcard_by_id()` / `get_flashcard_by_uuid()`
- `get_flashcard_by_key(key)`
- `search_flashcards(**kwargs)`
- `get_from_flashcards(condition: Callable, limit: Optional[int])`
- `count_flashcards()`

---

## 🧬 FlashcardModel

### Description
ORM data model defining the SQL schema and constraints.

### Table
- Stored under `Constants.FLASHCARDS`

### Fields
- `id`, `uuid`, `key`, `icon`
- `front_text`, `back_text`, `tags`, `custom_field_values`
- `difficulty`, `priority`, `status`, `familiarity`
- `word counts`, `created_at`, `updated_at`, `last_viewed_at`

Backed by the `Field` descriptor system with type safety and DB mapping.

---

## ✅ Best Practices for Contributors
- Use `FlashcardBuilder` or `FlashcardFactory` to create objects.
- Always validate your objects before passing to `FlashcardManager`.
- Use `FlashcardConverter` to bridge between model ↔ object.
- Prefer `get_flashcard_by_*` accessors over raw DB queries.
- Remember to call `count_flashcards()` if using custom key naming logic.

---

## 🚧 Ideas for Expansion
- Add support for scheduling algorithms (e.g., SM-2)
- Implement flashcard templates or rich formatting
- Integrate audio/image support for multimedia flashcards
- Improve familiarity tracking based on performance

---

Let’s make learning smarter – together 💚🐸

