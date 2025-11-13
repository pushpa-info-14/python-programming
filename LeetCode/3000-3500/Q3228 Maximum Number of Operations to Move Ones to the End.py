class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        res = 0
        ones = 0
        i = 0
        while i < n:
            if s[i] == '1':
                ones += 1
                i += 1
            else:
                while i < len(s) and s[i] == '0':
                    i += 1
                res += ones
        return res


s = Solution()
print(s.maxOperations(s="1001101"))
print(s.maxOperations(s="00111"))
print(s.maxOperations(s="110"))
