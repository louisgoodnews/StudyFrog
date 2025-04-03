# StudyFrog TextAnalyzer Module Documentation 🧠🔍🐸

Welcome to the documentation for the `text_analyzer` module in StudyFrog! This module implements a thread-safe, singleton-based semantic similarity analyzer using `sentence-transformers`. It provides model lifecycle management, encoding, and similarity computation for educational text input.

---

## 📘 Overview
The `TextAnalyzer` class is a **singleton** utility used to:
- Load and manage a transformer model (lazily)
- Encode input text into embeddings
- Compute cosine similarity between sentences
- Dispatch analysis start and completion events
- Automatically unload the model after inactivity

---

## 🧠 Class: `TextAnalyzer`

### Description
Handles loading and unloading of the `SentenceTransformer` model, computes sentence similarity, and ensures thread-safe singleton behavior. The model is auto-unloaded after a timeout (default: 600s).

### Singleton Pattern
Uses a `threading.Lock` and a private `_shared_instance` to ensure only one instance exists.

---

## 🛠 Initialization

### `__new__(model_name="sentence-transformers/all-MiniLM-L6-v2")`
Creates or returns the shared instance. Calls `.init()` during first-time setup.

### `init(model_name)`
Sets up the logger, dispatcher, time limit, timestamp, and model metadata. Does not load the model immediately.

---

## 🔧 Properties
- `model`: The loaded transformer model (or `None`)
- `model_name`: Name of the transformer model to load

Setters are provided for both properties.

---

## 🧰 Core Methods

### `_load_model()`
Loads the model using `SentenceTransformer`. If already loaded, does nothing. Updates internal timestamp.

### `_unload_model()`
Unloads the model if the configured time limit has passed since the last use. Schedules itself for future execution using `threading.Timer`.

### `_encode(sentences)`
Encodes one or more sentences into vector representations using the transformer model. Handles both strings and lists of strings.

### `get_similarity(original, compare_to)`
Computes the **cosine similarity** between two sentences or lists of sentences. Dispatches events to notify system of analysis progress:
- `TEXT_ANALYZER_ANALYSIS_STARTED`
- `TEXT_ANALYZER_ANALYSIS_COMPLETED`

---

## 📝 Example
```python
analyzer = TextAnalyzer()
similarity = analyzer.get_similarity("Study frogs", "Read frogs")
print(f"Similarity: {similarity:.2f}")
```

---

## ✅ Best Practices
- Always access via `TextAnalyzer()` for singleton behavior
- Let the analyzer manage model loading/unloading automatically
- Handle `None` or exceptions when model fails or is unavailable
- Use events and logs to monitor background analysis

---

## 💡 Future Enhancements
- Support for batching and matrix similarity
- Custom timeouts or scheduling strategies
- Switch between multiple models dynamically
- Persistent caching of encodings

---

Semantic similarity, simplified — the StudyFrog way 🧠✨🐸

