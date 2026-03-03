import cv2 as cv
import numpy as np

img = cv.imread("first/Cat2.jpg")

cv.imshow("Original",img)

#Translation--> Moving/shifting the image in the x or y axis
def translate(img,x,y):
    trans = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,trans,dimension)

translated = translate(img,100,-100)
cv.imshow("Translated Image:", translated)

cv.waitKey(0)