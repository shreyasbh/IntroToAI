import pandas as pd

items2 = [{'bikes': 20, 'pants': 30, 'watches': 35, 'shirts': 15, 'shoes':8, 'suits':45},
{'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5, 'shirts': 2, 'shoes':5, 'suits':7},
{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4, 'shoes':10}]

store_items = pd.DataFrame(items2, index = ['store 1', 'store 2', 'store 3'])

print(store_items)

print(store_items.isnull().sum())

print(store_items.count())

print(store_items.dropna(axis=0))
print(store_items.dropna(axis=1))






