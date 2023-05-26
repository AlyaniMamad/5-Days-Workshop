import numpy as np
import cv2
from scipy.signal import wiener

# Load the degraded image
degraded_image = cv2.imread("E:\myimg.png", 0)  # Assuming a grayscale image

# Perform Wiener filtering for image restoration
restored_image = wiener(degraded_image, mysize=3, noise=0.5)

# Display the restored image
cv2.imshow('Restored Image', restored_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
