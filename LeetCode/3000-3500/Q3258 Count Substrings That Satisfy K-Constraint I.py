class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        res = 0
        n = len(s)
        for i in range(n):
            counter = {'0': 0, '1': 0}
            for j in range(i, n):
                counter[s[j]] += 1
                if counter['0'] <= k or counter['1'] <= k:
                    res += 1
        return res

    def countKConstraintSubstrings2(self, s: str, k: int) -> int:
        res = 0
        n = len(s)
        counter = {'0': 0, '1': 0}
        l = 0
        for r in range(n):
            counter[s[r]] += 1
            while counter['0'] > k and counter['1'] > k:
                counter[s[l]] -= 1
                l += 1
            res += (r - l + 1)
        return res


s = Solution()
print(s.countKConstraintSubstrings(s="10101", k=1))
print(s.countKConstraintSubstrings(s="1010101", k=2))
print(s.countKConstraintSubstrings(s="11111", k=1))
print(s.countKConstraintSubstrings2(s="10101", k=1))
print(s.countKConstraintSubstrings2(s="1010101", k=2))
print(s.countKConstraintSubstrings2(s="11111", k=1))
