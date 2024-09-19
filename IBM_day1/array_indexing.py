import numpy as np

# Create the following rank 2 array with shape (3, 4)
# [[ 1 2 3 4]
# [ 5 6 7 8]
# [ 9 10 11 12]]

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

b = a[:2, 1:3]

# NOTE: A slice of an array is a view into the same data,
# so modifying it will modify the original array.

print(a[0, 1])

b[0, 0] = 77
print(a[0, 1])