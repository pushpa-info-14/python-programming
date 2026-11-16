from collections import deque
from typing import List


class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        r = n - 1
        dq = deque()
        op = 0
        res = 0
        for l in range(n - 1, -1, -1):
            new_size = 1
            while dq and nums[l] >= dq[-1][0]:
                height, size = dq.pop()
                op += (nums[l] - height) * size
                new_size += size
            dq.append([nums[l], new_size])
            while op > k:
                op -= dq[0][0] - nums[r]
                dq[0][1] -= 1
                if dq[0][1] == 0:
                    dq.popleft()
                r -= 1
            res += r - l + 1
        return res


s = Solution()
print(s.countNonDecreasingSubarrays(nums=[6, 3, 1, 2, 4, 4], k=7))
print(s.countNonDecreasingSubarrays(nums=[6, 3, 1, 3, 6], k=4))
