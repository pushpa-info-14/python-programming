class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = (high - low) // 2
        if low & 1 or high & 1:
            res += 1
        return res


s = Solution()
print(s.countOdds(low=3, high=7))
print(s.countOdds(low=8, high=10))
print(s.countOdds(low=14, high=17))
