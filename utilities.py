import re
conversation_memory = []
emotion_memory = []

def update_memory(text, emotion):
    conversation_memory.append(text)
    emotion_memory.append(emotion)

def get_context():
    return " ".join(conversation_memory[-5:])


def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"(.)\1{2,}", r"\1\1", text)
    return text


def history_signal(emotion_memory):
    scores = {}

    for emo in emotion_memory[-3:]:  # last 3 emotions
        scores[emo] = scores.get(emo, 0) + 0.5

    return scores


def combine_signals(rule_scores, model_scores, history_scores):
    final_scores = {}

    all_emotions = set(rule_scores) | set(model_scores) | set(history_scores)

    for emo in all_emotions:
        final_scores[emo] = (
            0.3 * rule_scores.get(emo, 0) +
            0.6 * model_scores.get(emo, 0) +
            0.1 * history_scores.get(emo, 0)
        )

    return final_scores