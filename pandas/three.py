import pandas as pd

items = {'Bob' : pd.Series(data = [245, 25, 55], index = ['bike', 'pants', 'watch']),
         'Alice' : pd.Series(data = [40, 110, 500, 45], index = ['book', 'glasses', 'bike', 'pants'])}

print(type(items))
shopping_carts = pd.DataFrame(items)
print(shopping_carts)

data = {'Bob' : pd.Series(data = [245, 25, 55]),
         'Alice' : pd.Series(data = [40, 110, 500, 45])}

test = pd.DataFrame(data)
print(test)
