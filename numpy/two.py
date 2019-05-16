import numpy as np

X= np.zeros((3,4), dtype=int)
print(X)

X = np.ones((4,5), dtype=int)
print(X)

X = np.full((4,3), 5)
print(X)

X = np.eye(5)
print(X)

X = np.diag([10,20,30,40])
print(X)

X = np.arange(10)
print(X)

X = np.arange(1, 10)
print(X)

X = np.arange(1,14,3)
print(X)


X = np.linspace(0, 24, 10)
print(X)

X = np.linspace(0,25,10, endpoint=False)
print(X)

x = np.reshape(X, (2,5))
print(x)

Y = np.arange(20).reshape((10,2))
print(Y)

Y = np.linspace(0,50,10, endpoint=False).reshape(5,2)

print(Y)


X = np.random.randint(4, 15, (3,2))
print(X)



