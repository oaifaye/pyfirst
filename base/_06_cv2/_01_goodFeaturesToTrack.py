
import numpy as np
import cv2


video_src = "C:/Users/Administrator/Desktop/zawu/新建文件夹/十大反败为胜.mp4"
feature_params = dict(maxCorners=500,
                      qualityLevel=0.05,
                      minDistance=7,
                      blockSize=7)
lk_params = dict(winSize=(15, 15),
                 maxLevel=2,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

tracks = []
prev_gray = None
cam = cv2.VideoCapture(video_src)
i = 0
while True:
    ret, frame = cam.read()  # 读取视频帧
    if(ret):
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 转化为灰度虚图像
        if i>0:
            p0 = np.float32([tr[-1] for tr in tracks]).reshape(-1, 1, 2)
            img0, img1 = prev_gray, frame_gray
            print('img0:', img0.shape)
            print('img1:', img1.shape)
            print('p0:', p0)
            p1, st, err = cv2.calcOpticalFlowPyrLK(img0, img1, p0, None,
                                               **lk_params)  # 前一帧的角点和当前帧的图像作为输入来得到角点在当前帧的位置
            print('p1:',p1)
            print('st:', st.shape)
            d = abs(p0 - p1).reshape(-1, 2).max(-1)
            print('d:',d)
            for x, y in np.float32(p1).reshape(-1, 2):
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
                cv2.imshow('lk_track', frame)

        # vis = frame.copy()
        mask = np.zeros_like(frame_gray)  # 初始化和视频大小相同的图像
        mask[:] = 255  # 将mask赋值255也就是算全部图像的角点
        p = cv2.goodFeaturesToTrack(frame_gray, mask=mask, **feature_params)
        if p is not None:
            for x, y in np.float32(p).reshape(-1, 2):
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
                tracks.append([(x, y)])
                # cv2.imshow('lk_track', frame)
        prev_gray = frame_gray
        i = i + 1
        ch = 0xFF & cv2.waitKey(1)
        if ch == 27:
            break