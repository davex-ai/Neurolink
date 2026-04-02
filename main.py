from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from model import predict_emotion
from utilities import update_memory
from responses import generate_responses

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "NeuroLink API running 🧠"}


@app.post("/predict")
def predict(data: dict):
    text = data.get("text", "")

    if not text:
        return {"error": "No text provided"}

    emotion, confidence = predict_emotion(text)

    update_memory(text, emotion)

    response = generate_responses(emotion)

    return {
        "emotion": emotion,
        "confidence": confidence,
        "response": response
    }