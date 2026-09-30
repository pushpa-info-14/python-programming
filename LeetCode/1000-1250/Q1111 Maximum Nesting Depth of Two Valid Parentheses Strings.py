class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        depth = 0
        res = []
        for c in seq:
            if c == '(':
                res.append(depth % 2)
                depth += 1
            else:
                depth -= 1
                res.append(depth % 2)
        return res


s = Solution()
print(s.maxDepthAfterSplit(seq="(()())"))
print(s.maxDepthAfterSplit(seq="()(())()"))
