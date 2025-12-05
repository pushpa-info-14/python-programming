from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        res = 0
        cur = 0
        for num in nums[:-1]:
            cur += num
            total -= num
            if (cur - total) % 2 == 0:
                res += 1
        return res

    def countPartitions2(self, nums: List[int]) -> int:
        return len(nums) - 1 if sum(nums) % 2 == 0 else 0


s = Solution()
print(s.countPartitions(nums=[10, 10, 3, 7, 6]))
print(s.countPartitions(nums=[1, 2, 2]))
print(s.countPartitions(nums=[2, 4, 6, 8]))
print(s.countPartitions2(nums=[10, 10, 3, 7, 6]))
print(s.countPartitions2(nums=[1, 2, 2]))
print(s.countPartitions2(nums=[2, 4, 6, 8]))
