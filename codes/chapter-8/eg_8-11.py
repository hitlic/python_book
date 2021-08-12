import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

font = {'family': 'simhei', 'size': 12}  # 中文字体和字号
# 图像大小和分辨率
plt.figure(figsize=[8, 6], dpi=100)

# 折线图
x = np.arange(-10, 10.1, 0.1)
y1 = x ** 2
y2 = np.array([64] * len(x))
plt.plot(x, y1, label='$y=x^2$', marker='s', markevery=20)
plt.plot(x, y2, label='$y=64$', marker='o', markevery=20)

# 区域填充
x_fill = np.arange(-8, 8, 0.1)
y1_fill = x_fill ** 2
y2_fill = np.array([64]*len(x_fill))
plt.fill_between(x_fill, y1_fill, y2_fill, alpha=.2)

# 坐标轴配置
plt.xlim(-11, 11)      # x轴刻度区间
plt.ylim(-5, 105)      # y轴刻度区间
ax = plt.gca()         # 获取坐标轴对象
# ax.set_xticks(range(-10, 11, 5))   # 设置x轴刻度
# ax.set_yticks(range(-0, 101, 10))  # 设置y轴刻度
ax.xaxis.set_major_locator(MultipleLocator(5))  # x轴主刻度
ax.xaxis.set_minor_locator(MultipleLocator(1))  # x轴副刻度
ax.yaxis.set_major_locator(MultipleLocator(10))  # y轴主刻度
ax.yaxis.set_minor_locator(MultipleLocator(5))  # y轴副刻度

plt.annotate('$y=x^2$', xy=(-9, 81), xytext=(-7, 90),  # 标注
             arrowprops={'arrowstyle': "->"})
plt.xlabel('x轴标识（xlabel）', fontdict=font)    # x轴标识
plt.ylabel('y轴标识（ylabel）', fontdict=font)    # y轴标识
plt.title("标题（title）", fontdict={'family': 'simhei'})  # 图像标题
plt.legend(loc='upper right')                   # 图例
plt.show()                                      # 显示图像
