StudyFrog Documentation
===============================

Welcome to the comprehensive documentation for StudyFrog, a powerful flashcard study application built with Python and CustomTkinter.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   CONTRIBUTOR_GUIDE
   ARCHITECTURE
   CODE_DESIGN_PRINCIPLES
   CORE_MODULES
   MODEL_LAYER
   GUI_LAYER
   UTILITY_MODULES
   CONSTANTS_AND_CONFIG
   DISPATCHING_SYSTEM
   DEVELOPMENT_GUIDE

Project Overview
----------------

StudyFrog is a comprehensive flashcard application that provides:

* **Flashcard Management**: Create, edit, and organize flashcards with rich metadata
* **Stack Organization**: Group flashcards into thematic collections
* **Rehearsal System**: Practice sessions with multiple question types
* **Data Persistence**: JSON-based storage with backup and restore
* **Event-Driven Architecture**: Modular, maintainable codebase
* **Modern GUI**: CustomTkinter-based interface with dark/light themes

Getting Started
---------------

For New Contributors
~~~~~~~~~~~~~~~~~~~

1. Read the :doc:`CONTRIBUTOR_GUIDE` for an overview
2. Follow the :doc:`DEVELOPMENT_GUIDE` for setup instructions
3. Review the :doc:`ARCHITECTURE` to understand the system design
4. Explore the module documentation for specific areas

For Users
~~~~~~~~~~

1. Install Python 3.11+
2. Clone the repository
3. Install dependencies: ``pip install -r requirements.txt``
4. Run the application: ``python -m studyfrog.main``

Documentation Structure
----------------------

The documentation is organized to help you quickly find the information you need:

**For Contributors**
* :doc:`CONTRIBUTOR_GUIDE` - Comprehensive guide for contributors
* :doc:`DEVELOPMENT_GUIDE` - Setup, workflow, and deployment
* :doc:`ARCHITECTURE` - System design and patterns

**For Developers**
* :doc:`CORE_MODULES` - Application lifecycle and bootstrap
* :doc:`MODEL_LAYER` - Data structures and business logic
* :doc:`GUI_LAYER` - User interface components
* :doc:`UTILITY_MODULES` - Storage, events, and utilities
* :doc:`CONSTANTS_AND_CONFIG` - Configuration and constants

Quick Reference
---------------

Application Entry Point
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from studyfrog.main import main
   
   # Run the application
   main()

Creating a Flashcard
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

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

Handling Events
~~~~~~~~~~~~~~~~

.. code-block:: python

   from studyfrog.utils.dispatcher import dispatch, subscribe
   from studyfrog.constants.events import FLASHCARD_CREATED
   
   # Subscribe to events
   def on_flashcard_created(event_data):
       flashcard = event_data.get('flashcard')
       print(f"New flashcard: {flashcard.front}")
   
   subscribe(FLASHCARD_CREATED, on_flashcard_created)
   
   # Dispatch events
   dispatch(FLASHCARD_CREATED, {'flashcard': flashcard})

Key Concepts
------------

Event-Driven Architecture
~~~~~~~~~~~~~~~~~~~~~~~~

StudyFrog uses an event-driven architecture where components communicate through events rather than direct method calls. This provides:

* **Loose Coupling**: Components don't depend on each other directly
* **Flexibility**: Easy to add new features or modify existing ones
* **Testability**: Components can be tested in isolation

Model-Factory Pattern
~~~~~~~~~~~~~~~~~~~~~

Models are created using factory functions to ensure consistency and validation:

.. code-block:: python

   # Use factory functions (recommended)
   flashcard = get_flashcard_model(front="Q", back="A")
   
   # Avoid direct instantiation
   flashcard = FlashcardModel(front="Q", back="A")  # No validation

JSON-Based Storage
~~~~~~~~~~~~~~~~~~

All data is stored in JSON files with a consistent structure:

.. code-block:: json

   {
       "created_at": "2026-01-01T10:00:00.000000",
       "created_on": "2026-01-01",
       "entries": {
           "entries": {
               "0": { /* model data */ }
           },
           "total": 1
       },
       "metadata": {
           "available_ids": [],
           "fields": { /* field definitions */ },
           "next_id": 1,
           "schema": {}
       },
       "updated_at": "2026-01-01T10:00:00.000000",
       "updated_on": "2026-01-01",
       "uuid": "unique-identifier"
   }

Module Organization
------------------

The application is organized into logical modules:

* **Core**: Application lifecycle and bootstrap
* **Models**: Data structures and business logic
* **GUI**: User interface components
* **Utils**: Storage, events, logging, and utilities
* **Constants**: Configuration and event definitions

Development Workflow
---------------------

1. **Setup**: Follow the development guide to set up your environment
2. **Understand**: Review the architecture and module documentation
3. **Develop**: Follow the coding standards and patterns
4. **Test**: Write and run tests for your changes
5. **Document**: Update relevant documentation
6. **Contribute**: Submit a pull request with clear description

Support and Contributing
------------------------

Getting Help
~~~~~~~~~~~~~

* **Issues**: Report bugs or request features through GitHub issues
* **Discussions**: Ask questions in GitHub discussions
* **Documentation**: Refer to these docs for detailed information

Contributing
~~~~~~~~~~~~

We welcome contributions! Please:

1. Read the :doc:`CONTRIBUTOR_GUIDE`
2. Follow the :doc:`DEVELOPMENT_GUIDE`
3. Write tests for new features
4. Update documentation
5. Submit pull requests with clear descriptions

License
-------

StudyFrog is released under the MIT License. See the LICENSE file for details.

---

**Happy studying and happy coding!** 🐸
