from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        x = nums[0]

        for i in range(1, len(nums)):
            if nums[i] - x > k:
                x = nums[i]
                ans += 1

        return ans


s = Solution()
print(s.partitionArray(nums=[3, 6, 1, 2, 5], k=2))
print(s.partitionArray(nums=[1, 2, 3], k=1))
print(s.partitionArray(nums=[2, 2, 4, 5], k=0))
print(s.partitionArray(nums=[16, 8, 17, 0, 3, 17, 8, 20], k=10))
