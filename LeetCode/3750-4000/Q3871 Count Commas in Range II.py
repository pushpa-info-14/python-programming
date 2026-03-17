class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        res = 0
        for i in range(3, 16, 3):
            if n >= 10 ** i:
                res += n - 10 ** i + 1
            else:
                break
        return res


s = Solution()
print(s.countCommas(1002))
print(s.countCommas(998))
