class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        for i in range(len(s)):
            if s[i] in seen:
                continue
            if s.count(s[i]) == 1:
                return i
            seen.add(s[i])
        return -1


s = Solution()
print(s.firstUniqChar("leetcode"))
