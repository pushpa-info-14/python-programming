class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        s += ' '
        ones = 1 if s[0] == '1' else 0
        segments = []
        count = 1
        prev = s[0]
        for c in s[1:]:
            if c == '1':
                ones += 1
            if c != prev:
                segments.append([prev, count])
                count = 1
            else:
                count += 1
            prev = c
        res = ones
        mx = 0
        for i in range(1, len(segments) - 1):
            l = segments[i - 1]
            r = segments[i + 1]
            if l[0] == '0' and r[0] == '0':
                mx = max(mx, l[1] + r[1])
        return res + mx


s = Solution()
print(s.maxActiveSectionsAfterTrade(s="01"))
print(s.maxActiveSectionsAfterTrade(s="0100"))
print(s.maxActiveSectionsAfterTrade(s="1000100"))
print(s.maxActiveSectionsAfterTrade(s="01010"))
