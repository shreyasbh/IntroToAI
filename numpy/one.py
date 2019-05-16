import numpy as np

x = np.array([1, 2, 3, 4, 5])
print('x= ', x)

print(x.shape)
print(type(x))
print(x.dtype)

x = np.array(['Hello', 'World'])
print()
print('x= ', x)
print()

print(x.shape)
print(type(x))
print(x.dtype)


x = np.array([1,2,'hello'])
print(x)


Y = np.array([[1,2,3], [4,5,6], [7,8,8], [10,11,12]])
print(Y)
print(Y.shape)
print(Y.size)
print(Y.dtype)


x = np.array([1.5, 2.2, 3.7, 4.0, 5.9], dtype=np.int64)
print(x)


np.save('my_array', x)

y = np.load('my_array.npy')
print(y)






