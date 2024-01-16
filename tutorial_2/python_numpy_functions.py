import numpy as np
import time as time

#keep the seed number the same
seed_number = 0
seed = np.random.seed(seed_number)


#%% Array Indexing 
# create a 5 x 5 matrix of random numbers between 0 and 50
toy_array = np.random.randint(0, 50, (5, 5))

# get the first column of the matrix
first_column = toy_array[:, 0]
print("First column of the matrix: ", first_column)

# get the first row of the matrix
first_row = toy_array[0, :]
print("First row of the matrix: ", first_row)

# dot product of the first row and first column
dot_product = np.dot(first_row, first_column)
print("Dot product of the first row and first column: ", dot_product)


#cross product of the first row and first column
cross_product = np.cross(first_row, first_column)
print("Cross product of the first row and first column: ", cross_product)   