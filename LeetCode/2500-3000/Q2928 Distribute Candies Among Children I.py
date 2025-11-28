class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for i in range(limit + 1):
            for j in range(limit + 1):
                k = n - (i + j)
                if 0 <= k <= limit:
                    res += 1
        return res


s = Solution()
print(s.distributeCandies(n=5, limit=2))
print(s.distributeCandies(n=3, limit=3))
