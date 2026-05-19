
import requests
import json

def emotion_detector(text_to_analyze):
    """
    analyzes text emotion - using Watson Emotion Predict
    function of the Watson NLP library

    """

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": { "text": text_to_analyze }}    
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url, json = myobj, headers=headers)

    return response.text


