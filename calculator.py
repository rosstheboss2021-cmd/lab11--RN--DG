#https://github.com/rosstheboss2021-cmd/lab11--RN--DG.git
#Partner 1: Ross Noland
# Partner 2: Daniel Gomez

import math
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm arguments")
    return math.log(b, a)


def exponent(a, b):
    return a ** b

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



