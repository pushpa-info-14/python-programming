class Solution:
    def minOperations(self, s: str) -> int:
        res1 = 0
        res2 = 0
        cur = "0"
        for c in s:
            if c == cur:
                res1 += 1
            else:
                res2 += 1
            cur = "1" if cur == "0" else "0"
        return min(res1, res2)


s = Solution()
print(s.minOperations(s="0100"))
print(s.minOperations(s="10"))
print(s.minOperations(s="1111"))
