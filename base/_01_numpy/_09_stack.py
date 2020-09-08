# coding=utf-8
#================================================================
#
#   File name   : _09_stack.py
#   Author      : Faye
#   Created date: 2020/8/21 9:36 
#   Description :
#
#================================================================

import numpy as np

a = np.zeros((256, 50, 3))
b = np.zeros((256, 206, 3)) + 255

c = np.stack((a, b), axis=1)
print(a.shape)