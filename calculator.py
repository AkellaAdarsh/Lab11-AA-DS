import math
def square_root(a):
    try:
        value = math.sqrt(a)
    except ValueError:
        if a < 0:
            raise ValueError
    return value
def hypotenuse(a,b):
    try:
        value = math.hypot(a,b)
    except ValueError:
        raise ValueError
    return value
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a
def logarithm(a,b):
    try:
        value = math.log(a,b)
    except ValueError:
        raise ValueError
    return value
def exponent(a,b):
    return a ** b


