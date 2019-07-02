#!/usr/bin/python3

import cv2

#starting camera
cap=cv2.VideoCapture(2)

tp1=cap.read()[1]	#take 1
tp2=cap.read()[1]	#take 2
tp3=cap.read()[1]	#take 3

#to make more perfect
gray1=cv2.cvtColor(tp1,cv2.COLOR_BGR2GRAY)  # converting to gray
gray2=cv2.cvtColor(tp2,cv2.COLOR_BGR2GRAY)  # converting to gray
gray3=cv2.cvtColor(tp3,cv2.COLOR_BGR2GRAY)  # converting to gray

#now creating image diff
def img_diff(x,y,z):
	#diff b/w x,y --gray1,gray2 --d1
	d1=cv2.absdiff(x,y)
	#diff b/w x,y --gray2,gray3 --d2
	d2=cv2.absdiff(y,z)
	#absdiff d1-d2
	finalimg=cv2.bitwise_and(d1,d2)
	return finalimg

#now apply function
while cap.isOpened():
	status,frame=cap.read() #continue image taker
	motioning=img_diff(gray1,gray2,gray3)
	#replacing image frame
	gray1=gray2
	gray2=gray3
	gray3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #passing live img to gray3
	cv2.imshow('live',frame)
	cv2.imshow('motion',motioning) #motion detect
	if cv2.waitKey(10) & 0vff==ord('q'):
		break
cv2.destroyAllWindows()
cv2.release()
