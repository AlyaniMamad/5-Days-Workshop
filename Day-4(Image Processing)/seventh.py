import cv2

image = cv2.imread("E:\myimg.png")

scale_x = 0.5 
scale_y = 0.5 

new_width = int(image.shape[1] * scale_x)
new_height = int(image.shape[0] * scale_y)

scaled_image = cv2.resize(image, (new_width, new_height))

cv2.imshow('Original Image', image)
cv2.imshow('Scaled Image', scaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
