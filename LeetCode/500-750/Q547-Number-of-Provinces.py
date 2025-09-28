from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        par = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0

            if rank[p1] < rank[p2]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    union(i, j)

        res= 0
        for i in range(n):
            if par[i] == i:
                res += 1
        return res

    def findCircleNum2(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False for _ in range(n)]
        provinces = 0

        def dfs(node):
            if visited[node]:
                return
            visited[node] = True
            for nei in range(n):
                if isConnected[node][nei] and not visited[nei] :
                    dfs(nei)

        for i in range(n):
            if not visited[i]:
                provinces += 1
                dfs(i)
        return provinces

s = Solution()
print(s.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(s.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
print(s.findCircleNum([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))

print(s.findCircleNum2([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(s.findCircleNum2([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
print(s.findCircleNum2([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
