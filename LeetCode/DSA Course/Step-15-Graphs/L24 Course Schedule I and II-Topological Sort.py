from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        n = numCourses
        in_degree = [0] * n

        for i in range(n):
            for nei in graph[i]:
                in_degree[nei] += 1

        q = deque()
        for i in range(n):
            if in_degree[i] == 0:
                q.append(i)

        count = 0
        while q:
            node = q.popleft()
            count += 1
            for nei in graph[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
        return True if n == count else False

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for v, u in prerequisites:
            graph[u].append(v)

        n = numCourses
        in_degree = [0] * n

        for i in range(n):
            for nei in graph[i]:
                in_degree[nei] += 1

        q = deque()
        for i in range(n):
            if in_degree[i] == 0:
                q.append(i)

        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for nei in graph[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
        return res if n == len(res) else []


s = Solution()
print(s.canFinish(numCourses=2, prerequisites=[[1, 0]]))
print(s.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]))

print(s.findOrder(numCourses=2, prerequisites=[[1, 0]]))
print(s.findOrder(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]))
print(s.findOrder(numCourses=1, prerequisites=[]))
