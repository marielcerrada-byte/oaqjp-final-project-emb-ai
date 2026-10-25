import json
import requests

def emotion_detector(text_to_analyze):
    """
    Analiza el texto proporcionado y devuelve un diccionario con los puntajes de las emociones
    (anger, disgust, fear, joy, sadness) y la emoción dominante.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Realizar la solicitud POST a la API de Watson NLP
    response = requests.post(url, json=input_json, headers=headers)
    
    # 1. Convertir la respuesta de texto a un diccionario de Python
    response_dict = json.loads(response.text)
    
    # 2 y 3. Extraer el diccionario de emociones
    # La estructura de Watson NLP para esta respuesta es:
    # response_dict['emotionPredictions'][0]['emotion']
    emotions = response_dict['emotionPredictions'][0]['emotion']
    
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)
    
    # 4. Encontrar la emoción dominante (la que tiene el puntaje más alto)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # 5. Devolver el diccionario con el formato solicitado
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

