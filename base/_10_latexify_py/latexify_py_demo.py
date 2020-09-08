# coding=utf-8
#================================================================
#
#   File name   : latexify_py_demo.py
#   Author      : Faye
#   Created date: 2020/8/11 12:53 
#   Description : latexify 一款python转LaTeX的工具
#
#================================================================

import math
import latexify


@latexify.with_latex
def solve(a, b, c):
    return (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

print(solve(1, 4, 3))
print(solve)
# print()
# solve