

# importing required modules for the project

import cv2
import numpy as np
import face_recognition as face_rec
import os
import sys
import time
import pyttsx3 as textspeech
from datetime import datetime


# Initializing The pyttsx3 Module
engine = textspeech.init()



# Taking Required Fields For the class
print("Please Enter the Following Fields. They all must be Positive and Non Decimal.")
try:
    classduration = int(input("Enter the duration of the class in Minutes: "))
    timeduration = int(input("Enter the time duration in minutes for which student have to present in the class: "))
    if classduration < 0 or timeduration < 0:
        raise ValueError("Invalid value. Please enter a valid value.")
except ValueError:
    print("Invalid value. Please enter a valid value.")
    sys.exit(1)


# converting class duration and time duration in seconds
classduration = classduration * 60
timeduration = timeduration * 60


def resize(img, size):
    width = int(img.shape[1]*size)
    height = int(img.shape[0] * size)
    dimension = (width, height)
    return cv2.resize(img, dimension, interpolation= cv2.INTER_AREA)


path = 'Student_Dataset'
studentImg = []
studentName = []
myList = os.listdir(path)
for cl in myList:
    curimg = cv2.imread(f'{path}/{cl}')
    studentImg.append(curimg)
    studentName.append(os.path.splitext(cl)[0])


# def findencoding(images):
#     imgEncodings = []
#     for img in images :
#         img = resize(img, 0.50)
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         encodeimg = face_rec.face_encodings(img)[0]
#         imgEncodings.append(encodeimg)
#     return imgEncodings


def findencoding(images):
    imgEncodings = []

    for img in images:
        img = resize(img, 0.50)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        encodings = face_rec.face_encodings(img)

        if len(encodings) > 0:
            imgEncodings.append(encodings[0])
        else:
            print("WARNING: No face detected in one of the student images.")

    return imgEncodings


presentrollnolist = []


def markattendance(rollno):
    with open(f'Attendance_Logs/{rollno}.csv', 'a') as f:
        if rollno not in presentrollnolist:
            statment = str('welcome to class' + rollno)
            engine.say(statment)
            engine.runAndWait()
            presentrollnolist.append(rollno)
            now = datetime.now()
            timestr = now.strftime('%H:%M:%S')
            f.write(f'{rollno},{timestr}\n')
        else:
            now = datetime.now()
            timestr = now.strftime('%H:%M:%S')
            f.write(f'{rollno},{timestr}\n')


EncodeList = findencoding(studentImg)


vid = cv2.VideoCapture(0)
start_time = time.time()
while True:
    elapsed_time = time.time() - start_time
    if elapsed_time >= classduration:
        break
    success, frame = vid.read()
    Smaller_frames = cv2.resize(frame, (0,0), None, 0.25, 0.25)

    facesInFrame = face_rec.face_locations(Smaller_frames)
    encodeFacesInFrame = face_rec.face_encodings(Smaller_frames, facesInFrame)

    for encodeFace, faceloc in zip(encodeFacesInFrame, facesInFrame):
        matches = face_rec.compare_faces(EncodeList, encodeFace)
        facedis = face_rec.face_distance(EncodeList, encodeFace)
        matchIndex = np.argmin(facedis)

        if matches[matchIndex]:
            rollno = studentName[matchIndex].upper()
            y1, x2, y2, x1 = faceloc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
            cv2.rectangle(frame, (x1, y2-25), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, rollno, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markattendance(rollno)

    cv2.imshow('video', frame)
    cv2.waitKey(1)
vid.release()
cv2.destroyAllWindows()


# Set the path to the folder
folder_path = 'Attendance_Logs'

# Iterate over all the files and directories in the folder
for item_name in os.listdir(folder_path):
    # Construct the full path to the item
    item_path = os.path.join(folder_path, item_name)

    # Check if the item is a file
    if os.path.isfile(item_path):
        print(f"Processing file: {item_name}")
        with open(f'{item_path}', 'r') as f:
            lines = f.readlines()
            student_log = []
            for line in lines:
                if line not in student_log:
                    student_log.append(line)
            print(len(student_log))
            noofsecondsstudentpresent = len(student_log) + ((classduration/100) * 7) # hack to increase the accuracy
            if noofsecondsstudentpresent >= classduration:
                noofsecondsstudentpresent = len(student_log)
            noofminutesstudentpresent = noofsecondsstudentpresent / 60
            if noofsecondsstudentpresent >= timeduration:
                with open('result.csv', 'a') as f1:
                    student_rollno = item_name[:-4]
                    f1.write(f'{student_rollno} have attended the class for {noofminutesstudentpresent} minutes.')
    else:
        print(f"Skipping unknown item: {item_name}")
