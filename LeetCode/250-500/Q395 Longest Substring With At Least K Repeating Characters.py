from collections import defaultdict


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        if n == 0 or n < k: return 0
        if k <= 1: return n
        freq = defaultdict(int)

        for c in s:
            freq[c] += 1
        l = 0
        while l < n and freq[s[l]] >= k:
            l += 1
        if l == n: return l

        r1 = self.longestSubstring(s[:l], k)

        while l < n and freq[s[l]] < k:
            l += 1
        r2 = 0 if l == n else self.longestSubstring(s[l:], k)
        return max(r1, r2)


s = Solution()
print(s.longestSubstring("aaabb", 3))
print(s.longestSubstring("ababbc", 2))
print(s.longestSubstring("ababacb", 3))
