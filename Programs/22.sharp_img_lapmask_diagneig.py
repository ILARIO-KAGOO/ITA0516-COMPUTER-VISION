#Perform Sharpening of Image using Laplacian mask implemented with an extension of diagonal neighbors,

import cv2
import numpy as np
img = cv2.imread("D:\Workspace (VS Code)\College\Slot-B-Computer Vision\Input\cat2.jpg")
kernel = np.array([[0,1,0], [1,-4,1], [0,1,0]])
sharpened = cv2.filter2D(img, -1, kernel)
cv2.imshow('Original', img)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()