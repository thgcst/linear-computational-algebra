import numpy as np
import copy
from utils import determinant, is_square, is_positive_definite

def LU_decomposition(matrix):

  if determinant(matrix) == 0:
    raise Exception("Determinant must not be 0")

  number_of_rows = len(matrix)

  L = np.identity(number_of_rows)
  U = copy.deepcopy(matrix).astype(float)

  for k in range(0, number_of_rows):
    for i in range(k+1, number_of_rows):
      transform_matrix = np.identity(number_of_rows)
      transform_matrix[i][k] = -float(U[i][k]/U[k][k])

      L[i][k] = -transform_matrix[i][k]
      U = transform_matrix.dot(U)
        
  return L, U

def cholesky(matrix):
  if not is_square(matrix):
    raise Exception("Matrix must be square")

  if not is_positive_definite(matrix):
    raise Exception("Matrix must be positive definite")

  number_of_rows = len(matrix)
  L = copy.deepcopy(matrix).astype(float)

  for i in range(number_of_rows):
    sum_of_squares = 0
    for k in range(i):
      sum_of_squares += L[i][k]**2

    L[i][i] = np.sqrt(L[i][i] - sum_of_squares)

    for j in range(i+1, number_of_rows):
      sum_of_products = 0
      for k in range(i):
        sum_of_products += L[i][k]*L[j][k]
      
      L[j][i] = (L[i][j]-sum_of_products)/L[i][i]

  for i in range(0, number_of_rows):
    for j in range(i+1, number_of_rows):
      L[i][j] = 0

  return L


def R(x0,x1):
  return np.sum((x1[0:]-x0[0:])**2) / np.sum((x1[0:])**2)


def jacobi(matrix_A, matrix_b, x0 = None):
  number_of_rows = len(matrix_A)
  if x0 is None:
    x0 = np.zeros(number_of_rows)

  x1 = copy.deepcopy(x0).astype(float)

  for i in range(len(x0)):
    sum = 0
    for j in range(len(x0)):
      if j != i:
        sum += matrix_A[i][j] * x0[j]

    x1[i] = (matrix_b[i] - sum) / matrix_A[i][i]

  E = R(x0,x1)

  tolerance = 10**-7

  if E < tolerance:
    return x1
  elif E > 1:
    print("Não convergiu ->", x1, E)
  else:
    return jacobi(matrix_A, matrix_b, x1)
  

def gauss_seidel(matrix_A, matrix_b, x0 = None):
  number_of_rows = len(matrix_A)
  if x0 is None:
    x0 = np.zeros(number_of_rows)

  x1 = copy.deepcopy(x0).astype(float)

  for i in range(len(x0)):
    sum = 0
    for j in range(i):
      sum += matrix_A[i][j] * x1[j]
    for j in range(i+1, len(x0)):
      sum += matrix_A[i][j] * x0[j]

    x1[i] = (matrix_b[i] - sum) / matrix_A[i][i]

  E = R(x0,x1)
  tolerance = 10**-7


  if E < tolerance:
    return x1
  elif E > 1:
    print("Não convergiu ->", x1, E)
  else:
    return jacobi(matrix_A, matrix_b, x1)