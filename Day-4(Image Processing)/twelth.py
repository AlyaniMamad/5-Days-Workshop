import cv2
import numpy as np

image = cv2.imread("E:\myimg.png", cv2.IMREAD_GRAYSCALE)

laplacian_kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

padded_image = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_REPLICATE)

filtered_image = np.zeros_like(image, dtype=np.float32)
for i in range(1, padded_image.shape[0] - 1):
    for j in range(1, padded_image.shape[1] - 1):
        patch = padded_image[i - 1:i + 2, j - 1:j + 2]
        filtered_pixel = np.sum(patch * laplacian_kernel)
        filtered_image[i - 1, j - 1] = filtered_pixel

filtered_image = cv2.convertScaleAbs(filtered_image)

cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
