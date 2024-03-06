#Perform Sharpening of Image using Laplacian mask with negative center coefficient.

import cv2
import numpy as np
img = cv2.imread("D:\Workspace (VS Code)\College\Slot-B-Computer Vision\Input\cat2.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.array([[0,1,0], [1,-8,1], [0,1,0]])
sharpened = cv2.filter2D(img, -1, kernel)
cv2.imshow('Original', img)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()