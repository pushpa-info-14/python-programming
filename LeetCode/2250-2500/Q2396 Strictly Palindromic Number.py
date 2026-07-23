def is_palindrome(base, num):
    digits = []
    while num:
        digits.append(num % base)
        num //= base
    n = len(digits)
    for i in range(n // 2):
        if digits[i] != digits[n - i - 1]:
            return False
    return True


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for x in range(2, n - 1):
            if not is_palindrome(x, n):
                return False
        return True


s = Solution()
print(s.isStrictlyPalindromic(9))
print(s.isStrictlyPalindromic(4))
