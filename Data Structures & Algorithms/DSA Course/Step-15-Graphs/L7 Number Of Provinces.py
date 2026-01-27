from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        res = 0

        def dfs(node):
            visited.add(node)
            for nei in range(n):
                if isConnected[node][nei] and nei not in visited:
                    dfs(nei)

        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res


# LeetCode 547
s = Solution()
print(s.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(s.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))

# SC O(N) + O(N)
# TC O(N) + O(V+2E)
