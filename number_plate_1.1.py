import cv2
import numpy as np

img = cv2.imread('10.png')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(img2,127,255,cv2.THRESH_BINARY)
edges = cv2.Canny(img,200,200)
contours, heirarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    area = cv2.contourArea(cnt)
    if(area > 1000):
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('img',img)
#cv2.imshow('img2',img2)
cv2.imshow('thresh',thresh)
cv2.imshow('edges',edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
