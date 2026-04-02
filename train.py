from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sentence_transformers import SentenceTransformer
from clean import train_df, preprocess, label_map
from responses import rule_based_override

print("Encoding text into embeddings...")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# We apply the embeddings to the whole cleaned dataset
X = embedder.encode(train_df["text"].tolist(), show_progress_bar=True)
y = train_df["label"]

# 2. Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. Train - Logistic Regression is great with embeddings
model = LogisticRegression(max_iter=1000, class_weight="balanced")
model.fit(X_train, y_train)

# 4. Evaluate
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(f"Report: {classification_report(y_test, y_pred)}")


def predict_emotion(text):
    text = preprocess(text)
    # Encode the single input text
    overide = rule_based_override(text)
    if overide:
        return overide, 0.9

    vector = embedder.encode([text])
    probs = model.predict_proba(vector)[0]

    max_idx = probs.argmax()
    confidence = probs[max_idx]
    prediction_label_id = model.classes_[max_idx]

    if confidence < 0.4:  # Lowered threshold slightly as embeddings distribute probability more
        return "uncertain", confidence

    return label_map[int(prediction_label_id)], confidence


test_sentences = [
    "I feel amazing today",
    "I hate everything",
    "I don't know how I feel anymore",
    "I'm smiling but I'm actually tired",
    "This is fine I guess"
]

for s in test_sentences:
    emotion, conf = predict_emotion(s)
    print(f"[{emotion}] ({conf:.2f}) -> {s}")
