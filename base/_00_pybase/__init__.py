#utf-8

#输出结果是以指数形式输出一个保留2位小数的实数
def point2():
    a = "%.2e" % 10000
    print(a)

#for的链式写法
def linkforin():
    arr = ['a','b','c','d']
    m = [x for x in arr]
    print(m)
    arr1 = []
    def ei(t):
        print(str(t))
        arr1.append(str(t))
    [ei(t) for t in range(20)]
    print('arr1:',arr1)
    print(['ei_{}{}'.format(t,t*t) for t in range(20)])
linkforin()

#set测试
def settest1():
    arr = (1,2,3,None)
    l = list(arr)
    s = set(l)
    print(type(arr),type(l),type(s))
    shusu = [i for i in l if i == i]
    print(shusu)
    print(type(shusu))