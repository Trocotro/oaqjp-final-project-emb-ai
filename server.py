from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
#Init flask
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    #Get the parameter sent by the request
    my_text_to_analize = request.args.get('textToAnalyze')
    my_analysis = emotion_detector(my_text_to_analize)
    #Extract each value from Dictionary in a variable
    reply = "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, \
    'joy': {} and 'sadness': {}. The dominant emotion is <b>{}</b>.".format(my_analysis['anger'],\
    my_analysis['disgust'],my_analysis['fear'],my_analysis['joy'],my_analysis['sadness'],\
    my_analysis["dominant_emotion"])
    return reply
 
@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    #Run flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)