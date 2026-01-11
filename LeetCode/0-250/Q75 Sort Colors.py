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

    def sortColors2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1

        print(nums)


s = Solution()
print(s.sortColors([2, 0, 2, 1, 1, 0]))
print(s.sortColors2([2, 0, 2, 1, 1, 0]))
