import cv2
import numpy as np

np.set_printoptions(threshold=999999)
img = cv2.imread(r'C:\Users\Administrator\Desktop/2008_002079.png')
img[img!=0]*=5
cv2.imwrite(r'C:\Users\Administrator\Desktop/2008_0020791.png', img)
print(img)