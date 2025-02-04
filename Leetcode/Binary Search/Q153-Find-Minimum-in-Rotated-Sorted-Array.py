import math
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        res = math.inf
        while l <= r:
            mid = (l + r) // 2
            res = min(res, nums[mid])

            # Left sorted portion
            if nums[l] <= nums[mid]:
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                r = mid - 1
        return res


s = Solution()
print(s.findMin([3, 4, 5, 0, 1, 2]))
