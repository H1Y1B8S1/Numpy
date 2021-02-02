# Initializing Different Types of Arrays
import numpy as np

a = np.array([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)])
print(a, '\n')

""" All 0s matrix"""
zerosM = np.zeros((2, 3))  # 2D, 2x3 matrix
# zerosM = np.zeros((3,2, 3))  # 3D 3-layers, 2x3 matrix
print(zerosM, '\n')

""" All 1s matrix"""
onesM = np.ones((4, 2, 2), dtype='int32')  # 3D 4-layers, 2x2 matrix
print(onesM, '\n')

""" Any other numbers"""
fullM = np.full((2, 2), 99)  # 2x2 matrix with num you want
print(fullM)
fullM1 = np.full_like(a, 4)  # we changed value of all elements of matrix a.
print(fullM1, '\n')

""" Random decimal numbers  """
randomM = np.random.rand(4, 2)  # 4x2 random matrix with random decimal values.
print(randomM, '\n')

""" Random Integer values """
randomM = np.random.randint(-4, 4, size=(3, 3))  # low,high and size of matrix
print(randomM, '\n')

""" The identity matrix"""
identityM = np.identity(6)
print(identityM, '\n')

""" Repeat an array"""
arr = np.array([(1, 2, 3)])
r1 = np.repeat(arr, 3, axis=0)
print(r1)
