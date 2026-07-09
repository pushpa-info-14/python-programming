from typing import List


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        parent = list(range(n))
        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                parent[i] = parent[i - 1]
        return [parent[a] == parent[b] for a, b in queries]


s = Solution()
print(s.pathExistenceQueries(n=2, nums=[1, 3], maxDiff=1, queries=[[0, 0], [0, 1]]))
print(s.pathExistenceQueries(n=4, nums=[2, 5, 6, 8], maxDiff=2, queries=[[0, 1], [0, 2], [1, 3], [2, 3]]))
