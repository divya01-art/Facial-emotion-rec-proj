!pip install deepface
import cv2
from deepface import DeepFace

def detect_depression_from_face(image_path):
    try:
        # Analyze the image using DeepFace
        result = DeepFace.analyze(image_path)

        # Access the dominant emotion
        dominant_emotion = result[0]['dominant_emotion']

        # Check if the dominant emotion is indicative of depression
        depression_labels = ['sad']
        is_depressed = any(label in dominant_emotion.lower() for label in depression_labels)

        # Return the result
        return is_depressed, dominant_emotion

    except Exception as e:
        print(f"Error: {str(e)}")
        return None, None

# Provide the path to the image you want to analyze
image_path = '/content/photo.jpg'

# Detect depression in the image
is_depressed, dominant_emotion = detect_depression_from_face(image_path)!pip install deepface
import cv2
from deepface import DeepFace

def detect_depression_from_face(image_path):
    try:
        # Analyze the image using DeepFace
        result = DeepFace.analyze(image_path)

        # Access the dominant emotion
        dominant_emotion = result[0]['dominant_emotion']

        # Check if the dominant emotion is indicative of depression
        depression_labels = ['sad']
        is_depressed = any(label in dominant_emotion.lower() for label in depression_labels)

        # Return the result
        return is_depressed, dominant_emotion

    except Exception as e:
        print(f"Error: {str(e)}")
        return None, None

# Provide the path to the image you want to analyze
image_path = '/content/photo.jpg'

# Detect depression in the image
is_depressed, dominant_emotion = detect_depression_from_face(image_path)

# Print the result
if is_depressed is not None:
    if is_depressed:
        print(f"The person is showing signs of depression. Dominant emotion: {dominant_emotion}")
    else:
        print(f"The person is not showing signs of depression. Dominant emotion: {dominant_emotion}")
