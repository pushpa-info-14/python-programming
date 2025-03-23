priority = {
    "^": 4,
    "*": 3,
    "/": 3,
    "+": 2,
    "-": 2,
    "(": 0,
}


def reverse(s):
    res = []
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "(":
            res.append(")")
        elif s[i] == ")":
            res.append("(")
        else:
            res.append(s[i])
    return "".join(res)


def infix_to_prefix(s: str) -> str:
    s = reverse(s)

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
            if s[i] == "^":
                while stack and priority[s[i]] <= priority[stack[-1]]:
                    res += stack.pop()
            else:
                while stack and priority[s[i]] < priority[stack[-1]]:
                    res += stack.pop()
            stack.append(s[i])
        i += 1
    while stack:
        res += stack.pop()

    return reverse(res)


# Reverse the infix
# Convert infix to postfix
# Reverse the answer
print(infix_to_prefix("(a+b)*c-d+f"))
