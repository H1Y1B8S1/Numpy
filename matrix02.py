import numpy as np

M1 = np.ones((5, 5))  # 5x5 ones matrix
print(M1, '\n')

M2 = np.zeros((3, 3))  # 3x3 zeros matrix
M2[1, 1] = 9  # we changed value of particular element position
print(M2, '\n')

M1[1:-1, 1:-1] = M2  # we changed values of M1 with whole values of M2
print(M1)

""" Be careful when copying arrays!!"""
a = np.array([(1, 2, 3), (4, 5, 6)])
print(a, '\n')

b = a.copy()
b[1, 0] = 100
print(b)
