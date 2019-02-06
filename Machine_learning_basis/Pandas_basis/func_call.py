import pandas

titanic_survival = pandas.read_csv("titanic_train.csv")


def not_null_count(column):
    row_null = pandas.isnull(column)
    null = column[row_null]
    return len(null)


column_null_count = titanic_survival.apply(not_null_count)
print(column_null_count)


def which_class(row):
    pclass = row["Pclass"]
    if pandas.isnull(pclass):
        return "Unknown"
    elif pclass == 1:
        return "First Class"
    elif pclass == 2:
        return "Second Class"
    elif pclass == 3:
        return "Third Class"


# axis默认值为0
# * 0 or 'index': apply function to each column
# * 1 or 'columns': apply function to each row
classes = titanic_survival.apply(which_class, axis=1)
print(classes)
