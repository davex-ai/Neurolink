# 🧠 NeuroLink — Emotion-Aware AI API

> *“Not just what you say… but how you feel.”*

---

## 🚀 Overview

**NeuroLink** is an emotion-aware AI system that understands human input using:

* 🧠 **Embeddings (semantic understanding)**
* 📜 **Rule-based signals (emotion cues)**
* 🕰️ **Conversation memory (context awareness)**
* ⚖️ **Multi-signal fusion (real intelligence)**

It doesn’t just classify text — it **interprets emotional intent** and responds accordingly.

---

## ✨ Features

* 🎯 Emotion Detection (joy, anger, sadness, etc.)
* 🧠 Context-Aware Memory (last 5 messages)
* ⚡ Real-Time API (FastAPI backend)
* 🎤 Voice Input (Web Speech API)
* 💬 Emotion-Based Responses
* 🔀 Multi-Signal Prediction (rules + ML + history)

---

## 🧩 Architecture

```
User Input
   ↓
Preprocessing
   ↓
├── Rule Signal (keywords, patterns)
├── Embedding Model (MiniLM + Logistic Regression)
└── History Signal (past emotions)
   ↓
⚖️ Signal Fusion Engine
   ↓
Emotion + Confidence
   ↓
Response Generator
```

---

## 🛠️ Tech Stack

* **Backend:** FastAPI ⚡
* **ML:** SentenceTransformers + Logistic Regression
* **Frontend:** HTML + JS
* **Voice:** Web Speech API
* **Dataset:** GoEmotions

---

---

## ⚙️ Installation

```bash
git clone https://github.com/davex-ai/Neurolink.git
cd neurolink

pip install -r requirements.txt
```

---

## ▶️ Run the API

```bash
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## 📡 API Usage

### POST `/neurolink/predict`

```json
{
  "text": "I feel amazing today"
}
```

### Response

```json
{
  "emotion": "joy",
  "confidence": 0.91,
  "response": "That's awesome 😄 What made you feel this way?"
}
```

---

## 🧠 Example Predictions

| Input                     | Emotion      |
| ------------------------- | ------------ |
| "I feel amazing today"    | joy 😄       |
| "I hate everything"       | anger 😠     |
| "I'm smiling but tired"   | sadness 😔   |
| "I'm confused about life" | confusion 🤔 |

---

## 🎤 Voice Support

Click the 🎤 button to:

* Speak naturally
* Auto-convert speech → text
* Get emotion-aware responses

---

## 🧪 Model Details

* Embeddings: `all-MiniLM-L6-v2`
* Classifier: Logistic Regression
* Classes:

  * neutral
  * anger
  * annoyance
  * approval
  * caring
  * joy

---

## 🧠 Intelligence Layer

NeuroLink uses **multi-signal fusion**:

```python
final_score = (
    0.3 * rule_signal +
    0.6 * model_prediction +
    0.1 * history_signal
)
```

This makes predictions:

* More stable
* More human-like
* Context-aware

---

## 🔮 Future Improvements

* 🧠 Transformer Fine-Tuning (DistilBERT)
* 🗣️ Text-to-Speech (AI voice responses)
* 🧬 Emotion Smoothing (less jumpy behavior)
* 📊 User Personalization
* 📱 Mobile App

---

## 🧪 Example UI

```
You: I feel great today  
NeuroLink: That's awesome 😄 What made you feel this way?

You: I'm sooo tired  
NeuroLink: That sounds tough. Do you want to talk about it?
```

---

## ⚠️ Known Limitations

* Limited emotional nuance (MVP stage)
* Small label space
* Rule system is heuristic-based

---

## 💡 Why This Project Matters

Most NLP systems:

> classify text

NeuroLink:

> **understands emotional intent + context**

---

## 🧑‍💻 Author

Built by a developer pushing beyond beginner level into real AI systems 🚀

---

## ⭐ If you like this project

* Star the repo ⭐
* Fork it 🍴
* Build on it 🧠

---

## 🧠 Final Thought

> “The next generation of software won’t just respond… it will *understand*.”

---
