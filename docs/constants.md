# StudyFrog Constants Module Documentation 🧾🎨🐸

Welcome to the documentation for the `constants` module in StudyFrog. This module provides centralized access to all static values, paths, color definitions, UI defaults, and table names used throughout the application.

---

## 📘 Overview
The `Constants` class defines and organizes:
- 📦 Application metadata and paths
- 🎨 Color palettes
- 📐 Font and geometry settings
- 🗃️ Table and namespace identifiers
- 🕓 Date-related constants
- ⚙️ Learning configuration presets

This module ensures consistency across modules and simplifies customization and theme management.

---

## 🧠 Core Class: `Constants`

A static-only class with no instantiation, containing hundreds of constants organized by purpose.

---

## 🖥️ Application Metadata
- `APPLICATION_NAME`: The name of the app (e.g., "🐸 StudyFrog")
- `APPLICATION_VERSION`: Version number (e.g., `0.1`)
- `BASE_ID`: Starting ID for system-generated entries

---

## 📁 Filesystem Paths
- `CWD`, `DATA_PATH`, `DATABASE_PATH`
- `IMPORT_PATH`, `EXPORT_PATH`

---

## 📊 Table Names
Used throughout the ORM and DB layer:
- `ANSWERS`, `FLASHCARDS`, `QUESTIONS`, `NOTES`, `TAGS`, `STACKS`, ...

---

## 🎨 Color Definitions
Color palettes for UI design, based on Material Design:
- Full color dictionaries: `BLUE`, `RED`, `GREEN`, `YELLOW`, `PURPLE`, `PINK`, `ORANGE`, `TEAL`, etc.
- `WHITE`, `BLACK` as hex strings
- Accessible via `Constants.get_colors(as_dict=True|False)`

---

## 🖋️ Font and Typography
- `DEFAULT_FONT_FAMILY`: e.g., Helvetica
- Sizes: `SMALL_FONT_SIZE`, `MEDIUM_FONT_SIZE`, `LARGE_FONT_SIZE`, `VERY_LARGE_FONT_SIZE`
- Weights: `BOLD`, `ITALIC`, `NORMAL`, `UNDERLINE`, `OVERSTRIKE`

---

## 🧭 UI & Namespace Constants
Used for dispatcher-based event routing and UI-specific logic:
- `FLASHCARD_NAMESPACE`, `STACK_NAMESPACE`, `TAG_NAMESPACE`, etc.
- `CREATE_UI_NAMESPACE`, `DASHBOARD_UI_NAMESPACE`, `EDIT_UI_NAMESPACE`, ...

---

## 📅 Date and Time Constants
- `NOW`, `TODAY`, `TOMORROW`, `YESTERDAY`
- `START_OF_WEEK`, `END_OF_WEEK`
- `START_OF_MONTH`, `END_OF_MONTH`
- `START_OF_YEAR`, `END_OF_YEAR`

---

## 🎓 Learning Configurations
- `LEARNING_MODES`: List of learning types
  - e.g., "Default", "Recall", "Spaced Repetition"

---

## ⚖️ Enum-Like Values
- Difficulties: `EASY`, `MEDIUM`, `HARD`
- Priorities: `LOWEST`, `LOW`, `MEDIUM`, `HIGH`, `HIGHEST`
- Statuses: `NEW`, `LEARNING`, `REVIEW`, `COMPLETED`
- Boolean equivalents: `TRUE`, `FALSE`

---

## 🔍 Utility Methods
### `get_base_id()`
Returns a deep copy of `BASE_ID` to avoid mutation.

### `get_colors(as_dict: bool = False)`
Returns all defined UI colors as:
- Dict mapping color names to hex codes (if `as_dict=True`)
- Flat list of hex values (if `False`)

---

## ✅ Best Practices
- Never hardcode color codes, font sizes, or DB names – use `Constants`
- Use provided date fields to ensure consistency in calculations
- Centralize new constant declarations here for traceability

---

## 💡 Future Improvements
- Add themes (light/dark) based on these constants
- Auto-document all `Constants` via introspection
- Environment-sensitive paths for deployment vs. dev
- Integration with user-facing settings editor

---

Keep your app constant – and your constants centralized 🐸🧾