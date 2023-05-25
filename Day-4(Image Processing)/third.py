import cv2
import matplotlib.pyplot as plt

imgWin = "E:\myimg.png"
img1 = cv2.imread(imgWin,1)
img2 = abs(255-img1)

'''cv2.imshow('Original Image',img1)
cv2.waitKey(0)

cv2.imshow('Negative Image',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
titles = ['Original Image' , 'Negative Image']
images = [img1,img2]

for k in range(2):
    plt.subplot(1,2,k+1)
    plt.imshow(images[k],cmap='gray')
    plt.title(titles[k])
    plt.xticks([])
    plt.yticks([])
    
plt.show()

