from P2.tasks.task1 import *
import math

def run_exercise_1():
  print("Exercício 1")

  def f1(x):
    return math.log(math.cosh(x * math.sqrt(9.806 * 0.00341)), 10) - 50

  print("\tMétodo da bisseção: ",bissection_method(f1, 0, 1000))
  print("\tMétodo de Newton original: ",newton_method(f1, 1000))
  print("\tMétodo de Newton secante", secant_method(f1, 1000))
  print("\tMétodo da interpolação reversa", reverse_interpolation_method(f1, 0, 100, 1000))
  print("")

run_exercise_1()

def run_exercise_2():
  print("Exercício 2")

  def f1(x):
    return 4*math.cos(x) - math.exp(2*x)

  print("\tMétodo da bisseção: ", bissection_method(f1, 2, 0))
  print("\tMétodo de Newton original: ", newton_method(f1, 0))
  print("\tMétodo de Newton secante", secant_method(f1, 0))
  print("\tMétodo da interpolação reversa", reverse_interpolation_method(f1, 0, 1, 10))
  print("")

run_exercise_2()