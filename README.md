# Face Recognition Attendance System

## Overview
This project is a real-time Face Recognition Attendance System built using Python.
It captures video from a webcam, detects and recognizes faces, and automatically
records attendance with date and time.

## Tech Stack
- Python
- OpenCV
- face_recognition
- NumPy
- CSV file handling

## Project Structure
face_recognition_attendance/
├── known_faces/
│ ├── Arun.jpg
│ ├── Person2.png
├── attendance.csv
└── face_attendance.py

## How It Works
- Known face images are stored in the `known_faces` folder
- Face encodings are generated from these images
- Webcam input is processed in real time
- Detected faces are matched against known encodings
- Attendance is logged only once per person with timestamp

## Setup Instructions
1. Clone the repository
2. Install required libraries:
   pip install opencv-python face-recognition numpy
3. Add clear face images to the `known_faces` folder
4. Run the script:
   python face_attendance.py

## Output
- Webcam window showing detected and recognized faces
- Attendance recorded in `attendance.csv` with timestamp

## Notes
- Project runs locally due to webcam and system-level dependencies
- PNG and JPG image formats are supported
- Each image should contain only one face

## Learning Outcomes
- Real-time computer vision using OpenCV
- Face recognition using facial encodings
- File handling and data logging in Python
- Practical application of AI in real-world scenarios

