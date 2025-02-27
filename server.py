"""Module for managing the requests from Enotion detector webpages."""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
#Init flask
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """Function to call module emotion_detector and send output to web page"""
    #Get the parameter sent by the request
    my_text_to_analize = request.args.get('textToAnalyze')
    my_analysis = emotion_detector(my_text_to_analize)
    #if no text introduced
    if my_analysis["dominant_emotion"] is None:
        return "<b>Invalid text! Please try again!.</b>"
    # Otherwise Extract each value from Dictionary in a variable
    reply = f"For the given statement, the system response is \
    'anger': {my_analysis['anger']}, 'disgust': {my_analysis['disgust']}, 'fear': {my_analysis['fear']}, \
    'joy': {my_analysis['joy']} and 'sadness': {my_analysis['sadness']}. The dominant emotion \
    is <b>{my_analysis['dominant_emotion']}</b>."
    return reply

@app.route("/")
def render_index_page():
    """Function to render initial  page to Web Application"""
    return render_template('index.html')

if __name__ == "__main__":
    #Run flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
