from collections import defaultdict
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for prq, crs in prerequisites:
            adj[crs].append(prq)

        prerequisite_map = {}  # map crs -> hashset of indirect prerequisites
        def dfs(crs):
            if crs not in prerequisite_map:
                prerequisite_map[crs] = set()
                for prq in adj[crs]:
                    prerequisite_map[crs] |= dfs(prq) # union
                prerequisite_map[crs].add(crs)
            return prerequisite_map[crs]


        for crs in range(numCourses):
            dfs(crs)

        res = []
        for u, v in queries:
            res.append(u in prerequisite_map[v])
        return res

s = Solution()
print(s.checkIfPrerequisite(2, [[1,0]], [[0,1],[1,0]]))