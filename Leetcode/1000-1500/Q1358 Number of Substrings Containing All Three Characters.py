from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        positions = {"a": -1, "b": -1, "c": -1}
        r = 0
        res = 0
        while r < n:
            positions[s[r]] = r
            if positions["a"] >= 0 and positions["b"] >= 0 and positions["c"] >= 0:
                min_idx = min(positions["a"], positions["b"], positions["c"])
                res += min_idx + 1

            r += 1
        return res

    def numberOfSubstrings2(self, s: str) -> int:
        n = len(s)
        chars = defaultdict(int)
        l = 0
        r = 0
        res = 0
        while r < n:
            chars[s[r]] += 1
            while len(chars) == 3:
                res += n - r
                chars[s[l]] -= 1
                if chars[s[l]] == 0:
                    del chars[s[l]]
                l += 1
            r += 1
        return res


s = Solution()
print(s.numberOfSubstrings("abcabc"))
print(s.numberOfSubstrings("aaacb"))
print(s.numberOfSubstrings("abc"))
print(s.numberOfSubstrings("acbbcac"))
print(s.numberOfSubstrings2("abcabc"))
print(s.numberOfSubstrings2("aaacb"))
print(s.numberOfSubstrings2("abc"))
print(s.numberOfSubstrings2("acbbcac"))
