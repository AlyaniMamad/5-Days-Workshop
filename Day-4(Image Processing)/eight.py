import cv2
import numpy as np


image = cv2.imread("E:\myimg.png")


tx = 100  
ty = 50   
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])


angle = 30  
rotation_matrix = cv2.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2), angle, 1)


scale_x = 0.8
scale_y = 1.2
scaling_matrix = np.float32([[scale_x, 0, 0], [0, scale_y, 0]])


pts1 = np.float32([[50, 50], [200, 50], [50, 200]])  
pts2 = np.float32([[10, 100], [200, 50], [100, 250]]) 
perspective_matrix = cv2.getAffineTransform(pts1, pts2)

translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))
rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))
scaled_image = cv2.warpAffine(image, scaling_matrix, (image.shape[1], image.shape[0]))
perspective_transformed_image = cv2.warpAffine(image, perspective_matrix, (image.shape[1], image.shape[0]))


cv2.imshow('Original Image', image)
cv2.imshow('Translated Image', translated_image)
cv2.imshow('Rotated Image', rotated_image)
cv2.imshow('Scaled Image', scaled_image)
cv2.imshow('Perspective Transformed Image', perspective_transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
