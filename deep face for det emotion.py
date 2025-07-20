# Installing Deepface Library
!pip3 install deepface

#emotion_detection.py
import cv2
from deepface import DeepFace
import numpy as np  #this will be used later in the process

imgpath = '/content/photo.jpg'
image = cv2.imread(imgpath)

analyze = DeepFace.analyze(image,actions=['emotion'])  #here the first parameter is the image we want to analyze #the second one there is the action
print(analyze)
print()
dominant_emotion = analyze[0]['dominant_emotion']
print(f"Dominant Emotion: {dominant_emotion}")
