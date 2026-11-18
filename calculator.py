
# https://github.com/rosstheboss2021-cmd/lab11--RN--DG
# Partner 1: Ross Noland
# Partner 2: Daniel Gomez
import math
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a
def log(a, b):
    if a == 0:
        raise ValueError
    return math.log(b, a)
def exp(a, b):
    return a ** b
def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError("Cannot take square root of a negative number")


def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except (TypeError, ValueError):
        raise ValueError("Invalid hypotenuse arguments")


