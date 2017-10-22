import random

from emotion import Emotion

def handle_sadness(probability):
    if probability > .75:
        return Emotion.HAPPY
    elif probability > .6:
        return Emotion.TRUST
    else:
        return Emotion.GRATITUDE

def handle_joy(probability):
    if probability > .75:
        return Emotion.LOVE
    elif probability > .6:
        return Emotion.PRAISE
    else:
        return Emotion.GRATITUDE 

def handle_fear(probability):
    return (Emotion.PEACE, Emotion.TRUST, Emotion.ENCOURAGEMENT)[random.randrange(3)]

def handle_disgust(probability):
    return (Emotion.PEACE, Emotion.ENCOURAGEMENT)[random.randrange(2)]

def handle_anger(probability):
    if probability > .7:
        return Emotion.PEACE
    elif probability > .6:
        return Emotion.TRUST 
    else:
        return Emotion.ENCOURAGMENT


