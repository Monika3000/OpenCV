import cv2 as cv
import numpy as np

img = cv.imread("first/cat2.jpg")
cv.imshow("The Original Image",img)

#1.Averaging
avgMethod = cv.blur(img,(5,5))
cv.imshow("Averaging Image",avgMethod)

#2. Gaussian Blur (MOST POPULAR)
gaussian = cv.GaussianBlur(img,(7,7),0)
cv.imshow("Gaussian Blur Image",gaussian)

#3. Median Blur
medianBlur = cv.medianBlur(img,5)
cv.imshow("Median Blur Image",medianBlur) #shows the image almost like a painting as you can see!

#Bilateral Blur (This isn't a blur but actually a filter, 
#that help in effectively reducing the blurwhile keeking the edges sharp)
bilateralBlur = cv.bilateralFilter(img,9,85,85)
cv.imshow("Bilateral Blur Image",bilateralBlur)
cv.waitKey(0)