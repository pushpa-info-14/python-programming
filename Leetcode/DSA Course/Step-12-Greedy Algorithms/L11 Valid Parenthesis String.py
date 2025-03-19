class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        memo = [[-1] * n for _ in range(n)]

        def dfs(index, cnt):
            if cnt < 0: return False
            if index == n:
                return cnt == 0

            if memo[index][cnt] != -1:
                return memo[index][cnt]

            res = False
            if s[index] == "(":
                res = dfs(index + 1, cnt + 1)
            if s[index] == ")":
                res = dfs(index + 1, cnt - 1)
            if s[index] == "*":
                res = dfs(index + 1, cnt + 1) or dfs(index + 1, cnt - 1) or dfs(index + 1, cnt)
            memo[index][cnt] = res
            return res

        return dfs(0, 0)

    def checkValidString2(self, s: str) -> bool:
        n = len(s)
        dp = {(n, 0): True}  # key=(i, leftCount) -> isValid

        def dfs(i, cnt):
            if i == n or cnt < 0:
                return cnt == 0
            if (i, cnt) in dp:
                return dp[(i, cnt)]

            if s[i] == "(":
                dp[(i, cnt)] = dfs(i + 1, cnt + 1)
            elif s[i] == ")":
                dp[(i, cnt)] = dfs(i + 1, cnt - 1)
            else:
                dp[(i, cnt)] = dfs(i + 1, cnt + 1) or dfs(i + 1, cnt - 1) or dfs(i + 1, cnt)
            return dp[(i, cnt)]

        return dfs(0, 0)

    def checkValidString3(self, s: str) -> bool:
        minimum = 0
        maximum = 0
        for c in s:
            if c == "(":
                minimum += 1
                maximum += 1
            elif c == ")":
                minimum -= 1
                maximum -= 1
            else:
                minimum -= 1
                maximum += 1

            if maximum < 0: return False  # )(((
            if minimum < 0: minimum = 0

        return minimum == 0


s = Solution()
print(s.checkValidString("()"))
print(s.checkValidString("(*)"))
print(s.checkValidString("(*))"))
print(s.checkValidString(
    "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
print(s.checkValidString2(
    "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
print(s.checkValidString3(
    "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
