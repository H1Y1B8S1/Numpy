import numpy as np

a = np.array([(1, 2, 3, 4)])
print(a, '\n')

print('> add 2 to all elements\n', a + 2)  # add value '2' in every elements of array
print('> subtract 2 form all elements\n', a - 2)
print('> multiple 2 to all elements\n', a * 2)
print('> divide 2 to all elements\n', a / 2)
print(a ** 2, '\n')

b = np.array([(1, 0, 3, 0)])
print('sum',a + b)

"""Take the sin cos"""
print(np.cos(a))
print('\n')
print('\n')

""" LINEAR ALGEBRA"""
a = np.ones((2, 3))
print(a)
b = np.full((3, 2), 2)
print(b)

print(np.matmul(a, b))

""" Find the determinate"""
c = np.identity(3)
print(np.linalg.det(c))

""" Statistics"""
stats = np.array([(1,2,3),(4,5,6)])
print(stats)
print(np.min(stats))
print(np.max(stats,axis=1))
print(np.sum(stats))
