
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

    # error handling - manage blank text entries.  
    # if status_code = 400 then return empty emotion_dict
    if response.status_code == 400:

        # return an empty dict - all emotions have None as their values
        emotion_dict = {"anger": None, "disgust": None,
                        "fear": None, "joy": None,
                        "sadness": None, "dominant_emotion": None}
        
        return emotion_dict
    
    # case where the text entry is valid - process response
    else:
        # format the response object
        formatted_response = response.json()

        # extract the emotion dict
        emotion_dict = formatted_response["emotionPredictions"][0]["emotion"]

        # find the dominant emotion - the key with the highest value
        dominant_emotion = max(emotion_dict, key = emotion_dict.get)

        # add the dominant emotion to the emotion_dict
        emotion_dict['dominant_emotion'] = dominant_emotion
    
        return emotion_dict






