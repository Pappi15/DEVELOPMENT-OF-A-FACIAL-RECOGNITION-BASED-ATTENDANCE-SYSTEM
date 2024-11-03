import cv2
from simple_facerec import SimpleFacerec
import sqlite3 as sl
import time 

def cctv():
    # Connect to the database
    con = sl.connect('data.db')

    # Initialize SimpleFacerec for face encoding
    sfr = SimpleFacerec()
    sfr.load_encoding_images("images/")

    # Initialize the camera
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Detect faces
        face_locations, ids = sfr.detect_known_faces(frame)
        for face_loc, id in zip(face_locations, ids):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
            name = ""
            if id == "Unknown":
                color = (0, 0, 200)
                name = "Unknown"
            else:
                color = (0, 200, 0)
                # Update user location and time in the database
                query = "UPDATE USER SET location=?, time=? WHERE id=?"
                data = ('COLLEGE 1', time.time(), id)
                with con:
                    con.execute(query, data)
                # Retrieve user's name from the database
                with con:
                    data = con.execute("SELECT name FROM USER WHERE id=?", (id,))
                    for row in data:
                        name = row[0]
            print(name)
            # Display the name and draw a rectangle around the face
            cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, color, 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 4)

        # Display the resulting frame
        cv2.imshow("Frame", frame)

        # Exit on pressing the ESC key
        key = cv2.waitKey(1)
        if key == 27:
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

#cctv()
