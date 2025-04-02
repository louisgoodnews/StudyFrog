# StudyFrog UIRegistry Module Documentation 🧩🖼️🐸

Welcome to the documentation for the `ui_registry` module in StudyFrog! This module manages a registry of user interface (UI) widget classes. It allows for the registration, lookup, and removal of widgets by name.

---

## 📘 Overview
The `UIRegistry` class provides a global, singleton-like registry to map widget names (as strings) to their associated Tkinter class objects. This is useful for dynamic UI creation, plugin systems, and menu loading.

---

## 🧠 Class: `UIRegistry`

### Description
A centralized class for registering and retrieving UI widgets by name.

### Attributes
- `registry: Dict[str, Type[tkinter.Misc]]` – Internal mapping of widget names to Tkinter widget classes.
- `logger: Logger` – Logger instance used to report registration and access issues.

---

## 🔍 Methods

### `get(name: str) → Optional[Type[tkinter.Misc]]`
Looks up a widget class by name.

- Logs a warning if the widget name is not found.
- Returns `None` if no match is found.

```python
view = UIRegistry.get("DashboardUI")
```

---

### `register(name: str, widget: Type[tkinter.Misc]) → None`
Adds or updates a widget entry in the registry.

- Logs a warning if the widget is being overwritten.
- Logs an info message upon successful registration.
- Logs an error and raises if the operation fails.

```python
UIRegistry.register("DashboardUI", DashboardUI)
```

---

### `unregister(name: str) → None`
Removes a widget from the registry.

- Logs a warning if the widget does not exist.
- Logs an info message on successful removal.
- Logs and raises an error on failure.

```python
UIRegistry.unregister("DashboardUI")
```

---

## ✅ Best Practices
- Use descriptive, unique names for UI components (e.g. "EditorUI", "SettingsView")
- Always register widgets during application bootstrap
- Use `UIRegistry.get()` to support dynamic loading of views
- Handle `None` returns from `.get()` gracefully

---

## 💡 Future Enhancements
- Support for widget metadata (tags, categories)
- Auto-discovery of widgets using reflection
- UI plugin registration via entry points

---

Your dynamic UI manager – connected by name, powered by frogs 🐸🧩