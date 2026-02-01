from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        res = 10 ** 10
        for i in range(1, n):
            for j in range(i + 1, n):
                res = min(res, nums[0] + nums[i] + nums[j])
        return res

    def minimumCost2(self, nums: List[int]) -> int:
        first = nums[0]
        rest = nums[1:]
        rest.sort()
        return first + rest[0] + rest[1]


s = Solution()
print(s.minimumCost(nums=[1, 2, 3, 12]))
print(s.minimumCost(nums=[5, 4, 3]))
print(s.minimumCost(nums=[10, 3, 1, 1]))
print("---------------------")
print(s.minimumCost2(nums=[1, 2, 3, 12]))
print(s.minimumCost2(nums=[5, 4, 3]))
print(s.minimumCost2(nums=[10, 3, 1, 1]))
