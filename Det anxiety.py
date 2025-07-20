!pip install deepface
import cv2
from deepface import DeepFace

def detect_anxiety_from_face(image_path):
    try:
        # Analyze the image using DeepFace
        result = DeepFace.analyze(image_path, actions=['emotion'])

        # Access the dominant emotion
        dominant_emotion = result[0]['dominant_emotion']

        # Check if the dominant emotion is indicative of anxiety
        anxiety_labels = ['fear']
        is_anxious = any(label in dominant_emotion.lower() for label in anxiety_labels)

        # Return the result
        return is_anxious, dominant_emotion

    except Exception as e:
        print(f"Error: {str(e)}")
        return None, None

# Provide the path to the image you want to analyze
image_path = '/content/photo.jpg'

# Detect anxiety in the image
is_anxious, dominant_emotion = detect_anxiety_from_face(image_path)

# Print the result
if is_anxious is not None:
    if is_anxious:
        print(f"The person is showing signs of anxiety. Dominant emotion: {dominant_emotion}")
    else:
        print(f"The person is not showing signs of anxiety. Dominant emotion: {dominant_emotion}")
