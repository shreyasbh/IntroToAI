import numpy as np

X = np.arange(25).reshape(5,5)
print(X)

print(X[X>10])

x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,10])

print(np.intersect1d(x,y))
print(np.setdiff1d(x,y))
print(np.union1d(x,y))

