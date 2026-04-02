import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sentence_transformers import SentenceTransformer
from clean import train_df

print("Encoding text into embeddings...")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

X = embedder.encode(train_df["text"].tolist(), show_progress_bar=True)
y = train_df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = LogisticRegression(max_iter=1000, class_weight="balanced")
model.fit(X_train, y_train)
joblib.dump(model, "classifier.pkl")

print("Model + Vectorizer saved ✅")