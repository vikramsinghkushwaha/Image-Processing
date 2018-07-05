import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow("Trackbars")

cv2.createTrackbar("L-H","Trackbars",0,179, nothing)
cv2.createTrackbar("L-S","Trackbars",0,255, nothing)
cv2.createTrackbar("L-V","Trackbars",0,255, nothing)
cv2.createTrackbar("U-H","Trackbars",0,179, nothing)
cv2.createTrackbar("U-S","Trackbars",0,255, nothing)
cv2.createTrackbar("U-V","Trackbars",0,255, nothing)
kernel = np.ones((11,11),np.uint8)

while(1):

    _,frame = cap.read()


    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    filtered = cv2.GaussianBlur(hsv,(5,5),0)

    l_h = cv2.getTrackbarPos("L-H","Trackbars")
    l_s = cv2.getTrackbarPos("L-S","Trackbars")
    l_v = cv2.getTrackbarPos("L-V","Trackbars")
    u_h = cv2.getTrackbarPos("U-H","Trackbars")
    u_s = cv2.getTrackbarPos("U-S","Trackbars")
    u_v = cv2.getTrackbarPos("U-V","Trackbars")

    #lower_value = np.array([l_h,l_s,l_v])     Uncomment this to get the visual HSV chooser
    #upper_value = np.array([u_h,u_s,u_v])     Similar as above, uncoment this too
    lower_value = np.array([110,55,55])
    upper_value = np.array([130,255,255])

    mask = cv2.inRange(hsv,lower_value,upper_value)

    median = cv2.medianBlur(mask,15)
    erode = cv2.erode(mask,kernel,iterations = 7)
    dilate = cv2.dilate(mask,kernel,iterations = 7)

    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

    res = cv2.bitwise_and(frame,frame,mask = mask)
    ret,thresh = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)

    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    #cv2.drawContours(frame,contours,-1,(0,255,0),3)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if(area > 100):
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)


    if(cv2.waitKey(10) & 0xFF == ord('q')):
        cap.release()
        break

cv2.destroyAllWindows()
