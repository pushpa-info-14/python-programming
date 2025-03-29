from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n - k + 1):
            maxi = nums[i]
            for j in range(i + 1, i + k):
                maxi = max(maxi, nums[j])
            res.append(maxi)
        return res

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        dq = deque()
        for i in range(n):
            if dq and dq[0] <= i - k:
                dq.popleft()
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res


s = Solution()
print(s.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
print(s.maxSlidingWindow(nums=[1], k=1))
print(s.maxSlidingWindow2(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
print(s.maxSlidingWindow2(nums=[1], k=1))
