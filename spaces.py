import cv2 as cv
import matplotlib.pyplot as plt



img = cv.imread('opencv\photos\pboston.jpg')
cv.imshow('ptest',img)



# BGR
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grey',grey)

# # BGR to HSV (Hue Saturation value)
# hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow('hsv',hsv)

# # BGR to L*A*B
# lab= cv.cvtColor(img,cv.COLOR_BGR2LAB) 
# cv.imshow('lab',lab)

# # BGR to RGB (opencv read in bgr and others read in rgb)
# rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
# cv.imshow('rgb',rgb)


# plt.imshow(rgb)
# plt.show()




cv.waitKey(0)