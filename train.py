from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from clean import train_df, preprocess

vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1,2))

x = vectorizer.fit_transform(train_df["clean_text"])
y = train_df["label"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(f"x_train.shape: {x_train.shape}, y_train.shape: {y_train.shape}, x_test.shape: {x_test.shape}, y_test.shape: {y_test.shape}")

models = [RandomForestClassifier(n_estimators=100, random_state=42), LogisticRegression(max_iter=1000), LinearRegression(), DecisionTreeClassifier()]
for model in models:
    print("Training model with", model, "...")
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    if not isinstance(model, LinearRegression):
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("Report:", classification_report(y_test, y_pred))
    else:
        print("MSE:", mean_squared_error(y_test, y_pred))
        print("R2 Score:", r2_score(y_test, y_pred))

def predict_emotion(text):
    text = preprocess(text)
    vector = vectorizer.transform([text])
    prediction = model.predict(vector)[0] # what is the [0] for?
    return prediction

print(predict_emotion("I feel amazing today"))
print(predict_emotion("I hate everything"))