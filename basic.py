import cv2 as cv

img = cv.imread('opencv\photos\ptest.jpg')

cv.imshow('basic',img)

# comverting to greyscale

grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('grey',grey)


# blur
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_REPLICATE)
cv.imshow('blur',blur)

# Edge Cascade

canny = cv.Canny(img,125,175)
# canny1 = cv.Canny(blur,125,175)
cv.imshow('canny',canny)
# cv.imshow('canny1',canny1)

# Dilating the images

dilated = cv.dilate(canny,(7,7), iterations=1)
cv.imshow('dilated',dilated)


# Eroding

eroded = cv.erode(dilated,(7,7),iterations=1)
cv.imshow('eroded',eroded)



# resize
resized = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('re',resized)

# cropped

cropped = img[50:200,200:400]
cv.imshow('crop',cropped)

cv.waitKey(0)