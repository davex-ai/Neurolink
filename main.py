from fastapi import FastAPI, APIRouter
import joblib
from starlette.middleware.cors import CORSMiddleware

from clean import preprocess, label_map
from responses import generate_responses, rule_based_override

# Load model
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

app = FastAPI()
neurolink = APIRouter(prefix="/neurolink")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
conversation_memory = []
emotion_memory = []
@neurolink.get("/")
def home():
    return {"message": "NeuroLink API is running 🧠"}

@neurolink.post("/predict")
def predict(data: dict):
    text = data.get("text", "")
    conversation_memory.append(text)
    context = " ".join(conversation_memory[-5:])
    cleaned = preprocess(context)
    embedding = vectorizer.encode([cleaned])

    if not text:
        return {"error": "No text provided"}

    cleaned = preprocess(text)
    embedding = vectorizer.encode([cleaned])

    override = rule_based_override(text)

    if override and confidence < 0.6: # Unresolved reference 'confidence'
        emotion = override
        confidence = 0.9
    else:
        probs = model.predict_proba(embedding)[0]
        idx = probs.argmax()

        prediction = model.classes_[idx]
        confidence = float(probs[idx])

        if confidence < 0.45:
            emotion = "uncertain"
        else:
            emotion = label_map[prediction]

    response = generate_responses(emotion)
    emotion_memory.append(emotion)
    if emotion == "uncertain" and emotion_memory:
        emotion = emotion_memory[-1]

    return {
        "emotion": emotion,
        "confidence": confidence,
        "response": response
    }
app.include_router(neurolink)
