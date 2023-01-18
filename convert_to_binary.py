import cv2
import numpy as np

img = cv2.imread('images/lena.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

size = (img.shape)


for i in range(size[0]):
    for j in range(size[1]):
        if img[i][j]>127:
            img[i][j] = 255
        else:
            img[i][j] = 0

img = cv2.resize(img, (200,200))

border_img = [ [0] * 300 for _ in range(300)]

for i in range(300):
    for j in range(300):
        if i<50 or i>249 or j<50 or j>249:
            continue
        else:
            border_img[i][j] = img[i-50][j-50]
        

print(img)
border_img = np.array(border_img, dtype=np.uint8)

cv2.imshow("image",border_img)

cv2.waitKey(0)

cv2.destroyAllWindows() 