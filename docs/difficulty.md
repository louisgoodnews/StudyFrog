# StudyFrog Difficulty Module Documentation 🎯📊

Welcome to the documentation for the `difficulty` module in the StudyFrog API. This module manages **difficulty levels**, which are used across StudyFrog to define the importance or complexity of an item (e.g., flashcards, questions).

---

## 📘 Overview
A `Difficulty` is defined by a `name`, `emoji`, and a `value` between 0 and 1. This module provides:

- Mutable and immutable object representations
- Conversion between DB model and object
- Creation through a factory
- Full database CRUD support
- ORM mapping with field definitions

---

## 📦 ImmutableDifficulty

### Description
Represents a read-only difficulty entry. Used across the system for safe reference.

### Attributes
- `name`: Difficulty name (e.g., *easy*, *medium*, *hard*)
- `emoji`: Visual representation (⭐, ⭐⭐, ⭐⭐⭐)
- `value`: Float from 0.0 to 1.0
- `id`, `key`, `uuid`, `icon`
- `created_at`, `updated_at`

### Methods
- `to_mutable() → MutableDifficulty`

---

## ✍️ MutableDifficulty

### Description
An editable difficulty instance.

### Methods
- `to_immutable() → ImmutableDifficulty`

---

## 🔁 DifficultyConverter

### Description
Bidirectional converter between `DifficultyModel` and `ImmutableDifficulty`.

### Methods
- `model_to_object(model) → ImmutableDifficulty`
- `object_to_model(object) → DifficultyModel`

Error handling is robust via the `Logger` class.

---

## 🏭 DifficultyFactory

### Description
Factory class for creating `ImmutableDifficulty` objects.

### Method
- `create_difficulty(...) → Optional[ImmutableDifficulty]`

Supports full initialization with sensible defaults and error logging.

---

## 🧠 DifficultyManager

### Description
Singleton-style manager to handle database interaction for difficulties.

### Key Methods
- `count_difficulties()`
- `create_difficulty(difficulty)`
- `delete_difficulty(difficulty)`
- `get_all_difficulties()`
- `get_default_difficulties()` – loads EASY, MEDIUM, HARD if missing
- `get_difficulty_by(field, value)` / `get_difficulty_by_id()` / `get_difficulty_by_uuid()`
- `search_difficulties(**kwargs)`
- `update_difficulty(difficulty)`

Internally uses caching, `Miscellaneous` tools, and consistent key naming like `DIFFICULTY_1`.

---

## 🧬 DifficultyModel

### Description
ORM table representation for `Difficulty`, used in DB operations.

### Table
- Stored in: `Constants.DIFFICULTIES`

### Fields
- `id`, `created_at`, `updated_at`, `emoji`, `icon`, `key`, `name`, `uuid`, `value`

Backed by the `Field` descriptor system for typed, schema-safe DB access.

---

## ✅ Best Practices for Contributors
- Use `DifficultyFactory` to instantiate new objects
- Use `DifficultyManager.create_difficulty()` to insert into DB
- Call `get_default_difficulties()` to ensure standard entries exist
- Avoid manipulating the cache manually
- Use the converter to ensure consistency across model ↔ object layers

---

## 🚀 Example Usage
```python
manager = DifficultyManager()
all_difficulties = manager.get_all_difficulties()

# Create a new difficulty
new_diff = DifficultyFactory.create_difficulty(name="Extreme", emoji="🔥", value=1.2)
manager.create_difficulty(new_diff)
```

---

## 💡 Ideas for Future Expansion
- Dynamic user-specific difficulty scaling
- Difficulty history tracking
- Visualization of difficulty distribution per stack/user
- Integration with scheduling/spaced repetition systems

---

Helping you fine-tune your learning – one ⭐ at a time 🐸💚

