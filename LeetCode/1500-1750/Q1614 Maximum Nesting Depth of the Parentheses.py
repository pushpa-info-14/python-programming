class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                res = max(res, count)
                count -= 1
        return res


s = Solution()
print(s.maxDepth(s="(1+(2*3)+((8)/4))+1"))
print(s.maxDepth(s="(1)+((2))+(((3)))"))
print(s.maxDepth(s="()(())((()()))"))
