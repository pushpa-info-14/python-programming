def fib(n):
    if n <= 1:
        return n
    return fib(n - 2) + fib(n - 1)


# O(n!)
print(fib(3))
print(fib(4))
print(fib(5))
