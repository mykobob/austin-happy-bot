import random

def handle_sadness(probability):
    if probability > .75:
        return HAPPY
    elif probability > .6:
        return TRUST
    else:
        return GRATITUDE

def handle_joy(probability):
    if probability > .75:
        return LOVE
    elif probability > .6:
        return PRAISE
    else:
        return GRATITUDE 

def handle_fear(probability):
    return (PEACE, TRUST, ENCOURAGEMENT)[random.randrange(3)]

def handle_disgust(probability):
    return (PEACE, ENCOURAGEMENT)[random.randrange(2)]

def handle_anger(probability):
    if probability > .7:
        return PEACE
    elif probability > .6:
        return TRUST 
    else:
        return ENCOURAGMENT


