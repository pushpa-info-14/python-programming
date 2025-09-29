from collections import defaultdict
from math import inf
from typing import List


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        subtree = [0] * n
        adj = defaultdict(list)
        time = 0
        start = [0] * n
        end = [0] * n
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node, par):
            nonlocal time
            val = nums[node]
            time += 1
            start[node] = time

            for nei in adj[node]:
                if nei != par:
                    val ^= dfs(nei, node)
            time += 1
            end[node] = time
            subtree[node] = val
            return val

        def is_ancestor(u, v):
            return start[u] <= start[v] and end[u] >= end[v]

        dfs(0, -1)
        ans = inf
        for i in range(1, n):
            for j in range(i + 1, n):
                sub1 = subtree[i]
                sub2 = subtree[j]

                if is_ancestor(i, j):
                    sub1 ^= sub2
                elif is_ancestor(j, i):
                    sub2 ^= sub1
                third = subtree[0] ^ sub1 ^ sub2

                ans = min(ans, max(sub1, sub2, third) - min(sub1, sub2, third))
        return ans


s = Solution()
print(s.minimumScore(nums=[1, 5, 5, 4, 11], edges=[[0, 1], [1, 2], [1, 3], [3, 4]]))
print(s.minimumScore(nums=[5, 5, 2, 4, 4, 2], edges=[[0, 1], [1, 2], [5, 2], [4, 3], [1, 3]]))
