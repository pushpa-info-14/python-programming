class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                x = s[:l] + s[l + 1:]
                y = s[:r] + s[r + 1:]
                if x == x[::-1] or y == y[::-1]:
                    return True
                else:
                    return False
        return True


s = Solution()
print(s.validPalindrome(s="aba"))
print(s.validPalindrome(s="abca"))
print(s.validPalindrome(s="abc"))
print(s.validPalindrome(s="eceec"))
