class Solution:
    @staticmethod
    def runLengthEncoding(s: str) -> str:
        n = len(s)
        res = ""
        i = 0
        while i < n:
            count = 1
            while i + 1 < n and s[i] == s[i + 1]:
                count += 1
                i += 1
            res += f"{count}{s[i]}"
            i += 1
        return res

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.runLengthEncoding(self.countAndSay(n - 1))

    def countAndSay2(self, n: int) -> str:
        res = "1"
        for i in range(2, n + 1):
            res = self.runLengthEncoding(res)
        return res


solution = Solution()
print(solution.countAndSay(4))
print(solution.countAndSay(1))
print(solution.countAndSay2(4))
print(solution.countAndSay2(1))
