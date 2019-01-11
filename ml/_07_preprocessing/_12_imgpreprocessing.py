'''
Created on 2019年1月5日

@author: Administrator
'''
import cv2 # 导入图像处理库
import numpy as np # 导入numpy库
from matplotlib import pyplot as plt # 导入展示库
# 展示图像模块
def img_show(img_name, img):
    cv2.imshow(img_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# 原始图像
img_file = 'content1.jpg' # 定义原始数据文件
img = cv2.imread(img_file) # 以彩色模式读取图像文件
rows, cols, ch = img.shape # 获取图像形状
img_show('raw img', img) # 展示彩色图像
# 图像缩放
img_scale = cv2.resize(img, None, fx=0.6, fy=0.6, interpolation=cv2.INTER_CUBIC) # 图像缩放
img_show('scale img', img_scale) # 展示缩放后的图像
# 图像平移
M = np.float32([[1, 0, 100], [0, 1, 50]]) # 定义平移中心
img_transform = cv2.warpAffine(img, M, (cols, rows)) # 平移图像
img_show('transform img', img_transform) # 展示平移后的图像
# 图像旋转
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 0.6) # 定义旋转中心
img_rotation = cv2.warpAffine(img, M, (cols, rows)) # 第一个参数为旋转中心，第二个为旋转角度，第三个为旋转后的缩放因子
img_show('rotation img', img_rotation) # 展示旋转后的图像
# 透视变换
pts1 = np.float32([[76, 89], [490, 74], [37, 515], [520, 522]]) # 定义变换前的四个校准点
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]]) # 定义变换后的四个角点
M = cv2.getPerspectiveTransform(pts1, pts2) # 定义变换中心点
img_perspective = cv2.warpPerspective(img, M, (300, 300)) # 透视变换
img_show('perspective img', img_perspective) # 展示透视变换后的图像
# 转换为灰度图像
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 图像转灰度
img_show('gray img', img_gray) # 展示灰度图像
# 边缘检测
img_edges = cv2.Canny(img, 100, 200) # 检测图像边缘
img_show('edges img', img_edges) # 展示图像边缘
# 图像二值化
ret, th1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY) # 简单阈值
th2 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2) # 自适应均值阈值
th3 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2) # 自适应高斯阈值
titles = ['Gray Image', 'Global Thresholding (v = 127)',
'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding'] # 定义图像标题
images = [img_gray, th1, th2, th3] # 定义图像集
for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray') # 以灰度模式展示每个子网格的图像
    plt.title(titles[i]) # 设置每个自网格标题
    plt.xticks([]), plt.yticks([]) # 设置x轴和y轴标题
plt.show() # 展示图像
# 图像平滑
kernel = np.ones((5, 5), np.float32) / 25 # 设置平滑内核大小
img_smoth_filter2D = cv2.filter2D(img, -1, kernel) # 2D卷积法
img_smoth_blur = cv2.blur(img, (5, 5)) # 平均法
img_smoth_gaussianblur = cv2.GaussianBlur(img, (5, 5), 0) # 高斯模糊
img_smoth_medianblur = cv2.medianBlur(img, 5) # 中值法
titles = ['filter2D', 'blur', 'GaussianBlur', 'medianBlur'] # 定义标题集
images = [img_smoth_filter2D, img_smoth_blur, img_smoth_gaussianblur, img_smoth_medianblur] # 定义图像集
for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray') # 以灰度模式展示每个子网格的图像
    plt.title(titles[i]) # 设置每个自网格标题
    plt.xticks([]), plt.yticks([]) # 设置x轴和y轴标题
plt.show() # 展示全部图像
# 形态学处理
img2 = cv2.imread('content1.jpg', 0) # 以灰度模式读取图像
kernel = np.ones((5, 5), np.uint8) # 设置形态学处理内核大小
erosion = cv2.erode(img2, kernel, iterations=1) # 腐蚀
dilation = cv2.dilate(img2, kernel, iterations=1) # 膨胀
plt.subplot(1, 3, 1), plt.imshow(img2, 'gray') # 设置自网格1图像
# plt.subplot(1, 3, 2), plt.imshow(erosion, 'gray') # 设置自网格2图像
plt.subplot(1, 3, 3), plt.imshow(dilation, 'gray') # 设置自网格3图像
plt.show() 