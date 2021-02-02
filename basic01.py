import numpy as np

a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)], dtype='int8')

b = np.array([0, 8, 6], dtype=None)

c = np.array([('hi',), ('hello',), ('how r u',)])

print(a, '\n')
print(b, '\n')
print(c, '\n')

print('> dimensions of "a" is ', a.ndim, 'D')  # dimension of array ex: 1D,2D
print('> dimensions of "b" is ', b.ndim, 'D\n')  # dimension of array ex: 1D,2D

print('> rows and col. of "a" is ', a.shape)  # It will show rows and col. of array. Like (r,c)
print(f"""> Matrix 'a' has rows {a.shape[0]} and col. {a.shape[1]}""")
"""
a.shape[0] is 0th position of (3,3), so its rows value.
"""
print(b.shape)  # b has only one row and 3 col.

print('> data type of "a" is', a.dtype)  # dtype show which type of datatype used, normally "int32" used by default.
print('> data type of "b" is', b.dtype, '\n')  # 'int32' means 4 byte size of every elements. 32/8=4Bytes ,16/8=2Bytes.

print(a.itemsize)  # array's elements size
print(b.itemsize, '\n')

print('> Size of "a" is {} bytes'.format(a.nbytes))  # To find total size of array
print('> Size of "b" is {} bytes'.format(b.nbytes))
print('> Size of c is', c.nbytes, '\n')

print('> Numbers of elements of "a" is', a.size)  # number of element's
