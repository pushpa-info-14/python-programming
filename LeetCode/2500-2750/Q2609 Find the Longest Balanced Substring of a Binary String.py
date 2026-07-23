class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        r = 0
        while r < n:
            zeros = 0
            while r < n and s[r] == '0':
                r += 1
                zeros += 1
            ones = 0
            while r < n and s[r] == '1':
                r += 1
                ones += 1
            if zeros > 0 or ones > 0:
                res = max(res, min(zeros, ones) * 2)
                r -= 1
            r += 1
        return res

    def findTheLongestBalancedSubstring2(self, s: str) -> int:
        n = len(s)
        res = 0
        zeros = 0
        ones = 0
        for i in range(n):
            if s[i] == '0':
                if i > 0 and s[i - 1] == '1':
                    zeros = 0
                    ones = 0
                zeros += 1
            else:
                ones += 1
            res = max(res, min(zeros, ones) * 2)
        return res


s = Solution()
print(s.findTheLongestBalancedSubstring(s="01000111"))
print(s.findTheLongestBalancedSubstring(s="00111"))
print(s.findTheLongestBalancedSubstring(s="111"))
print(s.findTheLongestBalancedSubstring(s="101"))
print(s.findTheLongestBalancedSubstring2(s="01000111"))
print(s.findTheLongestBalancedSubstring2(s="00111"))
print(s.findTheLongestBalancedSubstring2(s="111"))
print(s.findTheLongestBalancedSubstring2(s="101"))
