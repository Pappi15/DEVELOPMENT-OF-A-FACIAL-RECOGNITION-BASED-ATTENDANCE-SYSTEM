# Assuming you have a dataset of facial images for training
# You can use this Python code snippet to capture facial recognition data

import cv2
import os

# Initialize the OpenCV face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Create a directory to save captured images
output_dir = "captured_faces"
os.makedirs(output_dir, exist_ok=True)

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Set the number of images to capture
num_images_to_capture = 7
captured_images = 0

while captured_images < num_images_to_capture:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # If a face is detected, save the face image
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            face_image = frame[y:y+h, x:x+w]
            face_filename = os.path.join(output_dir, f"face_{captured_images}.jpg")
            cv2.imwrite(face_filename, face_image)
            captured_images += 1
            print(f"Captured image {captured_images}/{num_images_to_capture}")

    # Display the frame
    cv2.imshow('Capture Faces', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()

print(f"Captured {captured_images} face images. Saved in {output_dir}")

