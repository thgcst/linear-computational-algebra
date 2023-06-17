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

    print("\tMétodo da bisseção: ", bissection_method(f, 0, 1000))
    print("\tMétodo de Newton original: ", newton_method(f, 1000))
    print("\tMétodo de Newton secante", secant_method(f, 1000))
    print(
        "\tMétodo da interpolação reversa",
        reverse_interpolation_method(f, 0, 100, 1000),
    )
    print("")


run_exercise_1()


def run_exercise_2():
    print("Exercício 2")

    def f(x):
        return 4 * math.cos(x) - math.exp(2 * x)

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


def run_exercise_6():
    print("Exercício 6")

    def S_sigma(x):
        return 2 / ((1 - x**2) ** 2 + (x / 10) ** 2)

    def m0(x):
        return S_sigma(x)

    def m2(x):
        return x**2 * S_sigma(x)

    simpson_results = adaptive_simpson_method(m0, 0, 10)["results"]
    print("\tFunção m0 - Regra de Simpson: ", simpson_results[-1])

    gauss_result = gauss_quadrature(m0, 0, 10, points=11)
    print("\tFunção m0 - Método da Quadratura de Gauss (11 pontos): ", gauss_result)

    simpson_results = adaptive_simpson_method(m2, 0, 10)["results"]
    print("\tFunção m2 - Regra de Simpson: ", simpson_results[-1])

    gauss_result = gauss_quadrature(m2, 0, 10, points=11)
    print("\tFunção m2 - Método da Quadratura de Gauss (11 pontos): ", gauss_result)

    print("")


run_exercise_6()


def run_exercise_7():
    print("Exercício 7")

    def S_n(x):
        return (
            4
            * math.pi**3
            * 3**2
            * math.exp(-16 * math.pi**3 / (x**4 * 5**4))
            / (x**5 * 5**4)
        )

    def S_sigma(x):
        return 1 / ((1 - x**2) ** 2 + (x / 10) ** 2) * S_n(x)

    def m0(x):
        return S_sigma(x)

    def m2(x):
        return x**2 * S_sigma(x)

    simpson_results = adaptive_simpson_method(m0, 0.01, 10)["results"]
    print("\tFunção m0 - Regra de Simpson: ", simpson_results[-1])

    gauss_result = gauss_quadrature(m0, 0.01, 10, points=11)
    print("\tFunção m0 - Método da Quadratura de Gauss (11 pontos): ", gauss_result)

    simpson_results = adaptive_simpson_method(m2, 0.01, 10)["results"]
    print("\tFunção m2 - Regra de Simpson: ", simpson_results[-1])

    gauss_result = gauss_quadrature(m2, 0.01, 10, points=11)
    print("\tFunção m2 - Método da Quadratura de Gauss (11 pontos): ", gauss_result)

    print("")


run_exercise_7()
