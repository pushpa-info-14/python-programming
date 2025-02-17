class Solution:
    def longest_substring(self, s: str, k: int) -> int:
        n = len(s)
        l, r = 0, 0
        max_len = 0
        freq = {}
        while r < n:
            if s[r] not in freq:
                freq[s[r]] = 0
            freq[s[r]] += 1

            # while len(freq) > k:
            if len(freq) > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            if len(freq) <= k:
                max_len = max(max_len, r - l + 1)
            r += 1
        return max_len


s = Solution()
print(s.longest_substring("aaabbccd", 2))
print(s.longest_substring("aaabbccd", 3))
