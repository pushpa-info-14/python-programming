class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = [int(x) for x in s]

        while len(digits) > 2:
            cur = []
            for i in range(len(digits) - 1):
                cur.append((digits[i] + digits[i + 1]) % 10)
            digits = cur
        if digits[0] == digits[1]:
            return True
        return False


s = Solution()
print(s.hasSameDigits(s="3902"))
print(s.hasSameDigits(s="34789"))
