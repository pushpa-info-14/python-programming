class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        return (n - 1000) + 1


s = Solution()
print(s.countCommas(1002))
print(s.countCommas(998))
