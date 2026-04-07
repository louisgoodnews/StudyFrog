# StudyFrog 🐸

A comprehensive flashcard study application built with Python and CustomTkinter, featuring event-driven architecture, JSON-based storage, and a modern dark-themed interface.

## Features

- **📚 Flashcard Management**: Create, edit, and organize flashcards with rich metadata
- **🗂️ Stack Organization**: Group flashcards into thematic collections  
- **🎯 Rehearsal System**: Practice sessions with multiple question types
- **💾 Data Persistence**: JSON-based storage with backup and restore
- **🔗 Event-Driven Architecture**: Modular, maintainable codebase
- **🎨 Modern GUI**: CustomTkinter-based interface with dark/light themes
- **🌍 World Capitals**: Pre-loaded with 100 world capital flashcards

## Quick Start

### Prerequisites

- Python 3.11+
- pip (Python package manager)

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd StudyFrog

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python -m studyfrog.main
```

## Documentation

📖 **Comprehensive documentation is available in the `docs/` directory:**

- **[CONTRIBUTOR_GUIDE.md](docs/CONTRIBUTOR_GUIDE.md)** - Complete guide for contributors
- **[ARCHITECTURE.md](docs/ARCHITECTURE.md)** - System design and patterns
- **[CORE_MODULES.md](docs/CORE_MODULES.md)** - Application lifecycle and bootstrap
- **[MODEL_LAYER.md](docs/MODEL_LAYER.md)** - Data structures and business logic
- **[GUI_LAYER.md](docs/GUI_LAYER.md)** - User interface components
- **[UTILITY_MODULES.md](docs/UTILITY_MODULES.md)** - Storage, events, and utilities
- **[CONSTANTS_AND_CONFIG.md](docs/CONSTANTS_AND_CONFIG.md)** - Configuration and constants
- **[DEVELOPMENT_GUIDE.md](docs/DEVELOPMENT_GUIDE.md)** - Setup, workflow, and deployment

### Quick Reference

#### Creating a Flashcard

```python
from studyfrog.models.factory import get_flashcard_model
from studyfrog.utils.storage import add_entry
from studyfrog.constants.files import FLASHCARDS_DB_JSON

# Create flashcard
flashcard = get_flashcard_model(
    front="What is the capital of France?",
    back="Paris",
    difficulty="Easy"
)

# Save to storage
add_entry(FLASHCARDS_DB_JSON, flashcard)
```

#### Handling Events

```python
from studyfrog.utils.dispatcher import dispatch, subscribe
from studyfrog.constants.events import FLASHCARD_CREATED

# Subscribe to events
def on_flashcard_created(event_data):
    flashcard = event_data.get('flashcard')
    print(f"New flashcard: {flashcard.front}")

subscribe(FLASHCARD_CREATED, on_flashcard_created)

# Dispatch events
dispatch(FLASHCARD_CREATED, {'flashcard': flashcard})
```

## Project Structure

```
StudyFrog/
├── src/studyfrog/           # Source code
│   ├── main.py             # Application entry point
│   ├── core/               # Core application logic
│   ├── models/             # Data models
│   ├── gui/                # User interface
│   ├── utils/              # Utility functions
│   ├── constants/          # Configuration constants
│   └── common/            # Shared utilities
├── tests/                  # Test suite
├── docs/                   # Documentation 📖
├── .local/                 # Local data (gitignored)
├── requirements.txt         # Dependencies
└── README.md             # This file
```

## Development

### Setting Up Development Environment

1. **Clone and setup**:
   ```bash
   git clone <repository-url>
   cd StudyFrog
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Run tests**:
   ```bash
   pytest tests/ -v
   ```

3. **Code formatting**:
   ```bash
   black src/studyfrog/
   isort src/studyfrog/
   ```

### Contributing

We welcome contributions! 🎉

1. Read the [Contributor Guide](docs/CONTRIBUTOR_GUIDE.md)
2. Follow the [Development Guide](docs/DEVELOPMENT_GUIDE.md)
3. Write tests for new features
4. Update documentation
5. Submit a pull request

## Architecture Overview

StudyFrog uses an **event-driven architecture** with clear separation of concerns:

```
main.py → core.application → core.bootstrap → GUI → Event System
    ↓           ↓                ↓           ↓
Lifecycle   System Init     User Interface  Component Communication
```

**Key Concepts:**

- **Event-Driven**: Components communicate through events
- **Model-Factory**: Consistent model creation with validation
- **JSON Storage**: Human-readable, version-controllable data format
- **Modular GUI**: Separate views, forms, and logic

## Data Storage

All data is stored in `.local/data/` using JSON format:

- `flashcards.json` - Flashcard data
- `stacks.json` - Stack organization  
- `questions.json` - Question data
- `answers.json` - Answer data
- `rehearsal_runs.json` - Rehearsal sessions
- And more...

Each file follows a consistent structure with metadata, timestamps, and UUIDs.

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=studyfrog --cov-report=html

# Run specific test file
pytest tests/test_models.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **CustomTkinter** - For the modern GUI framework
- **Python Community** - For excellent libraries and tools
- **Contributors** - Everyone who has helped improve StudyFrog

---

**Happy studying! 🐸📚**

*For detailed documentation, see the [docs/](docs/) directory.*
