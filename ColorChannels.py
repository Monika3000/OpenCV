import cv2 as cv
import numpy as np

img = cv.imread('first/pic.jpg')
cv.imshow("The Original Image",img)
b,g,r = cv.split(img)
cv.imshow("The Blue",b)
cv.imshow("The Green",g)
cv.imshow("The Red",r)
mergeThem = cv.merge([b,g,r]) #this turns the splitted color channels as the origigal image!
cv.imshow("Merged Image",mergeThem)
cv.waitKey(0)