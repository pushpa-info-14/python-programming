class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        mid = n // 2
        m = ''
        l = list(s[:mid])
        if n & 1:
            m = s[mid]
        l.sort()
        return ''.join(l) + m + ''.join(l[::-1])


s = Solution()
print(s.smallestPalindrome(s="z"))
print(s.smallestPalindrome(s="babab"))
print(s.smallestPalindrome(s="daccad"))
