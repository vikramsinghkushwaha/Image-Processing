import cv2
import numpy as np
from PIL import Image,ImageChops,ImageOps
import pytesseract
#from skimage.transform import resize

pic = cv2.imread('10.png')
img = cv2.imread('10.png')
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img,200,200)

#kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
kernel1 = np.ones((5,5))

#med = cv2.GaussianBlur(thresh,(5,5),0)

contours, heirarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    area = int(cv2.contourArea(cnt))
    if(area > 1999 and area < 50000):
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(pic,(x,y),(x+w,y+h),(0,255,0),2)
        crop = img[y:y+h,x:x+w]

crop_grey = cv2.cvtColor(crop,cv2.COLOR_BGR2GRAY)
_,crop_thresh = cv2.threshold(crop_grey,125,255,cv2.THRESH_BINARY)
#resized = resize(crop_thresh, (28,28))

text = pytesseract.image_to_string(crop_thresh,lang = 'eng')
print "The license number is: ",text

cv2.imshow('edges',edges)
cv2.imshow('crop_thresh',crop_thresh)
cv2.imshow('img',img)
cv2.imshow('pic',pic)
#cv2.imshow('crop_grey',crop_grey)

cv2.waitKey(0)
cv2.destroyAllWindows()
