import requests, json
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputjson = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = inputjson, headers = header)
    formated_response = json.loads(response.text)
    if response.status_code == 200:
        #Get the emotions list
        emotions = formated_response['emotionPredictions'][0]['emotion']
        #we add the dominant emotion with value equal to the emotion with higher value
        emotions['dominant_emotion']= max(emotions,key=emotions.get)
        return emotions
    elif response.status_code == 400:
        empty_response = {"anger" : None, "disgust" : None, "fear" : None, "joy" : None, "sadness" : None, "dominant_emotion" :None} 
        return empty_response       