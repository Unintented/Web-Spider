import numpy

vector = numpy.array([5, 10, 15, 20])
# 将array中的值与目标值一一对比，得到包含相同个数布尔值的array
equal_to_ten = vector == 10
print(equal_to_ten)
# 取出布尔值为true的对应元素
print(vector[equal_to_ten])

# 二维一样
matrix = numpy.array([
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
])
# 第二列中等于25的元素位置
second_column_equal_to_25 = matrix[:, 1] == 25
print(matrix[second_column_equal_to_25, :])
# 类型转换
matrix=matrix.astype(float)
print(matrix)
# print(help(numpy.array))

matrix_2=numpy.array([
    [5,10,15],
    [20,25,30],
    [30,35,40]
])
# 横向求和
print(matrix_2.sum(axis=1))
# 纵向求和
print(matrix_2.sum(axis=0))
