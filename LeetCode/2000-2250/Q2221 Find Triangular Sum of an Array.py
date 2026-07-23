from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            cur = []
            for i in range(len(nums) - 1):
                cur.append((nums[i] + nums[i + 1]) % 10)
            nums = cur.copy()
        return nums[0]

    def triangularSum2(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n - 1, 0, -1):
            for j in range(i):
                nums[j] = (nums[j] + nums[j + 1]) % 10
        return nums[0]


s = Solution()
print(s.triangularSum(nums=[1, 2, 3, 4, 5]))
print(s.triangularSum(nums=[5]))
print(s.triangularSum2(nums=[1, 2, 3, 4, 5]))
print(s.triangularSum2(nums=[5]))
