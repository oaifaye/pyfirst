# coding=utf-8
#================================================================
#
#   File name   : face_mix.py
#   Author      : Faye
#   Created date: 2021/2/2 17:33 
#   Description : 把一张脸挪到另外一张脸，只是平移，没有任何变换
#
#================================================================

import dlib
import cv2
import numpy as np

def shape_to_np(shape, dtype="int", point_count=68): # 将包含68个特征的的shape转换为numpy array格式
    coords = np.zeros((point_count, 2), dtype=dtype)
    for i in range(0, point_count):
        coords[i] = (shape.part(i).x, shape.part(i).y)
    return coords

if __name__ == '__main__':
    # img_new = cv2.imread('face_mix/0016_01_1.png')
    # img = cv2.imread('face_mix/0016_01_5.png')
    img = cv2.imread(r'C:\Users\Administrator\Desktop\zawu\20210208/20210208123543.jpg')
    img_new = cv2.imread(r'C:\Users\Administrator\Desktop\zawu\20210208/20210208123539.jpg')
    detector = dlib.get_frontal_face_detector()
    pointer = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 1)
    if len(rects) != 0:
        rect = rects[0]
        shape = pointer(gray, rect)
        shape = shape_to_np(shape, point_count=68)
        max_xy = np.max(shape, axis=0)
        min_xy = np.min(shape, axis=0)
        w = max_xy[0] - min_xy[0]
        h = max_xy[1] - min_xy[1]
        wh = np.max((w, h)) + 20
        middle = (int(min_xy[0] + w / 2), int(min_xy[1] + h / 2))
        x = int(middle[0] - wh / 2)
        y = int(middle[1] - wh / 2)
        face_area = []
        for i in range(0, 17):
            face_area.append((shape[i][0], shape[i][1]))
        face_area.append((shape[24][0], shape[24][1]-4))
        face_area.append((shape[18][0], shape[18][1]-4))
        face_area.append((shape[0][0], shape[0][1]))

        # for i in range(3, 14):
        #     face_area.append((shape[i][0], shape[i][1]))
        # # face_area.append((shape[29][0], shape[29][1]))
        # face_area.append((shape[3][0], shape[3][1]))

        face_area = np.asarray(face_area)
        cv2.fillConvexPoly(img[y:y + wh, x:x + wh, :], face_area - (x, y), (0, 0, 0), lineType=0)
        face_preplace = img[y:y + wh, x:x + wh, :]
        face_balck = np.where(np.all(face_preplace == [0, 0, 0], axis=-1))
        for black_x, black_y in zip(face_balck[0], face_balck[1]):
            face_preplace[black_x, black_y, :] = img_new[black_x+y, black_y+x, :]
        img[y:y + wh, x:x + wh, :] = face_preplace

        # Create a black image
        # print('rect[1]:', rect.height)
        # print('rect[1][0]-rect[0][0]:', rect[1][0]-rect[0][0])
        # print('rect[1][1]-rect[0][1]:', rect[1][1]-rect[0][1])
        # img = np.zeros((1024, 1024, 3), np.uint8)
        # pts = np.array(shape, np.int32)  # 每个点都是(x, y)
        # pts = pts.reshape((-1, 1, 2))
        # cv2.polylines(img, [pts], True, (0, 255, 255))
        cv2.imshow('img2', img)
        cv2.waitKey()