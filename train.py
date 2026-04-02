from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from clean import train_df, preprocess, label_map

vectorizer = TfidfVectorizer(max_features=10000, ngram_range=(1,2), stop_words='english', max_df=0.8, min_df=5)

x = vectorizer.fit_transform(train_df["clean_text"])
y = train_df["label"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)
print(f"x_train.shape: {x_train.shape}, y_train.shape: {y_train.shape}, x_test.shape: {x_test.shape}, y_test.shape: {y_test.shape}")

model = LogisticRegression(max_iter=1000, class_weight="balanced")
print("Training model with", model, "...")
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Report:", classification_report(y_test, y_pred))

def predict_emotion(text):
    text = preprocess(text)
    vector = vectorizer.transform([text])
    probs = model.predict_proba(vector)[0]
    prediction = probs.argmax()
    confidence = probs.max()
    if confidence < 0.5:
        return "uncertain" , confidence
    return label_map[int(prediction)], confidence

print(predict_emotion("I feel amazing today"))
print(predict_emotion("I hate everything"))
print(predict_emotion("I don't know how I feel anymore"))
print(predict_emotion("I'm smiling but I'm actually tired"))
print(predict_emotion("This is fine I guess"))