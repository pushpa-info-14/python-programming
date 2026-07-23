from typing import List


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if i % 10 == nums[i]:
                return i
        return -1

s = Solution()
print(s.smallestEqual(nums = [0,1,2]))
print(s.smallestEqual(nums = [4,3,2,1]))
print(s.smallestEqual(nums = [1,2,3,4,5,6,7,8,9,0]))

