# generate 3x3 image
import numpy as np
import cv2


# Create an image from the pixel values
img1 = np.zeros((100, 100, 3), dtype=np.uint8)
img2 = np.ones((100, 100, 3), dtype=np.uint8)*255

for i in range(100):
    for j in range(100):
        if j>=25 and j<=75:
            img1[i,j] = 255
        if i>=25 and i<=75:
            img1[i,j] = 255

for i in range(100):
    for j in range(100):
        if j>=25 and j<=75:
            img2[i,j] = 0


rows, cols, channels = img1.shape

# Create a new image for the addition operation
add = np.zeros((rows, cols, channels), dtype=np.uint8)

# Create a new image for the subtraction operation
sub = np.zeros((rows, cols, channels), dtype=np.uint8)

# Perform the addition and subtraction operations
for i in range(rows):
    for j in range(cols):
        for k in range(channels):
            add[i,j,k] = img1[i,j,k] + img2[i,j,k]
            sub[i,j,k] = abs(img1[i,j,k] - img2[i,j,k])

# cv2.imshow('Image 1', img1)
# cv2.imshow('Image 2', img2)
# cv2.imshow('Addition', add)
cv2.imshow('Subtraction', sub)

cv2.waitKey(0)
# cv2.destroyAllWindows()