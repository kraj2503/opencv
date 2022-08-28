import cv2 as cv
import numpy as np


img = cv.imread('opencv\photos\pboston.jpg')
cv.imshow('ptest',img)

#  Translation

# def translate(img ,x ,y):
#     transMAt = np.float32([[1,0,x],[0,1,y]])
#     dimensions = (img.shape[1],img.shape[0])
#     return cv.warpAffine(img,transMAt,dimensions)

#     # -x --> left
#     # -y --> up
#     # x --> right
#     # y --> down

# translated = translate(img ,100,100)
# cv.imshow('translate',translated)


# Rotation
# def rotate (img,angle,rotPoint=None):
#     (height,width)=img.shape[:2]

#     if rotPoint is None:
#         rotpoint = (width//2,height//2)

#     rotMat =cv.getRotationMatrix2D(rotPoint,angle,1.0)
#     dimensions =(width,height)

#     return cv.warpAffine(img,rotMat,dimensions)

# rotated = rotate(img ,90) 
# cv.imshow('rotated',rotated)


# resize

resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resied',resized)

# flipping

flip = cv.flip(img,-1)
cv.imshow('flip',flip)

# cropping

cropped = img[200:4000,300:4000]
cv.imshow('cropped',cropped)
cv.waitKey(0)