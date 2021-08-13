# coding=utf-8
#================================================================
#
#   File name   : read_video.py
#   Author      : Faye
#   Created date: 2021/1/2 13:57 
#   Description :
#
#================================================================
import cv2

def read():
    cap = cv2.VideoCapture(r'C:\Users\Administrator\Desktop\00501141812_bd954e7b.mp4')
    target = r'C:\Users\Administrator\Desktop\t/'
    i = 0
    while True:
        _, frame = cap.read()
        if not _:
            break
        cv2.imwrite(target+str(i)+'.jpg', frame)
        i += 1
    cv2.destroyAllWindows()
    cap.release()

def read_write():
    '''

    文件扩展名.avi:
        cv2.VideoWriter_fourcc('I','4','2','0')---未压缩的YUV颜色编码，4:2:0色度子采样。兼容性好，但文件较大。
        cv2.VideoWriter_fourcc('P','I','M','1')---MPEG-1编码类型。随机访问，灵活的帧率、可变的图像尺寸、定义了I-帧、P-帧和B-帧 、运动补偿可跨越多个帧 、半像素精度的运动向量 、量化矩阵、GOF结构 、slice结构 、技术细节、输入视频格式。
        cv2.VideoWriter_fourcc('X','V','I','D')---MPEG-4编码类型，视频大小为平均值，MPEG4所需要的空间是MPEG1或M-JPEG的1/10，它对运动物体可以保证有良好的清晰度，间/时间/画质具有可调性。
    文件扩展名.ogv:
        cv2.VideoWriter_fourcc('T','H','E','O')---OGGVorbis，音频压缩格式，有损压缩，类似于MP3等的音乐格式,兼容性差。
    文件扩展名.flv:
        cv2.VideoWriter_fourcc('F','L','V','1')---FLV是FLASH VIDEO的简称，FLV流媒体格式是一种新的视频格式。由于它形成的文件极小、加载速度极快，使得网络观看视频文件成为可能，它的出现有效地解决了视频文件导入Flash后，使导出的SWF文件体积庞大，不能在网络上很好的使用等缺点。
    '''
    cap = cv2.VideoCapture(r'C:\Users\Administrator\Desktop\zawu\20210615\095531_0.mp4')
    target = r'C:\Users\Administrator\Desktop\zawu\20210615/095531_0_a.mp4'
    i = 0
    # 帧率
    fps = int(round(cap.get(cv2.CAP_PROP_FPS)))
    # 分辨率-宽度
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # 分辨率-高度
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # 总帧数
    frame_counter = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    target_video = cv2.VideoWriter(target, cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), fps, (width, height))
    while True:
        _, frame = cap.read()
        if not _:
            break
        target_video.write(frame)
        i += 1
    cap.release()
    target_video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    read_write()