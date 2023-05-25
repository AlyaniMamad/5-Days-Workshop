import cv2
import numpy as np

image = cv2.imread("E:\myimg.png")

tx = 100 
ty = 50  
M = np.float32([[1, 0, tx], [0, 1, ty]])

translated_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow('Original Image', image)
cv2.imshow('Translated Image', translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
