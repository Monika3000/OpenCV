import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')

cv.putText(blank, "Hello Monika!", (150,255), cv.FONT_HERSHEY_TRIPLEX, 1, (0,255,0), 2)

cv.imshow("Text on Image", blank)

cv.waitKey(0)