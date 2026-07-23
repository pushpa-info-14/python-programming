class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        odds = []
        evens = []
        str_evens = ''
        n = len(s)
        for i in range(n):
            if i & 1:
                odds.append(int(s[i]))
            else:
                evens.append(int(s[i]))
                str_evens += s[i]

        all_odds = []
        for i in range(10):
            all_odds.append(''.join(map(str, ((d + i * a) % 10 for d in odds))))

        all_evens = [str_evens]
        if b & 1:  # If b is odd, even indices will get a chance to increment by a
            for i in range(10):
                all_evens.append(''.join(map(str, ((d + i * a) % 10 for d in evens))))
        res = s
        for even in all_evens:
            for odd in all_odds:
                cur = ''.join(e + o for e, o in zip(even, odd))
                for i in range(n):
                    cur = cur[b:] + cur[:b]
                    res = min(res, cur)
        return res


s = Solution()
print(s.findLexSmallestString(s="5525", a=9, b=2))  # 2050
print(s.findLexSmallestString(s="74", a=5, b=1))  # 24
print(s.findLexSmallestString(s="0011", a=4, b=2))  # 0011
print(s.findLexSmallestString(s="43987654", a=7, b=3))  # 00553311
