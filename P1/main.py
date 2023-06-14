import numpy as np
from tasks.task1 import LU_decomposition, cholesky, jacobi, gauss_seidel
from tasks.task2 import power_method, jacobi_eigen
from utils import forward_substitution, backward_substitution, print_result
import sys

np.set_printoptions(linewidth=sys.maxsize)

A = np.loadtxt('data/Matriz_A.dat')
b1 = np.loadtxt('data/Vetor_B_01.dat')
b2 = np.loadtxt('data/Vetor_B_02.dat')
b3 = np.loadtxt('data/Vetor_B_03.dat')

print("╔═════════════╗")
print("║   WELCOME   ║")
print("╚═════════════╝")
while True:
  print("\n-----------------------\n")
  print("Choose a task to run:")
  print("  - Task 1 (ICOD=1)")
  print("  - Task 2 (ICOD=2)")
  print("")
  print("  - Exit program (anything else)")
  print("")
  task = input("Insert: ")

  if task == '1':
    print("\n-----------------------\n")
    print("╔════════════╗")
    print("║   Task 1   ║")
    print("╚════════════╝")
    print("")
    print("Task 1 solves an AX=B linear system of equations")
    print("")
    print("Choose a method to run:")
    print("  - LU decomposition (ICOD=1)")
    print("  - Cholesky (ICOD=2)")
    print("  - Jacobi (ICOD=3)")
    print("  - Gauss-Jordan (ICOD=4)")
    print("")
    print("  - Go back (ICOD=5)")
    print("")
    method = input("Insert: ")

    if method == '1':
      print("")
      print("╔══════════════════════╗")
      print("║   LU decomposition   ║")
      print("╚══════════════════════╝")
      L, U = LU_decomposition(A)
      print("L:")
      print_result(L)
      print("")
      print("U:")
      print_result(U)
      print("")
      for b, n in [[b1, 1], [b2, 2], [b3, 3]]:
        y = forward_substitution(L, b)
        x = backward_substitution(U, y)

        print("╔════════════════╗")
        print("║   Vetor_B_0{}   ║".format(n))
        print("╚════════════════╝")

        print("y:")
        print_result(y)
        print("")
        print("x:")
        print_result(x)
        print("")

    elif method == '2':
      print("")
      print("╔══════════════╗")
      print("║   Cholesky   ║")
      print("╚══════════════╝")
      L = cholesky(A)
      print("L:")
      print_result(L)
      print("")
      for b, n in [[b1, 1], [b2, 2], [b3, 3]]:
        y = forward_substitution(L, b)
        x = backward_substitution(L.transpose(), y)

        print("╔════════════════╗")
        print("║   Vetor_B_0{}   ║".format(n))
        print("╚════════════════╝")

        print("y:")
        print_result(y)
        print("")
        print("x:")
        print_result(x)
        print("")

    elif method == '3':
      print("")
      print("╔════════════╗")
      print("║   Jacobi   ║")
      print("╚════════════╝")
      for b, n in [[b1, 1], [b2, 2], [b3, 3]]:
        print("")
        print("╔════════════════╗")
        print("║   Vetor_B_0{}   ║".format(n))
        print("╚════════════════╝")
        x = jacobi(A, b)
        print("x:")
        print_result(x)

    elif method == '4':
      print("")
      print("╔══════════════════╗")
      print("║   Gauss-Seidel   ║")
      print("╚══════════════════╝")
      for b, n in [[b1, 1], [b2, 2], [b3, 3]]:
        print("")
        print("╔════════════════╗")
        print("║   Vetor_B_0{}   ║".format(n))
        print("╚════════════════╝")
        x = gauss_seidel(A, b)
        print("x:")
        print_result(x)

  elif task == '2':
    print("\n-----------------------\n")
    print("╔════════════╗")
    print("║   Task 2   ║")
    print("╚════════════╝")
    print("")
    print("Task 2 finds the eigenvalues and eigenvectors of a matrix A")
    print("")
    print("Choose a method to run:")
    print("  - Power method (ICOD=1)")
    print("  - Jacobi (ICOD=2)")
    print("")
    method = input("Insert: ")

    if method == '1':
      print("")
      print("╔══════════════════╗")
      print("║   Power method   ║")
      print("╚══════════════════╝")
      eigenvalue, eigenvector = power_method(A)
      print("Eigenvalue: {}".format(eigenvalue))
      print("")
      print("Eigenvector:")
      print_result(eigenvector)
      print("")
    
    elif method == '2':
      print("")
      print("╔═══════════════════╗")
      print("║   Jacobi method   ║")
      print("╚═══════════════════╝")
      eigenvalues, eigenvector = jacobi_eigen(A)
      print("Eigenvalues:")
      print_result(eigenvalues)
      print("")
      print("Eigenvector:")
      print_result(eigenvector)
      print("")

  else:
    exit()

