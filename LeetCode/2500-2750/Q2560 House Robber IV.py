from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def is_valid(capability):
            i = 0
            count = 0
            while i < len(nums):
                if nums[i] <= capability:
                    i += 2
                    count += 1
                else:
                    i += 1
                if count == k:
                    break
            return count == k

        res = 0
        l, r = min(nums), max(nums)
        while l <= r:
            mid = (l + r) // 2
            if is_valid(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res


s = Solution()
print(s.minCapability(nums=[2, 3, 5, 9], k=2))
print(s.minCapability(nums=[2, 7, 9, 3, 1], k=2))
