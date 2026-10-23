from typing import List


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        nums_sorted = sorted(nums)
        res = -1
        for i in range(n):
            if nums_sorted[i] != nums[i]:
                if res == -1:
                    res = nums[i]
                else:
                    res &= nums[i]
        return res if res != -1 else 0


s = Solution()
print(s.sortPermutation(nums=[0, 3, 2, 1]))
print(s.sortPermutation(nums=[0, 1, 3, 2]))
print(s.sortPermutation(nums=[3, 2, 1, 0]))
