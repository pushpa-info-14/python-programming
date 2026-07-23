class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


s = Solution()
print(s.removeDuplicates(s="abbaca"))
print(s.removeDuplicates(s="azxxzy"))
