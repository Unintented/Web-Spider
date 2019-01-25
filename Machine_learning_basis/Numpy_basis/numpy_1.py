import numpy

world_alcohol = numpy.genfromtxt("world_alcohol.txt", delimiter=",", dtype=str)
print(type(world_alcohol))
print(world_alcohol)
# 查询函数或类用法，不用括号
# print(help(numpy.genfromtxt))

# 将列表（不限维数）作为输入，元素必须为相同类型，否则所有元素会转换成一个更通用的类型
vector = numpy.array([5, 10, 15, 20])
matrix = numpy.array([[5, 10, 15], [20, 25, 30]])
print(vector)
print(matrix)
# 输出array结构，debug常用
print(vector.shape)
print(matrix.shape)

# 取array元素通过下标（从0开始）
third_country = world_alcohol[2][1]
print(third_country)
# 可使用切片访问多个元素，使用“:”表示“不限”
print(matrix[:, 2])
print(matrix[:, 1:3])
