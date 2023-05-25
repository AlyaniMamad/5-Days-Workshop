import cv2
imgpath="E:\myimg.png"

img1=cv2.imread(imgpath,1)

print(type(img1))
print('image data type : ',img1.dtype)
print('Row column : ',img1.shape)
print('Dimension : ',img1.ndim)
print('image size: ',img1.size)
(nr,nc,ch)=img1.shape

print('No of row',nr)
print('No of Column',nc)
print('No of Channels',ch)

cv2.imshow('Alyani',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()