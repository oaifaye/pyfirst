import cv2

img=cv2.imread('timg.jpg')

#                卷积核尺寸
blur=cv2.blur(img,(4,4))

cv2.imshow('blur',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()