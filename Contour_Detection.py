import cv2 as cv
import numpy as np

img = cv.imread("first/Cat2.jpg")

cv.imshow("Original Image",img)

grayScale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("GRAYSCALE Image", grayScale)

cv.waitKey(0)