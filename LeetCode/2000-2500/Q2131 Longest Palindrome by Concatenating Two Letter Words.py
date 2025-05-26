from collections import defaultdict
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq = defaultdict(int)
        res = 0
        mid_count = 0

        for word in words:
            reversed_word = word[::-1]
            if reversed_word in freq:
                res += 4
                freq[reversed_word] -= 1
                if freq[reversed_word] == 0:
                    del freq[reversed_word]
                if word == reversed_word:
                    mid_count -= 1
            else:
                if word == reversed_word:
                    mid_count += 1
                freq[word] += 1

        if mid_count > 0:
            res += 2
        return res


s = Solution()
print(s.longestPalindrome(["lc", "cl", "gg"]))
print(s.longestPalindrome(["ab", "ty", "yt", "lc", "cl", "ab"]))
print(s.longestPalindrome(["cc", "ll", "xx"]))
