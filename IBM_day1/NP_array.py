#Numpy provides many functions to create arrays
import numpy as np

a = np.zeros((2, 2))  #array of all zeroes
print(a)

print('\n')

b = np.ones((1, 2))  #array of all ones
print(b)

print('\n')

c = np.full((2, 2), 7) #constant matrix
print(c)

print('\n')

d = np.eye(2)  #2x2 identity matrix
print(d)

print('\n')

e = np.random.random((2, 2))  #array with random values
print(e)