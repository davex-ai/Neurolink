import joblib
from sentence_transformers import SentenceTransformer
from utilities import preprocess
from responses import rule_signal

label_map = {
    0: "neutral",
    2: "anger",
    3: "annoyance",
    4: "approval",
    5: "caring",
    7: "joy"
}

model = joblib.load("classifier.pkl")
embedder = SentenceTransformer("all-MiniLM-L6-v2")


def predict_emotion(text):
    from utilities import emotion_memory, history_signal, combine_signals

    text = preprocess(text)

    # ---- 1. RULE SIGNAL ----
    rule_scores = rule_signal(text)

    # ---- 2. MODEL SIGNAL ----
    vector = embedder.encode([text])
    probs = model.predict_proba(vector)[0]

    model_scores = {
        label_map[model.classes_[i]]: probs[i]
        for i in range(len(probs))
    }

    history_scores = history_signal(emotion_memory)

    final_scores = combine_signals(rule_scores, model_scores, history_scores)

    emotion = max(final_scores, key=final_scores.get)
    confidence = float(final_scores[emotion])

    if confidence < 0.4:
        emotion = "uncertain"

    return emotion, confidence