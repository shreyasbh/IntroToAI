import numpy as np

X = np.array([1,2,3,4,5])
print(X[0])
print(X[1])
print(X[-1])

X[4] = 20
print(X)

X = np.arange(1,10).reshape(3,3)
print(X)
print(X[0,0])
print(X[0,1])
print(X[2,2])

X[0,0] = 20
print(X)


x = np.array([1,2,3,4,5])
print(x)

x = np.delete(x, [0, 4])
print(x)


Y = np.arange(1, 10).reshape(3,3)
print(Y)

w = np.delete(Y, 0, axis=0)
print(w)

v = np.delete(Y, [0,2], axis=1)
print(v)

x = np.array([1,2,3,4,5])
print(x)

x = np.append(x, [7,8])
print(x)

Y = np.arange(1,10).reshape(3,3)
print(Y)

W = np.append(Y, [[10,11,12]], axis=0)
print(W)

V = np.append(Y, [[10], [11], [12]], axis=1)
print(V)


x = np.array([1,2,3,4,5])
print(x)

y = np.insert(x, 2, [3,4])
print(y)

Y = np.array([[1,2,3], [7,8,9]])
print(Y)

w = np.insert(Y, 1, [4,5,6], axis=0)
print(w)

v = np.insert(Y, 1, 5, axis=1)
print(v)





