# Face Recognition Attendance System

## Project Overview

The **Face Recognition Attendance System** is a Python-based application that automatically identifies students using face recognition and records their attendance.

The system captures the student's face through a webcam and compares it with the pre-stored student images available in the `Student_Dataset` folder. When a matching face is detected, the student's roll number is identified and the attendance time is recorded.

The system also calculates the approximate amount of time each student was present in the class and generates the final attendance result.

---

## Features

* Face detection using a webcam
* Face recognition using stored student images
* Automatic student identification using roll numbers
* Attendance logging with time
* Voice greeting when a student is detected
* Configurable class duration
* Configurable minimum attendance duration
* Generates attendance result based on student presence
* Prevents duplicate voice greetings for the same student during a session

---

## Technologies Used

* **Python**
* **OpenCV (`cv2`)** – Used for webcam access, image processing, face detection visualization, and displaying the video.
* **NumPy** – Used for numerical operations and face-distance comparison.
* **face_recognition** – Used to generate face encodings and compare faces.
* **OS** – Used for reading student image files and working with folders.
* **pyttsx3** – Used for voice output.
* **datetime** – Used to record attendance time.
* **CSV files** – Used to store attendance logs and final results.

---

## Project Structure

```text
Face-Recognition-Attendance/
│
├── main.py
│
├── Student_Dataset/
│   ├── 101.jpg
│   ├── 102.jpg
│   ├── 103.jpg
│   └── ...
│
├── Attendance_Logs/
│   ├── 101.csv
│   ├── 102.csv
│   └── ...
│
├── result.csv
│
└── README.md
```

### Folder Description

**Student_Dataset/**
Contains the stored student photographs. The filename is used as the student's roll number.

Example:

```text
101.jpg
102.jpg
103.jpg
```

**Attendance_Logs/**
Contains individual attendance log files for students identified by the system.

**result.csv**
Stores the final attendance result, including the approximate duration for which each student attended the class.

**main.py**
Contains the main Python application code.

---

## How the System Works

### 1. Enter Class Details

When the application starts, it asks the user to enter:

* Class duration in minutes
* Minimum time a student should be present in the class

Example:

```text
Enter the duration of the class in Minutes: 60
Enter the time duration in minutes for which student have to present in the class: 45
```

The entered values are converted from minutes into seconds for processing.

---

### 2. Load Student Images

The application reads the images from the `Student_Dataset` folder.

The filename is used as the student's roll number.

For example:

```text
Student_Dataset/
├── 101.jpg
├── 102.jpg
└── 103.jpg
```

The system identifies these students as:

```text
101
102
103
```

---

### 3. Generate Face Encodings

The `face_recognition` library is used to generate a numerical representation called a **face encoding** for each student's image.

The encoding represents important facial features and is later used for comparison with the live webcam image.

---

### 4. Capture Live Video

The application opens the computer's webcam using OpenCV.

```python
vid = cv2.VideoCapture(0)
```

The webcam continuously captures frames while the class is in progress.

---

### 5. Detect and Recognize Faces

For every captured frame:

1. The frame is resized to improve processing speed.
2. Faces are detected.
3. Face encodings are generated for detected faces.
4. The live face encoding is compared with the stored student encodings.
5. The closest matching face is identified.

When a match is found, the student's roll number is displayed on the screen.

---

### 6. Mark Attendance

When a student is recognized, the `markattendance()` function records the student's roll number and current time.

Example:

```text
101,10:15:23
101,10:15:24
101,10:15:25
```

The system also provides a voice greeting when the student is detected for the first time during the session.

Example:

```text
Welcome to class 101
```

---

### 7. Calculate Attendance Duration

After the class duration is completed, the system reads the attendance log files.

It counts the recorded attendance entries and calculates the approximate amount of time the student was present.

The calculated duration is then compared with the minimum required attendance duration entered at the beginning.

---

### 8. Generate Final Result

If the student's calculated attendance duration meets the required duration, the student is added to `result.csv`.

Example:

```text
101 have attended the class for 47.0 minutes.
```

---

## Installation

Make sure Python is installed on your system.

Install the required Python libraries:

```bash
pip install opencv-python
pip install numpy
pip install face-recognition
pip install pyttsx3
```

---

## How to Run

### Step 1: Create the Required Folders

Create the following folders in the project directory:

```text
Student_Dataset
Attendance_Logs
```

### Step 2: Add Student Images

Place student photographs inside:

```text
Student_Dataset/
```

Use the student's roll number as the image filename.

Example:

```text
Student_Dataset/
├── 101.jpg
├── 102.jpg
└── 103.jpg
```

### Step 3: Run the Application

Open the terminal in the project directory and run:

```bash
python main.py
```

### Step 4: Enter Class Details

Enter the class duration and required attendance duration when prompted.

### Step 5: Start Face Recognition

The webcam will open and the system will recognize students automatically.

### Step 6: View the Result

After the class duration is completed, check:

result.csv

for the final attendance result.

Main Python Modules
OpenCV

OpenCV is used for:

Accessing the webcam
Capturing video frames
Resizing images
Drawing rectangles around detected faces
Displaying the live video

Example:

vid = cv2.VideoCapture(0)
NumPy

NumPy is used for numerical operations and finding the closest face match.

matchIndex = np.argmin(facedis)
face_recognition

The face_recognition library is responsible for:

Detecting faces
Generating face encodings
Comparing live faces with stored faces
Calculating face distance
pyttsx3

pyttsx3 provides voice output when a student is recognized.

Input

The system requires:

Student photographs
Student roll numbers through image filenames
Class duration
Required minimum attendance duration
Webcam access
Output

The system produces:

Recognized student roll number on the webcam screen
Individual attendance logs in Attendance_Logs/
Final attendance information in result.csv
Voice greeting for recognized students
Important Notes
The student image should clearly show the student's face.
Good lighting improves recognition accuracy.
The webcam must be connected and accessible.
The Student_Dataset folder must exist before running the application.
The Attendance_Logs folder must exist before attendance is recorded.
Student image filenames should represent the corresponding roll numbers.
Future Enhancements

The project can be enhanced by adding:

Database integration using MySQL or Oracle
Web-based attendance dashboard
Admin login and authentication
Student registration functionality
Attendance reports and analytics
Email notifications
Improved attendance calculation
Multiple classroom support
Cloud deployment
Conclusion

The Face Recognition Attendance System automates the traditional attendance process by using computer vision and face recognition technology. It identifies students through a webcam, records their attendance timestamps, calculates their approximate presence duration, and generates a final attendance result automatically.
