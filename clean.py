import pandas as pd
import re
from datasets import load_dataset


def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    return text



dataset = load_dataset("go_emotions", "simplified")
train_df = pd.DataFrame(dataset["train"])

# print(train_df.head())
#                                                 text labels       id
# 0  My favourite food is anything I didn't have to...   [27]  eebbqej
# 1  Now if he does off himself, everyone will thin...   [27]  ed00q6i
# 2                     WHY THE FUCK IS BAYLESS ISOING    [2]  eezlygj
# 3                        To make her feel threatened   [14]  ed7ypvh
# 4                             Dirty Southern Wankers    [3]  ed0bdzj

def simplify_label(labels):
    return labels[0] if len(labels) > 0 else -1
train_df["label"] = train_df["labels"].apply(simplify_label)
train_df = train_df[train_df["label"] != -1]
# print(train_df.head())
#                                                 text labels       id  label
# 0  My favourite food is anything I didn't have to...   [27]  eebbqej     27
# 1  Now if he does off himself, everyone will thin...   [27]  ed00q6i     27
# 2                     WHY THE FUCK IS BAYLESS ISOING    [2]  eezlygj      2
# 3                        To make her feel threatened   [14]  ed7ypvh     14
# 4                             Dirty Southern Wankers    [3]  ed0bdzj      3
train_df["clean_text"] = train_df["text"].apply(preprocess)
selected_labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
train_df = train_df[train_df["label"].isin(selected_labels)]
# print(train_df.head())
#                                               text  ...                                         clean_text
# 0  My favourite food is anything I didn't have to...  ...  my favourite food is anything i didn t have to...
# 1  Now if he does off himself, everyone will thin...  ...  now if he does off himself  everyone will thin...
# 2                     WHY THE FUCK IS BAYLESS ISOING  ...                     why the fuck is bayless isoing
# 3                        To make her feel threatened  ...                        to make her feel threatened
# 4                             Dirty Southern Wankers  ...                             dirty southern wankers
# print(train_df.describe())
