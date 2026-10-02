class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def dfs(c, a, b):
            if a > n or b > n or a < b:
                return
            if len(c) == 2 * n:
                res.append(c)
            dfs(c + '(', a + 1, b)
            dfs(c + ')', a, b + 1)

        dfs('(', 1, 0)
        return res


s = Solution()
print(s.generateParenthesis(3))
print(s.generateParenthesis(1))
