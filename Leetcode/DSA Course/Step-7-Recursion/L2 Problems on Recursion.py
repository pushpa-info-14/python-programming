# Print name n times
def printName(name, n):
    if n == 0: return
    print(name)
    printName(name, n - 1)


printName("Pushpa", 5)
print("----------------")


# Print 1 to n
def print_one_to_n(i, n):
    if i > n: return

    print(i)
    print_one_to_n(i + 1, n)


print_one_to_n(1, 5)
print("----------------")


# Print n to 1
def print_n_to_one(i, n):
    if i < n: return

    print(i)
    print_n_to_one(i - 1, n)


print_n_to_one(5, 1)
print("----------------")


# Print 1 to n. Cannot use i + 1
def print_backtrack(i, n):
    if i < n: return
    print_backtrack(i - 1, n)
    print(i)


print_backtrack(5, 1)
print("----------------")


# Print n to 1. Cannot use i - 1
def print_backtrack2(i, n):
    if i > n: return
    print_backtrack2(i + 1, n)
    print(i)


print_backtrack2(1, 5)
print("----------------")
