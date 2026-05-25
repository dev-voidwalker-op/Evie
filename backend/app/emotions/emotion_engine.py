import random

#These are the emotions that will be there in Evie
EMOTIONS = [
    "idle",
    "happy",
    "sad",
    "angry",
    "thinking"
]


class EmotionEngine:

    def get_random_emotion(self):

        return random.choice(EMOTIONS)


emotion_engine = EmotionEngine()
