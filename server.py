
# import Flask class
from flask import Flask, request, render_template

# import the emotion_detector function
from EmotionDetection.emotion_detection import emotion_detector

# create an instance of the Flask class
app = Flask(__name__)



# define the route for the emotionDetector
@app.route("/emotionDetector")
def analyze_emotion():
    textToAnalyze = str(request.args.get("textToAnalyze"))

    result = emotion_detector(textToAnalyze)
    





@app.route("/")
def render_index_page():
    return render_template("index.html")

in __name__ == "__main__":
    app.run(host="localhost", port=5000)



