#!/usr/bin/python3

import cv2

#starting camera
cap=cv2.VideoCapture(0)

while cap.isOpened():
	status,frame=cap.read()

	cv2.imshow('live',frame)
#	if cv2.waitkey(10) & 0xff == ord('q'):
#		break
cv2.waitKey(0)
#cv2.destroyWindow('live')
cv2.destroyAllWindows()  #this will destroy all windows
# to close camera
cap.release()
