priority = {
    "^": 4,
    "*": 3,
    "/": 3,
    "+": 2,
    "-": 2,
    "(": 0,
}


def prefix_to_postfix(s: str) -> str:
    n = len(s)
    stack = []
    i = n - 1
    while i >= 0:
        if s[i].isalnum():
            stack.append(s[i])
        else:
            t1 = stack.pop()
            t2 = stack.pop()
            combined = t1 + t2 + s[i]
            stack.append(combined)
        i -= 1
    return stack[0]


print(prefix_to_postfix("/-ab*+def"))
