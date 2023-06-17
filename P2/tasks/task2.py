from P2.Gauss_Weights import Gauss_Weights

TOL = 1e-5
MAX_ITER = 20


def simpson_method(function, a, b):
    h = (b - a) / 2
    return h / 3 * (function(a) + 4.0 * function((a + b) / 2) + function(b))


def adaptive_simpson_method(function, a, b):
    results = []
    for i in range(MAX_ITER):
        intervals = 2 ** (i)
        L = (b - a) / intervals

        iteration_result = 0
        for k in range(intervals):
            iteration_result += simpson_method(function, a + k * L, a + (k + 1) * L)

        if i > 0 and abs(iteration_result - results[-1]) / abs(iteration_result) < TOL:
            break
        else:
            results.append(iteration_result)

    return {
        "results": results,
        "iterations": i + 1,
        "integration_points": (intervals * 2) + 1,
    }


def gauss_quadrature(function, a, b, points=3):
    def f(x):
        def change_of_variable(x):
            return 1 / 2 * ((b - a) * x + (b + a)) * (b - a) / 2

        return function(change_of_variable(x))

    result = 0
    for i in range(points):
        result += Gauss_Weights[points]["weights"][i] * f(
            Gauss_Weights[points]["points"][i]
        )

    return result


def central_derivative(f, x, delta):
    return (f(x + delta) - f(x - delta)) / (2 * delta)


def backward_derivative(f, x, delta):
    return (f(x) - f(x - delta)) / delta


def forward_derivative(f, x, delta):
    return (f(x + delta) - f(x)) / delta


def richard_extrapolation(f, x, delta, p):
    d1 = forward_derivative(f, x, delta)
    q = 2
    d2 = forward_derivative(f, x, delta / q)

    return d1 + (d1 - d2) / (q**p - 1)


def second_derivative(f, x, delta):
    return forward_derivative(forward_derivative(f, x, delta), x, delta)
