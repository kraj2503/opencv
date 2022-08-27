import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8') 

# img = cv.imread('opencv\photos\cvimg.jpg')
# cv.imshow('random',img)
#1 paint a certain colour

# blank[:]=156,255,0 #colour
# blank[200:300,300:400]=0,255,0 #colour

# thickness of -1 fills the image
 
# draw a rectangle
# cv.rectangle(blank,(0,0),(250,250), (0,250,0), thickness =2)
# cv.rectangle(blank,(0,0),(250,250), (0,250,0), thickness = -1)
# cv.rectangle(blank,(0,0),(250,250), (0,250,0), thickness = cv.FILLED)
# cv.rectangle(blank,(0,0), (blank.shape[1]//2, blank.shape[0]//2) ,(0,225,0), thickness = -1)


# circle

# cv.circle(blank,(250,250),40,(0,0,255),thickness =3)
cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),40,(0,0,255),thickness =3 )

# line

cv.line(blank,(0,0),(250,250),(0,255,0),thickness =2)

# write text

cv.putText(blank,'hello',(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0))

cv.imshow('blank',blank)

cv.waitKey( 0) 