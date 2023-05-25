import cv2
import numpy as np

# Load the image
image = cv2.imread("E:\myimg.png")

# Define the transformation matrix for translation
tx = 100  # translation along the x-axis
ty = 50   # translation along the y-axis
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])

# Define the transformation matrix for rotation
angle = 30  # rotation angle in degrees
rotation_matrix = cv2.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2), angle, 1)

# Define the transformation matrix for scaling
scale_x = 0.8  # scale factor along the x-axis
scale_y = 1.2  # scale factor along the y-axis
scaling_matrix = np.float32([[scale_x, 0, 0], [0, scale_y, 0]])

# Define the transformation matrix for perspective transformation
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])  # original points
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])  # transformed points
perspective_matrix = cv2.getAffineTransform(pts1, pts2)

# Apply the transformations
translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))
rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))
scaled_image = cv2.warpAffine(image, scaling_matrix, (image.shape[1], image.shape[0]))
perspective_transformed_image = cv2.warpAffine(image, perspective_matrix, (image.shape[1], image.shape[0]))

# Display the original and transformed images
cv2.imshow('Original Image', image)
cv2.imshow('Translated Image', translated_image)
cv2.imshow('Rotated Image', rotated_image)
cv2.imshow('Scaled Image', scaled_image)
cv2.imshow('Perspective Transformed Image', perspective_transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
