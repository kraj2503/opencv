import cv2 as cv

# img = cv.imread('photos\cvimg (2).jpg')
# cv.imshow('random',img)

capture = cv.VideoCapture(0)

# capture = cv.VideoCapture('videos\qwe.mp4')
while True:
    isTrue, frame= capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break; 

capture.release()
cv.destroyAllWindows()