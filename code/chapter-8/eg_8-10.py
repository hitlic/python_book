import matplotlib.pyplot as plt
# （a）折线图
x = range(10)
y = [i**2 for i in x]
plt.plot(x, y)
plt.show()
# （b）散点图
x = range(10)
y = [i**2 for i in x]
plt.scatter(x, y)
plt.show()
# （c）柱状图
x = range(10)
y = [i**2 for i in x]
plt.bar(x, y)
plt.show()
# （d）饼图
numbers = [0.1, 0.4, 0.3, 0.2]
plt.pie(numbers)
plt.show()
# （e）直方图
x = [1, 1, 2, 2, 2, 2, 3, 3]
plt.hist(x)
plt.show()
# （f）热力图
X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
plt.imshow(X)
plt.show()
