import joblib
from sentence_transformers import SentenceTransformer
from utilities import preprocess
from responses import rule_based_override

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
    text = preprocess(text)

    # Rule first
    override = rule_based_override(text)

    vector = embedder.encode([text])
    probs = model.predict_proba(vector)[0]

    idx = probs.argmax()
    confidence = float(probs[idx])
    prediction = model.classes_[idx]

    # Hybrid logic
    if override and confidence < 0.6:
        return override, 0.85

    if confidence < 0.45:
        return "uncertain", confidence

    return label_map[prediction], confidence