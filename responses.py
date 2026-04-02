import random

response_map = {
    # --- POSITIVE EMOTIONS ---
    "admiration": [
        "That's truly impressive. What do you respect most about it?",
        "I can see why you'd look up to that. Want to tell me more?",
    ],
    "amusement": [
        "Haha, that is pretty funny! What was the best part?",
        "Glad that gave you a good laugh. Want to share the story?",
    ],
    "approval": [
        "Sounds like you’re okay with it. What made it work?",
        "I agree, that seems like the right call. How did it happen?",
    ],
    "caring": [
        "That’s very kind of you. Who are you looking out for?",
        "It's great to see you looking after others. How are they doing?",
    ],
    "desire": [
        "That sounds like something you really want. What's the plan to get it?",
        "I can feel the motivation there. What's driving that wish?",
    ],
    "excitement": [
        "That energy is contagious! What are you most hyped about?",
        "Wow, sounds like big things are happening! Want to dive into details?",
    ],
    "gratitude": [
        "It’s wonderful to feel thankful. What are you most grateful for today?",
        "I'm glad you're feeling that appreciation. Want to tell me more?",
    ],
    "joy": [
        "That's awesome 😄 What made you feel this way?",
        "Love that energy. Want to share more?",
    ],
    "love": [
        "That’s such a beautiful sentiment. Who or what is on your mind?",
        "I can really feel the affection there. Want to talk about it?",
    ],
    "optimism": [
        "I love the positive outlook. What makes you so hopeful?",
        "Looking on the bright side! What’s the best-case scenario here?",
    ],
    "pride": [
        "You should be proud! What was the hardest part of achieving that?",
        "That's a huge win. How does it feel to see your hard work pay off?",
    ],
    "relief": [
        "Phew! I'm glad that weight is off your shoulders. How are you feeling now?",
        "That must be a massive relief. What was the turning point?",
    ],

    # --- NEGATIVE EMOTIONS ---
    "anger": [
        "That sounds frustrating. What happened?",
        "I can feel the tension. Want to talk it out?",
    ],
    "annoyance": [
        "That does sound irritating. What caused it?",
        "Ugh, I get why that's bothersome. Want to vent?",
    ],
    "disappointment": [
        "I'm sorry it didn't go as planned. What were you hoping for?",
        "That's tough when things fall short. How are you handling it?",
    ],
    "disapproval": [
        "I hear you. What specifically didn't sit right with you?",
        "It sounds like you're not a fan. What would you have changed?",
    ],
    "disgust": [
        "That sounds genuinely unpleasant. What made it feel that way?",
    ],
    "embarrassment": [
        "We've all been there! Do you want to talk about what happened?",
        "Ouch, those moments can be awkward. How are you feeling now?",
    ],
    "fear": [
        "I’m sorry you’re feeling scared. What’s the main thing on your mind?",
        "That sounds overwhelming. I'm here if you want to talk through it.",
    ],
    "grief": [
        "I am so sorry for what you're going through. I'm here for you.",
        "That is an incredibly heavy feeling. Do you want to share a memory?",
    ],
    "nervousness": [
        "It’s totally normal to feel a bit anxious. What’s the big event?",
        "I can tell you're a bit on edge. What's the main concern?",
    ],
    "remorse": [
        "It sounds like you're carrying some regret. What's weighing on you?",
        "Acknowledging that is a big step. Do you want to talk about it?",
    ],
    "sadness": [
        "I'm here for you. What's been weighing on you?",
        "That sounds tough. Do you want to talk about it?",
    ],

    # --- AMBIGUOUS & NEUTRAL ---
    "confusion": [
        "I'm a bit lost too. Can you help me understand what's happening?",
        "That does sound puzzling. What part is the most confusing?",
    ],
    "curiosity": [
        "That's a great question! What got you thinking about that?",
        "I love the interest there. What are you hoping to find out?",
    ],
    "realization": [
        "Oh! It sounds like something just clicked. What did you figure out?",
        "That 'aha' moment is the best. How did you come to that conclusion?",
    ],
    "surprise": [
        "Whoa, I didn't see that coming! Was it a good surprise?",
        "That’s unexpected! What was your first reaction?",
    ],
    "neutral": [
        "Got it. Tell me more.",
        "I'm listening.",
    ],
    "uncertain": [
    "I'm not fully sure I understand how you're feeling. Can you tell me more?",
    "That’s a bit hard to read. Want to explain a little more?",
    ]
}

scores = {
        "joy": 0,
        "anger": 0,
        "sadness": 0,
        "confusion": 0,
        "annoyance": 0,
        "approval": 0,
        "neutral": 0
 }

rules = {
    "joy": ["amazing", "great", "awesome", "fantastic", "happy"],
    "anger": ["hate", "angry", "furious"],
    "sadness": ["sad", "tired", "down"],
    "confusion": ["confused", "lost"],
    "annoyance": ["ugh", "annoying", "irritating"],
    "approval": ["fine", "okay", "works"],
    "neutral": ["hungry", "eating", "food"]
}

def generate_responses(emotion):
    if emotion in response_map:
        return random.choice(response_map[emotion])
    return "Tell me more"


def rule_signal(text):
    for emotion, words in rules.items():
        if any(w in text for w in words):
            scores[emotion] += 2

    return scores