import cv2
import numpy as np

image = cv2.imread("E:\myimg.png")

kernel = np.ones((3, 3), np.float32) / 9

filtered_image = cv2.filter2D(image, -1, kernel)

cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
