import heapq
from typing import List


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        q = len(queries)
        queries.sort()
        candidates = []  # max heap
        chosen = []  # min heap
        ans = 0
        j = 0
        for i in range(n):
            while j < q and queries[j][0] == i:
                heapq.heappush(candidates, -queries[j][1])
                j += 1

            nums[i] -= len(chosen)

            while nums[i] > 0 and len(candidates) > 0 and -candidates[0] >= i:
                ans += 1
                heapq.heappush(chosen, -heapq.heappop(candidates))
                nums[i] -= 1

            if nums[i] > 0:
                return -1
            while len(chosen) > 0 and chosen[0] == i:
                heapq.heappop(chosen)

        return q - ans


s = Solution()
print(s.maxRemoval(nums=[2, 0, 2], queries=[[0, 2], [0, 2], [1, 1]]))  # 1
print(s.maxRemoval(nums=[1, 1, 1, 1], queries=[[1, 3], [0, 2], [1, 3], [1, 2]]))  # 2
print(s.maxRemoval(nums=[1, 2, 3, 4], queries=[[0, 3]]))  # -1
print(s.maxRemoval(nums=[0, 3], queries=[[0, 1], [0, 0], [0, 1], [0, 1], [0, 0]]))  # 2
print(s.maxRemoval(nums=[1, 0], queries=[[1, 1], [1, 1], [0, 1], [0, 1], [0, 0], [1, 1]]))  # 5
