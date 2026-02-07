class Solution:
    def minimumDeletions(self, s: str) -> int:
        a = s.count("a")
        b = 0
        res = a
        for c in s:
            a -= c == "a"
            b += c == "b"
            res = min(res, a + b)
        return res


s = Solution()
print(s.minimumDeletions(s="aababbab"))
print(s.minimumDeletions(s="bbaaaaabb"))
print(s.minimumDeletions(s="aaaaabb"))
print(s.minimumDeletions(s="a"))
print(s.minimumDeletions(s="b"))
print(s.minimumDeletions(
    s="bbbbbbbaabbbbbaaabbbabbbbaabbbbbbaabbaaabaabbbaaaabaaababbbabbabbaaaabbbabbbbbaabbababbbaaaaaababaaababaabbabbbaaaabbbbbabbabaaaabbbaba"))
