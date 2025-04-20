from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        min_q = deque()  # mono increasing
        max_q = deque()  # mono decreasing
        l = 0
        res = 0

        for r in range(n):
            while min_q and nums[r] < min_q[-1]:
                min_q.pop()
            while max_q and nums[r] > max_q[-1]:
                max_q.pop()
            min_q.append(nums[r])
            max_q.append(nums[r])

            while max_q[0] - min_q[0] > limit:
                if nums[l] == max_q[0]:
                    max_q.popleft()
                if nums[l] == min_q[0]:
                    min_q.popleft()
                l += 1
            res = max(res, r - l + 1)
        return res


s = Solution()
print(s.longestSubarray([8, 2, 4, 7], 4))
print(s.longestSubarray([10, 1, 2, 4, 7, 2], 5))
print(s.longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0))
print(s.longestSubarray([1, 5, 6, 7, 8, 10, 6, 5, 6], 4))  # 5
