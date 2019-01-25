import numpy

a = numpy.arange(15).reshape(3, 5)
print(a)
# 维度
print(a.ndim)
# 元素类型
print(a.dtype)
# 元素个数
print(a.size)
# 批量初始化，默认float型
b = numpy.zeros((3, 4))
c = numpy.ones((2, 3, 4), dtype=numpy.int32)
print(b)
print(c)
# 产生一个包含负1到正1随机值的array
print(numpy.random.random((2, 3)))
# 从初始值到结束值平均分割
print(numpy.linspace(0, 10, 100))
