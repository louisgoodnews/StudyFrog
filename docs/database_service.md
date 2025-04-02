# StudyFrog DatabaseService Module Documentation 💾⚙️🐸

Welcome to the documentation for the `database_service` module in StudyFrog! This module provides an asynchronous, high-level API for executing SQL queries against a SQLite database using `aiosqlite`. All operations are wrapped with detailed error handling and integrated logging.

---

## 📘 Overview
The `DatabaseService` class exposes **static methods** for performing database CRUD operations with:
- SQL validation (e.g. `INSERT`, `SELECT`, etc.)
- Automatic transaction commits
- Full exception logging via StudyFrog’s `Logger`
- Structured return types for easy integration

---

## 🧠 Class: `DatabaseService`

### Description
This class exposes a collection of `@classmethod`s that allow asynchronous interaction with the database.

---

## 📥 `create()`
Inserts a new row using a provided SQL `INSERT` statement.

### Parameters
- `database: str`: Path to DB file
- `sql: str`: SQL statement (must start with `INSERT`)
- `parameters: Tuple`: Bound parameters

### Returns
- `Optional[int]`: ID of inserted row, or `None` if error

---

## ❌ `delete()`
Deletes rows via `DELETE` statement.

### Returns
- `bool`: `True` if rows were deleted, `False` otherwise

---

## ⚙️ `execute()`
Executes any SQL query (e.g., DDL or general-purpose commands).

### Returns
- `Any`: Result of query (typically `list[tuple]`), or `None` on error

---

## 📚 `read_all()`
Performs a `SELECT` query and returns all results as dictionaries.

### Returns
- `List[Dict[str, Any]]`: List of rows as dicts

---

## 🔍 `read_one()`
Performs a `SELECT` and returns one row as a dictionary.

### Returns
- `Dict[str, Any]`: Single row or empty dict

---

## ✏️ `update()`
Performs an `UPDATE` SQL query.

### Returns
- `bool`: `True` if any rows were updated, `False` otherwise

---

## ✅ Best Practices
- Validate all input SQL using `startswith()` guards (as implemented)
- Use `read_all()` and `read_one()` for ORM-style row handling
- Always check return values for `None`, `False`, or `{}` to detect errors
- Avoid raw SQL string concatenation – always use parameterized queries

---

## 💡 Future Enhancements
- Connection pooling or persistent DB sessions
- Retry/backoff mechanisms
- Support for migrations and schema diffing
- Performance logging (e.g., query timing)

---

Async-safe. Log-rich. Developer-friendly. StudyFrog’s database layer 💾🐸

