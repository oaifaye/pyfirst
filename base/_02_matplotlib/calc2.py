import pandas as PD
import numpy as NP
import matplotlib.pyplot as PLT
import matplotlib.ticker as MTK
from matplotlib.pyplot import MultipleLocator

'''
    是0点数据点不显示
'''

file = r'calc2.csv'
df = PD.read_csv(file,header=0, names=['datetime', 'vix_all'], sep='	')
#用下标代理原始时间戳数据
idx_pxy = NP.arange(df.shape[0])
#下标-时间转换func
def x_fmt_func(x, pos=None):
    idx = NP.clip(int(x+0.5), 0, df.shape[0]-1)
    return df['datetime'].iat[idx]
#绘图流程
def decorateAx(ax, xs, ys, x_func):
    ax.plot(xs, ys, color="green", linewidth=1, linestyle="-")
    ax.plot(ax.get_xlim(), [0,0], color="blue",
            linewidth=0.5, linestyle="--")
    PLT.tick_params(labelsize=6)
    #把x轴的刻度间隔设置为1，并存在变量里
    x_major_locator = MultipleLocator(10)
    ax.xaxis.set_major_locator(x_major_locator)
    if x_func:
        #set数据代理func
        ax.xaxis.set_major_formatter(MTK.FuncFormatter(x_func))
    ax.grid(True)
    return

fig = PLT.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
print(df['vix_all'])
decorateAx(ax1, df['datetime'], df['vix_all'], None)
decorateAx(ax2, idx_pxy, df['vix_all'], x_fmt_func)
#优化label显示,非必须
fig.autofmt_xdate()
PLT.show()