from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        n = len(s)
        l, r = 0, 0
        max_freq = 0
        res = 0
        while r < n:
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])

            while r - l + 1 - max_freq > k:
                freq[s[l]] -= 1
                max_freq = 0
                for key in freq.keys():
                    max_freq = max(max_freq, freq[key])
                l += 1

            if r - l + 1 - max_freq <= k:
                res = max(res, r - l + 1)
            r += 1
        return res

    def characterReplacement2(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        n = len(s)
        l, r = 0, 0
        max_freq = 0
        res = 0
        while r < n:
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])

            if r - l + 1 - max_freq > k:
                freq[s[l]] -= 1
                l += 1

            if r - l + 1 - max_freq <= k:
                res = max(res, r - l + 1)
            r += 1
        return res


s = Solution()
print(s.characterReplacement("ABAB", 2))
print(s.characterReplacement("AABABBA", 1))

print(s.characterReplacement2("ABAB", 2))
print(s.characterReplacement2("AABABBA", 1))
