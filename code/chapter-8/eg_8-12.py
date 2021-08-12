import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc('font', family='simsun')          # 设置字体
china = [11791, 79824, 81554, 82874, 83017, 83534, 84337,
         85058, 85414, 85997, 86542, 87071]
usa = [11, 66, 140640, 1003974, 1734040, 2537636, 4388566,
       5899504, 7077015, 8852730, 13082877, 19346790]
mothons = ['1月', '2月', '3月', '4月', '5月', '6月',
           '7月', '8月', '9月', '10月', '11月', '12月']
plt.plot(china, label='中国', marker='o')
plt.plot(usa, label='美国', marker='s')
plt.legend()
plt.xticks(range(0, 12), mothons, rotation=45)  # 设置x轴坐标标签
plt.yscale('log')                               # 设置y轴为对数坐标
plt.title('中美新冠病毒确诊数量对比', fontdict={'size': 16})
plt.show()
