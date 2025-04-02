# StudyFrog Change History Module Documentation 🕒🧾🐸

Welcome to the documentation for the `change_history` module in StudyFrog. This module provides a detailed infrastructure for tracking and managing all changes made to objects across the StudyFrog ecosystem.

---

## 📘 Overview
This module enables the creation, tracking, and retrieval of change histories and their individual change items:

- `ChangeHistory`: Represents a full change event (e.g., user updates a flashcard)
- `ChangeHistoryItem`: Represents a single field change within that event (e.g., "front" field updated)
- Designed for audit logging, undo functionality, and user insights
- Fully supports mutability, ORM integration, factory/converter patterns, and singleton-style managers

---

## 🧱 ImmutableChangeHistory / MutableChangeHistory

### Purpose
Holds structured metadata about a full change event, including:
- `source`: Dictionary describing the origin and context of the change
- `created_at`, `updated_at`, `uuid`, `key`, `id`, `icon`

### Methods
- `.to_mutable()` / `.to_immutable()` – Switch between forms

### Use Cases
- Recording a set of related updates (e.g., batch flashcard edits)
- Logging external data syncs

---

## 🔘 ImmutableChangeHistoryItem / MutableChangeHistoryItem

### Purpose
Represents a single atomic change within a change history.
- `from_`: Previous value
- `to`: New value
- Same metadata as change history (timestamps, uuid, etc.)

### Methods
- `.to_mutable()` / `.to_immutable()`

---

## 🏭 Factory Classes

### ChangeHistoryFactory / ChangeHistoryItemFactory
- Create `ImmutableChangeHistory` or `ImmutableChangeHistoryItem` objects with error-safe defaults

### Example
```python
ChangeHistoryFactory.create_change_history(source={"action": "edit_flashcard"})
```

---

## 🔁 Converter Classes

### ChangeHistoryConverter / ChangeHistoryItemConverter
- Convert from object → ORM model and back
- Used by managers and database layers
- Includes logging for error tracking

---

## 🧠 Managers (Singletons)

### ChangeHistoryManager / ChangeHistoryItemManager
- Inherit from `BaseObjectManager`
- Implemented as **Singletons** to ensure shared cache state
- Provide full CRUD APIs:
  - `create_change_history[_item]`
  - `update_change_history[_item]`
  - `delete_change_history[_item]`
  - `get_all_change_history[_items]`
  - `get_change_history_by_id/uuid/field`
  - `search_change_histories`
  - `count_change_history_items`

### Example
```python
manager = ChangeHistoryManager()
manager.create_change_history_item(...)
```

---

## 🧬 ORM Models

### ChangeHistoryModel / ChangeHistoryItemModel
Define database table structures via StudyFrog’s `Field` and `ImmutableBaseModel` system.

#### Key Fields
- `source`, `from_`, `to`: Core data change fields
- `key`, `uuid`, `created_at`, `updated_at`, `icon`
- Stored in `Constants.CHANGE_HISTORIES` and `Constants.CHANGE_HISTORY_ITEMS`

---

## ✅ Best Practices
- Use factories to create change objects to avoid manual errors
- Call `.to_dict(exclude=["_logger"])` before persisting or converting
- Use manager `.create_*` methods for full tracking and DB-safe caching
- Avoid duplicate keys – use `Miscellaneous.get_uuid()` and `get_current_datetime()`
- Use history items for field-level audit logging

---

## 💡 Future Features
- Automatic history generation via decorators or mixins
- UI timeline visualizations per object
- Rollback/undo support via history replay
- Change diffs and summaries for user feedback

---

Track the past. Understand the present. Improve the future. 🕒📘🐸

