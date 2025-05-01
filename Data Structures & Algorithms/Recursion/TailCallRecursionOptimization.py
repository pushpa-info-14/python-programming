"""
Compiler optimization in certain languages to reduce stack overflows.
    - This works by ensuring the last function call is a recursive one
    - Rule of thumb: Make the recursive call the last instruction
    - Supported by mostly all functional languages.
      Not supported by Python, Java. Supported for JS in Safari.
"""


def factorial(n):
    return tail_factorial(n, 1)


def tail_factorial(n, multiplier):
    if n == 1:
        return multiplier
    else:
        return tail_factorial(n - 1, n * multiplier)


print(factorial(5))


"""
fac(4) = fac(4)
fac(4) = 4 x fac(3)
fac(4) = 4 x (3 x fac(2))
fac(4) = 4 x (3 x (2 x fac(1)))
fac(4) = 4 x (3 x (2 x 1))
fac(4) = 4 x (3 x 2)
fac(4) = 4 x 6
fac(4) = 24

fac(4) = tail_factorial(4, 1)
fac(4) = tail_factorial(3, 4 x 1)
fac(4) = tail_factorial(2, 3 x 4)
fac(4) = tail_factorial(1, 2 x 12)
fac(4) = 24
"""


# 0 1 1 2 3 5 8 13 ..................
def fib(n):
    return tail_fib(n, 0, 1)


def tail_fib(n, val1, val2):
    if n == 0:
        return val1
    elif n == 1:
        return val2
    else:
        return tail_fib(n - 1, val2, val1 + val2)


print(fib(4))
