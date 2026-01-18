import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')
cv.line(blank,(0,0), (100, 150), (255,255,255), thickness = 2)

cv.imshow("The Line", blank)

cv.waitKey(0)