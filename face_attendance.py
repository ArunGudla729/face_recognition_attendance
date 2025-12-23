import cv2
import face_recognition
import os
import csv
from datetime import datetime

# Path to known faces folder
KNOWN_FACES_DIR = "known_faces"

# Attendance file
ATTENDANCE_FILE = "attendance.csv"

# Load known faces
known_face_encodings = []
known_face_names = []

for file_name in os.listdir(KNOWN_FACES_DIR):
    image_path = os.path.join(KNOWN_FACES_DIR, file_name)
    image = face_recognition.load_image_file(image_path)
    encoding = face_recognition.face_encodings(image)

    if encoding:
        known_face_encodings.append(encoding[0])
        known_face_names.append(os.path.splitext(file_name)[0])

# Mark attendance
def mark_attendance(name):
    with open(ATTENDANCE_FILE, "a+", newline="") as file:
        file.seek(0)
        existing_names = [line.split(",")[0] for line in file.readlines()]
        if name not in existing_names:
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer = csv.writer(file)
            writer.writerow([name, time_now])

# Start webcam
video_capture = cv2.VideoCapture(0)

print("Press 'q' to quit")

while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            match_index = matches.index(True)
            name = known_face_names[match_index]
            mark_attendance(name)

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(
            frame,
            name,
            (left, top - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2
        )

    cv2.imshow("Face Recognition Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
