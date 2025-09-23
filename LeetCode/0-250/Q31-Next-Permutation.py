from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # Find the peak of last ascending order
        last_inc = -1
        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                last_inc = i + 1

        # Array is descending order
        if last_inc == -1:
            for i in range(n // 2):
                nums[i], nums[n - 1 - i] = nums[n - 1 - i], nums[i]
            return

        # Find element in the range
        # nums[last_inc - 1] to nums[last_inc] to the right
        index = last_inc
        for i in range(last_inc, n):
            if nums[last_inc - 1] < nums[i] < nums[index]:
                index = i

        nums[last_inc - 1], nums[index] = nums[index], nums[last_inc - 1]

        for i in range(last_inc, n):
            for j in range(i, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        print(nums)


s = Solution()
print(s.nextPermutation([1, 2, 3]))
print(s.nextPermutation([3, 2, 1]))
print(s.nextPermutation([1, 1, 5]))
print(s.nextPermutation([1, 3, 2]))
