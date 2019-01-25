import numpy

A = numpy.array([
    [1, 1],
    [0, 1]
])
B = numpy.array([
    [2, 0],
    [3, 4]
])
# 相同位置分别相乘
print(A * B)
# 矩阵相乘
print(A.dot(B))
print(numpy.dot(A, B))
C = numpy.arange(3)
# 以e为底数的指数函数
print(numpy.exp(C))
# 对array中元素分别开方
print(numpy.sqrt(C))
# 向下取整
D = numpy.floor(10 * numpy.random.random((3, 4)))
print(D)
# 将矩阵转换成一维向量
print(D.ravel())
# 转置
# 此步等价于D.reshape((4,-1)),-1表示让计算机根据已知自己计算
D.shape = (4, -1)
print(D.T)
# 拼接矩阵
print(numpy.hstack((A, B)))
print(numpy.vstack((A, B)))
# 切分矩阵,第二个参数可传入元组，表示切分位置
print(numpy.hsplit(A,2))
print(numpy.vsplit(A,2))
