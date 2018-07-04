import cv2
import numpy as np

img1 = cv2.imread('messi4.jpg')
img2 = cv2.imread('opencv.png')

row,column,dim = img2.shape
roi = img1[0:row, 0:column]

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(img2gray,155,255,cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
img2_bg = cv2.bitwise_and(img2,img2,mask = mask)

dst = cv2.add(img1_bg,img2_bg)
img1[0:row, 0:column] = dst

cv2.imshow('ouptut',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
