class Solution:
    def modifyString(self, s: str) -> str:
        s = ' ' + s + ' '
        chars = list(s)
        n = len(chars)
        t = ord('a')
        cur = 0
        for i in range(1, n - 1):
            if chars[i] == '?':
                while chr(cur + t) == chars[i - 1] or chr(cur + t) == chars[i + 1]:
                    cur += 1
                    cur %= 26
                chars[i] = chr(cur + t)
        return ''.join(chars[1:-1])


s = Solution()
print(s.modifyString(s="?zs"))
print(s.modifyString(s="ubv?w"))
