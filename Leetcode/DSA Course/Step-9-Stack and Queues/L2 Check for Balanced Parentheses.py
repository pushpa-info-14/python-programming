class Solution:
    def isValid(self, s: str) -> bool:
        mp = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if len(stack) == 0: return False
                if mp[stack.pop()] != c:
                    return False
        return len(stack) == 0


s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([])"))
