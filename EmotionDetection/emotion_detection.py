import requests
import json

def emotion_detector(text_to_analyze):
    url ='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=input_json, headers=headers)
    status_code = response.status_code

    emotion_scores = {}
    
    response = requests.post(url, headers=headers, json=input_json)
    response_data = response.json()
    status_code = response.status_code
    
    if status_code == 200:
        emotion_scores = response_data['emotionPredictions'][0]['emotion']
        dominant = max(emotion_scores.items(), key=lambda x: x[1])[0]
        emotion_scores['dominant_emotion'] = dominant
    
    if status_code == 400:
        emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']
        for emotion in emotions:
            emotion_scores[emotion] = None
            
    return emotion_scores