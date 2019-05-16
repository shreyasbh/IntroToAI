import numpy as np

x = np.arange(20).reshape(4,5)
print(x)

z = x[1:4, 2:5]
print(z)

#z[2,2] = 555
#print(x)

z = x[1:4, 2:5].copy()
print(z)

z[2,2] = 555
print(x)

z = np.diag(x)
print(z)

z = np.diag(x, k=1)
print(z)

