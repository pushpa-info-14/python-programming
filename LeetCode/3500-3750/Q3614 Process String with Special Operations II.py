class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0
        for c in s:
            if c == '*':
                if length > 0:
                    length -= 1
            elif c == '#':
                length *= 2
            elif c == '%':
                continue
            else:
                length += 1
        if k >= length:
            return '.'
        for c in reversed(s):
            if c == '*':
                length += 1
            elif c == '#':
                length //= 2
                if k >= length:
                    k -= length
            elif c == '%':
                k = length - 1 - k
            else:
                if k == length - 1:
                    return c
                length -= 1


s = Solution()
print(s.processStr(s="a#b%*", k=1))
print(s.processStr(s="cd%#*#", k=3))
print(s.processStr(s="z*#", k=0))
