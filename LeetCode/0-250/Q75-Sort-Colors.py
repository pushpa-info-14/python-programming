from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0, 0, 0]

        for i in nums:
            buckets[i] += 1
        k = 0
        for i in range(len(buckets)):
            for j in range(buckets[i]):
                if i == 0:
                    nums[k] = 0
                elif i == 1:
                    nums[k] = 1
                else:
                    nums[k] = 2
                k += 1
        print(nums)


s = Solution()
print(s.sortColors([2, 0, 2, 1, 1, 0]))
