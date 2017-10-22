from collections import defaultdict
import random

allVerses = defaultdict(list)
confThreshEncourage = 20
confThreshVerse = 50

# creating class
class VerseObj:

    def __init__(self,book,chap,startV,endV):
        self.book = book
        self.chap = chap
        self.startV = startV
        self.endV = endV
    
    def getVerse(emotionNum):
        return verses[emotionNum]

    def __repr__(self):
        return str(self)

    def __str__(self):
        if self.startV != self.endV:
            return self.book + ' ' + str(self.chap) + ':' + str(self.startV) + '-' + str(self.endV)
        else:
            return self.book + ' ' + str(self.chap) + ':' + str(self.startV)

import requests
import json

# reads in the verses in the text file
def init():
    
    #allVerses = defaultdict(list)
    
    verseFile = open("Emotion_Verse_List.txt","r")

    # the first line is the number of emotions
    numEmotions = verseFile.readline()
    
    for i in range(int(numEmotions)):

        emotion = verseFile.readline()        
        verseCount = verseFile.readline()
 #       print(emotion)
 #       print(verseCount)

        actualCount = 0
        for j in range(int(verseCount)):
            
            book, chap, startV, endV = verseFile.readline().strip().split(',')
            if chap == 'Psalm':
                chap == 'Psalms'
            
            allVerses[i + 1].append(VerseObj(book, chap, startV, endV))
            actualCount += 1
            
 #   print(str(allVerses))

    from pprint import pprint
    book = "Psalms"
    chapter = 10
    verse = 4
    
    verSe = "Psalms 10:4-10" #will get all the verses, but haven't fixed the printing
    
    reference = '{} {}:{}'.format(book, chapter, verse)

    bible_response = requests.get('http://getbible.net/json?passage=' + reference)
    bible_obj = json.loads(bible_response.text[1:-2])
 #   pprint(bible_obj)

    verse = bible_obj['book'][0]['chapter'][str(verse)]['verse'].strip()#need to be fixed
 #   pprint(verse)
 #   print(verse)
    

    
    verseFile.close()

    return verse

message = init()
print(allVerses)

def getVerse(emotionNum):
    verses = allVerses[emotionNum]
    return verses[random.randint(0, len(verses)-1)]

def getEncouragement():
  positiveMessages = ["I hope you have a great day!", "Have a beautiful day, friend!","You can do whatever you set your mind to!", "Enjoy the rest of your day!"]
  ranGen = random.randint(0,len(positiveMessages)-1)
  return positiveMessages[ranGen] + " " + getVerse(7)


def giveVerse():
  givingVerse = ["Here is something that might make your day: ", "I think that this might be helpful: ", "I hope that you find this verse helpful: ", "Here is something that may encourage you: ", "I think this may help you with what you're struggling with: ", " Here's something that may help you: ", "I hope this may be helpful: ","This may be helpful: ", "Here's something that may help you think this through: "]
  ranGen = random.randint(0,len(givingVerse))
  return givingVerse[ranGen]

print(str(giveVerse()), str(getVerse(1)),"\n")
print(message)

def getResponse(emotion, confidence):
  print(emotion, confidence)
  
  if (confidence < confThreshEncourage):
    return getEncouragement()
  print('past the first check')
  #if (confidence < confThreshVerse):
  print('before greeting')
  greeting = giveVerse()
  print('greeting', greeting)
  verse = getVerse(emotion)
  print(greeting, verse)
  return greeting + verse
  
""" 
print(getResponse(1, 19))
"""
   

