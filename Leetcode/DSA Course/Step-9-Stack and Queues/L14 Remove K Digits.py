def removeDigits(s: str, k: int):
    stack = []
    for c in s:
        while stack and k > 0 and ord(stack[-1]) > ord(c):
            stack.pop()
            k -= 1
        stack.append(c)

    while k:
        stack.pop()
        k -= 1
    if not stack:
        return "0"

    res = []
    while stack:
        res.append(stack.pop())

    while res and res[-1] == "0":
        res.pop()

    if not res:
        return "0"

    return "".join(reversed(res))


# Remove maximum k digits from left to right
"""
Edge cases: k == n "0"
000100 --> 1000
123456 k=3 123
"""
print(removeDigits("1432219", 3))
print(removeDigits("100002", 3))
print(removeDigits("100002", 1))
