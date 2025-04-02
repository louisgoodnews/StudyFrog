# StudyFrog Object Module Documentation 🧱🐸

Welcome to the documentation for the `object` module. This module forms the backbone of StudyFrog’s data model system, providing **base classes for mutable and immutable objects** used throughout the application.

---

## 📘 Overview
This module defines two key classes:
- `MutableBaseObject`: Used as a flexible base class for all modifiable domain objects.
- `ImmutableBaseObject`: Inherits from `MutableBaseObject` but overrides setters and deleters to prevent post-initialization changes.

Both classes integrate with the StudyFrog `Logger` system and offer convenience methods for attribute access, debugging, comparison, and dictionary conversion.

---

## 🧰 MutableBaseObject

### Description
Provides a flexible object base with dictionary-style attribute access and built-in logging. Ideal for all data objects that are meant to be changed dynamically.

### Key Features
- Dynamic attribute management via `__getattr__`, `__getitem__`, `__setattr__`, `__setitem__`
- Safe attribute deletion with logging
- Equality checks and filtered comparison via `compare_to()`
- Safe getters/setters: `get()`, `set()`
- Attribute presence checks: `contains_key()`, `contains_value()`
- Custom logging per object type using `Logger.get_logger()`
- Conversion to dictionary with exclusions via `to_dict()`

### Example
```python
obj = MutableBaseObject(name="Test", value=42)
print(obj.name)              # → Test
print(obj["value"])         # → 42
obj.set("new_attr", 100)
```

---

## 🧊 ImmutableBaseObject

### Description
A read-only version of `MutableBaseObject`. Prevents changes after initialization. Used when data integrity is critical.

### Overrides & Protections
- Prevents setting attributes via `__setattr__` / `__setitem__`
- Prevents deleting attributes via `__delattr__` / `delete()`
- Immutable nature is emphasized via modified `__repr__()` output
- Allows new attributes during init, but blocks post-creation changes

### Example
```python
obj = ImmutableBaseObject(id=1, label="Frozen")
obj.label = "Modified"   # ❌ Raises AttributeError
```

---

## 🔍 Comparison & Logging

### Methods
- `compare_to(keys, other)` – checks equality of specific keys between two objects
- `logger.warning(...)` – used internally to alert about missing attributes or invalid operations

---

## ✅ Best Practices
- Use `MutableBaseObject` for all editable models (e.g., builders, draft objects)
- Use `ImmutableBaseObject` for finalized data objects (e.g., loaded from DB or used in UI)
- Prefer `get()`, `set()`, `contains_*()` over direct dictionary access for robustness
- Use `to_dict()` for debugging, serialization, or API output

---

## 💡 Future Extensions
- Attribute-level locking (per field)
- Versioning / change tracking built-in
- Automatic schema validation for dynamic attributes

---

Consistency starts with the right foundation – and this module is it 🧱💚🐸

