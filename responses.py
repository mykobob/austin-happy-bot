from ibm import get_emotion_probabilities
import sys

from emotion_handlers import *

from classObj import getResponse

MINIMUM_THRESHOLD = 0.5

def has_dominant_emotion(response):
    return any(v > MINIMUM_THRESHOLD for k, v in response.items())

def get_dominant_emotion(response):
    best_prob = -1
    strongest_emotion = 'something'
    for k, v in response.items():
        if v > best_prob:
            best_prob = v
            strongest_emotion = k

    return strongest_emotion, best_prob

def get_emotion_for_verse(response):
    # Maps sadness, joy, fear, disgust, anger to the below emotions
    # HAPPY = 1
    # PRAISE = 2
    # LOVE = 3
    # PEACE = 4
    # GRATITUDE = 5
    # TRUST = 6
    # ENCOURAGEMENT = 7

    # sadness -> [HAPPY, TRUST, GRATITUDE]
    # joy -> [LOVE, PRAISE, GRATITUDE]
    # fear -> [PEACE, TRUST, ENCOURAGEMENT]
    # disgust -> [PEACE, ENCOURAGEMENT] 
    # anger -> [PEACE, TRUST, ENCOURAGEMENT]
    highest_emotion, value = get_dominant_emotion(response)
    if highest_emotion == 'sadness':
        return handle_sadness(value), value
    elif highest_emotion == 'joy':
        return handle_joy(value), value
    elif highest_emotion == 'fear':
        return handle_fear(value), value
    elif highest_emotion == 'disgust':
        return handle_disgust(value), value
    else: # must be anger
        return handle_anger(value), value

def generate_response(text):
    # 1) Send data to IBM Watson
    # 2) Retrieve emotion probabilities
    #   2a) Determine if we have a clear emotion
    #      3) Get random verse
    #      4) Get verse text
    #      5) return the verse
    #   2b) 
    #      3) Ask another question to figure out emotion
    text = text.lower()

    try:
        emotion_probabilities = get_emotion_probabilities(text)
        if has_dominant_emotion(emotion_probabilities):
            # response = ['{}-{} '.format(k, v) for k, v in response.items()]
            # response = str(response)
            print('Is Dominant emotion')
            emotion_verse, confidence = get_emotion_for_verse(emotion_probabilities)
            print('Emotion for verse is', emotion_verse)

            response = getResponse(emotion_verse.value, confidence)
            print('Response for the message is', response)
            return response
        else:
            return "Can you elaborate a little more on that?"
    except:
        e = sys.exc_info()[0]
        return "Oh. What do you mean?"

    #if 'sad' in text:
    #    return 'Cheer up! God is with you (Joshua 1:9)'

    #return "Don't worry. Jesus loves you"

