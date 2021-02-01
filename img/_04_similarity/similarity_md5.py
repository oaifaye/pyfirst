import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import time
import similarity_util

if __name__ == '__main__':
    # check_path = r'C:\Users\Administrator\Desktop\zawu\similarity\check'
    # check_path = r'F:\pub_pic\004'
    # save_hist_path = r'C:\Users\Administrator\Desktop\zawu\similarity\res_hist'
    # save_MD5_path = r'C:\Users\Administrator\Desktop\zawu\similarity\res_md5'
    # standard_path = r'C:\Users\Administrator\Desktop\zawu\similarity\dui'

    check_path = r'/opt/10.20.31.124.pub.pic'
    save_hist_path = r'res_hist'
    save_MD5_path = r'res_md5'
    standard_path = r'dui'
    need_file_count = False

    point_file_name = r'md5.point'
    img_min_wh = 100
    hist_size = 256
    hist_min_similar = 0.75
    run_hist = False
    run_MD5 = True
    print('run_hist:', run_hist)
    print('run_MD5:', run_MD5)
    if not os.path.exists(save_hist_path):
        os.makedirs(save_hist_path)
    if not os.path.exists(save_MD5_path):
        os.makedirs(save_MD5_path)

    if need_file_count:
        file_count = 0
        for fpathe, dirs, check_img_names in os.walk(check_path):
            for check_img_name in check_img_names:
                file_count += 1
        print('file_count：', file_count)

    duiHistArr = similarity_util.initDuiHistArr(standard_path, hist_size)
    duiMD5Arr = similarity_util.initDuiMD5Arr(standard_path)

    t = time.time()
    i = 0
    point_num = 0
    if os.path.exists(point_file_name):
        with open(point_file_name, 'r') as point_file:
            point_num = int(point_file.readline())

    for fpathe, dirs, check_img_names in os.walk(check_path):
        for check_img_name in check_img_names:
            i += 1
            if i < point_num:
                continue
            try:
                font, ext = os.path.splitext(check_img_name)[0], os.path.splitext(check_img_name)[1]
                if ext == '.gif':
                    continue
                check_img_path_name = os.path.join(fpathe, check_img_name)
                # print('start:', os.path.join(fpathe, check_img_name))
                vis = cv2.imread(check_img_path_name)
                if vis.shape[0] < img_min_wh or vis.shape[1] < img_min_wh:
                    continue
                if run_hist:
                    corrcuomean, minbc = similarity_util.check_one_img_hist(vis, duiHistArr, hist_size)
                    # print(os.path.join(fpathe, check_img_name), corrcuomean, minbc)
                    if corrcuomean > hist_min_similar:
                        font, ext = os.path.splitext(check_img_name)[0], os.path.splitext(check_img_name)[1]
                        corrcuomean = ('%.2f' % corrcuomean)
                        cv2.imwrite(os.path.join(save_hist_path, font+"_"+str(corrcuomean)+ext), vis)

                # mD5相似
                if run_MD5:
                    is_MD5_similar = similarity_util.check_one_img_md5(check_img_path_name, duiMD5Arr)
                    if is_MD5_similar:
                        cv2.imwrite(os.path.join(save_MD5_path, check_img_name), vis)

                if i % 1000 == 0:
                    print('耗时：', str(time.time()-t), check_img_path_name, i)
                    point_num = i
                    with open(point_file_name, 'w+') as point_file:
                        point_file.write(str(i))
            except Exception as e:
                print('error:', os.path.join(fpathe, check_img_name))

