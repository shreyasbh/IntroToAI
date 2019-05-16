import pandas as pd
import numpy as np

fruits= pd.Series(data = [10, 6, 3,], index = ['apples', 'oranges', 'bananas'])
print(fruits)
print(fruits+2)
print(fruits-2)
print(fruits*2)
print(fruits/2)

print(np.sqrt(fruits))
