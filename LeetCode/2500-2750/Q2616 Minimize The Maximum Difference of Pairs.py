from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)

        def is_possible(max_value):
            valid_pairs = 0
            i = 1
            while i < n:
                if abs(nums[i - 1] - nums[i]) <= max_value:
                    valid_pairs += 1
                    i += 2
                else:
                    i += 1
                if valid_pairs == p:
                    return True
            return False

        res = 0
        low, high = 0, nums[n - 1]
        while low <= high:
            mid = low + (high - low) // 2
            if is_possible(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res


# LeetCode
# Q278: First Bad Version
# Q2064: Minimized Maximum of Products Distributed to Any Store
s = Solution()
print(s.minimizeMax(nums=[10, 1, 2, 7, 1, 3], p=2))
print(s.minimizeMax(nums=[4, 2, 1, 2], p=1))
print(s.minimizeMax(nums=[1, 1, 0, 3], p=2))
