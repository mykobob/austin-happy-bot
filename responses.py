from ibm import call_ibm_watson
import sys

MINIMUM_THRESHOLD = 0.5

def clear_emotion(response):
    return any(v > MINIMUM_THRESHOLD for k, v in response.items())

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
    print('text', text)
    try:
        response = call_ibm_watson(text)['emotion']['document']['emotion']
        if clear_emotion(response):
            # get verse and stuff
            response = ['{}-{} '.format(k, v) for k, v in response.items()]
            response = str(response)
            return response
        else:
            return "Can you elaborate a little more on that?"
    except:
        e = sys.exc_info()[0]
        return "Oh. What do you mean?"

    #if 'sad' in text:
    #    return 'Cheer up! God is with you (Joshua 1:9)'

    #return "Don't worry. Jesus loves you"

