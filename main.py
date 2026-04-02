from fastapi import FastAPI, APIRouter
import joblib

from clean import preprocess, label_map
from responses import generate_responses

# Load model
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

app = FastAPI()
neurolink = APIRouter(prefix="/neurolink")

@neurolink.get("/")
def home():
    return {"message": "NeuroLink API is running 🧠"}

@neurolink.post("/predict")
def predict(data: dict):
    text = data.get("text", "")

    if not text:
        return {"error": "No text provided"}

    # Preprocess
    cleaned = preprocess(text)
    vector = vectorizer.transform([cleaned])

    probs = model.predict_proba(vector)[0]
    idx = probs.argmax()

    prediction = model.classes_[idx]
    confidence = float(probs[idx])

    emotion = label_map[prediction]
    if confidence < 0.5:
        emotion = "uncertain"
    else:
        response = generate_responses(emotion)
        return {
            "emotion": emotion,
            "confidence": confidence,
            "response": response
        }

    return {
        "emotion": label_map[prediction],
        "confidence": confidence
    }
app.include_router(neurolink)
