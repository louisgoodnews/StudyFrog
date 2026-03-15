# StudyFrog Roadmap

## Current State

StudyFrog has a meaningful amount of application code already in place:

- A domain model layer for flashcards, notes, questions, answers, stacks, priorities, difficulties, and related entities
- JSON-backed storage utilities
- An event-dispatch architecture
- A CustomTkinter GUI structure with multiple views and forms
- Basic project scaffolding for packaging, docs, and CI

At the same time, the project is not yet in a dependable release-ready state.

Key issues confirmed during review:

- Package imports are not install-safe and currently break `import studyfrog...`
- Automated tests are effectively absent
- Several GUI flows still contain placeholder `pass` implementations
- Some destructive workflows such as deleting nested models are incomplete
- README and docs are still mostly scaffold-level
- Import-time side effects create noisy warnings and make startup behavior harder to reason about

This roadmap is organized to first stabilize the project, then make it fully usable as an MVP, and finally expand it into a stronger study product.

## Guiding Priorities

1. Make the project runnable and testable.
2. Finish incomplete core workflows before adding new features.
3. Document the real state of the application clearly.
4. Add product features only after the foundation is stable.

## Phase 1: Stabilize the Foundation

Goal: make the application runnable, debuggable, and safe to change.

### Must complete

- Fix all package import paths so the project works as `studyfrog` from `src`
- Ensure a supported entrypoint works consistently, ideally `python -m studyfrog.main`
- Verify startup and shutdown flows behave correctly once dependencies are installed
- Reduce import-time side effects, especially default model creation and warning spam
- Make CI meaningful by adding at least smoke-level tests
- Rewrite README setup instructions so a new developer can install and run the app
- Expand docs from placeholder text into a basic project overview

### Deliverables

- Working package imports throughout `src/studyfrog`
- A documented local run command
- Smoke tests for:
  - package imports
  - model factory creation
  - storage initialization
  - application bootstrap behavior where possible
- Updated `README.md`
- Updated `docs/index.rst`

### Suggested task order

1. Fix import paths across `main`, `core`, `models`, `utils`, `gui`, and `constants`
2. Add one import smoke test that fails if package structure breaks again
3. Add storage and model tests
4. Clean up startup logging and side effects
5. Refresh docs and onboarding material

## Phase 2: Deliver a Usable MVP

Goal: make StudyFrog function as a coherent study app for day-to-day use.

### Core workflows that must work end-to-end

- Create, view, edit, and delete stacks
- Create, view, edit, and delete flashcards
- Create, view, edit, and delete notes
- Create, view, edit, and delete questions and answers
- Launch a rehearsal run from the UI
- Complete a rehearsal session without hitting placeholder views
- Persist rehearsal results correctly
- Re-open the app and see stored data intact

### Known implementation gaps to finish

- Answer rehearsal view
- Question rehearsal view
- Note rehearsal view
- Rehearsal run result view
- Flashcard edit form
- Delete confirmation behavior for models with sub-items

### MVP quality bar

- No obvious dead buttons or empty placeholder screens
- No data loss during normal CRUD operations
- Error messages are visible and understandable
- Basic manual regression checklist exists for common flows

### Deliverables

- Complete GUI behavior for the currently exposed views
- CRUD tests for storage-backed entities
- Manual QA checklist for primary user journeys
- A short feature-status section in the README

## Phase 3: Improve Data Integrity and Maintainability

Goal: make the system safer as the data model grows.

### Needed fixes

- Define clearer validation rules for models before persistence
- Protect against malformed or partially written JSON data
- Review ID generation, UUID usage, and table metadata consistency
- Add migration or repair utilities for older data formats if storage schema evolves
- Make delete behavior explicit for parent-child relationships
- Add better internal boundaries between GUI, application logic, and storage logic

### Technical improvements

- Introduce stricter typing where it adds clarity
- Reduce wildcard imports from constants/events modules
- Add linting and formatting commands to regular developer workflow
- Strengthen logging so errors are easier to trace to feature areas
- Add targeted unit tests for dispatcher behavior and storage edge cases

### Deliverables

- Validation helpers for persisted models
- Data-repair or schema-check utilities
- Better test coverage around storage and events
- Cleaner separation of concerns in the core modules

## Phase 4: Product Features That Should Exist

Goal: make StudyFrog feel like a complete study companion rather than only a CRUD app.

### High-value product features

- Search across stacks, flashcards, notes, and questions
- Filter by tags, subject, teacher, difficulty, or priority
- Sort study content by recency, difficulty, or priority
- Dashboard summaries such as total cards, due items, and recent activity
- Better rehearsal setup options such as selecting content by type or stack
- Study progress tracking across rehearsal runs

### Scheduling and repetition

- Daily review queue
- Basic spaced-repetition scheduling
- Review recommendations based on difficulty and past performance
- Per-item rehearsal history

### Data portability

- Export study data to JSON or CSV
- Import study data from supported formats
- Backup and restore workflow

## Phase 5: Nice-to-Have Features

Goal: expand usefulness and polish once the core product is dependable.

### Nice to have

- Keyboard-first study mode
- Richer dashboard analytics and streaks
- Image attachments for flashcards or notes
- Custom fields exposed cleanly in the UI
- Bulk edit and bulk delete actions
- Theme customization and UI polish
- Better empty states and onboarding flows
- Session summaries after each rehearsal run

### Longer-term possibilities

- Multi-user profiles
- Cloud sync
- Plugin or extension architecture
- Optional web companion or mobile companion

## Suggested Milestones

### Milestone 1: Project Health

- Imports fixed
- App starts reliably
- Smoke tests added
- README and docs updated

### Milestone 2: MVP Complete

- CRUD flows work for main study entities
- Rehearsal flows are functional
- Placeholder views removed or implemented
- Manual QA checklist completed

### Milestone 3: Reliable Persistence

- Data validation improved
- Edge-case tests added
- Delete and nested-model behavior clarified

### Milestone 4: Study Experience Upgrade

- Search, filtering, dashboard metrics, and review history added
- Scheduling logic introduced

## Immediate Next Actions

If work starts now, the highest-leverage next steps are:

1. Fix package-relative imports across the project.
2. Add a minimum test suite so CI validates something real.
3. Implement or temporarily hide placeholder GUI flows.
4. Finish deletion and edit behavior for nested data.
5. Rewrite README and docs to match the actual project.
