import cv2 as cv
import numpy as np

blank = np.zeros((500,100),dtype='uint8') 
cv.imshow('blank',blank)

img = cv.imread('opencv\photos\cvimg.jpg')

cv.imshow('random',img)

cv.waitKey( 0) 