#!/usr/bin/python3

import cv2

#starting camera
cap=cv2.VideoCapture(0)

while cap.isOpened():
    status,frame=cap.read()
    #converting image frame into gray scale
    grayimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    print(frame.shape)
    #line
    cv2.line(frame,(0,0),(200,300),(0,255,0),3)
    #rectangle
    cv2.rectangle(frame,(150,150),(450,450),(0,0,255),2)
    #circle
    cv2.circle(frame,(200,300),100,(13,44,123),2)
    #text writing
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'Hello',(100,100),font,2,(0,2,55),2,cv2.LINE_AA)
    cv2.imshow('live',frame)
    cv2.imshow('livegray',grayimg)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break
    #cv2.waitKey(0)

#cv2.destroyWindow('live')
cv2.destroyAllWindows()  #this will destroy all windows
# to close camera
cap.release()
