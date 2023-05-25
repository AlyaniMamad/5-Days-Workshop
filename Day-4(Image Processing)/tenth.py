import cv2
import numpy as np

# Load the image
image = cv2.imread("E:\myimg.png")

# Define the 3x3 blur kernel
kernel = np.ones((3, 3), np.float32) / 9

# Apply the spatial filtering
filtered_image = cv2.filter2D(image, -1, kernel)

# Display the original and filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
