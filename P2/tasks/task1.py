from utils import derivative

TOL = 1e-4
MAX_ITER = 100

def bissection_method(function, a, b):
  if function(a) > 0:
    raise Exception("f(a) must be negative")
  if function(b) < 0:
    raise Exception("f(b) must be positive")
  
  while(abs(b-a) > TOL):
    c = (a+b)/2
    if function(c) > 0:
      b = c
    else:
      a = c
  
  return c

def newton_method(function, x0):
  x1 = x0
  for k in range(MAX_ITER):
    x1 = x0 - function(x0)/derivative(function, x0)
    if abs(x1-x0) < TOL:
      break
    x0 = x1
  
  return x1

def secant_method(function, x0):
  delta = 1e-3
  
  x_prev = x0
  x_curr = x0 + delta
  x_next = x_curr

  for k in range(MAX_ITER):
    x_next = x_curr - function(x_curr)*(x_curr-x_prev)/(function(x_curr)-function(x_prev))
    if abs(x_next-x_curr) < TOL:
      break
    x_prev = x_curr
    x_curr = x_next

  return x_next

def reverse_interpolation_method(function, x1, x2, x3):
  if not (x1 < x2 < x3):
    raise Exception("x1 < x2 < x3 must be true")
  
  x0 = 1e36
  
  for k in range(MAX_ITER):
    y1 = function(x1)
    y2 = function(x2)
    y3 = function(x3)

    xk = x1*y2*y3/((y1-y2)*(y1-y3)) + x2*y1*y3/((y2-y1)*(y2-y3)) + x3*y1*y2/((y3-y1)*(y3-y2))
    
    if abs(xk-x0) < TOL:
      break
    else:
      max_y = max(y1, y2, y3)
      if max_y == y1:
        x1 = xk
        y1 = function(xk)
      elif max_y == y2:
        x2 = xk
        y2 = function(xk)
      else:
        x3 = xk
        y3 = function(xk)

    x0 = xk

  return xk