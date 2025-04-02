# StudyFrog Tag Module Documentation 🔖🏷️

Welcome to the documentation for the `tag` module in the StudyFrog API. Tags allow for flexible categorization and filtering of flashcards, notes, questions, and stacks.

---

## 📘 Overview
Tags are text-based labels assigned to study content for organization, filtering, and search. Each tag has a string `value`, an emoji-style `icon`, and a unique `key` and `uuid`.

This module provides:

- Mutable and immutable tag representations
- Converters between object and model
- Factory for tag creation
- Manager for database operations
- ORM model for persistence

---

## 📦 ImmutableTag

### Description
Read-only representation of a tag, suitable for usage across the application without risk of unintended modification.

### Attributes
- `value`: String label of the tag (e.g., "biology", "revision")
- `icon`: Visual emoji indicator (default = "🔖")
- `id`, `key`, `uuid`
- `created_at`, `updated_at`

### Method
- `to_mutable() → MutableTag`

---

## ✍️ MutableTag

### Description
Writable version of a tag, used during creation and editing.

### Method
- `to_immutable() → ImmutableTag`

---

## 🔁 TagConverter

### Description
Converts between database model `TagModel` and domain object `ImmutableTag`.

### Methods
- `model_to_object(model: TagModel) → Optional[ImmutableTag]`
- `object_to_model(object: ImmutableTag) → Optional[TagModel]`

Robust error handling and logging included.

---

## 🏭 TagFactory

### Description
Creates new `ImmutableTag` instances with optional metadata and default values.

### Method
- `create_tag(...) → Optional[ImmutableTag]`

---

## 🧠 TagManager

### Description
Main interface for managing tags in the database. Inherits from `BaseObjectManager` and handles full lifecycle.

### Key Methods
- `count_tags()`
- `create_tag(tag)`
- `delete_tag(tag)`
- `get_all_tags()`
- `search_tags(**kwargs)`
- `get_from_tags(condition, limit)` – filters tags using Python callable
- `get_tag_by(field, value)` / `get_tag_by_id()` / `get_tag_by_uuid()`
- `update_tag(tag)`

Tags are automatically cached to reduce redundant DB queries.

---

## 🧬 TagModel

### Description
ORM model defining the `tags` table schema. Used for all persistent operations.

### Table
- Stored under: `Constants.TAGS`

### Fields
- `id`, `value`, `icon`, `key`, `uuid`, `created_at`, `updated_at`

---

## ✅ Contributor Best Practices
- Always create tags with `TagFactory`
- Store via `TagManager.create_tag()`
- Avoid manually assigning keys or UUIDs — let the manager handle it
- Use `get_from_tags()` with lambda filters for advanced use cases

---

## 🚀 Example Usage
```python
manager = TagManager()
tag = TagFactory.create_tag(value="exam")
manager.create_tag(tag)
```

---

## 💡 Future Ideas
- Tag color or grouping support
- User-specific favorite tags
- Tag suggestions based on stack/question context
- Tag merging or cleanup utilities

---

Organize your mind – one tag at a time 🧠🔖🐸

