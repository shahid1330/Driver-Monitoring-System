# # '''This script detects if a person is drowsy or not,using dlib and eye aspect ratio
# # calculations. Uses webcam video feed as input.'''

import cv2
from scipy.spatial import distance
from imutils import face_utils
import numpy as np
import pygame  # For playing sound
import time
import dlib
import tkinter as tk
from threading import Thread

# Initialize Pygame and load music
pygame.mixer.init()
pygame.mixer.music.load("alert.wav")

# Minimum threshold of eye aspect ratio below which alarm is triggered
EYE_ASPECT_RATIO_THRESHOLD = 0.3

# Load face cascade which will be used to draw a rectangle around detected faces.
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Load face detector and predictor, uses dlib shape predictor file
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# Extract indexes of facial landmarks for the left and right eye
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS['left_eye']
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']

# Start webcam video capture
video_capture = cv2.VideoCapture(0)

# Give some time for camera to initialize(not required)
time.sleep(1)

# Initialize variable to track if sound is playing
sound_playing = False

# Initialize a counter for closed eyes
closed_eye_counter = 0

# Initialize a boolean variable to track if the eyes were closed in the previous frame
eyes_closed_prev = False

# Threshold for consecutive frames to consider eyes closed
CLOSED_EYE_THRESHOLD = 3 * 30  # Assuming 30 frames per second

# Function to calculate and return eye aspect ratio
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])

    ear = (A + B) / (2 * C)
    return ear

# Function to start the drowsiness detection
def start_detection():
    global video_capture, closed_eye_counter, sound_playing, eyes_closed_prev

    while True:
        # Read each frame and flip it, and convert to grayscale
        ret, frame = video_capture.read()
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces through haarcascade_frontalface_default.xml
        face_rectangle = face_cascade.detectMultiScale(gray, 1.3, 5)

        # Draw rectangle around each face detected
        for (x, y, w, h) in face_rectangle:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Detect facial points
        faces = detector(gray, 0)
        for face in faces:
            shape = predictor(gray, face)
            shape = face_utils.shape_to_np(shape)

            # Get array of coordinates of leftEye and rightEye
            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]

            # Calculate aspect ratio of both eyes
            leftEyeAspectRatio = eye_aspect_ratio(leftEye)
            rightEyeAspectRatio = eye_aspect_ratio(rightEye)

            eyeAspectRatio = (leftEyeAspectRatio + rightEyeAspectRatio) / 2

            # Use hull to remove convex contour discrepancies and draw eye shape around eyes
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

            # Detect if eye aspect ratio is less than threshold
            if eyeAspectRatio < EYE_ASPECT_RATIO_THRESHOLD:
                # Increment counter for closed eyes
                closed_eye_counter += 1

                # If eyes were closed in the previous frame and continue to be closed,
                # and if the closed eye counter exceeds the threshold, start playing sound
                if eyes_closed_prev and closed_eye_counter >= CLOSED_EYE_THRESHOLD:
                    # If sound is not playing, start playing sound
                    if not sound_playing:
                        pygame.mixer.music.play(-1)
                        sound_playing = True

            else:
                # Reset closed eye counter if eyes are open
                closed_eye_counter = 0

                # If sound is playing, stop playing sound
                if sound_playing:
                    pygame.mixer.music.stop()
                    sound_playing = False

            # Update the boolean variable for eyes closed in the previous frame
            eyes_closed_prev = eyeAspectRatio < EYE_ASPECT_RATIO_THRESHOLD

        # Show video feed
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Finally when video capture is over, release the video capture and destroyAllWindows
    video_capture.release()
    cv2.destroyAllWindows()

# Function to update statistics in GUI
def update_statistics():
    global closed_eye_counter

    while True:
        eye_status_var.set("Eyes Closed" if closed_eye_counter >= CLOSED_EYE_THRESHOLD else "Eyes Open")
        time.sleep(0.1)  # Update statistics every 0.1 second

# Create GUI window
root = tk.Tk()
root.title("Drowsiness Detection System")

# Variable to update eye status
eye_status_var = tk.StringVar()

# Label for displaying eye status
eye_status_label = tk.Label(root, textvariable=eye_status_var, font=("Helvetica", 20))
eye_status_label.pack(pady=20)

# Start detection in a separate thread
detection_thread = Thread(target=start_detection)
detection_thread.start()

# Update statistics in a separate thread
update_thread = Thread(target=update_statistics)
update_thread.start()

# Run GUI
root.mainloop()

