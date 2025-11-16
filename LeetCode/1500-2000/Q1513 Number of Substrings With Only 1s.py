class Solution:
    def numSub(self, s: str) -> int:
        mod = 10 ** 9 + 7
        res = 0
        cur = 0
        for c in s:
            if c == '1':
                cur += 1
            else:
                res += cur * (cur + 1) // 2
                cur = 0
        res += cur * (cur + 1) // 2
        return res % mod


solution = Solution()
print(solution.numSub(s="0110111"))
print(solution.numSub(s="101"))
print(solution.numSub(s="111111"))
