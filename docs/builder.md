# StudyFrog Builder Module Documentation 🏗️🧱🐸

Welcome to the documentation for the `builder` module in StudyFrog. This module defines the `BaseObjectBuilder` class, which serves as the common superclass for all builder-style classes in the application.

---

## 📘 Overview
Builder classes in StudyFrog allow the creation of complex, often immutable objects using a **chainable and expressive interface**. The `BaseObjectBuilder` provides the base structure and enforces the implementation of a `build()` method.

---

## 🧠 Class: `BaseObjectBuilder`

### Description
An **immutable base class** for all builders. It uses a central `configuration` dictionary to collect parameters and settings that will later be used to construct the target object.

### Inherits from
- `ImmutableBaseObject`

### Attributes
- `configuration: Dict[str, Any]` – Stores build-time options and keyword arguments

---

## 🧰 Constructor
```python
builder = BaseObjectBuilder()
```
Initializes the `configuration` dictionary as an empty dict.

---

## 🔧 Methods

### `build() → Any`
Abstract method that must be implemented by subclasses. Raises `NotImplementedError` if not overridden.

Used to generate the final object from the configuration.

```python
def build(self):
    return MyObject(**self.configuration)
```

### `kwargs(**kwargs) → None`
Updates the internal configuration with the supplied keyword arguments.

Example usage:
```python
builder.kwargs(name="Alice", age=25)
```

---

## ✅ Best Practices
- Subclass `BaseObjectBuilder` to create domain-specific builders (e.g. `FlashcardBuilder`, `LearningSessionBuilder`)
- Always implement the `build()` method to generate the target object
- Keep `configuration` internal and only manipulate it through safe setters
- Chain `.kwargs(...)` or define custom setters for improved API fluency

---

## 💡 Future Enhancements
- Type enforcement for configuration values
- Builder introspection / auto-doc generation

---

Build clean. Build safe. Build with frogs. 🏗️🐸

