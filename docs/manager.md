# StudyFrog Manager Module Documentation 🧠🗂️

Welcome to the documentation for the `manager` module in the StudyFrog API. This module provides a powerful caching and object management system, designed to optimize database access and ensure consistency across all manager classes.

---

## 📘 Overview
At the heart of this module is the `BaseObjectManager` class, which:
- Acts as the **foundation** for all object managers (e.g., FlashcardManager, TagManager)
- Provides an **in-memory cache system**
- Handles **timestamp-based cache validation**
- Offers a unified interface for **CRUD-like caching operations**

---

## 🏗️ BaseObjectManager

### Description
The `BaseObjectManager` serves as a superclass for all specific object managers. It includes a built-in cache with timestamp validation and a wide range of helper methods for managing key-value pairs in memory.

### Attributes
- `logger`: Dedicated logger for each manager class
- `_cache`: Internal list of dictionaries, each containing a `key` and `value`
- `_timestamp`: Last updated time of the cache
- `_time_limit`: Time in seconds for which the cache remains valid (default: 3600)

---

## 🧰 Core Features

### Initialization
```python
manager = BaseObjectManager()
```
Creates a manager with an empty cache and timestamp set to `datetime.now()`.

---

## 🔄 Cache Control Methods

### `add_to_cache(key, value)`
Adds an item to the cache. Overwrites existing key if necessary.

### `flush_cache(force=False)`
Clears the cache if outdated (timestamp check) or always if `force=True`.

### `clear_cache()`
Immediately clears the cache and resets timestamp.

### `check_timestamp()`
Returns whether the cache should be considered outdated.

---

## 📦 Cache Query & Inspection

### `get_cache_keys()` / `get_cache_values()`
Returns list of all keys/values in the cache.

### `get_key_from_cache(value)` / `get_value_from_cache(key)`
Searches the cache for a matching value or key.

### `is_cache_empty()` / `is_cache_valid()`
Boolean checks for cache state.

### `is_key_in_cache(key)` / `is_value_in_cache(value)`
Checks existence of key or value.

---

## 🛠️ Cache Mutation

### `update_in_cache(key, value)`
Updates an existing cached item by key.
Raises `KeyError` if not found.

### `remove_from_cache(key)`
Removes item from cache by key.

> 🔥 All mutations are logged via the `Logger`.

---

## 🧠 Best Practices for Developers
- Extend `BaseObjectManager` to build custom managers (e.g., for Flashcards, Tags)
- Implement your custom manager classes as **Singletons** to avoid inconsistent cache states
- Avoid direct DB queries when you can use the cache
- Call `flush_cache(force=True)` when data outside of cache may have changed
- Use `update_in_cache()` instead of deleting and re-adding entries

---

## 🧪 Example Usage
```python
manager = BaseObjectManager()
manager.add_to_cache("flashcard_001", {"front": "Q", "back": "A"})
print(manager.get_value_from_cache("flashcard_001"))  # → {"front": "Q", ...}
```

---

## 💡 Ideas for Expansion
- Add expiration per item instead of global cache timeout
- Add event hooks (e.g., `on_add`, `on_remove`)
- Introduce support for async I/O and external cache (e.g., Redis)

---

Your cache. Your control. Study smarter. 🧠⚡🐸