import cv2
import numpy as np

crop_image = cv2.imread('cameraman.tif')
crop_image = cv2.cvtColor(crop_image, cv2.COLOR_BGR2GRAY)
print("Enter 2 Co-ordinates x1,x2,y1,y2")
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
cropped_image = np.empty((x2-x1,y2-y1,1), dtype=np.uint8)
print(cropped_image.shape)
a1=0
b1=0
for i in range(x1, x2):
    for j in range(y1, y2):
        cropped_image[a1][b1] = crop_image[i][j]
        b1+=1
    a1+=1
    b1=0

print(cropped_image)
cv2.imshow('image', cropped_image)
cv2.waitKey(0)