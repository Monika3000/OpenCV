import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')

cv.circle(blank, (250,250), 40, (0,0,250), thickness = cv.FILLED)

cv.imshow("The Circle", blank)

cv.waitKey(0)
