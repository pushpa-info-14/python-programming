class Solution:
    def countDigits(self, num: int) -> int:
        res = 0
        original = num
        while num:
            digit = num % 10
            if original % digit == 0:
                res += 1
            num //= 10

        return res


s = Solution()
print(s.countDigits(7))
print(s.countDigits(121))
print(s.countDigits(1248))
