from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []

        def dfs(i, cur):
            if i == n - 1:
                res.append(cur)
                return
            if cur[-1] == '0':
                dfs(i + 1, cur + '1')
            else:
                dfs(i + 1, cur + '0')
                dfs(i + 1, cur + '1')
            return

        dfs(0, '0')
        dfs(0, '1')
        return res


s = Solution()
print(s.validStrings(3))
print(s.validStrings(1))
