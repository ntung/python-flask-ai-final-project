import json, requests

def emotion_detector(text_to_analyse):
    nothing = {
        "anger": None, 
        "disgust": None, 
        "fear": None, 
        "joy": None, 
        "sadness": None,
        "dominant_emotion": None
    }
    
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, headers=headers, json=input_json)
    if text_to_analyse is None or text_to_analyse == "" or response.status_code == 400:
        return nothing

    # response = requests.post(URL, headers=headers, data=json.dumps(input_json))
    data_json = json.loads(response.text)
    # Predicted Emotion
    pe = data_json["emotionPredictions"][0]["emotion"]
    returned_data = { 
        "anger": pe["anger"], 
        "disgust": pe["disgust"], 
        "fear": pe["fear"], 
        "joy": pe["joy"], 
        "sadness": pe["sadness"]
    }
    dominant = max(returned_data, key=returned_data.get)
    returned_data["dominant_emotion"] = dominant
    return returned_data
    