"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def add(a, b): 
    return a + b
def sub(a,b):
    return a -b
def mul(a,b):
    return a * b
def div(a,b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b/a
def log(a,b):
    if b <= 0:
        raise ValueError("Log undefined for b <= 0.")
    if a <= 0 or a == 1:
        raise ValueError("Base must be > 0 and cannot equal 1.")
    return math.log(b,a)
def exp(a,b):
    return a ** b
