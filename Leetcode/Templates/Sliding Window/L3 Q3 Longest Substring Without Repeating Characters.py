class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = {}
        l = 0
        r = 0
        max_len = 0

        while r < n:
            if s[r] in seen:
                if seen[s[r]] >= l:
                    l = seen[s[r]] + 1
            max_len = max(max_len, r - l + 1)
            seen[s[r]] = r
            r += 1
        return max_len


s = Solution()
print(s.lengthOfLongestSubstring("cadbzabcd"))
