import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import time
import similarity_util
import sys

def get_suffix():
    return "_"+str(dir_1).zfill(3)+"_"+str(dir_2_start).zfill(3)+"_"+str(dir_2_end).zfill(3)

def log(content, need_time=False):
    if need_time:
        content = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\t' + content
    print(content)
    # with open("similarity_hist_md5" + get_suffix() + ".log", 'a') as log:
    #     #     log.write(content+"\n")

if __name__ == '__main__':
    # check_path = r'C:\Users\Administrator\Desktop\zawu\similarity\check'
    # check_path = r'F:\pub_pic\004'
    # save_hist_path = r'C:\Users\Administrator\Desktop\zawu\similarity\res_hist'
    # save_MD5_path = r'C:\Users\Administrator\Desktop\zawu\similarity\res_md5'
    # standard_path = r'C:\Users\Administrator\Desktop\zawu\similarity\dui'
    dir_1 = int(sys.argv[1])
    dir_2_start = int(sys.argv[2])
    dir_2_end = int(sys.argv[3])

    check_paths = []
    check_root_path = r'/opt/10.20.31.124.pub.pic'
    save_hist_path = r'res_hist_1'
    save_MD5_path = r'res_md5_1'
    standard_path = r'dui'

    point_file_name = r'hist_md5'+get_suffix()+'.point'
    img_min_wh = 100
    hist_size = 256
    hist_min_similar = 0.80
    run_hist = True
    run_MD5 = True
    log('run_hist:' + str(run_hist), True)
    log('run_MD5:' + str(run_MD5), True)
    log('dir_1:' + str(dir_1), True)
    log('dir_2_start:' + str(dir_2_start), True)
    log('dir_2_end:' + str(dir_2_end), True)

    for f in range(dir_2_start, dir_2_end):
        check_path = os.path.join(str(check_root_path).zfill(3), str(dir_1).zfill(3), str(f).zfill(3))
        check_paths.append(check_path)
        log('check_path:' + check_path)

    if not os.path.exists(save_hist_path):
        os.makedirs(save_hist_path)
    if not os.path.exists(save_MD5_path):
        os.makedirs(save_MD5_path)

    duiHistArr = similarity_util.initDuiHistArr(standard_path, hist_size)
    duiMD5Arr = similarity_util.initDuiMD5Arr(standard_path)

    t = time.time()
    i = 0
    point_num = 0
    if os.path.exists(point_file_name):
        with open(point_file_name, 'r') as point_file:
            point_num = int(point_file.readline())

    for check_path in check_paths:
        if not os.path.exists(check_path):
            log('file not found:' + check_path)
            continue
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

                    if i % 5000 == 0:
                        # print('cost：', str(time.time()-t), check_img_path_name, i)
                        point_num = i
                        with open(point_file_name, 'w+') as point_file:
                            point_file.write(str(i))
                        log(str(time.time() - t) + "\t" + check_img_path_name + "\t" + str(i) )
                except Exception as e:
                    log('error:' + os.path.join(fpathe, check_img_name))
    print("finished!!!!!!!!!!!!!")

'''
 003: 1281492  004:26875537  005:2335789
 nohup python -u similarity_hist_md5.py 003 000 034 > similarity_hist_md5_003_000_034.log  2>&1 &
 nohup python -u similarity_hist_md5.py 005 000 026 > similarity_hist_md5_005_000_026.log  2>&1 &
 nohup python -u similarity_hist_md5.py 004 033 041 > similarity_hist_md5_004_033_041.log  2>&1 &
 nohup python -u similarity_hist_md5.py 004 041 049 > similarity_hist_md5_004_041_049.log  2>&1 &
 nohup python -u similarity_hist_md5.py 004 049 057 > similarity_hist_md5_004_049_057.log  2>&1 &
 nohup python -u similarity_hist_md5.py 004 057 074 > similarity_hist_md5_004_057_074.log  2>&1 &
 nohup python -u similarity_hist_md5.py 004 074 082 > similarity_hist_md5_004_074_082.log  2>&1 &
 nohup python -u similarity_hist_md5.py 004 082 090 > similarity_hist_md5_004_082_090.log  2>&1 &
 nohup python -u similarity_hist_md5.py 004 090 098 > similarity_hist_md5_004_090_098.log  2>&1 &
 nohup python -u similarity_hist_md5.py 004 098 106 > similarity_hist_md5_004_098_106.log  2>&1 &
 nohup python -u similarity_hist_md5.py 004 106 115 > similarity_hist_md5_004_106_115.log  2>&1 &
'''