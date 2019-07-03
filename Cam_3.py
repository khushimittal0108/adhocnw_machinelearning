#!/usr/bin/python3

import cv2

#start camera 
cap=cv2.VideoCapture(0)

#status of camera
while cap.isOpened():
    status,frame=cap.read()
    redimg=cv2.inRange(frame,(0,0,0),(0,0,255))
    cv2.imshow('loveredcolor',redimg)
    if cv2.waitKey(10) & 0xff==ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
