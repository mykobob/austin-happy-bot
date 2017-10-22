from ibm import call_ibm_watson

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
        response = call_ibm_watson(text)
        print(response)
    except:
        return "Oh. How is that?"
    return response

    if 'sad' in text:
        return 'Cheer up! God is with you (Joshua 1:9)'

    return "Don't worry. Jesus loves you"

