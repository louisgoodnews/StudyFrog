# StudyFrog Logger Module Documentation 📢🧾🐸

Welcome to the documentation for the `logger` module in StudyFrog. This module provides a rich, colorized logging system tailored for both synchronous and asynchronous function monitoring.

---

## 📘 Overview
This module defines the `Logger` class, which offers:
- Colorized console output based on log level
- Support for `Level` types (CRITICAL, DEBUG, ERROR, INFO, SILENT, WARNING)
- Structured logging for functions and event tracking
- Dynamic invocation of sync and async functions with timing support

---

## 🧠 Logger Class

### Constructor
```python
Logger(name: str, colorisation: Dict[str, Any] | None = default, level: Level | None = INFO)
```

### Attributes
- `name`: Identifier for the logger instance
- `level`: Current log level (default: INFO)
- `colorisation`: ANSI color codes for terminal output (customizable)

---

## 🔧 Core Logging Methods

### `log(message: Any, level=Level.INFO, *args, **kwargs)`
Generic logger with dynamic formatting and level-based colorisation.

### Convenience Wrappers:
- `.info(message)`
- `.debug(message)`
- `.error(message)`
- `.critical(message)`
- `.warning(message)`
- `.silent(message)`

Each wrapper routes through `.log()` with the respective `Level`.

---

## ⏱️ Function Tracking

### `callable(function, level=Level.INFO, *args, **kwargs)`
Logs the start and end of a synchronous or asynchronous function call, including:
- Arguments and keyword arguments
- Return value
- Execution duration
- Exception details (if any)

Uses `asyncio.run()` to safely execute async functions.

---

## 🏷️ Level Control

### `.level`
Get or set the logging level. Only messages at or above this level will be displayed.

### `.name`
Get or set the logger's name.

---

## 🎨 Color Scheme
Uses ANSI escape sequences for vibrant terminal output:
- CRITICAL → 🔴 Red
- DEBUG → 🔵 Blue
- ERROR → 🟡 Yellow
- INFO → 🟢 Green
- SILENT → ⚪ Grey
- WARNING → 🟣 Magenta

The mapping can be overridden by providing a custom `colorisation` dict.

---

## 🏭 Logger Factory

### `Logger.get_logger(name: str, colorisation = default, level: Level = INFO)`
Returns a ready-to-use logger instance. Useful for consistent formatting across modules.

---

## ✅ Best Practices
- Use `.get_logger()` instead of creating loggers manually
- Prefer `.callable()` when monitoring function behavior
- Use `.level` to filter verbosity dynamically
- Consider integrating log output into file-based or web-based diagnostics

---

## 💡 Future Enhancements
- File output or remote logging support
- Timestamps with timezone awareness
- Log rotation and archival
- Structured JSON or CSV log export

---

Make your code speak with color and clarity 📢🌈🐸

