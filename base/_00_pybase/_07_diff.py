#求导数
from sympy import *
x = symbols("x") # 符号x，自变量
y = x ** 8
yd = diff(y,x,2) #2阶导
print(yd)