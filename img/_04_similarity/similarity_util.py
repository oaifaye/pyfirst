import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import time
import hashlib


def initDuiHistArr(path, hist_size):
    duiHistArr = []
    for img in os.listdir(path):
        hists = []
        image1 = cv2.imread(path+"/"+img)
        # image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)  # 转化为灰度虚图像
        histb = cv2.calcHist([image1], [0], None, [hist_size], [0, 256])
        hists.append(normalize(histb))
        histg = cv2.calcHist([image1], [1], None, [hist_size], [0, 256])
        hists.append(normalize(histg))
        histr = cv2.calcHist([image1], [2], None, [hist_size], [0, 256])
        hists.append(normalize(histr))
        duiHistArr.append(hists)
    return duiHistArr

def initDuiMD5Arr(path):
    duiMD5Arr = []
    for img in os.listdir(path):
        file = open(os.path.join(path, img), "rb")
        md = hashlib.md5()
        md.update(file.read())
        res1 = md.hexdigest()
        duiMD5Arr.append(res1)
    return duiMD5Arr

# 直方图相似
def check_one_img_hist(img, duiHistArr, hist_size):
    imghistb = cv2.calcHist([img], [0], None, [hist_size], [0, 256])
    imghistg = cv2.calcHist([img], [1], None, [hist_size], [0, 256])
    imghistr = cv2.calcHist([img], [2], None, [hist_size], [0, 256])
    maxcorrcuo = 0
    minbc = 999999
    for duiHist in duiHistArr:
        corrcuob = cv2.compareHist(duiHist[0], normalize(imghistb), cv2.HISTCMP_CORREL)
        corrcuog = cv2.compareHist(duiHist[1], normalize(imghistg), cv2.HISTCMP_CORREL)
        corrcuor = cv2.compareHist(duiHist[2], normalize(imghistr), cv2.HISTCMP_CORREL)
        meancorrcuo = np.mean([corrcuob, corrcuog, corrcuor])
        if meancorrcuo > maxcorrcuo:
            maxcorrcuo = meancorrcuo

        # 巴氏距离
        # bcb = cv2.compareHist(duiHist[0], normalize(imghistb), cv2.HISTCMP_BHATTACHARYYA)
        # bcg = cv2.compareHist(duiHist[1], normalize(imghistg), cv2.HISTCMP_BHATTACHARYYA)
        # bcr = cv2.compareHist(duiHist[2], normalize(imghistr), cv2.HISTCMP_BHATTACHARYYA)
        # meanbc = np.mean([bcb, bcg, bcr])
        # if meanbc < minbc:
        #     minbc = meanbc

    return maxcorrcuo, minbc

# md5相似度
def check_one_img_md5(filepath, duiMD5Arr):
    file = open(filepath, "rb")
    md = hashlib.md5()
    md.update(file.read())
    res1 = md.hexdigest()
    for duiMD5 in duiMD5Arr:
        if res1 == duiMD5:
            return True
    return False

def getPathHist(path):
    histsb = []
    histsg = []
    histsr = []
    for img in os.listdir(path):
        image1 = cv2.imread(path+"/"+img)
        # image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)  # 转化为灰度虚图像
        histb = cv2.calcHist([image1], [0], None, [256], [0, 256])
        histsb.append(histb)
        histg = cv2.calcHist([image1], [1], None, [256], [0, 256])
        histsg.append(histg)
        histr = cv2.calcHist([image1], [2], None, [256], [0, 256])
        histsr.append(histr)
    meanhistb = np.sum(histsb, axis=0)
    meanhistg = np.sum(histsg, axis=0)
    meanhistr = np.sum(histsr, axis=0)
    sumhist = np.sum([meanhistb,meanhistg,meanhistr])
    return meanhistb/sumhist,meanhistg/sumhist,meanhistr/sumhist
    # plt.plot(meanhistb,color = 'b')
    # plt.plot(meanhistg,color = 'g')
    # plt.plot(meanhistr,color = 'r')
    # plt.xlim([0,256])
    # plt.show()

def getImageHist(image):
    histb = cv2.calcHist([image], [0], None, [256], [0, 255])
    histg = cv2.calcHist([image], [1], None, [256], [0, 255])
    histr = cv2.calcHist([image], [2], None, [256], [0, 255])
    return normalize(histb), normalize(histg), normalize(histr)

def normalize(data):
    return data / np.sum(data)


# if __name__ == '__main__':
#
#     # check_path = r'C:\Users\Administrator\Desktop\zawu\similarity\check'
#     check_path = r'F:\pub_pic\004'
#     save_hist_path = r'C:\Users\Administrator\Desktop\zawu\similarity\res_hist'
#     save_MD5_path = r'C:\Users\Administrator\Desktop\zawu\similarity\res_md5'
#     standard_path = r'C:\Users\Administrator\Desktop\zawu\similarity\dui'
#     img_min_wh = 100
#     hist_size = 256
#     hist_min_similar = 0.75
#     run_hist = True
#     run_MD5 = True
#     print('run_hist:', run_hist)
#     print('run_MD5:', run_MD5)
#     if not os.path.exists(save_hist_path):
#         os.makedirs(save_hist_path)
#     if not os.path.exists(save_MD5_path):
#         os.makedirs(save_MD5_path)
#
#     file_count = 0
#     for fpathe, dirs, check_img_names in os.walk(check_path):
#         for check_img_name in check_img_names:
#             file_count += 1
#     print('file_count：', file_count)
#
#     initDuiHistArr(standard_path)
#     initDuiMD5Arr(standard_path)
#
#     t = time.time()
#     i = 0
#     for fpathe, dirs, check_img_names in os.walk(check_path):
#         for check_img_name in check_img_names:
#             i += 1
#             try:
#                 font, ext = os.path.splitext(check_img_name)[0], os.path.splitext(check_img_name)[1]
#                 if ext == '.gif':
#                     continue
#                 check_img_path_name = os.path.join(fpathe, check_img_name)
#                 # print('start:', os.path.join(fpathe, check_img_name))
#                 vis = cv2.imread(check_img_path_name)
#                 if vis.shape[0] < img_min_wh or vis.shape[1] < img_min_wh:
#                     continue
#                 if run_hist:
#                     corrcuomean, minbc = check_one_img_hist(vis)
#                     # print(os.path.join(fpathe, check_img_name), corrcuomean, minbc)
#                     if corrcuomean > hist_min_similar:
#                         font, ext = os.path.splitext(check_img_name)[0], os.path.splitext(check_img_name)[1]
#                         corrcuomean = ('%.2f' % corrcuomean)
#                         cv2.imwrite(os.path.join(save_hist_path, font+"_"+str(corrcuomean)+ext), vis)
#
#                 # mD5相似
#                 if run_MD5:
#                     is_MD5_similar = check_one_img_md5(check_img_path_name)
#                     if is_MD5_similar:
#                         cv2.imwrite(os.path.join(save_MD5_path, check_img_name), vis)
#
#                 if i % 1000 == 0:
#                     print('耗时：', str(time.time()-t), check_img_path_name, i)
#             except Exception as e:
#                 print('error:', os.path.join(fpathe, check_img_name))
#
