from collections import deque
from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        indices = set()
        for i in range(n):
            if nums[i] == key:
                start = max(0, i - k)
                end = min(n - 1, i + k)
                for j in range(start, end + 1):
                    indices.add(j)
        return sorted(list(indices))

    def findKDistantIndices2(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        indices = deque()
        for i in range(n):
            if nums[i] == key:
                indices.append(i - k)

        r = -1
        res = []
        for i in range(n):
            while indices and indices[0] <= i:
                r = max(r, indices[0] + k + k)
                indices.popleft()
            if i <= r:
                res.append(i)
        return res


s = Solution()
print(s.findKDistantIndices(nums=[3, 4, 9, 1, 3, 9, 5], key=9, k=1))
print(s.findKDistantIndices(nums=[2, 2, 2, 2, 2], key=2, k=2))
print(s.findKDistantIndices2(nums=[3, 4, 9, 1, 3, 9, 5], key=9, k=1))
print(s.findKDistantIndices2(nums=[2, 2, 2, 2, 2], key=2, k=2))
