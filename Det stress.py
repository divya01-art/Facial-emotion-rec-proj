# MENTAL HEALTH PREDICTION ->

# DETECTION OF STRESS AT FIRST LEVEL

!pip install deepface
import cv2
from deepface import DeepFace

def detect_stress_from_face(image_path):
    try:
        # Analyze the image using DeepFace
        result = DeepFace.analyze(image_path)

        # Access the dominant emotion
        dominant_emotion = result[0]['dominant_emotion']

        # Check if the dominant emotion is indicative of stress
        stress_labels = ['angry', 'fear', 'sad', 'disgust']
        is_stressed = any(label in dominant_emotion.lower() for label in stress_labels)

        # Return the result
        return is_stressed, dominant_emotion

    except Exception as e:
        print(f"Error: {str(e)}")
        return None, None

# Provide the path to the image you want to analyze
image_path = '/content/photo.jpg'

# Detect stress in the image
is_stressed, dominant_emotion = detect_stress_from_face(image_path)

# Print the result
if is_stressed is not None:
    if is_stressed:
        print(f"The person is showing signs of stress. Dominant emotion: {dominant_emotion}")
    else:
        print(f"The person is not showing signs of stress. Dominant emotion: {dominant_emotion}")
