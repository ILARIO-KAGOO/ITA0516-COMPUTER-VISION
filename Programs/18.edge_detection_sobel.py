#Perform Edge detection using Sobel Matrix along X axis

import cv2
img = cv2.imread("D:\Workspace (VS Code)\College\Slot-B-Computer Vision\Input\cat2.jpg")
cv2.imshow('Original', img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
cv2.imshow('Sobel X', sobelx)
cv2.waitKey(0)
cv2.destroyAllWindows()