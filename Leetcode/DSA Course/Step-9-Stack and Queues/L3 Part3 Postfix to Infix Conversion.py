priority = {
    "^": 4,
    "*": 3,
    "/": 3,
    "+": 2,
    "-": 2,
    "(": 0,
}


def postfix_to_infix(s: str) -> str:
    n = len(s)
    stack = []
    i = 0
    while i < n:
        if s[i].isalnum():
            stack.append(s[i])
        else:
            t1 = stack.pop()
            t2 = stack.pop()
            combined = "(" + t2 + s[i] + t1 + ")"
            stack.append(combined)
        i += 1
    return stack[0]


print(postfix_to_infix("ab-de+f*/"))
