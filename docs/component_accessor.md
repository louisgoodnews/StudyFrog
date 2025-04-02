# StudyFrog ComponentAccessor Module Documentation 🧩🗂️🐸

Welcome to the documentation for the `component_accessor` module in StudyFrog. This module offers a centralized, structured interface to access **manager instances** for all major components of the application.

---

## 📘 Overview
The `ComponentAccessor` class is a **utility hub** that provides access to singleton-style manager instances such as:
- FlashcardManager, StackManager, TagManager, etc.
- Support managers like `Dispatcher` and `Logger`
- A dynamically registered `UnifiedObjectManager`

It ensures standardized access to components across backend and plugin layers.

---

## 🧠 ComponentAccessor

### Description
Exposes static class attributes and class methods to retrieve the correct manager instance for a given component.

### Responsibilities
- Maintain singleton access to core components
- Provide utility methods for flexible component lookup
- Instantiate and register managers in the `UnifiedObjectManager`

---

## 🔑 Key Attributes
Each attribute is statically initialized and reused throughout the application:

- `answer_manager`, `association_manager`, `change_history_manager`, ...
- `dispatcher`: Event dispatcher instance
- `logger`: Logger bound to the accessor
- `unified_manager`: Instance of `UnifiedObjectManager` with all managers registered

---

## 🔍 Component Access Methods
All `get_*_manager()` methods return fresh instances. These include:

```python
get_flashcard_manager()
get_stack_manager()
get_tag_manager()
get_user_manager()
...
```

Additional utilities:

### `get_component(component_name: str) → Any`
Dynamically returns a component manager based on string name (e.g., "flashcard").

### `get_logger(name: str) → Logger`
Returns a logger instance with the given name.

---

## 🧭 Unified Manager Bootstrapping
The `get_unified_manager()` method:
- Creates a fresh `UnifiedObjectManager`
- Registers all core manager types via `.register_manager()`

This enables full dynamic routing support using keys or manager strings.

```python
manager = ComponentAccessor.get_unified_manager()
obj = manager.get_by_key("FLASHCARD_1")
```

---

## ✅ Best Practices
- Use this accessor class to avoid manually instantiating managers
- Prefer `get_component("flashcard")` for flexibility in dynamic contexts
- Use `get_unified_manager()` early in your service initialization
- Catch and log all access errors to assist with debugging

---

## 💡 Future Improvements
- Caching or lazy loading for managers
- Auto-registration of new managers via reflection
- Integration with plugin systems
- Dependency injection support for testing contexts

---

The hub where all StudyFrog components come together 🧠🔌🐸