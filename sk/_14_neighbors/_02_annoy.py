
'''https://blog.csdn.net/m0_37850187/article/details/92712490'''
from annoy import AnnoyIndex
import random
import datetime

f = 512
t = AnnoyIndex(f=f,metric='angular')  # Length of item vector that will be indexed
vs = []
for i in range(100000):
    v = [random.gauss(0, 1) for z in range(f)]
    vs.append(v)

print('开始插')
tim = datetime.datetime.now()
for i,v in enumerate(vs):
    t.add_item(i, v)
print('插：', str(datetime.datetime.now() - tim))

# t.build(10) # 10 trees
print('开始build')
tim = datetime.datetime.now()
t.build(10)
print('build：', str(datetime.datetime.now() - tim))
tim = datetime.datetime.now()
t.save('test.ann',prefault=True)
print('save：', str(datetime.datetime.now() - tim))

# ...

u = AnnoyIndex(f,metric='angular')
tim = datetime.datetime.now()
u.load('test.ann',prefault=True ) # super fast, will just mmap the file
print('load：', str(datetime.datetime.now() - tim))
# u.unbuild()
# for i in range(2):
#     v = [random.gauss(0, 1) for z in range(f)]
#     u.add_item(10000+i, v)
t2 = datetime.datetime.now()
for i in range(100):
    v1 = [random.gauss(0, 1) for z in range(f)]
    print(u.get_nns_by_vector(vector=v1, n=3, include_distances=True))
print('检索耗时：', str(datetime.datetime.now() - t2))
# print(u.get_nns_by_item(0, 1000)) # will find the 1000 nearest neighbors