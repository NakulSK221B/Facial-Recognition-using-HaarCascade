import numpy as np
import cv2
from subprocess import call
import time
import os
import glob
import smtplib
import base64
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
print("Setup complete")
#face_cascade_name = cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml'
#face_cascade = cv2.CascadeClassifier()
#if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):
    #print("Error loading xml file")
    #exit(0)

##img=cv2.imread("")
number=0
cam=cv2.VideoCapture("face-demographics-walking-and-pause.mp4")
print("video upload complete")
#cam=cv2.VideoCapture(0)-->for live integrated webcam input(0) and for external webcam(1)
while(True):
    #print("entered while loop")
    try:
        _,img=cam.read()
        grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
        faces=face_cascade.detectMultiScale(grayimg);
        if len(faces)==0:
            print("No faces found")
        else:
            print("No of faces detected: "+str(faces.shape[0]))
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,225,0),1)
            cv2.rectangle(img,(0,img.shape[0]-25),(270,img.shape[0]),(255,255,255),-1)
            cv2.putText(img,"No of faces detected: "+ str(faces.shape[0])+"/1",(0,img.shape[0]-10),cv2.FONT_HERSHEY_TRIPLEX,0.5,(0,0,0),1)
            cv2.imshow('Image with faces',img)
            cv2.imshow('Grey scale',grayimg)
            cv2.waitKey(1)
            number=faces.shape[0]
            # Code Snippet for sending an email when a face is recognised (Not yet resolved)
            # if number>=3:
            #     #print("entered loop")
            #     msg=MIMEMultipart()
            #     time.sleep(1)
            #     msg['Subject']="Security Breach"
            #     body="More than one person detected in the facility"
            #     msg.attach(MIMEText(body,'plain'))
            #     print("Setup complete")
            #     time.sleep(1)
            #     msg.attach(cam)
            #     time.sleep(1)
            #     print("Image attached")
            #     try:
            #         user=""
            #         pwd=""
            #         From="Support Team"
            #         To= ""
            #         serv=smtplib.SMTP("smtp.gmail.com",587)
            #         print("smtp gmail")
            #         serv.ehlo()
            #         print("ehlo")
            #         serv.starttls()
            #         print("starttls")
            #         serv.login(user,pwd)
            #         print("reading email and password")
            #         serv.sendmail(From,To,msg.as_string(1))
            #         print("from")
            #         serv.close()
            #         print("Sent email successfully")
            #     except:
            #         print("Failed to send email")  
    except:
        pass
