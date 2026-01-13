import cv2 as cv

def rescaleFrame(frame, scale = 0.55):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[1]*scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

cap = cv.VideoCapture("video1.mp4")
while True:
    isTrue, frame = cap.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0XFF == ord('d'):
        break
cap.release()
cv.destroyAllWindows()