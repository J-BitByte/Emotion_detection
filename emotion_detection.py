import requests
import json

def emotion_detection(text_to_analyse):
    # URL for the emotion detection WatsonNLP library
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # payload created for the text to be analysed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Headers set with the required model ID for the API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(URL, json=myobj, headers=headers)

    return response.text
