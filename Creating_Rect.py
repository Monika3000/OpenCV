import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")

#blank[120:200, 400:500] = 250,135,241 #pink color

#cv.imshow("Selecting Certain pixels to be pink: 120:200 and 400:500", blank)

cv.rectangle(blank,(0,0), (blank.shape[1]//2,blank.shape[0]//2), (90,173,228), thickness = cv.FILLED)

cv.imshow("The Rectangle", blank)
cv.waitKey(0)
 