# Minimum Cost Spanning Tree
# Must be connected
import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i:[] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+ 1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prim's
        res= 0
        visit = set()
        q = [[0,0]] # [cost, point]
        while len(visit) < n:
            cost, i =  heapq.heappop(q)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for nei_cost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(q, [nei_cost, nei])
        return res

s=Solution()
print(s.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
print(s.minCostConnectPoints([[3,12],[-2,5],[-4,1]]))
