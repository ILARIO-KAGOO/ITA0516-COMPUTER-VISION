#Perform Edge detection using Sobel Matrix along XY axis

import cv2
img = cv2.imread("D:\Workspace (VS Code)\College\Slot-B-Computer Vision\Input\cat2.jpg")

# Display original image
cv2.imshow('Original', img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection

cv2.imshow('Sobel XY', sobelxy)
cv2.waitKey(0)
cv2.destroyAllWindows()
