priority = {
    "^": 4,
    "*": 3,
    "/": 3,
    "+": 2,
    "-": 2,
    "(": 0,
}


def infix_to_postfix(s: str) -> str:
    n = len(s)
    res = ""
    stack = []
    i = 0
    while i < n:
        if s[i].isalnum():
            res += s[i]
        elif s[i] == "(":
            stack.append(s[i])
        elif s[i] == ")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop()
        else:
            while stack and priority[s[i]] <= priority[stack[-1]]:
                res += stack.pop()
            stack.append(s[i])
        i += 1
    while stack:
        res += stack.pop()
    return res


print(infix_to_postfix("a+b*(c^d-c)"))
