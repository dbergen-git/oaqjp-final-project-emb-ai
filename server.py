
# import Flask class
from flask import Flask, request, render_template

# import the emotion_detector function
from EmotionDetection.emotion_detection import emotion_detector

# create an instance of the Flask class
app = Flask(__name__)


# define the route for the emotionDetector
@app.route("/emotionDetector")
def analyze_emotion_route():
    textToAnalyze = str(request.args.get("textToAnalyze"))

    # analyze text - return dict of emotion(s) + score
    emotion_dict = emotion_detector(textToAnalyze)

    # format str opertions - into the needed string
    dominant_emotion = emotion_dict["dominant_emotion"]

    # error handling: test to determine if dominant_emotion is None
    # if so - then inform user of incorrect text + try again
    if dominant_emotion is None:        
         formatted_result = "Invalid text! Please try again!"

         return formatted_result

    # error handling: case where dominant_emotion is NOT None
    else:        
        # prepare the emotion values - exclude the dominant emotion
        # using list comprehension - generate the formatted list - as '<emotion>': value
        emotions = [f"'{k}': {v}" for k, v in emotion_dict.items() if k != "dominant_emotion"]

        # join the emotions with commas and the last two emotions separated by 'and'
        emotions_str = ', '.join(emotions[:-1]) + f" and {emotions[-1]}"

        # format the final string
        formatted_result = (f"For the given statement, the system response is {emotions_str}. "
                            f"The dominant emotion is {dominant_emotion}.")                        

        return formatted_result


@app.route("/")
def render_index_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5001)



