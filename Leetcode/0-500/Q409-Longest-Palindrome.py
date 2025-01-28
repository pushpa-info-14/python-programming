from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)

        odd = 0
        length = 0
        for i in counts:
            if counts[i] % 2 == 0:
                length += counts[i]
            else:
                odd = counts[i] % 2
                length += counts[i] - 1

        return length + odd


s = Solution()
print(s.longestPalindrome("abccccdd"))
print(s.longestPalindrome("ccc"))
print(s.longestPalindrome("cccc"))
