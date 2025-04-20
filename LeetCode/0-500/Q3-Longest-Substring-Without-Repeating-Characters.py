class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0
        if n == 1: return 1

        l = 0
        max_length = 0
        seen = {}
        for i in range(n):
            if s[i] in seen and seen[s[i]] >= l:
                l = seen[s[i]] + 1
            else:
                max_length = max(max_length, i - l + 1)
            seen[s[i]] = i
        return max_length


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("au"))
print(s.lengthOfLongestSubstring("aab"))
print(s.lengthOfLongestSubstring("dvdf"))
print(s.lengthOfLongestSubstring("tmmzuxt"))
