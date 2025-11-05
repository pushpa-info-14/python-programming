class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        carry = 0
        while n:
            teams = carry + n
            n = teams // 2
            res += n
            carry = teams % 2
        return res

    def numberOfMatches2(self, n: int) -> int:
        return n - 1


s = Solution()
print(s.numberOfMatches(7))  # 6
print(s.numberOfMatches(14))  # 13
print(s.numberOfMatches(3))  # 2
print(s.numberOfMatches2(7))  # 6
print(s.numberOfMatches2(14))  # 13
print(s.numberOfMatches2(3))  # 2
