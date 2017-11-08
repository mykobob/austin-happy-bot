from collections import defaultdict
import random
import json
import pprint

import requests

pp = pprint.PrettyPrinter(indent=4)

conf_thresh_encourage = 20
confThreshVerse = 50

class Verse:

    def __init__(self,book,chap,startV,endV):
        self.book = book
        self.chap = chap
        self.startV = startV
        self.endV = endV
    
    def getVerse(emotion_num):
        return verses[emotion_num]

    def verse_range(self):
        start = int(self.startV)
        end = int(self.endV)
        for i in range(start, end + 1):
            yield str(i)

    def __repr__(self):
        return str(self)

    def __str__(self):
        if self.startV != self.endV:
            return self.book + ' ' + str(self.chap) + ':' + str(self.startV) + '-' + str(self.endV)
        else:
            return self.book + ' ' + str(self.chap) + ':' + str(self.startV)

class VerseDb:
    def __init__(self):
        self.all_verses = defaultdict(list)
        
        with open('Emotion_Verse_List.txt','r') as verse_file:
            num_emotions = int(verse_file.readline())
            
            for i in range(num_emotions):
    
                emotion = verse_file.readline()        
                verse_count = int(verse_file.readline())
    
                actualCount = 0
                for j in range(verse_count):
                    
                    book, chap, startV, endV = verse_file.readline().strip().split(',')
                    if chap == 'Psalm':
                        chap = 'Psalms'
                    
                    self.all_verses[i + 1].append(Verse(book, chap, startV, endV))
                    actualCount += 1
    
    def get_verse_text(self, verse):
        verse_ref = str(verse) #will get all the verses, but haven't fixed the printing
        
        bible_response = requests.get('http://getbible.net/json?passage=' + verse_ref)
        bible_obj = json.loads(bible_response.text[1:-2])
    
        verse_texts = bible_obj['book'][0]['chapter']

        return ' '.join(verse_texts[i]['verse'].strip() for i in verse.verse_range())
    
    def get_verse(self, emotion_num):
        verses = self.all_verses[emotion_num]
        return verses[random.randint(0, len(verses)-1)]
    
    def get_encouragement():
      positive_messages = ["I hope you have a great day!", "Have a beautiful day, friend!","You can do whatever you set your mind to!", "Enjoy the rest of your day!"]
      ranGen = random.randint(0,len(positive_messages)-1)
      return positive_messages[ranGen] + " " + getVerse(7)
    
    
    def get_greeting():
      greetings = ["Here is something that might make your day: ", "I think that this might be helpful: ", "I hope that you find this verse helpful: ", "Here is something that may encourage you: ", "I think this may help you with what you're struggling with: ", " Here's something that may help you: ", "I hope this may be helpful: ","This may be helpful: ", "Here's something that may help you think this through: "]
      ranGen = random.randint(0,len(greetings) - 1)
      return greetings[ranGen]
    
    def get_response(emotion, confidence):
      print(emotion, confidence)
      
      if (confidence < conf_thresh_encourage):
        return get_encouragement()
      greeting = get_gretting()
      verse = get_verse(emotion)
      text = get_verse_text(verse)
    
      return "{}{} '{}'".format(greeting, str(verse), text)
      
    """ 
    print(get_response(1, 19))
    """
   
if __name__ == '__main__':
    verse = Verse('John', '3', '16', '17')
    print(VerseDb().get_verse_text(verse))
