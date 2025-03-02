'''Deploy a Flask application that will allow a user to provide
a text string which will then be analyzed to determine which emotion amongst a set of 5
is the most likely emotion being conveyed by the given text.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """Analyze the emotion of the provided text."""
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Call the emotion detection function
    response = emotion_detector(text_to_analyze)
    
    anger = response.get('anger', 0)
    disgust = response.get('disgust', 0)
    fear = response.get('fear', 0)
    joy = response.get('joy', 0)
    sadness = response.get('sadness', 0)
    dominant_emotion = response.get('dominant_emotion', 0)
    
    if dominant_emotion == None:
        return "Invalid text! Please try again!"
    
    return (
        f"For the given text = {text_to_analyze}, the system response is: \n"
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy}, 'sadness': {sadness}, the dominant emotion is: {dominant_emotion}"
    )
@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
