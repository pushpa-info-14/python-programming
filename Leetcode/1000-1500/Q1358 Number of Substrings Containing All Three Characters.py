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


s = Solution()
print(s.numberOfSubstrings("abcabc"))
print(s.numberOfSubstrings("aaacb"))
print(s.numberOfSubstrings("abc"))
print(s.numberOfSubstrings("acbbcac"))
