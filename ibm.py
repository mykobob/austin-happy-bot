import json, os
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    Features

def call_ibm_watson(text):
    username = os.environ['BLUEMIX_USERNAME']
    password = os.environ['BLUEMIX_PASSWORD']
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2017-02-27',
        username=os.environ['BLUEMIX_USERNAME'],
        password=os.environ['BLUEMIX_PASSWORD'])
    
    response = natural_language_understanding.analyze(
        text=text,
        features=[
          Features.Entities(
            emotion=True,
            sentiment=True,
            limit=2
          ),
          Features.Keywords(
            emotion=True,
            sentiment=True,
            limit=2
          )
        ])
    
    return json.loads(response)
