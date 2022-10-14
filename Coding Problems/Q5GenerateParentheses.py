"""
Given integer n, generate all the valid combinations of n pairs of parentheses
"""


def is_valid1(combination):
    stack = []
    for par in combination:
        if par == '(':
            stack.append(par)
        else:
            """
            Validity condition1: Not trying to pop from an empty stack.
            Otherwise, it means that we found a closing parenthesis without an opening one from it.
            """
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    """
    Validity condition2: Stack must be empty at the end.
    Otherwise, it means that we have opening parentheses that we didn't close
    """
    return len(stack) == 0


def is_valid2(combination):
    diff = 0
    for par in combination:
        if par == '(':
            diff += 1
        else:
            if diff == 0:
                return False
            else:
                diff -= 1
    return diff == 0


s1 = "()(()(())"
s2 = "()(()))(())"
s3 = "()((()))(())"

print(is_valid1(s1))
print(is_valid1(s2))
print(is_valid1(s3))
print(is_valid2(s1))
print(is_valid2(s2))
print(is_valid2(s3))


def generate(n):
    def rec(n, diff, comb, combs):
        if diff < 0 or diff > n:
            return
        elif n == 0:
            if diff == 0:
                combs.append(''.join(comb))  # n
        else:
            comb.append('(')  # 1
            rec(n - 1, diff + 1, comb, combs)  # T(n-1)
            comb.pop()  # 1
            comb.append(')')  # 1
            rec(n - 1, diff - 1, comb, combs)  # T(n-1)
            comb.pop()  # 1

    combs = []
    rec(2 * n, 0, [], combs)
    return combs
# T(0) = n
# T(n) = 2T(n-1) + 1
# T(n) = 2(2T(n-1) + 1) + 1
# T(n) = 4T(n-2) + 3
# T(n) = 4(2T(n-3) + 1) + 3
# T(n) = 8T(n-3) + 7

# T(n) = 2kT(n-k) + (2k - 1)

# T(n) = 2nT(n - n) + (2n - 1)
# T(n) = 2nT(0) + 2n - 1
# T(n) = 2n*n + 2n - 1
# T(n) = O(n*2n)
# Learn substitution method

# S(n) = [n + 1] + [n * 2n]
# Call stack size + combs array size
# S(n) = O(n*2n)


print(generate(2))
