import cv2
import numpy as np

r1,r2,s1,s2 = 80,180,100,220


num_channels = (2**8)-1
alpha = (s1-0)/(r1-0)
beta = (s2-s1)/(r2-r1)
gamma = (num_channels-s2)/(num_channels-r2)

s = [0] *256

for i in range(num_channels+1):
    if i<r1:
        s[i] = alpha*i
    elif i<r2:
        s[i] = beta*(i-r1) + s1
    else:
        s[i] = gamma * (i-r2) + s2


s = np.round(s).astype(np.uint8)

img = cv2.imread('images/lena.jpg',0)
img = cv2.resize(img, (256,256))
cv2.imshow('original', img)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img[i,j] = s[img[i,j]]

cv2.imshow("img",img)
cv2.waitKey(0)

