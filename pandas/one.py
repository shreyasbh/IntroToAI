import pandas as pd

groceries = pd.Series(data=[30,6,"yes","no"], index=["eggs","apples", "milk", "bread"])
print(groceries)
print(groceries.shape)
print(groceries.ndim)
print(groceries.size)
print(groceries.index)
print(groceries.values)

print(groceries[['eggs', 'milk']])
print(groceries[[0,1]])

print(groceries.loc[['eggs','apples']])
print(groceries.iloc[[2,3]])

groceries.drop('apples', inplace=True)
print(groceries)

