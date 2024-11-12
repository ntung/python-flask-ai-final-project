import unittest

from EmotionDetection.emotion_detection import emotion_detector as ed

test_cases = {
    "joy": "I am glad this happened",
    "anger": "I am really mad about this",
    "disgust": "I feel disgusted just hearing this",
    "sadness": "I am so sad about this",
    "fear": "I am really afraid that this will happen"
}

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detector(self):
        for dominant, statement in test_cases.items():
            r = ed(statement)
            self.assertEqual(r["dominant_emotion"], dominant)


if __name__ == "__main__":
    unittest.main()
