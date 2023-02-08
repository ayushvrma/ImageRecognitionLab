import cv2
import numpy as np

image_inverse = cv2.imread('cameraman.tif')
image_inverse = cv2.cvtColor(image_inverse, cv2.COLOR_BGR2GRAY)
max_value = image_inverse.max()
for i in range(0,image_inverse.shape[0]):
    for j in range(0, image_inverse.shape[1]):
        image_inverse[i][j] = max_value - image_inverse[i][j]
print(image_inverse)
cv2.imshow('image', image_inverse)
cv2.waitKey(0)