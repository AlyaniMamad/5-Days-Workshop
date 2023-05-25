import cv2

# Load the image
image = cv2.imread("E:\myimg.png")

# Set the scale factors
scale_x = 0.5  # scale factor along the x-axis
scale_y = 0.5  # scale factor along the y-axis

# Compute the new image dimensions
new_width = int(image.shape[1] * scale_x)
new_height = int(image.shape[0] * scale_y)

# Resize the image
scaled_image = cv2.resize(image, (new_width, new_height))

# Display the original and scaled images
cv2.imshow('Original Image', image)
cv2.imshow('Scaled Image', scaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
