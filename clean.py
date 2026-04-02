import pandas as pd
from datasets import load_dataset

from utilities import preprocess

dataset = load_dataset("go_emotions", "simplified")
train_df = pd.DataFrame(dataset["train"])

def simplify_label(labels):
    return labels[0] if len(labels) > 0 else -1
train_df["label"] = train_df["labels"].apply(simplify_label)
train_df = train_df[train_df["label"] != -1]

train_df["clean_text"] = train_df["text"].apply(preprocess)
# selected_labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
label_map = {
    0: "neutral",
    2: "anger",
    3: "annoyance",
    4: "approval",
    5: "caring",
    7: "joy"
}
train_df = train_df[train_df["label"].isin(label_map)]
# print(train_df.head())
# print(train_df.describe())
