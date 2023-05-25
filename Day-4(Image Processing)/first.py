import cv2

img = cv2.imread("E:\myimg.png",0)

outpath = "E:\myimg.png"

cv2.imshow('Alyani',img)
cv2.imwrite(outpath,img)
cv2.waitKey(0)
cv2.destroyAllWindows()