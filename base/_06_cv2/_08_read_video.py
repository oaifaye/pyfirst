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
