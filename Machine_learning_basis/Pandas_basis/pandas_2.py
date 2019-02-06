import pandas

food_info = pandas.read_csv("food_info.csv")
# 对数据排序，默认升序，Inplace表示是否在原dataframe中排序，若不是，则原dataframe中顺序不变
food_info.sort_values("Sodium_(mg)", inplace=True, ascending=False)
# print(food_info["Sodium_(mg)"])

titanic_survival=pandas.read_csv("titanic_train.csv")
new_titanic_survival=titanic_survival.sort_values("Age",ascending=False)
print(new_titanic_survival[0:10])
# 排序后索引重排
titanic_reindexed=new_titanic_survival.reset_index(drop=True)
print(titanic_reindexed.loc[0:10])