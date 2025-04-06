# 🧠 StudyFrog – The Intelligent Learning Assistant

**StudyFrog** is a modular, extendable learning platform designed to help students and professionals organize, test, and visualize their knowledge. Built with Python and Tkinter, it combines modern UI principles with powerful data-handling, monitoring, and semantic similarity features.

## ✨ Key Features

- 📝 **Flexible Input Fields**: Modular `BaseField` system (e.g. text, numeric, date) with UI components built on Tkinter.
- 🧠 **Semantic Recall Matching**: Uses `sentence-transformers` to compare user input with expected answers for open-text recall.
- 📊 **Smart Monitoring**: Tracks user interactions, recall accuracy, difficulty & priority of content.
- 🗕️ **Calendar-Integrated Date Fields**: Intuitive `DateSelectField` with format validation and visual date picker.
- 🧪 **Fully Testable Architecture**: Separation of concerns and injectable logic ensure full test coverage and debuggability.
- 🧱 **Builder Pattern for Fields**: The `FieldBuilder` provides fluent, reusable and safe construction of field objects.
- ⚙️ **Pluggable UI Design**: Supports dynamic stack/flashcard/question creation.

## 🛡️ Technologies Used

- Python 3.11+
- Tkinter + ttk (custom widgets)
- SQLite (backend storage)
- `sentence-transformers` (semantic matching)
- spaCy (optional NLP features)
- `Logger`, `Dispatcher`, `Event` system (custom utils)

## 🚧 Roadmap

- [x] BaseField System
- [x] FieldBuilder with dynamic mapping
- [x] Semantic comparison engine
- [ ] Error handling service (global listener)
- [ ] GUI-based performance dashboard
- [ ] Export/Import feature (JSON & CSV)
- [ ] Persistent user preferences

## 🤝 Contributions

This project is currently being developed by **lodego** as a self-driven, showcase-worthy initiative to demonstrate professional software architecture, UI/UX skills, and a passion for ed-tech and psychological learning principles.

If you're interested in collaborating, feel free to get in touch or fork the project to explore further!

