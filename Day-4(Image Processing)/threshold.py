import cv2
import numpy as np

image = cv2.imread("E:\myimg.png", 0)

threshold_value = 128
max_value = 255 

_, binary_thresholded = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_BINARY)

_, binary_inverse_thresholded = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_BINARY_INV)

_, truncated_thresholded = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_TRUNC)

_, threshold_to_zero = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_TOZERO)

_, threshold_to_zero_inverse = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_TOZERO_INV)

cv2.imshow('Binary Thresholded', binary_thresholded)
cv2.imshow('Binary Inverse Thresholded', binary_inverse_thresholded)
cv2.imshow('Truncated Thresholded', truncated_thresholded)
cv2.imshow('Threshold to Zero', threshold_to_zero)
cv2.imshow('Threshold to Zero Inverse', threshold_to_zero_inverse)

cv2.waitKey(0)
cv2.destroyAllWindows()
