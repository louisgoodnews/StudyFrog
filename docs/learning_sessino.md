# StudyFrog Learning Session Module Documentation 📚🧪

Welcome to the documentation for the `learning_session` module in StudyFrog. This module manages the structure and persistence of **learning sessions** and **learning session items**, which track interactions with study content like flashcards, notes, or questions.

---

## 📘 Overview
This module defines:

- Mutable & immutable data structures for sessions and items
- Builder and factory patterns for structured creation
- Converters for object ↔ model mapping
- Managers for full database lifecycle
- ORM-backed models for persistent storage

---

## 🧠 LearningSession & LearningSessionItem Objects

### ImmutableLearningSession / MutableLearningSession
Encapsulate one study session.

#### Key Fields
- `children`: Nested session keys
- `contents`: List of studied object keys
- `stacks`: Related stack keys
- `start`, `end`, `duration`: Time tracking
- `result`, `status`: Outcome & status (e.g. success, paused)
- `filters`, `settings`, `custom_field_values`

#### Methods (selected)
- `get_custom_field_value(id)` / `set_custom_field_value(id, value)`
- `get_setting(key)` / `set_setting(key, value)`
- `calculate_duration()`
- `add_child()`
- `to_mutable()` / `to_immutable()`

---

### ImmutableLearningSessionItem / MutableLearningSessionItem
Represents an atomic action (e.g. answering a flashcard).

#### Key Fields
- `reference`: Reference to the studied object
- `start`, `end`, `duration`
- `custom_field_values`

#### Methods
- `to_mutable()` / `to_immutable()`

---

## 🏗️ Builder & Factory

### LearningSessionBuilder / LearningSessionItemBuilder
Used for fluent, chainable object construction.
```python
builder = LearningSessionBuilder()
session = builder.contents(["flashcard_1", "note_3"]).start(datetime.now()).build()
```

### LearningSessionFactory / LearningSessionItemFactory
Used to create valid `Immutable...` objects with full error logging.

---

## 🔁 Converters

### LearningSessionConverter / LearningSessionItemConverter
Map between domain objects and database models.
- `model_to_object()`
- `object_to_model()`

---

## 🧬 Model Definitions

### LearningSessionModel / LearningSessionItemModel
ORM schema defining storage in `Constants.LEARNING_SESSIONS` and `Constants.LEARNING_SESSION_ITEMS`

#### Field Types
- JSON: `children`, `contents`, `filters`, `settings`, `custom_field_values`
- Time: `start`, `end`, `created_at`, `updated_at`
- Numeric: `status`, `result`, `duration`
- Reference: `result` links to `LEARNING_SESSION_ITEMS(id)`

---

## 🧠 Manager API

### LearningSessionManager / LearningSessionItemManager
Singleton-style database handlers for caching and I/O.

#### Core Methods
- `create_learning_session(...)`
- `get_learning_session_by(field, value)` / `by_id()` / `by_key()` / `by_uuid()`
- `get_all_learning_sessions()`
- `update_learning_session(...)`
- `delete_learning_session(...)`
- `search_learning_sessions(**kwargs)`

All methods use cache internally and fallback to SQLite when needed.

---

## ✅ Best Practices
- Use Builder or Factory to instantiate sessions
- Always prefer `Manager.create_*` over raw DB interaction
- Use `add_child()` to establish parent-child sessions
- Track `duration` with `calculate_duration()` before saving
- Use `custom_field_values` for flexible, schema-free extensions

---

## 🚀 Example
```python
session = LearningSessionBuilder()
    .contents(["card_001"])
    .start(datetime.now())
    .status(1)
    .build()
LearningSessionManager().create_learning_session(session)
```

---

## 💡 Future Ideas
- Advanced analytics & charting (avg. session duration, item-level stats)
- Adaptive session difficulty & content suggestions
- Export to CSV/JSON for user summaries
- Integration with spaced repetition algorithms

---

Your learning process, tracked and optimized – one session at a time 🧠📈🐸

