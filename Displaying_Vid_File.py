import cv2 as cv

cap = cv.VideoCapture("video1.mp4")

# We need to use while loop, as videos can be short or big. 
# So to make sure the video runs on loop we use a while loop

while True:
    isTrue, frame = cap.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord('d'): # So, when we press 'd' it closes the video (as in here)
        break

cap.release()
cv.destroyAllWindows() # Closes all GUI windows created by OpenCV