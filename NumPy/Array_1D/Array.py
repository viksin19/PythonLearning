import numpy as np

array = np.array([0,1,2,3,4])
print(array.size)  # Output : array size : 5
print(array.ndim)  # Output : Dimension -- 1D
print(array)  # Output : [0,1,2,3,4]
print(array[1]+array[2]) # Output : 1+2 = 3

# Re-assigning value at particular array
array[0] = 10   # array : [10,1,2,3,4]
array[1] = 30   # array : [10,30,2,3,4]
print(array)
# At one time
array[2:5] = 20,40,50    # array : [10,30,20,40,50]           [i:j]  i is inclusive , j is exclusive
print(array)
# vector operation using Numpy

U = np.array([1,-1])
V = np.array([1,-1])

#Addition
Z = U + V
print(Z)

#Subtraction
Z = U - V
print(Z)

#Multiplication with scalar quantity
Z = 3*U
print(Z)

#Product between two vector
Z = U*V
print(Z)

#Dot product
Z = np.dot(np.array([1,-1]),np.array([1,1]))   # dot product 1*1 + -1*1 = 1-1 = 0
print(Z)

# Other Operations
array2 = np.array([10,20,-10,30,40,70,50])

mean = array2.mean()
print('Mean of the array2 : ',mean)
max = array2.max()
print('Maximum value in array2 : ',max)

theta = np.array([0,np.pi/2,np.pi])    # theta : [0,pi/2,pi]
print("Theta -- ",theta)

print("Sin value : ",np.sin(theta))    # np.sin(theta) : [sin(0), sin(pi/2), sin(pi)]