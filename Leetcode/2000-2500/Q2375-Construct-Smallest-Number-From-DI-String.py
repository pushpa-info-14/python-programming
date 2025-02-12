class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        digits = "123456789"
        res = [""]

        def dfs(i, num, frequency):
            if res[0] != "":
                return False

            if len(num) > 1:
                if frequency[num[i]] > 1:
                    return False
                if pattern[i - 1] == "I" and num[i - 1] >= num[i]:
                    return False
                if pattern[i - 1] == "D" and num[i - 1] <= num[i]:
                    return False

            if i == n:
                res[0] = num
                return True

            for digit in digits:
                if digit not in frequency:
                    frequency[digit] = 0
                frequency[digit] += 1
                dfs(i + 1, num + digit, frequency)
                frequency[digit] -= 1
                if frequency[digit] == 0:
                    del frequency[digit]

        dfs(-1, "", {})
        return res[0]

    def smallestNumber2(self, pattern: str) -> str:
        stack = []
        result = []
        n = len(pattern)
        for i in range(n + 1):
            stack.append(str(i + 1))
            if i == n or pattern[i] == 'I':
                while stack:
                    result.append(stack.pop())
        return ''.join(result)


s = Solution()
print(s.smallestNumber("IIIDIDDD"))
print(s.smallestNumber2("IIIDIDDD"))
