
# import the test package
import unittest

# import the emotion_detector function
from EmotionDetection.emotion_detection import emotion_detector

# define the unit test case(s)

class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector(self):
        # test case for joy
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1.get("dominant_emotion"), "joy")

        # test case for anger
        result_2 = emotion_detector("I am really mad about this")
        self.assertEqual(result_2.get("dominant_emotion"), "anger")

        # test case for disgust
        result_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_3.get("dominant_emotion"), "disgust")        

        # test case for sadness
        result_4 = emotion_detector("I am so sad about this")
        self.assertEqual(result_4.get("dominant_emotion"), "sadness") 

        # test case for fear
        result_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_5.get("dominant_emotion"), "fear")

if __name__ == '__main__':
    unittest.main()
