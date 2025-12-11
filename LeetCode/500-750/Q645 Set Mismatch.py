from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = 0
        duplicate = -1
        for num in nums:
            num = abs(num)
            total += num
            if nums[num - 1] > 0:
                nums[num - 1] = -nums[num - 1]
            else:
                duplicate = num
        missing = (n * (n + 1) // 2) - (total - duplicate)
        return [duplicate, missing]


s = Solution()
print(s.findErrorNums(nums=[1, 2, 2, 4]))
print(s.findErrorNums(nums=[1, 1]))
