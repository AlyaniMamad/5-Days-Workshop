import cv2
import numpy as np

# Load the image
image = cv2.imread("E:\myimg.png")

# Define the transformation matrix (translation)
tx = 100  # translation along the x-axis
ty = 50   # translation along the y-axis
M = np.float32([[1, 0, tx], [0, 1, ty]])

# Apply the transformation
translated_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

# Display the original and transformed images
cv2.imshow('Original Image', image)
cv2.imshow('Translated Image', translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
