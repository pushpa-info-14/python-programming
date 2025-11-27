class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for c in s:
            if stack:
                if stack[-1] == 'A' and c == 'B':
                    stack.pop()
                elif stack[-1] == 'C' and c == 'D':
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        return len(stack)


s = Solution()
print(s.minLength(s="ABFCACDB"))
print(s.minLength(s="ACBBD"))
