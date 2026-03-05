class Solution:
    def longestBalanced(self, s: str) -> int:
        p = [[0, 0, 0]]
        res = 0
        for c in s:
            p.append(p[-1][:])
            p[-1]["abc".index(c)] += 1

        first = dict()
        for i, (a, b, c) in enumerate(p):
            keys = [
                ("abc", a - b, a - c),
                ("ab", a - b, c),
                ("bc", b - c, a),
                ("ac", c - a, b),
                ("a", b, c),
                ("b", a, c),
                ("c", a, b)
            ]
            for key in keys:
                res = max(res, i - first.get(key, i))
                first.setdefault(key, i)
        return res

    def longestBalanced2(self, s: str) -> int:
        n = len(s)
        res = 0

        # One char
        def one():
            mx = 0
            i = 0
            while i < n:
                j = i
                while j < n and s[i] == s[j]:
                    j += 1
                mx = max(mx, j - i)
                i = j
            return mx

        # Two chars
        def two(x, y, exclude):
            mx = 0
            i = 0
            while i < n:
                if s[i] == exclude:
                    i += 1
                    continue
                last = {0: i - 1}
                cx, cy = 0, 0
                while i < n and s[i] != exclude:
                    if s[i] == x:
                        cx += 1
                    else:
                        cy += 1
                    key = cx - cy
                    if key in last:
                        mx = max(mx, i - last[key])
                    else:
                        last[key] = i
                    i += 1
            return mx

        # Three chars
        def three():
            mx = 0
            last = {(0, 0): -1}
            ca, cb, cc = 0, 0, 0
            for i in range(n):
                if s[i] == 'a':
                    ca += 1
                elif s[i] == 'b':
                    cb += 1
                else:
                    cc += 1
                key = (ca - cb, cb - cc)
                if key in last:
                    mx = max(mx, i - last[key])
                else:
                    last[key] = i
            return mx

        res = max(res, one())
        res = max(res, two("a", "b", "c"))
        res = max(res, two("a", "c", "b"))
        res = max(res, two("b", "c", "a"))
        res = max(res, three())

        return res


s = Solution()
print(s.longestBalanced(s="abbac"))
print(s.longestBalanced(s="aabcc"))
print(s.longestBalanced(s="aba"))
print("----------")
print(s.longestBalanced2(s="abbac"))
print(s.longestBalanced2(s="aabcc"))
print(s.longestBalanced2(s="aba"))
