import cv2
import numpy as np

def without_background(img):
    r1,r2 = 140,185
    s = [0] *256
    num_channels = (2**8)-1

    img = cv2.resize(img, (256,256))
    cv2.imshow('original', img)
    s = [0] *256

    for i in range(num_channels+1):
        if i>=r1 and i<=r2:
            s[i] = 255

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i,j] = s[img[i,j]]

    cv2.imshow("img",img)
    print(img)
    cv2.waitKey(0)


def with_background(img):
    r1,r2 = 140,185
    s = [0] *256
    num_channels = (2**8)-1

    img = cv2.resize(img, (256,256))
    cv2.imshow('original', img)
    s = [0] *256

    for i in range(num_channels+1):
        if i>=r1 and i<=r2:
            s[i] = 255
        else:
            s[i] = i

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i,j] = s[img[i,j]]

    cv2.imshow("img",img)
    print(img)
    cv2.waitKey(0)

img = cv2.imread('images/lena.jpg',0)
with_background(img)