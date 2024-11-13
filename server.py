"""
This is the main file where we define all routes and 
principal logical for the application.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

"""
Define a route to detect emotion basing on a given statement
"""
@app.route("/emotionDetector")
def detect_emotion():
    """
    input: a string indicating a statement
    output: a statement 
            either trying again or the actually analysed result
    """
    text_to_analyze = request.args.get('textToAnalyze')
    dominant_emotion = emotion_detector(text_to_analyze)
    message = ""
    if dominant_emotion["dominant_emotion"] is None:
        message = "Invalid text! Please try again."
    else:
        message = "The given text has been identified as " + dominant_emotion

    return message


@app.route("/")
def render_index_page():
    """ An only action: rendering the index.html page """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
