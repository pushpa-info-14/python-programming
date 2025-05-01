# Sum of first n numbers
# Parameterised way
def calSumParameterised(i, summation):
    if i < 1: return summation
    return calSumParameterised(i - 1, summation + i)


print(calSumParameterised(2, 0))
print(calSumParameterised(5, 0))


# Functional way
def calSumFunctional(i):
    if i == 0: return 0
    return i + calSumFunctional(i - 1)


print(calSumFunctional(2))
print(calSumFunctional(5))


def factorial(n):
    if n == 0: return 1
    return n * factorial(n - 1)

print(factorial(2))
print(factorial(3))
