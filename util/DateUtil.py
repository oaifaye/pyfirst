# -*- coding: utf-8 -*-

import datetime
import time

#获取格式化后的当前时间
def nowToStrNormal():
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime());


