#Perform Edge Detection using Canny Method

import cv2
img = cv2.imread("D:\Workspace (VS Code)\College\Slot-B-Computer Vision\Input\cat2.jpg")
cv2.imshow('Original', img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()