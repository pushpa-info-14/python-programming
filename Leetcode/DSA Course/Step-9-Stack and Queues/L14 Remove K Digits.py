class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
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
s = Solution()
print(s.removeKdigits("1432219", 3))
print(s.removeKdigits("100002", 3))
print(s.removeKdigits("100002", 1))
