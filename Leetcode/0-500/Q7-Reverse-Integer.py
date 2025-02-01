class Solution:
    def reverse(self, x: int) -> int:
        n = x
        if x < 0:
            n = abs(x)

        res = 0
        while n:
            res = res * 10
            res += n % 10
            n = n // 10

        if res > 2 ** 31 - 1:
            return 0
        return res if x > 0 else -res


s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
