"""Accessing/Changing specific elements, rows, columns, etc"""
import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [1, 2, 3, 4, 5, 6, 7]])
print(a, '\n')


# Get a specific element [r,c]
print(a[1, 5], '\n')  # 13 >2nd row and 6th col.
print(a[0, 0], '\n')  # 1  < 1st row and 1st col.


# Get a specific row
print('> [r,c], I want particular row and whole col.')
print(a[0, :])
print('> I want 2nd rows first 3 elements')
print(a[1, 0:3])
print(a[:, 6])
print('> I want particular row and particular col.')
print(a[:, 2:4], '\n')


# Getting a little more fancy.
print(a[0, 1:-1:1])  # [row, col(start-index:end-index:step-size)]
print("> I want to print all even cols.")
print(a[0:3:2, 0:8:2])  # [row,start-index:end-index:step-size]
