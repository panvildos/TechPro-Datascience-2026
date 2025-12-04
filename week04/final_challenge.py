import numpy as np 
matrix = np.array([[3,1,-2],
                   [0,4,5],
                   [1,-1,2]])
determinant = np.linalg.det(matrix)
print(determinant)
inverse_matrix = np.linalg.inv(matrix)
print(inverse_matrix)
