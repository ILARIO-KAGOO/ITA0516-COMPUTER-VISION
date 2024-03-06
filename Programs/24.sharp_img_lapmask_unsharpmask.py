# Perform Sharpening of Image using unsharp masking.

import cv2
import numpy as np
img = cv2.imread("D:\Workspace (VS Code)\College\Slot-B-Computer Vision\Input\cat2.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
laplacian_kernel = np.array([[0, 1, 0],
 [1, -4, 1],
 [0, 1, 0]])
laplacian = cv2.filter2D(img, -1, laplacian_kernel)
sharpened = cv2.add(img, laplacian)
cv2.imshow('Original Image', img)
cv2.imshow('Sharpened Image', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
