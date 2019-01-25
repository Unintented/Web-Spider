import numpy

# 直接赋值，则a,b是相同array的不同名称
a = numpy.arange(12)
b = a
print(b is a)
b.shape = (3, 4)
print(a.shape)
print(id(a))
print(id(b))
# c=a.view(),是浅复制，是不同的array，但拥有相同数据值（会同时变化，shape不会）
# d=a.copy(),是深复制，是不同的array
