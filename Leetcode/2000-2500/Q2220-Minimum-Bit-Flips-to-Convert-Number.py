class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        res = 0
        while start > 0 or goal > 0:
            if start & 1 != goal & 1:
                res += 1
            start >>= 1
            goal >>= 1
        return res


s = Solution()
print(s.minBitFlips(10, 7))
print(s.minBitFlips(3, 4))
