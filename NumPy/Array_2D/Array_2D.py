import numpy as np

array_2D = np.array([[1, 2, 1], [2, 3, 2], [3, 4, 3]])
print('Array__2D : ', array_2D)
print('Touple : ', array_2D.shape)   # (3,3) -- 3 rows , 3 column
print('Dimesion : ', array_2D.ndim)  # 2   2-Dimension

array_1 = np.array([[1, 2, 3], [2, 3, 4]])
array_2 = np.array([[3, 4, 5], [4, 5, 6]])

# Subtraction
Z = array_1 - array_2
print('Subtraction Result : ', Z)
# Addition
Z = array_1 + array_2
print('Addition Result : ', Z)

# Dot product
# Z = np.dot(array_1,array_2)   #throw error because array_1 rows ! = array_2 column
# print(Z)
X = np.array([[1,2],[2,3]])
Y = np.array([[2,3],[3,4]])
Z = np.dot(X,Y)
print(Z)

