import matplotlib.pyplot as plt
plt.subplot(2, 2, 1)  # 2行2列第 1 幅子图像
plt.text(0.5, 0.5, 'subplot(2,2,1)', ha='center', va='center', size=15)
plt.subplot(2, 2, 2)  # 2行2列第 2 幅子图像
plt.text(0.5, 0.5, 'subplot(2,2,2)', ha='center', va='center', size=15)
plt.subplot(2, 2, 3)  # 2行2列第 3 幅子图像
plt.text(0.5, 0.5, 'subplot(2,2,3)', ha='center', va='center', size=15)
plt.subplot(2, 2, 4)  # 2行2列第 4 幅子图像
plt.text(0.5, 0.5, 'subplot(2,2,4)', ha='center', va='center', size=15)
plt.subplots_adjust(left=0.08, bottom=0.08, right=0.96, top=0.96,
                    wspace=0.3, hspace=0.3)  # 调整图像的边距和间距
plt.show()
