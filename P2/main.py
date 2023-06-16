from P2.tasks.task1 import *
from P2.tasks.task2 import *
import math

print("╔════════════╗")
print("║   Task 1   ║")
print("╚════════════╝")

def run_exercise_1():
  print("Exercício 1")

  def f(x):
    return math.log(math.cosh(x * math.sqrt(9.806 * 0.00341)), 10) - 50

  print("\tMétodo da bisseção: ",bissection_method(f, 0, 1000))
  print("\tMétodo de Newton original: ",newton_method(f, 1000))
  print("\tMétodo de Newton secante", secant_method(f, 1000))
  print("\tMétodo da interpolação reversa", reverse_interpolation_method(f, 0, 100, 1000))
  print("")

run_exercise_1()

def run_exercise_2():
  print("Exercício 2")

  def f(x):
    return 4*math.cos(x) - math.exp(2*x)

  print("\tMétodo da bisseção: ", bissection_method(f, 2, 0))
  print("\tMétodo de Newton original: ", newton_method(f, 0))
  print("\tMétodo de Newton secante", secant_method(f, 0))
  print("\tMétodo da interpolação reversa", reverse_interpolation_method(f, 0, 1, 10))
  print("")

run_exercise_2()

print("╔════════════╗")
print("║   Task 2   ║")
print("╚════════════╝")

def run_exercise_5():
  print("Exercício 5")

  def f(x):
    return 1 / (1 + x**2)

  results, iterations, integration_points = adaptive_simpson_method(f, 0, 3).values()

  print("\tIterações: ", iterations)
  print("\tPontos de integração: ", integration_points)
  print("\tResultados: ", results)
  print("")
  

run_exercise_5()