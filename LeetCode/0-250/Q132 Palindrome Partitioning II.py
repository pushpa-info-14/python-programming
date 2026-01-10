class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        memo = {}

        def dfs(i):
            if i == n:
                return 0
            if i in memo:
                return memo[i]
            res = n
            temp = ""
            for j in range(i, n):
                temp += s[j]
                if temp == temp[::-1]:
                    res = min(res, 1 + dfs(j + 1))
            memo[i] = res
            return res

        return dfs(0) - 1


s = Solution()
print(s.minCut(s="aab"))
print(s.minCut(s="a"))
print(s.minCut(s="ab"))
print(s.minCut(s="bababcbadcede"))
