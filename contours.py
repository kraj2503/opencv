import cv2 as cv
import numpy as np

img = cv.imread('opencv\photos\pboston.jpg')
cv.imshow('ptest',img)

blank = np.zeros(img.shape,dtype ='uint8')
cv.imshow('blank',blank)

grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('d',grey)
# blur = cv.GaussianBlur(grey,(5,5), cv.BORDER_DEFAULT)
# # cv.imshow('blur',blur)
canny= cv.Canny(img,125,175)
cv.imshow('canny',canny)

ret,thres =cv.threshold(grey,128,255,cv.THRESH_BINARY)

contours, hierarchies = cv.findContours(thres,cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')


cv.drawContours(blank,contours, -1 , (0,0,255),1)
cv.imshow("draw",blank)

cv.imshow('th',thres)


cv.waitKey(0)