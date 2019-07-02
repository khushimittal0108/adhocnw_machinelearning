#!/usr/bin/python3

import cv2

#start camera 
cap=cv2.VideoCapture(2)

#status of camera
while cap.isOpened():
 	status,frame=cap.read()
	redimg=cv.inRange(frame,(0,0,0),(0,0,255))
	cv.imshow('loveredcolor',redimg)

	if cv2.waitkey(10) & 0xff==ord('q'):
		break

cv2.DestroyAllWindows()
cap.release()
