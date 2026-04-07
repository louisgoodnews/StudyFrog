# Development Guide

## Overview

This guide provides comprehensive information for developers working on StudyFrog, including setup procedures, development workflows, testing strategies, and deployment instructions.

## Table of Contents

1. [Development Environment Setup](#development-environment-setup)
2. [Project Structure](#project-structure)
3. [Development Workflow](#development-workflow)
4. [Testing Strategy](#testing-strategy)
5. [Debugging Guide](#debugging-guide)
6. [Performance Optimization](#performance-optimization)
7. [Deployment Guide](#deployment-guide)

---

## Development Environment Setup

### Prerequisites

- **Python 3.11+**: Required for modern type hints and features
- **Git**: Version control
- **pip**: Package manager
- **VS Code** (recommended): With Python extensions

### Initial Setup

```bash
# 1. Clone the repository
git clone <repository-url>
cd StudyFrog

# 2. Create virtual environment
python -m venv .venv

# 3. Activate virtual environment
# On Unix/macOS:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Install development dependencies (if available)
pip install -r requirements-dev.txt

# 6. Set up pre-commit hooks (if configured)
pre-commit install
```

### IDE Configuration

#### VS Code Setup

```json
// .vscode/settings.json
{
    "python.defaultInterpreterPath": "./.venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": ["tests"],
    "python.testing.unittestEnabled": false,
    "files.exclude": {
        "**/__pycache__": true,
        "**/*.pyc": true,
        ".pytest_cache": true,
        ".venv": true
    }
}
```

#### Recommended Extensions

- **Python**: Microsoft Python extension
- **Pylance**: Python language server
- **Black Formatter**: Code formatting
- **Python Docstring Generator**: Documentation
- **GitLens**: Git integration
- **Thunder Client**: API testing (if needed)

### Environment Variables

```bash
# Development environment variables
export STUDYFROG_ENV=development
export STUDYFROG_DEBUG=true
export STUDYFROG_LOG_LEVEL=DEBUG
export STUDYFROG_DATA_DIR=./dev_data
```

---

## Project Structure

### Directory Layout

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
├── docs/                   # Documentation
├── .local/                 # Local data (gitignored)
├── .venv/                 # Virtual environment (gitignored)
├── requirements.txt         # Production dependencies
├── requirements-dev.txt     # Development dependencies
├── pyproject.toml         # Project configuration
├── setup.cfg              # Setup configuration
├── Makefile               # Build commands
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

### Code Organization

#### Module Responsibilities

- **main.py**: Application entry point and lifecycle
- **core/**: Application bootstrap and core functionality
- **models/**: Data structures and business logic
- **gui/**: User interface components
- **utils/**: Utility functions and services
- **constants/**: Configuration and constants

#### Import Patterns

```python
# Standard library imports
import os
import sys
from pathlib import Path
from typing import Optional, Dict, List

# Third-party imports
import customtkinter as ctk
import pytest

# Local imports
from studyfrog.core.application import start_application
from studyfrog.models.factory import get_flashcard_model
from studyfrog.utils.storage import add_entry
from studyfrog.constants.events import FLASHCARD_CREATED
```

---

## Development Workflow

### Git Workflow

#### Branch Strategy

```bash
# Main branches
main          # Production-ready code
develop        # Integration branch

# Feature branches
feature/feature-name
bugfix/bug-description
hotfix/critical-fix
```

#### Commit Guidelines

```bash
# Commit message format
<type>(<scope>): <description>

[optional body]

[optional footer]

# Examples
feat(gui): Add flashcard creation dialog
fix(storage): Handle file locking errors
docs(readme): Update installation instructions
test(models): Add flashcard validation tests
```

**Commit Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Code formatting
- `refactor`: Code refactoring
- `test`: Test additions
- `chore`: Maintenance tasks

#### Development Process

```bash
# 1. Create feature branch
git checkout -b feature/new-feature

# 2. Make changes
# ... develop ...

# 3. Run tests
pytest

# 4. Commit changes
git add .
git commit -m "feat(feature): Implement new feature"

# 5. Push to remote
git push origin feature/new-feature

# 6. Create pull request
# Through GitHub/GitLab interface
```

### Code Quality

#### Linting and Formatting

```bash
# Run linter
pylint src/studyfrog/

# Format code
black src/studyfrog/
isort src/studyfrog/

# Run both
make lint
make format
```

#### Type Checking

```bash
# Run type checker
mypy src/studyfrog/

# Check specific module
mypy src/studyfrog/models/models.py
```

#### Pre-commit Hooks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 22.3.0
    hooks:
      - id: black
        language_version: python3.11

  - repo: https://github.com/pycqa/isort
    rev: 5.10.1
    hooks:
      - id: isort

  - repo: https://github.com/pycqa/pylint
    rev: v2.13.9
    hooks:
      - id: pylint
```

### Development Commands

#### Makefile Commands

```makefile
# Makefile
.PHONY: help install test lint format clean run

help:           ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install:         ## Install dependencies
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

test:            ## Run tests
	pytest tests/ -v

lint:            ## Run linting
	pylint src/studyfrog/
	mypy src/studyfrog/

format:          ## Format code
	black src/studyfrog/
	isort src/studyfrog/

clean:           ## Clean temporary files
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache
	rm -rf build/
	rm -rf dist/

run:             ## Run application
	python -m studyfrog.main
```

---

## Testing Strategy

### Test Organization

```
tests/
├── conftest.py              # Pytest configuration
├── test_models.py           # Model tests
├── test_storage.py          # Storage tests
├── test_dispatcher.py       # Event system tests
├── test_gui.py            # GUI tests
├── test_integration.py     # Integration tests
└── fixtures/              # Test data
    ├── sample_flashcards.json
    ├── sample_stacks.json
    └── test_config.json
```

### Test Types

#### Unit Tests

```python
# tests/test_models.py
import pytest
from studyfrog.models.factory import get_flashcard_model

def test_flashcard_creation():
    """Test flashcard model creation."""
    flashcard = get_flashcard_model(
        front="What is 2+2?",
        back="4"
    )
    
    assert flashcard.front == "What is 2+2?"
    assert flashcard.back == "4"
    assert flashcard.type_ == "FLASHCARD"
    assert flashcard.is_valid()

def test_flashcard_validation():
    """Test flashcard validation."""
    # Valid flashcard
    flashcard = get_flashcard_model(front="Q", back="A")
    assert flashcard.is_valid()
    
    # Invalid flashcard (empty front)
    invalid_flashcard = get_flashcard_model(front="", back="A")
    assert not invalid_flashcard.is_valid()
```

#### Integration Tests

```python
# tests/test_integration.py
def test_flashcard_crud_workflow():
    """Test complete flashcard CRUD workflow."""
    # Create
    flashcard = get_flashcard_model(front="Q", back="A")
    success = add_entry(FLASHCARDS_DB_JSON, flashcard)
    assert success
    
    # Read
    retrieved = get_entry(FLASHCARDS_DB_JSON, flashcard.key)
    assert retrieved is not None
    assert retrieved['front'] == "Q"
    
    # Update
    flashcard.front = "Updated Q"
    success = update_entry(FLASHCARDS_DB_JSON, flashcard)
    assert success
    
    # Delete
    success = delete_entry(FLASHCARDS_DB_JSON, flashcard.key)
    assert success
```

#### GUI Tests

```python
# tests/test_gui.py
import pytest
from unittest.mock import Mock, patch
from studyfrog.gui.views.dashboard_view import get_dashboard_view

def test_dashboard_view_creation():
    """Test dashboard view creation."""
    with patch('studyfrog.gui.gui.get_center_frame') as mock_frame:
        view = get_dashboard_view()
        assert view is not None
        mock_frame.assert_called()

def test_dashboard_navigation():
    """Test dashboard navigation events."""
    with patch('studyfrog.utils.dispatcher.dispatch') as mock_dispatch:
        # Simulate button click
        dashboard = get_dashboard_view()
        dashboard.on_create_button_click()
        
        # Verify event was dispatched
        mock_dispatch.assert_called_with('GET_CREATE_VIEW', {})
```

### Test Configuration

#### Pytest Configuration

```python
# tests/conftest.py
import pytest
import tempfile
from pathlib import Path

@pytest.fixture
def temp_data_dir():
    """Create temporary data directory for tests."""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield Path(temp_dir)

@pytest.fixture
def sample_flashcard():
    """Sample flashcard for testing."""
    return get_flashcard_model(
        front="Test Question",
        back="Test Answer",
        difficulty="Easy"
    )

@pytest.fixture
def mock_event_dispatcher():
    """Mock event dispatcher for testing."""
    with patch('studyfrog.utils.dispatcher.dispatch') as mock:
        yield mock
```

#### Test Database Setup

```python
# tests/conftest.py (continued)
@pytest.fixture(autouse=True)
def setup_test_database(temp_data_dir, monkeypatch):
    """Set up test database for all tests."""
    # Override data directory
    monkeypatch.setattr('studyfrog.constants.files.DATA_DIR', temp_data_dir)
    
    # Create test database files
    from studyfrog.utils.files import ensure_file
    from studyfrog.constants.files import FLASHCARDS_DB_JSON
    
    test_db_content = {
        "created_at": "2026-01-01T00:00:00.000000",
        "created_on": "2026-01-01",
        "entries": {"entries": {}, "total": 0},
        "metadata": {
            "available_ids": [],
            "fields": {"fields": [], "total": 0},
            "next_id": 1,
            "schema": {}
        },
        "updated_at": "2026-01-01T00:00:00.000000",
        "updated_on": "2026-01-01",
        "uuid": "test-uuid"
    }
    
    ensure_file(FLASHCARDS_DB_JSON, test_db_content)
```

### Running Tests

#### Basic Test Commands

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=studyfrog --cov-report=html

# Run specific test file
pytest tests/test_models.py

# Run specific test function
pytest tests/test_models.py::test_flashcard_creation

# Run with verbose output
pytest -v

# Run with specific markers
pytest -m "unit"
pytest -m "integration"
pytest -m "gui"
```

#### Test Markers

```python
# tests/conftest.py
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "unit: Mark test as unit test"
    )
    config.addinivalue_line(
        "markers", "integration: Mark test as integration test"
    )
    config.addinivalue_line(
        "markers", "gui: Mark test as GUI test"
    )
    config.addinivalue_line(
        "markers", "slow: Mark test as slow running"
    )

# Usage in tests
@pytest.mark.unit
def test_flashcard_validation():
    pass

@pytest.mark.integration
def test_full_workflow():
    pass

@pytest.mark.gui
def test_dashboard_view():
    pass

@pytest.mark.slow
def test_large_dataset():
    pass
```

---

## Debugging Guide

### Debugging Setup

#### Logging Configuration

```python
# Enable debug logging
from studyfrog.utils.logging import set_log_level, set_debug_mode

set_log_level('DEBUG')
set_debug_mode(True)

# Or use environment variable
export STUDYFROG_DEBUG=true
```

#### Debug Mode Features

```python
# In debug mode, the application provides:
# - Verbose logging
# - Performance metrics
# - Debug information in GUI
# - Additional validation
# - Development tools

if GLOBAL.get('debug_mode', False):
    # Enable debug features
    enable_debug_toolbar()
    show_performance_overlay()
    log_all_events()
```

### Common Debugging Scenarios

#### 1. Import Issues

```python
# Debug import problems
import sys
print("Python path:", sys.path)

try:
    import studyfrog.models.models
    print("Import successful")
except ImportError as e:
    print("Import failed:", e)
    print("Module location:", studyfrog.models.models.__file__)
```

#### 2. Event System Debugging

```python
# Debug event flow
def debug_event_handler(event_name: str, event_data: dict):
    print(f"Event: {event_name}")
    print(f"Data: {event_data}")
    print(f"Stack: {traceback.format_stack()}")

# Subscribe to all events for debugging
from studyfrog.constants.events import EVENT_CATEGORIES
for category, events in EVENT_CATEGORIES.items():
    for event in events:
        subscribe(event, lambda data, e=event: debug_event_handler(e, data))
```

#### 3. Storage Debugging

```python
# Debug storage operations
def debug_storage_operation(operation: str, file_path: Path, data: dict):
    print(f"Storage Operation: {operation}")
    print(f"File: {file_path}")
    print(f"Data size: {len(str(data))}")
    print(f"Data preview: {str(data)[:200]}...")

# Wrap storage functions
original_add_entry = add_entry
def debug_add_entry(file_path, model):
    debug_storage_operation("ADD", file_path, model.to_dict())
    return original_add_entry(file_path, model)

add_entry = debug_add_entry
```

#### 4. GUI Debugging

```python
# Debug GUI components
def debug_widget_info(widget):
    print(f"Widget: {widget}")
    print(f"Class: {widget.__class__}")
    print(f"Geometry: {widget.winfo_geometry()}")
    print(f"Children: {widget.winfo_children()}")

# Add debug info to widgets
def create_debug_button(parent, text, command):
    button = ctk.CTkButton(parent, text=text, command=command)
    button.bind("<Button-1>", lambda e: debug_widget_info(button))
    return button
```

### Performance Debugging

#### Timing Analysis

```python
import time
from functools import wraps

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__}: {end_time - start_time:.4f}s")
        return result
    return wrapper

# Apply to functions
@timing_decorator
def slow_function():
    time.sleep(1)
    return "done"
```

#### Memory Profiling

```python
import tracemalloc

def start_memory_profiling():
    tracemalloc.start()

def stop_memory_profiling():
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 1024 / 1024:.1f} MB")
    print(f"Peak memory usage: {peak / 1024 / 1024:.1f} MB")
    tracemalloc.stop()

# Usage
start_memory_profiling()
# ... run code ...
stop_memory_profiling()
```

---

## Performance Optimization

### Database Optimization

#### Efficient Queries

```python
# Good - batch operations
def add_flashcards_batch(flashcards: list[FlashcardModel]) -> bool:
    """Add multiple flashcards efficiently."""
    return add_entries(FLASHCARDS_DB_JSON, flashcards)

# Avoid - individual operations
def add_flashcards_slow(flashcards: list[FlashcardModel]) -> bool:
    """Inefficient individual operations."""
    for flashcard in flashcards:
        add_entry(FLASHCARDS_DB_JSON, flashcard)  # Multiple file writes
```

#### Caching Strategy

```python
from functools import lru_cache
import time

class ModelCache:
    def __init__(self, max_size: int = 1000, ttl: int = 3600):
        self.cache = {}
        self.max_size = max_size
        self.ttl = ttl
    
    def get(self, key: str):
        item = self.cache.get(key)
        if item and time.time() - item['timestamp'] < self.ttl:
            return item['data']
        return None
    
    def set(self, key: str, data):
        if len(self.cache) >= self.max_size:
            # Remove oldest item
            oldest_key = min(self.cache.keys(), 
                          key=lambda k: self.cache[k]['timestamp'])
            del self.cache[oldest_key]
        
        self.cache[key] = {
            'data': data,
            'timestamp': time.time()
        }

# Global cache instance
model_cache = ModelCache()
```

### GUI Optimization

#### Lazy Loading

```python
def load_flashcards_lazy(stack_key: str) -> list[FlashcardModel]:
    """Load flashcards only when needed."""
    cache_key = f"flashcards_{stack_key}"
    
    # Check cache first
    cached = model_cache.get(cache_key)
    if cached:
        return cached
    
    # Load from storage
    stack = get_entry(STACKS_DB_JSON, stack_key)
    flashcards = get_entries(FLASHCARDS_DB_JSON, stack.items)
    
    # Cache result
    model_cache.set(cache_key, flashcards)
    return flashcards
```

#### Virtual Scrolling

```python
# For large lists, use virtual scrolling
class VirtualListbox(ctk.CTkScrollableFrame):
    def __init__(self, parent, items, item_height=30):
        super().__init__(parent)
        self.items = items
        self.item_height = item_height
        self.visible_items = []
        
        # Create only visible items
        self.bind("<Configure>", self._on_scroll)
    
    def _on_scroll(self, event):
        """Update visible items based on scroll position."""
        # Calculate visible range
        scroll_info = self._get_scroll_info()
        start_idx = int(scroll_info['top'] / self.item_height)
        end_idx = int(scroll_info['bottom'] / self.item_height)
        
        # Update visible items
        self._update_visible_items(start_idx, end_idx)
```

### Memory Management

#### Resource Cleanup

```python
def cleanup_gui_resources():
    """Clean up GUI resources to prevent memory leaks."""
    # Clear event subscriptions
    from studyfrog.utils.dispatcher import clear_all_subscriptions
    clear_all_subscriptions()
    
    # Clear caches
    model_cache.clear()
    
    # Destroy GUI components
    if GLOBAL.get('root'):
        GLOBAL['root'].destroy()
    
    # Force garbage collection
    import gc
    gc.collect()
```

---

## Deployment Guide

### Building for Distribution

#### Setup Configuration

```python
# setup.py
from setuptools import setup, find_packages

setup(
    name="studyfrog",
    version="1.0.0",
    description="A comprehensive flashcard study application",
    author="Louis Goodnews",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "customtkinter>=5.0.0",
        "typing-extensions>=4.0.0",
    ],
    python_requires=">=3.11",
    entry_points={
        "console_scripts": [
            "studyfrog=studyfrog.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "studyfrog": ["assets/*", "templates/*"],
    },
)
```

#### PyInstaller Configuration

```python
# build.spec
import sys
from pathlib import Path

# Analysis
a = Analysis(
    ['src/studyfrog/main.py'],
    pathex=['src'],
    binaries=[],
    datas=[
        ('src/studyfrog/assets', 'assets'),
        ('src/studyfrog/templates', 'templates'),
    ],
    hiddenimports=[
        'tkinter',
        'customtkinter',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

# PYZ
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

# EXE
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='StudyFrog',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
```

### Build Commands

```bash
# Create source distribution
python setup.py sdist

# Create wheel distribution
python setup.py bdist_wheel

# Build executable with PyInstaller
pyinstaller build.spec --clean

# Create installer (platform-specific)
# Windows: Use NSIS or Inno Setup
# macOS: Use create-dmg or Packages
# Linux: Use AppImage or Flatpak
```

### Version Management

#### Semantic Versioning

```python
# version.py
VERSION = (1, 0, 0)
VERSION_STRING = "1.0.0"

def get_version():
    return VERSION_STRING

def increment_version(part):
    """Increment version part."""
    global VERSION, VERSION_STRING
    if part == 'major':
        VERSION = (VERSION[0] + 1, 0, 0)
    elif part == 'minor':
        VERSION = (VERSION[0], VERSION[1] + 1, 0)
    elif part == 'patch':
        VERSION = (VERSION[0], VERSION[1], VERSION[2] + 1)
    
    VERSION_STRING = f"{VERSION[0]}.{VERSION[1]}.{VERSION[2]}"
```

#### Release Process

```bash
# 1. Update version
python -c "from version import increment_version; increment_version('minor')"

# 2. Update changelog
# Edit CHANGELOG.md

# 3. Commit changes
git add .
git commit -m "Release v1.1.0"

# 4. Create tag
git tag v1.1.0

# 5. Build distribution
python setup.py sdist bdist_wheel

# 6. Upload to PyPI (if public)
twine upload dist/*

# 7. Push to remote
git push origin main --tags
```

### Deployment Automation

#### GitHub Actions

```yaml
# .github/workflows/build.yml
name: Build and Release

on:
  push:
    tags:
      - 'v*'

jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pyinstaller
    
    - name: Build executable
      run: |
        pyinstaller build.spec --clean
    
    - name: Upload artifacts
      uses: actions/upload-artifact@v2
      with:
        name: studyfrog-${{ matrix.os }}
        path: dist/
```

This development guide provides comprehensive information for contributing to StudyFrog, from initial setup through deployment.
