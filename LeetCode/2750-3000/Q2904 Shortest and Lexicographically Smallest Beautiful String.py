class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        l = 0
        ones = 0
        res = ''
        for r in range(n):
            ones += int(s[r])
            while ones > k and l < r:
                ones -= int(s[l])
                l += 1
            while ones == k and s[l] == '0':
                l += 1
            if ones == k:
                cur = s[l: r + 1]
                if res == '' or len(res) > len(cur):
                    res = cur
                elif len(res) == len(cur):
                    res = min(res, s[l:r + 1])
        return res


s = Solution()
print(s.shortestBeautifulSubstring(s="100011001", k=3))
print(s.shortestBeautifulSubstring(s="1011", k=2))
print(s.shortestBeautifulSubstring(s="000", k=1))
print(s.shortestBeautifulSubstring(s="1100100101011001001", k=7))
