from sklearn import neighbors, datasets
from sklearn.utils import shuffle

iris = datasets.load_iris()                          # 加载数据集

X, y = shuffle(iris.data, iris.target)               # 随机打乱数据
X_train, X_test = X[:120], X[120:]                   # 训练集与测试集特征
y_train, y_test = y[:120], y[120:]                   # 训练集与测试集标签

knn = neighbors.KNeighborsClassifier(n_neighbors=10,  # K最近邻估计器
                                     metric='minkowski', p=2)
knn.fit(X_train, y_train)                            # 训练

accuracy = knn.score(X_test, y_test)                 # 模型评价
print("测试集正确率：", accuracy)

d_id = 10
data_x = iris.data[d_id]
data_y = iris.target[d_id]
result = knn.predict([data_x])                       # 预测

print('预测样本：', data_x)
print('预测类别：', iris.target_names[result[0]])
print('真实类别：', iris.target_names[data_y])
