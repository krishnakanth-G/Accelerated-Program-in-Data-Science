# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 07:59:20 2022
https://www.linkedin.com/in/raghuraj-singh-475b8715
@author: (raghuraj@hotmail.com)
"""

import numpy as np
print(dir(np))

row = np.array([1,2,3,4,5,6])
print(row)
type(row)

col = np.array([[1],[2],[3],[4],[5],[6],[7]])
print(col)

row = np.array((1,2,3,4,5,6))
print(row)

a = np.array([(1,2,3),(4,5,6)])
print(a)

a = np.array([[1,2,3],[4,5,6]])
print(a)

a = np.array([[1,2,3],(4,5,6)])

a = np.arange(5)
print(a)

a = np.arange(3,10)
print(a)

a = np.arange(1,10,2) 
print(a)


a = np.linspace(0,10) 
print(a)

np.linspace(1,5,10)

np.linspace(0,10,5, dtype=int)

np.linspace(0,10, num=5, endpoint=False) 

a = np.zeros((3,3))	
print(a)

np.ones((2,2))	

a = np.empty((2,2))
print(a)



mat = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(mat)

shape = mat.shape
shape[0]

# len(mat)
mat.ndim
mat.dtype
mat.astype(float)
type(mat)
mat.size
mat.itemsize
mat.data 


mat = np.array([['a','b','c'],['d','e','f'],('g','h','i')])


com = np.array([[1,2,3],[4,5,6]], dtype = complex)
print(com)
com.dtype 
com.size
com.itemsize


mat = np.array([[1, 2, 3, 'a'], [5, 6, 7, 8], [9, 10, 11, 12]])


arr1 = [1,2,3,4,5,6,7,8,9]

arr2 = arr1

id(arr1)
id(arr2)

arr2_c = arr1.copy()

id(arr2_c)

arr2_c2 = np.copy(arr1)

arr = np.array([6,4,2,9,5,8,7,3,1])
arr.sort()

arr2d = np.array([[6,4,2],[9,5,8],[7,3,1]])

arr2d.sort()

arr2d.sort(axis=0)  # column wise
arr2d


arr2d.sort(axis=1)  # row wise
arr2d


a = [1,2,3]
b = [4,5,6]

c = np.append(a,b)
c

np.insert(a, 1, 3, axis=0)

c.shape

np.resize(c, (2,10))


matrix = np.array([[1, 2, 3], [2, 4, 6], [3, 8, 9]])
matrix

matrix.diagonal()

matrix.diagonal(offset=1)
matrix.diagonal(offset=-1)

matrix.diagonal(offset=2)
matrix.diagonal(offset=-2)

matrix.trace()
sum(matrix.diagonal())



###################################################################################130122
import numpy as np

a = np.empty((2,2))
print(a)

a = np.zeros((2,2))
print(a)


matrix = np.array([[1, 2, 3], [2, 4, 6], [3, 8, 9]])

matrix.diagonal()

matrix.trace()

sum(matrix.diagonal())

np.diag(matrix)

sum(np.diag(matrix[::, ::-1]))

np.fliplr(matrix)


# Slicing and Subsetting
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

arr1[0]
arr1[-1]

arr1[0:3]
arr1[:1]
arr1[3:]
arr1[:]
arr1[::]
arr1[::2]
arr1[: : -1]


arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

arr2[0,0]

arr2[0:1,:]
arr2[0:2,1]
arr2[1:2, :]
arr2[1:3,1:3]

arr2[::-1, ::-1]


a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.array([9,0,1,2])


d = np.vstack((a,b,c))
print(d)
d.shape

d = np.hstack((a,b,c))
d.shape

np.row_stack((a, b, c))
np.column_stack((a, b, c))


arr2d = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,0]])

arr2d.flatten()
arr2d.reshape(-1, 1)
arr2d.reshape(1, -1)
arr2d.ravel()   
arr2d.reshape(2,6)
arr2d.reshape(4,3)
arr2d.reshape(4,4)


matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix.T
np.transpose(matrix)

np.linalg.inv(matrix)
np.linalg.det(matrix)

matrix @ np.linalg.inv(matrix)

a = np.array([1,2,3])
b = np.array([4,5,6])

np.dot(a, b)   # (1*4 + 2*5 + 3*6)


arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2 = np.array([[9,8,7],[6,5,4],[3,2,1]])


np.add(arr1, arr2)
arr1 + arr2
np.subtract(arr1, arr2)
arr1 - arr2
np.divide(arr1,arr2)
arr1 / arr2
np.multiply(arr1, arr2)
arr1 * arr2

arr1 % arr2

np.dot(arr1, arr2) 
arr1 @ arr2

np.sqrt(arr1)
np.sin(arr1)

arr1 == arr2
arr1 !=	arr2
arr1 <  arr2

np.array_equal(arr1, arr2)
np.array_equal(arr1, arr1)

np.array_split(arr1, 3)
np.array_split(arr1, 3, 0)
np.array_split(arr1, 3, 1)

arr = np.array([1,2,3,4,5,6,7,8,9,10])

np.mean(arr)
np.median(arr)
np.std(arr)
np.var(arr)
np.var(arr) ** 0.5

np.min(arr)
np.max(arr)


arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2d.sum()
arr2d.min()
arr2d.max(axis=0)
np.mean(arr2d, axis=0)
np.std(arr2d, axis=0)


matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

matrix + 100
matrix - 50

matrix += 1 
matrix -= 1

matrix ** (1/2)

np.sin(matrix) + np.cos(matrix)



import time

my_arr = np.arange(1000000)
my_list = list(range(1000000))

start = time.time()
my_arr2 = my_arr * 2
end = time.time()
print(f'Time taken: {end - start}')


start = time.time()
my_list_copy = [x*2 for x in my_list]
end = time.time()
print(f'Time taken: {end - start}')


from scipy import sparse
matrix = np.array([[0, 0],[0, 1],[3, 0]])
matrix_sparse = sparse.csr_matrix(matrix)
print(matrix_sparse)








