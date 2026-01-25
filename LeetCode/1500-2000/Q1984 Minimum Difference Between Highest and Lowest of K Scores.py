from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        res = 10 ** 10
        for i in range(n - k + 1):
            res = min(res, nums[i + k - 1] - nums[i])
        return res


s = Solution()
print(s.minimumDifference(nums=[90], k=1))
print(s.minimumDifference(nums=[9, 4, 1, 7], k=2))
