import numpy as np

""" Reorganizing Arrays"""

before = np.array([(1, 2, 3, 4), (5, 6, 7, 8)])
print(before, '\n')

after = before.reshape((4, 2))  # replacing the rows and col.
print(after, '\n')

""" Vertically stacking vectors"""
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])
v3 = np.array([9, 10, 11, 12])
h1 = np.array([(1,), (2,), (3,)])
h2 = np.array([(4,), (5,), (6,)])

print(np.vstack([v1, v2, v3]))
print(np.hstack([h1, h2]))

""" multiplication of matrix"""
x = np.array([[1, 2, 3],
              [4, 5, 6],
              [5, 4, 6]])
y = np.array([[1, 2, 3],
              [4, 5, 6],
              [4, 6, 7]])

result = np.dot(x, y)
for r in result:
    print(r)
