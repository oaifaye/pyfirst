'''
Created on 2018年12月6日
https://blog.csdn.net/saltriver/article/details/52270371
'''
import random


print('random.random():',random.random())             #产生0-1的随机浮点数
print('random.uniform():',random.uniform(0,100))        #产生指定范围内的随机浮点数
print('random.randint():',random.randint(0,100))        #产生指定范围内的随机整数
print('random.randrange():',random.randrange(0, 100, 2)) #从一个指定步长的集合中产生随机数,从0-100步长是2的数中随机，如2,4,6,8,10...
print('random.choice():',random.choice('1234567890'))     #从序列中产生一个随机数
list = [1, 2, 3, 4, 5, 6]
random.shuffle(list)
print('random.shuffle():',list) #将一个列表中的元素打乱

print('random.sample():',random.sample('1234567890', 3))  #从序列中随机获取指定长度的片断

# 三角分布的随机数 random.triangular(low, high, mode)
print('random.gauss():',random.gauss(5, 0.5))    # 高斯分布的随机数（稍快） 
# 正态分布的随机数 random.normalvariate(mu, sigma)
# beta β分布的随机数 random.betavariate(alpha, beta)
# 指数分布的随机数 random.expovariate(lambd)
# 伽马分布的随机数 random.gammavariate(alpha, beta)
# 对数正态分布的随机数 random.lognormvariate(mu, sigma)
# 冯米塞斯分布的随机数 random.vonmisesvariate(mu, kappa)
# 帕累托分布的随机数 random.paretovariate(alpha)
# 韦伯分布的随机数 random.weibullvariate(alpha, beta) 