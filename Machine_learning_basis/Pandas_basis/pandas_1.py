import pandas

food_info = pandas.read_csv("food_info.csv")
# 在Pandas中将字符串类型认作object类型
print(food_info.dtypes)
# print(help(pandas.read_csv))
# 默认显示前五行数据，参数自调
print(food_info.head())
print(food_info.tail())
# 显示第一列
print(food_info.columns)
# 取得特定行，可传入切片、元组,loc[5,"Age"]取特定值
print(food_info.loc[0])
# 通过列名可取得特定列
print(food_info["NDB_No"])
