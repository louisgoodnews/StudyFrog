# StudyFrog Unified Module Documentation 🔗📦🐸

Welcome to the documentation for the `unified` module in StudyFrog! This module provides a central hub for managing and routing object-level operations across all core entities in the system. It consists of two powerful singleton classes:

- `UnifiedObjectManager`: Dynamically delegates data access and object lifecycle operations to registered managers.
- `UnifiedObjectService`: Handles event-based dispatch for object creation, update, deletion, and retrieval.

---

## 🧠 UnifiedObjectManager

### Description
Acts as a **singleton facade** for all individual manager instances (e.g., `FlashcardManager`, `TagManager`, etc.).

It supports:
- Dynamic attribute resolution
- Routing logic for `.get_by_key()` and `.get_by_keys()`
- Manager registration and dynamic method dispatch

### Key Attributes
- `managers`: Dictionary of registered manager instances
- `logger`: Internal logger

### Key Methods

#### `register_manager(name: str, manager: Type[Any])`
Registers a new manager with the given name. This method instantiates the manager class.

#### `get_by_key(key: str) → Optional[Any]`
Determines the target manager from the object's key prefix and forwards the call to its `.get_by_key()` method.

#### `get_by_keys(keys: List[str]) → List[Optional[Any]]`
Runs `.get_by_key()` for each item in the input list.

#### `run(manager: str, method: str, **kwargs)`
Executes a named method on the specified manager with the given arguments.

---

## 📡 UnifiedObjectService

### Description
A **singleton service layer** responsible for event-based coordination of operations across all supported entities.

### Core Idea
Rather than calling manager methods directly, StudyFrog components dispatch events like:
```python
service.on_request_flashcard_create(flashcard)
```
Which internally calls:
```python
manager.create_flashcard(flashcard=flashcard)
```

### Features
- Event-based structure for decoupled system design
- One entry point for create/update/delete/load/lookup operations
- Supports all objects: Flashcards, Notes, Tags, etc.
- Safe execution with full error handling

### Common Event Prefixes
- `on_request_*_create`
- `on_request_*_delete`
- `on_request_*_load`
- `on_request_*_lookup`
- `on_request_*_update`
- `on_request_get_all_*`

This naming scheme provides a predictable, maintainable API for service-based architecture.

### Example
```python
service = UnifiedObjectService(unified_manager=UnifiedObjectManager())
flashcard = ImmutableFlashcard(...)
service.on_request_flashcard_create(flashcard)
```

---

## ✅ Best Practices
- Instantiate managers using `register_manager()` in your startup routine
- Use `UnifiedObjectManager().run(...)` for dynamic, string-based routing
- Use `UnifiedObjectService()` as your primary interface in frontends or plugins
- Treat both classes as **singletons** – never instantiate directly

---

## 💡 Future Extensions
- Middleware hooks (e.g., validation, permission checks)
- Event queue support for background processing
- Auto-wiring based on reflection
- CLI or GraphQL interface to expose unified operations

---

One interface to rule them all – unify your object world 🧠🌐🐸

