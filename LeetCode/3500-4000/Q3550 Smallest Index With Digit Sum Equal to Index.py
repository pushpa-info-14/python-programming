from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            cur = 0
            num = nums[i]
            while num:
                cur += num % 10
                num //= 10
            if cur == i:
                return i
        return -1


s = Solution()
print(s.smallestIndex(nums=[1, 3, 2]))
print(s.smallestIndex(nums=[1, 10, 11]))
print(s.smallestIndex(nums=[1, 2, 3]))
