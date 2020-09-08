import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

xls = pd.read_excel("data.xls")
df = xls.sort_values("pv", ascending=True) # 按照列col1降序排列数据
df = df["pv"]
sum = df.mean() * df.count() # 总数
print('sum:',sum)
ys = np.cumsum(np.asarray(df)) #累计求和
ys = ys / sum
# ystmp = np.asarray(df)#y轴
# ys = np.zeros(df.count())
# for i,y in enumerate(ystmp):
#     if i == 0:
#         ys[i] = 0
#         continue
#     ystmp[i] = ystmp[i]+ystmp[i-1]
#     ys[i] = ys[i] + ystmp[i] / sum

# print('ys[i]',ys[df.count()-1])
# print('ys:',ys)
yy = 0
s = 0 #数据面积
for i,y in enumerate(df):
    if i == 0:
        continue
    y0 = ys[i-1]
    y1 = ys[i]
    s1 = (1/ df.count()) * y0 + (1/ df.count()) * (y1-y0)/2
    # print(y0,y1 ,s1)
    s = s + s1
    yy = yy + y1
sz = 1/2 #总面积
print('s:',s)
# print('ys:',ys)
print('sz:',sz)
gini = (sz-s)/sz
print('gini:',gini)
xs = [i for i in range(df.count())]
plt.plot(xs, ys)
plt.scatter(xs, ys)
plt.show()

