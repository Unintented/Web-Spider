import pandas
import numpy

titanic_survival = pandas.read_csv("titanic_train.csv")
# print(titanic_survival.head(10))
age = titanic_survival["Age"]
# 找出有缺失值的行，其表示为True或False
age_is_null = pandas.isnull(age)
# 找到含缺失值的行
age_isnull_true = age[age_is_null]
print(age_isnull_true)
# 去除缺失值后计算平均值，也可用titanic_survival["Age"].mean()
ages = titanic_survival["Age"][age_is_null == False]
mean_age = sum(ages) / len(ages)
print(mean_age)
# index tells the method which column to group by
# values is the column that we want to apply the calculation to
# aggfunc specifies the calculation we want to perform
passanger_survival = titanic_survival.pivot_table(index="Pclass", values="Survived", aggfunc=numpy.mean)
print(passanger_survival)
port_stats=titanic_survival.pivot_table(index="Embarked",values=["Fare","Survived"],aggfunc=numpy.sum)
print(port_stats)
