TOL = 1e-5
MAX_ITER = 10

def simpson_method(function, a, b):
  h = (b-a)/2
  return h/3*(function(a) + 4.0*function((a+b)/2) + function(b))

def adaptive_simpson_method(function, a, b):
  results = []
  for i in range(MAX_ITER):
    intervals = 2**(i)
    L = (b-a)/ intervals

    iteration_result = 0
    for k in range(intervals):
      iteration_result += simpson_method(function, a + k*L, a + (k+1)*L)
    
    if i > 0 and abs(iteration_result - results[-1])/abs(iteration_result) < TOL:
      return {"results": results, "iterations": i+1, "integration_points": (intervals*2)+1}
    else:
      results.append(iteration_result)