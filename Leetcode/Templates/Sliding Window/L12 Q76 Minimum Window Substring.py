import math
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mapping = defaultdict(int)
        n = len(s)
        t_len = len(t)
        count = 0
        min_length = math.inf
        start_index = -1
        end_index = -1
        l, r = 0, 0

        for c in t:
            mapping[c] += 1

        while r < n:
            if mapping[s[r]] > 0:
                count += 1
            mapping[s[r]] -= 1

            while count == t_len:
                if r - l + 1 < min_length:
                    start_index = l
                    end_index = r
                    min_length = r - l + 1

                mapping[s[l]] += 1
                if mapping[s[l]] > 0:
                    count -= 1
                l += 1
            r += 1

        return s[start_index:end_index + 1]


s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
print(s.minWindow("a", "a"))
print(s.minWindow("a", "aa"))
print(s.minWindow("aa", "aa"))
print(s.minWindow("abc", "aabc"))
print(s.minWindow("cabwefgewcwaefgcf", "cae"))  # cwae
