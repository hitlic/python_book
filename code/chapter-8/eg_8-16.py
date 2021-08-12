import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

font = {'family': 'simsun', 'size': 12}
plt.figure(figsize=[10, 5])

centers = [[0, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(n_samples=300,              # 生成数据集
                            centers=centers, cluster_std=0.3)

# 画出原始数据
plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1])
plt.xlabel('(a) 原始数据', fontdict=font)

k_means = KMeans(n_clusters=3)                          # K均值估计器
k_means.fit(X)                                          # 聚类

# 画出聚类结果
plt.subplot(1, 2, 2)
marker_list = ['o', 's', '^']
color_list = ['r', 'b', 'g']
for i in range(3):
    c_data = X[k_means.labels_ == i]  # 获取一个类别的数据
    plt.scatter(c_data[:, 0], c_data[:, 1],             # 画出一个类别
                c=color_list[i], marker=marker_list[i], alpha=0.6)

plt.xlabel('(b) 聚类结果', fontdict=font)
plt.show()
