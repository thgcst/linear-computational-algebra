import numpy as np
import copy
from utils import is_symmetrical, get_biggest_superior_element

def R(x0 = None, x1 = 0):
  if x0 == None or x1 == 0:
    return 999.0
  return np.fabs(x1 - x0) / x1

def power_method(matrix, x0 = None, lambda0 = None):
  number_of_rows = len(matrix)

  if x0 is None:
    x0 = np.ones(number_of_rows)

  x1 = matrix.dot(x0)

  lambda1 = x1[0]

  x1 = np.divide(x1, lambda1)

  residue = R(lambda0, lambda1)

  tolerance = 10**-5

  if residue > tolerance:
    return power_method(matrix, x1, lambda1)
  else:
    return lambda1, x1
  

def phi(matrix, i, j):
  if matrix[i][i] == matrix[j][j]:
    return np.pi/4
  else:
    return 1/2 * np.arctan(2*matrix[i][j] / (matrix[i][i] - matrix[j][j]))
  

def generate_P(matrix, i, j):
  number_of_rows = len(matrix)
  P = np.identity(number_of_rows)

  phi_value = phi(matrix, i, j)

  P[i][i] = np.cos(phi_value)
  P[i][j] = -1 * np.sin(phi_value)
  P[j][i] = np.sin(phi_value)
  P[j][j] = np.cos(phi_value)

  return P

def jacobi_eigen(matrix, X = None):
  if not is_symmetrical(matrix):
    raise Exception("Matrix must be symmetrical")

  number_of_rows = len(matrix)
  tolerance = 10**-5

  if X is None:
    X = np.identity(number_of_rows)

    
  biggest, i, j = get_biggest_superior_element(matrix)
  if biggest < tolerance:
    return matrix, X
  

  P = generate_P(matrix, i, j)
  Pt = P.transpose()

  A2 = np.around(Pt.dot(matrix).dot(P), 10)
  X2 = X.dot(P)

  return jacobi_eigen(A2, X2)