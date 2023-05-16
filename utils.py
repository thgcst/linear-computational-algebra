import numpy as np
import copy

def is_square(matrix):
  number_of_rows = len(matrix)
  number_of_columns = len(matrix[0])

  return number_of_rows == number_of_columns

def is_symmetrical(matrix):
  if not is_square(matrix):
    raise Exception("Matrix must be square")

  number_of_rows = len(matrix)

  for i in range(number_of_rows):
    for j in range(number_of_rows):
      if matrix[i][j] != matrix[j][i]:
        return False

  return True

def cofactor(matrix, i, j):
  result = copy.deepcopy(matrix)

  result = np.delete(result, i, axis=0)
  result = np.delete(result, j, axis=1)

  return result

def determinant(matrix):
  if not is_square(matrix):
    raise Exception("Matrix must be square")

  number_of_rows = len(matrix)

  if number_of_rows == 1:
    return matrix[0][0]

  result = 0
  j = 0

  for i in range(0, number_of_rows):
    if matrix[i][j] != 0:
      result += matrix[i][j] * (-1)**(i+j) * determinant(cofactor(matrix,i,j))

  return result

def forward_substitution(matrix_L, matrix_b):
  number_of_rows = len(matrix_L)
  y = np.zeros(number_of_rows)

  y[0] = matrix_b[0]/matrix_L[0][0]

  for i in range(1, number_of_rows):
    sum = 0
    for j in range(i):
      sum += matrix_L[i][j]*y[j]
    
    y[i] = (matrix_b[i]-sum)/matrix_L[i][i]

  return y

def backward_substitution(matrix_U, matrix_y):
  number_of_rows = len(matrix_U)
  x = np.zeros(number_of_rows)

  x[number_of_rows-1] = matrix_y[number_of_rows-1]/matrix_U[number_of_rows-1][number_of_rows-1]

  for i in range(number_of_rows-2, -1, -1):
    sum = 0
    for j in range(i+1, number_of_rows):
      sum += matrix_U[i][j]*x[j]
    
    x[i] = (matrix_y[i] - sum)/matrix_U[i][i]

  return x

def is_positive_definite(x):
    return np.all(np.linalg.eigvals(x) > 0)

def print_result(matrix):
  print(np.around(matrix, 2))

def get_biggest_superior_element(matrix):
  number_of_rows = len(matrix)

  biggest = 0.0
  biggest_i = 0
  biggest_j = 0

  for i in range(number_of_rows):
    for j in range(i+1, number_of_rows):
      if np.fabs(matrix[i][j]) > biggest:
        biggest = np.fabs(matrix[i][j])
        biggest_i = i
        biggest_j = j
  
  return biggest, biggest_i, biggest_j