class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        res = 0
        len1 = min(n, k)
        len2 = max(0, n - k)
        res += len1 * len2
        len1 = min(m, k)
        len2 = max(0, m - k)
        res += len1 * len2
        return res


s = Solution()
print(s.minCuttingCost(n=6, m=5, k=5))
print(s.minCuttingCost(n=4, m=4, k=6))
