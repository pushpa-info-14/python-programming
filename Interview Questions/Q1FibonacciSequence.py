# F(0) = 1
# F(1) = 1
# F(n) = F(n-1) + F(n-2)

# using recursion
def cal1(n):
    if n in {0, 1}:
        return n
    return cal1(n - 1) + cal1(n - 2)


print([cal1(n) for n in range(15)])

cache = {0: 0, 1: 1}


# Memoizing the recursive algorithm
def cal2(n):
    if n in cache:
        return cache[n]
    cache[n] = cal1(n - 1) + cal1(n - 2)
    return cache[n]


print([cal2(n) for n in range(15)])


# Using iteration
def cal3(n):
    # Validate the value of n
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(f'Positive integer number expected, got "{n}"')

    # Handle the base cases
    if n in {0, 1}:
        return n

    previous, fib_number = 0, 1
    for _ in range(2, n + 1):
        # Compute the next Fibonacci number, remember the previous one
        previous, fib_number = fib_number, previous + fib_number

    return fib_number


print([cal3(n) for n in range(15)])
